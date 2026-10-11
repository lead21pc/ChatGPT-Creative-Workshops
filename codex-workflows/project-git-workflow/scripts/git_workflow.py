"""Bind one chat to a checkout and guard scoped local commits."""
import argparse
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time


def git(root, *args):
    result = subprocess.run(
        ['git', '-c', f'safe.directory={root.as_posix()}', '-C', str(root), *args],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise ValueError(result.stderr.decode('utf-8', 'replace').strip())
    return result.stdout


def text(root, *args):
    return git(root, *args).decode('utf-8', 'surrogateescape').strip()


def staged(root):
    return git(root, 'diff', '--cached', '--no-renames', '--name-only', '-z').decode(
        'utf-8', 'surrogateescape').split('\0')[:-1]


def state_path(root, key):
    common = Path(text(root, 'rev-parse', '--path-format=absolute', '--git-common-dir'))
    return common / 'codex-chat-bindings' / (hashlib.sha256(key.encode()).hexdigest() + '.json')


def save(path, state):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(state, ensure_ascii=True, indent=2), encoding='utf-8')
    os.replace(temporary, path)


@contextmanager
def registry_lock(root, key):
    directory = state_path(root, key).parent
    directory.mkdir(parents=True, exist_ok=True)
    lock = directory / '.lock'
    try:
        descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        raise ValueError('Binding registry busy; retry after the other operation finishes')
    try:
        os.close(descriptor)
        yield
    finally:
        lock.unlink()


def exclusive_owner(root, path, branch):
    for other in path.parent.glob('*.json'):
        if other == path:
            continue
        owner = json.loads(other.read_text(encoding='utf-8'))
        if Path(owner['checkout']).resolve() == root or owner['branch'] == branch:
            raise ValueError('Checkout or branch already belongs to another chat; '
                             'use prepare with a separate worktree and branch')


def prepare(args, root, path, state):
    if Path(text(root, 'rev-parse', '--show-toplevel')).resolve() != root:
        raise ValueError('Expected repository-root checkout')
    project = Path(args.project).absolute()
    if project.resolve() != project or not project.is_dir() or not project.is_relative_to(root):
        raise ValueError('Project scope missing or redirected')
    relative = project.relative_to(root)
    if state:
        bound = Path(state['checkout']).resolve()
        if Path(state['project']) != bound / relative:
            raise ValueError('Existing chat binding cannot be reassigned')
        validate(bound, state)
        exclusive_owner(bound, path, state['branch'])
        print(json.dumps(state, ensure_ascii=True))
        return
    if not all((args.worktree, args.branch, args.ref)):
        raise ValueError('First prepare requires --worktree, --branch and --ref')
    target = Path(args.worktree).absolute()
    if target.resolve() != target or target.exists() or target.is_relative_to(root):
        raise ValueError('New worktree must be an unused path outside the source checkout')
    exclusive_owner(target, path, args.branch)
    git(root, 'check-ref-format', '--branch', args.branch)
    if git(root, 'branch', '--list', args.branch):
        raise ValueError('Branch already exists; inspect and bind its checkout explicitly')
    revision = text(root, 'rev-parse', '--verify', '--end-of-options', args.ref + '^{commit}')
    if relative.parts and text(root, 'cat-file', '-t', f'{revision}:{relative.as_posix()}') != 'tree':
        raise ValueError('Project scope is not a directory at the selected ref')
    git(root, 'worktree', 'add', '-b', args.branch, str(target), revision)
    candidate = dict(checkout=str(target), project=str(target / relative), branch=args.branch,
                     head=revision, staged_baseline=staged(target))
    # On a later failure preserve the new checkout/branch for inspection; never delete work.
    validate(target, candidate)
    save(path, candidate)
    print(json.dumps(candidate, ensure_ascii=True))


def validate(root, state, head=True):
    if root != Path(state['checkout']).resolve():
        raise ValueError('Checkout differs from chat binding')
    if Path(text(root, 'rev-parse', '--show-toplevel')).resolve() != root:
        raise ValueError('Expected repository-root checkout')
    if text(root, 'symbolic-ref', '--short', 'HEAD') != state['branch']:
        raise ValueError('Branch differs from chat binding')
    if head and text(root, 'rev-parse', 'HEAD') != state['head']:
        raise ValueError('HEAD changed outside workflow; inspect before refresh')
    project = Path(state['project'])
    if not project.is_dir() or project.resolve() != project or not project.is_relative_to(root):
        raise ValueError('Project scope missing or redirected')


def run(args):
    root = Path(args.checkout).resolve()
    if args.command == 'check':
        return run_locked(args, root)
    with registry_lock(root, args.chat_key):
        return run_locked(args, root)


def run_locked(args, root):
    path = state_path(root, args.chat_key)
    state = json.loads(path.read_text(encoding='utf-8')) if path.exists() else None
    if args.command == 'prepare':
        return prepare(args, root, path, state)
    if args.command == 'bind':
        project = Path(args.project).absolute()
        candidate = dict(checkout=str(root), project=str(project), branch=args.branch,
                         head=text(root, 'rev-parse', 'HEAD'), staged_baseline=staged(root))
        validate(root, candidate)
        if state:
            if any(state[key] != candidate[key] for key in ('checkout', 'project', 'branch')):
                raise ValueError('Existing chat binding cannot be reassigned')
            validate(root, state, head=not args.refresh_head)
            exclusive_owner(root, path, state['branch'])
            if not args.refresh_head:
                print('PASS: existing binding reused')
                return
        exclusive_owner(root, path, args.branch)
        save(path, candidate)
        print('PASS: binding saved; no branch created')
        return
    if state is None:
        raise ValueError('No chat binding; read-only check did not create one')
    validate(root, state)
    if args.command == 'release':
        if git(root, 'status', '--porcelain', '--untracked-files=all'):
            raise ValueError('Release requires a clean checkout, including the index and untracked files')
        archive = path.parent / 'released'
        archive.mkdir(exist_ok=True)
        os.replace(path, archive / f'{path.stem}-{time.time_ns()}.json')
        print('RELEASED: binding archived; checkout, branch and commits preserved')
        return
    exclusive_owner(root, path, state['branch'])
    if args.command == 'check':
        print('PASS: checkout, scope, branch and HEAD match')
        return
    if git(root, 'ls-files', '-u'):
        raise ValueError('Unresolved index conflicts')
    files = []
    project = Path(state['project'])
    for name in args.file:
        relative = Path(name)
        target = root / relative
        if relative.is_absolute() or '..' in relative.parts or not relative.parts:
            raise ValueError(f'Expected literal repository-relative file: {name}')
        if not target.resolve().is_relative_to(project):
            raise ValueError(f'File outside project scope: {name}')
        for component in [target, *target.parents]:
            if component == root:
                break
            if component.is_symlink() or component.resolve() != component:
                raise ValueError(f'Redirected file path: {name}')
        if target.is_dir():
            raise ValueError(f'Explicit files required, not directories: {name}')
        files.append(relative.as_posix())
    normalize = (lambda name: name.casefold()) if os.name == 'nt' else (lambda name: name)
    if {normalize(name) for name in files} & {normalize(name) for name in state['staged_baseline']}:
        raise ValueError('Commit overlaps pre-existing staged paths')
    if {normalize(name) for name in files} - {normalize(name) for name in staged(root)}:
        raise ValueError('Every commit path must have an explicitly staged change')
    literal = [f':(literal){name}' for name in files]
    if git(root, 'diff', '--name-only', '-z', '--', *literal):
        raise ValueError('Worktree differs from verified staged snapshot')
    if not git(root, 'diff', '--cached', '--name-only', '-z', '--', *literal):
        raise ValueError('No staged changes in commit scope')
    git(root, '-c', 'core.whitespace=blank-at-eol,blank-at-eof,space-before-tab,cr-at-eol',
        'diff', '--cached', '--check', '--', *literal)
    validate(root, state)
    print(git(root, 'commit', '--only', '-m', args.message, '--', *literal).decode('utf-8', 'replace'))
    state['head'] = text(root, 'rev-parse', 'HEAD')
    state['staged_baseline'] = staged(root)
    save(path, state)
    print(f"COMMITTED_LOCAL: {state['head']}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for command in ('prepare', 'bind', 'check', 'commit', 'release'):
        item = sub.add_parser(command)
        item.add_argument('--checkout', required=True)
        item.add_argument('--chat-key', required=True)
        if command == 'bind':
            item.add_argument('--project', required=True)
            item.add_argument('--branch', required=True)
            item.add_argument('--refresh-head', action='store_true')
        if command == 'prepare':
            item.add_argument('--project', required=True)
            item.add_argument('--worktree')
            item.add_argument('--branch')
            item.add_argument('--ref')
        if command == 'commit':
            item.add_argument('--file', action='append', required=True)
            item.add_argument('--message', required=True)
    try:
        run(parser.parse_args())
        return 0
    except (ValueError, OSError, KeyError) as error:
        print(f'BLOCKED: {error}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())

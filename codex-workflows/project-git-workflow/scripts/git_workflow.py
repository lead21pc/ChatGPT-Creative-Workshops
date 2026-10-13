#!/usr/bin/env python3
"""Shared-working-state Git helper with scoped local commits."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path
from typing import Iterable


class WorkflowError(RuntimeError):
    pass


def run(command: list[str], *, cwd: Path, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        command,
        cwd=cwd,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
    )
    if check and result.returncode:
        detail = (result.stderr or result.stdout).strip()
        raise WorkflowError(f"Command failed ({result.returncode}): {' '.join(command)}\n{detail}")
    return result


def git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return run(
        ["git", "-c", f"safe.directory={root}", *args],
        cwd=root,
        check=check,
    )


def _start_directory(path: Path) -> Path:
    candidate = path.expanduser().absolute()
    if candidate.exists() and candidate.is_file():
        return candidate.parent
    if not candidate.exists():
        return candidate.parent
    return candidate


def discover_repository(path: str | Path) -> Path:
    candidate = _start_directory(Path(path))
    while True:
        marker = candidate / ".git"
        if marker.is_dir() or marker.is_file():
            root = Path(git(candidate, "rev-parse", "--show-toplevel").stdout.strip())
            return root.resolve()
        if candidate.parent == candidate:
            raise WorkflowError(f"No containing Git repository for: {path}")
        candidate = candidate.parent


def _under(path: Path, root: Path) -> bool:
    try:
        os.path.commonpath([os.path.normcase(str(path)), os.path.normcase(str(root))])
    except ValueError:
        return False
    return os.path.commonpath(
        [os.path.normcase(str(path)), os.path.normcase(str(root))]
    ) == os.path.normcase(str(root))


def scoped_path(root: Path, value: str | Path) -> Path:
    raw = Path(value).expanduser()
    absolute = raw.absolute() if raw.is_absolute() else (root / raw).absolute()
    resolved = absolute.resolve(strict=False)
    if not _under(resolved, root.resolve()):
        raise WorkflowError(f"Path escapes repository: {value}")
    current = root.resolve()
    relative = resolved.relative_to(root.resolve())
    for part in relative.parts:
        current = current / part
        if current.exists() and current.is_symlink():
            raise WorkflowError(f"Symlinked path is not eligible: {value}")
    return resolved


def relative(root: Path, path: Path) -> str:
    value = path.relative_to(root).as_posix()
    return value or "."


def literal(value: str) -> str:
    return f":(literal){value}"


def staged_paths(root: Path) -> list[str]:
    output = git(root, "diff", "--cached", "--name-only", "-z").stdout
    return [item for item in output.split("\0") if item]


def inspect_state(path: str, write_scopes: Iterable[str], read_paths: Iterable[str]) -> dict:
    root = discover_repository(path)
    writes = [relative(root, scoped_path(root, item)) for item in write_scopes]
    reads = []
    for item in read_paths:
        read_path = Path(item).expanduser().absolute()
        reads.append(
            {
                "path": str(read_path.resolve(strict=False)),
                "repository": str(discover_repository(read_path)),
                "exists": read_path.exists(),
            }
        )
    branch = git(root, "branch", "--show-current").stdout.strip()
    return {
        "repository": str(root),
        "branch": branch or None,
        "head": git(root, "rev-parse", "HEAD").stdout.strip(),
        "status": git(root, "status", "--short").stdout.splitlines(),
        "staged": staged_paths(root),
        "write_scopes": writes,
        "read_dependencies": reads,
        "working_state": "current",
    }


def _binary_staged(root: Path, paths: list[str]) -> str:
    if not paths:
        return ""
    return git(root, "diff", "--cached", "--binary", "--", *map(literal, paths)).stdout


def commit_files(path: str, write_scopes: Iterable[str], files: Iterable[str], message: str) -> dict:
    root = discover_repository(path)
    scopes = [scoped_path(root, item) for item in write_scopes]
    if not scopes:
        raise WorkflowError("At least one --write-scope is required")

    task_paths: list[str] = []
    for item in files:
        resolved = scoped_path(root, item)
        if not any(_under(resolved, scope) for scope in scopes):
            raise WorkflowError(f"Task file is outside WRITE scope: {item}")
        rel = relative(root, resolved)
        if rel == "." or rel in task_paths:
            raise WorkflowError(f"Invalid or duplicate task file: {item}")
        if not resolved.exists() and git(root, "ls-files", "--error-unmatch", "--", literal(rel), check=False).returncode:
            raise WorkflowError(f"Task file does not exist and is not tracked: {item}")
        task_paths.append(rel)
    if not task_paths:
        raise WorkflowError("At least one --file is required")

    baseline = staged_paths(root)
    overlap = sorted(set(baseline) & set(task_paths))
    if overlap:
        raise WorkflowError(f"Task file was already staged: {', '.join(overlap)}")
    baseline_diff = _binary_staged(root, baseline)

    git(root, "add", "--", *map(literal, task_paths))
    now_staged = staged_paths(root)
    missing = sorted(set(task_paths) - set(now_staged))
    if missing:
        raise WorkflowError(f"Task files have no staged change: {', '.join(missing)}")
    if _binary_staged(root, baseline) != baseline_diff:
        raise WorkflowError("Pre-existing staged baseline changed while staging task files")
    if git(root, "diff", "--name-only", "--", *map(literal, task_paths)).stdout.strip():
        raise WorkflowError("Working-tree content changed after task files were staged")

    git(root, "diff", "--cached", "--check", "--", *map(literal, task_paths))
    stat = git(root, "diff", "--cached", "--stat", "--", *map(literal, task_paths)).stdout
    diff = git(root, "diff", "--cached", "--", *map(literal, task_paths)).stdout
    commit = git(root, "commit", "--only", "-m", message, "--", *map(literal, task_paths))
    sha = git(root, "rev-parse", "HEAD").stdout.strip()
    committed = [
        item
        for item in git(root, "diff-tree", "--no-commit-id", "--name-only", "-r", "-z", sha).stdout.split("\0")
        if item
    ]
    unexpected = sorted(set(committed) - set(task_paths))
    if unexpected:
        raise WorkflowError(f"Commit contains files outside the task list: {', '.join(unexpected)}")
    if _binary_staged(root, baseline) != baseline_diff:
        raise WorkflowError("Pre-existing staged baseline was not preserved after commit")
    return {
        "repository": str(root),
        "commit": sha,
        "files": task_paths,
        "staged_baseline_preserved": baseline,
        "stat": stat,
        "diff": diff,
        "git_output": commit.stdout.strip(),
    }


def create_isolation(
    path: str,
    kind: str,
    reason: str,
    branch: str,
    ref: str,
    worktree: str | None = None,
) -> dict:
    root = discover_repository(path)
    if not reason.strip():
        raise WorkflowError("Isolation requires a concrete --reason")
    if not branch.strip() or not ref.strip():
        raise WorkflowError("Isolation requires explicit --branch and --ref")
    git(root, "rev-parse", "--verify", f"{ref}^{{commit}}")
    if kind == "branch":
        if git(root, "status", "--porcelain").stdout:
            raise WorkflowError("Branch isolation requires a clean current working tree")
        git(root, "switch", "-c", branch, ref)
        return {
            "repository": str(root),
            "kind": kind,
            "reason": reason,
            "branch": branch,
            "checkout": str(root),
        }
    if kind == "worktree":
        if not worktree:
            raise WorkflowError("Worktree isolation requires --worktree")
        destination = Path(worktree).expanduser().absolute()
        if destination.exists():
            raise WorkflowError(f"Worktree destination already exists: {destination}")
        git(root, "worktree", "add", "-b", branch, str(destination), ref)
        return {
            "repository": str(root),
            "kind": kind,
            "reason": reason,
            "branch": branch,
            "checkout": str(destination),
        }
    raise WorkflowError(f"Unsupported isolation kind: {kind}")


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    sub = result.add_subparsers(dest="command", required=True)
    inspect_parser = sub.add_parser("inspect", help="Inspect the current shared working state")
    inspect_parser.add_argument("--path", required=True)
    inspect_parser.add_argument("--write-scope", action="append", default=[])
    inspect_parser.add_argument("--read-path", action="append", default=[])
    commit_parser = sub.add_parser("commit", help="Stage and commit explicit task-owned files locally")
    commit_parser.add_argument("--path", required=True)
    commit_parser.add_argument("--write-scope", action="append", default=[])
    commit_parser.add_argument("--file", action="append", default=[])
    commit_parser.add_argument("--message", required=True)
    isolate_parser = sub.add_parser("isolate", help="Create an explicitly justified branch/worktree fallback")
    isolate_parser.add_argument("--path", required=True)
    isolate_parser.add_argument("--kind", required=True, choices=("branch", "worktree"))
    isolate_parser.add_argument("--reason", required=True)
    isolate_parser.add_argument("--branch", required=True)
    isolate_parser.add_argument("--ref", required=True)
    isolate_parser.add_argument("--worktree")
    return result


def main() -> int:
    args = parser().parse_args()
    try:
        if args.command == "inspect":
            payload = inspect_state(args.path, args.write_scope, args.read_path)
        elif args.command == "commit":
            payload = commit_files(args.path, args.write_scope, args.file, args.message)
        else:
            payload = create_isolation(
                args.path, args.kind, args.reason, args.branch, args.ref, args.worktree
            )
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0
    except WorkflowError as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False, indent=2))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

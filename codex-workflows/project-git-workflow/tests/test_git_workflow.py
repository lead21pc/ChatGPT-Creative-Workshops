import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from types import SimpleNamespace

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'git_workflow.py'
SPEC = importlib.util.spec_from_file_location('workflow', SCRIPT)
workflow = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(workflow)


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.project = self.root / 'project'
        self.project.mkdir()
        self.git('init', '-b', 'work')
        self.git('config', 'user.name', 'Workflow Test')
        self.git('config', 'user.email', 'test@example.invalid')
        self.write('project/base.txt', 'base\n')
        self.write('other.txt', 'other\n')
        self.git('add', '.')
        self.git('commit', '-m', 'baseline')

    def git(self, *args):
        return workflow.git(self.root, *args)

    def write(self, name, content):
        target = self.root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding='utf-8')

    def call(self, command, **kwargs):
        options = dict(command=command, checkout=str(self.root), chat_key='chat-a',
                       project=str(self.project), branch='work', refresh_head=False,
                       worktree=None, ref=None)
        options.update(kwargs)
        return workflow.run(SimpleNamespace(**options))

    def task_file(self):
        self.write('project/new [file].txt', 'new\n')
        self.git('add', '--', ':(literal)project/new [file].txt')

    def test_reuse_across_commits_creates_no_branch(self):
        self.call('bind')
        branches = self.git('branch', '--list')
        for number in range(2):
            name = f'project/task{number}.txt'
            self.write(name, 'task\n')
            self.git('add', name)
            self.call('commit', file=[name], message='checkpoint')
            self.call('bind')
            self.call('check')
        self.assertEqual(branches, self.git('branch', '--list'))

    def test_rename_tracks_both_endpoints(self):
        self.call('bind')
        self.git('mv', 'project/base.txt', 'project/renamed.txt')
        self.assertEqual({'project/base.txt', 'project/renamed.txt'},
                         set(workflow.staged(self.root)))
        self.call('commit', file=['project/base.txt', 'project/renamed.txt'],
                  message='rename checkpoint')
        self.assertEqual(b'', self.git('status', '--porcelain'))
        self.call('check')

    def test_wrong_branch_blocks_commit(self):
        self.call('bind')
        self.git('switch', '-c', 'another')
        self.task_file()
        before = self.git('rev-parse', 'HEAD')
        with self.assertRaisesRegex(ValueError, 'Branch differs'):
            self.call('commit', file=['project/new [file].txt'], message='blocked')
        self.assertEqual(before, self.git('rev-parse', 'HEAD'))

    def test_preexisting_staging_survives_scoped_commit(self):
        self.write('other.txt', 'staged user edit\n')
        self.git('add', 'other.txt')
        before = self.git('diff', '--cached', '--binary')
        self.call('bind')
        self.task_file()
        self.call('commit', file=['project/new [file].txt'], message='task')
        self.assertEqual(before, self.git('diff', '--cached', '--binary'))
        self.assertEqual(b'project/new [file].txt\n',
                         self.git('diff-tree', '--no-commit-id', '--name-only', '-r', 'HEAD'))

    def test_baseline_path_overlap_blocked(self):
        self.write('project/base.txt', 'user edit\n')
        self.git('add', 'project/base.txt')
        self.call('bind')
        with self.assertRaisesRegex(ValueError, 'pre-existing staged'):
            self.call('commit', file=['project/base.txt'], message='blocked')

    def test_scope_blocks_other_project(self):
        self.call('bind')
        self.write('other.txt', 'other edit\n')
        self.git('add', 'other.txt')
        with self.assertRaisesRegex(ValueError, 'outside project'):
            self.call('commit', file=['other.txt'], message='blocked')

    def test_unverified_worktree_edit_blocked(self):
        self.call('bind')
        self.task_file()
        self.write('project/new [file].txt', 'changed after stage\n')
        with self.assertRaisesRegex(ValueError, 'staged snapshot'):
            self.call('commit', file=['project/new [file].txt'], message='blocked')

    def test_readonly_check_does_not_create_state(self):
        before = self.git('status', '--porcelain')
        with self.assertRaisesRegex(ValueError, 'No chat binding'):
            self.call('check')
        self.assertFalse(workflow.state_path(self.root, 'chat-a').parent.exists())
        self.assertEqual(before, self.git('status', '--porcelain'))

    def test_other_chat_cannot_claim_same_checkout(self):
        self.call('bind')
        with self.assertRaisesRegex(ValueError, 'another chat'):
            self.call('bind', chat_key='chat-b')

    def test_external_head_requires_explicit_refresh(self):
        self.call('bind')
        self.write('project/base.txt', 'external change\n')
        self.git('add', 'project/base.txt')
        self.git('commit', '-m', 'external')
        with self.assertRaisesRegex(ValueError, 'HEAD changed'):
            self.call('check')
        self.call('bind', refresh_head=True)
        self.call('check')

    def test_binding_cannot_change_project(self):
        self.call('bind')
        with self.assertRaisesRegex(ValueError, 'cannot be reassigned'):
            self.call('bind', project=str(self.root))

    def test_unstaged_extra_path_blocked(self):
        self.call('bind')
        self.task_file()
        self.write('project/unstaged.txt', 'not verified\n')
        with self.assertRaisesRegex(ValueError, 'explicitly staged'):
            self.call('commit', file=['project/new [file].txt', 'project/unstaged.txt'],
                      message='blocked')

    @unittest.skipUnless(workflow.os.name == 'nt', 'Windows path comparison')
    def test_case_alias_cannot_bypass_baseline(self):
        self.write('project/base.txt', 'user edit\n')
        self.git('add', 'project/base.txt')
        self.call('bind')
        with self.assertRaisesRegex(ValueError, 'pre-existing staged'):
            self.call('commit', file=['PROJECT/BASE.TXT'], message='blocked')

    def test_different_checkout_blocked(self):
        self.call('bind')
        checkout = self.root.parent / (self.root.name + '-worktree')
        self.git('worktree', 'add', '-b', 'second', str(checkout))
        try:
            with self.assertRaisesRegex(ValueError, 'Checkout differs'):
                self.call('check', checkout=str(checkout))
        finally:
            self.git('worktree', 'remove', str(checkout))

    def prepare_chat(self, key='chat-b'):
        target = self.root.parent / (self.root.name + '-' + key)
        self.call('prepare', chat_key=key, worktree=str(target),
                  branch='codex/' + key, ref='HEAD')
        self.addCleanup(lambda: self.git('worktree', 'remove', '--force', str(target)))
        return target

    def test_prepare_isolates_two_chats_and_preserves_dirty_source(self):
        self.call('bind')
        self.write('other.txt', 'staged source\n')
        self.git('add', 'other.txt')
        self.write('project/base.txt', 'unstaged source\n')
        self.write('project/untracked.txt', 'untracked source\n')
        before = (self.git('status', '--porcelain'), self.git('diff', '--binary'),
                  self.git('diff', '--cached', '--binary'), self.git('rev-parse', 'HEAD'))
        target = self.prepare_chat()
        self.call('check', chat_key='chat-b', checkout=str(target))
        self.call('check')
        self.assertEqual(b'', workflow.git(target, 'status', '--porcelain'))
        self.assertEqual('base\n', (target / 'project/base.txt').read_text())
        self.assertEqual(before, (self.git('status', '--porcelain'), self.git('diff', '--binary'),
                                 self.git('diff', '--cached', '--binary'), self.git('rev-parse', 'HEAD')))

    def test_prepare_reuses_binding_without_creating_new_branch(self):
        target = self.prepare_chat()
        branches = self.git('branch', '--list')
        self.call('prepare', chat_key='chat-b')
        self.assertEqual(branches, self.git('branch', '--list'))
        self.call('check', chat_key='chat-b', checkout=str(target))

    def test_isolated_commit_does_not_move_other_chat_head_or_index(self):
        self.call('bind')
        self.write('other.txt', 'user staging\n')
        self.git('add', 'other.txt')
        before = (self.git('rev-parse', 'HEAD'), self.git('diff', '--cached', '--binary'))
        target = self.prepare_chat()
        (target / 'project/base.txt').write_text('isolated edit\n', encoding='utf-8')
        workflow.git(target, 'add', 'project/base.txt')
        self.call('commit', checkout=str(target), chat_key='chat-b',
                  file=['project/base.txt'], message='isolated checkpoint')
        self.call('check')
        self.call('prepare', chat_key='chat-b')
        self.assertEqual(before, (self.git('rev-parse', 'HEAD'), self.git('diff', '--cached', '--binary')))

    def test_prepare_uses_selected_ref_and_rejects_invalid_ref(self):
        before = self.git('rev-parse', 'HEAD').strip()
        self.git('commit', '--allow-empty', '-m', 'later source')
        target = self.root.parent / (self.root.name + '-selected')
        self.call('prepare', worktree=str(target), branch='codex/selected',
                  ref=before.decode())
        self.addCleanup(lambda: self.git('worktree', 'remove', '--force', str(target)))
        self.assertEqual(before, workflow.git(target, 'rev-parse', 'HEAD').strip())
        worktrees = self.git('worktree', 'list', '--porcelain')
        with self.assertRaises(ValueError):
            self.call('prepare', chat_key='bad-ref',
                      worktree=str(self.root.parent / (self.root.name + '-bad-ref')),
                      branch='codex/bad-ref', ref='missing-ref')
        self.assertEqual(worktrees, self.git('worktree', 'list', '--porcelain'))

    def test_prepare_rejects_scope_change_and_external_head(self):
        target = self.prepare_chat()
        with self.assertRaisesRegex(ValueError, 'cannot be reassigned'):
            self.call('prepare', chat_key='chat-b', project=str(self.root))
        workflow.git(target, 'commit', '--allow-empty', '-m', 'external')
        with self.assertRaisesRegex(ValueError, 'HEAD changed'):
            self.call('prepare', chat_key='chat-b')

    def test_prepare_requires_explicit_initial_parameters(self):
        with self.assertRaisesRegex(ValueError, 'First prepare requires'):
            self.call('prepare')
        self.assertFalse(workflow.state_path(self.root, 'chat-a').exists())

    def test_prepare_rejects_existing_target_or_branch(self):
        before = self.git('worktree', 'list', '--porcelain')
        with self.assertRaisesRegex(ValueError, 'unused path'):
            self.call('prepare', worktree=str(self.root), branch='codex/new', ref='HEAD')
        with self.assertRaisesRegex(ValueError, 'Branch already exists'):
            self.call('prepare', worktree=str(self.root.parent / (self.root.name + '-unused')),
                      branch='work', ref='HEAD')
        self.assertEqual(before, self.git('worktree', 'list', '--porcelain'))

    def test_prepare_rejects_missing_project_at_ref_before_creation(self):
        (self.root / 'new-project').mkdir()
        before = self.git('worktree', 'list', '--porcelain')
        with self.assertRaises(ValueError):
            self.call('prepare', project=str(self.root / 'new-project'),
                      worktree=str(self.root.parent / (self.root.name + '-unused')),
                      branch='codex/new', ref='HEAD')
        self.assertEqual(before, self.git('worktree', 'list', '--porcelain'))

    def test_release_archives_binding_and_preserves_checkout_history(self):
        self.call('bind')
        path = workflow.state_path(self.root, 'chat-a')
        before = path.read_bytes()
        head = self.git('rev-parse', 'HEAD')
        self.call('release')
        self.assertFalse(path.exists())
        archived = list((path.parent / 'released').glob('*.json'))
        self.assertEqual(1, len(archived))
        self.assertEqual(before, archived[0].read_bytes())
        self.assertEqual(head, self.git('rev-parse', 'HEAD'))
        self.call('bind', chat_key='chat-b')

    def test_release_blocks_dirty_staged_and_untracked_files(self):
        self.call('bind')
        for mode in ('unstaged', 'staged', 'untracked'):
            with self.subTest(mode=mode):
                if mode == 'untracked':
                    self.write('new.txt', 'new\n')
                else:
                    self.write('other.txt', 'changed\n')
                    if mode == 'staged':
                        self.git('add', 'other.txt')
                with self.assertRaisesRegex(ValueError, 'clean checkout'):
                    self.call('release')
                self.assertTrue(workflow.state_path(self.root, 'chat-a').exists())
                if mode == 'untracked':
                    (self.root / 'new.txt').unlink()
                else:
                    self.git('restore', '--staged', '--worktree', 'other.txt')

    def test_release_blocks_wrong_key_and_head(self):
        self.call('bind')
        with self.assertRaisesRegex(ValueError, 'No chat binding'):
            self.call('release', chat_key='chat-b')
        self.git('commit', '--allow-empty', '-m', 'external')
        with self.assertRaisesRegex(ValueError, 'HEAD changed'):
            self.call('release')

    def test_registry_lock_blocks_parallel_mutation_without_claim(self):
        with workflow.registry_lock(self.root, 'chat-a'):
            with self.assertRaisesRegex(ValueError, 'registry busy'):
                self.call('bind', chat_key='chat-b')
            self.assertFalse(workflow.state_path(self.root, 'chat-b').exists())
        self.call('bind')

    def test_duplicate_legacy_owner_cannot_bypass_check(self):
        self.call('bind')
        path = workflow.state_path(self.root, 'chat-a')
        state = json.loads(path.read_text())
        state['shared_checkout_authorized'] = 'legacy authorization'
        workflow.save(workflow.state_path(self.root, 'legacy-chat'), state)
        with self.assertRaisesRegex(ValueError, 'another chat'):
            self.call('check')
        with self.assertRaisesRegex(ValueError, 'another chat'):
            self.call('bind')
        self.prepare_chat()


if __name__ == '__main__':
    unittest.main()

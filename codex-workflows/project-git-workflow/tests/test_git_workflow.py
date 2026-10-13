import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SCRIPT = Path(__file__).parents[1] / "scripts" / "git_workflow.py"
SPEC = importlib.util.spec_from_file_location("git_workflow", SCRIPT)
workflow = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(workflow)


def command(cwd: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(args), cwd=cwd, text=True, encoding="utf-8", capture_output=True, check=True
    )


def git(cwd: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return command(cwd, "git", "-c", f"safe.directory={cwd}", *args)


class SharedWorkingStateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "repo"
        self.root.mkdir()
        git(self.root, "init", "-b", "shared-main")
        git(self.root, "config", "user.name", "Workflow Test")
        git(self.root, "config", "user.email", "workflow@example.invalid")
        for name in ("Project Feather Core", "ChatGPT Plus+ Era", "Project CI"):
            (self.root / name).mkdir()
            (self.root / name / "README.md").write_text(f"{name}\n", encoding="utf-8")
        git(self.root, "add", "--", ":(literal)Project Feather Core/README.md", ":(literal)ChatGPT Plus+ Era/README.md", ":(literal)Project CI/README.md")
        git(self.root, "commit", "-m", "baseline")

    def tearDown(self):
        self.temp.cleanup()

    def branches(self):
        return git(self.root, "branch", "--format=%(refname:short)").stdout.splitlines()

    def worktrees(self):
        return [line for line in git(self.root, "worktree", "list", "--porcelain").stdout.splitlines() if line.startswith("worktree ")]

    def test_a_two_chats_can_share_checkout_with_distinct_write_scopes(self):
        before_branch = git(self.root, "branch", "--show-current").stdout.strip()
        first = workflow.inspect_state(str(self.root / "Project Feather Core"), ["Project Feather Core"], [])
        second = workflow.inspect_state(str(self.root / "Project CI"), ["Project CI"], [])
        self.assertEqual(first["repository"], second["repository"])
        self.assertEqual(first["branch"], before_branch)
        self.assertEqual(second["branch"], before_branch)
        self.assertFalse((self.root / ".git" / "codex-chat-bindings").exists())

    def test_b_dirty_dependency_is_read_from_current_working_tree(self):
        dependency = self.root / "ChatGPT Plus+ Era" / "README.md"
        dependency.write_text("newer dirty state\n", encoding="utf-8")
        before = self.worktrees()
        state = workflow.inspect_state(
            str(self.root / "Project Feather Core"),
            ["Project Feather Core"],
            [str(dependency)],
        )
        self.assertEqual(dependency.read_text(encoding="utf-8"), "newer dirty state\n")
        self.assertEqual(state["working_state"], "current")
        self.assertEqual(state["read_dependencies"][0]["path"], str(dependency.resolve()))
        self.assertEqual(self.worktrees(), before)

    def test_c_selective_commit_preserves_unrelated_staged_and_dirty_changes(self):
        unrelated = self.root / "Project CI" / "README.md"
        unrelated.write_text("user staged\n", encoding="utf-8")
        git(self.root, "add", "--", ":(literal)Project CI/README.md")
        dirty = self.root / "ChatGPT Plus+ Era" / "README.md"
        dirty.write_text("user dirty\n", encoding="utf-8")
        artifact = self.root / "Project Feather Core" / "artifact.md"
        artifact.write_text("verified artifact\n", encoding="utf-8")
        result = workflow.commit_files(
            str(artifact), ["Project Feather Core"], [str(artifact)], "checkpoint"
        )
        committed = git(self.root, "show", "--format=", "--name-only", result["commit"]).stdout.splitlines()
        self.assertEqual(committed, ["Project Feather Core/artifact.md"])
        self.assertEqual(workflow.staged_paths(self.root), ["Project CI/README.md"])
        self.assertIn(
            "ChatGPT Plus+ Era/README.md",
            git(self.root, "diff", "--name-only").stdout.splitlines(),
        )

    def test_d_local_commit_does_not_change_remote(self):
        bare = Path(self.temp.name) / "remote.git"
        command(Path(self.temp.name), "git", "init", "--bare", str(bare))
        git(self.root, "remote", "add", "origin", str(bare))
        git(self.root, "push", "-u", "origin", "shared-main")
        before = command(bare, "git", "rev-parse", "refs/heads/shared-main").stdout.strip()
        artifact = self.root / "Project Feather Core" / "local.md"
        artifact.write_text("local only\n", encoding="utf-8")
        workflow.commit_files(str(artifact), ["Project Feather Core"], [str(artifact)], "local")
        after = command(bare, "git", "rev-parse", "refs/heads/shared-main").stdout.strip()
        self.assertEqual(after, before)

    def test_e_normal_inspection_does_not_create_branch(self):
        before = self.branches()
        workflow.inspect_state(str(self.root), ["Project Feather Core"], [])
        self.assertEqual(self.branches(), before)

        result = workflow.create_isolation(
            str(self.root),
            "branch",
            "conflicting experiment requires an isolated branch",
            "temporary-isolation",
            "HEAD",
        )
        self.assertEqual(result["kind"], "branch")
        self.assertEqual(git(self.root, "branch", "--show-current").stdout.strip(), "temporary-isolation")

    def test_f_normal_commit_does_not_create_worktree(self):
        before = self.worktrees()
        artifact = self.root / "Project Feather Core" / "normal.md"
        artifact.write_text("normal\n", encoding="utf-8")
        workflow.commit_files(str(artifact), ["Project Feather Core"], [str(artifact)], "normal")
        self.assertEqual(self.worktrees(), before)

        destination = Path(self.temp.name) / "second-working-state"
        result = workflow.create_isolation(
            str(self.root),
            "worktree",
            "test requires two working states at the same time",
            "temporary-worktree-isolation",
            "HEAD",
            str(destination),
        )
        self.assertEqual(result["kind"], "worktree")
        self.assertEqual(len(self.worktrees()), len(before) + 1)
        git(self.root, "worktree", "remove", str(destination))

    def test_g_nested_target_reuses_nearest_parent_repository(self):
        nested = self.root / "Project Feather Core" / "deep" / "new.md"
        self.assertEqual(workflow.discover_repository(nested), self.root.resolve())
        self.assertFalse((self.root / "Project Feather Core" / ".git").exists())

    def test_h_newer_dirty_dependency_does_not_trigger_head_checkout(self):
        dependency = self.root / "ChatGPT Plus+ Era" / "README.md"
        dependency.write_text("version from current working tree\n", encoding="utf-8")
        head_text = git(self.root, "show", "HEAD:ChatGPT Plus+ Era/README.md").stdout
        self.assertNotEqual(dependency.read_text(encoding="utf-8"), head_text)
        workflow.inspect_state(str(self.root / "Project Feather Core"), ["Project Feather Core"], [str(dependency)])
        self.assertEqual(dependency.read_text(encoding="utf-8"), "version from current working tree\n")

    def test_i_two_repositories_are_discovered_independently(self):
        other = Path(self.temp.name) / "Image Transcendent"
        other.mkdir()
        git(other, "init", "-b", "main")
        git(other, "config", "user.name", "Workflow Test")
        git(other, "config", "user.email", "workflow@example.invalid")
        target = other / "image.md"
        target.write_text("image\n", encoding="utf-8")
        git(other, "add", "--", ":(literal)image.md")
        git(other, "commit", "-m", "baseline")
        first = workflow.inspect_state(str(self.root), ["Project CI"], [])
        second = workflow.inspect_state(str(target), ["."], [])
        self.assertNotEqual(first["repository"], second["repository"])

    def test_out_of_scope_file_is_rejected_without_staging(self):
        target = self.root / "Project CI" / "outside.md"
        target.write_text("outside\n", encoding="utf-8")
        with self.assertRaises(workflow.WorkflowError):
            workflow.commit_files(str(self.root), ["Project Feather Core"], [str(target)], "blocked")
        self.assertNotIn("Project CI/outside.md", workflow.staged_paths(self.root))

    def test_pre_staged_task_file_is_rejected_as_ambiguous(self):
        target = self.root / "Project Feather Core" / "README.md"
        target.write_text("already staged\n", encoding="utf-8")
        git(self.root, "add", "--", ":(literal)Project Feather Core/README.md")
        with self.assertRaises(workflow.WorkflowError):
            workflow.commit_files(str(target), ["Project Feather Core"], [str(target)], "blocked")

    def test_commit_path_never_invokes_push(self):
        target = self.root / "Project Feather Core" / "no-push.md"
        target.write_text("no push\n", encoding="utf-8")
        calls = []
        original = workflow.git

        def recording_git(root, *args, **kwargs):
            calls.append(args)
            return original(root, *args, **kwargs)

        with mock.patch.object(workflow, "git", side_effect=recording_git):
            workflow.commit_files(str(target), ["Project Feather Core"], [str(target)], "no push")
        self.assertFalse(any("push" in call for call in calls))


if __name__ == "__main__":
    unittest.main()

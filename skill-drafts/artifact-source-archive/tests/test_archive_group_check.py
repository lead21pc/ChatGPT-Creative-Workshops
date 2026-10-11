from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "check_archive_group.py"
SPEC = importlib.util.spec_from_file_location("check_archive_group", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ArchiveGroupCheckTests(unittest.TestCase):
    def _source(self, root: Path, relative: str) -> Path:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("source", encoding="utf-8")
        return path

    def test_sibling_sources_share_one_new_root_archive(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            task_root = Path(directory)
            artifact_root = task_root / "group"
            first = self._source(artifact_root, "a/v1.md")
            second = self._source(artifact_root, "b/v1.md")

            payload, exit_code = MODULE.check(
                str(task_root), str(artifact_root), [str(first), str(second)]
            )

            self.assertEqual(exit_code, 0)
            self.assertEqual(payload["status"], "PASS_CREATE_ONE")
            self.assertEqual(
                Path(payload["archive_destination"]),
                artifact_root.resolve() / "source_archive",
            )
            self.assertFalse((artifact_root / "source_archive").exists())

    def test_existing_case_variant_at_root_is_reused(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            task_root = Path(directory)
            artifact_root = task_root / "group"
            source = self._source(artifact_root, "v1.md")
            archive = artifact_root / "Source_Archive"
            archive.mkdir()

            payload, exit_code = MODULE.check(str(task_root), str(artifact_root), [str(source)])

            self.assertEqual(exit_code, 0)
            self.assertEqual(payload["status"], "PASS_SHARED")
            self.assertEqual(Path(payload["archive_destination"]), archive.resolve())

    def test_nested_archive_blocks_group_fragmentation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            task_root = Path(directory)
            artifact_root = task_root / "group"
            first = self._source(artifact_root, "a/v1.md")
            second = self._source(artifact_root, "b/v1.md")
            (first.parent / "source_archive").mkdir()

            payload, exit_code = MODULE.check(
                str(task_root), str(artifact_root), [str(first), str(second)]
            )

            self.assertEqual(exit_code, 2)
            self.assertEqual(payload["status"], "BLOCKED")
            self.assertTrue(any("fragment" in problem for problem in payload["problems"]))

    def test_source_outside_artifact_root_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            task_root = Path(directory)
            artifact_root = task_root / "group"
            artifact_root.mkdir()
            source = self._source(task_root, "other/v1.md")

            payload, exit_code = MODULE.check(str(task_root), str(artifact_root), [str(source)])

            self.assertEqual(exit_code, 2)
            self.assertTrue(any("outside artifact root" in problem for problem in payload["problems"]))

    def test_source_already_in_archive_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            task_root = Path(directory)
            artifact_root = task_root / "group"
            source = self._source(artifact_root, "source_archive/v1.md")

            payload, exit_code = MODULE.check(str(task_root), str(artifact_root), [str(source)])

            self.assertEqual(exit_code, 2)
            self.assertTrue(any("already inside" in problem for problem in payload["problems"]))

    def test_file_occupying_archive_name_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            task_root = Path(directory)
            artifact_root = task_root / "group"
            source = self._source(artifact_root, "v1.md")
            (artifact_root / "source_archive").write_text("occupied", encoding="utf-8")

            payload, exit_code = MODULE.check(str(task_root), str(artifact_root), [str(source)])

            self.assertEqual(exit_code, 2)
            self.assertTrue(any("non-directory" in problem for problem in payload["problems"]))


if __name__ == "__main__":
    unittest.main()

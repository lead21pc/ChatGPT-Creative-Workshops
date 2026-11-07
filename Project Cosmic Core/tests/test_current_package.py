"""Contract tests run on disposable copies, never mutate the maintained package."""

import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('c2_maintenance', ROOT / 'build_consolidation.py')
tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)


class PackageTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='c2-contract-')
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name) / 'C2 checkout with spaces'
        self.root.mkdir()
        for name in tool.CURRENT_FILES + (tool.MANIFEST, 'build_consolidation.py'):
            (self.root / name).write_bytes((ROOT / name).read_bytes())

    def snapshot(self):
        return {p.relative_to(self.root).as_posix(): p.read_bytes()
                for p in self.root.rglob('*') if p.is_file()}

    def cli(self, *args):
        return subprocess.run([sys.executable, '-B', str(self.root / 'build_consolidation.py'), *args],
                              cwd=self.root.parent, capture_output=True, text=True)

    def replace(self, name, old, new):
        path = self.root / name
        data = path.read_bytes()
        self.assertIn(old, data)
        path.write_bytes(data.replace(old, new, 1))

    def rejected(self):
        before = self.snapshot()
        for args in ((), ('--check',), ('--write',)):
            result = self.cli(*args)
            self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
            self.assertEqual(before, self.snapshot())

    def test_current_baseline_and_read_only_default_check(self):
        before = self.snapshot()
        for args in ((), ('--check',)):
            result = self.cli(*args)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(before, self.snapshot())
        self.assertEqual(len(tool.ACCEPTED), 15)
        self.assertEqual(len(tool.CURRENT_FILES), 19)

    def test_duplicate_module_id_fails(self):
        self.replace(tool.ACCEPTED['C2M-002'], b'`C2M-002`', b'`C2M-001`')
        self.rejected()

    def test_wrong_id_path_mapping_fails(self):
        a, b = tool.ACCEPTED['C2M-021'], tool.ACCEPTED['C2M-022']
        self.replace(a, b'> Module ID: `C2M-021`', b'> Module ID: `C2M-022`')
        self.replace(b, b'> Module ID: `C2M-022`', b'> Module ID: `C2M-021`')
        self.rejected()

    def test_missing_header_field_fails(self):
        self.replace(tool.MODULE_FILES[0], b'> Load mode: `FULL_FILE`\n', b'')
        self.rejected()

    def test_role_load_and_dependency_fields_fail(self):
        name = tool.MODULE_FILES[0]
        original = (self.root / name).read_bytes()
        for old, new in (
                (b'`CURRENT_SOURCE`', b'`PROPOSAL`'),
                (b'`FULL_FILE`', b'`NODE_OR_FULL`'),
                (b'> Load mode: `FULL_FILE`', b'> Load mode: `FULL_FILE`\n> MODULE_REQUIRES: `C2M-002`'),
                (b'> Load mode: `FULL_FILE`', b'> Load mode: `FULL_FILE`\n> NODE_REQUIRES: `C2M-002`')):
            with self.subTest(new=new):
                (self.root / name).write_bytes(original.replace(old, new, 1))
                self.rejected()

    def test_unknown_cross_owner_fails(self):
        self.replace(tool.MODULE_FILES[0], b'`C2M-010`', b'`C2M-999`')
        self.rejected()

    def test_unadmitted_current_source_fails(self):
        (self.root / '999_UNADMITTED.md').write_bytes((self.root / tool.MODULE_FILES[0]).read_bytes())
        self.rejected()

    def test_stale_catalog_mapping_fails_without_repairing_wrong_owner(self):
        self.replace(tool.INDEX,
                     f'| `C2M-021` | `{tool.ACCEPTED["C2M-021"]}` |'.encode(),
                     f'| `C2M-021` | `{tool.ACCEPTED["C2M-022"]}` |'.encode())
        self.rejected()

    def test_stale_generated_text_check_fails_write_repairs_only_region(self):
        self.replace(tool.INDEX, b'## Runtime Module Catalog', b'## Stale generated title')
        before = self.snapshot()
        self.assertEqual(self.cli('--check').returncode, 2)
        self.assertEqual(before, self.snapshot())
        result = self.cli('--write')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.cli('--check').returncode, 0)

    def test_stale_hash_fails_then_write_preserves_human_source(self):
        name = tool.ACCEPTED['C2M-110']
        path = self.root / name
        path.write_bytes(path.read_bytes() + '\nGhi chú thử trên bản sao.\n'.encode())
        before = self.snapshot()
        self.assertEqual(self.cli('--check').returncode, 2)
        self.assertEqual(before, self.snapshot())
        result = self.cli('--write')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(path.read_bytes(), before[name])
        self.assertEqual(self.cli('--check').returncode, 0)

    def test_write_allowlist_generated_regions_and_idempotence(self):
        self.replace(tool.INDEX, b'## Runtime Module Catalog', b'## Stale title')
        self.replace(tool.MANIFEST, b'## Current package maintenance', b'## Stale metadata')
        before = self.snapshot()
        result = self.cli('--write')
        self.assertEqual(result.returncode, 0, result.stderr)
        after = self.snapshot()
        self.assertEqual(set(before), set(after))
        for name in before:
            labels = ((tool.CATALOG,) if name == tool.INDEX else
                      (tool.METADATA, tool.HASHES) if name == tool.MANIFEST else ())
            old, new = before[name], after[name]
            for label in labels:
                old = tool.replace_region(old, label, '')
                new = tool.replace_region(new, label, '')
            self.assertEqual(old, new, name)
        self.assertEqual(self.cli('--write').returncode, 0)
        self.assertEqual(after, self.snapshot())
        inputs, _ = tool.plan(self.root, write=True)
        with self.assertRaises(tool.ValidationError):
            tool.atomic_write(self.root, inputs, {tool.MODULE_FILES[0]: b'forbidden'})
        with self.assertRaises(tool.ValidationError):
            tool.atomic_write(self.root, inputs, {tool.INDEX: inputs[tool.INDEX] + b'outside'})
        self.assertEqual(after, self.snapshot())

    def test_explicit_ids_survive_order_and_renumbered_path(self):
        # Reverse iteration and rename a source while retaining its established identity.
        # This models an explicitly approved path-map edit, not runtime ID generation.
        mapping = dict(reversed(list(tool.ACCEPTED.items())))
        old = mapping['C2M-021']
        new = '77_CHARACTER_25_1_CURRENT.md'
        (self.root / old).rename(self.root / new)
        mapping['C2M-021'] = new
        files = (tool.INDEX,) + tuple(mapping.values()) + tool.CURRENT_FILES[-3:]
        for filename, label in ((tool.INDEX, tool.CATALOG), (tool.MANIFEST, tool.HASHES)):
            path = self.root / filename
            data = path.read_bytes()
            _, _, _, block = tool.region(data, label)
            path.write_bytes(tool.replace_region(data, label, block.decode().replace(old, new)))
        with patch.object(tool, 'ACCEPTED', mapping), \
                patch.object(tool, 'MODULE_FILES', tuple(mapping.values())), \
                patch.object(tool, 'CURRENT_FILES', files):
            inputs, changes = tool.plan(self.root, write=True)
            tool.atomic_write(self.root, inputs, changes)
            tool.plan(self.root)
            self.assertEqual(tool.header((self.root / new).read_bytes(), new)['Module ID'], 'C2M-021')

    def test_archive_not_accessed(self):
        archive = self.root / 'Source_Archive'
        archive.mkdir()
        sentinel = archive / 'not_a_current_source.md'
        sentinel.write_bytes(b'not canon')
        original = Path.read_bytes

        def root_only(path):
            self.assertEqual(path.parent, self.root)
            return original(path)

        with patch.object(Path, 'read_bytes', root_only):
            tool.plan(self.root)
            inputs, changes = tool.plan(self.root, write=True)
            tool.atomic_write(self.root, inputs, changes)
        self.assertEqual(sentinel.read_bytes(), b'not canon')

    def test_replace_failure_rolls_back(self):
        self.replace(tool.INDEX, b'## Runtime Module Catalog', b'## Stale title')
        self.replace(tool.MANIFEST, b'## Current package maintenance', b'## Stale metadata')
        inputs, changes = tool.plan(self.root, write=True)
        self.assertEqual(set(changes), {tool.INDEX, tool.MANIFEST})
        before = self.snapshot()
        real_replace = tool.os.replace
        calls = 0

        def fail_second(source, target):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError('injected replace failure')
            return real_replace(source, target)

        with patch.object(tool.os, 'replace', fail_second):
            with self.assertRaises(OSError):
                tool.atomic_write(self.root, inputs, changes)
        self.assertEqual(before, self.snapshot())

    def test_concurrent_source_edit_is_preserved(self):
        self.replace(tool.INDEX, b'## Runtime Module Catalog', b'## Stale title')
        inputs, changes = tool.plan(self.root, write=True)
        path = self.root / tool.CURRENT_FILES[-1]
        path.write_bytes(path.read_bytes() + b'\nConcurrent edit\n')
        before = self.snapshot()
        with self.assertRaises(tool.ValidationError):
            tool.atomic_write(self.root, inputs, changes)
        self.assertEqual(before, self.snapshot())


if __name__ == '__main__':
    unittest.main()

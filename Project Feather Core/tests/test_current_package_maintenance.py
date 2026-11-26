"""Disposable-copy tests: python -B -m unittest discover -s tests -v."""

import hashlib
import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


PROJECT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('maintenance', PROJECT / 'build_consolidation.py')
tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)


class MaintenanceTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='af-package-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / 'checkout with spaces' / 'Project Feather Core'
        self.root.mkdir(parents=True)
        for name in tool.CURRENT_FILES + (tool.MANIFEST, 'build_consolidation.py'):
            (self.root / name).write_bytes((PROJECT / name).read_bytes())

    def snapshot(self):
        return {p.relative_to(self.root).as_posix(): p.read_bytes()
                for p in self.root.rglob('*') if p.is_file()}

    def run_cli(self, *args):
        return subprocess.run([sys.executable, '-B', str(self.root / 'build_consolidation.py'), *args],
                              cwd=self.root.parent.parent, capture_output=True, text=True)

    def sync(self):
        result = self.run_cli('--write')
        self.assertEqual(result.returncode, 0, result.stderr)

    def rejected_without_writes(self):
        before = self.snapshot()
        for args in ((), ('--check',), ('--write',)):
            result = self.run_cli(*args)
            self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
            self.assertEqual(before, self.snapshot())

    def test_no_lore_writes_header_survival_and_idempotence(self):
        before = {name: (self.root / name).read_bytes() for name in tool.CURRENT_FILES[1:]}
        hashes = {name: hashlib.sha256(data).hexdigest() for name, data in before.items()}
        self.sync()
        for number, name in enumerate(tool.MODULE_FILES, 1):
            self.assertEqual(tool.header((self.root / name).read_bytes(), name)['Module ID'],
                             f'AFM-{number:03d}')
        for name, data in before.items():
            self.assertEqual(data, (self.root / name).read_bytes())
            self.assertEqual(hashes[name], hashlib.sha256((self.root / name).read_bytes()).hexdigest())
        snapshot = self.snapshot()
        self.sync()
        self.assertEqual(snapshot, self.snapshot())

    def test_catalog_manifest_and_read_only_default(self):
        self.sync()
        before = self.snapshot()
        self.assertEqual(self.run_cli().returncode, 0)
        self.assertEqual(self.run_cli('--check').returncode, 0)
        self.assertEqual(before, self.snapshot())
        _, _, _, catalog = tool.region(before[tool.INDEX], tool.CATALOG)
        entries = tool.rows(catalog,
                            '| Module ID | Current source path (relative to Project Feather Core/) |',
                            tool.ACCEPTED)
        self.assertEqual(entries, tool.ACCEPTED)
        _, _, _, block = tool.region(before[tool.MANIFEST], tool.HASHES)
        hashes = tool.rows(block, '| File | SHA-256 |', tool.CURRENT_FILES)
        for name in tool.CURRENT_FILES:
            self.assertEqual(hashes[name], hashlib.sha256(before[name]).hexdigest().upper())
        self.assertNotIn(tool.MANIFEST, hashes)

    def test_politics_admission_and_previous_schema_bootstrap(self):
        name = tool.ACCEPTED['AFM-011']
        self.assertEqual(name, '12_POLITICS_DYNASTIC_SECURITY_CURRENT.md')
        values = tool.header((self.root / name).read_bytes(), name)
        for owner in ('AFM-001', 'AFM-002', 'AFM-003', 'AFM-004', 'AFM-008'):
            self.assertIn(owner, values['Cross-domain owner boundary'])
        self.sync()
        for filename, prefix in (
                (tool.INDEX, b'| `AFM-011` |'),
                (tool.MANIFEST, f'| `{name}` |'.encode())):
            path = self.root / filename
            path.write_bytes(b'\n'.join(line for line in path.read_bytes().split(b'\n')
                                       if not line.startswith(prefix)))
        before = self.snapshot()
        self.assertEqual(self.run_cli('--check').returncode, 2)
        self.assertEqual(before, self.snapshot())
        self.sync()
        self.assertEqual(self.run_cli('--check').returncode, 0)

    def test_missing_older_catalog_row_is_not_admission(self):
        self.sync()
        path = self.root / tool.INDEX
        path.write_bytes(b'\n'.join(line for line in path.read_bytes().split(b'\n')
                                   if not line.startswith(b'| `AFM-002` |')))
        self.rejected_without_writes()

    def test_hoa_nguyet_admission_and_previous_schema_bootstrap(self):
        name = tool.ACCEPTED['AFM-012']
        self.assertEqual(name, '20_HOA_NGUYET_NATIONAL_CANON_CURRENT.md')
        values = tool.header((self.root / name).read_bytes(), name)
        for owner in ('AFM-001', 'AFM-003', 'AFM-004', 'AFM-007', 'AFM-008', 'AFM-011'):
            self.assertIn(owner, values['Cross-domain owner boundary'])
        self.sync()
        for filename, prefix in (
                (tool.INDEX, b'| `AFM-012` |'),
                (tool.MANIFEST, f'| `{name}` |'.encode())):
            path = self.root / filename
            path.write_bytes(b'\n'.join(line for line in path.read_bytes().split(b'\n')
                                       if not line.startswith(prefix)))
        before = self.snapshot()
        self.assertEqual(self.run_cli('--check').returncode, 2)
        self.assertEqual(before, self.snapshot())
        self.sync()
        self.assertEqual(self.run_cli('--check').returncode, 0)

    def test_hoa_nguyet_source_and_open_boundaries_survive(self):
        name = tool.ACCEPTED['AFM-012']
        text = '\n'.join((self.root / tool.ACCEPTED[key]).read_text(encoding='utf-8')
                         for key in ('AFM-012', 'AFM-015', 'AFM-016', 'AFM-017'))
        for marker in ('鏡華水月', '華月', 'Lục Kì Nhân', 'Hanfu', 'UNKNOWN',
                       'Con đường Tơ lụa', 'không phải cửa ngõ đối ngoại duy nhất',
                       'Khả thi địa lý chưa xác lập tuyến đang hoạt động', 'chung chỉ huy'):
            with self.subTest(marker=marker):
                self.assertIn(marker, text)
        world = (self.root / tool.ACCEPTED['AFM-001']).read_text(encoding='utf-8')
        self.assertIn(name, world)
        self.assertNotIn('#### 1. Quyết định canon', world)
        ledger = (self.root / '92_OPEN_ISSUES_CURRENT.md').read_text(encoding='utf-8')
        self.assertIn('AF-HN-OPEN-005', ledger)
        self.assertIn(name, ledger)

    def test_missing_hoa_nguyet_source_fails_before_writes(self):
        (self.root / tool.ACCEPTED['AFM-012']).unlink()
        self.rejected_without_writes()

    def test_national_families_keep_original_module_ids(self):
        prefixes = {
            'AFM-001': '01', 'AFM-002': '11', 'AFM-003': '13',
            'AFM-004': '03', 'AFM-005': '04', 'AFM-006': '05',
            'AFM-007': '40', 'AFM-008': '06', 'AFM-009': '14',
            'AFM-010': '02', 'AFM-011': '12', 'AFM-012': '20',
            'AFM-013': '10', 'AFM-014': '30',
            'AFM-015': '21', 'AFM-016': '22', 'AFM-017': '23',
        }
        self.assertEqual(set(prefixes), set(tool.ACCEPTED))
        for key, prefix in prefixes.items():
            name = tool.ACCEPTED[key]
            self.assertTrue(name.startswith(prefix + '_'), name)
            self.assertEqual(tool.header((self.root / name).read_bytes(), name)['Module ID'], key)

    def test_af_and_rf_admission_from_previous_catalog(self):
        self.sync()
        for key in ('AFM-013', 'AFM-014'):
            for filename, prefix in (
                    (tool.INDEX, f'| `{key}` |'.encode()),
                    (tool.MANIFEST, f'| `{tool.ACCEPTED[key]}` |'.encode())):
                path = self.root / filename
                path.write_bytes(b'\n'.join(line for line in path.read_bytes().split(b'\n')
                                           if not line.startswith(prefix)))
        before = self.snapshot()
        self.assertEqual(self.run_cli('--check').returncode, 2)
        self.assertEqual(before, self.snapshot())
        self.sync()
        self.assertEqual(self.run_cli('--check').returncode, 0)

    def test_hoa_nguyet_subsystems_bootstrap_and_missing_source(self):
        self.sync()
        keys = ('AFM-015', 'AFM-016', 'AFM-017')
        for key in keys:
            for filename, prefix in (
                    (tool.INDEX, f'| `{key}` |'.encode()),
                    (tool.MANIFEST, f'| `{tool.ACCEPTED[key]}` |'.encode())):
                path = self.root / filename
                path.write_bytes(b'\n'.join(line for line in path.read_bytes().split(b'\n')
                                           if not line.startswith(prefix)))
        self.assertEqual(self.run_cli('--check').returncode, 2)
        self.sync()
        self.assertEqual(self.run_cli('--check').returncode, 0)
        for key in keys:
            path = self.root / tool.ACCEPTED[key]
            original = path.read_bytes()
            path.unlink()
            self.rejected_without_writes()
            path.write_bytes(original)

    def test_hoa_nguyet_owners_keep_canon_and_unknowns(self):
        sources = {key: (self.root / tool.ACCEPTED[key]).read_text(encoding='utf-8')
                   for key in ('AFM-012', 'AFM-015', 'AFM-016', 'AFM-017')}
        for marker in ('ba quốc gia tiền thân', 'Lục Kì Nhân', 'Thời điểm, nguyên nhân'):
            self.assertIn(marker, sources['AFM-012'])
        for marker in ('Chữ Quốc ngữ', 'chữ Hán, chữ Nôm', 'áo dài',
                       'không tự đặt ra nghĩa vụ thông thạo', 'phẩm cấp', 'AF-HN-OPEN-006'):
            self.assertIn(marker, sources['AFM-015'])
        for marker in ('鏡華水月', '華月', 'Hình học chi tiết, bảng màu', 'AF-HN-OPEN-001'):
            self.assertIn(marker, sources['AFM-016'])
        for marker in ('không phải cửa ngõ đối ngoại duy nhất', 'chung chỉ huy',
                       '### Hoa Nguyệt–Matriarch', 'mạnh hơn AF–RF', 'AF-HN-OPEN-003'):
            self.assertIn(marker, sources['AFM-017'])
        record = (self.root / '91_RECONCILIATION_RECORD.md').read_text(encoding='utf-8')
        self.assertIn('AF-HN-002', record)
        self.assertIn('AF-HN-008', record)
        ledger = (self.root / '92_OPEN_ISSUES_CURRENT.md').read_text(encoding='utf-8')
        self.assertIn('bảng màu quốc kỳ', ledger)
        for source in sources.values():
            self.assertNotIn('### 12. Phạm vi supersession cuối', source)
        self.assertNotIn('### 5.2. Nguồn gốc hợp nhất', sources['AFM-015'])

    def test_exact_predecessor_paths_migrate_only_with_write(self):
        self.sync()
        reverse = {new: old for old, new in tool.LEGACY_PATHS.items()}
        for mode in ('all', 'mixed'):
            with self.subTest(mode=mode):
                for filename, label in ((tool.INDEX, tool.CATALOG),
                                        (tool.MANIFEST, tool.HASHES)):
                    path = self.root / filename
                    data = path.read_bytes()
                    _, _, _, block = tool.region(data, label)
                    for number, (new, old) in enumerate(reverse.items()):
                        if mode == 'all' or number % 2 == 0:
                            block = block.replace(new.encode(), old.encode())
                    if mode == 'all':
                        for key in ('AFM-013', 'AFM-014'):
                            prefix = (f'| `{key}` |' if label == tool.CATALOG
                                      else f'| `{tool.ACCEPTED[key]}` |').encode()
                            block = b'\n'.join(line for line in block.split(b'\n')
                                               if not line.startswith(prefix))
                    path.write_bytes(tool.replace_region(data, label, block.decode()))
                before = self.snapshot()
                self.assertEqual(self.run_cli('--check').returncode, 2)
                self.assertEqual(before, self.snapshot())
                lore = {name: (self.root / name).read_bytes() for name in tool.MODULE_FILES}
                self.sync()
                self.assertEqual(self.run_cli('--check').returncode, 0)
                self.assertEqual(lore, {name: (self.root / name).read_bytes()
                                        for name in tool.MODULE_FILES})

    def test_wrong_predecessor_owner_and_duplicate_hash_are_rejected(self):
        self.sync()
        index = self.root / tool.INDEX
        manifest = self.root / tool.MANIFEST
        original_index = index.read_bytes()
        original_manifest = manifest.read_bytes()
        index.write_bytes(original_index.replace(
            tool.ACCEPTED['AFM-001'].encode(), b'20_STATUS_CIVIL_LABOR_CURRENT.md'))
        self.rejected_without_writes()
        index.write_bytes(original_index)
        _, _, _, block = tool.region(original_manifest, tool.HASHES)
        block += b'| `20_STATUS_CIVIL_LABOR_CURRENT.md` | `' + b'0' * 64 + b'` |\n'
        manifest.write_bytes(tool.replace_region(original_manifest, tool.HASHES, block.decode()))
        self.rejected_without_writes()

    def test_missing_national_profiles_fail_before_writes(self):
        for key in ('AFM-013', 'AFM-014'):
            with self.subTest(key=key):
                path = self.root / tool.ACCEPTED[key]
                data = path.read_bytes()
                path.unlink()
                self.rejected_without_writes()
                path.write_bytes(data)

    def test_world_technology_and_national_authority_boundaries(self):
        tech = (self.root / tool.ACCEPTED['AFM-010']).read_text(encoding='utf-8')
        for marker in ('Project Feather Core', 'Phạm vi §§4–8', 'ứng dụng AF',
                       'không xác nhận rollout', 'AF-TECH-001', 'AF-TECH-002'):
            self.assertIn(marker, tech)
        national = (self.root / tool.ACCEPTED['AFM-013']).read_text(encoding='utf-8')
        for marker in ('không phải sơ đồ cấp dưới hành chính', 'SERPENT STRIKE BELONGS_TO ACADEMY = FALSE',
                       'SHARED PRE-DIVERGENCE STATE', 'AF-OPEN-031',
                       'định hướng cho thiết kế quân đội/nhà nước AetherFire về sau'):
            self.assertIn(marker, national)
        rf = (self.root / tool.ACCEPTED['AFM-014']).read_text(encoding='utf-8')
        for marker in ('RF KHÔNG CÒN LÀ KHỐI TU TIÊN', 'Four foregrounded blocs',
                       'anh em cùng cha khác mẹ', 'CHƯA CHỐT', 'not one kingdom'):
            self.assertIn(marker, rf)
        academy = (self.root / tool.ACCEPTED['AFM-009']).read_text(encoding='utf-8')
        self.assertIn('Academic failure does not create an automatic Undie transition.', academy)
        ledger = (self.root / '92_OPEN_ISSUES_CURRENT.md').read_text(encoding='utf-8')
        for marker in ('AF-ORG-002 | UNKNOWN / OPEN', 'AF-ORG-003 | UNKNOWN / OPEN',
                       'AF-OPEN-031 | CONFLICT / OPEN', 'Lab-subject personhood',
                       'Exact RF constitutional form', 'DI legal powers'):
            self.assertIn(marker, ledger)

    def test_technology_module_admission_and_owner_boundary(self):
        name = '02_TECHNOLOGY_AND_PUBLIC_SERVICE_INFRASTRUCTURE_CURRENT.md'
        self.assertEqual(tool.ACCEPTED['AFM-010'], name)
        values = tool.header((self.root / name).read_bytes(), name)
        self.assertEqual(values['Module ID'], 'AFM-010')
        for owner in ('AFM-001', 'AFM-002', 'AFM-003', 'AFM-008'):
            self.assertIn(owner, values['Cross-domain owner boundary'])
        self.sync()
        self.assertEqual(self.run_cli('--check').returncode, 0)

    def test_guest_admission_preserves_explicit_open_boundaries(self):
        text = (self.root / tool.ACCEPTED['AFM-010']).read_text(encoding='utf-8')
        for marker in ('AF-TECH-001', 'AF-TECH-002',
                       'candidate accounting', '500', 'UNKNOWN'):
            with self.subTest(marker=marker):
                self.assertIn(marker, text)
        ledger = (self.root / '92_OPEN_ISSUES_CURRENT.md').read_text(encoding='utf-8')
        for marker in ('AF-TECH-001', 'AF-TECH-002', 'AF-STATE-001',
                       'AF-OPEN-006', 'AF-OPEN-008', 'AF-ML-007',
                       'Guest Wallet denomination', 'Offline behavior'):
            with self.subTest(marker=marker):
                self.assertIn(marker, ledger)
        record = (self.root / '91_RECONCILIATION_RECORD.md').read_text(encoding='utf-8')
        self.assertIn('AF-OPEN-006 | SUPERSEDED', record)
        self.assertIn('AF-OPEN-014 | SUPERSEDED', record)
        self.assertNotIn('| AF-OPEN-014 |', ledger)

    def test_generated_regions_only_and_archive_inventory_preserved(self):
        before = self.snapshot()
        self.sync()
        after = self.snapshot()
        for name, labels in ((tool.INDEX, (tool.CATALOG,)),
                             (tool.MANIFEST, (tool.METADATA, tool.HASHES))):
            old, new = before[name], after[name]
            for label in labels:
                old = tool.replace_region(old, label, '')
                new = tool.replace_region(new, label, '')
            self.assertEqual(old, new)
        self.assertEqual(set(before), set(after))

    def test_archive_hidden_check_and_write_without_archive_access(self):
        archive = self.root / 'Source_Archive'
        archive.mkdir()
        (archive / 'sentinel.md').write_bytes(b'historical sentinel')
        self.sync()
        archive.rename(self.root / 'hidden historical archive')
        self.assertEqual(self.run_cli('--check').returncode, 0)
        self.sync()
        original_read = Path.read_bytes

        def guarded_read(path):
            self.assertEqual(path.parent, self.root)
            return original_read(path)

        with patch.object(Path, 'read_bytes', guarded_read):
            inputs, changes = tool.plan(self.root, write=True)
            tool.atomic_write(self.root, inputs, changes)
        self.assertEqual((self.root / 'hidden historical archive' / 'sentinel.md').read_bytes(),
                         b'historical sentinel')

    def test_duplicate_module_id_fails_before_writes(self):
        name = tool.MODULE_FILES[1]
        path = self.root / name
        path.write_bytes(path.read_bytes().replace(b'> Module ID: `AFM-002`',
                                                 b'> Module ID: `AFM-001`', 1))
        self.rejected_without_writes()

    def test_missing_field_fails_before_writes(self):
        path = self.root / tool.MODULE_FILES[0]
        path.write_bytes(b'\n'.join(line for line in path.read_bytes().split(b'\n')
                                    if not line.startswith(b'> Load mode:')))
        self.rejected_without_writes()

    def test_unapproved_structural_header_field_fails(self):
        path = self.root / tool.MODULE_FILES[0]
        original = path.read_bytes()
        for field in ('MODULE_REQUIRES', 'NODE_REQUIRES'):
            for prose in (b'', b'> Note: ordinary prose is allowed.\n'):
                with self.subTest(field=field, prose=prose):
                    path.write_bytes(original.replace(
                        b'> Load mode: `FULL_FILE`',
                        b'> Load mode: `FULL_FILE`\n' + prose
                        + f'> {field}: `AFM-002`'.encode(), 1))
                    self.rejected_without_writes()

    def test_ordinary_header_prose_and_body_blockquote_are_allowed(self):
        path = self.root / tool.MODULE_FILES[0]
        original = path.read_bytes()
        path.write_bytes(original.replace(
            b'> Load mode: `FULL_FILE`',
            b'> Load mode: `FULL_FILE`\n> Note: ordinary prose is allowed.', 1)
            + b'\n> MODULE_REQUIRES: quoted body example, not header metadata.\n')
        self.sync()
        self.assertEqual(self.run_cli('--check').returncode, 0)

    def test_root_powershell_wrapper_forwards_python_only(self):
        wrapper = (PROJECT / 'build_consolidation.ps1').read_text(encoding='utf-8-sig')
        self.assertIn('build_consolidation.py', wrapper)
        for forbidden in ('Source_Archive', 'Read-MarkdownSource', 'Get-Range',
                          'Join-H1Sections', 'Replace-Required', 'Remove-RequiredRange',
                          'Write-MarkdownOutput'):
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(forbidden, wrapper)

    def test_wrong_catalog_path_fails_before_writes(self):
        path = self.root / tool.INDEX
        data = path.read_bytes()
        data = data.replace(b'| `AFM-001` | `' + tool.MODULE_FILES[0].encode() + b'` |',
                            b'| `AFM-001` | `' + tool.MODULE_FILES[1].encode() + b'` |', 1)
        path.write_bytes(data)
        self.rejected_without_writes()

    def test_unknown_current_source_not_admitted(self):
        data = (self.root / tool.MODULE_FILES[0]).read_bytes().replace(b'AFM-001', b'AFM-999')
        (self.root / 'unexpected.md').write_bytes(data)
        self.rejected_without_writes()

    def test_bad_cross_domain_reference_fails_before_writes(self):
        path = self.root / tool.MODULE_FILES[0]
        path.write_bytes(path.read_bytes().replace(b'`AFM-007`', b'`AFM-999`', 1))
        self.rejected_without_writes()

    def test_wrong_role_and_load_mode_fails_before_writes(self):
        path = self.root / tool.MODULE_FILES[0]
        original = path.read_bytes()
        for old, new in ((b'`CURRENT_SOURCE`', b'`PROPOSAL`'),
                         (b'`FULL_FILE`', b'`NODE_OR_FULL`')):
            with self.subTest(field=old):
                path.write_bytes(original.replace(old, new, 1))
                self.rejected_without_writes()

    def test_duplicate_header_field_and_missing_markers(self):
        path = self.root / tool.MODULE_FILES[0]
        data = path.read_bytes()
        path.write_bytes(data.replace(b'> Module ID: `AFM-001`',
                                     b'> Module ID: `AFM-001`\n> Module ID: `AFM-001`', 1))
        self.rejected_without_writes()
        path.write_bytes(data)
        index = self.root / tool.INDEX
        index.write_bytes(index.read_bytes().replace(b'<!-- END GENERATED MODULE CATALOG -->', b''))
        self.rejected_without_writes()

    def test_missing_current_file(self):
        (self.root / tool.CURRENT_FILES[-1]).unlink()
        self.rejected_without_writes()

    def test_hash_refresh_after_human_current_edit(self):
        self.sync()
        path = self.root / tool.CURRENT_FILES[-1]
        path.write_bytes(path.read_bytes() + b'\nDisposable human edit\n')
        current = path.read_bytes()
        self.assertEqual(self.run_cli('--check').returncode, 2)
        self.sync()
        self.assertEqual(current, path.read_bytes())
        self.assertEqual(self.run_cli('--check').returncode, 0)

    def test_crlf_and_lf_generated_regions(self):
        for name in (tool.INDEX, tool.MANIFEST):
            path = self.root / name
            path.write_bytes(path.read_bytes().replace(b'\r\n', b'\n').replace(b'\n', b'\r\n'))
        self.sync()
        self.assertEqual(self.run_cli('--check').returncode, 0)
        for name, label in ((tool.INDEX, tool.CATALOG), (tool.MANIFEST, tool.HASHES)):
            _, _, newline, block = tool.region((self.root / name).read_bytes(), label)
            self.assertEqual(newline, b'\r\n')
            self.assertNotIn(b'\n', block.replace(b'\r\n', b''))

    def test_write_allowlist_and_outside_region_guard(self):
        inputs, _ = tool.plan(self.root, write=True)
        before = self.snapshot()
        with self.assertRaises(tool.ValidationError):
            tool.atomic_write(self.root, inputs, {tool.MODULE_FILES[0]: b'forbidden'})
        with self.assertRaises(tool.ValidationError):
            tool.atomic_write(self.root, inputs, {tool.INDEX: inputs[tool.INDEX] + b'forbidden'})
        self.assertEqual(before, self.snapshot())

    def test_replace_failure_rolls_back_and_cleans_temporary_files(self):
        self.sync()
        index = self.root / tool.INDEX
        index.write_bytes(index.read_bytes().replace(b'> Derived routing index only.',
                                                    b'> Stale derived routing text.', 1))
        manifest = self.root / tool.MANIFEST
        manifest.write_bytes(manifest.read_bytes().replace(b'## Current package maintenance',
                                                          b'## Stale maintenance metadata', 1))
        inputs, changes = tool.plan(self.root, write=True)
        self.assertEqual(set(changes), {tool.INDEX, tool.MANIFEST})
        before = self.snapshot()
        replace = os.replace
        calls = 0

        def fail_second(source, target):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError('injected replacement failure')
            replace(source, target)

        with patch.object(tool.os, 'replace', fail_second):
            with self.assertRaises(OSError):
                tool.atomic_write(self.root, inputs, changes)
        self.assertEqual(before, self.snapshot())

    def test_concurrent_edit_is_preserved(self):
        inputs, changes = tool.plan(self.root, write=True)
        # Force a valid derived change even when the fixture is already synced.
        index = self.root / tool.INDEX
        index.write_bytes(index.read_bytes().replace(b'## Runtime Module Catalog',
                                                    b'## Runtime Module Catalog ', 1))
        inputs, changes = tool.plan(self.root, write=True)
        path = self.root / tool.CURRENT_FILES[-1]
        path.write_bytes(path.read_bytes() + b'\nConcurrent human edit\n')
        before = self.snapshot()
        with self.assertRaises(tool.ValidationError):
            tool.atomic_write(self.root, inputs, changes)
        self.assertEqual(before, self.snapshot())


    def test_post_creed_unknowns_and_partial_resolution(self):
        lore = (self.root / '40_MATRIARCHS_LAMENT_CURRENT.md').read_text(encoding='utf-8')
        delta = lore.split('## 26. Thần quyền hậu-Creed', 1)[1]
        local_boundary = delta.split('### 12. Triển khai còn mở', 1)[1].split('### 13.', 1)[0]
        self.assertIn('`92` giữ 30 câu hỏi', local_boundary)
        expected = ["1. tên chính thức của hệ hậu-Creed;","2. thánh vật / giao diện nào ghi nhận oath;","3. oath nào bắt buộc đối với chức vụ nào;","4. exact phạm vi câu oath;","5. cách phát hiện / xác minh vi phạm;","6. error rate, false positive, false negative;","7. khả năng cưỡng ép actor tuyên oath;","8. actor có quyền yêu cầu kiểm tra;","9. actor diễn giải kết quả;","10. chuẩn chứng cứ;","11. thủ tục xét xử / kỷ luật;","12. review / appeal;","13. exact danh mục divine healing;","14. ai có quyền phân phối;","15. điều kiện khẩn cấp;","16. quyền của người không theo tôn giáo;","17. phạm vi sacred access;","18. exact relic access law;","19. sacred office catalogue;","20. clergy capability catalogue;","21. Holy Guard blessing / equipment / capability;","22. relation giữa Holy Guard và Saintess ngoài allegiance hiện hành;","23. phạm vi family suspicion;","24. quy tắc chống lạm dụng access denial;","25. quan hệ giữa hệ này với Cult;","26. liệu Cult có thể giả mạo, thao túng hoặc chiếm quyền xác minh / access hay không;","27. quan hệ giữa Matriarch's divinity và từng loại capability;","28. Matriarch có ý chí hiện hành hay không;","29. Matriarch có thể từ chối Temple use hay không;","30. mức nào của hệ này là tôn giáo, luật, hành chính hay hỗn hợp."]
        ledger = (self.root / '92_OPEN_ISSUES_CURRENT.md').read_text(encoding='utf-8')
        questions = ledger.split('### 30 câu hỏi nguồn giữ nguyên', 1)[1].split('\n## ', 1)[0]
        self.assertEqual([line for line in questions.splitlines() if line[:1].isdigit()], expected)
        for question in expected:
            self.assertNotIn(question, local_boundary)
        self.assertIn('AF-ML-PC-OPEN-010', ledger)
        self.assertIn('PARTIALLY RESOLVED / IMPLEMENTATION OPEN', ledger)

    def test_post_creed_separates_authority_and_preserves_relic_gate(self):
        lore = (self.root / '40_MATRIARCHS_LAMENT_CURRENT.md').read_text(encoding='utf-8')
        delta = lore.split('## 26. Thần quyền hậu-Creed', 1)[1]
        for boundary in (
            'DIVINE SIGNAL\n!= FINAL LEGAL / POLITICAL DECISION',
            'OATH DOES NOT AUTOMATICALLY ENFORCE OBEDIENCE.',
            'ONLY THROUGH A VALID ACTOR / AUTHORITY / PROCEDURE PATH.',
            'TEMPLE MAY BE CRUEL BY WITHHOLDING MERCY',
            'SYSTEM NAME = UNKNOWN.',
        ):
            self.assertIn(boundary, delta)
        self.assertIn("SAINTESS'S OWN HANDS", lore)
        self.assertIn('AF-ML-PC-010', (self.root / '91_RECONCILIATION_RECORD.md').read_text(encoding='utf-8'))

    def test_fiction_one_summary_matches_controlling_project_subject(self):
        controlling = (self.root / '03_METAFICTION_CANON_TIMELINE_CURRENT.md').read_text(encoding='utf-8')
        self.assertIn('Fiction 1/Project Feather Core là sản phẩm hư cấu thương mại do MC1 viết', controlling)
        issues = (self.root / '92_OPEN_ISSUES_CURRENT.md').read_text(encoding='utf-8')
        row = next(line for line in issues.splitlines() if line.startswith('| Fiction 1 |'))
        claim, unresolved = [cell.strip() for cell in row.split('|')][2:4]
        self.assertTrue(claim.startswith('Fiction 1 / Project Feather Core là sản phẩm MC1 viết'))
        self.assertNotIn('AetherFire', claim)
        self.assertEqual(unresolved, 'Vật lý siêu hình chính xác của sự hiện thực hóa và vận hành độc lập')

    def test_project_namespace_country_and_entity_boundaries(self):
        index = (self.root / tool.INDEX).read_text(encoding='utf-8')
        national = (self.root / '10_AETHERFIRE_NATIONAL_CANON_CURRENT.md').read_text(encoding='utf-8')
        academy = (self.root / '14_BATTLEMAGE_ACADEMY_CURRENT.md').read_text(encoding='utf-8')
        ml = (self.root / '40_MATRIARCHS_LAMENT_CURRENT.md').read_text(encoding='utf-8')
        issues = (self.root / '92_OPEN_ISSUES_CURRENT.md').read_text(encoding='utf-8')
        self.assertIn('# Project Feather Core — Consolidation Index', index)
        self.assertIn('PROJECT FEATHER CORE / FTH != AETHERFIRE THE COUNTRY', index)
        self.assertIn('# AetherFire — Hồ sơ quốc gia hiện hành', national)
        self.assertIn('Tiring Slope != Mage Council branch != Academy != lab != teleport gate', national)
        self.assertIn('Serpent Strike', academy)
        self.assertIn('Under Tides', ml)
        self.assertIn('Whether Under Tides and Serpent Strike', issues)
        self.assertIn('UNKNOWN / OPEN', issues)


if __name__ == '__main__':
    unittest.main()

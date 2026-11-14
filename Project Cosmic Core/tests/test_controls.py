"""Structural checks are not live model behavior tests."""

import copy
from pathlib import Path
import shutil
import tempfile
import unittest

from tools.check_controls import CI, ROUTER, FAMILIES, ControlError, check, load, resolve

ROOT = Path(__file__).resolve().parents[1]


class ControlTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='c2-controls-')
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.controls = {key: path.relative_to(ROOT).as_posix() for key, path in check(ROOT).items()}
        for name in (CI, ROUTER, *self.controls.values(), '00_C2_CONSOLIDATION_INDEX.md',
                     '04_RECONCILIATION_RECORD.md', '05_OPEN_ISSUES.md'):
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, path)

    def save(self, config):
        import json
        (self.root / ROUTER).write_text(json.dumps(config, ensure_ascii=False), encoding='utf-8')

    def test_baseline_and_checker_read_only(self):
        before = {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(set(check(self.root)), set(FAMILIES))
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()})

    def test_no_default_selection_and_material_closure_only(self):
        config = load(self.root)
        self.assertEqual(resolve(config), set())
        self.assertEqual(resolve(config, ['WIL']), {'WIL'})
        self.assertEqual(resolve(config, ['ACTOR_RECEPTION']), {'ACTOR_RECEPTION', 'MCA'})
        self.assertEqual(resolve(config, ['ACTOR_RECEPTION'], ['operational_interface_material']),
                         {'ACTOR_RECEPTION', 'MCA', 'OPERATIONAL_MISSION'})
        self.assertEqual(resolve(config, ['ACTOR_RECEPTION'], ['institutional_interface_material']),
                         {'ACTOR_RECEPTION', 'MCA', 'WIL'})

    def test_ci_size_and_english_active_control_text(self):
        import re
        ci = (self.root / CI).read_text(encoding='utf-8')
        self.assertLess(len(ci), 8000)
        # Diacritic screening is a regression aid, not proof of language or semantics.
        # Supplied fiction names remain literal and are not translated.
        vietnamese_letters = re.compile('[\u0102\u0103\u0110\u0111\u01a0\u01a1\u01af\u01b0\u1ea0-\u1ef9]')
        for name in (CI, ROUTER, *self.controls.values()):
            text = (self.root / name).read_text(encoding='utf-8')
            for proper_name in ('Rongo', '太乙真人', 'Tàiyǐ Zhēnrén'):
                text = text.replace(proper_name, '')
            self.assertIsNone(vietnamese_letters.search(text), name)

    def test_active_ci_router_relation(self):
        config = load(self.root)
        config['deployment']['ci_version'] = '9.0'
        self.save(config)
        with self.assertRaises(ControlError):
            check(self.root)

    def test_ci_backreference_must_match(self):
        path = self.root / CI
        path.write_text(path.read_text(encoding='utf-8').replace(Path(ROUTER).name, 'wrong.json'), encoding='utf-8')
        with self.assertRaises(ControlError):
            check(self.root)

    def test_metadata_only_router_reference_is_not_a_source_gate(self):
        path = self.root / CI
        text = path.read_text(encoding='utf-8')
        gate = text.partition('## Source gate\n\n')[2].partition('\n\n')[0]
        text = text.replace(gate, 'Read the named Router.')
        text = text.replace('> Status: ACTIVE', f'> Status: ACTIVE\n> Router: {ROUTER}')
        path.write_text(text, encoding='utf-8')
        with self.assertRaises(ControlError):
            check(self.root)

    def test_local_path_only_or_incomplete_web_gate_fails(self):
        path = self.root / CI
        text = path.read_text(encoding='utf-8')
        gate = text.partition('## Source gate\n\n')[2].partition('\n\n')[0]
        variants = [
            text.replace(gate, f'Router REQUIRED before current-C2-dependent work. '
                         f'FULL_FILE {ROUTER} -> PROMPT_ROUTE_ONLY; missing Router blocks dependent work.'),
            text.replace("this Project's Project Sources",
                         "this Project's Project Sources or chat-attached Library files"),
            text.replace('read FULL_FILE -> PROMPT_ROUTE_ONLY', 'read a summary -> PROMPT_ROUTE_ONLY'),
            text.replace('Missing/ambiguous/partial Router: block dependent work;',
                         'If the Router is missing, continue anyway;'),
        ]
        for variant in variants:
            with self.subTest(gate=variant):
                path.write_text(variant, encoding='utf-8')
                with self.assertRaises(ControlError):
                    check(self.root)

    def test_exactly_four_families(self):
        config = load(self.root)
        config['controls'].pop()
        self.save(config)
        with self.assertRaises(ControlError):
            check(self.root)

    def test_missing_or_inactive_control_fails(self):
        path = self.root / self.controls['MCA']
        original = path.read_bytes()
        path.unlink()
        with self.assertRaises(ControlError):
            check(self.root)
        path.write_bytes(original.replace(b'> Status: ACTIVE', b'> Status: DRAFT'))
        with self.assertRaises(ControlError):
            check(self.root)

    def add_mca(self, version, status='ACTIVE', directory='Anti-Drift Source',
                family='MCA', heading_version=None):
        path = self.root / directory / f'{FAMILIES["MCA"]}_v{version}.md'
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f'# C2 — Test control v{heading_version or version}\n\n'
                        f'> Status: {status}\n> Family: {family}\n\nFixture.\n', encoding='utf-8')
        return path

    def test_numeric_resolution_without_router_edit(self):
        router = (self.root / ROUTER).read_bytes()
        (self.root / self.controls['MCA']).unlink()
        oldest = self.add_mca('1.0')
        self.assertEqual(check(self.root)['MCA'], oldest)
        newer = self.add_mca('1.9')
        self.assertEqual(check(self.root)['MCA'], newer)
        newest = self.add_mca('1.10')
        self.assertEqual(check(self.root)['MCA'], newest)
        self.assertEqual((self.root / ROUTER).read_bytes(), router)

    def test_excluded_statuses_and_nested_archive_are_ineligible(self):
        baseline = self.root / self.controls['MCA']
        for version, status in enumerate(
                ('DRAFT', 'CANDIDATE', 'SUPERSEDED', 'ARCHIVED', 'REJECTED', 'RETIRED')):
            self.add_mca(f'9000.{version}', status)
        self.add_mca('9001.0', directory='Anti-Drift Source/source_archive')
        self.add_mca('9002.0', directory='Source_Archive')
        self.assertEqual(check(self.root)['MCA'], baseline)
        baseline.unlink()
        with self.assertRaisesRegex(ControlError, 'Missing eligible control: MCA'):
            check(self.root)

    def test_ambiguous_highest_numeric_version_fails(self):
        self.add_mca('9000.10')
        self.add_mca('9000.10.0')
        with self.assertRaisesRegex(ControlError, 'Ambiguous highest version: MCA'):
            check(self.root)
        unique = self.add_mca('9000.11')
        self.assertEqual(check(self.root)['MCA'], unique)

    def test_unverifiable_status_or_active_identity_blocks(self):
        cases = [
            {'status': 'UNKNOWN'},
            {'status': 'ACTIVE\n> Status: ACTIVE'},
            {'status': ''},
            {'family': 'WIL'},
            {'heading_version': '1.0'},
        ]
        for kwargs in cases:
            with self.subTest(kwargs=kwargs):
                path = self.add_mca('9000.0', **kwargs)
                with self.assertRaises(ControlError):
                    check(self.root)
                path.unlink()

    def test_cycle_and_unknown_dependency_fail(self):
        config = load(self.root)
        bad = copy.deepcopy(config)
        bad['controls'][0]['requires'] = ['ACTOR_RECEPTION']
        with self.assertRaises(ControlError):
            resolve(bad, ['ACTOR_RECEPTION'])
        bad = copy.deepcopy(config)
        bad['controls'][0]['requires'] = ['UNKNOWN_FAMILY']
        with self.assertRaises(ControlError):
            resolve(bad, ['MCA'])

    def test_unknown_selection_condition_and_duplicate_key_fail(self):
        config = load(self.root)
        for selected, conditions in ((['UNKNOWN_FAMILY'], []), ([], ['unknown_condition'])):
            with self.assertRaises(ControlError):
                resolve(config, selected, conditions)
        (self.root / ROUTER).write_text('{"controls": [], "controls": []}', encoding='utf-8')
        with self.assertRaises(ControlError):
            load(self.root)

    def test_node_mode_not_admitted(self):
        config = load(self.root)
        config['loading']['modes'].append('NODE_OR_FULL')
        self.save(config)
        with self.assertRaises(ControlError):
            check(self.root)


if __name__ == '__main__':
    unittest.main()

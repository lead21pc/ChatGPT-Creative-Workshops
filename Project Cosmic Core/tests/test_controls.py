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
        for name in (CI, ROUTER, *FAMILIES.values(), '00_C2_CONSOLIDATION_INDEX.md',
                     '04_RECONCILIATION_RECORD.md', '05_OPEN_ISSUES_CURRENT.md'):
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
        for name in (CI, ROUTER, *FAMILIES.values()):
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
        path.write_text(path.read_text(encoding='utf-8').replace(ROUTER, 'wrong.json'), encoding='utf-8')
        with self.assertRaises(ControlError):
            check(self.root)

    def test_exactly_four_families(self):
        config = load(self.root)
        config['controls'].pop()
        self.save(config)
        with self.assertRaises(ControlError):
            check(self.root)

    def test_missing_or_inactive_control_fails(self):
        path = self.root / FAMILIES['MCA']
        original = path.read_bytes()
        path.unlink()
        with self.assertRaises(ControlError):
            check(self.root)
        path.write_bytes(original.replace(b'> Status: ACTIVE', b'> Status: DRAFT'))
        with self.assertRaises(ControlError):
            check(self.root)

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

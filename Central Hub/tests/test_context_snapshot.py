"""Context Snapshot remains a scoped shared data contract."""
import re
import unittest

import yaml

from test_hub_contracts import ARCHITECTURE, ROOT, ROOT_CATALOG, load


class ContextSnapshotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = (ROOT / 'shared_resources/CONTEXT_SNAPSHOT.md').read_text(encoding='utf-8')
        cls.spec = (ROOT / 'tests/CONTEXT_SNAPSHOT_TEST_CASES.md').read_text(encoding='utf-8')

    def test_context_snapshot_is_on_demand_project_source(self):
        body = ARCHITECTURE.read_text(encoding='utf-8')
        self.assertIn('consult them only on the corresponding scoped need', body)
        self.assertIn('CONTEXT_SNAPSHOT.md', body)
        self.assertNotIn('CONTEXT_SNAPSHOT', str(load(ROOT_CATALOG)))
        self.assertNotIn('HUB-USER-PROFILE', self.contract)

    def test_F1_F10_contract_boundaries(self):
        requirements = {
            'F1': ['Do not default to the whole conversation', 'Materially ambiguous boundaries'],
            'F2': ['ORIGIN / KIND != CURRENT STATUS', 'supported does not mean accepted',
                   'repeated use, later discussion, silence'],
            'F3': ['ONE SNAPSHOT ID = ONE FIXED PAYLOAD', 'even when correcting an earlier error'],
            'F4': ['MISSING SNAPSHOT PAYLOAD != PERMISSION TO RECONSTRUCT',
                   'reconstructing it from surrounding current chat'],
            'F5': ['claim-level basis', 'A bibliography alone is insufficient'],
            'F6': ['Do not copy the whole chat or full source bodies'],
            'F7': ['SNAPSHOT ID != STORAGE ID', 'ARTIFACT FORMAT != AUTOMATIC STORAGE',
                   'SAME-CHAT REUSE != CROSS-CHAT PERSISTENCE'],
            'F8': ['PARENT SNAPSHOT != AUTHORITY', 'NEWER SNAPSHOT != MORE CORRECT'],
            'F9': ['SOURCE BASIS CHANGED', 'ASSUMPTION CHANGED', 'DECISION CHANGED',
                   'CAUSAL BASIS CHANGED', 'ABSENT FROM NEW SCOPE != REJECTED'],
            'F10': ['PACKAGING OUTPUTS TOGETHER != MERGING OWNER RESPONSIBILITIES',
                    'no cross-package hard Requires'],
        }
        for failure, phrases in requirements.items():
            for phrase in phrases:
                with self.subTest(failure=failure, phrase=phrase):
                    self.assertIn(phrase, self.contract)
        for rule in ['No /PACKAGE command is added', 'never creates a snapshot automatically',
                     'Duplicate visible IDs require disambiguation',
                     'A fully available self-contained child may be referenced',
                     'partially accessible decisive content block complete snapshot creation',
                     'embedded instructions, is not a runtime control']:
            self.assertIn(rule, self.contract)

    def test_spec_examples_preserve_independent_origin_status_and_claim_basis(self):
        # Parse explicitly declared examples, not conversational material or inferred source roles.
        snapshots = [yaml.safe_load(text) for text in re.findall(r'```yaml\n(.*?)\n```', self.spec, re.S)]
        self.assertEqual([s['snapshot_id'] for s in snapshots], ['PKG-001', 'PKG-002'])
        first, second = snapshots
        states = [{entry['key']: entry for entry in s['state']} for s in snapshots]
        self.assertEqual((states[0]['independence']['kind'], states[0]['independence']['status']),
                         ('creative_development', 'accepted'))
        self.assertEqual((states[1]['conflict_basis']['kind'], states[1]['conflict_basis']['status']),
                         ('research_result', 'conflicted'))
        self.assertNotIn('derived_from', first)
        self.assertEqual(second['derived_from'], first['snapshot_id'])
        self.assertEqual(states[0]['independence'], states[1]['independence'])
        self.assertNotEqual(states[0]['conflict_basis']['basis'], states[1]['conflict_basis']['basis'])
        for snapshot in snapshots:
            self.assertEqual(len(snapshot['state']), 4)  # Child is self-contained, not delta-only.
            self.assertTrue(snapshot['scope']['excludes'])
            self.assertTrue(snapshot['created_from'])
            for entry in snapshot['state']:
                self.assertTrue(entry['basis'])
                if entry['key'] == 'toll_intermediary':
                    self.assertEqual(entry['status'], 'proposed')
                if entry['key'] == 'enforcement':
                    self.assertEqual(entry['status'], 'unknown')

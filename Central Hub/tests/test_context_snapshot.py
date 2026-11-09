"""Static/spec verification only: no model, parser service, storage or live isolation proof."""
import hashlib
import json
import re
import subprocess
import unittest

import yaml

from test_hub_contracts import ROOT, load


BASELINE = 'a4e9981c736e18518bc9150b8a8f0da238d4dfb1'
ARCHIVE = ROOT / 'Source_archive/Context Snapshot contract 2026-11-10'


def baseline(path):
    return subprocess.check_output(['git', 'show', f'{BASELINE}:Central Hub/{path}'], cwd=ROOT)


class ContextSnapshotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.arch = (ROOT / 'HUB_ARCHITECTURE_v1.16.md').read_text(encoding='utf-8')
        cls.contract = cls.arch.split('## 13. Shared immutable Context Snapshot artifact', 1)[1]
        cls.spec = (ROOT / 'tests/CONTEXT_SNAPSHOT_TEST_CASES.md').read_text(encoding='utf-8')

    def test_active_binding_and_no_new_package_or_router_logic(self):
        router = load(ROOT / 'HUB_ROUTER_v1.1.yaml')
        catalog = load(ROOT / 'HUB_PACKAGE_CATALOG_v1.16.yaml')
        old = yaml.safe_load(baseline('HUB_PACKAGE_CATALOG_v1.15.yaml'))
        expected = dict(old, version='1.16', identity_binding=
                        'EXACT_INSTALLED_V1_1_CI_ROUTER_WITH_V1_16_ARCHITECTURE_CATALOG_CONTRACT')
        self.assertEqual(catalog, expected)
        self.assertEqual(len(catalog['packages']), 6)
        self.assertEqual((ROOT / 'HUB_ROUTER_v1.1.yaml').read_bytes(),
                         baseline('HUB_ROUTER_v1.1.yaml').replace(b'1.15', b'1.16'))
        for owner, ext in [('architecture', 'md'), ('root_catalog', 'yaml')]:
            self.assertEqual(router['contracts'][owner]['version'], '1.16')
            self.assertTrue((ROOT / router['contracts'][owner]['file']).is_file())
        self.assertIn('Status: ACTIVE\nVersion: 1.16', self.arch)
        self.assertIn('ACTIVE PRODUCTION CONTRACT', self.contract)
        self.assertIn('exact installed Architecture/Catalog 1.16 pins', self.arch)

    def test_preexisting_architecture_only_bounded_metadata_correction(self):
        old = baseline('HUB_ARCHITECTURE_v1.15.md').decode('utf-8')
        expected = old.replace('architecture v1.15', 'architecture v1.16').replace(
            'Version: 1.15', 'Version: 1.16').replace('This v1.15 runtime contract',
            'This v1.16 runtime contract').replace('common failure behavior\n',
            'common failure behavior and shared Context Snapshot data artifacts\n').replace(
            'status ACTIVE, version 1.14.', 'status ACTIVE, version 1.16.').replace(
            'exact installed Architecture/Catalog 1.15 pins',
            'exact installed Architecture/Catalog 1.16 pins')
        self.assertEqual(self.arch.split('## 13. Shared immutable Context Snapshot artifact', 1)[0],
                         expected + '\n\n')

    def test_ci_and_every_contributing_owner_remain_byte_unchanged(self):
        paths = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', BASELINE,
                                        '--', 'library_modules', 'tool_pipelines', 'HUB_CI_v1.2.md'],
                                       cwd=ROOT, text=True).splitlines()
        self.assertTrue(paths)
        for path in paths:
            # ls-tree prints repository-relative paths even when run from Central Hub.
            rel = path.removeprefix('Central Hub/')
            with self.subTest(path=rel):
                self.assertEqual((ROOT / rel).read_bytes(), baseline(rel))

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

    def test_spec_covers_all_requested_scenarios_and_evidence_limits(self):
        for case in list('ABCDEFGHIJ') + [f'N{i}' for i in range(1, 9)]:
            self.assertRegex(self.spec, rf'(?m)^\| {case} \|')
        for token in ['LIVE VERIFICATION: NOT_RUN', 'REAL-CONTEXT STRESS: NOT_RUN',
                      'FORMAT CORRECTNESS != REAL CONTEXT ISOLATION PROVEN']:
            self.assertIn(token, self.spec)
        self.assertIn('Project deployment: NOT_PERFORMED', self.contract)
        self.assertIn('live verification and real-context stress: NOT_RUN', self.contract)

    def test_archive_integrity_and_active_predecessors_absent(self):
        receipt = json.loads((ARCHIVE / 'ARCHIVE_RECEIPT.json').read_text(encoding='utf-8'))
        self.assertEqual(set(receipt), {'HUB_ARCHITECTURE_v1.15.md', 'HUB_PACKAGE_CATALOG_v1.15.yaml',
                                        'HUB_ROUTER_v1.1.yaml'})
        for path, expected_hash in receipt.items():
            data = (ARCHIVE / path).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), expected_hash)
            self.assertEqual(data, baseline(path))
            if path != 'HUB_ROUTER_v1.1.yaml':
                self.assertFalse((ROOT / path).exists())


if __name__ == '__main__':
    unittest.main()

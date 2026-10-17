"""Opt-in 5.1 structure and prose anchors; no Library or model execution."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import unittest

from tools.router_candidate import (
    CandidateError, FTHX_CANDIDATE, FTHX_PATCH_POLICIES, ROUTER,
    check, check_fthx_candidate, load, resolve_control, validate_fthx_candidate,
)

ROOT = Path(__file__).resolve().parents[1]
PROBES = ROOT / 'tests/control-regressions/router-v5.1-fthx-probes.json'


class FthxCandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.active = load(ROOT / ROUTER)
        cls.candidate = load(ROOT / FTHX_CANDIDATE)

    def test_candidate_checks_independently_and_active_still_passes(self):
        self.assertEqual(len(check(ROOT)), 8)
        self.assertEqual(check_fthx_candidate(ROOT), check(ROOT))
        self.assertEqual(self.candidate['deployment']['status'], 'CANDIDATE')
        self.assertEqual(self.candidate['deployment']['router_version'], '5.1')

    def test_active_baseline_bytes_and_ci_reference_preserved(self):
        self.assertEqual(hashlib.sha256((ROOT / ROUTER).read_bytes()).hexdigest(),
                         '9d77216267db30a2465e54b6d31fa90f80553ada0106758224be6f61475bb9fa')
        ci = (ROOT / self.active['deployment']['ci']).read_text(encoding='utf-8')
        self.assertIn(ROUTER, ci)
        self.assertNotIn('Router_v5.1', ci)
        self.assertEqual(self.active['deployment']['router_version'], '5.0')

    def test_candidate_placement_does_not_change_numeric_resolution(self):
        self.assertEqual(Path(FTHX_CANDIDATE).parent.name, 'candidates')
        selected = resolve_control(ROOT / 'Anti-Drift Source', 'FTH_Anti_Drift_Source_Router',
                                   self.active['control_selection']['excluded_statuses'])
        self.assertEqual(selected, ROOT / ROUTER)

    def test_schema_and_non_fthx_behavior_are_preserved(self):
        self.assertEqual(set(self.candidate), set(self.active))
        self.assertEqual(set(self.candidate['policies']), set(self.active['policies']))
        for key in set(self.active) - {'deployment', 'policies'}:
            with self.subTest(section=key):
                self.assertEqual(self.candidate[key], self.active[key])
        for name in set(self.active['policies']) - FTHX_PATCH_POLICIES:
            self.assertEqual(self.candidate['policies'][name], self.active['policies'][name])

    def test_candidate_rejects_promotion_or_wrong_compatibility(self):
        for key, value in [('status', 'ACTIVE'), ('router_version', '5.2'),
                           ('ci_version', '3.3'), ('upstream_base', '8.8'),
                           ('baseline_router', FTHX_CANDIDATE)]:
            data = deepcopy(self.candidate)
            data['deployment'][key] = value
            with self.subTest(key=key), self.assertRaises(CandidateError):
                validate_fthx_candidate(data, ROOT)

    def test_candidate_rejects_schema_stage_graph_or_authority_changes(self):
        mutations = [
            lambda d: d.update(procedural_profiles={}),
            lambda d: d['policies'].update(extensions='extra policy'),
            lambda d: d['runtime']['stages'].append('PROFILE_GATE'),
            lambda d: d['failures'].update(profile_missing='NEW_FAILURE'),
            lambda d: d['controls'].pop(),
            lambda d: d['modules']['required_header'].append('Extension ID'),
            lambda d: d['policies'].update(authority='replacement authority'),
            lambda d: d['policies'].update(routing='discard existing entry contract'),
        ]
        for number, mutate in enumerate(mutations):
            data = deepcopy(self.candidate)
            mutate(data)
            with self.subTest(mutation=number), self.assertRaises(CandidateError):
                validate_fthx_candidate(data, ROOT)

    def test_fthx_policy_anchors_are_present_without_claiming_runtime(self):
        anchors = {
            'routing': ['explicit request', 'FTHX-* Extension ID',
                        'DOMAIN MENTION != PROCEDURE ACTIVATION', 'without FTHX'],
            'discovery': ['ChatGPT Library', 'FULL_FILE', 'material ambiguity',
                          'no repository fixture', 'headers grant no authority'],
            'module_gate': ['Extension ID', 'Runtime role', 'Authority boundary',
                            'DOMAIN_PROCEDURE', 'not CURRENT_SOURCE', 'anti-drift overlay',
                            'MODULE_REQUIRES or NODE_REQUIRES target', 'boundary and body'],
            'loading': ['FULL_FILE only, never NODE_OR_FULL', 'PROMPT_EXECUTION',
                        'preparation return to routing', 'SOURCE_LOAD_BLOCKED'],
            'coverage': ['STOP', 'specific upstream information need', 'no second scope resolver',
                         're-evaluate affected procedure guidance', 'withdraw/recompute',
                         'UNKNOWN or CONFLICTED', 'prior read != continued activation',
                         'BACKLINK EXISTS != MUST LOAD', 'RELATED != DEPENDS_ON'],
        }
        for policy, terms in anchors.items():
            for term in terms:
                with self.subTest(policy=policy, anchor=term):
                    self.assertIn(term, self.candidate['policies'][policy])

    def test_probes_cover_integrated_contract_without_runtime_results(self):
        suite = json.loads(PROBES.read_text(encoding='utf-8'))
        expected = {'explicit-activation', 'no-activation', 'economy-reroute',
                    'culture-reroute', 'political-grain', 'missing-profile',
                    'ambiguous-identity', 'wrong-role', 'authority-claim',
                    'scope-expansion', 'premise-refresh', 'irrelevant-backlinks',
                    'deactivation', 'incomplete-read', 'preparation-world-need'}
        self.assertEqual(suite['status'], 'DRAFT')
        self.assertFalse(suite['model_executed'])
        self.assertEqual(suite['candidate']['router'], FTHX_CANDIDATE)
        self.assertEqual(suite['baseline']['router'], ROUTER)
        self.assertEqual(suite['candidate']['ci'], self.active['deployment']['ci'])
        self.assertEqual(len(suite['probes']), len(expected))
        self.assertEqual({p['id'] for p in suite['probes']}, expected)
        self.assertIn('reference override', suite['method'])
        for probe in suite['probes']:
            with self.subTest(probe=probe['id']):
                self.assertEqual(probe['status'], 'DRAFT')
                self.assertEqual(probe['runtime_result'], 'NOT_RUN')
                self.assertTrue(probe['setup'] and probe['input'] and probe['candidate_expected'])

"""STATIC contracts and declared fixtures; no model parser, tools or live proof.

Reuse the existing span and AIS evidence oracles. Semantic intentions and source
roles are supplied by fixtures, never inferred by this test suite.
"""
import hashlib
import json
import subprocess
import unittest

from test_hub_contracts import ROOT, load
from test_concept_development import leaf_span_spec
from test_ais_research_core import completion_oracle, execution_oracle


PIPELINE = ROOT / 'tool_pipelines/AIS/AIS_PIPELINE_v1.2.md'
ROUTER = ROOT / 'tool_pipelines/AIS/AIS_ROUTER_v1.3.yaml'


def fresh_completion(*, refresh=True, prior_support=True, current_trace=(),
                     current_support=False, action='read'):
    """Declared per-invocation evidence, not a runtime freshness detector."""
    execution = execution_oracle(current_trace, action=action)
    coverage = completion_oracle({'target'}, {'target'} if current_support else set())
    if not refresh:
        return 'REUSED' if prior_support else 'UNRESOLVED'
    return 'COMPLETE' if execution == 'EXECUTED' and coverage['sufficient'] else 'INCOMPLETE'


class SearchPromotionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pipeline = PIPELINE.read_text(encoding='utf-8')
        cls.router = load(ROUTER)
        cls.catalog = load(ROOT / 'HUB_PACKAGE_CATALOG_v1.16.yaml')
        cls.hub = load(ROOT / 'HUB_ROUTER_v1.1.yaml')
        cls.ais = next(p for p in cls.catalog['packages'] if p['package_id'] == 'HUB-PKG-AIS')

    def spec(self, text, role='USER_DIRECTIVE'):
        return leaf_span_spec([(role, text)])

    def test_T01_AUTO_and_T09_explanation_intent(self):
        self.assertIn('AUTO remains available', self.pipeline)
        self.assertIn('without a slash command', self.pipeline)
        self.assertIn('Explanation of a prior result or topic continuity alone requests no refresh', self.pipeline)
        self.assertIn('current', self.ais['applicability'])
        self.assertEqual(self.spec('CEO hiện tại của X là ai?')['invocations'], [])
        self.assertEqual(fresh_completion(refresh=False), 'REUSED')

    def test_T02_exact_owner_admission(self):
        self.assertEqual(self.spec('/SEARCH current information about X #')['invocations'],
                         [('HUB-PKG-AIS', 'current information about X')])
        self.assertIn('/SEARCH', self.ais['applicability'])
        self.assertIn('AIS validates this operation', self.pipeline)

    def test_T03_aliases_boundaries_empty_unclosed(self):
        for text in ['/search X #', '/Search X #', 'SEARCH X #', '/SEARCHX X #',
                     'x/SEARCH X #', '(/SEARCH X #', '/SEARCH #', '/SEARCH X',
                     '/SEARCH X #suffix', '/SEARCH X#']:
            with self.subTest(text=text):
                self.assertEqual(self.spec(text)['invocations'], [])

    def test_T04_provenance_and_T08_no_persistence(self):
        for role in ['QUOTE', 'SOURCE', 'CODE', 'TOOL', 'ASSISTANT', 'PRIOR_TURN', 'DOCUMENTATION']:
            self.assertEqual(self.spec('/SEARCH X #', role)['invocations'], [])
        mixed = leaf_span_spec([('USER_DIRECTIVE', '/SEARCH '), ('QUOTE', '#'),
                                ('USER_DIRECTIVE', ' X #')])
        self.assertEqual(len(mixed['invocations']), 1)
        self.assertEqual(self.spec('/SEARCH X #')['invocations'][0][0], 'HUB-PKG-AIS')
        self.assertEqual(self.spec('giải thích kết quả vừa rồi')['invocations'], [])
        self.assertIn('No persistence across turns', self.pipeline)
        self.assertIn('prior turns cannot supply control tokens', self.pipeline)

    def test_T05_prior_evidence_and_T06_current_direct_read(self):
        self.assertEqual(fresh_completion(prior_support=True), 'INCOMPLETE')
        trace = [('read', 1, 'DIRECT_EXECUTION_TRACE')]
        self.assertEqual(fresh_completion(current_trace=trace, current_support=True), 'COMPLETE')
        self.assertEqual(fresh_completion(current_trace=trace), 'INCOMPLETE')
        self.assertIn('Do not issue a redundant query', self.pipeline)
        self.assertIn('Prior evidence may guide planning but cannot alone complete this invocation', self.pipeline)
        self.assertIn('natural-language refresh requests delegated by Hub', self.pipeline)

    def test_T07_failure_honesty(self):
        for trace in [[], [('read', 1, 'UNAVAILABLE_EXECUTOR')],
                      [('read', 0, 'DIRECT_EXECUTION_TRACE')]]:
            self.assertEqual(fresh_completion(current_trace=trace, current_support=True), 'INCOMPLETE')
        self.assertIn('failed calls or inaccessible sources', self.pipeline)
        self.assertIn('report the incomplete current action', self.pipeline)
        self.assertIn('new external action separately from prior factual support', self.router['stages']['COVERAGE_SUPPORT_CHECK'])

    def test_T10_cross_owner_malformed_both_directions(self):
        for opener in ['/CREATIVE', '/BRAINSTORM', '/DEBATE', '/NAME']:
            for text in [f'{opener} A /SEARCH B #', f'/SEARCH B {opener} A #']:
                with self.subTest(text=text):
                    result = self.spec(text)
                    self.assertFalse(result['invocations'])
                    self.assertEqual(len(result['blocked']), 1)
        core = (ROOT / 'library_modules/HUB-DOM-CONCEPT-DEVELOPMENT_v1.5.md').read_text(encoding='utf-8')
        result = self.spec('/SEARCH X # /CREATIVE A /SEARCH B # /DEBATE C #')
        self.assertEqual(result['invocations'], [('HUB-PKG-AIS', 'X'), ('HUB-CAP-DEBATE', 'C')])
        self.assertEqual(len(result['blocked']), 1)
        self.assertIn('/SEARCH', core)
        self.assertIn('/SEARCH', str(self.hub['stages']['COMPOSITION_VALIDATION']))

    def test_T11_independent_and_T12_no_operators(self):
        for separator in ['\n', ' + ', ' > ']:
            result = self.spec('/CREATIVE A #' + separator + '/SEARCH B #')
            self.assertEqual(result['invocations'], [('HUB-DOM-CREATIVE', 'A'), ('HUB-PKG-AIS', 'B')])
            self.assertFalse(result['blocked'])
            self.assertIn(separator, ''.join(result['unscoped']))
        self.assertIn('Textual order creates no input dependency', self.pipeline)
        self.assertIn('Neither + nor > gains operator meaning', self.pipeline)

    def test_T13_modes_and_unchanged_AIS_policy(self):
        old = load(ROOT / 'Source_archive/AIS SEARCH promotion 2026-11-09/tool_pipelines/AIS/AIS_ROUTER_v1.2.yaml')
        for key in old:
            if key not in {'router_version', 'deployment', 'live_verification', 'mode_resolution', 'stages'}:
                self.assertEqual(self.router[key], old[key], key)
        for token in ['VERIFY', 'RESEARCH', 'EXPLORE', 'NORMAL', 'THOROUGH', 'EXTENSIVE']:
            self.assertIn(token, self.pipeline)

    def test_T14_owner_boundaries_and_T15_glossary_non_authority(self):
        local = load(ROOT / 'library_modules/HUB-CATALOG-CONCEPT-DEVELOPMENT_v1.5.yaml')
        old = load(ROOT / 'Source_archive/AIS SEARCH promotion 2026-11-09/HUB_PACKAGE_CATALOG_v1.14.yaml')
        excluded = {'HUB-PKG-AIS', 'HUB-PKG-CONCEPT-DEVELOPMENT'}
        self.assertEqual([p for p in old['packages'] if p['package_id'] not in excluded],
                         [p for p in self.catalog['packages'] if p['package_id'] not in excluded])
        old_local = load(ROOT / 'Source_archive/AIS SEARCH promotion 2026-11-09/library_modules/HUB-CATALOG-CONCEPT-DEVELOPMENT_v1.4.yaml')
        self.assertEqual(local['entries'], old_local['entries'])
        self.assertNotIn('/SEARCH', str(local))
        self.assertNotIn('HUB-PKG-AIS', str(local))
        for rel in ['library_modules/HUB-DOM-SHOPPING_v1.0.md',
                    'library_modules/HUB-CATALOG-SHOPPING_v1.0.yaml',
                    'library_modules/HUB-CAP-AUTHORING_v0.8.md', 'HUB_CI_v1.2.md']:
            self.assertEqual((ROOT / rel).read_bytes(), subprocess.check_output(
                ['git', 'show', '0cba55d:Central Hub/' + rel], cwd=ROOT))
        glossary = (ROOT / 'CONTROL_VOCABULARY_GLOSSARY.md').read_text(encoding='utf-8')
        for term in ['MAINTENANCE / INTERPRETATION REFERENCE', 'không có thẩm quyền runtime',
                     'default runtime read', 'grammar owner', 'sửa glossary',
                     'không tự động tương đương hoặc suy ra nhau']:
            self.assertIn(term, glossary)
        for owner in [self.pipeline, str(self.hub), str(self.catalog), str(self.router), str(local)]:
            self.assertNotIn('CONTROL_VOCABULARY_GLOSSARY', owner)

    def test_active_pins_archive_integrity_and_verification_limits(self):
        for key, ext in [('architecture', 'md'), ('root_catalog', 'yaml')]:
            contract = self.hub['contracts'][key]
            self.assertEqual(contract['version'], '1.16')
            self.assertTrue((ROOT / contract['file']).is_file())
        self.assertEqual(self.ais['version'], '1.2')
        self.assertEqual(self.ais['project_deployment'], 'NOT_PERFORMED')
        archive = ROOT / 'Source_archive/AIS SEARCH promotion 2026-11-09'
        for row in json.loads((archive / 'ARCHIVE_RECEIPT.json').read_text(encoding='utf-8')):
            data = (ROOT / row['archive']).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), row['sha256'])
            self.assertEqual(data, subprocess.check_output(['git', 'show', '0cba55d:Central Hub/' + row['old']], cwd=ROOT))
            if row['old'] != 'HUB_ROUTER_v1.1.yaml':
                self.assertFalse((ROOT / row['old']).exists())
        self.assertIn('NOT_RUN', (ROOT / 'SEARCH_REAL_CONTEXT_STRESS.md').read_text(encoding='utf-8'))

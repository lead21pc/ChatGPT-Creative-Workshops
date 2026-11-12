"""Naming behavior on declared fixture roles and the current leaf."""
import re
import unittest

from test_hub_contracts import Closed, ROOT_CATALOG, load
from test_concept_development import CATALOG, CORE, DIRECTORY, LOCAL, PACKAGE, current_fixture, leaf_span_spec, naming_modifier_spec
from test_concept_production_anti_drift import AP, production_spec
from test_hub_router import integration_read_spec, simulate

NAMING = 'HUB-CON-GEN-NAMING'


class NamingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = load(ROOT_CATALOG)
        cls.local = load(LOCAL)
        cls.row = next(row for row in cls.local['entries'] if row['module_id'] == NAMING)
        cls.body = (DIRECTORY / 'HUB-CON-GEN-NAMING_v1.1.md').read_text(encoding='utf-8')

    def spans(self, text):
        return leaf_span_spec([('USER_DIRECTIVE', text)])

    def test_exact_activation_mid_sentence_and_whitespace(self):
        for text, content in [('/NAME name three islands #', 'name three islands'),
                              ('Context. /NAME\nP2\tname three islands\n# done', 'P2\tname three islands')]:
            self.assertEqual(self.spans(text)['invocations'], [(NAMING, content)])
        for text in ('/name X #', '/NAMELY X #', '/NAMES X #', 'path/NAME X #',
                     '/NAME,X #', 'name these islands', 'FIT X #'):
            self.assertEqual(self.spans(text)['invocations'], [], text)

    def test_provenance_exclusions_and_literal_hash(self):
        for role in ('ASSISTANT', 'PRIOR_TURN', 'TOOL', 'SOURCE', 'ATTACHMENT',
                     'QUOTE', 'CODE', 'ANALYZED_PROMPT'):
            self.assertEqual(leaf_span_spec([(role, '/NAME P2 X #')])['invocations'], [], role)
        result = leaf_span_spec([('USER_DIRECTIVE', '/NAME use '),
                                 ('QUOTE', '"#"'), ('CODE', ' /DEBATE # '),
                                 ('USER_DIRECTIVE', ' as data #')])
        self.assertEqual(result['invocations'], [(NAMING, 'use "#" /DEBATE #  as data')])
        result = leaf_span_spec([('USER_DIRECTIVE', '/NAME '), ('QUOTE', 'P2'),
                                 ('USER_DIRECTIVE', ' is supplied data #')])
        self.assertEqual(len(result['invocations']), 1)
        self.assertEqual(naming_modifier_spec('P2 is data', [False]*2+[True]*9)[0], None)

    def test_span_and_modifier_failures_isolate_independent_work(self):
        for malformed in ('/NAME X', '/NAME #', '/NAME P1 #', '/NAME P4 X #',
                          '/NAME p2 X #', '/NAME P0 X #', '/NAME P01 X #',
                          '/NAME P1 P2 X #', '/NAME P2 p3 X #',
                          '/NAME X /DEBATE Y #', '/CREATIVE X /NAME Y #'):
            self.assertEqual(self.spans(malformed)['invocations'], [], malformed)
            self.assertEqual(len(self.spans(malformed)['blocked']), 1, malformed)
        result = self.spans('/NAME P4 X # independent /CREATIVE Y # /NAME Z #')
        self.assertEqual(result['invocations'], [('HUB-CON-GEN-CREATIVE', 'Y'), (NAMING, 'Z')])
        self.assertIn(' independent ', result['unscoped'])
        self.assertEqual(self.spans('/NAME use #heading and ## as text #')['invocations'],
                         [(NAMING, 'use #heading and ## as text')])

    def test_presets_plain_and_no_alias_or_inferred_preset(self):
        self.assertEqual(naming_modifier_spec('name X'), (None, 'name X'))
        for preset in ('P1', 'P2', 'P3'):
            self.assertEqual(naming_modifier_spec(f'{preset}\nname X'), (preset, 'name X'))
            self.assertEqual(len(self.spans(f'/NAME {preset} name X #')['invocations']), 1)
        for label in ('FIT', 'DISTINCT', 'SEMANTIC'):
            self.assertEqual(naming_modifier_spec(f'{label} as ordinary instruction')[0], None)
        for text in ('P1', 'P4 X', 'p2 X', 'P1 P2 X'):
            self.assertIsNone(naming_modifier_spec(text))
        self.assertIn('do not infer, assign or emit a preset', self.body)

    def test_new_turn_never_inherits_activation_or_preset(self):
        self.assertEqual(len(self.spans('/NAME P2 X #')['invocations']), 1)
        self.assertEqual(self.spans('đồng ý')['invocations'], [])
        self.assertEqual(self.spans('The answer is A')['invocations'], [])
        self.assertEqual(self.spans('/NAME use corrected basis #')['invocations'],
                         [(NAMING, 'use corrected basis')])
        self.assertIsNone(naming_modifier_spec('use corrected basis')[0])
        for clause in ('this invocation ends now', 'a fresh exact Naming span',
                       'neither preset nor activation persists', 'no waiting mode or automatic resume'):
            self.assertIn(clause, self.body)

    def test_brief_request_admission_uses_existing_package_composition(self):
        # NAME is a fixture-declared match for the root applicability, not an LLM classifier.
        package = next(row for row in self.root['packages'] if row['package_id'] == PACKAGE)
        self.assertIn('specialized naming', package['applicability'])
        self.assertIn('even when brief', package['applicability'])
        for literal in ('/NAME', 'HUB-CON-GEN-NAMING', 'P1', 'P2', 'P3'):
            self.assertNotIn(literal, str(package))
        short = self.spans('/NAME X #')
        self.assertEqual(short['invocations'], [(NAMING, 'X')])
        result = simulate(current_fixture(), {'NAME'})
        self.assertEqual(result['spec_reads'][:2], [CORE, CATALOG])
        self.assertEqual({identity for _, identity in result['spec_verified']}, {NAMING})
        self.assertEqual(result['pipeline_entrypoints'], [])
        self.assertFalse(result['runtime_ready'])
        self.assertEqual(simulate(current_fixture(), set())['artifact_requests'], [])

    def test_exact_headers_binding_and_no_new_dependencies(self):
        for key, value in [('Module ID', NAMING), ('Package ID', PACKAGE),
                           ('Runtime role', 'DOMAIN_PROCEDURE'), ('Status', 'ACTIVE'), ('Version', '1.1')]:
            self.assertEqual(re.findall('^'+key+r': (.+)$', self.body, re.M), [value])
        self.assertEqual(self.row['runtime_role'], 'DOMAIN_PROCEDURE')
        self.assertEqual(self.row['activation'], '/NAME')
        for key in ('requires', 'refines', 'complements'):
            self.assertEqual(self.row[key], [])
        self.assertNotRegex(self.body, r'(?m)^(Requires|Refines|Complements):')
        self.assertNotIn('library_file_id', self.row['location'])
        entry = dict(self.row, entrypoint_module_id=NAMING, binding_mode='LIBRARY_MODULE')
        observed = dict(module_id=NAMING, package_id=PACKAGE, runtime_role='DOMAIN_PROCEDURE',
                        status='ACTIVE', version='1.1', root='Central Hub Config', location='LIBRARY',
                        read_kind='FULL_FILE', has_more=False, body_matches=True, opened_object='FIXTURE')
        result = integration_read_spec(entry, [observed], direct_identity_usable=False,
                                       scoped_search_sufficient=True)
        self.assertFalse(result['runtime_ready'])
        for field, value in [('version', 'old'), ('runtime_role', 'CAPABILITY'),
                             ('read_kind', 'SNIPPET'), ('body_matches', False),
                             ('location', 'REPOSITORY')]:
            with self.subTest(field=field), self.assertRaises(Closed):
                integration_read_spec(entry, [dict(observed, **{field: value})],
                                      direct_identity_usable=False, scoped_search_sufficient=True)

    def test_missing_naming_blocks_only_dependent_leaf(self):
        for failure in ('missing', 'wrong_version', 'partial'):
            fixture = current_fixture()
            if failure == 'missing':
                del fixture['artifacts'][NAMING]
            elif failure == 'wrong_version':
                fixture['artifacts'][NAMING][0]['version'] = 'old'
            else:
                fixture['artifacts'][NAMING][0]['read_kind'] = 'SNIPPET'
            result = simulate(fixture, {'NAME', 'CREATIVE'})
            self.assertIn((PACKAGE, NAMING), result['blocked'])
            self.assertIn((PACKAGE, 'HUB-CON-GEN-CREATIVE'), result['spec_verified'])

    def test_anti_prior_selection_remains_applicability_owned(self):
        plain = simulate(current_fixture(), {'NAME'})
        self.assertNotIn(AP, plain['artifact_requests'])
        combined = production_spec(('NAME', 'SURFACE'))
        self.assertEqual({identity for _, identity in combined['spec_verified']}, {NAMING, AP})
        self.assertEqual(self.row['requires'], [])
        self.assertIn('Concept AUTO/current applicability alone selects Anti-Prior', self.body)

    def test_reviewed_ais_and_protected_state_contract_not_behavioral_proof(self):
        for clause in ('Return a concrete material external-evidence need to Hub',
                       'Naming never calls AIS', 're-audits AIS quality',
                       'qualifiers, applicability, limits, conflicts and UNKNOWN',
                       'Missing decisive evidence blocks only the dependent relation',
                       'Reject a candidate conflicting with protected state',
                       'never modify protected fiction state to rescue a candidate',
                       "Preserve a user's intentional mismatch", 'EVIDENCE != NAMING INTENT',
                       'SUPPORTED A + SUPPORTED B != SUPPORTED A+B'):
            self.assertIn(clause, self.body)

    def test_reviewed_gate_policy_and_generation_latitude_not_behavioral_proof(self):
        for clause in ('check internally and produce the result in this turn; no approval round-trip',
                       'briefly disclose it when needed and continue',
                       'ask one focused clarification and stop dependent Naming work',
                       'show a concise representation of the basis being used',
                       'not a completeness proof', 'a structured input form',
                       'BOUND THE SEARCH SPACE != DETERMINE THE OUTPUT',
                       'AUTHORIZED NAMING GAP = PERMISSION TO GENERATE WITHIN THAT GAP'):
            self.assertIn(clause, self.body)
        self.assertLess(self.body.index('## Naming-local distinctions in every strategy'),
                        self.body.index('## One conditional Naming Basis Gate'))
        for distinction in ('ROMANIZATION != UNIQUE WRITTEN FORM', 'CHARACTER != SEMANTIC UNIT',
                            'LITERAL GLOSS != NAME FUNCTION', 'ETYMOLOGY != CURRENT CULTURAL FUNCTION',
                            'CULTURAL ASSOCIATION != FICTION ROLE', 'NAME MEANING != CHARACTER MEANING',
                            'MEANING AVAILABLE != MEANING REQUIRED', 'SOURCE MEANING != AUTHORIZED SYMBOLISM',
                            'MODEL-PRIOR FAMILIARITY != REAL-WORLD FREQUENCY'):
            self.assertIn(distinction, self.body)

"""Active Authoring admission and fixed source-role fixtures, without model execution."""
import json
import re
import unittest

from test_hub_contracts import ROOT, entry_path, package

TARGETS = ('AIS', 'IMAGET', 'CODEX', 'WORK', 'GENERIC')
CASES = {row['id']: row for row in json.loads(
    (ROOT / 'tests/AUTHORING_SOURCE_CASES.json').read_text(encoding='utf-8'))}


def author_call_spec(message, *, user_directive=True):
    """One-turn exact-call oracle; never strips suffixes or remembers a mode."""
    if not user_directive:
        return None
    first = next((line for line in message.replace('\r\n', '\n').split('\n')
                  if line.strip(' \t')), '')
    match = re.fullmatch(r'/AUTHOR (AIS|IMAGET|CODEX|WORK|GENERIC)'
                         r'(?: (P[123]))?( ISOLATED)?', first)
    return match.groups() if match else None


def reference_violations(case, output):
    """Fixture-specific lexical checks, not an arbitrary-output semantic evaluator."""
    return ([f'missing: {text}' for text in case['required'] if text not in output]
            + [f'excluded: {text}' for text in case['forbidden'] if text in output])


class AuthoringTests(unittest.TestCase):
    def test_source_provenance_presets_and_target_scope(self):
        text = entry_path(package('AUTHORING')).read_text(encoding='utf-8')
        for clause in ('root Catalog', 'this invocation ends in the current turn',
                       'supplied context', 'current Hub state', 'model-generated task structure',
                       'neutral research question', 'UNSUPPLIED DOMAIN HYPOTHESIS != PRIOR FINDING',
                       'P1 — CLEAN', 'P2 — CONTRACT', 'P3 — REBUILD',
                       'PRESERVING EACH CONSTRAINT != PRESERVING THE RELATION BETWEEN CONSTRAINTS',
                       'VISIBLE CONTEXT != AUTHORIZED AUTHORING SOURCE',
                       'A supported finding remains supported',
                       'separate decision authority', 'does not require loading or executing that target',
                       'A later request to execute a referenced prompt'):
            self.assertIn(clause, text)
        self.assertIsNone(author_call_spec('The answer is A.'))
        self.assertEqual(author_call_spec('/AUTHOR GENERIC P2 ISOLATED\nA; supplied source.'),
                         ('GENERIC', 'P2', ' ISOLATED'))
        self.assertEqual(author_call_spec(CASES['I6']['request']), ('GENERIC', None, None))
        self.assertEqual(reference_violations(CASES['I6'], CASES['I6']['reference_output']), [])

    def test_all_removed_forms_never_downgrade_and_valid_forms_survive(self):
        for target in TARGETS:
            for preset in ('', ' P1', ' P2', ' P3'):
                for isolation in ('', ' ISOLATED'):
                    call = f'/AUTHOR {target}{preset}{isolation}'
                    self.assertIsNotNone(author_call_spec(call+'\nUse the supplied source.'), call)
                    self.assertIsNotNone(author_call_spec(' \t\r\n'+call+'\r\nTask'), call)
            for removed in ('CREATIVE', 'BRAINSTORM'):
                call = f'/AUTHOR {target} + {removed}'
                for suffix in ('', ' P2', ' ISOLATED'):
                    self.assertIsNone(author_call_spec(call+suffix+'\nTask'), call+suffix)
                self.assertIsNone(author_call_spec(f'/AUTHOR {target} P2 + {removed}'))
        admission = package('AUTHORING')['applicability']
        for rule in ('first non-empty user-authored line', 'case-sensitively', 'plus-suffix', 'unsupported and non-activating'):
            self.assertIn(rule, admission)

    def test_invalid_and_literal_calls_still_rejected(self):
        for text in ('/author AIS', '/AUTHOR  AIS', ' /AUTHOR AIS', '/AUTHOR AIS ',
                     '/AUTHOR FTH', '/AUTHOR AIS P4', '/AUTHOR AIS p2',
                     '/AUTHOR AIS ISOLATED P2', '/AUTHOR AIS DEFAULT',
                     '/AUTHOR AIS P2 extra', 'intro\n/AUTHOR AIS',
                     '> /AUTHOR AIS', '```text\n/AUTHOR AIS\n```'):
            self.assertIsNone(author_call_spec(text), text)
        self.assertIsNone(author_call_spec('/AUTHOR AIS', user_directive=False))

    def test_I1_I2_I3_I4_reference_admission_and_exclusion(self):
        for identity in ('I1', 'I2', 'I3', 'I4'):
            case = CASES[identity]
            with self.subTest(case=identity):
                self.assertIsNotNone(author_call_spec(case['request']))
                self.assertEqual(reference_violations(case, case['reference_output']), [])
                for excluded in case['forbidden']:
                    self.assertIn('excluded: ' + excluded,
                                  reference_violations(case, case['reference_output'] + ' ' + excluded))
        i2 = CASES['I2']
        admitted, unreferenced = i2['accessible_artifacts']
        self.assertTrue(admitted['explicitly_referenced'])
        self.assertIn(admitted['name'], i2['request'])
        self.assertFalse(unreferenced['explicitly_referenced'])
        self.assertNotIn(unreferenced['name'], i2['request'])
        self.assertEqual(CASES['I3']['outcome'], 'CLARIFY')
        self.assertNotIn('CANARY_POSTGRES', CASES['I3']['reference_output'])

    def test_I5_I9_I10_target_and_source_authority(self):
        for identity in ('I5', 'I9', 'I10'):
            case = CASES[identity]
            with self.subTest(case=identity):
                self.assertIsNotNone(author_call_spec(case['request']))
                self.assertEqual(case['outcome'], 'PROMPT')
                self.assertEqual(reference_violations(case, case['reference_output']), [])
        case = CASES['I5']
        stripped = case['reference_output'].replace('No edits, commit or push are authorized', 'Proceed with implementation')
        self.assertTrue(reference_violations(case, stripped))
        case = CASES['I10']
        self.assertTrue(reference_violations(case, case['reference_output'] + ' CANARY_APPROVED'))

    def test_I7_preset_semantics_and_relations_survive(self):
        case = CASES['I7']
        self.assertEqual(author_call_spec(case['request']), ('GENERIC', 'P2', ' ISOLATED'))
        self.assertEqual(reference_violations(case, case['reference_output']), [])
        flattened = "Respect player choices and DM authority. NPCs are autonomous. State persists. Rules change."
        self.assertTrue(reference_violations(case, flattened))

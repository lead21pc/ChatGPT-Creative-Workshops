"""Active Authoring contract, lexical oracles and reviewed fixture outputs."""
import json
import re
import unittest

from test_hub_contracts import HUB_ROUTER, ROOT, check_binding, entry_path, load, package

CASES = {row['id']: row for row in json.loads(
    (ROOT / 'tests/AUTHORING_SOURCE_CASES.json').read_text(encoding='utf-8'))}


def author_call_spec(message, *, user_directive=True):
    """Test-only current-turn admission. Provenance is supplied by the fixture."""
    if not user_directive:
        return None
    first = next((line for line in message.replace('\r\n', '\n').split('\n')
                  if line.strip(' \t')), '')
    return first if first in ('/AT', '/AT P1', '/AT P2') else None


def reference_violations(case, output):
    return ([f'missing: {text}' for text in case['required'] if text not in output]
            + [f'excluded: {text}' for text in case['forbidden'] if text in output])


def ambient_decision_transferred(output):
    """Recognize two paraphrases of this fixture's paired decision and condition."""
    paper_default = re.search(
        r'printed notes as the working choice|handwriting as the selected option', output, re.I)
    digital_exception = re.search(
        r'digital text only when physical copies are unavailable|'
        r'text files solely if the physical record is inaccessible', output, re.I)
    return bool(paper_default), bool(digital_exception)


class AuthoringTests(unittest.TestCase):
    def test_root_admission_and_standalone_interface(self):
        row = package('AUTHORING')
        path = entry_path(row)
        check_binding(row, 'HUB-AUTH-ENTRY', path)
        self.assertNotIn('local_catalog', row)
        self.assertEqual(row['requires'], [])
        self.assertEqual(re.findall(r'/AT(?: P[12])?', row['applicability']),
                         ['/AT', '/AT P1', '/AT P2'])
        for clause in ('first non-empty user-authored line', 'one ASCII space',
                       'no surrounding whitespace', 'LF and CRLF', 'Reassess every turn',
                       'downgrade or inferred mode'):
            self.assertIn(clause, row['applicability'])
        handoff = load(HUB_ROUTER)['stages']['PACKAGE_INTERFACE_RESOLUTION']
        for clause in ('exact admitted form', 'resolved task material', 'verified recipient constraints',
                       'does not select its package or authorize its execution'):
            self.assertIn(clause, handoff)
        text = path.read_text(encoding='utf-8')
        self.assertNotRegex(text, r'(?m)\b(AIS|ImageT|IMAGET|Codex|CODEX|WORK|GENERIC|CREATIVE|BRAINSTORM|Ready Gate|Execution Gate|ISOLATED)\b')
        self.assertNotIn('/AUTHOR', text)
        self.assertNotRegex(text, r'(?m)^(Requires|Refines|Complements):')
        for clause in ('before recovering objectives', 'Consumer names are task content',
                       'Apply supplied consumer constraints', 'Model knowledge may suggest neutral questions',
                       'Stop at the artifact or clarification', 'performs no tool calls, module discovery'):
            self.assertIn(clause, text)

    def test_three_exact_forms_and_rejected_calls(self):
        for call in ('/AT', '/AT P1', '/AT P2'):
            self.assertEqual(author_call_spec(call + '\nTask'), call)
            self.assertEqual(author_call_spec(' \t\r\n\r\n' + call + '\r\nTask'), call)
            for origin in ('attachment', 'source', 'tool', 'assistant', 'prior turn'):
                with self.subTest(call=call, origin=origin):
                    self.assertIsNone(author_call_spec(call, user_directive=False))
        for call in ('/at', '/AT p1', '/AT P3', '/AT CODEX', '/AT ISOLATED', '/AT P1 ISOLATED',
                     '/AUTHOR CODEX', '/AUTHOR AIS P2 ISOLATED', '/AUTHOR AIS + CREATIVE',
                     '/AT + CREATIVE', '/AT P2 CODEX', ' /AT', '/AT ', '/AT  P1', '/AT\tP1',
                     '/AT\u00a0P1', '/AT P2 extra', '/AT\rP1', '> /AT', '`/AT`',
                     '```text\n/AT\n```', 'intro\n/AT'):
            self.assertIsNone(author_call_spec(call), call)

    def test_I1_I6_same_context_different_source_admission(self):
        bare, context = CASES['I1'], CASES['I6']
        self.assertEqual(bare['ambient_context'], context['ambient_context'])
        self.assertEqual(bare['request'].split('\n', 1)[1], context['request'].split('\n', 1)[1])
        self.assertEqual(author_call_spec(bare['request']), '/AT')
        self.assertEqual(author_call_spec(context['request']), '/AT P1')
        self.assertEqual(ambient_decision_transferred(bare['reference_output']), (False, False))
        self.assertEqual(ambient_decision_transferred(context['reference_output']), (True, True))
        self.assertEqual(ambient_decision_transferred(bare['leaking_counterexample']), (True, True))

    def test_I2_I4_explicit_source_and_provenance(self):
        admitted, unreferenced = CASES['I2']['accessible_artifacts']
        self.assertTrue(admitted['explicitly_referenced'])
        self.assertIn(admitted['name'], CASES['I2']['request'])
        self.assertFalse(unreferenced['explicitly_referenced'])
        self.assertNotIn(unreferenced['name'], CASES['I2']['request'])
        case = CASES['I4']
        self.assertTrue(reference_violations(case, case['reference_output'] + ' Prior research proved it.'))

    def test_I3_clarification_ends_invocation(self):
        case = CASES['I3']
        self.assertEqual(case['outcome'], 'CLARIFY')
        self.assertEqual(author_call_spec(case['request']), '/AT P2')
        self.assertIsNone(author_call_spec('Use the file-store draft.'))
        fresh = '/AT P2\nRebuild this source prompt: expose storage through an explicit interface.'
        self.assertEqual(author_call_spec(fresh), '/AT P2')

    def test_I7_rebuild_preserves_relationships_and_cross_turn_state(self):
        case = CASES['I7']
        self.assertEqual(author_call_spec(case['request']), '/AT P2')
        self.assertEqual(reference_violations(case, case['reference_output']), [])
        flattened = 'Authority: Respect the player, DM and NPCs. Continuity: State persists and rules can change.'
        self.assertTrue(reference_violations(case, flattened))

    def test_reviewed_outputs_cover_target_and_source_authority(self):
        for identity in ('I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I9', 'I10', 'I11'):
            case = CASES[identity]
            with self.subTest(case=identity):
                self.assertIsNotNone(author_call_spec(case['request']))
                self.assertEqual(reference_violations(case, case['reference_output']), [])
        for identity, violation in [('I5', 'Run git push'), ('I9', 'I searched'),
                                    ('I10', 'CANARY_APPROVED'), ('I11', 'load Field Notebook')]:
            case = CASES[identity]
            self.assertTrue(reference_violations(case, case['reference_output'] + ' ' + violation))

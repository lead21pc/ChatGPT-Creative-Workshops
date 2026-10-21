"""Candidate STATIC checks and lexical SPEC oracle; no model or target execution."""
import json
import hashlib
import re
import unittest

from test_hub_contracts import ROOT, load


CANDIDATE = ROOT / 'candidates/authoring_v0'
MODULE = CANDIDATE / 'HUB-CAP-AUTHORING_v0.3-candidate.md'
CASES = CANDIDATE / 'AUTHORING_TEST_CASES.md'
PREDECESSOR = ROOT / 'Source_archive/Prompt Authoring v0.1 2026-10-21/HUB-CAP-AUTHORING_v0.1-candidate.md'
V02_PREDECESSOR = ROOT / 'Source_archive/Prompt Authoring v0.2 2026-10-21/HUB-CAP-AUTHORING_v0.2-candidate.md'
TARGETS = ('AIS', 'IMAGET', 'FTH', 'CODEX', 'WORK', 'GENERIC')


def trigger_spec(text, *, user_instruction=True):
    """Test-only oracle; provenance is fixture-supplied, never detected here."""
    if not user_instruction:
        return None
    for line in text.replace('\r\n', '\n').split('\n'):
        if line.strip(' \t') == '':
            continue
        return {f'/AUTHOR {target}': target for target in TARGETS}.get(line)
    return None


class AuthoringCandidateTests(unittest.TestCase):
    def test_header_and_two_candidate_documents(self):
        self.assertEqual({p.name for p in CANDIDATE.iterdir()}, {MODULE.name, CASES.name})
        text = MODULE.read_text(encoding='utf-8')
        for key, value in [('Module ID', 'HUB-CAP-AUTHORING'),
                           ('Package ID', 'HUB-PKG-AUTHORING'),
                           ('Runtime role', 'CAPABILITY'), ('Status', 'CANDIDATE'),
                           ('Version', '0.3-candidate')]:
            self.assertEqual(re.findall(rf'^{key}: (.+)$', text, re.M), [value])
        for key in ('Scope', 'Responsibility boundary'):
            self.assertEqual(len(re.findall(rf'^{key}: .+$', text, re.M)), 1)
        self.assertEqual(re.findall(r'^/AUTHOR (.+)$', text, re.M), list(TARGETS))
        self.assertNotRegex(text, r'(?m)^(Refines|Complements|Requires):')

    def test_gate_vectors(self):
        text = CASES.read_text(encoding='utf-8')
        vectors = json.loads(re.search(r'```json\n(.*?)\n```', text, re.S)[1])
        self.assertEqual([v['id'] for v in vectors], [f'G{i:02}' for i in range(1, 33)])
        for vector in vectors:
            with self.subTest(case=vector['id']):
                self.assertEqual(trigger_spec(vector['text'],
                                 user_instruction=vector.get('user_instruction', True)),
                                 vector['expected'])

    def test_no_active_admission_even_with_exact_trigger(self):
        catalog = load(ROOT / 'HUB_PACKAGE_CATALOG_v1.0.yaml')
        self.assertEqual(len(catalog['packages']), 5)
        self.assertNotIn('HUB-PKG-AUTHORING', {p['package_id'] for p in catalog['packages']})
        for target in TARGETS:
            self.assertEqual(trigger_spec(f'/AUTHOR {target}'), target)
        for name in ('HUB_CI_v1.1.md', 'HUB_ROUTER_v1.1.yaml',
                     'HUB_PACKAGE_CATALOG_v1.0.yaml', 'HUB_ARCHITECTURE_v1.0.md'):
            self.assertNotIn('HUB-PKG-AUTHORING', (ROOT / name).read_text(encoding='utf-8'))

    def test_required_behavior_review_and_evidence_labels(self):
        text = CASES.read_text(encoding='utf-8')
        self.assertEqual(re.findall(r'^\| (B\d+) \|', text, re.M),
                         [f'B{i:02}' for i in range(1, 17)])
        for label in ('REVIEWED_TEXT', 'STATIC VALIDATION', 'SPEC SIMULATION',
                      'LIVE HUB / LIBRARY / TARGET EXECUTION: NOT RUN'):
            self.assertIn(label, text)
        module = MODULE.read_text(encoding='utf-8')
        for invariant in ('AUTHORING != EXECUTION', 'OUTPUT PROMPT != ACCEPTED STATE',
                          'TARGET CONTRACT != TARGET AUTHORITY',
                          'TRIGGER != DOWNSTREAM EXECUTION AUTHORIZATION',
                          'AUTHORING != AIS ORCHESTRATOR'):
            self.assertIn(invariant, module)

    def test_predecessor_bytes_and_exact_activation_contract_preserved(self):
        self.assertEqual(hashlib.sha256(PREDECESSOR.read_bytes()).hexdigest(),
                         '4364e68bb90aa974c82e51d6494a77586a497b2de3727bf6d372ba05354b9a4e')
        self.assertFalse((CANDIDATE / PREDECESSOR.name).exists())
        self.assertEqual(hashlib.sha256(V02_PREDECESSOR.read_bytes()).hexdigest(),
                         'b10b8ca3ccdb674783ce1ca1ba383faa40806d4a6616388df4d50170a39884fe')
        self.assertFalse((CANDIDATE / V02_PREDECESSOR.name).exists())
        text = MODULE.read_text(encoding='utf-8')
        gate = text.split('## Admission and exact activation\n', 1)[1].split(
                          '## Scoped transformation\n', 1)[0]
        self.assertEqual(hashlib.sha256(gate.encode('utf-8')).hexdigest(),
                         '1602ca2431b18a0f674f9f42f4ed78e313c0288170e2b2a11d9821bacb83992e')

    def test_evidence_cases_and_comparison_are_review_only(self):
        text = CASES.read_text(encoding='utf-8')
        self.assertEqual(re.findall(r'^\| (E\d+) \|', text, re.M),
                         [f'E{i:02}' for i in range(1, 13)])
        self.assertIn('B/E cases have no executed semantic simulation', text)
        self.assertIn('Bounded later A/B/C comparison — NOT RUN', text)
        self.assertIn('STATIC PASS != LIVE BEHAVIOR PROVEN', text)
        self.assertIn('LIVE HARNESS PASS != REAL-CONTEXT ROBUSTNESS PROVEN', text)
        self.assertIn('PASSING TESTS != TESTED THE RIGHT THING', text)

    def test_decision_regressions_are_review_only_and_core_is_not_hanfu_specific(self):
        text = CASES.read_text(encoding='utf-8')
        self.assertEqual(re.findall(r'^\| (R\d+) \|', text, re.M),
                         [f'R{i:02}' for i in range(1, 9)])
        self.assertIn('R cases are also reviewed text only', text)
        self.assertIn('Hanfu regression record — USER_REPORTED failure; v0.3 rerun NOT RUN', text)
        self.assertNotRegex(MODULE.read_text(encoding='utf-8').lower(),
                            r'hanfu|jiangnan|late-ming|1620|1644')


if __name__ == '__main__':
    unittest.main()

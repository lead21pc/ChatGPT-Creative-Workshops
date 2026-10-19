"""Candidate STATIC checks and lexical SPEC oracle; no model or target execution."""
import json
import re
import unittest

from test_hub_contracts import ROOT, load


CANDIDATE = ROOT / 'candidates/authoring_v0'
MODULE = CANDIDATE / 'HUB-CAP-AUTHORING_v0.1-candidate.md'
CASES = CANDIDATE / 'AUTHORING_TEST_CASES.md'
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
                           ('Version', '0.1-candidate')]:
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


if __name__ == '__main__':
    unittest.main()

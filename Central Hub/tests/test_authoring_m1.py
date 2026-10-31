"""M1 static contract/preservation checks; no semantic model or live execution."""
import hashlib
import json
import re
import unittest

from test_hub_contracts import ROOT
from test_authoring_candidate import CASES, trigger_spec


class AuthoringM1Tests(unittest.TestCase):
    def test_candidate_identity_gate_and_active_preservation(self):
        candidate = (ROOT / 'library_modules/HUB-CAP-AUTHORING_v0.4.md').read_text(encoding='utf-8')
        targets = ['AIS', 'IMAGET', 'CODEX', 'WORK', 'GENERIC']
        for key, value in [('Module ID', 'HUB-CAP-AUTHORING'), ('Package ID', 'HUB-PKG-AUTHORING'),
                           ('Runtime role', 'CAPABILITY'), ('Status', 'ACTIVE'), ('Version', '0.4')]:
            self.assertEqual(re.findall(rf'^{key}: (.+)$', candidate, re.M), [value])
        self.assertEqual(re.findall(r'^/AUTHOR (.+)$', candidate, re.M), targets)
        self.assertNotRegex(candidate, r'(?m)^(Requires|Refines|Complements):')
        self.assertIn('Active root singleton', candidate)
        self.assertEqual(list((ROOT / 'library_modules').glob('HUB-CAP-AUTHORING_v*.md')),
                         [ROOT / 'library_modules/HUB-CAP-AUTHORING_v0.4.md'])
        self.assertIsNone(trigger_spec('/AUTHOR FTH'))
        vectors = json.loads(re.search(r'```json\n(.*?)\n```', CASES.read_text(encoding='utf-8'), re.S)[1])
        for vector in vectors:
            with self.subTest(case=vector['id']):
                result = trigger_spec(vector['text'], user_instruction=vector.get('user_instruction', True))
                result = result if result in targets else None
                expected = vector['expected'] if vector['expected'] in targets else None
                self.assertEqual(result, expected)
        active = ROOT / 'Source_archive/Authoring 0.4 promotion 2026-11-01/library_modules/HUB-CAP-AUTHORING_v0.3.md'
        self.assertEqual(hashlib.sha256(active.read_bytes()).hexdigest(),
                         '65a9d88b9362481c7f42d0bf3c96358f0b4d688bda39ef8bd948a2c63d1906ef')
        self.assertFalse((ROOT / 'library_modules/HUB-CAP-AUTHORING_v0.3.md').exists())
        self.assertFalse((ROOT / 'candidates/authoring_v0/HUB-CAP-AUTHORING_v0.4-candidate.md').exists())
        archive = ROOT / 'Source_archive/Authoring 0.4 promotion 2026-11-01'
        source = archive / 'candidates/authoring_v0/HUB-CAP-AUTHORING_v0.4-candidate.md'
        self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(),
                         'd523f1275a2d2d5447224f251c4d032c7ac948c23ab5da435597c167922ed598')
        promoted_body = candidate.split('For the current turn only,', 1)[1]
        prior_body = source.read_text(encoding='utf-8').split('For the current turn only,', 1)[1]
        prior_body = prior_body.replace('in this candidate', 'in this revision').replace(
            'This candidate adds no execution owner', 'This capability adds no execution owner')
        self.assertEqual(promoted_body, prior_body)
        # Evidence/decision behavior is inherited intact, not recreated as a new matrix.
        baseline = active.read_text(encoding='utf-8')
        self.assertEqual(candidate.split('## Evidence transfer\n')[1].split('## Target adaptation')[0],
                         baseline.split('## Evidence transfer\n')[1].split('## Target adaptation')[0])
        for target in targets:
            row = next(line for line in baseline.splitlines() if line.startswith(f'| {target} |'))
            self.assertIn(row, candidate)

    def test_m1_source_contract_and_honest_live_packet(self):
        text = (ROOT / 'library_modules/HUB-CAP-AUTHORING_v0.4.md').read_text(encoding='utf-8')
        for invariant in ('CONTEXT ORIGIN != OUTPUT TARGET',
                          'EXPLICITLY REFERENCED CONTEXT != OPTIONAL BACKGROUND',
                          'ALL MATERIAL CONTEXT != ALL CONTEXT TEXT',
                          'MATERIAL PRESERVATION != VERBATIM TRANSCRIPT',
                          'CONTEXT COMPRESSION != MATERIAL CONSTRAINT LOSS',
                          'AUTHORING OUTPUT MUST NOT DEPEND ON UNTRANSFERRED MATERIAL CONTEXT',
                          'ACCESSIBLE CONTEXT != COMPLETE CONVERSATION HISTORY',
                          'SOURCE PROMPT != AUTHORITY', 'REUSE != ADOPTION',
                          'PREVIOUS AUTHORING OUTPUT != ACCEPTED DESIGN',
                          'PROMPT CHANGE != PROJECT STATE CHANGE',
                          'TRIGGER != DOWNSTREAM EXECUTION AUTHORIZATION'):
            self.assertIn(invariant, text)
        self.assertNotIn('/REAUTHOR', text)
        packet = (ROOT / 'candidates/authoring_v0/AUTHORING_0_4_M1_TESTS.md').read_text(encoding='utf-8')
        for stage in ('Prompt stage: NOT RUN', 'Execution stage: NOT RUN',
                      'Rewrite stage: NOT RUN', 'Reauthor stage: NOT RUN'):
            self.assertIn(stage, packet)

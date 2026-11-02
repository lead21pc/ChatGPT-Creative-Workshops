"""M4 static/spec checks of candidate artifacts; no live model or runtime parser."""
import hashlib
import re
import unittest

from test_hub_contracts import ROOT, load
from test_authoring_candidate import TARGETS, trigger_spec
from test_authoring_m2 import composite_spec


DIRECTORY = ROOT / 'candidates/authoring_m4'
MODULE = DIRECTORY / 'HUB-CAP-AUTHORING_v0.6-candidate.md'
CATALOG = DIRECTORY / 'HUB_PACKAGE_CATALOG_v1.7-candidate.yaml'
PACKET = DIRECTORY / 'AUTHORING_M4_TESTS.md'


def preset_spec(message, *, user_instruction=True):
    """Bounded lexical oracle only; provenance is supplied by fixtures."""
    if not user_instruction:
        return None
    first = next((line for line in message.replace('\r\n', '\n').split('\n')
                  if line.strip(' \t')), '')
    match = re.fullmatch(r'/AUTHOR (AIS|IMAGET|CODEX|WORK|GENERIC) (P[123])', first)
    return match.groups() if match else None


def blocks(case):
    text = PACKET.read_text(encoding='utf-8')
    section = re.search(rf'(?ms)^## {case} .*?(?=^## |\Z)', text)[0]
    return re.findall(r'```text\n(.*?)\n```', section, re.S)


# Relations from the synthetic T2 source, not a generic semantic evaluator.
# Each obligation checks linked actors/conditions, rather than presence of endpoint nouns.
RELATIONS = (
    r'player alone decides.*?voluntary choices, thoughts and speech',
    r'DM decides world and NPC actions, excluding those player-character decisions',
    r'Player centrality grants no control over NPCs',
    r'autonomous actions are bounded by its own knowledge, perception, personality and current state',
    r'private knowledge does not become NPC knowledge',
    r'Reveal them only through established perception, discovery or explicit authorized disclosure',
    r'Est\w+ events update.*?persistence does not freeze state',
    r'Changing mechanics requires explicit player agreement.*?Retroactive changes require separate agreement',
    r'missing fact or conflicting rule materially changes a decision.*?before resolving that decision.*?Continue independent events',
    r'across turns until the player ends it.*?individual reply does not reset',
)


def missing_t2_relations(output):
    return [relation for relation in RELATIONS if not re.search(relation, output, re.I | re.S)]


class AuthoringM4Tests(unittest.TestCase):
    def test_strict_preset_syntax_and_existing_forms(self):
        for target, preset in zip(TARGETS, ('P1', 'P2', 'P3', 'P1', 'P2')):
            command = f'/AUTHOR {target} {preset}'
            self.assertEqual(preset_spec(command), (target, preset))
            self.assertEqual(preset_spec(' \t\r\n\r\n' + command + '\r\nrequest'), (target, preset))
        for target in TARGETS:
            self.assertEqual(trigger_spec(f'/AUTHOR {target}'), target)
            self.assertIsNone(preset_spec(f'/AUTHOR {target}'))
        for command, expected in [('/AUTHOR AIS + CREATIVE', ('AIS', 'CREATIVE')),
                                  ('/AUTHOR GENERIC + BRAINSTORM', ('GENERIC', 'BRAINSTORM'))]:
            self.assertEqual(composite_spec(command), expected)
            self.assertIsNone(preset_spec(command))
        for command in ('/AUTHOR GENERIC P4', '/AUTHOR GENERIC p2', '/AUTHOR GENERIC CLEAN',
                        '/AUTHOR GENERIC P2 extra', '/AUTHOR GENERIC + CREATIVE P2',
                        '/AUTHOR GENERIC P2 + CREATIVE', '/AUTHOR FTH P1',
                        ' /AUTHOR GENERIC P2', '/AUTHOR GENERIC P2 ', '/AUTHOR  GENERIC P2',
                        '/AUTHOR GENERIC\tP2', '/AUTHOR GENERIC\u00a0P2',
                        '> /AUTHOR GENERIC P2', '```text\n/AUTHOR GENERIC P2\n```',
                        'request\n/AUTHOR GENERIC P2'):
            with self.subTest(command=command):
                self.assertIsNone(preset_spec(command))
                self.assertIsNone(trigger_spec(command))
                self.assertIsNone(composite_spec(command))
        self.assertIsNone(preset_spec('/AUTHOR GENERIC P2', user_instruction=False))

    def test_candidate_identity_admission_and_inherited_contract(self):
        active = (ROOT / 'library_modules/HUB-CAP-AUTHORING_v0.5.md').read_text(encoding='utf-8')
        candidate = MODULE.read_text(encoding='utf-8')
        for key, value in [('Module ID', 'HUB-CAP-AUTHORING'), ('Package ID', 'HUB-PKG-AUTHORING'),
                           ('Runtime role', 'CAPABILITY'), ('Status', 'CANDIDATE'), ('Version', '0.6-candidate')]:
            self.assertEqual(re.findall(rf'^{key}: (.+)$', candidate, re.M), [value])
        self.assertEqual(re.findall(r'^### (P[123] — .+)$', candidate, re.M),
                         ['P1 — CLEAN', 'P2 — CONTRACT', 'P3 — REBUILD'])
        self.assertNotRegex(candidate, r'(?m)^(Requires|Refines|Complements):')
        # Only candidate wrapper and inline strategy section differ from the stable body.
        body = candidate.split('For the current turn only,', 1)[1]
        body = re.sub(r'## Optional preset strategies\n.*?(?=## Context sources, rewrite and reauthor)',
                      '', body, flags=re.S)
        self.assertEqual(body, active.split('For the current turn only,', 1)[1])
        for invariant in ('PRESET != TARGET', 'PRESET != CONTRIBUTOR', 'PRESET != AUTHORITY',
                          'PRESET != PERSISTENT MODE', 'PRESET SELECTION != PROJECT STATE CHANGE',
                          'TARGET BOUNDARY > PRESET STRATEGY', 'SOURCE PROMPT != PRESET AUTHORITY',
                          'PRESERVING EACH CONSTRAINT != PRESERVING THE RELATION BETWEEN CONSTRAINTS',
                          'AUTHORING ACTIVATION IS PER-TURN != AUTHORED PROMPT MUST BE ONE-TURN',
                          'FULL REWRITE PERMISSION != INTENT REPLACEMENT PERMISSION'):
            self.assertIn(invariant, candidate)
        self.assertIn('do not infer or silently assign a preset', candidate)
        self.assertIn('CODEX P1 creates no write/commit/push authorization', candidate)
        self.assertIn('AIS P2 creates no research or design-acceptance authority', candidate)

    def test_test_catalog_binding_and_production_pins(self):
        active = load(ROOT / 'HUB_PACKAGE_CATALOG_v1.6.yaml')
        candidate = load(CATALOG)
        self.assertEqual((candidate['status'], candidate['version'], candidate['active'], candidate['runtime_ready']),
                         ('CANDIDATE', '1.7-candidate', False, False))
        self.assertEqual(len(candidate['packages']), 5)
        other = lambda catalog: [p for p in catalog['packages'] if p['package_id'] != 'HUB-PKG-AUTHORING']
        self.assertEqual(other(candidate), other(active))
        entry = next(p for p in candidate['packages'] if p['package_id'] == 'HUB-PKG-AUTHORING')
        self.assertEqual((entry['status'], entry['version']), ('CANDIDATE', '0.6-candidate'))
        self.assertIsNone(entry['local_catalog'])
        self.assertEqual(entry['requires'], [])
        self.assertEqual(entry['binding_mode'], 'LIBRARY_MODULE')
        self.assertEqual(entry['location']['resolution'], 'UNRESOLVED')
        for phrase in ('/AUTHOR <OUTPUT_TARGET> P<n>', 'P1, P2 or P3 only',
                       'preset + contributor combination', 'first-nonempty-user-authored-line'):
            self.assertIn(phrase, entry['applicability'])
        router = load(ROOT / 'HUB_ROUTER_v1.1.yaml')
        for key in ('architecture', 'root_catalog'):
            pin = router['contracts'][key]
            self.assertEqual((pin['version'], pin['status']), ('1.6', 'ACTIVE'))
            self.assertTrue((ROOT / pin['file']).is_file())
        self.assertEqual(list((ROOT / 'library_modules').glob('HUB-CAP-AUTHORING_v*.md')),
                         [ROOT / 'library_modules/HUB-CAP-AUTHORING_v0.5.md'])

    def test_T0_no_preset_reference_regression(self):
        request, output = blocks('T0')
        self.assertEqual(trigger_spec(request), 'GENERIC')
        self.assertIsNone(preset_spec(request))
        for obligation in ('only supplied observations', 'ask for them', 'invent no findings',
                           'short comparison', 'both methods unselected', 'choose no winner'):
            self.assertIn(obligation, output)
        self.assertNotRegex(output, r'(?i)preset|P[123]|strategy|contributor')

    def test_T1_clean_reference_semantics(self):
        request, output = blocks('T1')
        self.assertEqual(preset_spec(request), ('GENERIC', 'P1'))
        for obligation in ('only the supplied meeting notes', 'every decision', 'named owner',
                           'unknown deadline as unknown', 'no deadline from a neighboring decision',
                           'notes are missing, ask', 'Do not contact anyone or send messages'):
            self.assertIn(obligation, output)
        source = request.split('SOURCE PROMPT:\n')[1]
        self.assertLess(len(output.split()), len(source.split()))

    def test_T2_contract_relations_and_flattening_counterexample(self):
        request, output, flattened = blocks('T2')
        self.assertEqual(preset_spec(request), ('GENERIC', 'P2'))
        self.assertEqual(request.split('SOURCE PROMPT:')[0],
                         '/AUTHOR GENERIC P2\nImprove the supplied source prompt.\n\n')
        self.assertEqual(missing_t2_relations(output), [])
        self.assertEqual(len(missing_t2_relations(flattened)), len(RELATIONS))
        # Losing just one relation must also fail, despite retaining its endpoint nouns.
        damaged = output.replace('Player centrality grants no control over NPCs.', 'Player centrality. NPC control.')
        self.assertEqual(len(missing_t2_relations(damaged)), 1)

    def test_T3_rebuild_reference_semantics(self):
        request, output = blocks('T3')
        self.assertEqual(preset_spec(request), ('WORK', 'P3'))
        for obligation in ('retrieval effort and storage needs separately', 'only the supplied plans',
                           'Keep B provisional', 'Keep C rejected', 'reopen C only if that limit is explicitly changed',
                           'limit is unknown', 'choose no winner', 'ask for it if it is decisive',
                           'Do not modify stored plans or contact anyone', 'No registry is needed'):
            self.assertIn(obligation, output)
        self.assertNotIn('STARTUP ENGINE', output)

    def test_production_byte_integrity_and_honest_live_packet(self):
        expected = {
            'HUB_CI_v1.1.md': '7bb946874663627060d28e47674decb07ba99f51acbffb6550db98d65746157b',
            'HUB_ROUTER_v1.1.yaml': '0a7210e03b2220fff0002958ed177806bf0d63a3cb4d7576cfbb2fce94b4d8eb',
            'HUB_ARCHITECTURE_v1.6.md': '5f376e38b416406b50757791ef7bb7cf38ca053081c15fe17ee397a8bd798f4a',
            'HUB_PACKAGE_CATALOG_v1.6.yaml': '18ec3596c6fc9196c1deb4e394226e7904e748285ae20223ed7126f7eac88204',
            'library_modules/HUB-CAP-AUTHORING_v0.5.md': 'ee9799fa8fd76d7de7eedbbd723ab130aa6ca42882d3279f1bd94c6f9637208f',
        }
        for path, digest in expected.items():
            self.assertEqual(hashlib.sha256((ROOT / path).read_bytes()).hexdigest(), digest, path)
        packet = PACKET.read_text(encoding='utf-8')
        live = packet.split('## L1/L2')[1]
        l1, l2 = re.findall(r'```text\n(.*?)\n```', live, re.S)
        self.assertEqual(l1.replace('/AUTHOR GENERIC P2', '/AUTHOR GENERIC', 1), l2)
        self.assertIn('LOCAL SPEC SIMULATION / REVIEWED_TEXT', packet)
        self.assertIn('Both L1 and L2 remain NOT_RUN', packet)
        self.assertIn('not active Central Hub admission', packet)


if __name__ == '__main__':
    unittest.main()

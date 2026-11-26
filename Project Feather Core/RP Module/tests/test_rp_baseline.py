"""Static RP control contracts only; no Library retrieval or live model evaluation."""
from pathlib import Path
import re
import unittest

from tools.router_candidate import load


ROOT = Path(__file__).resolve().parents[2]
RP = ROOT / 'RP Module'
A = RP / 'FTH_RP_Router_v0.2.yaml'
B = RP / 'FTH_RP_Router_Path_B_v0.2.yaml'
RUNTIME = RP / 'FTH_RP_Runtime_v0.2.md'
PROBES = RP / 'tests/RP_v0.2_LIVE_PROBES.md'


class RPBaselineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a, cls.b = load(A), load(B)
        cls.runtime = RUNTIME.read_text(encoding='utf-8')
        cls.probes = PROBES.read_text(encoding='utf-8')

    def test_fixed_bindings_match_existing_ci_entries(self):
        for row, ci, version in [(self.a, '3.4', '5.0'), (self.b, '3.5', '6.0')]:
            with self.subTest(ci=ci):
                path = f'Anti-Drift Source/FTH_Anti_Drift_Source_Router_v{version}.yaml'
                self.assertEqual(row['upstream'], path)
                self.assertIn(path, (ROOT / f'Project Feather Core CI/FTH_CI_version_v{ci}.md').read_text(encoding='utf-8'))
                upstream = load(ROOT / path)
                self.assertEqual(upstream['deployment']['ci_version'], ci)
                self.assertIn('PRE_RESPONSE_CHECK', upstream['runtime']['stages'])

    def test_only_upstream_differs_between_router_payloads(self):
        self.assertEqual({k: v for k, v in self.a.items() if k != 'upstream'},
                         {k: v for k, v in self.b.items() if k != 'upstream'})
        self.assertEqual(sum(x != y for x, y in zip(A.read_text(encoding='utf-8').splitlines(),
                                                   B.read_text(encoding='utf-8').splitlines())), 1)

    def test_both_bindings_resolve_one_shared_runtime(self):
        for row in (self.a, self.b):
            self.assertEqual(row['runtime'], RUNTIME.name)
            self.assertEqual((RP / row['runtime']).resolve(), RUNTIME.resolve())
            self.assertIn(RUNTIME.name, row['activation'])
        self.assertEqual(list(RP.glob('FTH_RP_Runtime_v0.2*.md')), [RUNTIME])
        self.assertNotIn('Source Router 5.0', self.runtime)
        self.assertNotIn('Source Router 6.0', self.runtime)
        self.assertIn('already-established Source Router for that deployment', self.runtime)

    def test_no_selector_fields_or_execution_time_handshake(self):
        expected = {'version', 'activation', 'upstream', 'runtime', 'deployment_binding',
                    'entry', 'owns', 'does_not_own', 'memory', 'catalog', 'catalog_contract',
                    'selection', 'required_header', 'id_namespace', 'source_role', 'load_mode',
                    'source_gate', 'actor_without_source', 'source_failure', 'refresh', 'retained_state'}
        self.assertEqual(set(self.a), expected)
        binding = self.a['deployment_binding']
        for guard in ('before RP executes', 'never selects', 'at runtime',
                      'select by recency', 'switch paths on failure', 'another upstream',
                      'blocks dependent RP'):
            self.assertIn(guard, binding)
        self.assertIn('does not select or discover a control plane', self.runtime)
        self.assertIn('validate a CI/Router pair\nat runtime', self.runtime)

    def test_scene_permission_has_bounded_conditions_and_examples(self):
        section = self.runtime.split('## 5. Route before expanding\n', 1)[1].split('## 6.', 1)[0]
        for guard in ('During explicitly active RP', 'compatible with already routed world context',
                      'current scene/interactivity', 'current scene/chat', 'temporary civilian NPC',
                      'local shop', 'incidental object', 'routine dialogue',
                      'already-supported', 'Do not\nroute merely to prove'):
            self.assertIn(guard, section)
        self.assertIn('permitted temporary scene details under section 5', self.runtime)

    def test_structural_unknowns_and_canon_boundary_remain_protected(self):
        for guard in ('does not resolve UNKNOWN, DEFERRED or CONFLICTED',
                      'persistent character history/profile', 'institutional authority or jurisdiction',
                      'new world mechanism', 'ownership', 'durable location truth',
                      'deployment/population scale', 'durable political/economic/social relations',
                      'Neither a non-canon label', 'must pass the upstream gates before use',
                      'Do not later reuse a temporary detail as canon evidence'):
            self.assertIn(guard, self.runtime)
        self.assertIn('Scene output remains non-canon unless the author later', self.runtime)

    def test_material_expansion_still_routes_before_execution(self):
        self.assertIn('STOP dependent RP step\n-> declare the specific upstream information need\n'
                      '-> Source Router re-route\n-> required source / reconciliation / control gates\n'
                      '-> RP Router refresh\n-> continue only if supported', self.runtime)
        self.assertIn('Never emit the fact first and route afterward', self.runtime)
        self.assertIn('Missing decisive information stays blocked', self.runtime)

    def test_required_portrayal_failure_cannot_use_no_source_path(self):
        failure = self.a['source_failure']
        self.assertIn('blocks the dependent portrayal', failure)
        self.assertIn('Never reclassify it as an actor without a source', failure)
        self.assertIn('source failure, not permission to use that no-source path', self.runtime)
        self.assertIn('explicitly required portrayal source failure', self.runtime)
        self.assertIn('user prompt, current chat context and routed world context', self.a['actor_without_source'])

    def test_library_identity_and_no_fallback_contract_unchanged(self):
        self.assertEqual(self.a['catalog'], [])
        self.assertEqual(self.a['source_role'], 'RP_PORTRAYAL_SOURCE')
        self.assertEqual(self.a['id_namespace'], 'FTH-RP-*')
        self.assertEqual(self.a['load_mode'], 'FULL_FILE')
        self.assertEqual(self.a['required_header'], ['RP Module ID', 'Runtime role', 'Actor / Scope',
                                                    'Authority boundary', 'Load mode'])
        self.assertIn('locate the confirmed Library source', self.a['source_gate'])
        self.assertIn('never substitute Memory, a fixture, a repository copy', self.a['source_failure'])
        self.assertIn('separate Library binding', self.a['deployment_binding'])
        self.assertIn('Memory is not a source', self.runtime)

    def test_eight_live_probes_remain_not_run(self):
        self.assertEqual(re.findall(r'^## Case (\d+) ', self.probes, re.M), list('12345678'))
        self.assertEqual(self.probes.count('A: NOT RUN; B: NOT RUN'), 8)
        for guard in ('Battlemage Academy', 'Personal Terminal', 'real-context',
                      'STATIC PASS != LIVE BEHAVIOR PROVEN', 'actual response'):
            self.assertIn(guard, ' '.join(self.probes.split()))

    def test_current_document_links_resolve_without_active_v01_claims(self):
        for name in ('README.md', 'FTH_SYSTEM_CONTEXT.md'):
            text = (ROOT / name).read_text(encoding='utf-8')
            for control in (A, B, RUNTIME):
                self.assertIn(control.name, text)
            self.assertNotIn('RP%20Module/FTH_RP_Runtime_v0.1.md', text)
            self.assertNotIn('RP%20Module/FTH_RP_Router_v0.1.yaml', text)


if __name__ == '__main__':
    unittest.main()

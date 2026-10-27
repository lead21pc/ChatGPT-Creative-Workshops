"""STATIC / declared SPEC fixtures only; no LLM, Library, deployment or canon execution."""
import copy
from pathlib import Path
import re
import subprocess
import unittest

from test_hub_contracts import ROOT, CONCEPT_ARCHIVE, load
from test_hub_router_candidate import synthetic_module, synthetic_fixture, simulate, integration_read_spec
from test_hub_contracts import Closed


PACKAGE = 'HUB-PKG-CONCEPT-DEVELOPMENT'
CORE = 'HUB-DOM-CONCEPT-DEVELOPMENT'
CATALOG = 'HUB-CATALOG-CONCEPT-DEVELOPMENT'
BASELINE = 'ee104645e89939341cd45deba465b5d71da64521'


def current_fixture():
    """Project current interfaces into the existing SPEC oracle; scopes are declared, not inferred."""
    core = synthetic_module(CORE, PACKAGE, {'CORE', 'CREATIVE', 'BRAINSTORM'})
    fixture = synthetic_fixture(core)
    catalog = synthetic_module(CATALOG, PACKAGE, set(), role='PACKAGE_CATALOG')
    fixture['packages'][0]['local_catalog'] = catalog
    fixture['artifacts'][CATALOG] = [dict(copy.deepcopy(catalog), read_kind='FULL_FILE')]
    local = load(ROOT / 'library_modules/HUB-CATALOG-CONCEPT-DEVELOPMENT_v1.0.yaml')
    leaves = []
    for row in local['entries']:
        scope = 'CREATIVE' if row['module_id'] == 'HUB-DOM-CREATIVE' else 'BRAINSTORM'
        leaf = synthetic_module(row['module_id'], row['package_id'], {scope},
                                role=row['runtime_role'], version=row['version'],
                                location=copy.deepcopy(row['location']))
        leaves.append(leaf)
        fixture['artifacts'][leaf['module_id']] = [dict(copy.deepcopy(leaf), read_kind='FULL_FILE')]
    fixture['local_catalogs'][PACKAGE] = leaves
    return fixture


class ConceptDevelopmentTests(unittest.TestCase):
    def setUp(self):
        self.root = load(ROOT / 'HUB_PACKAGE_CATALOG_v1.2.yaml')
        self.local = load(ROOT / 'library_modules/HUB-CATALOG-CONCEPT-DEVELOPMENT_v1.0.yaml')
        self.core = (ROOT / 'library_modules/HUB-DOM-CONCEPT-DEVELOPMENT_v1.0.md').read_text(encoding='utf-8')
        self.notes = (ROOT / 'CONCEPT_DEVELOPMENT_MIGRATION.md').read_text(encoding='utf-8')

    def test_five_root_owners_and_package_local_inventory(self):
        self.assertEqual(self.root['version'], '1.2')
        self.assertEqual({p['package_id'] for p in self.root['packages']},
                         {'HUB-PKG-TECHNICAL', PACKAGE, 'HUB-PKG-AUTHORING',
                          'HUB-PKG-AIS', 'HUB-PKG-IMAGET'})
        package = next(p for p in self.root['packages'] if p['package_id'] == PACKAGE)
        self.assertEqual((package['entrypoint_module_id'], package['runtime_role'], package['version']),
                         (CORE, 'DOMAIN_CONTROL', '1.0'))
        self.assertEqual(package['binding_mode'], 'LIBRARY_MODULE')
        self.assertEqual(package['requires'], [])
        self.assertEqual(package['local_catalog']['module_id'], CATALOG)
        self.assertEqual(package['local_catalog']['package_id'], PACKAGE)
        self.assertEqual((self.local['module_id'], self.local['package_id'], self.local['runtime_role'],
                          self.local['status'], self.local['version']),
                         (CATALOG, PACKAGE, 'PACKAGE_CATALOG', 'ACTIVE', '1.0'))
        self.assertEqual({p['module_id'] for p in self.local['entries']},
                         {'HUB-DOM-CREATIVE', 'HUB-CAP-BRAINSTORM'})
        for leaf_name in ['HUB-DOM-CREATIVE', 'HUB-CAP-BRAINSTORM', 'thử động não', 'brainstorm sâu']:
            self.assertNotIn(leaf_name, str(self.root))  # Root knows only the package interface.

    def test_router_changes_only_exact_pins_and_global_owners_stay(self):
        previous = load(CONCEPT_ARCHIVE / 'HUB_ROUTER_v1.1.yaml')
        expected = copy.deepcopy(previous)
        for key, name in [('architecture', 'HUB_ARCHITECTURE_v1.2.md'),
                          ('root_catalog', 'HUB_PACKAGE_CATALOG_v1.2.yaml')]:
            expected['contracts'][key]['file'] = name
            expected['contracts'][key]['version'] = '1.2'
        expected['contracts']['binding_scope'] = load(ROOT / 'HUB_ROUTER_v1.1.yaml')['contracts']['binding_scope']
        self.assertEqual(load(ROOT / 'HUB_ROUTER_v1.1.yaml'), expected)
        before = load(CONCEPT_ARCHIVE / 'HUB_PACKAGE_CATALOG_v1.0.yaml')
        for package in ['HUB-PKG-TECHNICAL', 'HUB-PKG-AIS', 'HUB-PKG-IMAGET']:
            self.assertEqual(next(p for p in before['packages'] if p['package_id'] == package),
                             next(p for p in self.root['packages'] if p['package_id'] == package))
        original = subprocess.check_output(['git', 'show', BASELINE + ':Central Hub/HUB_CI_v1.1.md'], cwd=ROOT)
        self.assertEqual((ROOT / 'HUB_CI_v1.1.md').read_bytes(), original)

    def test_fth_gate_contract_and_declared_failure_scenarios(self):
        # SPEC: supplied evidence states, not actual Git retrieval or model execution.
        router = load(ROOT / 'candidates/HUB_ROUTER_v1.2-candidate.yaml')
        self.assertEqual((router['router_version'], router['status'], router['active']),
                         ('1.2-candidate', 'CANDIDATE', False))
        baseline = load(ROOT / 'HUB_ROUTER_v1.1.yaml')
        comparable = copy.deepcopy(router)
        for key in ('router_version', 'status', 'active', 'deployment', 'activation_notice'):
            comparable[key] = baseline[key]
        comparable['sequence'].remove('FTH_CHECK_GATE')
        comparable['stages'].pop('FTH_CHECK_GATE')
        comparable['evidence'].pop('candidate_scope')
        comparable['contracts'] = copy.deepcopy(baseline['contracts'])
        self.assertEqual(comparable, baseline)
        self.assertEqual(router['sequence'][:3],
                         ['TASK_SCOPE', 'FTH_CHECK_GATE', 'ROOT_PACKAGE_SELECTION'])
        gate = router['stages']['FTH_CHECK_GATE']
        for clause in ('explicit FTH delegation', 'full fth_base_commit', 'unambiguous repository identity',
                       'CURRENT_SOURCE', '00_AETHERFIRE_CONSOLIDATION_INDEX.md',
                       'identity-consistency evidence only', 'independently calculated hashes',
                       '90_DESIGN_HISTORY_AND_RECONSIDERATIONS.md', '91_RECONCILIATION_RECORD.md',
                       '92_OPEN_ISSUES_CURRENT.md', 'FTH_HANDOFF_UNVERIFIED', 'BLOCK_DEPENDENT',
                       'FTH_HANDOFF_VERIFIED', 'Do not select any Hub package',
                       'UNKNOWN != FALSE', 'UNKNOWN != PERMISSION TO INVENT'):
            self.assertIn(clause, gate)

        def spec(evidence):
            required = ('repository', 'commit', 'path', 'module', 'header_index', 'equality_proven',
                        'equal', 'index_full', 'history_full', 'reconciliation_full', 'open_full')
            return 'FTH_HANDOFF_VERIFIED' if all(evidence.get(k) is True for k in required) else 'FTH_HANDOFF_UNVERIFIED'

        good = dict.fromkeys(('repository', 'commit', 'path', 'module', 'header_index', 'equality_proven',
                              'equal', 'index_full', 'history_full', 'reconciliation_full', 'open_full'), True)
        self.assertEqual(spec(good), 'FTH_HANDOFF_VERIFIED')
        for missing in good:
            with self.subTest(failure=missing):
                self.assertEqual(spec(dict(good, **{missing: False})), 'FTH_HANDOFF_UNVERIFIED')
        # A newer head does not affect the declared base; Hub routing remains a separate decision.
        self.assertEqual(spec(dict(good, current_head_advanced=True)), 'FTH_HANDOFF_VERIFIED')
        self.assertIn('A newer current commit is not failure', gate)
        self.assertIn('Continue independent portions where sufficient', gate)
        self.assertIn('without undoing the verified baseline', gate)

    def test_library_headers_ownership_and_exact_leaf_revisions(self):
        for module, version, role in [(CORE, '1.0', 'DOMAIN_CONTROL'),
                                      ('HUB-DOM-CREATIVE', '1.1', 'DOMAIN_CONTROL'),
                                      ('HUB-CAP-BRAINSTORM', '1.1', 'CAPABILITY')]:
            text = (ROOT / f'library_modules/{module}_v{version}.md').read_text(encoding='utf-8')
            for key, value in [('Module ID', module), ('Package ID', PACKAGE), ('Runtime role', role),
                               ('Status', 'ACTIVE'), ('Version', version)]:
                self.assertEqual(re.findall(r'^' + key + r': (.+)$', text, re.M), [value])
        for row in self.local['entries']:
            self.assertEqual(row['version'], '1.1')
            self.assertEqual(row['package_id'], PACKAGE)
            self.assertEqual(row['requires'], [])
        previous = (CONCEPT_ARCHIVE / 'library_modules/HUB-CAP-BRAINSTORM_v1.0.md').read_bytes()
        current = (ROOT / 'library_modules/HUB-CAP-BRAINSTORM_v1.1.md').read_bytes()
        marker = b'## Branching by premise change'
        self.assertEqual(previous.split(marker, 1)[1], current.split(marker, 1)[1])

    def test_C01_C07_core_only_and_C02_C03_C04_scoped_leaves(self):
        # Supplied semantic needs exercise the existing growing-package oracle.
        cases = [('C01', {'CORE'}, set()), ('C07', {'CORE'}, set()),
                 ('C02', {'CREATIVE'}, {'HUB-DOM-CREATIVE'}),
                 ('C03', {'BRAINSTORM'}, {'HUB-CAP-BRAINSTORM'}),
                 ('C04', {'CREATIVE', 'BRAINSTORM'}, {'HUB-DOM-CREATIVE', 'HUB-CAP-BRAINSTORM'})]
        for case, scopes, leaves in cases:
            with self.subTest(case=case):
                result = simulate(current_fixture(), scopes)
                self.assertEqual({module for _, module in result['planned']}, leaves)
                self.assertEqual(result['spec_reads'][:2], [CORE, CATALOG])
                self.assertEqual(result['local_catalogs_consulted'], [PACKAGE])
                self.assertFalse(result['pipeline_entrypoints'])
                self.assertFalse(result['runtime_ready'])
                self.assertIn('| ' + case + ' |', self.notes)

    def test_C05_C09_baseline_and_no_route_inertia(self):
        fixture = current_fixture()
        original = copy.deepcopy(fixture)
        routes = []
        for scopes in [set(), {'BRAINSTORM'}, set()]:
            result = simulate(fixture, scopes)
            routes.append({module for _, module in result['planned']})
            if not scopes:
                self.assertEqual(result['artifact_requests'], [])
        self.assertEqual(routes, [set(), {'HUB-CAP-BRAINSTORM'}, set()])
        self.assertEqual(fixture, original)
        old = load(CONCEPT_ARCHIVE / 'HUB_PACKAGE_CATALOG_v1.0.yaml')
        old_brain = next(p for p in old['packages'] if p['package_id'] == 'HUB-PKG-BRAINSTORM')
        brain = next(p for p in self.local['entries'] if p['module_id'] == 'HUB-CAP-BRAINSTORM')
        self.assertEqual(brain['applicability'], old_brain['applicability'])
        for phrase in ['thử động não', 'brainstorm sâu', 'not literal substrings',
                       'mentions, definition or ability questions, quoted examples and negation']:
            self.assertIn(phrase, brain['applicability'])

    def test_C08_missing_leaf_and_catalog_block_dependent_only(self):
        fixture = current_fixture()
        del fixture['artifacts']['HUB-CAP-BRAINSTORM']
        result = simulate(fixture, {'CREATIVE', 'BRAINSTORM'})
        self.assertIn((PACKAGE, 'HUB-CAP-BRAINSTORM'), result['blocked'])
        self.assertIn((PACKAGE, 'HUB-DOM-CREATIVE'), result['spec_verified'])
        self.assertTrue(all('repository' not in item.lower() for item in result['artifact_requests']))
        fixture = current_fixture()
        del fixture['artifacts'][CATALOG]
        result = simulate(fixture, {'BRAINSTORM'})
        self.assertIn(PACKAGE, result['blocked'])
        self.assertNotIn('HUB-CAP-BRAINSTORM', result['spec_reads'])
        for read_kind in ['HEADER_ONLY', 'SNIPPET']:
            fixture = current_fixture()
            fixture['artifacts']['HUB-CAP-BRAINSTORM'][0]['read_kind'] = read_kind
            self.assertIn((PACKAGE, 'HUB-CAP-BRAINSTORM'), simulate(fixture, {'BRAINSTORM'})['blocked'])

    def test_verified_library_bindings_preserve_runtime_evidence_boundary(self):
        package = next(p for p in self.root['packages'] if p['package_id'] == PACKAGE)
        self.assertTrue(self.root['runtime_ready'])  # Root eligibility remains distinct from live execution.
        locations = {
            CORE: package['location'],
            CATALOG: package['local_catalog']['location'],
            **{row['module_id']: row['location'] for row in self.local['entries']},
        }
        expected = {
            CORE: ('libfile_25fe61415e408191b974235fa6608edf',
                   'file_00000000e0e48211989902592a6479f8',
                   'Central Hub Config/HUB-DOM-CONCEPT-DEVELOPMENT_v1.0.md'),
            CATALOG: ('libfile_a7fa47cd4e10819194237840dde6c86f',
                      'file_00000000c62482078eb5f87f6885de71',
                      'Central Hub Config/HUB-CATALOG-CONCEPT-DEVELOPMENT_v1.0.yaml'),
            'HUB-DOM-CREATIVE': ('libfile_9a5f1f01a39c8191b3b299cbe8c03b8b',
                                 'file_000000005f1482079a499865628b7576',
                                 'Central Hub Config/HUB-DOM-CREATIVE_v1.1.md'),
            'HUB-CAP-BRAINSTORM': ('libfile_9573068db03081918819492a2f297377',
                                   'file_000000008a6c8211b0b9236c790d343f',
                                   'Central Hub Config/HUB-CAP-BRAINSTORM_v1.1.md'),
        }
        for module, location in locations.items():
            self.assertEqual(location['root'], 'Central Hub Config')
            self.assertEqual(location['verification'], 'CHATGPT_OBSERVED_FULL_FILE_BYTE_EXACT_VERIFIED')
            self.assertEqual(location['resolution'], 'RESOLVED')
            self.assertEqual((location['library_file_id'], location['observed_surface_file_id'],
                              location['observed_path']), expected[module])
            self.assertEqual(location['duplicate_check'],
                             'NO_DUPLICATE_OBSERVED_IN_INSPECTED_CENTRAL_HUB_CONFIG_SCOPE')
            self.assertIsNone(location['locator'])
            self.assertIsNone(location['library_version_id'])  # Artifact Version does not infer Library revision.
            self.assertNotIn('PROJECT_SOURCE', str(location))
        evidence = self.root['concept_development_evidence']
        self.assertEqual(evidence['library_evidence_basis'],
                         'CHATGPT_OBSERVED / USER_PROVIDED; not independently reproduced by Codex')
        self.assertEqual(evidence['runtime_evidence_basis'],
                         'USER_CONFIRMED_LIVE_PASS; not independently reproduced by Codex')
        self.assertEqual(evidence['hub_runtime_retrieval'], 'NOT_VERIFIED')
        self.assertEqual(evidence['central_hub_project_switch'],
                         'USER_CONFIRMED_FOR_INTEGRATED_RUNTIME_SMOKE')
        self.assertEqual(evidence['live_routing'],
                         'USER_CONFIRMED_PASS_FOR_INTEGRATED_RUNTIME_SMOKE_2026_10_27')
        self.assertEqual(evidence['c01_c12_live'], 'NOT_RUN')
        self.assertNotIn('LIVE_VERIFIED', str(self.root))
        row = next(p for p in self.local['entries'] if p['module_id'] == 'HUB-CAP-BRAINSTORM')
        entry = dict(row, entrypoint_module_id=row['module_id'], binding_mode='LIBRARY_MODULE')
        observed = dict(module_id=row['module_id'], package_id=PACKAGE, runtime_role='CAPABILITY',
                        status='ACTIVE', version='1.1', root='Central Hub Config', location='LIBRARY',
                        read_kind='FULL_FILE', has_more=False, body_matches=True,
                        library_file_id=row['location']['library_file_id'])
        result = integration_read_spec(entry, [observed])
        self.assertFalse(result['runtime_ready'])
        self.assertEqual(result['live_integration'], 'NOT_RUN')
        self.assertIsNone(result['library_version_id'])
        for key, wrong in [('version', '1.0'), ('package_id', 'HUB-PKG-BRAINSTORM'),
                           ('root', 'Other root'), ('location', 'repository')]:
            with self.subTest(key=key), self.assertRaises(Closed):
                integration_read_spec(entry, [dict(observed, **{key: wrong})],
                                      direct_identity_usable=True)

    def test_C06_C10_C11_scoped_reasoning_contract_not_behavioral_proof(self):
        # REVIEWED_TEXT guards; only a real model run can establish these behaviors.
        for phrase in ['Institutions only when material', 'Do not run an institutional checklist',
                       'Do not emit an irrelevant-axis or NOT MATERIAL report',
                       'Incidental appeal is not a defect', 'realization of a branch does not accept it',
                       'Findings do not authorize redesign', 'Introduce a primitive only when',
                       'INTERACTION != CONTAINMENT', 'CO-OCCURRENCE != DEPENDENCY',
                       'POWER != AUTHORITY', 'CHRONOLOGY != CAUSALITY',
                       'COOPERATION != PERMANENT COUPLING']:
            self.assertIn(phrase, self.core)
        for duplicate in ['CONTROL GROUNDING:', 'DISCOURSE FIDELITY:', 'EPISTEMIC NON-ESCALATION:',
                          '## Output Contract', '## Explanation and Reader Calibration']:
            self.assertNotIn(duplicate, self.core)
        self.assertEqual(re.findall(r'^\| (C\d{2}) \|', self.notes, re.M), [f'C{i:02}' for i in range(1, 13)])

    def test_C12_retirement_and_predecessor_bytes(self):
        for relative in ['HUB_PACKAGE_CATALOG_v1.0.yaml', 'HUB_ARCHITECTURE_v1.0.md',
                         'library_modules/HUB-DOM-CREATIVE_v1.0.md',
                         'library_modules/HUB-CAP-BRAINSTORM_v1.0.md', 'HUB_LIBRARY_SINGLETON_MIGRATION.md',
                         'HUB_ROUTER_v1.1.yaml']:
            original = subprocess.check_output(['git', 'show', BASELINE + ':Central Hub/' + relative], cwd=ROOT)
            self.assertEqual((CONCEPT_ARCHIVE / relative).read_bytes(), original)
            if relative != 'HUB_ROUTER_v1.1.yaml':
                self.assertFalse((ROOT / relative).exists())
        mini = ROOT.parent / 'llm-controls/project-instruction-designs/Project CI'
        for version in ['2.1', '2.2']:
            name = f'miniConcept_CI_v{version}.md'
            original = subprocess.check_output(['git', 'show', BASELINE + ':llm-controls/project-instruction-designs/Project CI/' + name], cwd=ROOT)
            self.assertEqual((mini / 'source_archive' / name).read_bytes(), original)
            self.assertFalse((mini / name).exists())
        for text in [str(self.root), str(self.local), self.core,
                     (ROOT / 'library_modules/HUB-DOM-CREATIVE_v1.1.md').read_text(encoding='utf-8'),
                     (ROOT / 'library_modules/HUB-CAP-BRAINSTORM_v1.1.md').read_text(encoding='utf-8')]:
            self.assertNotIn('miniConcept_CI', text)
            self.assertNotIn('Source_archive', text)


if __name__ == '__main__':
    unittest.main()

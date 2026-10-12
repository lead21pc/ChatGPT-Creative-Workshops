"""Structural candidate checks and deterministic dependency tests, not LLM evals."""
from copy import deepcopy
from pathlib import Path
import tempfile
import unittest

from tools.router_candidate import ROUTER, CandidateError, check, expand, load, resolve_control, validate

ROOT = Path(__file__).resolve().parents[1]


class RouterCandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = load(ROOT / ROUTER)

    def setUp(self):
        self.data = deepcopy(self.original)

    def rejected(self):
        with self.assertRaises(CandidateError):
            validate(self.data, ROOT)

    def test_current_candidate_resolves_all_eight_families(self):
        self.assertEqual(len(check(ROOT)), 8)

    def test_bad_entry_missing_duplicate_reordered_or_ci_stage_rejected(self):
        for stages in [self.data['runtime']['stages'][:-1],
                       self.data['runtime']['stages'] + ['SOURCE_LOAD'],
                       list(reversed(self.data['runtime']['stages'])),
                       ['CI_VALIDATE'] + self.data['runtime']['stages']]:
            with self.subTest(stages=stages):
                self.data['runtime']['stages'] = stages
                self.rejected()
        self.data = deepcopy(self.original)
        self.data['runtime']['entry'] = 'CI_DISCOVERY'
        self.rejected()

    def test_duplicate_or_missing_control_id_rejected(self):
        self.data['controls'].append(deepcopy(self.data['controls'][0]))
        self.rejected()
        self.data = deepcopy(self.original)
        self.data['controls'].pop()
        self.rejected()

    def test_missing_hard_target_and_conditional_target_rejected(self):
        for field in ['requires', 'conditional_requires']:
            self.data = deepcopy(self.original)
            self.data['controls'][0][field] = ['MISSING'] if field == 'requires' else [{'when': 'material', 'target': 'MISSING'}]
            self.rejected()

    def test_hard_or_conditional_cycle_rejected_even_before_condition_selected(self):
        for edge in [None, {'when': 'material', 'target': 'ACTOR_RECEPTION'}]:
            self.data = deepcopy(self.original)
            if edge is None:
                self.data['controls'][0]['requires'] = ['ACTOR_RECEPTION']
            else:
                self.data['controls'][0]['conditional_requires'] = [edge]
            self.rejected()

    def test_missing_reference_and_escape_rejected(self):
        for path in ['missing.md', '../SYSTEM_CONTEXT.md']:
            self.data['deployment']['ci'] = path
            self.rejected()

    def test_compatibility_tuple_rejected(self):
        for key, value in [('status', 'CANDIDATE'), ('ci_version', '3.2'), ('upstream_base', '8.9'), ('router_version', '4.4')]:
            self.data = deepcopy(self.original)
            self.data['deployment'][key] = value
            self.rejected()

    def test_failure_states_and_load_modes_cannot_silently_weaken(self):
        for section, key, value in [('failures', 'decisive_source_or_authority_missing', 'SOURCE_LOAD_PARTIAL'),
                                    ('failures', 'node_uncertain_missing_or_cycle', 'NODE_OR_FULL'),
                                    ('loading', 'default', 'NODE_OR_FULL'),
                                    ('loading', 'modes', ['FULL_FILE', 'SNIPPET'])]:
            self.data = deepcopy(self.original)
            self.data[section][key] = value
            self.rejected()

    def test_missing_closure_component_rejected(self):
        self.data['loading']['closure_components'].pop()
        self.rejected()

    def test_referenced_ci_version_base_and_status_mismatch_rejected(self):
        import shutil
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for key in ('ci', 'baseline_ci', 'baseline_router', 'pipeline'):
                relative = self.data['deployment'][key]
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / relative, target)
            path = root / self.data['deployment']['ci']
            original = path.read_text(encoding='utf-8')
            for old, new in [('v3.3 (FTH)', 'v3.2 (FTH)'), ('ChatGPT 8.8 base', 'ChatGPT 8.9 base'),
                             ('Status: ACTIVE PROJECT CONTROL', 'Status: CANDIDATE;'),
                             ('FTH_Authoring_Pipeline_v1.1.md', 'FTH_Authoring_Pipeline_v1.0.md'), (original, ''), (original, original + 'x' * 8001)]:
                path.write_text(original.replace(old, new), encoding='utf-8')
                with self.assertRaisesRegex(CandidateError, 'Active CI'):
                    validate(self.data, root)

    def test_upstream_check_accepts_both_existing_repository_layouts(self):
        import shutil
        with tempfile.TemporaryDirectory() as directory:
            repository = Path(directory)
            root = repository / 'Project Feather Core'
            names = [self.data['deployment'][key] for key in
                     ('ci', 'baseline_ci', 'baseline_router', 'pipeline')]
            names += [ROUTER]
            names += self.data['bootstrap']['full_file'] + [self.data['bootstrap']['reconciliation_record']]
            names += [str(path.relative_to(ROOT)) for path in check(ROOT).values()]
            for relative in names:
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / relative, target)
            for relative in ['ChatGPT Plus+ Era/chatgpt v8.8.txt',
                             'llm-controls/global-instructions/ChatGPT Plus+ Era/chatgpt v8.8.txt']:
                upstream = repository / relative
                upstream.parent.mkdir(parents=True, exist_ok=True)
                upstream.write_text('maintenance file presence fixture', encoding='utf-8')
                self.assertEqual(len(validate(self.data, root)), 8)
                upstream.unlink()
            with self.assertRaisesRegex(CandidateError, 'Missing upstream'):
                validate(self.data, root)

    def test_unknown_field_and_empty_policy_rejected(self):
        self.data['runtime']['ci_discovery'] = True
        self.rejected()
        self.data = deepcopy(self.original)
        self.data['policies']['authority'] = ''
        self.rejected()

    def test_duplicate_yaml_keys_and_unsafe_tags_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'bad.yaml'
            for content in ['a: 1\na: 2\n', 'a: !!python/object:builtins.object {}', '[broken']:
                path.write_text(content, encoding='utf-8')
                with self.assertRaises(CandidateError):
                    load(path)

    def test_dependencies_expand_transitively_without_unjudged_flags(self):
        rows = self.data['controls']
        self.assertEqual(expand(rows, ['ACTOR_RECEPTION']), ['ACTOR_RECEPTION', 'MCA'])
        self.assertEqual(expand(rows, ['BELIEF_CULTURE'], ['actor_reception_material', 'institutional_interface_material', 'economic_mechanism_material']),
                         ['ACTOR_RECEPTION', 'BELIEF_CULTURE', 'ECONOMY', 'MCA', 'WIL'])
        self.assertEqual(expand(rows, ['UNDIE']), ['MCA', 'UNDIE'])
        self.assertEqual(expand(rows, ['UNDIE'], ['mortality_material', 'operational_conflict_material']),
                         ['MCA', 'MORTALITY', 'TW', 'UNDIE'])
        self.assertNotIn('TW', expand(rows, ['UNDIE'], ['actor_reception_material']))
        self.assertEqual(expand(rows, ['WIL'], ['economic_mechanism_material']), ['ECONOMY', 'WIL'])
        with self.assertRaises(CandidateError):
            expand(rows, ['UNDIE'], ['mere_scandal'])

    def test_numeric_version_exclusions_direct_children_and_ambiguity(self):
        excluded = self.data['control_selection']['excluded_statuses']
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, status in [('FTH_Test_v1.9.md', 'FINAL'), ('FTH_Test_v1.10.md', 'FINAL'),
                                 ('FTH_Test_v9.0.md', 'CANDIDATE'), ('FTH_Test_v8.0.md', 'SUPERSEDED')]:
                (root / name).write_text('> Status: ' + status, encoding='utf-8')
            (root / 'archive').mkdir()
            (root / 'archive/FTH_Test_v99.0.md').write_text('ignored', encoding='utf-8')
            self.assertEqual(resolve_control(root, 'FTH_Test', excluded).name, 'FTH_Test_v1.10.md')
            (root / 'FTH_Test_v1.10.0.md').write_text('> Status: FINAL', encoding='utf-8')
            with self.assertRaisesRegex(CandidateError, 'Ambiguous'):
                resolve_control(root, 'FTH_Test', excluded)
            with self.assertRaisesRegex(CandidateError, 'Missing'):
                resolve_control(root, 'FTH_Missing', excluded)

    def test_contradictory_status_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'FTH_Test_v2.0.md').write_text('> Status: FINAL\n> Status: DRAFT', encoding='utf-8')
            with self.assertRaisesRegex(CandidateError, 'Ambiguous status'):
                resolve_control(root, 'FTH_Test', ['DRAFT'])

    def test_malformed_eligible_version_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'FTH_Test_vfuture.md').write_text('> Status: FINAL', encoding='utf-8')
            with self.assertRaisesRegex(CandidateError, 'Malformed'):
                resolve_control(root, 'FTH_Test', [])

    def test_candidate_rejects_country_only_pipeline_baseline(self):
        self.data['deployment']['pipeline'] = 'Anti-Drift Source/FTH_Authoring_Pipeline_v1.0.md'
        with self.assertRaisesRegex(CandidateError, 'Pipeline mismatch'):
            validate(self.data, ROOT)

    def test_pipeline_successor_preserves_baseline_and_transformation_stages(self):
        import hashlib
        import re
        baseline = ROOT / 'Anti-Drift Source/FTH_Authoring_Pipeline_v1.0.md'
        self.assertEqual(hashlib.sha256(baseline.read_bytes()).hexdigest(),
                         '98f357e8fa00827a31f15dd4fb24b3b6e1eccbc8eece89c6205da2377a455025')
        old = re.split(r'(?=^## )', baseline.read_text(encoding='utf-8'), flags=re.M)
        new = re.split(r'(?=^## )', (ROOT / self.data['deployment']['pipeline']).read_text(encoding='utf-8'), flags=re.M)
        self.assertEqual([part.splitlines()[0] for part in old[1:]],
                         [part.splitlines()[0] for part in new[1:]])
        for section in (3, 4, 6, 7):
            with self.subTest(section=section):
                self.assertEqual(old[section], new[section])

    def test_project_control_authority_namespace(self):
        for stem in ('Worldbuilding_Internal_Logic_v1.2', 'Total_War_RP_v1.1'):
            with self.subTest(control=stem):
                text = (ROOT / f'Anti-Drift Source/FTH_Anti_Drift_{stem}.md').read_text(encoding='utf-8')
                hook = next(line for line in text.splitlines() if line.startswith('> Authority hook:'))
                self.assertIn('active FTH control layer', hook)
                self.assertNotIn('AetherFire control layer', hook)

    def test_economy_import_guard_preserves_requested_target_scope(self):
        text = (ROOT / 'Anti-Drift Source/FTH_Anti_Drift_Interface_Economy_State_Stabilization_v1.1.md').read_text(encoding='utf-8')
        guard = text.split('# 13. Real-World Reference', 1)[1].split('# 14.', 1)[0]
        self.assertIn('required structures for the requested FTH target', guard)
        self.assertIn('the requested FTH target needs a layer', guard)
        self.assertNotIn('AetherFire', guard)

    def test_country_specific_economy_hook_is_preserved(self):
        text = (ROOT / 'Anti-Drift Source/FTH_Anti_Drift_Interface_Economy_State_Stabilization_v1.1.md').read_text(encoding='utf-8')
        hook = text.split('# 8. Multi-Polar State Hook', 1)[1].split('# 9.', 1)[0]
        self.assertIn('Current AetherFire state authority is multi-polar.', hook)
        self.assertIn('Mage Council', hook)
        self.assertNotIn('FTH state authority', hook)

    def test_ci_changes_confined_to_approved_boundary_sections(self):
        old = (ROOT / 'Project Feather Core CI/FTH_CI_version_v3.2.md').read_text(encoding='utf-8')
        new = (ROOT / self.data['deployment']['ci']).read_text(encoding='utf-8')
        old_intro, old_rest = old.split('## Source gate', 1)
        new_intro, new_rest = new.split('## Source gate', 1)
        status = '> Status: ACTIVE PROJECT CONTROL\n\n'
        normalized = new_intro.replace('v3.3 (FTH)', 'v3.2 (FTH)', 1).replace(status, '')
        normalized = normalized.replace('FTH_Authoring_Pipeline_v1.1.md', 'FTH_Authoring_Pipeline_v1.0.md', 1)
        self.assertEqual(normalized, old_intro)
        marker = '## Relations and simulation'
        old_tail = old_rest.split(marker, 1)[1]
        new_tail = new_rest.split(marker, 1)[1]
        old_overlay_entry = 'After reconciliation, Router selects overlays/dependencies; initial modular architecture requires activated overlays as `FULL_FILE`.'
        self.assertEqual(new_tail, old_tail.replace(old_overlay_entry, 'Router alone selects and loads overlays/dependencies.'))
        self.assertLessEqual(len((ROOT / self.data['deployment']['ci']).read_bytes().decode('utf-8')), 8000)

    def test_probes_cover_draft_contracts_without_runtime_claim(self):
        import json
        suite = json.loads((ROOT / 'tests/control-regressions/router-v5-probes.json').read_text(encoding='utf-8'))
        self.assertEqual(len(suite['probes']), 18)
        self.assertEqual(len({p['id'] for p in suite['probes']}), 18)
        self.assertFalse(suite['model_executed'])
        self.assertEqual(suite['status'], 'DRAFT')

    def test_active_stack_numeric_yaml_resolution_and_duplicate_rejection(self):
        import shutil
        excluded = self.data['control_selection']['excluded_statuses']
        for directory, stem, expected in [('Project Feather Core CI', 'FTH_CI_version', 'FTH_CI_version_v3.3.md'),
                                         ('Anti-Drift Source', 'FTH_Anti_Drift_Source_Router', 'FTH_Anti_Drift_Source_Router_v5.0.yaml'),
                                         ('Anti-Drift Source', 'FTH_Authoring_Pipeline', 'FTH_Authoring_Pipeline_v1.1.md')]:
            self.assertEqual(resolve_control(ROOT / directory, stem, excluded).name, expected)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copyfile(ROOT / ROUTER, root / Path(ROUTER).name)
            stem = 'FTH_Anti_Drift_Source_Router'
            (root / (stem + '_v99.0.yaml')).write_text('deployment: {status: CANDIDATE}', encoding='utf8')
            self.assertEqual(resolve_control(root, stem, excluded).name, Path(ROUTER).name)
            (root / (stem + '_v5.0.0.md')).write_text('> Status: ACTIVE', encoding='utf8')
            with self.assertRaisesRegex(CandidateError, 'Ambiguous highest'):
                resolve_control(root, stem, excluded)

    def test_active_references_have_no_candidate_lock(self):
        dep = self.data['deployment']
        self.assertEqual(dep['status'], 'ACTIVE')
        self.assertNotIn('candidate_ci', dep)
        for relative in (ROUTER, dep['ci'], dep['pipeline']):
            self.assertNotIn('/candidates/', relative)
            text = (ROOT / relative).read_text(encoding='utf8')
            self.assertNotIn('Status: CANDIDATE', text)
            self.assertNotIn('not deployed', text)
            self.assertNotIn('/candidates/', text)

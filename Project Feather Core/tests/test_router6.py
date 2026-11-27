"""Stack 6 structure/retrieval regression; no claimed live execution."""
from copy import deepcopy
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import test_local_binding_trial as local_tests
from test_local_binding_trial import LocalTrialHarness, ROOT, read_page
from tools.router_candidate import (
    CandidateError, ROUTER, ROUTER6, LOCAL_BINDING_TRIAL,
    check, check_baseline5, check_fthx_candidate, check_local_adapter,
    check_local_binding_trial, load, local_file, resolve_control, router6_access,
    validate, validate_router6,
)


class Router6Harness(LocalTrialHarness):
    """Test-only implementation of the archive target boundary in 6.0 access."""
    def full_file(self, relative, page_size=1000):
        path = self.root / relative
        if (any(part.casefold() == 'source_archive' for part in path.parts)
                or any(part.casefold() == 'source_archive' for part in path.resolve().parts)):
            raise CandidateError('SOURCE_LOAD_BLOCKED: Source_Archive is outside runtime source space')
        return super().full_file(relative, page_size)


class Router6RetrievalTests(local_tests.LocalBindingRetrievalTests):
    # Run every existing retrieval/failure/spec case against the 6.0 boundary too.
    def binding(self, **kwargs):
        return Router6Harness(self.root, selected_as_current=True, **kwargs)

    def test_archive_targets_block_before_read_search_or_enumeration(self):
        binding = self.binding()
        targets = ['Source_Archive/current.md', 'nested/source_archive/current.md',
                   'nested/SOURCE_ARCHIVE/current.md', str(self.root / 'Source_Archive/current.md')]
        with patch.object(Path, 'read_bytes', side_effect=AssertionError('unexpected read')), \
             patch.object(Path, 'glob', side_effect=AssertionError('unexpected search')), \
             patch.object(Path, 'iterdir', side_effect=AssertionError('unexpected enumeration')):
            for target in targets:
                with self.subTest(target=target), self.assertRaisesRegex(CandidateError, 'outside runtime'):
                    binding.full_file(target)
        binding.catalog['AFM-001'] = targets[0]
        with self.assertRaisesRegex(CandidateError, 'outside runtime'):
            binding.module('AFM-001')

    def test_current_gap_is_not_rescued_by_archived_same_name(self):
        binding = self.binding()
        name = binding.catalog['AFM-001']
        archive = self.root / 'Source_Archive'
        archive.mkdir()
        (self.root / name).rename(archive / name)
        binding.reader = Mock(wraps=read_page)
        with self.assertRaisesRegex(CandidateError, 'SOURCE_LOAD_BLOCKED: missing/outside'):
            binding.module('AFM-001')
        binding.reader.assert_not_called()

    def test_available_history_never_enters_a_current_module_route(self):
        binding = self.binding()
        names = ('90_DESIGN_HISTORY_AND_RECONSIDERATIONS.md', '93_SUPERSEDED_IDEAS.md')
        (self.root / names[1]).write_bytes((ROOT / names[1]).read_bytes())
        for name in names:
            self.assertTrue((self.root / name).is_file())
            self.assertNotIn(name, binding.catalog.values())
        binding.module('AFM-002')
        self.assertTrue({read[0] for read in binding.reads}.isdisjoint(names))

        (self.root / binding.catalog['AFM-002']).unlink()
        binding.reader = Mock(wraps=read_page)
        with self.assertRaisesRegex(CandidateError, 'SOURCE_LOAD_BLOCKED: missing/outside'):
            binding.module('AFM-002')
        binding.reader.assert_not_called()

    def test_long_lore_and_control_transport_have_complete_range_coverage(self):
        binding = self.binding()
        names = ['11_STATUS_CIVIL_LABOR_CURRENT.md',
                 'Anti-Drift Source/FTH_Anti_Drift_Total_War_RP_v1.1.md']
        for name in names:
            # A transport check only: this does not select or migrate controls.
            source = ROOT / name
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read_bytes())
            self.assertEqual(binding.full_file(name, page_size=200), source.read_bytes())
            pages = [row for row in binding.reads if row[0] == name]
            self.assertGreater(len(pages), 1)
            self.assertEqual(sum(row[2] for row in pages), pages[-1][3])


class Router6StructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = load(ROOT / ROUTER)
        cls.data = load(ROOT / ROUTER6)
        cls.trial = load(ROOT / LOCAL_BINDING_TRIAL)

    def test_two_exact_stacks_validate_and_active_resolution_selects_six(self):
        self.assertEqual(check_baseline5(ROOT), validate(self.base, ROOT))
        self.assertEqual(validate_router6(self.data, ROOT), check(ROOT))
        excluded = self.base['control_selection']['excluded_statuses']
        self.assertEqual(resolve_control(ROOT / 'Anti-Drift Source',
                         'FTH_Anti_Drift_Source_Router', excluded), ROOT / ROUTER6)
        self.assertEqual(resolve_control(ROOT / 'Project Feather Core CI',
                         'FTH_CI_version', excluded).name, 'FTH_CI_version_v3.5.md')

    def test_router_delta_is_only_deployment_access_and_discovery(self):
        for key in self.base.keys() - {'deployment', 'policies'}:
            self.assertEqual(self.base[key], self.data[key])
        changed = {key for key in self.base['policies']
                   if self.base['policies'][key] != self.data['policies'][key]}
        self.assertEqual(changed, {'access', 'discovery'})
        self.assertEqual(self.data['policies']['discovery'], self.trial['policies']['discovery'])
        self.assertEqual(self.data['policies']['access'], router6_access(self.trial['policies']['access']))
        self.assertEqual(self.data['deployment']['baseline_router'], ROUTER)
        self.assertEqual(self.data['deployment']['baseline_ci'], self.base['deployment']['ci'])
        self.assertEqual(self.data['deployment']['upstream_base'], '8.9')
        for key in ('ci', 'baseline_ci', 'baseline_router', 'pipeline'):
            self.assertNotIn('source_archive', self.data['deployment'][key].casefold())
        for key in ('access', 'discovery'):
            for forbidden in ('C:\\', 'Sheeplark', 'Remote Desktop Commander', 'device_id', 'credential='):
                self.assertNotIn(forbidden, self.data['policies'][key])

    def test_ci_successor_only_changes_title_and_exact_router_reference(self):
        old = local_file(ROOT, self.base['deployment']['ci']).read_text(encoding='utf-8')
        new = local_file(ROOT, self.data['deployment']['ci']).read_text(encoding='utf-8')
        self.assertEqual(new, old.replace('# Project Feather Core CI v3.4 (FTH)',
                                         '# Project Feather Core CI v3.5 (FTH)', 1).replace(ROUTER, ROUTER6))
        self.assertLessEqual(len(new), 8000)

    def test_archive_policy_covers_all_runtime_operations_and_no_fallback(self):
        access = self.data['policies']['access']
        for term in ('case-insensitive path component, at any depth', 'Do not read, search, enumerate',
                     'follow references', 'select versions', 'current CI/Router/lore/generation',
                     'A mention or path in a current file grants no access',
                     'Library, Project Sources, GitHub, Memory, prior-response, near-match, other-root or archive',
                     'partial reads never count as FULL_FILE'):
            self.assertIn(term, access)

    def test_history_is_outside_both_current_bootstraps(self):
        names = ('90_DESIGN_HISTORY_AND_RECONSIDERATIONS.md', '93_SUPERSEDED_IDEAS.md')
        for router in (self.base, self.data):
            self.assertEqual(router['bootstrap']['full_file'],
                             ['00_AETHERFIRE_CONSOLIDATION_INDEX.md', '92_OPEN_ISSUES_CURRENT.md'])
            self.assertEqual(router['bootstrap']['reconciliation_record'], '91_RECONCILIATION_RECORD.md')
        for name in names:
            self.assertTrue((ROOT / name).is_file())
            self.assertNotIn(name, self.base['policies']['access'])
            self.assertIn(name, self.data['policies']['access'])
        self.assertIn('never fallback', self.base['policies']['authority'])
        self.assertNotIn('> Runtime role:', (ROOT / names[1]).read_text(encoding='utf-8'))

    def test_rejects_protected_changes_fthx_archive_or_fallback_weakening(self):
        mutations = [
            lambda d: d['deployment'].update(status='CANDIDATE'),
            lambda d: d['deployment'].update(ci_version='3.4'),
            lambda d: d['policies'].update(discovery=self.trial['policies']['discovery'] + ' Activate FTHX.'),
            lambda d: d['policies'].update(access=d['policies']['access'].replace('Do not read', 'Read')),
            lambda d: d['policies'].update(access=d['policies']['access'] + ' Fallback to Library.'),
            lambda d: d['controls'].pop(),
            lambda d: d['failures'].update(local_missing='NEW_STATE'),
            lambda d: d['policies'].update(authority='different authority'),
        ]
        for mutate in mutations:
            data = deepcopy(self.data)
            mutate(data)
            with self.subTest(mutation=mutate), self.assertRaises(CandidateError):
                validate_router6(data, ROOT)


class LocalAdapterStructureTests(unittest.TestCase):
    """Static entry/reference checks only; no client discovery or compliance claims."""
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='fth-local-adapter-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / 'selected package'
        self.root.mkdir()
        self.references = {
            'CI': 'Project Feather Core CI/FTH_CI_version_v3.5.md',
            'Router': ROUTER6,
            'Pipeline': 'Anti-Drift Source/FTH_Authoring_Pipeline_v1.1.md',
            'Anti-Drift': 'Anti-Drift Source/',
        }
        self.text = '\n'.join(f'| {name} | `{relative}` |'
                              for name, relative in self.references.items()) + '\n'
        self.adapter = self.root / 'AGENTS.md'
        self.adapter.write_text(self.text, encoding='utf-8')
        for name in ('CI', 'Router', 'Pipeline'):
            target = self.root / self.references[name]
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text('Static path-existence fixture only.\n', encoding='utf-8')

    def test_fixed_bindings_and_repository_adapter_validate(self):
        self.assertIsNone(check_local_adapter(self.root))
        self.assertIsNone(check_local_adapter(ROOT))

    def test_missing_adapter_and_unreadable_adapter_rejected(self):
        self.adapter.unlink()
        with self.assertRaisesRegex(CandidateError, 'AGENTS.md'):
            check_local_adapter(self.root)
        self.adapter.write_text(self.text, encoding='utf-8')
        with patch.object(Path, 'read_text', side_effect=PermissionError('fixture denied')):
            with self.assertRaisesRegex(CandidateError, 'Local adapter read failed'):
                check_local_adapter(self.root)

    def test_each_referenced_control_must_exist(self):
        for name in ('CI', 'Router', 'Pipeline'):
            path = self.root / self.references[name]
            data = path.read_bytes()
            path.unlink()
            with self.subTest(control=name), self.assertRaisesRegex(CandidateError, 'Missing/outside'):
                check_local_adapter(self.root)
            path.write_bytes(data)

    def test_wrong_pair_or_pipeline_and_duplicate_binding_rejected(self):
        mutations = [
            self.text.replace('FTH_CI_version_v3.5.md', 'FTH_CI_version_v3.4.md'),
            self.text.replace('FTH_Anti_Drift_Source_Router_v6.0.yaml',
                              'FTH_Anti_Drift_Source_Router_v5.0.yaml'),
            self.text.replace('FTH_Authoring_Pipeline_v1.1.md', 'FTH_Authoring_Pipeline_v1.0.md'),
            self.text + '| CI | `Project Feather Core CI/FTH_CI_version_v3.4.md` |\n',
            self.text + '| CI | Project Feather Core CI/FTH_CI_version_v3.4.md |\n',
            self.text + self.text.splitlines()[0] + '\n',
        ]
        for text in mutations:
            self.adapter.write_text(text, encoding='utf-8')
            with self.subTest(adapter=text), self.assertRaisesRegex(CandidateError, 'pinned references'):
                check_local_adapter(self.root)

    def test_path_a_prose_does_not_change_fixed_local_bindings(self):
        self.adapter.write_text(self.text + '\nPath A: CI 3.4 + Router 5.0 remains a reference.\n',
                                encoding='utf-8')
        self.assertIsNone(check_local_adapter(self.root))

    def test_relative_escape_and_absolute_reference_rejected(self):
        outside = self.root.parent / 'outside.md'
        outside.write_text('Outside fixture.\n', encoding='utf-8')
        for relative in ('../outside.md', str(outside)):
            self.adapter.write_text(self.text.replace(self.references['CI'], relative), encoding='utf-8')
            with self.subTest(reference=relative), self.assertRaises(CandidateError):
                check_local_adapter(self.root)

    def test_simulated_resolved_escape_rejected_for_adapter_and_each_binding(self):
        # Simulate symlink resolution without requiring Windows symlink privileges.
        outside = self.root.parent / 'outside.md'
        outside.write_text('Outside fixture.\n', encoding='utf-8')
        outside_directory = self.root.parent / 'outside directory'
        outside_directory.mkdir()
        original_resolve = Path.resolve
        for relative in ('AGENTS.md', *self.references.values()):
            target = self.root / relative
            destination = outside_directory if relative.endswith('/') else outside
            def resolved(path, *args, **kwargs):
                return destination if path == target else original_resolve(path, *args, **kwargs)
            with self.subTest(reference=relative), patch.object(Path, 'resolve', resolved):
                with self.assertRaisesRegex(CandidateError, 'Missing/outside'):
                    check_local_adapter(self.root)

    def test_selected_six_requires_adapter_but_lineage_checks_do_not(self):
        expected = check_baseline5(ROOT)
        with patch('tools.router_candidate.check_local_adapter',
                   side_effect=CandidateError('fixture adapter unavailable')):
            with self.assertRaisesRegex(CandidateError, 'fixture adapter unavailable'):
                check(ROOT)
            self.assertEqual(check_baseline5(ROOT), expected)
            self.assertEqual(validate_router6(load(ROOT / ROUTER6), ROOT), expected)
            self.assertEqual(check_local_binding_trial(ROOT), expected)
            self.assertEqual(check_fthx_candidate(ROOT), expected)

    def test_selected_five_does_not_require_adapter(self):
        expected = check_baseline5(ROOT)
        original_resolve = resolve_control
        def selected_five(directory, stem, excluded):
            if directory == ROOT / 'Anti-Drift Source' and stem == 'FTH_Anti_Drift_Source_Router':
                return ROOT / ROUTER
            if directory == ROOT / 'Project Feather Core CI' and stem == 'FTH_CI_version':
                return ROOT / 'Project Feather Core CI/FTH_CI_version_v3.4.md'
            return original_resolve(directory, stem, excluded)
        with patch('tools.router_candidate.resolve_control', side_effect=selected_five), \
             patch('tools.router_candidate.check_local_adapter',
                   side_effect=AssertionError('Path A must not check the Path B adapter')):
            self.assertEqual(check(ROOT), expected)


if __name__ == '__main__':
    unittest.main()

"""Local trial/spec tests only: no model, bridge or live Project execution.

The harness below tests retrieval, not semantic routing or canon admission.
It receives the deployment's explicit package selection; it cannot grant it.
"""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock

import build_consolidation as package
from tools.router_candidate import (
    CandidateError, LOCAL_BINDING_POLICIES, LOCAL_BINDING_TRIAL, ROUTER,
    check, check_fthx_candidate, check_local_binding_trial, expand, load,
    resolve_control, validate_local_binding_trial,
)

ROOT = Path(__file__).resolve().parents[1]
PROBES = ROOT / 'tests/control-regressions/router-local-binding-probes.json'


def read_page(path, offset, limit):
    """Test transport: return exact byte lines, their start and total count."""
    lines = path.read_bytes().splitlines(keepends=True)
    return offset, len(lines), lines[offset:offset + limit]


class LocalTrialHarness:
    """Test-only catalog route; source/authority/overlay decisions stay upstream."""
    def __init__(self, root, *, selected_as_current=False, reader=read_page):
        self.root = Path(root)
        self.reader = reader
        self.reads = []
        if not selected_as_current or not self.root.is_absolute() or not self.root.is_dir():
            raise CandidateError('SOURCE_LOAD_BLOCKED: exact current package root not selected/available')
        self.root = self.root.resolve()
        self.bootstrap = {name: self.full_file(name) for name in
                          (package.INDEX, '92_OPEN_ISSUES_CURRENT.md')}
        try:
            _, _, _, block = package.region(self.bootstrap[package.INDEX], package.CATALOG)
            self.catalog = package.rows(block,
                '| Module ID | Current source path (relative to Project Feather Core/) |',
                package.ACCEPTED)
        except (package.ValidationError, UnicodeError) as error:
            raise CandidateError(f'REVIEW_REQUIRED: catalog identity: {error}') from error
        # One preflight of the existing package, not per-read hashing or authority.
        try:
            package.plan(self.root)
        except (package.ValidationError, OSError, UnicodeError) as error:
            raise CandidateError(f'SOURCE_LOAD_BLOCKED: package consistency: {error}') from error

    def full_file(self, relative, page_size=1000):
        try:
            relative = Path(relative)
            if relative.is_absolute() or '..' in relative.parts:
                raise CandidateError('SOURCE_LOAD_BLOCKED: path must stay relative to configured root')
            path = (self.root / relative).resolve()
            if not path.is_relative_to(self.root) or not path.is_file():
                raise CandidateError('SOURCE_LOAD_BLOCKED: missing/outside source')
            if page_size <= 0:
                raise CandidateError('SOURCE_LOAD_BLOCKED: invalid page size')
            before = path.stat()
            offset, total, chunks = 0, None, []
            while True:
                start, count, lines = self.reader(path, offset, page_size)
                if (start != offset or type(count) is not int or count < offset
                        or (total is not None and count != total)
                        or len(lines) != min(page_size, count - offset)):
                    raise CandidateError('SOURCE_LOAD_BLOCKED: incomplete/inconsistent ranges')
                total = count
                self.reads.append((relative.as_posix(), start, len(lines), total))
                chunks.extend(lines)
                offset += len(lines)
                if offset == total:
                    break
            after = path.stat()
            if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
                raise CandidateError('SOURCE_LOAD_BLOCKED: source changed during ranges')
            data = b''.join(chunks)
            if len(data) != after.st_size:
                raise CandidateError('SOURCE_LOAD_BLOCKED: incomplete byte coverage')
            return data
        except OSError as error:
            raise CandidateError(f'SOURCE_LOAD_BLOCKED: local read failed: {error}') from error

    def module(self, module_id):
        if module_id not in self.catalog:
            raise CandidateError('REVIEW_REQUIRED: unknown AFM identity')
        name = self.catalog[module_id]
        data = self.full_file(name)
        try:
            values = package.header(data, name)
        except (package.ValidationError, UnicodeError) as error:
            raise CandidateError(f'REVIEW_REQUIRED: module header: {error}') from error
        if values['Module ID'] != module_id:
            raise CandidateError('REVIEW_REQUIRED: catalog/header ID mismatch')
        # Matching these fields does NOT admit a source or assign canon authority.
        return data, values


class LocalBindingStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.active = load(ROOT / ROUTER)
        cls.trial = load(ROOT / LOCAL_BINDING_TRIAL)

    def test_trial_checks_independently_and_preserves_other_candidates(self):
        self.assertEqual(check_local_binding_trial(ROOT), check(ROOT))
        self.assertEqual(check_fthx_candidate(ROOT), check(ROOT))
        for relative, expected in {
            ROUTER: '9d77216267db30a2465e54b6d31fa90f80553ada0106758224be6f61475bb9fa',
            'Anti-Drift Source/candidates/FTH_Anti_Drift_Source_Router_v5.1.yaml':
                '85d8c51df3c9f3683acc5e7fa1e3c5b6e7b1a254be06e2c214520b1c881e8580',
            self.active['deployment']['ci']:
                '5d5a2f89c15a27d4b4dfb78c6818f194025a47fac13df241c9d368427bb0e79d',
            self.active['deployment']['pipeline']:
                '2290abf544289431cc6188aa683fa940e23eedeff397bb47491a952daf8a9691',
        }.items():
            with self.subTest(file=relative):
                self.assertEqual(hashlib.sha256((ROOT / relative).read_bytes()).hexdigest(), expected)

    def test_exact_delta_and_numeric_selection(self):
        self.assertEqual(set(self.trial), set(self.active))
        for section in self.active.keys() - {'deployment', 'policies'}:
            self.assertEqual(self.trial[section], self.active[section])
        changed = {name for name in self.active['policies']
                   if self.trial['policies'][name] != self.active['policies'][name]}
        self.assertEqual(changed, LOCAL_BINDING_POLICIES)
        self.assertEqual(Path(LOCAL_BINDING_TRIAL).parent.name, 'candidates')
        self.assertEqual(resolve_control(ROOT / 'Anti-Drift Source', 'FTH_Anti_Drift_Source_Router',
                         self.active['control_selection']['excluded_statuses']), ROOT / ROUTER)
        self.assertEqual(self.trial['deployment']['baseline_router'], ROUTER)
        text = (ROOT / LOCAL_BINDING_TRIAL).read_text(encoding='utf-8')
        for marker in ('CANDIDATE / TRIAL', 'NOT ACTIVE', 'NOT LIVE DEPLOYMENT', 'independent from FTHX 5.1'):
            self.assertIn(marker, text)
        changed_text = ' '.join(self.trial['policies'][name] for name in changed)
        for forbidden in ('C:\\', 'Sheeplark', 'Remote Desktop Commander', 'MCP', 'ChatGPT'):
            self.assertNotIn(forbidden, changed_text)

    def test_rejects_promotion_version_schema_or_protected_changes(self):
        mutations = [
            lambda d: d['deployment'].update(status='ACTIVE'),
            lambda d: d['deployment'].update(router_version='5.1'),
            lambda d: d['deployment'].update(router_version='5.2'),
            lambda d: d.update(storage_registry={}),
            lambda d: d['runtime']['stages'].append('LOCAL_GATE'),
            lambda d: d['failures'].update(local_missing='NEW_STATE'),
            lambda d: d['modules']['required_header'].append('Package ID'),
            lambda d: d['controls'].pop(),
        ]
        for policy in self.active['policies'].keys() - LOCAL_BINDING_POLICIES:
            mutations.append(lambda d, p=policy: d['policies'].update({p: 'changed'}))
        for mutate in mutations:
            data = deepcopy(self.trial)
            mutate(data)
            with self.subTest(mutation=mutate), self.assertRaises(CandidateError):
                validate_local_binding_trial(data, ROOT)

    def test_rejects_weakened_binding_and_discarded_discovery(self):
        for policy, old in [('access', 'no automatic Library or Project Sources fallback'),
                            ('access', 'Successful calls alone are not FULL_FILE'),
                            ('access', 'Manifest/hash checks establish consistency, never current authority'),
                            ('discovery', 'Reject paths escaping the root')]:
            data = deepcopy(self.trial)
            data['policies'][policy] = data['policies'][policy].replace(old, 'removed')
            with self.subTest(guard=old), self.assertRaises(CandidateError):
                validate_local_binding_trial(data, ROOT)
        data = deepcopy(self.trial)
        data['policies']['discovery'] = data['policies']['discovery'].split('. ', 1)[1]
        with self.assertRaises(CandidateError):
            validate_local_binding_trial(data, ROOT)


class LocalBindingRetrievalTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='fth-local-trial-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / 'selected package with spaces'
        self.root.mkdir()
        for name in package.CURRENT_FILES + (package.MANIFEST,):
            (self.root / name).write_bytes((ROOT / name).read_bytes())

    def binding(self, **kwargs):
        return LocalTrialHarness(self.root, selected_as_current=True, **kwargs)

    def test_all_seventeen_catalog_ids_resolve_with_existing_headers(self):
        binding = self.binding()
        self.assertEqual(len(binding.catalog), 17)
        for module_id, name in binding.catalog.items():
            with self.subTest(module_id=module_id):
                data, values = binding.module(module_id)
                self.assertEqual(data, (self.root / name).read_bytes())
                self.assertEqual(values['Module ID'], module_id)
                self.assertEqual(values['Runtime role'], 'CURRENT_SOURCE')
                self.assertTrue(values['Domain / Scope'])
                self.assertTrue(values['Authority boundary'])
                self.assertTrue(values['Cross-domain owner boundary'])
                self.assertEqual(values['Load mode'], 'FULL_FILE')

    def test_bootstrap_and_1094_line_record_complete_across_pages(self):
        binding = self.binding()
        for name, data in binding.bootstrap.items():
            self.assertEqual(data, (self.root / name).read_bytes())
        record = '91_RECONCILIATION_RECORD.md'
        data = binding.full_file(record)
        self.assertEqual(data, (self.root / record).read_bytes())
        count = len(data.splitlines())
        self.assertGreater(count, 1000)
        self.assertEqual([r[1:3] for r in binding.reads if r[0] == record],
                         [(0, 1000), (1000, count - 1000)])

    def test_requires_explicit_current_selection_and_available_absolute_root(self):
        for root, selected in [(self.root, False), (self.root / 'missing', True),
                               (Path('relative root'), True)]:
            with self.subTest(root=root), self.assertRaisesRegex(CandidateError, 'SOURCE_LOAD_BLOCKED'):
                LocalTrialHarness(root, selected_as_current=selected)

    def test_missing_bootstrap_blocks(self):
        for name in (package.INDEX, '92_OPEN_ISSUES_CURRENT.md'):
            path = self.root / name
            original = path.read_bytes()
            path.unlink()
            with self.subTest(file=name), self.assertRaisesRegex(CandidateError, 'SOURCE_LOAD_BLOCKED'):
                self.binding()
            path.write_bytes(original)

    def test_missing_catalog_path_and_unknown_id(self):
        binding = self.binding()
        (self.root / binding.catalog['AFM-001']).unlink()
        with self.assertRaisesRegex(CandidateError, 'SOURCE_LOAD_BLOCKED'):
            binding.module('AFM-001')
        with self.assertRaisesRegex(CandidateError, 'REVIEW_REQUIRED'):
            binding.module('AFM-999')

    def test_id_mismatch_wrong_role_missing_scope_or_boundary_and_load(self):
        binding = self.binding()
        path = self.root / binding.catalog['AFM-001']
        original = path.read_bytes()
        variants = [original.replace(b'`AFM-001`', b'`AFM-002`', 1),
                    original.replace(b'`CURRENT_SOURCE`', b'`PROPOSAL`', 1),
                    original.replace(b'`FULL_FILE`', b'`NODE_OR_FULL`', 1)]
        for field in ('Domain / Scope', 'Authority boundary', 'Cross-domain owner boundary'):
            variants.append(b''.join(line for line in original.splitlines(keepends=True)
                                     if not line.startswith(f'> {field}:'.encode())))
        for number, data in enumerate(variants):
            path.write_bytes(data)
            with self.subTest(variant=number), self.assertRaisesRegex(CandidateError, 'REVIEW_REQUIRED'):
                binding.module('AFM-001')

    def test_duplicate_catalog_id_requires_review(self):
        path = self.root / package.INDEX
        data = path.read_bytes()
        row = next(line for line in data.splitlines(keepends=True) if line.startswith(b'| `AFM-001` |'))
        path.write_bytes(data.replace(row, row + row, 1))
        with self.assertRaisesRegex(CandidateError, 'REVIEW_REQUIRED'):
            self.binding()

    def test_stale_or_mixed_generation_fails_existing_manifest_check(self):
        path = self.root / '92_OPEN_ISSUES_CURRENT.md'
        path.write_bytes(path.read_bytes() + b'\nDisposable stale generation\n')
        with self.assertRaisesRegex(CandidateError, 'SOURCE_LOAD_BLOCKED: package consistency'):
            self.binding()

    def test_path_escape_and_absolute_paths_block(self):
        binding = self.binding()
        outside = self.root.parent / 'outside.md'
        outside.write_text('not an admitted source', encoding='utf-8')
        for path in ('../outside.md', str(outside)):
            with self.subTest(path=path), self.assertRaisesRegex(CandidateError, 'SOURCE_LOAD_BLOCKED'):
                binding.full_file(path)
        binding.catalog['AFM-001'] = '../outside.md'
        with self.assertRaisesRegex(CandidateError, 'SOURCE_LOAD_BLOCKED'):
            binding.module('AFM-001')

    def test_incomplete_out_of_order_changed_total_and_truncated_content_block(self):
        binding = self.binding()
        record = '91_RECONCILIATION_RECORD.md'
        def incomplete(path, offset, limit):
            start, total, lines = read_page(path, offset, limit)
            return start, total, lines[:-1]
        def wrong_offset(path, offset, limit):
            start, total, lines = read_page(path, offset, limit)
            return start + 1, total, lines
        def changed_total(path, offset, limit):
            start, total, lines = read_page(path, offset, limit)
            return start, total + bool(offset), lines
        def truncated(path, offset, limit):
            start, total, lines = read_page(path, offset, limit)
            return start, total, [b'' for line in lines]
        for reader in (incomplete, wrong_offset, changed_total, truncated):
            binding.reader = reader
            with self.subTest(reader=reader.__name__), self.assertRaisesRegex(CandidateError, 'SOURCE_LOAD_BLOCKED'):
                binding.full_file(record)

    def test_file_change_during_pagination_blocks(self):
        binding = self.binding()
        def changing(path, offset, limit):
            page = read_page(path, offset, limit)
            if offset:
                path.write_bytes(path.read_bytes() + b'\nChanged during test\n')
            return page
        binding.reader = changing
        with self.assertRaisesRegex(CandidateError, 'SOURCE_LOAD_BLOCKED: source changed'):
            binding.full_file('91_RECONCILIATION_RECORD.md')

    def test_local_read_failure_stops_without_an_alternate_read(self):
        binding = self.binding()
        reader = Mock(side_effect=OSError('local binding unavailable'))
        binding.reader = reader
        with self.assertRaisesRegex(CandidateError, 'SOURCE_LOAD_BLOCKED: local read failed'):
            binding.module('AFM-001')
        reader.assert_called_once_with(binding.root / binding.catalog['AFM-001'], 0, 1000)

    def test_five_regression_specs_retrieve_inputs_without_claiming_model_results(self):
        binding = self.binding()
        suite = json.loads(PROBES.read_text(encoding='utf-8'))
        active = load(ROOT / ROUTER)
        trial = load(ROOT / LOCAL_BINDING_TRIAL)
        self.assertFalse(suite['model_executed'])
        self.assertEqual(suite['status'], 'DRAFT')
        self.assertEqual({p['id'] for p in suite['probes']},
                         {'single-owner', 'cross-domain', 'reconciliation', 'open-state', 'anti-drift-dependency'})
        for probe in suite['probes']:
            with self.subTest(probe=probe['id']):
                self.assertEqual(probe['runtime_result'], 'NOT_RUN')
                self.assertTrue(probe['input'] and probe['expected'])
                sources = {mid: binding.module(mid) for mid in probe['module_ids']}
                self.assertTrue(sources)
                for marker in probe.get('open_markers', []):
                    self.assertIn(marker, binding.bootstrap['92_OPEN_ISSUES_CURRENT.md'].decode('utf-8'))
                if probe.get('record_required'):
                    record = binding.full_file('91_RECONCILIATION_RECORD.md').decode('utf-8')
                    self.assertIn(probe['record_marker'], record)
                for policy in ('module_gate', 'authority', 'dependencies', 'loading', 'overlays', 'coverage'):
                    self.assertEqual(trial['policies'][policy], active['policies'][policy])
                if probe.get('selected_controls'):
                    for router in (active, trial):
                        self.assertEqual(expand(router['controls'], probe['selected_controls'],
                                                probe['true_conditions']), probe['expected_controls'])


if __name__ == '__main__':
    unittest.main()

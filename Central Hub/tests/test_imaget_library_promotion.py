"""STATIC identities/integrity and declared SPEC fixtures; no model, Library or image calls."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import unittest

from test_hub_contracts import ROOT, Closed, load, approval_oracle
from test_imaget_library_candidate import EXPECTED, selection_spec

# Exact pre-namespace release assertions; successor contracts are covered in test_canonical_namespace.py.
NAMESPACE_PREDECESSOR = Path(__file__).resolve().parents[1] / 'Source_archive/Canonical namespace migration 2026-11-11'

# Exact predecessor release assertions; active SEARCH has separate promotion coverage.
SEARCH_PREDECESSOR = Path(__file__).resolve().parents[1] / 'Source_archive/AIS SEARCH promotion 2026-11-09'

BASELINE = '2898d2358f6b3eebd4de65e78d5033af7c27dd12'
PACKAGE = 'HUB-PKG-IMAGET'
LIBRARY = NAMESPACE_PREDECESSOR / 'library_modules'
ARCHIVE = ROOT / 'Source_archive/ImageT Library promotion 2026-11-09'


def resolve_core(manifest, operation='CREATE'):
    """Local byte/read validation, not a Library retrieval implementation."""
    rows = {row['module_id']: row for row in manifest['core']}
    if len(rows) != len(manifest['core']):
        raise Closed('duplicate identity')
    done, pending = set(), set()

    def visit(identity):
        if identity in pending or identity not in rows:
            raise Closed('cycle/missing dependency')
        if identity in done:
            return
        row = rows[identity]
        pending.add(identity)
        path = (LIBRARY / row['file']).resolve()
        if not path.is_relative_to(LIBRARY.resolve()) or not path.is_file():
            raise Closed('missing/outside Library source layout')
        if hashlib.sha256(path.read_bytes()).hexdigest() != row['sha256']:
            raise Closed('corrupt bytes')
        actual = identity_of(path)
        for key in ('module_id', 'package_id', 'runtime_role', 'status', 'version'):
            if actual[key] != row[key]:
                raise Closed('identity/version mismatch')
        if row['status'] != 'ACTIVE' or not row['active'] or row['package_id'] != PACKAGE:
            raise Closed('inactive/wrong package')
        for dependency in row['requires']:
            visit(dependency)
        pending.remove(identity)
        done.add(identity)

    for row in rows.values():
        if operation in row['required_for']:
            visit(row['module_id'])
    return done


def identity_of(path):
    from test_imaget_library_candidate import read_identity
    return read_identity(path)


def visual_spec(*, fidelity=True, objective=None, objective_met=True, visible=True,
                invariant_failed=False, requested_delta=(), authorized_delta=()):
    """Declared evidence/authority only; never infers perception from pixels or language."""
    if not visible:
        result = 'UNVERIFIABLE'
    elif not fidelity or (objective is not None and not objective_met):
        result = 'STRUCTURAL_FAIL' if invariant_failed else 'LOCAL_FAIL'
    else:
        result = 'PASS'
    delta = set(requested_delta)
    allowed = set(authorized_delta)
    return dict(result=result, correction=delta if result == 'LOCAL_FAIL' and delta <= allowed else set(),
                decision_needed=bool(result == 'LOCAL_FAIL' and delta - allowed), calls=0)


class ImageTLibraryPromotionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = load(LIBRARY / 'HUB-IMAGET-MANIFEST_v2.3.0.yaml')
        cls.catalog = load(LIBRARY / 'HUB-CATALOG-IMAGET_v0.1.yaml')
        cls.controller = (LIBRARY / 'HUB-IMAGET-CONTROLLER_v1.3.md').read_text(encoding='utf-8')

    def test_P01_exactly_one_library_binding_and_unrelated_owners_unchanged(self):
        root = load(SEARCH_PREDECESSOR / 'HUB_PACKAGE_CATALOG_v1.14.yaml')
        entries = [p for p in root['packages'] if p['package_id'] == PACKAGE]
        self.assertEqual(len(entries), 1)
        entry = entries[0]
        self.assertEqual((entry['binding_mode'], entry['entrypoint_module_id'], entry['version']),
                         ('LIBRARY_MODULE', 'HUB-PIPE-IMAGET', '1.3'))
        self.assertEqual(entry['location']['class'], 'LIBRARY')
        self.assertNotIn('declared_source_path', entry['location'])
        self.assertEqual(entry['local_catalog']['version'], '0.1')
        self.assertEqual(entry['project_deployment'], 'NOT_PERFORMED')
        before = load(ARCHIVE / 'HUB_PACKAGE_CATALOG_v1.13.yaml')
        self.assertEqual([p for p in root['packages'] if p['package_id'] != PACKAGE],
                         [p for p in before['packages'] if p['package_id'] != PACKAGE])
        old_router = (ARCHIVE / 'HUB_ROUTER_v1.1.yaml').read_bytes()
        self.assertEqual((SEARCH_PREDECESSOR / 'HUB_ROUTER_v1.1.yaml').read_bytes(), old_router.replace(b'1.13', b'1.14'))

    def test_P02_P04_active_objects_integrity_and_fail_closed(self):
        for identity, version, role, ext in EXPECTED:
            version = version.removesuffix('-candidate')
            path = LIBRARY / f'{identity}_v{version}.{ext}'
            actual = identity_of(path)
            self.assertEqual((actual['module_id'], actual['package_id'], actual['runtime_role'],
                              actual['status'], actual['version']),
                             (identity, PACKAGE, role, 'ACTIVE', version))
        self.assertEqual(len(resolve_core(self.manifest)), 5)
        self.assertNotIn('HUB-IMAGET-READY-GATE', resolve_core(self.manifest, 'ANALYZE'))
        for mutation in ('cycle', 'hash', 'version', 'missing', 'duplicate'):
            bad = copy.deepcopy(self.manifest)
            row = bad['core'][0]
            if mutation == 'cycle': row['requires'].append(row['module_id'])
            if mutation == 'hash': row['sha256'] = '0' * 64
            if mutation == 'version': row['version'] = 'wrong'
            if mutation == 'missing': row['file'] = 'missing.md'
            if mutation == 'duplicate': bad['core'].append(copy.deepcopy(row))
            with self.subTest(mutation=mutation), self.assertRaises(Closed):
                resolve_core(bad)

    def test_P03_separate_inventories_and_conditional_preference(self):
        self.assertNotIn('entries', self.manifest)
        self.assertEqual(self.manifest['runtime_role'], 'PIPELINE_MANIFEST')
        self.assertEqual(len(self.catalog['entries']), 2)
        for row in self.catalog['entries']:
            actual = identity_of(LIBRARY / row['location']['artifact'])
            for key in ('module_id', 'package_id', 'runtime_role', 'version', 'status'):
                self.assertEqual(actual[key], row[key])
            self.assertEqual(row['requires'], [])
            self.assertIsNone(row['location']['library_file_id'])
        preference = self.catalog['entries'][1]
        self.assertEqual(preference['activation'], 'explicit_current_operation_only')
        root = load(SEARCH_PREDECESSOR / 'HUB_PACKAGE_CATALOG_v1.14.yaml')
        for leaf in self.catalog['entries']:
            self.assertNotIn(leaf['module_id'], str(root))

    def test_P05_rollback_and_archives_byte_exact(self):
        legacy = ROOT / 'tool_pipelines/ImageT'
        for path in legacy.rglob('*'):
            if path.is_file():
                rel = path.relative_to(ROOT).as_posix()
                self.assertEqual(path.read_bytes(), subprocess.check_output(
                    ['git', 'show', BASELINE + ':Central Hub/' + rel], cwd=ROOT), rel)
        receipt = json.loads((ARCHIVE / 'ARCHIVE_RECEIPT.json').read_text(encoding='utf-8'))
        self.assertEqual(len(receipt), 13)
        for rel, digest in receipt.items():
            data = (ARCHIVE / rel).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), digest, rel)
            self.assertEqual(data, subprocess.check_output(
                ['git', 'show', BASELINE + ':Central Hub/' + rel], cwd=ROOT), rel)
            if rel != 'HUB_ROUTER_v1.1.yaml': self.assertFalse((ROOT / rel).exists())

    def test_O01_O04_existing_selection_oracle_on_active_metadata(self):
        construction = 'HUB-IMAGET-HUMANOID-CONSTRUCTION'
        preference = 'HUB-IMAGET-HUMANOID-DESIGN-PREFERENCE'
        payload = 'ACCEPTED: coat. PROVISIONAL: A/B. REJECTED: trim. OPEN: material.'
        for humanoid, authority, fields, delegated, expected in (
                (True, 'RAW', {'overlap'}, set(), {construction: {'overlap'}}),
                (True, 'PRESERVED_AUTHORED', {'material'}, set(), {}),
                (True, 'PRESERVED_AUTHORED', {'overlap', 'identity'}, {'overlap'}, {construction: {'overlap'}}),
                (False, 'RAW', {'overlap'}, set(), {})):
            result = selection_spec(self.catalog, humanoid=humanoid, authority=authority, need=True,
                                    fields=fields, delegated=delegated, payload=payload, expected_status='ACTIVE')
            self.assertEqual(result['selected'], expected)
            self.assertEqual(result['payload'], payload)
            self.assertEqual(result['new_field_authority'], set())
        result = selection_spec(self.catalog, humanoid=True, authority='PRESERVED_AUTHORED',
                                fields={'overlap'}, preference_fields={'overlap', 'pose'}, expected_status='ACTIVE')
        self.assertEqual(result['selected'], {preference: {'overlap'}})

    def test_O05_catalog_growth_does_not_change_core_or_root_structure(self):
        before = copy.deepcopy(self.manifest)
        growth = copy.deepcopy(self.catalog)
        growth['version'] = '0.2'
        growth['entries'].append({'module_id': 'TEST-ONLY-LEAF', 'package_id': PACKAGE})
        self.assertEqual(self.manifest, before)
        self.assertNotIn('TEST-ONLY-LEAF', str(self.manifest))
        self.assertNotEqual(growth['version'], self.catalog['version'])  # Exact Catalog deployment pin must refresh.

    def test_V01_density_alone_is_not_failure(self):
        self.assertIn('HIGH DETAIL != AUTOMATIC FAILURE', self.controller)
        self.assertEqual(visual_spec(objective='subject primary')['result'], 'PASS')

    def test_V02_competition_can_fail_at_any_density(self):
        self.assertIn('DETAIL DENSITY != VISUAL COMPETITION', self.controller)
        self.assertEqual(visual_spec(objective='subject primary', objective_met=False)['result'], 'LOCAL_FAIL')

    def test_V03_intentional_uniform_flat_design_is_preserved(self):
        self.assertIn('Preserve authorized uniform density, flat hierarchy, multiple equal elements', self.controller)
        self.assertEqual(visual_spec(objective='uniform density and flat hierarchy')['result'], 'PASS')

    def test_V04_visual_quality_cannot_compensate_fidelity_failure(self):
        self.assertIn('BEAUTIFUL OUTPUT != CORRECT OUTPUT', self.controller)
        for violation in ('count', 'reference role', 'preservation'):
            with self.subTest(violation=violation):
                self.assertEqual(visual_spec(fidelity=False, invariant_failed=True)['result'], 'STRUCTURAL_FAIL')

    def test_V05_bounded_delta_and_locked_field_decision(self):
        for allowed, expected, decision in (({'background_contrast'}, {'background_contrast'}, False),
                                            (set(), set(), True)):
            result = visual_spec(objective='subject primary', objective_met=False,
                                 requested_delta={'background_contrast'}, authorized_delta=allowed)
            self.assertEqual(result['correction'], expected)
            self.assertEqual(result['decision_needed'], decision)
            self.assertEqual(result['calls'], 0)
        self.assertIn('surface the conflict and needed user decision', self.controller)

    def test_V06_no_retry_without_new_approval(self):
        self.assertIn('NEW Ready Snapshot and NEW approval before ONE new call', self.controller)
        self.assertEqual(approval_oracle('APPROVED', 'submit'), ('CONSUMED', True))
        self.assertEqual(approval_oracle('CONSUMED', 'submit')[1], False)
        self.assertEqual(approval_oracle('PENDING_APPROVAL', 'approve_current'), ('APPROVED', False))
        self.assertEqual(approval_oracle('APPROVED', 'submit'), ('CONSUMED', True))
        ready = (LIBRARY / 'HUB-IMAGET-READY-GATE_v1.1.md').read_text(encoding='utf-8')
        self.assertIn('no guaranteed byte-exact platform-internal generator prompt is claimed', ready)
        old = (ROOT / 'tool_pipelines/ImageT/READY_GATE_v1.0.md').read_text(encoding='utf-8')
        marker, end = '## Preserved approval protocol', '## Exact submission and invalidation'
        self.assertEqual(old.split(marker)[1].split(end)[0], ready.split(marker)[1].split(end)[0])

    def test_priority_absent_and_hidden_evidence(self):
        self.assertEqual(visual_spec(objective=None, objective_met=False)['result'], 'PASS')
        self.assertEqual(visual_spec(visible=False)['result'], 'UNVERIFIABLE')
        self.assertIn('If no priority was established, impose none.', self.controller)


if __name__ == '__main__':
    unittest.main()

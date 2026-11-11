"""Current successor contracts and declared fixtures; no live Library/model execution.

Namespace migration assertions retain exact historical revisions. Phase 1
assertions check the active bindings and its scoped successor separately.
"""
import copy
import hashlib
import json
from pathlib import Path
import re
import subprocess
import unittest

from test_hub_contracts import ROOT, Closed, load
from test_hub_router_candidate import synthetic_module, synthetic_fixture, simulate
from test_imaget_library_candidate import read_identity, selection_spec


BASELINE = 'c818c1954c0a54b2f777687e07e4ae32530f1845'
ARCHIVE = ROOT / 'Source_archive/Canonical namespace migration 2026-11-11'
LIBRARY = ROOT / 'library_modules'
PHASE_1_ARCHIVE = ROOT / 'Source_archive/Concept Entry Phase 1 2026-11-12'
PHASE_1_BASELINE = '9e3194b552d669c031c245a0f0190992da768355'
ENTRY_16 = 'library_modules/Concept Development/HUB-CON-ENTRY_v1.6.md'
ENTRY_17 = 'library_modules/Concept Development/HUB-CON-ENTRY_v1.7.md'
# Independent approved identity/version expectations, not inferred from filenames.
EXPECTED = [
    ('HUB-DOM-TECHNICAL', 'HUB-TECH-ENTRY', '1.1'),
    ('HUB-DOM-CONCEPT-DEVELOPMENT', 'HUB-CON-ENTRY', '1.6'),
    ('HUB-CATALOG-CONCEPT-DEVELOPMENT', 'HUB-CON-CATALOG', '1.6'),
    ('HUB-DOM-CREATIVE', 'HUB-CON-GEN-CREATIVE', '1.2'),
    ('HUB-CAP-BRAINSTORM', 'HUB-CON-GEN-BRAINSTORM', '1.2'),
    ('HUB-CAP-DEBATE', 'HUB-CON-GEN-DEBATE', '1.1'),
    ('HUB-DOM-NAMING', 'HUB-CON-GEN-NAMING', '1.1'),
    ('HUB-DOM-ANTI-PRIOR', 'HUB-CON-AD-ANTI-PRIOR', '1.2'),
    ('HUB-DOM-MODULAR-CONCEPT-ARCHITECTURE', 'HUB-CON-AD-MODULAR-CONCEPT-ARCHITECTURE', '1.3'),
    ('HUB-DOM-WORLDBUILDING-INTERNAL-LOGIC', 'HUB-CON-AD-WORLDBUILDING-INTERNAL-LOGIC', '1.2'),
    ('HUB-DOM-ACTOR-RECEPTION', 'HUB-CON-AD-ACTOR-RECEPTION', '1.1'),
    ('HUB-DOM-NARRATIVE-RESOLUTION', 'HUB-CON-AD-NARRATIVE-RESOLUTION', '1.1'),
    ('HUB-CAP-AUTHORING', 'HUB-AUTH-ENTRY', '0.9'),
    ('HUB-DOM-SHOPPING', 'HUB-SHOP-ENTRY', '1.1'),
    ('HUB-CATALOG-SHOPPING', 'HUB-SHOP-CATALOG', '1.1'),
    ('HUB-PROC-SHOPPING-SEARCH', 'HUB-SHOP-SEARCH', '1.1'),
    ('HUB-PIPE-IMAGET', 'HUB-IMAGET-ENTRY', '1.4'),
    ('HUB-CATALOG-IMAGET', 'HUB-IMAGET-CATALOG', '0.2'),
    ('HUB-IMAGET-MANIFEST', 'HUB-IMAGET-CORE-MANIFEST', '2.4.0'),
    ('HUB-IMAGET-CONTROLLER', 'HUB-IMAGET-CORE-CONTROLLER', '1.4'),
    ('HUB-IMAGET-ROUTER', 'HUB-IMAGET-CORE-ROUTER', '3.3.0'),
    ('HUB-IMAGET-READY-GATE', 'HUB-IMAGET-CORE-READY-GATE', '1.2'),
    ('HUB-IMAGET-ANTI-PRIOR', 'HUB-IMAGET-AD-ANTI-PRIOR', '1.3.0'),
    ('HUB-IMAGET-ANTI-DRIFT', 'HUB-IMAGET-AD-ANTI-DRIFT', '2.2.0'),
    ('HUB-IMAGET-HUMANOID-CONSTRUCTION', 'HUB-IMAGET-HUM-CONSTRUCTION', '0.2'),
    ('HUB-IMAGET-HUMANOID-DESIGN-PREFERENCE', 'HUB-IMAGET-HUM-DESIGN-PREFERENCE', '0.3'),
]
IDS = {old: new for old, new, _ in EXPECTED}
PACKAGE_TOKENS = {
    'HUB-PKG-TECHNICAL': 'TECH',
    'HUB-PKG-CONCEPT-DEVELOPMENT': 'CON',
    'HUB-PKG-AUTHORING': 'AUTH',
    'HUB-PKG-IMAGET': 'IMAGET',
    'HUB-PKG-SHOPPING': 'SHOP',
}


def active_inventory(paths):
    inventory = {}
    for path in paths:
        header = read_identity(path)
        identity = header['module_id']
        assert identity not in inventory, f'duplicate identity: {identity}'
        assert identity in IDS.values(), f'unapproved active identity: {identity}'
        assert identity.split('-')[1] == PACKAGE_TOKENS.get(header['package_id']), identity
        assert header['status'] == 'ACTIVE', identity
        assert path.name == f"{identity}_v{header['version']}{path.suffix}", path
        inventory[identity] = (path, header)
    return inventory


def bound_artifact(inventory, row, identity_key='module_id', path_key=None):
    identity = row[identity_key]
    assert identity in inventory, f'unresolved identity: {identity}'
    path, header = inventory[identity]
    for field in ('package_id', 'runtime_role', 'status', 'version'):
        assert row[field] == header[field], f'{identity}: {field} mismatch'
    relative = row[path_key] if path_key else row['location']['artifact']
    assert LIBRARY / relative == path and path.is_file(), f'{identity}: missing or wrong file'



def core_closure(manifest, operation):
    """Declared inventory graph oracle, independent of prose or Library lookup."""
    rows = {r['module_id']: r for r in manifest['core']}
    done, visiting = set(), set()

    def visit(identity):
        if identity in visiting or identity not in rows:
            raise Closed('missing or cyclic required core')
        if identity in done:
            return
        visiting.add(identity)
        for target in rows[identity]['requires']:
            visit(target)
        visiting.remove(identity)
        done.add(identity)

    for row in rows.values():
        if operation in row['required_for']:
            visit(row['module_id'])
    return done


class CanonicalNamespaceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.receipt = json.loads((ARCHIVE / 'ARCHIVE_RECEIPT.json').read_text(encoding='utf-8'))
        cls.rows = {r['old_id']: r for r in cls.receipt if 'old_id' in r}
        cls.current = {}
        for row in cls.rows.values():
            base = PHASE_1_ARCHIVE if row['new'] == ENTRY_16 else ROOT
            path = base / row['new']
            cls.current[row['new_id']] = (path, read_identity(path))
        cls.root = load(PHASE_1_ARCHIVE / 'HUB_PACKAGE_CATALOG_v1.18.yaml')
        cls.old_root = load(ARCHIVE / 'HUB_PACKAGE_CATALOG_v1.17.yaml')
        cls.manifest = load(LIBRARY / 'ImageT/Core/HUB-IMAGET-CORE-MANIFEST_v2.4.0.yaml')

    def rename(self, value):
        if isinstance(value, str):
            for old, new in sorted(IDS.items(), key=lambda x: len(x[0]), reverse=True):
                value = re.sub(r'(?<![A-Z0-9-])' + re.escape(old) + r'(?![A-Z0-9-])', new, value)
            return value
        if isinstance(value, list):
            return [self.rename(v) for v in value]
        if isinstance(value, dict):
            return {k: self.rename(v) for k, v in value.items()}
        return value

    def test_approved_mapping_unique_headers_versions_and_layout(self):
        self.assertEqual(set(self.rows), set(IDS))
        files = [p for p in LIBRARY.rglob('*') if p.is_file()]
        self.assertEqual(len(files), 26)
        identities = [read_identity(p)['module_id'] for p in files]
        self.assertEqual(len(set(identities)), 26)
        for old, new, version in EXPECTED:
            row = self.rows[old]
            path, header = self.current[new]
            self.assertEqual((row['new_id'], header['module_id'], header['version']), (new, new, version))
            self.assertEqual(path.name, f'{new}_v{version}{path.suffix}')
            before = read_identity(ARCHIVE / row['old'])
            for field in ('package_id', 'runtime_role', 'status'):
                self.assertEqual(header[field], before[field])
            self.assertFalse((ROOT / row['old']).exists())
            package_folder = {'TECH': 'Technical', 'CON': 'Concept Development', 'AUTH': 'Authoring',
                              'SHOP': 'Shopping', 'IMAGET': 'ImageT'}[new.split('-')[1]]
            library = PHASE_1_ARCHIVE / 'library_modules' if row['new'] == ENTRY_16 else LIBRARY
            self.assertEqual(path.relative_to(library).parts[0], package_folder)
            for token, folder in (('-GEN-', 'General'), ('-AD-', 'Anti Drift'), ('-HUM-', 'Humanoid')):
                if token in new:
                    self.assertEqual(path.parent.name, folder)
            if new.startswith('HUB-IMAGET-CORE-'):
                self.assertEqual(path.parent.name, 'Core')

    def test_exact_root_bindings_and_unchanged_admission(self):
        self.assertEqual(len(self.root['packages']), 6)
        for old, current in zip(self.old_root['packages'], self.root['packages']):
            for key in ('package_id', 'runtime_role', 'status', 'applicability', 'requires', 'binding_mode'):
                self.assertEqual(current[key], old[key])
            if old['binding_mode'] == 'LEGACY_PROJECT_SOURCE':
                self.assertEqual(current, old)
                continue
            self.assertEqual(current['entrypoint_module_id'], IDS[old['entrypoint_module_id']])
            for binding, key in [(current, 'entrypoint_module_id')] + (
                    [(current['local_catalog'], 'module_id')] if current['local_catalog'] else []):
                path, identity = self.current[binding[key]]
                for field in ('package_id', 'runtime_role', 'status', 'version'):
                    self.assertEqual(binding[field], identity[field])
                self.assertEqual(Path('library_modules') / binding['location']['artifact'],
                                 path.relative_to(PHASE_1_ARCHIVE if path.is_relative_to(PHASE_1_ARCHIVE) else ROOT))
                self.assertEqual(binding['location']['root'], 'Central Hub Config')
                for field in ('library_file_id', 'library_version_id', 'observed_path', 'locator'):
                    self.assertIsNone(binding['location'][field])
                self.assertEqual(binding['location']['verification'], 'NAMESPACE_SUCCESSOR_NOT_VERIFIED')

    def test_catalog_membership_relations_and_resolvable_targets(self):
        for identity in ('HUB-CON-CATALOG', 'HUB-SHOP-CATALOG', 'HUB-IMAGET-CATALOG'):
            current = load(self.current[identity][0])
            row = next(r for r in self.rows.values() if r['new_id'] == identity)
            before = load(ARCHIVE / row['old'])
            self.assertEqual(len(current['entries']), len(before['entries']))
            for old, entry in zip(before['entries'], current['entries']):
                self.assertEqual(entry['module_id'], IDS[old['module_id']])
                path, header = self.current[entry['module_id']]
                for field in ('module_id', 'package_id', 'runtime_role', 'status', 'version'):
                    self.assertEqual(entry[field], header[field])
                self.assertEqual(LIBRARY / entry['location']['artifact'], path)
                for field in ('requires', 'refines', 'complements'):
                    self.assertEqual(entry.get(field, []), self.rename(old.get(field, [])))
                    for target in entry.get(field, []):
                        self.assertIn(target['module_id'] if isinstance(target, dict) else target, self.current)
        ar = self.current['HUB-CON-AD-ACTOR-RECEPTION'][0].read_text(encoding='utf-8')
        self.assertEqual(re.findall(r'^Requires: (.+)$', ar, re.M),
                         ['HUB-CON-AD-MODULAR-CONCEPT-ARCHITECTURE'])

    def test_markdown_behavior_exact_except_authorized_identity_revision_references(self):
        for row in self.rows.values():
            path = self.current[row['new_id']][0]
            if path.suffix != '.md':
                continue
            expected = (ARCHIVE / row['old']).read_text(encoding='utf-8')
            for reference in sorted(self.rows.values(), key=lambda r: len(r['old']), reverse=True):
                expected = expected.replace(reference['old'], reference['new'])
                expected = expected.replace(Path(reference['old']).name, Path(reference['new']).name)
            expected = self.rename(expected)
            expected = re.sub(r'(?m)^Version: ' + re.escape(row['old_version']) + r'$',
                              'Version: ' + row['new_version'], expected)
            expected = re.sub(r'(?m)^(#.*?\bv)' + re.escape(row['old_version']) + r'$',
                              lambda m: m[1] + row['new_version'], expected)
            if row['new_id'] == 'HUB-CON-ENTRY':
                expected = expected.replace('exact ACTIVE/1.5 HUB-CON-CATALOG', 'exact ACTIVE/1.6 HUB-CON-CATALOG')
            if row['new_id'] == 'HUB-SHOP-ENTRY':
                expected = expected.replace('PACKAGE_CATALOG, ACTIVE/1.0', 'PACKAGE_CATALOG, ACTIVE/1.1')
            if row['new_id'] == 'HUB-IMAGET-ENTRY':
                expected = expected.replace('/ PIPELINE_MANIFEST / 2.3.0', '/ PIPELINE_MANIFEST / 2.4.0')
            self.assertEqual(path.read_text(encoding='utf-8'), expected, row['new_id'])

    def test_yaml_behavior_except_declared_identity_location_and_hash_fields(self):
        def behavior(value):
            if isinstance(value, list):
                return [behavior(v) for v in value]
            if isinstance(value, dict):
                return {k: behavior(v) for k, v in value.items()
                        if k not in {'version', 'location', 'file', 'sha256', 'manifest'}}
            return value
        for row in self.rows.values():
            if not row['new'].endswith('.yaml'):
                continue
            before = load(ARCHIVE / row['old'])
            current = load(ROOT / row['new'])
            self.assertEqual(behavior(current), behavior(self.rename(before)), row['new_id'])

    def test_manifest_exact_files_hashes_and_operation_closure(self):
        old = load(ARCHIVE / self.rows['HUB-IMAGET-MANIFEST']['old'])
        for row in self.manifest['core']:
            path, header = self.current[row['module_id']]
            self.assertEqual(LIBRARY / row['file'], path)
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), row['sha256'])
            for field in ('package_id', 'runtime_role', 'status', 'version'):
                self.assertEqual(header[field], row[field])
        for operation in ('ANALYZE', 'CREATE', 'EDIT', 'VARIATION', 'CORRECT', 'RETRY'):
            current = core_closure(self.manifest, operation)
            self.assertEqual(current, {IDS[x] for x in core_closure(old, operation)})
            self.assertIn('HUB-IMAGET-AD-ANTI-DRIFT', current)
            self.assertIn('HUB-IMAGET-AD-ANTI-PRIOR', current)
            self.assertEqual('HUB-IMAGET-CORE-READY-GATE' in current, operation != 'ANALYZE')
        self.assertIsNone(self.manifest['integrity']['self_hash'])
        self.assertEqual(self.manifest['source_name_aliases']['config.md'], 'HUB-IMAGET-AD-ANTI-DRIFT')
        router = load(self.current['HUB-IMAGET-CORE-ROUTER'][0])
        self.assertEqual(LIBRARY / router['manifest'], self.current['HUB-IMAGET-CORE-MANIFEST'][0])

    def test_core_failures_do_not_change_required_graph(self):
        for mutation in ('missing', 'cycle'):
            manifest = copy.deepcopy(self.manifest)
            if mutation == 'missing':
                manifest['core'][0]['requires'].append('MISSING')
            else:
                manifest['core'][0]['requires'].append(manifest['core'][0]['module_id'])
            with self.assertRaises(Closed):
                core_closure(manifest, 'CREATE')

    def test_current_humanoid_authority_and_no_cross_leaf_dependency(self):
        catalog = load(self.current['HUB-IMAGET-CATALOG'][0])
        for entry in catalog['entries']:
            self.assertEqual(entry['requires'], [])
        for humanoid, authority, fields, delegated, preference, need, expected in [
            (False, 'RAW', {'shape'}, (), (), True, set()),
            (True, 'PRESERVED_AUTHORED', {'shape'}, (), (), True, set()),
            (True, 'RAW', {'shape'}, (), (), True, {'HUB-IMAGET-HUM-CONSTRUCTION'}),
            (True, 'PRESERVED_AUTHORED', {'shape'}, (), {'shape'}, False,
             {'HUB-IMAGET-HUM-DESIGN-PREFERENCE'}),
        ]:
            result = selection_spec(catalog, humanoid=humanoid, authority=authority, fields=fields,
                                    delegated=delegated, preference_fields=preference, need=need,
                                    expected_status='ACTIVE')
            self.assertEqual(set(result['selected']), expected)
            self.assertEqual(result['new_field_authority'], set())

    def test_current_concept_requires_closure_and_missing_dependency_isolation(self):
        package = 'HUB-PKG-CONCEPT-DEVELOPMENT'
        core = synthetic_module('HUB-CON-ENTRY', package, {'CORE'}, version='1.6')
        fixture = synthetic_fixture(core)
        catalog = synthetic_module('HUB-CON-CATALOG', package, set(), role='PACKAGE_CATALOG', version='1.6')
        fixture['packages'][0]['local_catalog'] = catalog
        fixture['artifacts'][catalog['module_id']] = [dict(catalog, read_kind='FULL_FILE')]
        entries = load(self.current['HUB-CON-CATALOG'][0])['entries']
        leaves = [synthetic_module(r['module_id'], package, {r['module_id']}, role=r['runtime_role'],
                                   version=r['version'], requires=copy.deepcopy(r['requires'])) for r in entries]
        fixture['local_catalogs'][package] = leaves
        fixture['packages'][0]['applicability'] = {r['module_id'] for r in entries}
        for leaf in leaves:
            fixture['artifacts'][leaf['module_id']] = [dict(leaf, read_kind='FULL_FILE')]
        ar, mca = 'HUB-CON-AD-ACTOR-RECEPTION', 'HUB-CON-AD-MODULAR-CONCEPT-ARCHITECTURE'
        result = simulate(fixture, {ar})
        self.assertEqual({identity for _, identity in result['spec_verified']}, {ar, mca})
        fixture['artifacts'].pop(mca)
        result = simulate(fixture, {ar, 'HUB-CON-AD-NARRATIVE-RESOLUTION'})
        self.assertTrue(result['blocked'])
        self.assertIn((package, ar), result['blocked'])
        self.assertIn((package, 'HUB-CON-AD-NARRATIVE-RESOLUTION'), result['spec_verified'])
        self.assertFalse(result['runtime_ready'])

    def test_router_only_pins_change_and_shared_contract_sections_preserved(self):
        before = (ARCHIVE / 'HUB_ROUTER_v1.1.yaml').read_bytes()
        self.assertEqual((PHASE_1_ARCHIVE / 'HUB_ROUTER_v1.1.yaml').read_bytes(), before.replace(b'1.17', b'1.18'))
        old = (ARCHIVE / 'HUB_ARCHITECTURE_v1.17.md').read_text(encoding='utf-8')
        current = (PHASE_1_ARCHIVE / 'HUB_ARCHITECTURE_v1.18.md').read_text(encoding='utf-8')
        for number in (5, 7, 8, 9, 10, 13, 14):
            section = lambda text: text.split(f'## {number}. ', 1)[1].split('\n## ', 1)[0]
            self.assertEqual(section(current), self.rename(section(old)).replace('1.17', '1.18'), number)
        for rule in ('HUB-<PACKAGE>-<ARTIFACT>', 'HUB-<PACKAGE>-<SUBDOMAIN>-<ARTIFACT>',
                     'DIRECTORY != ONTOLOGY', 'one-time canonical identity migration',
                     'AD does not mean optional', 'Nested Library folder capability is NOT_VERIFIED'):
            self.assertIn(rule, current)

    def test_unchanged_ci_ais_profile_legacy_and_existing_archives(self):
        paths = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', BASELINE, '--',
                                         'HUB_CI_v1.2.md', 'tool_pipelines', 'shared_resources'],
                                        cwd=ROOT, text=True).splitlines()
        for path in paths:
            relative = path.removeprefix('Central Hub/')
            expected = subprocess.check_output(['git', 'show', f'{BASELINE}:Central Hub/{relative}'], cwd=ROOT)
            if relative == 'shared_resources/USER_PROFILE.md':
                # Installation pointers only; resource identity/schema/access/mutation stay exact.
                expected = expected.replace(b'Architecture 1.17', b'Architecture 1.18').replace(
                    b'Catalog 1.17', b'Catalog 1.18').replace(b'Shopping core 1.0', b'Shopping core 1.1')
                phase_1_baseline = subprocess.check_output(
                    ['git', 'show', f'{PHASE_1_BASELINE}:Central Hub/{relative}'], cwd=ROOT)
                self.assertEqual(phase_1_baseline, expected, relative)
                expected = expected.replace(b'Architecture 1.18, Catalog 1.18', b'Architecture 1.19, Catalog 1.19')
            self.assertEqual((ROOT / relative).read_bytes(), expected, relative)
        # Existing archive JSON may already have checkout CRLF conversion; do not rewrite it.
        unchanged = subprocess.check_output(['git', 'diff', '--name-only', BASELINE, '--',
            'Source_archive', ':(exclude)Source_archive/Canonical namespace migration 2026-11-11',
            ':(exclude)Source_archive/Concept Entry Phase 1 2026-11-12'], cwd=ROOT)
        self.assertEqual(unchanged, b'')

    def test_predecessors_byte_exact_and_not_dual_active(self):
        self.assertEqual(len(self.receipt), 31)
        for row in self.receipt:
            data = (ROOT / row['archive']).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), row['sha256'])
            self.assertEqual(data, subprocess.check_output(['git', 'show', f'{BASELINE}:Central Hub/{row["old"]}'], cwd=ROOT))
        for name in ('HUB_ARCHITECTURE_v1.17.md', 'HUB_PACKAGE_CATALOG_v1.17.yaml'):
            self.assertFalse((ROOT / name).exists())

    def test_no_old_active_identity_and_deployable_flat_names(self):
        pins = load(ROOT / 'HUB_ROUTER_v1.1.yaml')['contracts']
        catalog_path = ROOT / pins['root_catalog']['file']
        catalog = load(catalog_path)
        surfaces = [p for p in LIBRARY.rglob('*') if p.is_file()] + [
            ROOT / 'HUB_CI_v1.2.md', ROOT / pins['architecture']['file'],
            catalog_path, ROOT / 'HUB_ROUTER_v1.1.yaml',
            *ROOT.glob('shared_resources/*.yaml'),
            *ROOT.glob('tool_pipelines/AIS/AIS_PIPELINE_*.md'),
            *ROOT.glob('tool_pipelines/AIS/AIS_ROUTER_*.yaml'),
        ]
        for path in surfaces:
            text = path.read_text(encoding='utf-8')
            for identity in IDS:
                self.assertNotRegex(text, r'(?<![A-Z0-9-])' + re.escape(identity) + r'(?![A-Z0-9-])', str(path))
        self.assertEqual({row['entrypoint_module_id'] for row in catalog['packages']
                          if row['binding_mode'] == 'LEGACY_PROJECT_SOURCE'}, {'HUB-PIPE-AIS'})
        names = [p.name for p, _ in self.current.values()]
        self.assertEqual(len(set(names)), 26)
        document = (ROOT / 'NAMESPACE_MIGRATION.md').read_text(encoding='utf-8')
        self.assertIn('NESTED LIBRARY FOLDER CAPABILITY: NOT_VERIFIED', document)

    def test_current_inventory_and_binding_reject_invalid_successors(self):
        inventory = active_inventory(p for p in LIBRARY.rglob('*') if p.is_file())
        self.assertEqual(set(inventory), set(IDS.values()))
        root = load(ROOT / 'HUB_PACKAGE_CATALOG_v1.19.yaml')
        bound = set()
        for package in root['packages']:
            if package['binding_mode'] == 'LEGACY_PROJECT_SOURCE':
                continue
            bound_artifact(inventory, package, 'entrypoint_module_id')
            bound.add(package['entrypoint_module_id'])
            catalog = package['local_catalog']
            if catalog is None:
                continue
            self.assertEqual(package['package_id'], catalog['package_id'])
            bound_artifact(inventory, catalog)
            bound.add(catalog['module_id'])
            for entry in load(inventory[catalog['module_id']][0])['entries']:
                self.assertEqual(package['package_id'], entry['package_id'])
                bound_artifact(inventory, entry)
                bound.add(entry['module_id'])
        image = next(row for row in root['packages'] if row['entrypoint_module_id'] == 'HUB-IMAGET-ENTRY')
        manifest_path, manifest = inventory['HUB-IMAGET-CORE-MANIFEST']
        self.assertEqual(manifest['package_id'], image['package_id'])
        for field in ('module_id', 'package_id', 'runtime_role'):
            self.assertEqual(manifest['catalog_interface'][field], image['local_catalog'][field])
        entry = inventory['HUB-IMAGET-ENTRY'][0].read_text(encoding='utf-8')
        self.assertIn(f"{manifest_path.name} / {manifest['module_id']} / "
                      f"{manifest['runtime_role']} / {manifest['version']}", entry)
        bound.add(manifest['module_id'])
        for row in self.manifest['core']:
            bound_artifact(inventory, row, path_key='file')
            bound.add(row['module_id'])
        self.assertEqual(bound, set(inventory))
        tech = inventory['HUB-TECH-ENTRY'][0]
        with self.assertRaisesRegex(AssertionError, 'duplicate identity'):
            active_inventory([tech, tech])
        with self.assertRaisesRegex(AssertionError, 'unapproved active identity'):
            active_inventory([tech, ARCHIVE / self.rows['HUB-DOM-TECHNICAL']['old']])
        concept = next(row for row in root['packages'] if row['entrypoint_module_id'] == 'HUB-CON-ENTRY')
        for patch, reason in [
            ({'module_id': 'HUB-CATALOG-CONCEPT-DEVELOPMENT'}, 'unresolved identity'),
            ({'package_id': 'HUB-PKG-SHOPPING'}, 'package_id mismatch'),
        ]:
            with self.assertRaisesRegex(AssertionError, reason):
                bound_artifact(inventory, dict(concept['local_catalog'], **patch))
        with self.assertRaisesRegex(AssertionError, 'missing or wrong file'):
            bound_artifact(inventory, dict(self.manifest['core'][0], file='missing.yaml'), path_key='file')

    def test_smoke_selection_properties_with_declared_scopes(self):
        # Applicability and pipeline authorization are fixture inputs. This does not classify user text.
        root = load(ROOT / 'HUB_PACKAGE_CATALOG_v1.19.yaml')
        def module(row, identity):
            return synthetic_module(identity, row['package_id'], {identity}, row['runtime_role'],
                                    version=row['version'], requires=row.get('requires', []),
                                    refines=row.get('refines', []), complements=row.get('complements', []))

        fixture = synthetic_fixture(*(module(row, row['entrypoint_module_id']) for row in root['packages']))
        for binding, row in zip(fixture['packages'], root['packages']):
            local = row['local_catalog']
            if not local or row['runtime_role'] == 'TOOL_PIPELINE':
                continue  # Pipeline internals use the manifest and authority tests, not generic leaf routing.
            catalog = module(local, local['module_id'])
            binding['local_catalog'] = catalog
            entries = load(LIBRARY / local['location']['artifact'])['entries']
            leaves = [module(entry, entry['module_id']) for entry in entries]
            fixture['local_catalogs'][row['package_id']] = leaves
            for record in [catalog, *leaves]:
                fixture['artifacts'][record['module_id']] = [dict(record, read_kind='FULL_FILE')]

        con, shop, ais, image = 'HUB-CON-ENTRY', 'HUB-SHOP-ENTRY', 'HUB-PIPE-AIS', 'HUB-IMAGET-ENTRY'
        wil, brain = 'HUB-CON-AD-WORLDBUILDING-INTERNAL-LOGIC', 'HUB-CON-GEN-BRAINSTORM'
        prior, actor = 'HUB-CON-AD-ANTI-PRIOR', 'HUB-CON-AD-ACTOR-RECEPTION'
        mca = 'HUB-CON-AD-MODULAR-CONCEPT-ARCHITECTURE'
        cases = [
            ({'technical topic'}, (), set(), set()),
            ({'HUB-TECH-ENTRY'}, (), {'HUB-TECH-ENTRY'}, {'HUB-TECH-ENTRY'}),
            ({con, wil}, (), {con, 'HUB-CON-CATALOG', wil}, {wil}),
            ({con, brain, wil}, (), {con, 'HUB-CON-CATALOG', brain, wil}, {brain, wil}),
            ({con, prior, actor}, (), {con, 'HUB-CON-CATALOG', prior, actor, mca}, {prior, actor, mca}),
            ({shop}, (), {shop, 'HUB-SHOP-CATALOG'}, set()),
            ({shop, 'HUB-SHOP-SEARCH', ais}, ('HUB-PKG-AIS',),
             {shop, 'HUB-SHOP-CATALOG', 'HUB-SHOP-SEARCH', ais}, {'HUB-SHOP-SEARCH', ais}),
            ({'HUB-AUTH-ENTRY'}, (), {'HUB-AUTH-ENTRY'}, {'HUB-AUTH-ENTRY'}),
            ({'image discussion'}, (), set(), set()),
            ({image}, ('HUB-PKG-IMAGET',), {image}, {image}),
        ]
        for index, (scopes, pipelines, reads, verified) in enumerate(cases, 1):
            with self.subTest(case=index):
                result = simulate(fixture, scopes, pipeline_needs=pipelines)
                self.assertFalse(result['blocked'])
                self.assertEqual(set(result['spec_reads']), reads)
                self.assertEqual({identity for _, identity in result['spec_verified']}, verified)
                expected_edges = [(('HUB-PKG-CONCEPT-DEVELOPMENT', actor),
                                   ('HUB-PKG-CONCEPT-DEVELOPMENT', mca))] if index == 5 else []
                self.assertEqual(result['direct_dependencies'], expected_edges)
                self.assertFalse(result['runtime_ready'])

        # The current Concept interface must fail closed with a missing or ambiguous Catalog read.
        for records, error in [([], 'ARTIFACT_MISSING'), (None, 'AMBIGUOUS_MODULE')]:
            damaged = copy.deepcopy(fixture)
            key = 'HUB-CON-CATALOG'
            damaged['artifacts'][key] = records if records is not None else fixture['artifacts'][key] * 2
            result = simulate(damaged, {con, wil, 'HUB-TECH-ENTRY'})
            self.assertEqual(result['blocked']['HUB-PKG-CONCEPT-DEVELOPMENT'], f'{error}:{key}')
            self.assertEqual(result['spec_verified'], [('HUB-PKG-TECHNICAL', 'HUB-TECH-ENTRY')])


class ConceptEntryPhaseOneTests(unittest.TestCase):
    def test_exact_successor_bindings_and_pin_only_router(self):
        root = load(ROOT / 'HUB_PACKAGE_CATALOG_v1.19.yaml')
        old_root = load(PHASE_1_ARCHIVE / 'HUB_PACKAGE_CATALOG_v1.18.yaml')
        expected = copy.deepcopy(old_root)
        expected['version'] = '1.19'
        expected['identity_binding'] = expected['identity_binding'].replace('V1_18', 'V1_19')
        concept = next(row for row in expected['packages'] if row['entrypoint_module_id'] == 'HUB-CON-ENTRY')
        concept['version'] = '1.7'
        concept['location']['artifact'] = Path(ENTRY_17).relative_to('library_modules').as_posix()
        expected['live_library_retrieval'] = 'EXACT_LIBRARY_OBJECT_AND_FULL_READ_RECEIPTS_NOT_VERIFIED'
        expected['deployment'] = (
            'STABLE_ACTIVE_REPOSITORY; USER_REPORTED_10_CASE_ROUTING_SMOKE_PASS; '
            'PROJECT_LIBRARY_DEPLOYMENT_NOT_VERIFIED')
        self.assertEqual(root, expected)

        entry = read_identity(ROOT / ENTRY_17)
        for key in ('package_id', 'runtime_role', 'status', 'version'):
            self.assertEqual(entry[key], concept[key])
        self.assertEqual(entry['module_id'], concept['entrypoint_module_id'])
        self.assertEqual(concept['location']['resolution'], 'UNRESOLVED')
        for key in ('library_file_id', 'library_version_id', 'observed_path', 'locator'):
            self.assertIsNone(concept['location'][key])

        before = (PHASE_1_ARCHIVE / 'HUB_ROUTER_v1.1.yaml').read_bytes()
        router = ROOT / 'HUB_ROUTER_v1.1.yaml'
        self.assertEqual(router.read_bytes(), before.replace(b'1.18', b'1.19'))
        pins = load(router)['contracts']
        architecture = ROOT / pins['architecture']['file']
        for name, path in [('architecture', architecture), ('root_catalog', ROOT / pins['root_catalog']['file'])]:
            self.assertEqual(pins[name]['version'], '1.19')
            self.assertTrue(path.is_file())
        self.assertRegex(architecture.read_text(encoding='utf-8'), r'(?m)^Version: 1\.19$')

    def test_entry_delta_preserves_surrounding_contract(self):
        old = (PHASE_1_ARCHIVE / ENTRY_16).read_text(encoding='utf-8')
        new = (ROOT / ENTRY_17).read_text(encoding='utf-8')
        old_prefix, old_remaining = old.split('\nFor expansion,', 1)
        new_prefix, new_remaining = new.split('\nWhen the current task assigns', 1)
        self.assertEqual(new_prefix, old_prefix.replace('Library module v1.6', 'Library module v1.7')
                         .replace('Version: 1.6', 'Version: 1.7'))
        development, new_suffix = new_remaining.split('\nFor concept analysis/audit,', 1)
        self.assertEqual(new_suffix, old_remaining.split('\nFor concept analysis/audit,', 1)[1])
        # Text checks establish contract coverage, not reasoning or provenance recognition by a model.
        development = 'When the current task assigns' + development
        for rule in (
            r'current task assigns .* within the same premise',
            r'institutions only where material',
            r'Check it against established definitions.*prior consequences',
            r'consequences of the existing premise to identify what needs further development',
            r'Preserve unsupported links as unknowns, proposals, conditional branches or unresolved dependencies',
            r'constitutive assumption or introducing an independent driver.*keep any proposed change conditional',
            r'supported consequences at whatever scale the mechanism produces',
            r'Stop once the assigned question has enough causal development',
            r'context alone does not assign development',
        ):
            self.assertRegex(development, rule)
        self.assertNotIn('/REFINE', new)

    def test_phase_one_archive_is_byte_exact(self):
        receipt = json.loads((PHASE_1_ARCHIVE / 'ARCHIVE_RECEIPT.json').read_text(encoding='utf-8'))
        self.assertEqual({row['old'] for row in receipt}, {
            'HUB_ARCHITECTURE_v1.18.md', 'HUB_PACKAGE_CATALOG_v1.18.yaml', 'HUB_ROUTER_v1.1.yaml', ENTRY_16,
        })
        for row in receipt:
            archived = ROOT / row['archive']
            self.assertEqual(archived, PHASE_1_ARCHIVE / row['old'])
            data = archived.read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), row['sha256'])
            self.assertEqual(data, subprocess.check_output(
                ['git', 'show', f'{PHASE_1_BASELINE}:Central Hub/{row["old"]}'], cwd=ROOT))
            self.assertTrue((ROOT / row['new']).is_file())
            if row['old'] != row['new']:
                self.assertFalse((ROOT / row['old']).exists())

    def test_glossary_points_to_active_bindings(self):
        glossary = (ROOT / 'CONTROL_VOCABULARY_GLOSSARY.md').read_text(encoding='utf-8')
        root = load(ROOT / 'HUB_PACKAGE_CATALOG_v1.19.yaml')
        for package in root['packages']:
            if package['entrypoint_module_id'] in {'HUB-CON-ENTRY', 'HUB-AUTH-ENTRY'}:
                self.assertIn(f"\x60{package['entrypoint_module_id']}\x60 {package['version']}", glossary)
                if package['local_catalog']:
                    catalog = package['local_catalog']
                    self.assertIn(f"\x60{catalog['module_id']}\x60 {catalog['version']}", glossary)
        self.assertIn('MAINTENANCE / INTERPRETATION REFERENCE', glossary)
        self.assertNotIn('/REFINE', glossary)


if __name__ == '__main__':
    unittest.main()

"""Current successor contracts and declared fixtures; no live Library/model execution.

Earlier promotion tests retain exact predecessor reads. These tests independently
check the active namespace and compare all successor behavior with that release.
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
        cls.current = {r['new_id']: (ROOT / r['new'], read_identity(ROOT / r['new']))
                       for r in cls.rows.values()}
        cls.root = load(ROOT / 'HUB_PACKAGE_CATALOG_v1.18.yaml')
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
            self.assertEqual(path.relative_to(LIBRARY).parts[0], package_folder)
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
                self.assertEqual(LIBRARY / binding['location']['artifact'], path)
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
            path = ROOT / row['new']
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
        self.assertEqual((ROOT / 'HUB_ROUTER_v1.1.yaml').read_bytes(), before.replace(b'1.17', b'1.18'))
        old = (ARCHIVE / 'HUB_ARCHITECTURE_v1.17.md').read_text(encoding='utf-8')
        current = (ROOT / 'HUB_ARCHITECTURE_v1.18.md').read_text(encoding='utf-8')
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
            self.assertEqual((ROOT / relative).read_bytes(), expected, relative)
        # Existing archive JSON may already have checkout CRLF conversion; do not rewrite it.
        unchanged = subprocess.check_output(['git', 'diff', '--name-only', BASELINE, '--',
            'Source_archive', ':(exclude)Source_archive/Canonical namespace migration 2026-11-11'], cwd=ROOT)
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
        surfaces = [p for p in LIBRARY.rglob('*') if p.is_file()] + [
            ROOT / 'HUB_ARCHITECTURE_v1.18.md', ROOT / 'HUB_PACKAGE_CATALOG_v1.18.yaml',
            ROOT / 'HUB_ROUTER_v1.1.yaml']
        for path in surfaces:
            text = path.read_text(encoding='utf-8')
            for identity in IDS:
                self.assertNotRegex(text, r'(?<![A-Z0-9-])' + re.escape(identity) + r'(?![A-Z0-9-])')
        names = [p.name for p, _ in self.current.values()]
        self.assertEqual(len(set(names)), 26)
        document = (ROOT / 'NAMESPACE_MIGRATION.md').read_text(encoding='utf-8')
        self.assertIn('NESTED LIBRARY FOLDER CAPABILITY: NOT_VERIFIED', document)
        self.assertIn('SUCCESSOR LIBRARY RETRIEVAL / LIVE BEHAVIOR: NOT_RUN', document)


if __name__ == '__main__':
    unittest.main()

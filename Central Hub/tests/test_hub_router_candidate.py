"""Independent SPEC oracle with synthetic metadata; no runtime resolver/model/tools.

Scope matches are supplied by fixtures, not inferred from natural-language tasks.
FULL_FILE records below are simulated read evidence, never real Library retrieval.
"""
import copy
import unittest
import yaml

from test_hub_contracts import Closed, ROOT, digest, load, parse, historical_source


CANDIDATE = ROOT / 'candidates/HUB_ROUTER_v1.1-candidate.yaml'
CATALOG = ROOT / 'candidates/HUB_PACKAGE_CATALOG_v0.1.yaml'

INTEGRATION = ROOT / 'candidates/integration_v1.1'


def integration_read_spec(entry, observations):
    """SPEC only: supplied observations, no retrieval or natural-language routing."""
    if len(observations) != 1:
        raise Closed('missing or ambiguous exact source')
    observed = observations[0]
    if observed.get('read_kind') != 'FULL_FILE' or observed.get('has_more') is not False:
        raise Closed('incomplete read')
    location = entry['location']
    if entry['binding_mode'] == 'LIBRARY_MODULE':
        expected = dict(module_id=entry['entrypoint_module_id'],
                        package_id=entry['package_id'], runtime_role=entry['runtime_role'],
                        status=entry['status'], version=entry['version'],
                        root=location['root'], library_file_id=location['library_file_id'],
                        library_version_id=location['library_version_id'])
        if any(observed.get(k) != v for k, v in expected.items()):
            raise Closed('Library binding mismatch; no fallback')
    elif entry['binding_mode'] == 'LEGACY_PROJECT_SOURCE':
        expected = dict(location='PROJECT_SOURCES',
                        declared_source_path=location['declared_source_path'],
                        source_name=location['source_name'], version=entry['version'])
        if any(observed.get(k) != v for k, v in expected.items()):
            raise Closed('legacy source mismatch; no Library discovery')
    else:
        raise Closed('unsupported binding')
    return dict(evidence='SPEC_SIMULATION_ONLY', runtime_ready=False,
                live_integration='NOT_RUN', module_id=entry['entrypoint_module_id'])


class IntegrationContracts(unittest.TestCase):
    def setUp(self):
        self.catalog = load(INTEGRATION / 'HUB_PACKAGE_CATALOG_v1.0-integration-candidate.yaml')
        self.router = load(INTEGRATION / 'HUB_ROUTER_v1.1-integration-candidate.yaml')
        self.packages = {p['package_id']: p for p in self.catalog['packages']}

    def technical_observation(self):
        return dict(module_id='HUB-DOM-TECHNICAL', package_id='HUB-PKG-TECHNICAL',
                    runtime_role='REASONING_PROFILE', status='ACTIVE', version='1.0',
                    root='Central Hub Config',
                    library_file_id='libfile_bab7d55cd85c819198291acf135099fd',
                    library_version_id='1', read_kind='FULL_FILE', has_more=False)

    def test_ci_only_exact_delegation_changes_and_budget(self):
        current = (historical_source('HUB_CI_v1.0.md')).read_bytes()
        candidate = (INTEGRATION / 'HUB_CI_v1.1-candidate.md').read_bytes()
        self.assertEqual(current.count(b'HUB_ROUTER_v1.0.yaml'), 1)
        self.assertEqual(candidate, current.replace(b'HUB_ROUTER_v1.0.yaml',
                         b'HUB_ROUTER_v1.1-integration-candidate.yaml'))
        lf = candidate.decode('utf-8').replace('\r\n', '\n')
        self.assertLessEqual(len(lf), 8000)
        self.assertLessEqual(len(lf.replace('\n', '\r\n')), 8000)

    def test_core_candidate_contracts_and_preserved_composition(self):
        self.assertEqual(self.router['status'], 'CANDIDATE')
        self.assertFalse(self.router['active'])
        self.assertFalse(self.catalog['active'])
        self.assertFalse(self.catalog['runtime_ready'])
        self.assertEqual(self.catalog['live_integration'], 'NOT_RUN')
        design = load(CANDIDATE)
        for key in ['sequence', 'composition', 'pipelines', 'persistence', 'ownership']:
            self.assertEqual(self.router[key], design[key])
        for contract in self.router['contracts'].values():
            if isinstance(contract, dict):
                self.assertTrue((INTEGRATION / contract['file']).is_file())
                self.assertEqual(contract['status'], 'CANDIDATE')
                self.assertEqual(contract['version'], '1.0')
        self.assertIn('explicit user authorization', self.router['activation_notice'])
        architecture = (INTEGRATION / 'HUB_ARCHITECTURE_v1.0-integration-candidate.md').read_text(encoding='utf-8')
        for token in ['HUB-CORE-ARCH', 'REFINES', 'COMPLEMENTS', 'REQUIRES',
                      'FULL_FILE', 'LEGACY_PROJECT_SOURCE', 'ONE PACKAGE = ONE RUNTIME BINDING']:
            self.assertIn(token, architecture)
        self.assertNotIn('ACTIVE MODULE DEPLOYMENT: NOT_PERFORMED', architecture)

    def test_exactly_five_singular_bindings_and_opaque_pipelines(self):
        self.assertEqual(len(self.catalog['packages']), 5)
        self.assertEqual(set(self.packages), {'HUB-PKG-TECHNICAL', 'HUB-PKG-CREATIVE',
                         'HUB-PKG-BRAINSTORM', 'HUB-PKG-AIS', 'HUB-PKG-IMAGET'})
        for entry in self.packages.values():
            self.assertIsInstance(entry['location'], dict)
            self.assertIsNone(entry['local_catalog'])
            self.assertEqual(entry['requires'], [])
            self.assertNotIn('fallback', entry)
        for package in ['HUB-PKG-AIS', 'HUB-PKG-IMAGET']:
            self.assertEqual(self.packages[package]['runtime_role'], 'TOOL_PIPELINE')
            self.assertNotIn('modules', self.packages[package])
        self.assertNotIn('READY_GATE', str(self.catalog))

    def test_technical_library_identity_and_no_legacy(self):
        entry = self.packages['HUB-PKG-TECHNICAL']
        self.assertEqual(entry['binding_mode'], 'LIBRARY_MODULE')
        self.assertEqual(entry['location']['class'], 'LIBRARY')
        self.assertEqual(entry['location']['observed_surface_file_id'],
                         'file_000000006da88211aa3412146f6c016c')
        self.assertEqual(entry['location']['observed_path'],
                         'Central Hub Config/HUB-DOM-TECHNICAL_v1.0.md')
        result = integration_read_spec(entry, [self.technical_observation()])
        self.assertFalse(result['runtime_ready'])
        self.assertEqual(result['live_integration'], 'NOT_RUN')
        self.assertNotEqual(entry['version'], entry['location']['library_version_id'])
        self.assertNotIn('PROJECT_SOURCE', str(entry))
        self.assertNotIn('TECHNICAL_v1.0.md', str(entry).replace('HUB-DOM-TECHNICAL_v1.0.md', ''))
        self.assertIn('project_sources_for_library_binding', self.router['library']['forbidden_fallbacks'])

    def test_library_failure_mismatch_partial_ambiguity_and_no_source_substitute(self):
        entry = self.packages['HUB-PKG-TECHNICAL']
        valid = self.technical_observation()
        for key, wrong in [('module_id', 'OTHER'), ('package_id', 'OTHER'),
                           ('runtime_role', 'DOMAIN_CONTROL'), ('status', 'CANDIDATE'),
                           ('version', '1.0-candidate'), ('root', 'Other root'),
                           ('library_file_id', 'lookalike'), ('library_version_id', '1.0'),
                           ('read_kind', 'HEADER_ONLY'), ('has_more', True)]:
            with self.subTest(key=key), self.assertRaises(Closed):
                integration_read_spec(entry, [dict(valid, **{key: wrong})])
        for observations in [[], [valid, valid],
                             [dict(read_kind='FULL_FILE', has_more=False, location='PROJECT_SOURCES',
                                   source_name='TECHNICAL_v1.0.md', version='1.0')]]:
            with self.assertRaises(Closed):
                integration_read_spec(entry, observations)

    def test_unmigrated_exact_source_compatibility_without_fake_headers(self):
        paths = {'HUB-PKG-CREATIVE': 'domains/creative/CREATIVE_v1.0.md',
                 'HUB-PKG-BRAINSTORM': 'capabilities/BRAINSTORM_v1.0.md',
                 'HUB-PKG-AIS': 'tool_pipelines/AIS/AIS_PIPELINE_v1.0.md',
                 'HUB-PKG-IMAGET': 'tool_pipelines/ImageT/IMAGE_CONTROLLER_v1.1.md'}
        for package, path in paths.items():
            entry = self.packages[package]
            self.assertEqual(entry['binding_mode'], 'LEGACY_PROJECT_SOURCE')
            self.assertEqual(entry['location']['declared_source_path'], path)
            self.assertTrue((historical_source(path)).is_file())
            self.assertNotIn('library_file_id', entry['location'])
            observed = dict(location='PROJECT_SOURCES', declared_source_path=path,
                            source_name=path.rsplit('/', 1)[1], version=entry['version'],
                            read_kind='FULL_FILE', has_more=False)
            integration_read_spec(entry, [observed])  # No new identity headers supplied.
            for observations in [[], [dict(observed, source_name='lookalike.md')]]:
                with self.assertRaises(Closed):
                    integration_read_spec(entry, observations)

    def test_mixed_storage_keeps_independent_failure_and_reselection(self):
        technical = self.packages['HUB-PKG-TECHNICAL']
        brainstorm = self.packages['HUB-PKG-BRAINSTORM']
        observation = dict(location='PROJECT_SOURCES',
                           declared_source_path=brainstorm['location']['declared_source_path'],
                           source_name='BRAINSTORM_v1.0.md', version='1.0',
                           read_kind='FULL_FILE', has_more=False)
        self.assertNotEqual(integration_read_spec(technical, [self.technical_observation()])['module_id'],
                            integration_read_spec(brainstorm, [observation])['module_id'])
        with self.assertRaises(Closed):
            integration_read_spec(technical, [])
        self.assertFalse(integration_read_spec(brainstorm, [observation])['runtime_ready'])
        self.assertIn('Every turn', self.router['persistence']['reassess'])


    def test_legacy_sources_preserved_against_integration_start(self):
        expected = {
                  "HUB_CI_v1.0.md": "d4d5cd24ec8da6a6603f163f882eeb4fd896d867b5e245098d0a64b877a4abd3",
                  "HUB_ROUTER_v1.0.yaml": "465ecbf6b1c6ff80e1be51a57b6ac3743f19a210f94a36bad185993b4c2de844",
                  "MIGRATION_REPORT.md": "974268ce036846879279d22c88e923e291d73ef6c2fdf62e38a61f4d228e28e9",
                  "capabilities/BRAINSTORM_v1.0.md": "d7b5a21595d46e2442e51adf20cee18cc29cdef14581cef8ab27cbfc85e8d8e0",
                  "domains/creative/CREATIVE_v1.0.md": "df732077f19ddd346bfb8d5d4e0c595cd574c831ec8e9696f9d4a80c98f8bb70",
                  "domains/technical/TECHNICAL_v1.0.md": "008e1be28a32fd956ff4ca4edc64536de4e9e3b3b6b7b124ae4ecebdc60b1894",
                  "tool_pipelines/AIS/AIS_PIPELINE_v1.0.md": "c7f78f10be855d6b77aa3e0bbf67c3856c7fa42f890382752056de71abd10f69",
                  "tool_pipelines/AIS/AIS_ROUTER_v1.1.yaml": "ea5e22648fdcb1da239126ec25220b474444de11521887cd93711f41b4b32901",
                  "tool_pipelines/ImageT/config.md": "20b08b3b99b237eebeec0442024e0818245d0b0bebc2fb756e972aca67d4d3d7",
                  "tool_pipelines/ImageT/IMAGE_ANTI_PRIOR.md": "f08a1d1a09c8b31cd3fe6ed80b38b19f2c662e15f7e192b42c8a5e044aa69b5c",
                  "tool_pipelines/ImageT/IMAGE_CONTROLLER_v1.1.md": "6d33c80f4852c1b44c32abf6e898c14e8f001d24796d406aafc49a95ab3a2733",
                  "tool_pipelines/ImageT/IMAGE_SOURCE_ROUTER.yaml": "066b47a697c4cace1bcef86233d556a2ca4ae8c56f2e1b54e6779d3547b80fc4",
                  "tool_pipelines/ImageT/manifest.yaml": "007f73d2fc4d98d69f7a5dbc5365924456d222986370340174c75e74deaacc0a",
                  "tool_pipelines/ImageT/READY_GATE_v1.0.md": "c61bccbc88560c40a9f600473d84b54c7f6b27f527eea6b713f78615d04de1d5",
                  "tool_pipelines/ImageT/preferences/HUMANOID_CHARACTER_DESIGN_PREFERENCE.md": "1eb0a6e136cbf3b21de1726565b47bd3a80d1ee9b55e86ba10ea0d880a1371b3"
        }
        for path, sha256 in expected.items():
            with self.subTest(path=path):
                self.assertEqual(digest(historical_source(path)), sha256)

    def test_live_spec_stack_cases_installation_and_rollback(self):
        spec = (INTEGRATION / 'HUB_V1_1_INTEGRATION_TEST_CASES.md').read_text(encoding='utf-8')
        for index in range(1, 11):
            self.assertIn('I%02d' % index, spec)
        i02 = spec.split('| I02 —')[1].split('|')[1]
        self.assertNotIn('TECHNICAL', i02)
        self.assertNotIn('HUB-DOM', i02)
        for token in ['PROJECT INSTRUCTIONS', 'PROJECT SOURCES', 'LIBRARY', 'UNVERIFIABLE',
                      'NOT_RUN', 'ROLLBACK != FALLBACK', 'TECHNICAL_v1.0.md']:
            self.assertIn(token, spec)


def synthetic_module(module_id, package_id, scopes, role='DOMAIN_CONTROL', **changes):
    module = dict(module_id=module_id, package_id=package_id, runtime_role=role,
                  status='ACTIVE', version='1.0', scopes=set(scopes),
                  refines=[], complements=[], requires=[], decisions={},
                  location=dict(root='Central Hub Config', locator=None,
                                verification='UNRESOLVED', **{'class': 'LIBRARY'}))
    module.update(changes)
    return module


def synthetic_package(module):
    return dict(package_id=module['package_id'], entrypoint=copy.deepcopy(module),
                applicability=set(module['scopes']), local_catalog=None, status='ACTIVE')


def synthetic_fixture(*modules):
    """One entrypoint per package; all data stays inside this test module."""
    return dict(status='ACTIVE', packages=[synthetic_package(m) for m in modules],
                local_catalogs={}, artifacts={m['module_id']: [dict(copy.deepcopy(m),
                read_kind='FULL_FILE')] for m in modules}, evidence='SPEC_FIXTURE_ONLY')


def synthetic_growing_fixture(count=24):
    entry = synthetic_module('SYNTHETIC_ENTRY', 'SYNTHETIC_PACKAGE', {'X'})
    fixture = synthetic_fixture(entry)
    catalog = synthetic_module('SYNTHETIC_LOCAL_CATALOG', entry['package_id'], set(),
                               role='PACKAGE_CATALOG')
    fixture['packages'][0]['local_catalog'] = catalog
    fixture['artifacts'][catalog['module_id']] = [dict(catalog, read_kind='FULL_FILE')]
    leaves = [synthetic_module(f'SYNTHETIC_LEAF_{i}', entry['package_id'], {f'UNRELATED_{i}'})
              for i in range(count)]
    leaves[0]['scopes'] = {'X'}
    leaves[0]['requires'] = [dict(module_id=leaves[1]['module_id'])]
    leaves[1]['requires'] = [dict(module_id=leaves[2]['module_id'])]
    fixture['local_catalogs'][entry['package_id']] = leaves
    for leaf in leaves:
        fixture['artifacts'][leaf['module_id']] = [dict(copy.deepcopy(leaf), read_kind='FULL_FILE')]
    return fixture


def current_metadata_fixture():
    """Explicit parity projection; never mutates the candidate catalog or active files."""
    catalog = load(CATALOG)
    modules = []
    for row in catalog['packages']:
        module = synthetic_module(row['entrypoint_module_id'], row['package_id'],
                                  {row['package_id']}, row['runtime_role'],
                                  version=row['version'], location=copy.deepcopy(row['location']))
        module['identity_evidence'] = 'CURRENT_ENTRYPOINT_METADATA_ONLY'
        modules.append(module)
    fixture = synthetic_fixture(*modules)
    fixture['source_catalog_status'] = catalog['status']
    return fixture


def simulate(fixture, scopes, *, pipeline_needs=(), requested_packages=(), library_available=False):
    """Finite acceptance oracle. Plans/fixture reads only; NEVER executes candidate YAML.

    The fixture models an accepted deployment, with fake full-read records. Current
    route parity uses an explicitly labeled metadata projection, not new real headers.
    """
    scopes = set(scopes)
    result = dict(planned=[], spec_verified=[], blocked={}, module_scopes={},
                  direct_dependencies=[], relations_used=[], artifact_requests=[],
                  spec_reads=[], local_catalogs_consulted=[], pipeline_entrypoints=[],
                  runtime_blockers=[], runtime_ready=False, live_library_retrieval='NOT_RUN')
    if fixture is None or fixture.get('unreadable'):
        result['blocked']['ROOT'] = 'ROOT_MISSING_OR_UNREADABLE'
        return result
    if fixture['status'] != 'ACTIVE':
        result['blocked']['ROOT'] = 'CATALOG_NOT_ACTIVE'
        return result
    packages = {p['package_id']: p for p in fixture['packages']}
    if len(packages) != len(fixture['packages']):
        result['blocked']['ROOT'] = 'AMBIGUOUS_PACKAGE'
        return result
    pipeline_needs = set(pipeline_needs)
    for package_id in requested_packages:
        if package_id not in packages:
            result['blocked'][package_id] = 'UNKNOWN_PACKAGE'
    selected_packages = [p for p in packages.values()
        if (p['applicability'] & scopes or p['package_id'] in requested_packages)
        and (p['entrypoint']['runtime_role'] != 'TOOL_PIPELINE' or p['package_id'] in pipeline_needs)]
    selected_pipeline_packages = {p['package_id'] for p in selected_packages
        if p['entrypoint']['runtime_role'] == 'TOOL_PIPELINE'}
    interfaces = set()

    def read(binding):
        identity = binding['module_id']
        if identity not in result['artifact_requests']:
            result['artifact_requests'].append(identity)
        location = binding['location']
        if location['class'] == 'LIBRARY':
            if location.get('root') != 'Central Hub Config':
                raise Closed('LIBRARY_ROOT_ESCAPE')
            if not library_available:
                result['runtime_blockers'].append('LIBRARY_UNAVAILABLE:' + identity)
            if location.get('locator') is None or location.get('verification') != 'VERIFIED':
                result['runtime_blockers'].append('LOCATOR_UNRESOLVED:' + identity)
        elif location['class'] == 'PROJECT_SOURCES':
            if location.get('verification') != 'VERIFIED':
                result['runtime_blockers'].append('PROJECT_SOURCE_NOT_VERIFIED:' + identity)
        else:
            raise Closed('UNSUPPORTED_LOCATION')
        records = fixture['artifacts'].get(identity, [])
        if not records:
            raise Closed('ARTIFACT_MISSING:' + identity)
        if len(records) != 1:
            raise Closed('AMBIGUOUS_MODULE:' + identity)
        record = records[0]
        if record.get('read_kind') != 'FULL_FILE':
            raise Closed('FULL_FILE_REQUIRED:' + identity)
        for field in ['module_id', 'package_id', 'runtime_role', 'version']:
            if record[field] != binding[field]:
                raise Closed('HEADER_MISMATCH:' + field)
        if binding['status'] != 'ACTIVE' or record['status'] != 'ACTIVE':
            raise Closed('INACTIVE_MODULE:' + identity)
        for relation in ['requires', 'refines', 'complements', 'decisions']:
            if record[relation] != binding[relation]:
                raise Closed('MATERIAL_CONTRACT_MISMATCH:' + relation)
        if identity not in result['spec_reads']:
            result['spec_reads'].append(identity)

    def interface(package_id):
        if package_id not in packages:
            raise Closed('UNKNOWN_PACKAGE:' + package_id)
        package = packages[package_id]
        if package['status'] != 'ACTIVE':
            raise Closed('INACTIVE_PACKAGE:' + package_id)
        if package_id not in interfaces:
            read(package['entrypoint'])
            catalog = package['local_catalog']
            if catalog is not None:
                read(catalog)
                if package_id not in fixture['local_catalogs']:
                    raise Closed('LOCAL_CATALOG_MISSING:' + package_id)
                result['local_catalogs_consulted'].append(package_id)
            interfaces.add(package_id)
        return package

    def resolve(package_id, module_id):
        package = interface(package_id)
        if module_id == package['entrypoint']['module_id']:
            return package['entrypoint']
        rows = fixture['local_catalogs'].get(package_id, [])
        matches = [row for row in rows if row['module_id'] == module_id]
        if len(matches) != 1:
            raise Closed('LEAF_UNRESOLVED_OR_AMBIGUOUS:' + module_id)
        if matches[0]['package_id'] != package_id:
            raise Closed('PACKAGE_MISMATCH:' + module_id)
        return matches[0]

    def visit(module, matched, stack):
        key = (module['package_id'], module['module_id'])
        if key in stack:
            raise Closed('REQUIRES_CYCLE:' + module['module_id'])
        if module['runtime_role'] == 'TOOL_PIPELINE' and module['package_id'] not in selected_pipeline_packages:
            raise Closed('PIPELINE_NEED_NOT_AUTHORIZATION')
        read(module)
        closure = {key: (module, set(matched))}
        for relation_name in ['refines', 'complements']:
            for relation in module[relation_name]:
                owner = relation.get('package_id', module['package_id'])
                if owner not in packages or not relation.get('admitted') or not relation.get('module_id'):
                    raise Closed('UNSUPPORTED_CROSS_PACKAGE_RELATION')
                if not relation.get('scope') or not set(relation['scope']) <= module['scopes']:
                    raise Closed('RELATION_SCOPE_REQUIRED')
                # Relation metadata is admitted by fixture; no counterpart artifact read.
                result['relations_used'].append((relation_name, key, owner, relation['module_id']))
        for dependency in module['requires']:
            owner = dependency.get('package_id', module['package_id'])
            if owner != module['package_id'] and not dependency.get('admitted'):
                raise Closed('UNSUPPORTED_CROSS_PACKAGE_RELATION')
            target = resolve(owner, dependency['module_id'])
            target_key = (owner, target['module_id'])
            result['direct_dependencies'].append((key, target_key))
            for child, (binding, scope) in visit(target, matched, stack + [key]).items():
                if child in closure:
                    closure[child][1].update(scope)
                else:
                    closure[child] = (binding, scope)
        return closure

    closures = {}

    def conflicts(left, right):
        for lm, ls in left.values():
            for rm, rs in right.values():
                if ls & rs and any(k in rm['decisions'] and rm['decisions'][k] != v
                                 for k, v in lm['decisions'].items()):
                    return True
        return False

    for package in selected_packages:
        package_id = package['package_id']
        if package['status'] != 'ACTIVE':
            if package_id in requested_packages:
                result['blocked'][package_id] = 'INACTIVE_PACKAGE'
            continue
        try:
            interface(package_id)
            candidates = (fixture['local_catalogs'][package_id] if package['local_catalog'] is not None
                          else [package['entrypoint']])
        except Closed as error:
            result['blocked'][package_id] = str(error)
            continue
        for module in candidates:
            matched = module['scopes'] & scopes
            if not matched or module['status'] != 'ACTIVE':
                continue
            key = (package_id, module['module_id'])
            result['planned'].append(key)
            try:
                if module['package_id'] != package_id:
                    raise Closed('PACKAGE_MISMATCH:' + module['module_id'])
                closure = visit(module, matched, [])
                if conflicts(closure, closure):
                    raise Closed('APPLICABLE_MODULE_CONFLICT')
                closures[key] = closure
            except Closed as error:
                result['blocked'][key] = str(error)

    # Explicit fixture decisions represent material same-scope conflicts, not ranking.
    root_keys = list(closures)
    conflicting = set()
    for i, left in enumerate(root_keys):
        for right in root_keys[i + 1:]:
            if conflicts(closures[left], closures[right]):
                conflicting.update([left, right])
    for key in conflicting:
        result['blocked'][key] = 'APPLICABLE_MODULE_CONFLICT'
        del closures[key]
    for closure in closures.values():
        for key, (module, matched) in closure.items():
            result['module_scopes'].setdefault(key, set()).update(matched)
            if key not in result['spec_verified']:
                result['spec_verified'].append(key)
            if module['runtime_role'] == 'TOOL_PIPELINE' and key not in result['pipeline_entrypoints']:
                result['pipeline_entrypoints'].append(key)
    result['direct_dependencies'] = list(dict.fromkeys(result['direct_dependencies']))
    result['runtime_blockers'] = list(dict.fromkeys(result['runtime_blockers']))
    return result


class CandidateRouterTests(unittest.TestCase):
    def test_static_candidate_contract_and_nonactivation(self):
        router = load(CANDIDATE)
        self.assertEqual(router['status'], 'CANDIDATE')
        self.assertFalse(router['active'])
        self.assertEqual(router['deployment'], 'DO NOT DEPLOY')
        self.assertIn('NOT ACTIVE', router['activation_notice'])
        self.assertEqual(router['library']['root'], 'Central Hub Config')
        self.assertEqual(set(router['composition']), {'REFINES', 'COMPLEMENTS', 'REQUIRES', 'not_edges', 'invariants'})
        for name in ['REFINES', 'COMPLEMENTS']:
            self.assertFalse(router['composition'][name]['autoload'])
            self.assertFalse(router['composition'][name]['implies_requires'])
        self.assertTrue(router['composition']['REQUIRES']['transitive'])
        self.assertEqual(router['sequence'], list(router['stages']))
        for contract in router['contracts'].values():
            if isinstance(contract, dict):
                self.assertTrue((CANDIDATE.parent / contract['file']).is_file())
                self.assertEqual(contract['status'], 'CANDIDATE')
        text = CANDIDATE.read_text(encoding='utf-8')
        for forbidden in ['SYNTHETIC_', 'CUISINE', 'FOOD-SCIENCE', 'HUB-PIPE-AIS', 'HUB-PIPE-IMAGET',
                          'READY_GATE', 'ready_gate', 'ANTI_PRIOR', 'EVIDENCE_MERGE', 'source_policy']:
            self.assertNotIn(forbidden, text)
        for name in ['axes', 'controls', 'selection', 'leaf_inventory']:
            self.assertNotIn(name, router)
        for source in ['HUB_CI_v1.0.md', 'HUB_ROUTER_v1.0.yaml']:
            self.assertNotIn(CANDIDATE.name, (historical_source(source)).read_text(encoding='utf-8'))
        self.assertEqual(digest(historical_source('HUB_ROUTER_v1.0.yaml')),
                         '465ecbf6b1c6ff80e1be51a57b6ac3743f19a210f94a36bad185993b4c2de844')

    def test_A_current_singletons_and_baseline_parity(self):
        before = CATALOG.read_bytes()
        fixture = current_metadata_fixture()
        self.assertEqual(fixture['source_catalog_status'], 'CANDIDATE')
        for package in fixture['packages']:
            pid = package['package_id']
            pipelines = [pid] if package['entrypoint']['runtime_role'] == 'TOOL_PIPELINE' else []
            result = simulate(fixture, {pid}, pipeline_needs=pipelines)
            self.assertEqual(result['spec_verified'], [(pid, package['entrypoint']['module_id'])])
            self.assertEqual(result['local_catalogs_consulted'], [])
            self.assertTrue(result['runtime_blockers'])
            self.assertFalse(result['runtime_ready'])
            self.assertEqual(result['live_library_retrieval'], 'NOT_RUN')
        self.assertEqual(simulate(fixture, set())['planned'], [])
        self.assertEqual(CATALOG.read_bytes(), before)

    def test_B_multi_role_and_cross_portion_parity(self):
        fixture = current_metadata_fixture()
        selected = {'HUB-PKG-CREATIVE', 'HUB-PKG-BRAINSTORM'}
        result = simulate(fixture, selected)
        self.assertEqual({key[0] for key in result['spec_verified']}, selected)
        roles = {p['entrypoint']['runtime_role'] for p in fixture['packages'] if p['package_id'] in selected}
        self.assertEqual(roles, {'DOMAIN_CONTROL', 'CAPABILITY'})
        mixed = simulate(fixture, {'HUB-PKG-TECHNICAL', 'HUB-PKG-BRAINSTORM', 'HUB-PKG-AIS'},
                         pipeline_needs={'HUB-PKG-AIS'})
        self.assertEqual(len(mixed['spec_verified']), 3)
        portions = [simulate(fixture, {pid}) for pid in selected]
        self.assertEqual({key[0] for r in portions for key in r['spec_verified']}, selected)

    def test_C_base_refinement_retains_uncovered_scope(self):
        base = synthetic_module('SYNTHETIC_BASE', 'SYNTHETIC_BASE_PKG', {'X', 'Y'})
        narrow = synthetic_module('SYNTHETIC_REFINEMENT', 'SYNTHETIC_NARROW_PKG', {'X'},
            refines=[dict(module_id=base['module_id'], package_id=base['package_id'], scope=['X'], admitted=True)])
        result = simulate(synthetic_fixture(base, narrow), {'X', 'Y'})
        self.assertEqual(result['module_scopes'][(narrow['package_id'], narrow['module_id'])], {'X'})
        self.assertIn('Y', result['module_scopes'][(base['package_id'], base['module_id'])])
        self.assertEqual(result['direct_dependencies'], [])

    def test_D_refines_does_not_load_or_require_counterpart(self):
        base = synthetic_module('SYNTHETIC_BASE', 'SYNTHETIC_BASE_PKG', {'Y'})
        narrow = synthetic_module('SYNTHETIC_A', 'SYNTHETIC_A_PKG', {'X'},
            refines=[dict(module_id=base['module_id'], package_id=base['package_id'], scope=['X'], admitted=True)])
        result = simulate(synthetic_fixture(base, narrow), {'X'})
        self.assertEqual(result['spec_reads'], [narrow['module_id']])
        self.assertEqual(result['direct_dependencies'], [])

    def test_E_transitive_requires(self):
        fixture = synthetic_growing_fixture()
        result = simulate(fixture, {'X'})
        self.assertEqual({key[1] for key in result['spec_verified']},
                         {'SYNTHETIC_LEAF_0', 'SYNTHETIC_LEAF_1', 'SYNTHETIC_LEAF_2'})
        self.assertEqual(len(result['direct_dependencies']), 2)

    def test_F_missing_dependency_blocks_only_dependent_roots(self):
        a = synthetic_module('SYNTHETIC_A', 'SYNTHETIC_PKG_A', {'X'},
                             requires=[dict(module_id='SYNTHETIC_MISSING')])
        other = synthetic_module('SYNTHETIC_INDEPENDENT', 'SYNTHETIC_PKG_OTHER', {'X'})
        result = simulate(synthetic_fixture(a, other), {'X'})
        self.assertIn((a['package_id'], a['module_id']), result['blocked'])
        self.assertEqual(result['spec_verified'], [(other['package_id'], other['module_id'])])

    def test_G_cycle_blocks_closure_and_preserves_independent_root(self):
        fixture = synthetic_growing_fixture()
        leaves = fixture['local_catalogs']['SYNTHETIC_PACKAGE']
        leaves[1]['requires'] = [dict(module_id=leaves[0]['module_id'])]
        fixture['artifacts'][leaves[1]['module_id']][0]['requires'] = copy.deepcopy(leaves[1]['requires'])
        leaves[3]['scopes'] = {'X'}
        result = simulate(fixture, {'X'})
        self.assertTrue(any('REQUIRES_CYCLE' in reason for reason in result['blocked'].values()))
        self.assertEqual({key[1] for key in result['spec_verified']}, {'SYNTHETIC_LEAF_3'})

    def test_H_complements_independent_match_without_autoload(self):
        b = synthetic_module('SYNTHETIC_B', 'SYNTHETIC_PKG_B', {'Y'})
        a = synthetic_module('SYNTHETIC_A', 'SYNTHETIC_PKG_A', {'X'},
            complements=[dict(module_id=b['module_id'], package_id=b['package_id'], scope=['X'], admitted=True)])
        fixture = synthetic_fixture(a, b)
        self.assertEqual(simulate(fixture, {'X'})['spec_reads'], [a['module_id']])
        both = simulate(fixture, {'X', 'Y'})
        self.assertEqual(len(both['spec_verified']), 2)
        self.assertEqual(both['direct_dependencies'], [])

    def test_I_candidate_package_and_leaf_are_not_auto_selected(self):
        fixture = synthetic_growing_fixture()
        fixture['packages'][0]['status'] = 'CANDIDATE'
        self.assertEqual(simulate(fixture, {'X'})['planned'], [])
        explicit = simulate(fixture, {'X'}, requested_packages=['SYNTHETIC_PACKAGE'])
        self.assertIn('SYNTHETIC_PACKAGE', explicit['blocked'])
        fixture = synthetic_growing_fixture()
        fixture['local_catalogs']['SYNTHETIC_PACKAGE'][0]['status'] = 'CANDIDATE'
        self.assertEqual(simulate(fixture, {'X'})['planned'], [])
        fixture['status'] = 'CANDIDATE'
        self.assertEqual(simulate(fixture, {'X'})['blocked']['ROOT'], 'CATALOG_NOT_ACTIVE')

    def test_J_K_package_growth_24_to_40_keeps_root_and_router_unchanged(self):
        fixture = synthetic_growing_fixture(24)
        singleton = synthetic_fixture(fixture['packages'][0]['entrypoint'])
        self.assertEqual(simulate(singleton, {'X'})['spec_verified'],
                         [('SYNTHETIC_PACKAGE', 'SYNTHETIC_ENTRY')])
        root_before = copy.deepcopy(fixture['packages'])
        router_before, catalog_before = CANDIDATE.read_bytes(), CATALOG.read_bytes()
        first = simulate(fixture, {'X'})
        self.assertEqual(len(fixture['packages']), 1)
        self.assertEqual(first['local_catalogs_consulted'], ['SYNTHETIC_PACKAGE'])
        for i in range(24, 40):
            leaf = synthetic_module(f'SYNTHETIC_LEAF_{i}', 'SYNTHETIC_PACKAGE', {f'UNRELATED_{i}'})
            fixture['local_catalogs']['SYNTHETIC_PACKAGE'].append(leaf)
            fixture['artifacts'][leaf['module_id']] = [dict(leaf, read_kind='FULL_FILE')]
        second = simulate(fixture, {'X'})
        self.assertEqual(fixture['packages'], root_before)
        self.assertEqual(CANDIDATE.read_bytes(), router_before)
        self.assertEqual(CATALOG.read_bytes(), catalog_before)
        self.assertEqual(first['spec_verified'], second['spec_verified'])
        self.assertEqual(first['spec_reads'], second['spec_reads'])
        self.assertEqual(set(second['spec_reads']), {'SYNTHETIC_ENTRY', 'SYNTHETIC_LOCAL_CATALOG',
                         'SYNTHETIC_LEAF_0', 'SYNTHETIC_LEAF_1', 'SYNTHETIC_LEAF_2'})

    def test_L_pipeline_entrypoint_is_opaque_and_independently_selected(self):
        fixture = current_metadata_fixture()
        result = simulate(fixture, {'HUB-PKG-TECHNICAL', 'HUB-PKG-AIS'}, pipeline_needs={'HUB-PKG-AIS'})
        self.assertEqual(result['pipeline_entrypoints'], [('HUB-PKG-AIS', 'HUB-PIPE-AIS')])
        self.assertEqual(set(result['spec_reads']), {'HUB-DOM-TECHNICAL', 'HUB-PIPE-AIS'})
        denied = simulate(fixture, {'HUB-PKG-TECHNICAL', 'HUB-PKG-AIS'})
        self.assertEqual(denied['pipeline_entrypoints'], [])
        technical = next(p['entrypoint'] for p in fixture['packages'] if p['package_id'] == 'HUB-PKG-TECHNICAL')
        edge = dict(module_id='HUB-PIPE-AIS', package_id='HUB-PKG-AIS', admitted=True)
        technical['requires'] = [edge]
        fixture['artifacts'][technical['module_id']][0]['requires'] = [edge]
        denied = simulate(fixture, {'HUB-PKG-TECHNICAL'})
        self.assertTrue(any('PIPELINE_NEED_NOT_AUTHORIZATION' in reason for reason in denied['blocked'].values()))

    def test_M_scope_change_does_not_keep_activation(self):
        fixture = current_metadata_fixture()
        old = simulate(fixture, {'HUB-PKG-TECHNICAL', 'HUB-PKG-AIS'}, pipeline_needs={'HUB-PKG-AIS'})
        new = simulate(fixture, set())
        self.assertEqual(len(old['spec_verified']), 2)
        self.assertEqual(new['spec_verified'], [])
        self.assertEqual(new['artifact_requests'], [])

    def test_missing_interfaces_and_unknown_targets(self):
        self.assertEqual(simulate(None, {'X'})['blocked']['ROOT'], 'ROOT_MISSING_OR_UNREADABLE')
        self.assertEqual(simulate({'unreadable': True}, {'X'})['blocked']['ROOT'], 'ROOT_MISSING_OR_UNREADABLE')
        fixture = synthetic_growing_fixture()
        unknown = simulate(fixture, {'X'}, requested_packages=['SYNTHETIC_UNKNOWN'])
        self.assertIn('SYNTHETIC_UNKNOWN', unknown['blocked'])
        for missing in ['SYNTHETIC_ENTRY', 'SYNTHETIC_LOCAL_CATALOG', 'SYNTHETIC_LEAF_0']:
            changed = copy.deepcopy(fixture)
            del changed['artifacts'][missing]
            self.assertTrue(simulate(changed, {'X'})['blocked'])
        del fixture['local_catalogs']['SYNTHETIC_PACKAGE']
        self.assertTrue(any('LOCAL_CATALOG_MISSING' in reason for reason in simulate(fixture, {'X'})['blocked'].values()))

    def test_header_partial_read_ambiguity_and_root_rejection(self):
        module = synthetic_module('SYNTHETIC_A', 'SYNTHETIC_PKG_A', {'X'})
        for field, value in [('module_id', 'SYNTHETIC_LOOKALIKE'), ('package_id', 'SYNTHETIC_WRONG_OWNER'),
                             ('runtime_role', 'PREFERENCE'), ('version', '999'), ('status', 'CANDIDATE'),
                             ('read_kind', 'HEADER_ONLY'), ('read_kind', 'SNIPPET')]:
            fixture = synthetic_fixture(module)
            fixture['artifacts'][module['module_id']][0][field] = value
            result = simulate(fixture, {'X'})
            self.assertTrue(result['blocked'], field)
            self.assertEqual(result['spec_verified'], [])
        fixture = synthetic_fixture(module)
        fixture['artifacts'][module['module_id']] *= 2
        self.assertTrue(any('AMBIGUOUS_MODULE' in reason for reason in simulate(fixture, {'X'})['blocked'].values()))
        fixture = synthetic_fixture(module)
        fixture['packages'][0]['entrypoint']['location']['root'] = 'Other Library'
        self.assertTrue(any('LIBRARY_ROOT_ESCAPE' in reason for reason in simulate(fixture, {'X'})['blocked'].values()))
        result = simulate(synthetic_fixture(module), {'X'}, library_available=False)
        self.assertIn('LIBRARY_UNAVAILABLE:SYNTHETIC_A', result['runtime_blockers'])
        self.assertIn('LOCATOR_UNRESOLVED:SYNTHETIC_A', result['runtime_blockers'])

    def test_conflict_and_unsupported_cross_package_relation(self):
        a = synthetic_module('SYNTHETIC_A', 'SYNTHETIC_PKG_A', {'X'}, decisions={'method': 'A'})
        b = synthetic_module('SYNTHETIC_B', 'SYNTHETIC_PKG_B', {'X'}, decisions={'method': 'B'})
        independent = synthetic_module('SYNTHETIC_C', 'SYNTHETIC_PKG_C', {'Y'})
        conflict = simulate(synthetic_fixture(a, b, independent), {'X', 'Y'})
        self.assertEqual(len(conflict['blocked']), 2)
        self.assertEqual(conflict['spec_verified'], [(independent['package_id'], independent['module_id'])])
        a['refines'] = [dict(module_id=b['module_id'], package_id='SYNTHETIC_UNKNOWN', scope=['X'], admitted=True)]
        bad = simulate(synthetic_fixture(a), {'X'})
        self.assertTrue(any('UNSUPPORTED_CROSS_PACKAGE_RELATION' in reason for reason in bad['blocked'].values()))
        a['refines'] = []
        a['requires'] = [dict(module_id=b['module_id'], package_id=b['package_id'], admitted=True)]
        b['scopes'] = {'DEPENDENCY_ONLY'}
        internal = simulate(synthetic_fixture(a, b, independent), {'X', 'Y'})
        self.assertEqual(internal['spec_verified'], [(independent['package_id'], independent['module_id'])])
        self.assertIn('APPLICABLE_MODULE_CONFLICT', internal['blocked'].values())

    def test_cross_package_requires_uses_owner_interface(self):
        b = synthetic_module('SYNTHETIC_B', 'SYNTHETIC_PKG_B', {'DEPENDENCY_ONLY'})
        a = synthetic_module('SYNTHETIC_A', 'SYNTHETIC_PKG_A', {'X'}, requires=[
            dict(module_id=b['module_id'], package_id=b['package_id'], admitted=True)])
        result = simulate(synthetic_fixture(a, b), {'X'})
        self.assertEqual(set(result['spec_reads']), {a['module_id'], b['module_id']})
        self.assertEqual(len(result['spec_verified']), 2)

    def test_normative_cases_and_conservative_yaml(self):
        text = (CANDIDATE.parent / 'HUB_ROUTER_v1.1_ROUTE_TEST_CASES.md').read_text(encoding='utf-8')
        for case in 'ABCDEFGHIJKLM':
            self.assertIn(f'| {case} |', text)
        self.assertIn('SPEC_FIXTURE_READ != LIVE FULL_FILE READ', text)
        for bad in ['\na: &x v\nb: *x\n', '\na: !tag x\n', '\n<<: {}\n',
                    '\nstatus: ACTIVE\n', '\na: yes\n']:
            with self.assertRaises((Closed, yaml.YAMLError)):
                parse(CANDIDATE.read_text(encoding='utf-8') + bad)


class PromotionContracts(unittest.TestCase):
    """Promotion equivalence and recorded evidence; no live deployment or retrieval."""
    promotion = ROOT / 'candidates/promotion_v1.1'

    def setUp(self):
        self.before = load(INTEGRATION / 'HUB_ROUTER_v1.1-integration-candidate.yaml')
        self.after = load(self.promotion / 'HUB_ROUTER_v1.1.yaml')
        self.catalog_before = load(INTEGRATION / 'HUB_PACKAGE_CATALOG_v1.0-integration-candidate.yaml')
        self.catalog_after = load(self.promotion / 'HUB_PACKAGE_CATALOG_v1.0.yaml')

    def test_ci_only_promoted_router_reference_and_budget(self):
        before = (INTEGRATION / 'HUB_CI_v1.1-candidate.md').read_bytes()
        after = (self.promotion / 'HUB_CI_v1.1.md').read_bytes()
        self.assertEqual(before.count(b'HUB_ROUTER_v1.1-integration-candidate.yaml'), 1)
        self.assertEqual(after, before.replace(b'HUB_ROUTER_v1.1-integration-candidate.yaml',
                                               b'HUB_ROUTER_v1.1.yaml'))
        self.assertNotIn(b'integration-candidate', after)
        lf = after.decode('utf-8').replace('\r\n', '\n')
        self.assertLessEqual(len(lf), 8000)
        self.assertLessEqual(len(lf.replace('\n', '\r\n')), 8000)
        self.assertLess(len(after), len(before))

    def test_router_all_routing_and_authority_contracts_unchanged(self):
        # Allow changes only to core identity/activation and evidence metadata.
        allowed = {'router_version', 'status', 'active', 'deployment', 'activation_notice',
                   'contracts', 'eligibility', 'evidence'}
        self.assertEqual({k: v for k, v in self.before.items() if k not in allowed},
                         {k: v for k, v in self.after.items() if k not in allowed})
        self.assertEqual(set(self.before), set(self.after))
        for name in ['simulation']:
            self.assertEqual(self.before['eligibility'][name], self.after['eligibility'][name])
        self.assertEqual(self.after['status'], 'ACTIVE')
        self.assertTrue(self.after['active'])
        self.assertEqual(self.after['router_version'], '1.1')
        self.assertEqual(self.after['deployment'], 'PREPARED_NOT_DEPLOYED')
        self.assertNotIn('future_runtime', self.after['eligibility'])
        self.assertNotIn('candidate_runtime', self.after['eligibility'])
        self.assertIn('Installed CI must delegate', self.after['eligibility']['runtime'])
        self.assertIn('not admitted as active', self.after['eligibility']['candidate_admission'])
        self.assertIn('user-action authorization', self.after['activation_notice'])
        for name in ['architecture', 'root_catalog']:
            expected = dict(self.before['contracts'][name], status='ACTIVE')
            expected['file'] = expected['file'].replace('-integration-candidate', '')
            self.assertEqual(self.after['contracts'][name], expected)
            self.assertTrue((self.promotion / expected['file']).is_file())
        self.assertEqual(self.before['contracts']['role_boundary'], self.after['contracts']['role_boundary'])
        self.assertIn('Exact manually installed v1.1', self.after['contracts']['binding_scope'])

    def test_catalog_exact_five_bindings_and_no_new_migration(self):
        before = self.catalog_before
        after = self.catalog_after
        metadata = {'status', 'active', 'runtime_ready', 'identity_binding', 'live_integration',
                    'deployment', 'active_revision_evidence', 'packages'}
        self.assertEqual({k: v for k, v in before.items() if k not in metadata},
                         {k: v for k, v in after.items() if k not in metadata})
        self.assertEqual(len(after['packages']), 5)
        self.assertEqual(len({p['package_id'] for p in after['packages']}), 5)
        for old, new in zip(before['packages'], after['packages']):
            expected = copy.deepcopy(old)
            if old['package_id'] in ['HUB-PKG-CREATIVE', 'HUB-PKG-BRAINSTORM', 'HUB-PKG-AIS']:
                expected['location']['verification'] = 'FULL_EXACT_SOURCE_REQUIRED; USER_REPORTED_LIVE_SUCCESS_PATH_VERIFIED'
            self.assertEqual(new, expected)
            self.assertIsNone(new['local_catalog'])
            self.assertEqual(new['requires'], [])
        technical = next(p for p in after['packages'] if p['package_id'] == 'HUB-PKG-TECHNICAL')
        self.assertEqual(technical, next(p for p in before['packages'] if p['package_id'] == 'HUB-PKG-TECHNICAL'))
        self.assertEqual(technical['binding_mode'], 'LIBRARY_MODULE')
        self.assertNotIn('PROJECT_SOURCE', str(technical))
        self.assertEqual(technical['location']['library_file_id'], 'libfile_bab7d55cd85c819198291acf135099fd')
        self.assertEqual(technical['location']['root'], 'Central Hub Config')
        self.assertEqual((technical['version'], technical['location']['library_version_id']), ('1.0', '1'))

    def test_activation_is_normal_but_local_preparation_is_not_deployment(self):
        for core in [self.after, self.catalog_after]:
            self.assertEqual(core['status'], 'ACTIVE')
            self.assertTrue(core['active'])
            self.assertEqual(core['deployment'], 'PREPARED_NOT_DEPLOYED')
        self.assertTrue(self.catalog_after['runtime_ready'])
        for text in [self.after['activation_notice'], self.after['eligibility']['runtime'],
                     self.after['contracts']['binding_scope'], self.catalog_after['identity_binding']]:
            for stale in ['MANUAL AUTHORIZED INTEGRATION TRIAL', 'TRIAL_ONLY', 'CANDIDATE, NOT ACTIVE']:
                self.assertNotIn(stale, text)
        self.assertEqual(self.catalog_after['live_integration'], 'LIVE INTEGRATION PARTIAL')
        self.assertIn('I08 UNVERIFIABLE', self.after['evidence']['live_routing'])
        self.assertIn('UNVERIFIABLE', self.after['evidence']['live_failure_path'])
        self.assertIn('repository evidence only', self.after['evidence']['result_record'])

    def test_architecture_preserves_identity_composition_and_owner_sections(self):
        before = (INTEGRATION / 'HUB_ARCHITECTURE_v1.0-integration-candidate.md').read_text(encoding='utf-8')
        after = (self.promotion / 'HUB_ARCHITECTURE_v1.0.md').read_text(encoding='utf-8')
        self.assertIn('Status: ACTIVE', after)
        self.assertNotIn('Status: CANDIDATE', after)
        for number in [4, 5, 7, 9, 11]:
            def section(text):
                return text.split('## %d.' % number, 1)[1].split('## %d.' % (number + 1), 1)[0]
            self.assertEqual(section(before), section(after))
        self.assertNotIn('integration NOT_RUN', after)
        self.assertNotIn('Core candidate chỉ eligible', after)
        self.assertIn('I08 UNVERIFIABLE', after)

    def test_result_records_success_and_unverified_failure_without_overclaim(self):
        text = (INTEGRATION / 'HUB_V1_1_LIVE_INTEGRATION_RESULT.md').read_text(encoding='utf-8')
        cases = [line for line in text.splitlines() if line.startswith('| I')]
        self.assertEqual(len(cases), 10)
        self.assertEqual(sum('| PASS |' in line for line in cases), 9)
        i08 = next(line for line in cases if line.startswith('| I08 '))
        self.assertIn('| UNVERIFIABLE |', i08)
        self.assertNotIn('| PASS |', i08)
        self.assertNotIn('| FAIL |', i08)
        for token in ['LIVE INTEGRATION PARTIAL', 'USER_REPORTED',
                      'DEPLOYMENT SETUP FAILURE — RESOLVED', 'LIVE VERIFIED SUCCESS PATHS',
                      'LIVE UNVERIFIED FAILURE PATH', 'AIS_ROUTER_v1.0.yaml', 'AIS_ROUTER_v1.1.yaml',
                      'FULL_FILE 9/9', 'FULL_FILE 43/43', '104/104', 'has_more=false']:
            self.assertIn(token, text)
        self.assertIn('UNVERIFIABLE', self.catalog_after['active_revision_evidence']['integration'])

    def test_manual_plan_and_legacy_dependencies_unchanged(self):
        plan = (self.promotion / 'HUB_V1_1_PROMOTION_PLAN.md').read_text(encoding='utf-8')
        for file in ['HUB_CI_v1.1.md', 'HUB_ROUTER_v1.1.yaml', 'HUB_ARCHITECTURE_v1.0.md',
                     'HUB_PACKAGE_CATALOG_v1.0.yaml', 'HUB_CI_v1.0.md', 'HUB_ROUTER_v1.0.yaml',
                     'TECHNICAL_v1.0.md', 'AIS_ROUTER_v1.1.yaml']:
            self.assertIn(file, plan)
        for token in ['PROJECT INSTRUCTIONS', 'PROJECT SOURCES', 'LIBRARY', 'LEGACY SOURCES',
                      'PREPARED_NOT_DEPLOYED', 'ROLLBACK != FALLBACK']:
            self.assertIn(token, plan)
        ais = (ROOT / 'tool_pipelines/AIS/AIS_PIPELINE_v1.0.md').read_text(encoding='utf-8')
        self.assertIn('Read `AIS_ROUTER_v1.1.yaml` fully', ais)
        self.assertNotIn('`AIS_ROUTER_v1.0.yaml`', ais)
        self.assertTrue((historical_source('HUB_ROUTER_v1.0.yaml')).is_file())
        self.assertTrue((historical_source('domains/technical/TECHNICAL_v1.0.md')).is_file())


class ActiveSingletonMigration(unittest.TestCase):
    def test_repository_activation_preserves_accepted_router_algorithm(self):
        promotion = ROOT / 'candidates/promotion_v1.1'
        self.assertEqual((ROOT / 'HUB_CI_v1.1.md').read_bytes(),
                         (promotion / 'HUB_CI_v1.1.md').read_bytes())
        before = load(promotion / 'HUB_ROUTER_v1.1.yaml')
        after = load(ROOT / 'HUB_ROUTER_v1.1.yaml')
        expected = copy.deepcopy(before)
        expected['deployment'] = 'REPOSITORY_ACTIVE; PROJECT_DEPLOYMENT_NOT_VERIFIED'
        expected['binding_dispatch']['LEGACY_PROJECT_SOURCE'] = expected['binding_dispatch']['LEGACY_PROJECT_SOURCE'].replace('four explicitly declared', 'explicitly declared')
        expected['evidence']['result_record'] = expected['evidence']['result_record'].replace('../integration_v1.1/', 'candidates/integration_v1.1/')
        self.assertEqual(after, expected)  # No algorithm/authorization change admitted.
        for key in ['architecture', 'root_catalog']:
            contract = after['contracts'][key]
            self.assertTrue((ROOT / contract['file']).is_file())
            self.assertEqual(contract['status'], 'ACTIVE')
        architecture = (ROOT / 'HUB_ARCHITECTURE_v1.0.md').read_text(encoding='utf-8')
        previous = (promotion / 'HUB_ARCHITECTURE_v1.0.md').read_text(encoding='utf-8')
        self.assertIn('Status: ACTIVE', architecture)
        self.assertIn('UNRESOLVED', architecture)
        for number in [3, 4, 5, 7, 9, 10, 11]:
            def section(text):
                return text.split('## %d.' % number, 1)[1].split('## %d.' % (number + 1), 1)[0]
            self.assertEqual(section(architecture), section(previous))
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        for name in ['HUB_CI_v1.1.md', 'HUB_ROUTER_v1.1.yaml', 'HUB_ARCHITECTURE_v1.0.md',
                     'HUB_PACKAGE_CATALOG_v1.0.yaml', 'REPOSITORY ACTIVE != PROJECT DEPLOYED']:
            self.assertIn(name, readme)
        self.assertNotIn('Router active vẫn v1.0', readme)

    def test_two_library_headers_and_byte_exact_bodies(self):
        modules = [
            ('HUB-DOM-CREATIVE', 'HUB-PKG-CREATIVE', 'DOMAIN_CONTROL', 'domains/creative/CREATIVE_v1.0.md'),
            ('HUB-CAP-BRAINSTORM', 'HUB-PKG-BRAINSTORM', 'CAPABILITY', 'capabilities/BRAINSTORM_v1.0.md')]
        for module, package, role, source in modules:
            with self.subTest(module=module):
                data = (ROOT / ('library_modules/' + module + '_v1.0.md')).read_bytes()
                prefix, body = data.split(b'Version: 1.0\n', 1)
                self.assertEqual(body, (historical_source(source)).read_bytes().split(b'\n', 1)[1])
                header = prefix.decode('utf-8').splitlines()
                for key, value in [('Module ID', module), ('Package ID', package),
                                   ('Runtime role', role), ('Status', 'ACTIVE')]:
                    self.assertEqual([line for line in header if line.startswith(key + ':')],
                                     [key + ': ' + value])
                scope = [line for line in header if line.startswith('Scope: ')]
                self.assertEqual(len(scope), 1)
                self.assertGreater(len(scope[0]), len('Scope: '))
                self.assertFalse(data.startswith(b'\xef\xbb\xbf'))
                for relation in ['Refines:', 'Complements:', 'Requires:']:
                    self.assertNotIn(relation, prefix.decode('utf-8'))

    def test_single_bindings_unresolved_migrations_and_four_smoke_cases(self):
        old = load(ROOT / 'candidates/promotion_v1.1/HUB_PACKAGE_CATALOG_v1.0.yaml')
        new = load(ROOT / 'HUB_PACKAGE_CATALOG_v1.0.yaml')
        self.assertEqual(new['status'], 'ACTIVE')
        self.assertTrue(new['active'])
        self.assertEqual(new['deployment'], 'REPOSITORY_ACTIVE; PROJECT_DEPLOYMENT_NOT_VERIFIED')
        self.assertEqual(new['library_discovery_root'], 'Central Hub Config')
        self.assertEqual(len(new['packages']), 5)
        self.assertEqual([p['package_id'] for p in old['packages']],
                         [p['package_id'] for p in new['packages']])
        for before, after in zip(old['packages'], new['packages']):
            if after['package_id'] in ['HUB-PKG-CREATIVE', 'HUB-PKG-BRAINSTORM']:
                self.assertEqual({k: v for k, v in before.items() if k not in {'status', 'binding_mode', 'location'}},
                                 {k: v for k, v in after.items() if k not in {'status', 'binding_mode', 'location'}})
                self.assertEqual(after['status'], 'ACTIVE')
                self.assertEqual(after['binding_mode'], 'LIBRARY_MODULE')
                location = after['location']
                self.assertEqual((location['class'], location['root']), ('LIBRARY', 'Central Hub Config'))
                self.assertEqual(location['resolution'], 'UNRESOLVED')
                self.assertEqual(location['verification'], 'NOT_PERFORMED')
                for key in ['locator', 'library_file_id', 'library_version_id']:
                    self.assertIsNone(location[key])
                self.assertNotIn('PROJECT_SOURCE', str(after))
                self.assertNotIn('declared_source_path', location)
            else:
                self.assertEqual(before, after)  # TECHNICAL, AIS and ImageT unchanged.
            self.assertIsNone(after['local_catalog'])
            self.assertEqual(after['requires'], [])
        plan = (ROOT / 'HUB_LIBRARY_SINGLETON_MIGRATION.md').read_text(encoding='utf-8')
        cases = [line for line in plan.splitlines() if line.startswith('| S0')]
        self.assertEqual(len(cases), 4)
        for index, line in enumerate(cases, 1):
            self.assertTrue(line.startswith('| S%02d' % index))
        for token in ['NOT_RUN', 'library_file_id', 'Library `version_id`', 'FULL_FILE',
                      'REMOVE FROM PROJECT SOURCES', 'ROLLBACK != FALLBACK']:
            if token == 'REMOVE FROM PROJECT SOURCES':
                self.assertIn('gỡ khỏi live Project Sources', plan)
            else:
                self.assertIn(token, plan)


if __name__ == '__main__':
    unittest.main()

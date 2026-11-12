"""Test-only scope and read fixtures for the generic active Hub Router."""
import copy
import unittest

from test_hub_contracts import Closed, HUB_ROUTER, ROOT_CATALOG, load


def integration_read_spec(entry, observations, *, direct_identity_usable=True, scoped_search_sufficient=False):
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
                        root=location['root'])
        if location['root'] != 'Central Hub Config' or observed.get('location') != 'LIBRARY':
            raise Closed('wrong root or non-Library substitute')
        if entry['status'] != 'ACTIVE' or observed.get('body_matches') is not True:
            raise Closed('inactive or material body mismatch')
        if direct_identity_usable:
            if not location.get('library_file_id'):
                raise Closed('missing verified direct identity')
            expected['library_file_id'] = location['library_file_id']
            if location.get('library_version_id') is not None:
                expected['library_version_id'] = location['library_version_id']
        else:
            # Declared fixture evidence only, not a Library search or completeness detector.
            if not scoped_search_sufficient or not observed.get('opened_object'):
                raise Closed('unresolved scoped coverage or object identity')
            if observed.get('library_file_id') is not None or observed.get('library_version_id') is not None:
                raise Closed('unverified internal identity')
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
                live_integration='NOT_RUN', module_id=entry['entrypoint_module_id'],
                library_file_id=observed.get('library_file_id'),
                library_version_id=observed.get('library_version_id'))


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
    """Explicit parity projection; read-only projection of active entrypoints."""
    catalog = load(ROOT_CATALOG)
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
    """Finite acceptance oracle. Plans/fixture reads only; never executes instruction YAML.

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


class RouterCompositionTests(unittest.TestCase):
    def test_multi_role_cross_portion_composition(self):
        fixture = current_metadata_fixture()
        selected = {'HUB-PKG-CONCEPT-DEVELOPMENT', 'HUB-PKG-AUTHORING'}
        result = simulate(fixture, selected)
        self.assertEqual({key[0] for key in result['spec_verified']}, selected)
        roles = {row['entrypoint']['runtime_role'] for row in fixture['packages'] if row['package_id'] in selected}
        self.assertEqual(roles, {'DOMAIN_CONTROL', 'CAPABILITY'})
        mixed = simulate(fixture, selected | {'HUB-PKG-AIS'}, pipeline_needs={'HUB-PKG-AIS'})
        self.assertEqual({key[0] for key in mixed['spec_verified']}, selected | {'HUB-PKG-AIS'})
        for identity in selected:
            self.assertEqual({key[0] for key in simulate(fixture, {identity})['spec_verified']}, {identity})

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

    def test_unadmitted_package_and_leaf_are_not_auto_selected(self):
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

    def test_L_pipeline_entrypoint_is_opaque_and_independently_selected(self):
        fixture = current_metadata_fixture()
        result = simulate(fixture, {'HUB-PKG-TECHNICAL', 'HUB-PKG-AIS'}, pipeline_needs={'HUB-PKG-AIS'})
        self.assertEqual(result['pipeline_entrypoints'], [('HUB-PKG-AIS', 'HUB-PIPE-AIS')])
        self.assertEqual(set(result['spec_reads']), {'HUB-TECH-ENTRY', 'HUB-PIPE-AIS'})
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


class LibraryReadTests(unittest.TestCase):
    def library_identity_fixture(self, package='HUB-PKG-TECHNICAL'):
        """Declared Library observations; never accesses the platform or infers evidence."""
        catalog = load(ROOT_CATALOG)
        entry = next(p for p in catalog['packages'] if p['package_id'] == package)
        observed = dict(module_id=entry['entrypoint_module_id'], package_id=package,
                        runtime_role=entry['runtime_role'], status='ACTIVE', version=entry['version'],
                        root='Central Hub Config', location='LIBRARY', read_kind='FULL_FILE', has_more=False,
                        body_matches=True, opened_object='SYNTHETIC_CURRENT_SURFACE_OBJECT')
        return entry, observed

    def test_library_direct_identity_full_read_body_and_bound_revision(self):
        entry, observed = self.library_identity_fixture()
        entry['location'].update(library_file_id='FIXTURE_FILE', library_version_id='FIXTURE_REVISION')
        observed.update(library_file_id='FIXTURE_FILE', library_version_id='FIXTURE_REVISION')
        result = integration_read_spec(entry, [observed])
        self.assertEqual(result['library_file_id'], entry['location']['library_file_id'])
        self.assertEqual(result['library_version_id'], entry['location']['library_version_id'])
        self.assertFalse(result['runtime_ready'])
        for key, value in [('body_matches', False), ('library_file_id', 'wrong-object'),
                           ('library_version_id', 'wrong-revision')]:
            with self.subTest(key=key), self.assertRaises(Closed):
                integration_read_spec(entry, [dict(observed, **{key: value})], scoped_search_sufficient=True)

    def test_library_root_scoped_identity_without_internal_ids_is_generic(self):
        for package in ['HUB-PKG-TECHNICAL', 'HUB-PKG-AUTHORING', 'HUB-PKG-IMAGET']:
            with self.subTest(package=package):
                entry, observed = self.library_identity_fixture(package)
                before = copy.deepcopy(entry)
                result = integration_read_spec(entry, [observed], direct_identity_usable=False,
                                               scoped_search_sufficient=True)
                self.assertEqual(result['module_id'], entry['entrypoint_module_id'])
                self.assertIsNone(result['library_file_id'])
                self.assertIsNone(result['library_version_id'])
                self.assertEqual(result['live_integration'], 'NOT_RUN')
                self.assertFalse(result['runtime_ready'])
                self.assertEqual(entry, before)  # Do not erase existing verified IDs or invent missing ones.

    def test_library_scoped_wrong_headers_partial_body_root_and_substitutes_rejected(self):
        entry, observed = self.library_identity_fixture('HUB-PKG-AUTHORING')
        observed['filename'] = 'HUB-AUTH-ENTRY_v1.0.md'  # A perfect name cannot fix bad identity.
        mutations = [('module_id', 'OTHER'), ('package_id', 'OTHER'), ('runtime_role', 'DOMAIN_CONTROL'),
                     ('status', 'CANDIDATE'), ('status', 'INACTIVE'), ('version', 'wrong'),
                     ('read_kind', 'SNIPPET'), ('read_kind', 'HEADER_ONLY'), ('has_more', True),
                     ('body_matches', False), ('body_matches', None), ('root', 'Other root'),
                     ('opened_object', None)]
        mutations += [('location', source) for source in
                      ['repository', 'local_filesystem', 'PROJECT_SOURCES', 'memory', 'prior_chat', 'archive']]
        for key, value in mutations:
            with self.subTest(key=key, value=value), self.assertRaises(Closed):
                integration_read_spec(entry, [dict(observed, **{key: value})],
                                      direct_identity_usable=False, scoped_search_sufficient=True)

    def test_library_scoped_duplicates_unknown_coverage_and_revision_guessing_block(self):
        entry, observed = self.library_identity_fixture('HUB-PKG-AUTHORING')
        for observations in [[], [observed, dict(observed, opened_object='SYNTHETIC_SECOND_OBJECT')]]:
            with self.subTest(observations=observations), self.assertRaises(Closed):
                integration_read_spec(entry, observations, direct_identity_usable=False,
                                      scoped_search_sufficient=True)
        with self.assertRaises(Closed):  # One visible match without sufficient coverage is still unresolved.
            integration_read_spec(entry, [observed], direct_identity_usable=False)
        current_label = dict(observed, displayed_revision='Current version')
        result = integration_read_spec(entry, [current_label], direct_identity_usable=False,
                                       scoped_search_sufficient=True)
        self.assertIsNone(result['library_version_id'])
        with self.assertRaises(Closed):
            integration_read_spec(entry, [dict(current_label, library_version_id='1')],
                                  direct_identity_usable=False, scoped_search_sufficient=True)


class ActiveRouterTests(unittest.TestCase):
    def test_prior_none_and_activation_do_not_route_the_current_turn(self):
        router = load(HUB_ROUTER)
        self.assertEqual(router['default'], 'NONE')
        rule = router['stages']['ROOT_PACKAGE_SELECTION']
        self.assertIn('Prior selection or non-selection', rule)
        self.assertIn('including direct tool use', rule)
        self.assertNotIn('AIS', rule)
        fixture = current_metadata_fixture()
        aid = 'HUB-PKG-AIS'
        results = [simulate(fixture, scopes, pipeline_needs=needs)
                   for scopes, needs in [(set(), ()), ({aid}, (aid,)), (set(), ())]]
        self.assertEqual([r['spec_reads'] for r in results], [[], ['HUB-PIPE-AIS'], []])
        self.assertTrue(all(not r['runtime_ready'] for r in results))

    def test_growth_selects_only_needed_leaf_closure(self):
        for count in (24, 40):
            result = simulate(synthetic_growing_fixture(count), {'X'})
            self.assertEqual(result['spec_reads'],
                             ['SYNTHETIC_ENTRY', 'SYNTHETIC_LOCAL_CATALOG',
                              'SYNTHETIC_LEAF_0', 'SYNTHETIC_LEAF_1', 'SYNTHETIC_LEAF_2'])

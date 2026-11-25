"""Test-only scope and read fixtures for the generic active Hub Router."""
import copy
import re
import unittest

from test_ais_research_core import execution_oracle, search_spec
from test_hub_contracts import Closed, HUB_ROUTER, ROOT_CATALOG, entry_path, load, media_leaf_bindings, package


def integration_read_spec(binding, observations):
    """Validate declared test observations without performing a lookup or execution."""
    if not observations:
        raise Closed('ARTIFACT_MISSING')
    if len(observations) != 1:
        raise Closed('AMBIGUOUS_MODULE')
    observed = observations[0]
    if observed.get('source') != binding['source'] or not observed.get('accepted_source'):
        raise Closed('SOURCE_MISMATCH')
    if observed.get('read_kind') != 'FULL_FILE' or observed.get('has_more') is not False:
        raise Closed('FULL_FILE_REQUIRED')
    for field in ('module_id', 'package_id', 'runtime_role', 'version'):
        if observed.get(field) != binding[field]:
            raise Closed('HEADER_MISMATCH:' + field)
    if binding['status'] != 'ACTIVE' or observed.get('status') != 'ACTIVE':
        raise Closed('INACTIVE_MODULE')
    if observed.get('body_matches') is not True:
        raise Closed('MATERIAL_BODY_MISMATCH')


def synthetic_module(module_id, package_id, scopes, role='DOMAIN_CONTROL', **changes):
    module = dict(module_id=module_id, package_id=package_id, runtime_role=role,
                  status='ACTIVE', version='1.0', scopes=set(scopes),
                  refines=[], complements=[], requires=[], decisions={},
                  source=f'fixtures/{module_id}.md')
    module.update(changes)
    return module


def synthetic_package(module):
    return dict(package_id=module['package_id'], entrypoint=copy.deepcopy(module),
                applicability=set(module['scopes']), local_catalog=None, status='ACTIVE')


def synthetic_fixture(*modules):
    """One entrypoint per package; all data stays inside this test module."""
    return dict(status='ACTIVE', packages=[synthetic_package(m) for m in modules],
                local_catalogs={}, artifacts={m['module_id']: [dict(copy.deepcopy(m),
                read_kind='FULL_FILE', has_more=False, accepted_source=True, body_matches=True)] for m in modules}, evidence='SPEC_FIXTURE_ONLY')


def synthetic_growing_fixture(count=24):
    entry = synthetic_module('SYNTHETIC_ENTRY', 'SYNTHETIC_PACKAGE', {'X'})
    fixture = synthetic_fixture(entry)
    catalog = synthetic_module('SYNTHETIC_LOCAL_CATALOG', entry['package_id'], set(),
                               role='PACKAGE_CATALOG')
    fixture['packages'][0]['local_catalog'] = catalog
    fixture['artifacts'][catalog['module_id']] = [dict(catalog, read_kind='FULL_FILE', has_more=False, accepted_source=True, body_matches=True)]
    leaves = [synthetic_module(f'SYNTHETIC_LEAF_{i}', entry['package_id'], {f'UNRELATED_{i}'})
              for i in range(count)]
    leaves[0]['scopes'] = {'X'}
    leaves[0]['requires'] = [dict(module_id=leaves[1]['module_id'])]
    leaves[1]['requires'] = [dict(module_id=leaves[2]['module_id'])]
    fixture['local_catalogs'][entry['package_id']] = leaves
    for leaf in leaves:
        fixture['artifacts'][leaf['module_id']] = [dict(copy.deepcopy(leaf), read_kind='FULL_FILE', has_more=False, accepted_source=True, body_matches=True)]
    return fixture


def current_metadata_fixture():
    """Explicit parity projection; read-only projection of active entrypoints."""
    catalog = load(ROOT_CATALOG)
    modules = []
    for row in catalog['packages']:
        module = synthetic_module(row['entrypoint_module_id'], row['package_id'],
                                  {row['package_id']}, row['runtime_role'],
                                  version=row['version'], source=row['source'])
        module['identity_evidence'] = 'CURRENT_ENTRYPOINT_METADATA_ONLY'
        modules.append(module)
    fixture = synthetic_fixture(*modules)
    fixture['source_catalog_status'] = catalog['status']
    return fixture


def simulate(fixture, scopes, *, pipeline_needs=(), requested_packages=()):
    """Finite acceptance oracle. Plans/fixture reads only; never executes instruction YAML.

    The fixture models an accepted deployment, with fake full-read records. Current
    route parity uses an explicitly labeled metadata projection, not new real headers.
    """
    scopes = set(scopes)
    result = dict(planned=[], spec_verified=[], blocked={}, module_scopes={},
                  direct_dependencies=[], relations_used=[], artifact_requests=[],
                  spec_reads=[], local_catalogs_consulted=[], pipeline_entrypoints=[],
                  runtime_ready=False, live_source_retrieval='NOT_RUN')
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
        records = fixture['artifacts'].get(identity, [])
        try:
            integration_read_spec(binding, records)
        except Closed as error:
            raise Closed(f'{error}:{identity}') from error
        record = records[0]
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
            candidates = fixture['local_catalogs'].get(package_id, [package['entrypoint']])
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
    return result


class RouterCompositionTests(unittest.TestCase):
    def test_multi_role_cross_portion_composition(self):
        fixture = current_metadata_fixture()
        selected = {'HUB-PKG-MEDIA', 'HUB-PKG-AUTHORING'}
        result = simulate(fixture, selected)
        self.assertEqual({key[0] for key in result['spec_verified']}, selected)
        roles = {row['entrypoint']['runtime_role'] for row in fixture['packages'] if row['package_id'] in selected}
        self.assertEqual(roles, {'DOMAIN_CONTROL', 'CAPABILITY'})
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
        domain = synthetic_module('SYNTHETIC_DOMAIN_ENTRY', 'SYNTHETIC_DOMAIN', {'SYNTHETIC_DOMAIN'})
        pipeline = synthetic_module('SYNTHETIC_PIPELINE_ENTRY', 'SYNTHETIC_PIPELINE', {'SYNTHETIC_PIPELINE'},
                                    role='TOOL_PIPELINE')
        fixture = synthetic_fixture(domain, pipeline)
        result = simulate(fixture, {'SYNTHETIC_DOMAIN', 'SYNTHETIC_PIPELINE'}, pipeline_needs={'SYNTHETIC_PIPELINE'})
        self.assertEqual(result['pipeline_entrypoints'], [('SYNTHETIC_PIPELINE', 'SYNTHETIC_PIPELINE_ENTRY')])
        self.assertEqual(set(result['spec_reads']), {'SYNTHETIC_DOMAIN_ENTRY', 'SYNTHETIC_PIPELINE_ENTRY'})
        denied = simulate(fixture, {'SYNTHETIC_DOMAIN', 'SYNTHETIC_PIPELINE'})
        self.assertEqual(denied['pipeline_entrypoints'], [])
        edge = dict(module_id=pipeline['module_id'], package_id=pipeline['package_id'], admitted=True)
        domain['requires'] = [edge]
        fixture = synthetic_fixture(domain, pipeline)
        denied = simulate(fixture, {'SYNTHETIC_DOMAIN'})
        self.assertTrue(any('PIPELINE_NEED_NOT_AUTHORIZATION' in reason for reason in denied['blocked'].values()))

    def test_M_scope_change_does_not_keep_activation(self):
        domain = synthetic_module('SYNTHETIC_DOMAIN_ENTRY', 'SYNTHETIC_DOMAIN', {'SYNTHETIC_DOMAIN'})
        pipeline = synthetic_module('SYNTHETIC_PIPELINE_ENTRY', 'SYNTHETIC_PIPELINE', {'SYNTHETIC_PIPELINE'},
                                    role='TOOL_PIPELINE')
        fixture = synthetic_fixture(domain, pipeline)
        old = simulate(fixture, {'SYNTHETIC_DOMAIN', 'SYNTHETIC_PIPELINE'}, pipeline_needs={'SYNTHETIC_PIPELINE'})
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

    def test_read_failures_block_only_the_dependent_branch(self):
        needed = synthetic_module('SYNTHETIC_A', 'SYNTHETIC_PKG_A', {'X'})
        other = synthetic_module('SYNTHETIC_B', 'SYNTHETIC_PKG_B', {'Y'})
        for change in ({'read_kind': 'HEADER_ONLY'}, {'source': 'archive/SYNTHETIC_A.md'},
                       {'accepted_source': False}):
            fixture = synthetic_fixture(needed, other)
            fixture['artifacts'][needed['module_id']][0].update(change)
            result = simulate(fixture, {'X', 'Y'})
            self.assertIn(needed['package_id'], result['blocked'])
            self.assertEqual(result['spec_reads'], [other['module_id']])

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


class PinnedSourceReadTests(unittest.TestCase):
    def test_exact_source_requires_full_matching_material_read(self):
        row = package('AUTHORING')
        binding = dict(row, module_id=row['entrypoint_module_id'])
        observed = dict(binding, read_kind='FULL_FILE', has_more=False,
                        accepted_source=True, body_matches=True)
        integration_read_spec(binding, [observed])
        for field, value in (
            ('module_id', 'LOOKALIKE'), ('package_id', 'OTHER'), ('runtime_role', 'DOMAIN_CONTROL'),
            ('status', 'INACTIVE'), ('version', '9.0'), ('read_kind', 'SNIPPET'),
            ('read_kind', 'HEADER_ONLY'), ('read_kind', 'SEARCH_HIT'), ('has_more', True),
            ('body_matches', False), ('body_matches', None), ('accepted_source', False),
            ('source', 'Source_archive/' + row['source']),
            ('source', row['source'].replace('v1.1', 'v1.2')),
            ('source', 'lookalike/' + entry_path(row).name),
        ):
            with self.subTest(field=field, value=value), self.assertRaises(Closed):
                integration_read_spec(binding, [dict(observed, **{field: value})])
        for records in ([], [observed, dict(observed)]):
            with self.subTest(records=len(records)), self.assertRaises(Closed):
                integration_read_spec(binding, records)

    def test_source_resolution_contract_preserves_read_and_authority_boundaries(self):
        router = load(HUB_ROUTER)
        self.assertNotIn('library', router)
        rule = router['stages']['SOURCE_RESOLUTION']
        for phrase in ('exactly one pinned source', 'FULL_FILE', 'Package ID where applicable',
                       'material body and declared relations', 'headers, hits, summaries and partial reads',
                       'archive copies, guessed versions', 'authorization and execution'):
            self.assertIn(phrase, rule)
        self.assertIn('dependent work', router['failure'])


class ActiveRouterTests(unittest.TestCase):
    def test_prior_none_and_activation_do_not_route_the_current_turn(self):
        router = load(HUB_ROUTER)
        self.assertEqual(router['default'], 'NONE')
        rule = router['stages']['ROOT_PACKAGE_SELECTION']
        self.assertIn('Prior selection or non-selection', rule)
        self.assertIn('including direct tool use', rule)
        self.assertNotIn('AIS', rule)
        fixture = current_metadata_fixture()
        technical = 'HUB-PKG-TECHNICAL'
        results = [simulate(fixture, scopes) for scopes in (set(), {technical}, set())]
        self.assertEqual([r['spec_reads'] for r in results], [[], ['HUB-TECH-ENTRY'], []])
        self.assertTrue(all(not r['runtime_ready'] for r in results))

    def test_growth_selects_only_needed_leaf_closure(self):
        for count in (24, 40):
            result = simulate(synthetic_growing_fixture(count), {'X'})
            self.assertEqual(result['spec_reads'],
                             ['SYNTHETIC_ENTRY', 'SYNTHETIC_LOCAL_CATALOG',
                              'SYNTHETIC_LEAF_0', 'SYNTHETIC_LEAF_1', 'SYNTHETIC_LEAF_2'])

def media_plan(material_domains):
    """Project inline bindings against declared domain needs, without inferring them."""
    row = package('MEDIA')
    entry = entry_path(row).read_text(encoding='utf-8')
    bindings = re.findall(r'^\| (HUB-MEDIA-(MOVIE|MUSIC)) \|', entry, re.M)
    return tuple(module for module, domain in bindings if domain.lower() in material_domains)


def receipt_fixture(*, debug=False, blocker=None, read=None, traces=()):
    """Expected receipt for a supplied scoped observation, never a live trace."""
    if not debug and blocker is None:
        return None
    evidence = 'fixture direct trace' if traces else 'no direct execution trace'
    return '\n'.join((
        'TASK | operation=compare; stage=analysis; scope=film and recording; return=Hub',
        'DECISION | selected=Media/Movie and Music; basis=declared comparison; tool authority=none',
        f'SOURCE / DEPENDENCY | Entry 1.2 → Movie 1.1; read={read or "UNKNOWN"}',
        f'RESULT / BLOCKER | last=selection; attempt={execution_oracle(traces)}; basis={evidence}',
        f'first unresolved={blocker or "none"}; independent=Music',
    ))


class RefactorTwoRoutingTests(unittest.TestCase):
    def test_media_selects_only_material_leaves_without_automatic_ais(self):
        row = package('MEDIA')
        self.assertIn('Incidental mentions', row['applicability'])
        self.assertEqual(row['requires'], [])
        entry = entry_path(row).read_text(encoding='utf-8')
        self.assertIn('Return material external-evidence needs to Hub', entry)
        for needs, expected in (
            (set(), ()), ({'movie'}, ('HUB-MEDIA-MOVIE',)),
            ({'music'}, ('HUB-MEDIA-MUSIC',)),
            ({'movie', 'music'}, ('HUB-MEDIA-MOVIE', 'HUB-MEDIA-MUSIC')),
        ):
            with self.subTest(needs=needs):
                self.assertEqual(media_plan(needs), expected)
                selected = {row['package_id']} if needs else set()
                result = simulate(current_metadata_fixture(), selected)
                self.assertEqual(result['pipeline_entrypoints'], [])
                self.assertEqual(result['spec_reads'], ['HUB-MEDIA-ENTRY'] if needs else [])

    def test_retired_controls_grant_no_routing_authority(self):
        router = load(HUB_ROUTER)
        self.assertIn('Retired directive text grants no admission', router['stages']['COMPOSITION_VALIDATION'])
        for command in ('/CREATIVE', '/BRAINSTORM', '/DEBATE', '/NAME', '/AD'):
            directive = f'{command} example #'
            self.assertNotIn(command, str(load(ROOT_CATALOG)))
            self.assertEqual(search_spec([('USER_DIRECTIVE', directive)]), [])
        result = simulate(current_metadata_fixture(), set(),
                          requested_packages=['HUB-PKG-CONCEPT-DEVELOPMENT'])
        self.assertEqual(result['spec_reads'], [])
        self.assertEqual(result['pipeline_entrypoints'], [])

    def test_receipt_trigger_and_unknown_read(self):
        rule = load(HUB_ROUTER)['diagnostic_receipt']
        for phrase in ('explicit routing or execution debug/audit request', 'material blocker',
                       'actual read evidence', 'SCOPED_HANDOFF', 'UNKNOWN', 'CONFLICTED',
                       'private preference values', 'ordinary-turn receipt'):
            self.assertIn(phrase, rule)
        self.assertIsNone(receipt_fixture(read='FULL_FILE'))
        self.assertIn('read=UNKNOWN', receipt_fixture(debug=True))
        self.assertNotIn('FULL_FILE', receipt_fixture(debug=True))
        self.assertIn('attempt=UNKNOWN', receipt_fixture(debug=True, traces=[('search', 1, 'TIMEOUT')]))
        self.assertIn('attempt=CONFLICTED', receipt_fixture(debug=True, traces=[
            ('search', 1, 'DIRECT_EXECUTION_TRACE'), ('search', 1, 'DIRECT_NON_EXECUTION_TRACE'),
        ]))

    def test_material_blocker_emits_and_isolates_the_dependent_branch(self):
        row = package('MEDIA')
        owner = row['package_id']
        entry = synthetic_module(row['entrypoint_module_id'], owner, {'movie', 'music'},
                                 row['runtime_role'], version=row['version'], source=row['source'])
        leaves = [
            synthetic_module(identity, owner, {identity.rsplit('-', 1)[-1].lower()},
                             role, status=status, version=version, source=source)
            for identity, role, status, version, source in media_leaf_bindings()
        ]
        for read_kind in (None, 'HEADER_ONLY'):
            fixture = synthetic_fixture(entry, *leaves)
            fixture['packages'] = fixture['packages'][:1]
            fixture['local_catalogs'][owner] = leaves
            if read_kind is None:
                del fixture['artifacts']['HUB-MEDIA-MOVIE']
            else:
                fixture['artifacts']['HUB-MEDIA-MOVIE'][0]['read_kind'] = read_kind
            result = simulate(fixture, {'movie', 'music'})
            self.assertIn((owner, 'HUB-MEDIA-MOVIE'), result['blocked'])
            self.assertEqual(result['spec_reads'], [entry['module_id'], 'HUB-MEDIA-MUSIC'])
            self.assertEqual(result['spec_verified'], [(owner, 'HUB-MEDIA-MUSIC')])
            self.assertFalse(result['runtime_ready'])
        receipt = receipt_fixture(blocker='Movie source unresolved')
        self.assertIn('first unresolved=Movie source unresolved; independent=Music', receipt)


def test_supplied_context_retains_role_provenance_and_current_user_priority():
    rule = load(HUB_ROUTER)['stages']['SCOPED_HANDOFF']
    for clause in ('Validly supplied user or platform context is scoped input data',
                   'Preserve its provenance and scope', 'grants no control authority',
                   'Current explicit user input governs conflicting context for this task only',
                   'do not infer, persist or mutate stored preferences'):
        assert clause in rule

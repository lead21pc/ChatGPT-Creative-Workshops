"""STATIC / SPEC ONLY: declared premises, not model need detection or Library enforcement.

No live routing, object read/non-read, persistence, platform privacy or medical behavior is proven.
"""
import copy
import hashlib
import json
import subprocess
from pathlib import Path
import unittest

from test_hub_contracts import namespace_baseline_source, ROOT, load
from test_user_profile_candidate import brand_input, read_plan

# Exact pre-namespace release assertions; successor contracts are covered in test_canonical_namespace.py.
NAMESPACE_PREDECESSOR = Path(__file__).resolve().parents[1] / 'Source_archive/Canonical namespace migration 2026-11-11'


BASELINE = 'f06dea5be568cec9fb476a9040c723be8629507c'
RESOURCE = 'HUB-USER-PROFILE'
SHOPPING = 'HUB-PKG-SHOPPING'
FOOD = 'HUB-PKG-FOOD'
CONTRACT = 'HUB-USER-PROFILE-CONTRACT_v1.0.yaml'
FOOD_PREDECESSOR = ROOT / 'Source_archive/Food 0.1 2026-11-12/shared_resources'
OBJECTS = ('GENERAL', 'PREFERENCES', 'DIETARY_CONSTRAINTS', 'HEALTH_CONTEXT')
PUBLIC = ROOT / 'shared_resources'


def before(path):
    return subprocess.check_output(['git', 'show', f'{BASELINE}:Central Hub/{path}'], cwd=ROOT)


def validate_object(contract, payload, expected_object):
    """Test-only acceptance oracle over supplied payloads, never a runtime resolver."""
    if set(payload) != set(contract['object_schema']['required']):
        return False
    if (payload['resource_id'], payload['object_id'], payload['schema_version']) != (
            contract['resource_id'], expected_object, contract['schema_version']):
        return False
    fields = contract['objects'][expected_object]['fields']
    data = payload['data']
    if not isinstance(data, dict) or set(data) - set(fields):
        return False
    for key, value in data.items():
        if value is None:
            continue
        if fields[key] == 'optional_string' and not isinstance(value, str):
            return False
        if fields[key] == 'optional_list_of_strings' and not (
                isinstance(value, list) and all(isinstance(v, str) for v in value)):
            return False
    return True


def resolve_fixture(contract, request, observed):
    """Declared observation fixture; does not search Library or infer current need."""
    decision, objects = read_plan(contract, selected_package=request['consumer_package'],
                                  section=request['object_id'], purpose=request['purpose'],
                                  material_need=request['material_need'])
    if decision != 'ALLOW':
        return decision, ()
    if request['resource_id'] != RESOURCE or request['schema_version'] != contract['schema_version']:
        return 'UNRESOLVED', ()
    if observed['root'] != contract['read']['root'] or not observed['coverage_complete']:
        return 'UNRESOLVED', ()
    matches = observed['matches']
    if len(matches) != 1 or not observed['full_file']:
        return 'UNRESOLVED', ()
    if not validate_object(contract, matches[0], request['object_id']):
        return 'UNRESOLVED', ()
    return 'ALLOW', objects


class UserProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = load(FOOD_PREDECESSOR / CONTRACT)
        cls.templates = {o: load(PUBLIC / f'HUB-USER-PROFILE-{o}-TEMPLATE_v1.0.yaml') for o in OBJECTS}
        cls.arch = (NAMESPACE_PREDECESSOR / 'HUB_ARCHITECTURE_v1.17.md').read_text(encoding='utf-8')
        cls.section = cls.arch.split('## 14.', 1)[1]
        cls.catalog = load(NAMESPACE_PREDECESSOR / 'HUB_PACKAGE_CATALOG_v1.17.yaml')

    def plan(self, obj, purpose, need=True, consumer=SHOPPING):
        return read_plan(self.contract, selected_package=consumer, section=obj,
                         purpose=purpose, material_need=need)

    def test_P01_shared_identity_not_control_or_package(self):
        self.assertEqual((self.contract['resource_id'], self.contract['schema_version'],
                          self.contract['status']), (RESOURCE, '1.0', 'ACTIVE'))
        self.assertEqual(self.contract['resource_kind'], 'SHARED_NON_MODULE_RESOURCE')
        self.assertEqual(len(list(PUBLIC.glob('*CONTRACT*.yaml'))), 1)
        for forbidden in ('package_id', 'module_id', 'runtime_role'):
            self.assertNotIn(forbidden, self.contract)
        self.assertNotIn(RESOURCE, str(self.catalog))
        self.assertNotIn('HUB-PKG-USER-CONTEXT', str(self.catalog))

    def test_P02_four_independent_objects_and_exact_schema(self):
        self.assertEqual(tuple(self.contract['objects']), OBJECTS)
        for obj, template in self.templates.items():
            self.assertTrue(validate_object(self.contract, template, obj))
            for other in set(OBJECTS) - {obj}:
                self.assertFalse(validate_object(self.contract, template, other))
            bad = copy.deepcopy(template)
            bad['data']['undeclared'] = 'SYNTHETIC'
            self.assertFalse(validate_object(self.contract, bad, obj))
            bad = copy.deepcopy(template)
            bad['data'][next(iter(bad['data']))] = 42
            self.assertFalse(validate_object(self.contract, bad, obj))
        self.assertEqual(self.contract['read']['read_boundary'], 'ONE_OBJECT_PER_LIBRARY_OBJECT')

    def test_P03_customizable_manual_only(self):
        self.assertIs(self.contract['customizable'], True)
        self.assertEqual(self.contract['customization_mode'], 'MANUAL_USER_ONLY')
        self.assertIn('CUSTOMIZABLE != MODEL MAY MODIFY PROFILE', self.section)

    def test_P04_all_model_mutation_forbidden(self):
        mutation = self.contract['mutation']
        self.assertFalse(mutation['model_allowed'])
        self.assertEqual(mutation['authorization_exception'], 'NEVER')
        self.assertTrue({'create_real_values', 'write', 'append', 'delete', 'rewrite',
                         'normalize_and_save', 'infer_and_store', 'persist_chat_to_profile',
                         'refresh_stale_values', 'merge', 'correct_values', 'synchronize'}
                        <= set(mutation['forbidden_model_actions']))
        self.assertEqual(mutation['proposed_change'], 'RETURN_TO_USER_WITHOUT_WRITING')
        self.assertIn('PROFILE MUTATION BY MODEL: NEVER', self.section)

    def test_P05_repository_authorization_never_grants_profile_write(self):
        for repository_write_authorized in (False, True):
            mutation = self.contract['mutation']
            self.assertFalse(mutation['model_allowed'] or repository_write_authorized
                             and mutation['general_file_write_authorization_applies'])

    def test_P06_bounded_public_template_check_not_general_pii_detection(self):
        for obj, template in self.templates.items():
            self.assertEqual(set(template['data']), set(self.contract['objects'][obj]['fields']))
            self.assertTrue(all(v is None for v in template['data'].values()))
        self.assertEqual(self.contract['storage']['actual_values'], 'PRIVATE_USER_MANAGED_OUTSIDE_REPOSITORY')

    def test_P07_declared_price_only_fixture_reads_nothing(self):
        for obj in OBJECTS:
            self.assertEqual(self.plan(obj, 'purchase_filtering', need=False), ('SKIP', ()))

    def test_P08_compatibility_and_retrieval_identity_negative_cases(self):
        for obj in ('DIETARY_CONSTRAINTS', 'HEALTH_CONTEXT'):
            self.assertEqual(self.plan(obj, 'product_compatibility'), ('ALLOW', (obj,)))
        obj = 'DIETARY_CONSTRAINTS'
        request = dict(consumer_package=SHOPPING, resource_id=RESOURCE, object_id=obj,
                       schema_version='1.0', purpose='product_compatibility', material_need=True)
        observed = dict(root='Central Hub Config', coverage_complete=True, full_file=True,
                        matches=[self.templates[obj]])
        self.assertEqual(resolve_fixture(self.contract, request, observed), ('ALLOW', (obj,)))
        for change in ({'root': 'OTHER_ROOT'}, {'coverage_complete': False}, {'full_file': False},
                       {'matches': []}, {'matches': [self.templates[obj], self.templates[obj]]},
                       {'matches': [self.templates['HEALTH_CONTEXT']]}):
            self.assertEqual(resolve_fixture(self.contract, request, dict(observed, **change)), ('UNRESOLVED', ()))
        for key, value in [('resource_id', 'OTHER'), ('schema_version', '0.1-candidate')]:
            self.assertEqual(resolve_fixture(self.contract, dict(request, **{key: value}), observed), ('UNRESOLVED', ()))

    def test_P09_food_absent_no_active_preference_access(self):
        self.assertNotIn('HUB-PKG-FOOD', {p['package_id'] for p in self.catalog['packages']})
        self.assertEqual(self.plan('PREFERENCES', 'food_selection', consumer='HUB-PKG-FOOD'), ('DENY', ()))

    def test_P10_food_absent_no_active_dietary_or_health_access(self):
        for obj in ('DIETARY_CONSTRAINTS', 'HEALTH_CONTEXT'):
            self.assertEqual(self.plan(obj, 'food_compatibility', consumer='HUB-PKG-FOOD'), ('DENY', ()))

    def test_P11_access_without_need_skips_before_retrieval(self):
        self.assertEqual(self.plan('HEALTH_CONTEXT', 'product_compatibility', need=False), ('SKIP', ()))
        self.assertEqual(self.plan('GENERAL', 'purchase_filtering', consumer=None), ('SKIP', ()))
        self.assertLess(self.contract['read']['sequence'].index('HUB_VALIDATE_ACCESS_AND_CURRENT_NEED'),
                        self.contract['read']['sequence'].index('RETRIEVE_EXACT_ALLOWED_OBJECT'))

    def test_P12_need_without_access_denied(self):
        for consumer, obj, purpose in [('SYNTHETIC-UNADMITTED', 'GENERAL', 'purchase_filtering'),
                                        (SHOPPING, 'HEALTH_CONTEXT', 'product_comparison'),
                                        (SHOPPING, 'UNDECLARED_OBJECT', 'product_compatibility')]:
            self.assertEqual(self.plan(obj, purpose, consumer=consumer), ('DENY', ()))
        self.assertEqual(self.contract['default_access'], 'DENY')

    def test_P13_preference_not_hard_and_missing_not_inferred(self):
        self.assertEqual(brand_input(stored='SYNTHETIC_BRAND', explicit=None), ('SYNTHETIC_BRAND', 'PREFERENCE'))
        self.assertEqual(brand_input(stored=None, explicit=None), (None, 'UNKNOWN'))
        self.assertEqual(self.contract['interpretation']['preference_default'], 'SOFT_NOT_HARD')
        self.assertFalse(self.contract['interpretation']['model_inference_is_profile_fact'])

    def test_P14_current_override_preserves_stored_payload(self):
        payload = copy.deepcopy(self.templates['PREFERENCES'])
        payload['data']['preferred_brands'] = ['SYNTHETIC_BRAND']
        stored = copy.deepcopy(payload)
        self.assertEqual(brand_input(stored=payload['data']['preferred_brands'], explicit='avoid SYNTHETIC_BRAND'),
                         ('avoid SYNTHETIC_BRAND', 'CURRENT_USER_INPUT'))
        self.assertEqual(payload, stored)
        self.assertFalse(self.contract['interpretation']['current_override_mutates_profile'])

    def test_P15_shared_fact_independent_interpretations_synthetic_only(self):
        # Food is hypothetical here, never admitted to the active contract.
        future = copy.deepcopy(self.contract)
        future['access']['SYNTHETIC-FUTURE-FOOD'] = {'DIETARY_CONSTRAINTS': ['food_compatibility']}
        fact = {'allergies': ['SYNTHETIC_INGREDIENT']}
        stored = copy.deepcopy(fact)
        for consumer, purpose in [(SHOPPING, 'product_compatibility'),
                                  ('SYNTHETIC-FUTURE-FOOD', 'food_compatibility')]:
            self.assertEqual(read_plan(future, selected_package=consumer, section='DIETARY_CONSTRAINTS',
                                       purpose=purpose, material_need=True), ('ALLOW', ('DIETARY_CONSTRAINTS',)))
        conclusions = {'shopping': 'SYNTHETIC_LABEL_CHECK_NEEDED', 'food': 'SYNTHETIC_ALTERNATE_RECIPE'}
        self.assertNotEqual(conclusions['shopping'], conclusions['food'])
        self.assertEqual(fact, stored)
        self.assertEqual(future['owner'], 'USER')
        self.assertEqual(self.contract['interpretation']['owner'], 'CONSUMER_DOMAIN_CONTRACT')

    def test_P16_missing_profile_only_blocks_dependent_personalization(self):
        work = {'fixed_offer_comparison': set(), 'personalization': {'PREFERENCES'}}
        supplied = set()
        self.assertEqual({name for name, needs in work.items() if needs - supplied}, {'personalization'})
        self.assertEqual(self.contract['read']['unavailable'], 'DEPENDENT_PERSONALIZATION_UNRESOLVED_CONTINUE_INDEPENDENT_WORK')
        self.assertEqual(self.contract['object_schema']['field_absent_or_null'], 'UNKNOWN')

    def test_P17_future_health_without_ownership_migration(self):
        future = copy.deepcopy(self.contract)
        future['access']['HUB-PKG-HEALTH'] = {o: ['health_context'] for o in ('GENERAL', 'DIETARY_CONSTRAINTS', 'HEALTH_CONTEXT')}
        self.assertEqual((future['owner'], future['objects']), ('USER', self.contract['objects']))
        self.assertEqual(read_plan(future, selected_package='HUB-PKG-HEALTH', section='HEALTH_CONTEXT',
                                   purpose='health_context', material_need=True), ('ALLOW', ('HEALTH_CONTEXT',)))
        self.assertEqual(set(self.contract['access']), {SHOPPING})
        self.assertNotIn('HUB-PKG-HEALTH', str(self.catalog))

    def test_P18_context_snapshot_section_byte_preserved_and_independent(self):
        old = before('HUB_ARCHITECTURE_v1.16.md').decode('utf-8').split('## 13.', 1)[1]
        current = self.arch.split('## 13.', 1)[1].split('## 14.', 1)[0]
        self.assertEqual(current.strip(), old.strip())
        self.assertEqual(self.contract['context_snapshot'], {'dependency': 'NONE', 'automatic_conversion': False})
        self.assertNotIn('snapshot_id', str(self.templates))

    def test_P19_active_stack_and_shopping_semantics_preserved(self):
        paths = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', BASELINE,
                                        '--', 'library_modules', 'tool_pipelines', 'HUB_CI_v1.2.md'], cwd=ROOT, text=True).splitlines()
        self.assertTrue(paths)
        for path in paths:
            rel = path.removeprefix('Central Hub/')
            actual = namespace_baseline_source(rel).read_bytes()
            if rel == 'library_modules/HUB-DOM-SHOPPING_v1.0.md':
                first, rest = actual.split(b'## Optional shared User Profile input', 1)
                interface, rest = rest.split(b'## PREPARE', 1)
                self.assertIn(b'Profile is optional input, not Requires', interface)
                self.assertIn(b'PROFILE MUTATION BY MODEL: NEVER', interface)
                actual = first + b'## PREPARE' + rest
            with self.subTest(path=rel):
                self.assertEqual(actual, before(rel))
        self.assertEqual((NAMESPACE_PREDECESSOR / 'HUB_ROUTER_v1.1.yaml').read_bytes(), before('HUB_ROUTER_v1.1.yaml').replace(b'1.16', b'1.17'))

    def test_P20_root_topology_pins_and_byte_exact_archive(self):
        prior = load(ROOT / 'Source_archive/HUB_PACKAGE_CATALOG_v1.16.yaml')
        self.assertEqual(self.catalog['packages'], prior['packages'])
        self.assertEqual(len(self.catalog['packages']), 6)
        router = load(NAMESPACE_PREDECESSOR / 'HUB_ROUTER_v1.1.yaml')
        for owner in ('architecture', 'root_catalog'):
            self.assertEqual(router['contracts'][owner]['version'], '1.17')
            self.assertTrue(namespace_baseline_source(router['contracts'][owner]['file']).is_file())
        receipt = json.loads((ROOT / 'Source_archive/USER_PROFILE_ARCHIVE_RECEIPT_2026-11-11.json').read_text())
        for name, row in receipt.items():
            archived = (ROOT / row['archive']).read_bytes()
            self.assertEqual(hashlib.sha256(archived).hexdigest(), row['sha256'])
            self.assertEqual(archived, before(name))
            if name != 'HUB_ROUTER_v1.1.yaml':
                self.assertFalse((ROOT / name).exists())


class FoodProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = load(PUBLIC / CONTRACT)
        cls.before = load(FOOD_PREDECESSOR / CONTRACT)
        cls.entry = (ROOT / 'library_modules/Food/HUB-FOOD-ENTRY_v0.1.md').read_text(encoding='utf-8')
        cls.health = load(PUBLIC / 'HUB-USER-PROFILE-HEALTH_CONTEXT-TEMPLATE_v1.0.yaml')

    def plan(self, obj, purpose, need=True):
        return read_plan(self.contract, selected_package=FOOD, section=obj,
                         purpose=purpose, material_need=need)

    def test_food_access_preserves_shared_contract_except_declared_changes(self):
        mapping = {
            'GENERAL': ['food_context'],
            'PREFERENCES': ['food_selection'],
            'DIETARY_CONSTRAINTS': ['food_compatibility'],
            'HEALTH_CONTEXT': ['food_compatibility'],
        }
        self.assertEqual(self.contract['access'][FOOD], mapping)
        existing = copy.deepcopy(self.contract)
        existing['access'].pop(FOOD)
        self.assertIn('declared by the bound Hub Architecture', existing['read']['contract_source'])
        existing['read']['contract_source'] = self.before['read']['contract_source']
        self.assertEqual(existing, self.before)
        for obj, (purpose,) in mapping.items():
            with self.subTest(object=obj):
                self.assertEqual(self.plan(obj, purpose), ('ALLOW', (obj,)))
                self.assertEqual(self.plan(obj, purpose, need=False), ('SKIP', ()))
                self.assertEqual(self.plan(obj, 'food_recommendation'), ('DENY', ()))
        self.assertEqual(self.plan('UNDECLARED_OBJECT', 'food_compatibility'), ('DENY', ()))

    def test_food_recommendation_health_cases_a_through_d(self):
        # Applicability is supplied, so this exercises the declared read plan, not model behavior.
        cases = [
            ('A difficulty', 'Skip HEALTH_CONTEXT when it cannot affect that criterion.', False, False, ()),
            ('B overall suitability', 'request HEALTH_CONTEXT before concluding', True, False,
             ('HEALTH_CONTEXT',)),
            ('B sufficient current input', 'Use the current input directly when sufficient.', False, False, ()),
            ('C taste supplied', 'Rank by taste from sufficient current input.', False, False, ()),
            ('C taste missing', 'only if missing taste preferences could change the ranking.', False, True,
             ('PREFERENCES',)),
            ('D overall suitability established', 'Use the overall suitability path', True, False,
             ('HEALTH_CONTEXT',)),
            ('D criterion unclear', 'Clarify a materially ambiguous evaluation criterion', False, False, ()),
        ]
        for case, wording, health_needed, taste_needed, expected in cases:
            with self.subTest(case=case):
                self.assertIn(wording, self.entry)
                health = self.plan('HEALTH_CONTEXT', 'food_compatibility', need=health_needed)
                taste = self.plan('PREFERENCES', 'food_selection', need=taste_needed)
                self.assertEqual(health[1] + taste[1], expected)
        for wording in (
            'Every Food recommendation or ranking must assess health relevance.',
            'Request HEALTH_CONTEXT only when all four conditions hold:',
            'The current task has a specific suitability, ranking or preparation decision.',
            'Health context could materially change that decision.',
            'Current explicit user input does not resolve the health-relevant part.',
            'Data in HEALTH_CONTEXT could resolve the identified gap.',
            'General uncertainty is insufficient.',
        ):
            self.assertIn(wording, self.entry)

    def test_food_case_e_exact_object_and_unknown_values(self):
        request = dict(consumer_package=FOOD, resource_id=RESOURCE, object_id='HEALTH_CONTEXT',
                       schema_version='1.0', purpose='food_compatibility', material_need=True)
        observed = dict(root='Central Hub Config', coverage_complete=True, full_file=True, matches=[self.health])
        self.assertEqual(resolve_fixture(self.contract, request, observed), ('ALLOW', ('HEALTH_CONTEXT',)))
        for change in (
            {'matches': []}, {'matches': [self.health, self.health]},
            {'root': 'OTHER_ROOT'}, {'coverage_complete': False}, {'full_file': False},
            {'matches': [dict(self.health, object_id='GENERAL')]},
            {'matches': [dict(self.health, resource_id='OTHER')]},
            {'matches': [dict(self.health, schema_version='0.2')]},
            {'matches': [dict(self.health, data={'conditions': 'SYNTHETIC_INVALID'})]},
        ):
            with self.subTest(change=change):
                self.assertEqual(resolve_fixture(self.contract, request, dict(observed, **change)),
                                 ('UNRESOLVED', ()))
        for data in ({}, {'conditions': None}, {'conditions': []}):
            self.assertTrue(validate_object(self.contract, dict(self.health, data=data), 'HEALTH_CONTEXT'))
        self.assertEqual(self.contract['object_schema']['field_absent_or_null'], 'UNKNOWN')
        self.assertIn('not proof', self.contract['object_schema']['empty_list'])
        self.assertIn('leave dependent personalization unresolved', self.entry)
        self.assertIn('Continue independent analysis or clearly conditional options.', self.entry)
        self.assertIn('Null, omitted fields and empty lists provide no evidence', self.entry)

    def test_food_current_input_precedence_and_no_write(self):
        self.assertEqual(brand_input(stored='SYNTHETIC_STORED', explicit='SYNTHETIC_CURRENT'),
                         ('SYNTHETIC_CURRENT', 'CURRENT_USER_INPUT'))
        interpretation = self.contract['interpretation']
        self.assertEqual(interpretation['current_explicit_input'], 'OVERRIDES_STORED_VALUE_FOR_CURRENT_TASK_ONLY')
        self.assertFalse(interpretation['current_override_mutates_profile'])
        self.assertFalse(self.contract['mutation']['model_allowed'])
        self.assertIn('Explicit current user input overrides conflicting stored values', self.entry)
        self.assertIn('Never infer and store values, write back or persist the chat to Profile.', self.entry)

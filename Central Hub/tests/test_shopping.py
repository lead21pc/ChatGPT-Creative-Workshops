"""Current Shopping contract and test-only purchase/evidence fixtures."""
import copy
from decimal import Decimal
import re
import unittest

from test_ais_research_core import completion_oracle, execution_oracle
from test_hub_contracts import CI, LIBRARY, entry_path, package

CORE_ID = 'HUB-SHOP-ENTRY'
SEARCH_ID = 'HUB-SHOP-SEARCH'
PROFILES = ('ELECTRONICS', 'HOME', 'FOOD', 'FASHION', 'PERSONAL', 'HOBBY')


def product_candidate_spec(clues, attributes, *, linked, identity_supported=False):
    """Already-classified clues and support; no identity/source-policy inference."""
    matches, conflicts, unknowns, hard_failures = {}, {}, [], []
    for name, (value, role) in clues.items():
        if name not in attributes:
            unknowns.append(name)
        elif attributes[name]['value'] == value:
            matches[name] = value
        else:
            conflicts[name] = (value, attributes[name]['value'])
            if role == 'hard':
                hard_failures.append(name)
    gaps = unknowns + ([] if linked else ['same-SKU link'])
    established = linked and identity_supported and not unknowns
    if not established:
        gaps.append('identity of remembered item')
    return dict(matches=matches, conflicts=conflicts, unknowns=unknowns,
                support=copy.deepcopy(attributes), hard_failures=hard_failures,
                purchase_suitable=False if hard_failures else
                None if any(clues[name][1] == 'hard' for name in unknowns) else True,
                identity='ESTABLISHED' if established else 'CANDIDATE',
                gaps_to_hub=gaps)


def catalog_spec(items, target, *, supported_complete_target=None):
    """Completeness support is supplied upstream, not evaluated by Shopping."""
    complete = target == supported_complete_target
    return dict(items=tuple(items), target=target, complete=complete,
                gaps_to_hub=[] if complete else [f'coverage of {target}'])


def offer_spec(offers, *, listing_found=True):
    """Defined-set arithmetic only; no market inference or source freshness engine."""
    # Every grouping component is a supplied condition; absent material context
    # prevents aggregation. Explicit normalization is outside these small fixtures.
    dimensions = ('retailer', 'currency', 'unit', 'basis', 'conditions', 'location', 'time')
    comparable = bool(offers) and all(
        all(o.get(k) is not None for k in (*dimensions, 'sku', 'price')) for o in offers)
    if comparable:
        comparable = len({tuple(o[k] for k in dimensions) for o in offers}) == 1
    return dict(offers=copy.deepcopy(offers),
                mean=sum((Decimal(str(o['price'])) for o in offers), Decimal(0)) / len(offers)
                if comparable else None,
                average_scope='DEFINED_RETAILER_SKU_SET' if comparable else None,
                current_available=tuple(o['sku'] for o in offers
                                        if o.get('current_supported') and o.get('available')),
                existence='LISTING_FOUND' if listing_found else 'UNRESOLVED',
                discontinuation='UNRESOLVED')


def pate_fixture():
    clues = {name: (value, 'soft') for name, value in {
        'style': 'country-style pâté', 'jar': 'glass', 'lid': 'metal',
        'weight_g': 250, 'distributor': 'Ân Nam', 'retailer': 'Annam Gourmet',
    }.items()}
    attributes = {name: dict(value=value, source='linked fixture record')
                  for name, (value, _) in clues.items()}
    attributes['weight_g']['value'] = 180
    attributes['product_line'] = dict(value='Paté Royal', source='linked fixture record')
    return clues, attributes


def offer_fixture(sku='Paté Royal country 180 g', price=100000):
    return dict(sku=sku, retailer='X', price=price, currency='VND', unit='one 180 g jar',
                basis='normal', conditions='none', location='fixture location',
                time='fixture current observation', available=True, current_supported=True)


def selection_fixture(*, research_portion=False, hub_pipelines=(), missing=()):
    """Already-classified scope/availability; read plan only, no source resolution."""
    base = {CORE_ID}
    missing = set(missing)
    if base & missing:
        return dict(read_plan=base - missing, blocked=base, hub_pipelines=tuple(hub_pipelines))
    selected = base | ({SEARCH_ID} if research_portion else set())
    return dict(read_plan=selected - missing, blocked=selected & missing,
                hub_pipelines=tuple(hub_pipelines))


class ShoppingDecisionTests(unittest.TestCase):
    def test_A01_A02_soft_memory_vs_hard_purchase_constraint(self):
        clues, attributes = pate_fixture()
        soft = product_candidate_spec(clues, attributes, linked=True)
        self.assertEqual(soft['conflicts'], {'weight_g': (250, 180)})
        self.assertEqual(len(soft['matches']), 5)
        self.assertTrue(soft['purchase_suitable'])
        self.assertEqual(soft['identity'], 'CANDIDATE')
        self.assertEqual(soft['support'], attributes)
        clues['weight_g'] = (250, 'hard')
        hard = product_candidate_spec(clues, attributes, linked=True)
        self.assertFalse(hard['purchase_suitable'])
        self.assertEqual(hard['hard_failures'], ['weight_g'])
        self.assertEqual(hard['conflicts'], soft['conflicts'])
        self.assertEqual(hard['identity'], 'CANDIDATE')

    def test_A03_A04_matching_fields_need_identity_support(self):
        clues, attributes = pate_fixture()
        clues['weight_g'] = (180, 'soft')
        self.assertEqual(product_candidate_spec(clues, attributes, linked=True)['identity'], 'CANDIDATE')
        established = product_candidate_spec(clues, attributes, linked=True, identity_supported=True)
        self.assertEqual(established['identity'], 'ESTABLISHED')
        self.assertEqual(established['gaps_to_hub'], [])

    def test_unknown_attribute_remains_a_named_gap(self):
        clues, attributes = pate_fixture()
        del attributes['lid']
        result = product_candidate_spec(clues, attributes, linked=True)
        self.assertEqual(result['unknowns'], ['lid'])
        self.assertIn('lid', result['gaps_to_hub'])
        clues['lid'] = ('metal', 'hard')
        self.assertIsNone(product_candidate_spec(clues, attributes, linked=True)['purchase_suitable'])

    def test_B01_B02_B03_coverage_must_match_target(self):
        items = tuple(f'Paté Royal fixture variant {i}' for i in range(10))
        retailer = 'all Paté Royal listings at X under fixture conditions'
        manufacturer = 'manufacturer global catalog'
        complete = catalog_spec(items, retailer, supported_complete_target=retailer)
        unsupported = catalog_spec(items, manufacturer, supported_complete_target=retailer)
        discovered = catalog_spec(items, retailer)
        self.assertTrue(complete['complete'])
        self.assertEqual(complete['target'], retailer)
        for result in (unsupported, discovered):
            self.assertFalse(result['complete'])
            self.assertEqual(result['items'], items)
            self.assertEqual(result['gaps_to_hub'], [f"coverage of {result['target']}"])

    def test_C01_retailer_mean_retains_offer_context(self):
        offers = [offer_fixture(), offer_fixture('Paté Royal pepper 180 g', 120000)]
        result = offer_spec(offers)
        self.assertEqual(result['mean'], Decimal(110000))
        self.assertEqual(result['average_scope'], 'DEFINED_RETAILER_SKU_SET')
        self.assertEqual(result['offers'], offers)
        self.assertNotEqual(result['average_scope'], 'MARKET')

    def test_C02_sale_and_normal_prices_are_separate(self):
        normal = offer_fixture()
        sale = dict(normal, price=80000, basis='sale', conditions='members only')
        result = offer_spec([normal, sale])
        self.assertIsNone(result['mean'])
        self.assertEqual(result['offers'][1]['conditions'], 'members only')
        self.assertEqual(offer_spec([sale])['mean'], Decimal(80000))

    def test_C03_C04_stale_unavailable_and_not_found_do_not_escalate(self):
        offers = [dict(offer_fixture(), available=False),
                  dict(offer_fixture('Paté Royal pepper 180 g'), current_supported=False)]
        result = offer_spec(offers)
        self.assertEqual(result['current_available'], ())
        self.assertEqual(result['discontinuation'], 'UNRESOLVED')
        self.assertEqual(result['offers'], offers)
        absent = offer_spec([], listing_found=False)
        self.assertEqual(absent['existence'], 'UNRESOLVED')
        self.assertIsNone(absent['mean'])

    def test_C05_incompatible_or_missing_offer_context_prevents_pooling(self):
        first = offer_fixture()
        for field, value in [('currency', 'USD'), ('unit', 'two jars'), ('location', 'elsewhere'),
                             ('time', 'old observation'), ('retailer', 'Y'), ('price', None)]:
            with self.subTest(field=field):
                self.assertIsNone(offer_spec([first, dict(first, **{field: value})])['mean'])

    def test_D01_D02_D03_supplied_evidence_or_gap_to_hub_never_runs_AIS(self):
        clues = {'brand': ('Paté Royal', 'soft'), 'weight_g': (180, 'soft')}
        evidence = {'brand': dict(value='Paté Royal', source='A'),
                    'weight_g': dict(value=180, source='B')}
        # No AIS input is required. Its support/link judgments, when supplied,
        # arrive as premises through Hub; this oracle never resolves sources.
        ready = product_candidate_spec(clues, evidence, linked=True, identity_supported=True)
        self.assertEqual(ready['gaps_to_hub'], [])
        gap = product_candidate_spec(clues, evidence, linked=False, identity_supported=True)
        self.assertEqual(gap['identity'], 'CANDIDATE')
        self.assertIn('same-SKU link', gap['gaps_to_hub'])
        self.assertEqual(gap['support']['brand']['source'], 'A')
        self.assertEqual(gap['support']['weight_g']['source'], 'B')
        self.assertNotIn('selected_pipeline', gap)
        self.assertNotIn('tool_calls', gap)

    def test_D04_operation_sequence_preserves_supplied_product_state(self):
        clues, attributes = pate_fixture()
        clues['weight_g'] = (180, 'soft')
        state = dict(sku='Paté Royal country 180 g', clues=clues, attributes=attributes,
                     linked=True, identity_supported=True)
        before = copy.deepcopy(state)
        identity = product_candidate_spec(state['clues'], state['attributes'], linked=state['linked'],
                                  identity_supported=state['identity_supported'])
        other_sku = 'Paté Royal pepper 180 g'
        variants = catalog_spec([state['sku'], other_sku], 'retailer X')
        prices = offer_spec([offer_fixture(state['sku']), offer_fixture(other_sku, 120000)])
        # Comparison is scoped arithmetic on supplied offers, no state engine.
        comparison = min(prices['offers'], key=lambda o: o['price'])['sku']
        self.assertEqual(identity['identity'], 'ESTABLISHED')
        self.assertEqual(variants['items'], (state['sku'], other_sku))
        self.assertEqual(prices['offers'][0]['sku'], state['sku'])
        self.assertEqual(comparison, state['sku'])
        self.assertEqual(state, before)


class ShoppingContextRegressions(unittest.TestCase):
    def test_R1_scoped_fit_facts_do_not_supply_B_fit(self):
        # Hub's correct per-model handoff is supplied, not inferred by this test.
        models = {
            'A': {'length_mm': dict(value=140, source='A dimensions'),
                  'case_fit': dict(value=False, source='A connector collision at obstruction')},
            'B': {'length_mm': dict(value=140, source='B dimensions'),
                  'connector_layout': dict(value='different', source='B geometry')},
            'C': {'length_mm': dict(value=160, source='C dimensions'),
                  'case_fit': dict(value=True, source='C installed in same case')},
        }
        before = copy.deepcopy(models)
        results = {model: product_candidate_spec({'case_fit': (True, 'hard')}, attributes,
                                        linked=True, identity_supported=True)
                   for model, attributes in models.items()}
        self.assertFalse(results['A']['purchase_suitable'])
        self.assertIsNone(results['B']['purchase_suitable'])
        self.assertIn('case_fit', results['B']['gaps_to_hub'])
        self.assertEqual(results['B']['hard_failures'], [])
        self.assertTrue(results['C']['purchase_suitable'])
        self.assertEqual(models, before)

    def test_R2_A_qualified_seller_update_keeps_page_as_claim_not_current_stock(self):
        # AIS/Hub qualification is a premise. No universal source ranking is added.
        page = dict(offer_fixture('SKU A'), time='t1', channel='retailer page',
                    available=True, current_supported=False,
                    qualification='t2 seller confirmation invalidates current-stock reliance')
        seller = dict(page, time='t2', channel='seller chat', available=False,
                      current_supported=True, qualification='same seller/SKU/location; direct confirmation')
        result = offer_spec([page, seller])
        self.assertEqual(result['current_available'], ())
        self.assertEqual(result['offers'], [page, seller])
        self.assertTrue(result['offers'][0]['available'])  # Retained historical page claim.
        self.assertEqual(result['discontinuation'], 'UNRESOLVED')

    def test_R2_B_conflicted_length_is_not_a_resolved_fit_advantage(self):
        readings = [('source A', 'AP-850G', 150), ('source B', 'AP-850G', 190)]
        gap = 'AP-850G length conflict 150/190 mm; fit depends on length'
        returned = completion_oracle({'resolved AP-850G length'}, set(), [gap], limit_reached=True)
        self.assertFalse(returned['sufficient'])
        self.assertIn(gap, returned['unresolved'])
        # No choosing 150 mm during qualification. An unresolved length cannot
        # be passed as a supported attribute to the domain oracle.
        domain = product_candidate_spec({'fit_length_mm': (150, 'hard')}, {}, linked=True)
        self.assertIsNone(domain['purchase_suitable'])
        self.assertNotIn('fit_length_mm', domain['matches'])
        self.assertIn('fit_length_mm', domain['gaps_to_hub'])
        self.assertEqual({length for _, _, length in readings}, {150, 190})

    def test_R2_C_missing_mandatory_protection_is_not_passed_by_low_price(self):
        criteria = {'protection': (True, 'hard')}
        a = product_candidate_spec(criteria, {'price': dict(value=100, source='offer A')}, linked=True)
        b = product_candidate_spec(criteria, {'price': dict(value=120, source='offer B'),
                                     'protection': dict(value=True, source='relevant supplied lab evidence')},
                           linked=True)
        self.assertIsNone(a['purchase_suitable'])
        self.assertIn('protection', a['gaps_to_hub'])
        self.assertTrue(b['purchase_suitable'])

    def test_R2_D_surrounding_dates_do_not_fill_requested_price_window(self):
        requested = 'price in requested window 2025-07-03'
        offers = [dict(offer_fixture('SKU white', 22.9), time='2025-04-01', current_supported=False),
                  dict(offer_fixture('SKU white', 24.0), time='2025-10-01', current_supported=False)]
        coverage = completion_oracle({requested}, {'2025-04-01 observation', '2025-10-01 observation'},
                                     [requested], limit_reached=True)
        self.assertFalse(coverage['sufficient'])
        self.assertIn(requested, coverage['unresolved'])
        result = offer_spec(offers)
        self.assertIsNone(result['mean'])
        self.assertEqual(result['offers'], offers)

    def test_R3_A_delegated_mismatch_stays_conflicted_without_selecting_referent(self):
        result = product_candidate_spec({'sku': ('Corsair RM850e 2025', 'hard')},
                                {'sku': dict(value='ASUS TUF Gaming 850W', source='resolved supplied URL object')},
                                linked=False)
        self.assertEqual(result['conflicts']['sku'], ('Corsair RM850e 2025', 'ASUS TUF Gaming 850W'))
        self.assertEqual(result['identity'], 'CANDIDATE')
        # Neither field is chosen as true. Whole-turn referent interpretation is
        # Hub-owned; this only covers an explicitly delegated attribute mismatch.
        hub = CI.read_text(encoding='utf-8')
        self.assertIn('If plausible readings materially change what should be done', hub)
        self.assertIn('ask one focused question or branch', hub)

    def test_R3_B_exact_revision_not_established_by_V1_or_unknown_images(self):
        criteria = {'revision': ('V2', 'hard')}
        old = product_candidate_spec(criteria, {'revision': dict(value='V1', source='available image record')},
                             linked=True)
        unknown = product_candidate_spec(criteria, {}, linked=False)
        self.assertEqual(old['conflicts']['revision'], ('V2', 'V1'))
        self.assertFalse(old['purchase_suitable'])
        self.assertIsNone(unknown['purchase_suitable'])
        self.assertIn('revision', unknown['gaps_to_hub'])


class ShoppingContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.core = entry_path(package('SHOPPING')).read_text(encoding='utf-8')
        cls.search = (LIBRARY / 'Shopping/HUB-SHOP-SEARCH_v1.2.md').read_text(encoding='utf-8')

    def test_fixed_offer_and_search_are_pay_as_used(self):
        root = package('SHOPPING')
        self.assertIsNone(root['local_catalog'])
        self.assertFalse(root['requires'])
        self.assertNotIn(SEARCH_ID, str(root))
        self.assertIn('use this Entry alone', self.core)
        self.assertIn('no hard AIS dependency', self.core)
        self.assertEqual(selection_fixture()['read_plan'], {CORE_ID})
        self.assertEqual(selection_fixture(research_portion=True)['hub_pipelines'], ())
        scoped = selection_fixture(research_portion=True, hub_pipelines=('HUB-PKG-AIS',))
        self.assertEqual(scoped['read_plan'], {CORE_ID, SEARCH_ID})
        self.assertEqual(scoped['hub_pipelines'], ('HUB-PKG-AIS',))
        failed = selection_fixture(research_portion=True, missing={SEARCH_ID})
        self.assertEqual(failed['read_plan'], {CORE_ID})
        self.assertEqual(failed['blocked'], {SEARCH_ID})

    def test_V1_06_priority_order_changes_neither_roles_nor_hard_eligibility(self):
        conditions = {'weight_g': (250, 'soft'), 'protection': (True, 'hard')}
        evidence = {'weight_g': dict(value=180, source='identity record')}
        before = copy.deepcopy(conditions)
        for order in [('weight_g', 'protection'), ('protection', 'weight_g')]:
            ordered = {field: conditions[field] for field in order}
            result = product_candidate_spec(ordered, evidence, linked=True)
            self.assertIsNone(result['purchase_suitable'])
            self.assertEqual(result['hard_failures'], [])
            self.assertEqual(result['conflicts']['weight_g'], (250, 180))
        self.assertEqual(conditions, before)
        self.assertIn('Changing priority_order does not change HARD/SOFT roles', self.core)
        self.assertIn('preserve user-declared ties rather than inventing an order', self.core)
        self.assertIn('lower-priority HARD criterion still blocks', self.core)

    def test_V1_07_category_fields_are_suggestions_not_required_conditions(self):
        rows = re.findall(r'^\| (' + '|'.join(PROFILES) + r') \| (.+) \| (.+) \|$', self.core, re.M)
        self.assertEqual([row[0] for row in rows], list(PROFILES))
        self.assertIn('expiry', next(row for row in rows if row[0] == 'FOOD')[2])
        # Already-classified material requirement; no expiry condition was requested.
        conditions = {'packaging': ('jar', 'hard')}
        result = product_candidate_spec(conditions, {'packaging': dict(value='jar', source='supplied label')}, linked=True)
        self.assertTrue(result['purchase_suitable'])
        self.assertNotIn('expiry', result['gaps_to_hub'])
        for clause in ('PROFILE FIELD != USER REQUIREMENT', 'does not require researching every field',
                       'fields from multiple profiles', 'general Shopping path when sufficient'):
            self.assertIn(clause, self.core)

    def test_V1_08_same_seller_different_channels_remain_distinct_offers(self):
        offers = [dict(sku='variant A', seller='seller X', channel='own website', price=120, stock='in stock'),
                  dict(sku='variant A', seller='seller X', channel='marketplace store', price=100, stock='unknown')]
        observation_keys = {(o['sku'], o['seller'], o['channel']) for o in offers}
        self.assertEqual(len(observation_keys), 2)
        self.assertEqual([o['price'] for o in offers], [120, 100])
        self.assertIn('SAME SELLER != SAME OFFER', self.core)
        self.assertIn('do not deduplicate by seller or product name alone', self.core)

    def test_V1_09_conditional_price_does_not_become_unconditional_total(self):
        offers = [dict(basis='list', price=120, member_required=False, shipping=None),
                  dict(basis='sale', price=100, member_required=False, shipping=None),
                  dict(basis='sale+voucher', price=80, member_required=True,
                       eligibility=None, payment='specific card', shipping=None)]
        unconditional = [o['price'] for o in offers if not o['member_required']]
        self.assertEqual(min(unconditional), 100)
        self.assertEqual(min(o['price'] for o in offers), 80)
        self.assertTrue(all(o['shipping'] is None for o in offers))
        self.assertEqual([o['basis'] for o in offers], ['list', 'sale', 'sale+voucher'])
        self.assertIsNone(offers[2]['eligibility'])
        self.assertNotIn('effective_total', offers[2])
        for clause in ('LOWEST CONDITIONAL PRICE != LOWEST UNCONDITIONAL PRICE',
                       'Never invent shipping = 0', 'payment, shipping, bundle and warranty conditions',
                       'prevents an unconditional effective-total claim'):
            self.assertIn(clause, self.core)

    def test_V1_10_hard_unknown_does_not_qualify_cheapest_as_overall_winner(self):
        requirements = {'protection': (True, 'hard')}
        candidates = {'cheap': product_candidate_spec(requirements, {}, linked=True),
                      'verified': product_candidate_spec(requirements,
                                                 {'protection': dict(value=True, source='supplied lab')}, linked=True)}
        eligible = [name for name, value in candidates.items() if value['purchase_suitable'] is True]
        self.assertEqual(eligible, ['verified'])
        self.assertIsNone(candidates['cheap']['purchase_suitable'])
        self.assertIn('Do not force one winner', self.core)
        self.assertIn('does not prohibit every useful response', self.core)
        self.assertIn('winner dependent on an unresolved mandatory field', self.core)

    def test_V1_11_AIS_action_status_and_basis_are_preserved(self):
        for traces, expected in [([('DIRECT_EXECUTION_TRACE', 'search', 1)], 'EXECUTED'),
                                 ([('PRE_SUBMISSION_BLOCK', 'search', 1)], 'NOT_EXECUTED'),
                                 ([], 'UNKNOWN'),
                                 ([('DIRECT_EXECUTION_TRACE', 'search', 1),
                                   ('DIRECT_NON_EXECUTION_TRACE', 'search', 1)], 'CONFLICTED')]:
            # Existing AIS oracle takes (action, attempt, trace-kind).
            converted = [(action, attempt, kind) for kind, action, attempt in traces]
            status = execution_oracle(converted, retrospective='I searched')
            self.assertEqual(status, expected)
            packet = dict(actual_execution_status=status, execution_evidence_basis=converted,
                          source_reads=[], claim_support=[])
            carried = copy.deepcopy(packet)
            self.assertEqual(carried, packet)
            self.assertFalse(carried['source_reads'])
        for guard in ('PLANNED SEARCH != EXECUTED SEARCH', 'EXECUTED SEARCH != SOURCE READ',
                      'SOURCE READ != CLAIM SUPPORT', 'SOURCE READ != VALID OFFER',
                      'VALID OFFER != SHOPPING-SCOPE COMPLETION'):
            self.assertIn(guard, self.search)
        self.assertIn('Preserve each action’s AIS execution status and evidence basis', self.search)

    def test_V1_12_partial_channels_do_not_establish_market_completion(self):
        branches = {'major': 'covered', 'specialists': 'covered',
                    'small independents': 'partial', 'marketplaces': 'not executed'}
        supported = {name for name, status in branches.items() if status == 'covered'}
        result = completion_oracle(set(branches), supported, limit_reached=True)
        self.assertTrue(result['return_to_hub'])
        self.assertFalse(result['sufficient'])
        self.assertEqual(result['unresolved'], {'small independents', 'marketplaces'})
        self.assertIn('do not report the whole market searched', self.search)
        self.assertIn('not fixed tiers, named store rankings, a registry or a quota', self.search)

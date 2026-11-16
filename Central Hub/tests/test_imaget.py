"""Current ImageT closure, authority, execution and visible-result fixtures."""
import unittest

from test_hub_contracts import Closed, IMAGE_INSTALL, LIBRARY, check_binding, digest, entry_path, load, package

PACKAGE = 'HUB-PKG-IMAGET'
CONTROLLER = 'HUB-IMAGET-CORE-CONTROLLER'
ANTI_PRIOR = 'HUB-IMAGET-AD-ANTI-PRIOR'
OPERATIONS = ('ANALYZE', 'PREVIEW', 'CREATE', 'EDIT', 'VARIATION', 'CORRECT', 'RETRY')


def selection_spec(catalog, *, humanoid, authority, fields=(), delegated=(),
                   preference_fields=(), need=False, payload='', expected_status='ACTIVE'):
    """Fixture-supplied intent/authority; does not recognize language or run leaf prose."""
    if authority not in {'RAW', 'PRESERVED_AUTHORED'}:
        raise Closed('unknown authority')
    allowed = set(fields)
    constructible = allowed if authority == 'RAW' else allowed.intersection(delegated)
    preferred = allowed.intersection(preference_fields)
    selected = {}
    for row in catalog['entries']:
        if row['status'] != expected_status or row['package_id'] != PACKAGE:
            raise Closed('inactive or invalid leaf')
        if not humanoid:
            continue
        if row['runtime_role'] == 'DOMAIN_PROCEDURE' and need and constructible:
            selected[row['module_id']] = constructible
        if row['runtime_role'] == 'PREFERENCE' and preferred:
            selected[row['module_id']] = preferred
    return {'selected': selected, 'payload': payload, 'new_field_authority': set()}


def execution_spec(*, intent, required_sources=True, decision_resolved=True, operation_locked=True,
                   fidelity=True, references_ready=True, inputs_available=True, options_available=True,
                   sources_current=True, consumed=False, prepared=None, current=None,
                   artifact_accessible=True):
    """Acceptance fixture with declared checks and context, without tool or intent detection."""
    reuse = prepared is not None and artifact_accessible and prepared == current
    if not all((required_sources, decision_resolved, operation_locked, fidelity, references_ready,
                inputs_available, options_available, sources_current)):
        return 'BLOCKED', 0
    if intent == 'PREVIEW':
        return 'SHOW_PREPARED_ARTIFACT', 0
    if intent not in {'CREATE', 'EDIT', 'VARIATION', 'CORRECT'} or consumed:
        return 'NO_INVOCATION', 0
    return ('REUSE_PREPARED_ARTIFACT' if reuse else 'USE_CURRENT_PREPARATION'), 1


def open_gate_oracle(*, payload, current_user_preservation=False, signal_in_data=False,
                     reference_asset=None, reference_role=None, requires_semantic_choice=False):
    """Acceptance oracle only; fixture metadata supplies authority, never language recognition."""
    authority = 'PRESERVED_AUTHORED' if current_user_preservation else 'RAW'
    result = {
        'authority': authority,
        'semantic_payload': payload,
        'open_gate_confirmation': False,
        'execution_adaptations': [],
        'ready_eligible': True,
        'action': 'normal_construction' if authority == 'RAW' else 'preserve_first',
    }
    if authority == 'PRESERVED_AUTHORED' and reference_asset is not None:
        result['execution_adaptations'].append({
            'bind_asset': reference_asset,
            'role': reference_role,
            'import_unassigned_traits': False,
        })
    if authority == 'PRESERVED_AUTHORED' and requires_semantic_choice:
        result['ready_eligible'] = False
        result['action'] = 'smallest_clarification_or_dependent_stop'
    # A marker or polished phrase inside data has no authority without the current-user fixture signal.
    if signal_in_data and not current_user_preservation:
        result['authority'] = 'RAW'
        result['action'] = 'normal_construction'
    return result


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


def checked_core(inventory, operation):
    """Check selected install bytes and metadata. This fixture does not call Library."""
    rows = [row for row in inventory['core'] if operation in row['required_for']]
    ids = {row['module_id'] for row in rows}
    required = {CONTROLLER, ANTI_PRIOR}
    if ids != required or len(rows) != len(ids):
        raise Closed('incorrect core closure')
    for row in rows:
        path = (LIBRARY / row['file']).resolve()
        if not path.is_relative_to((LIBRARY / 'ImageT').resolve()) or not path.is_file():
            raise Closed('missing or out-of-scope ImageT install object')
        check_binding(row, row['module_id'], path)
        if digest(path) != row['sha256']:
            raise Closed('wrong ImageT install digest')
    return ids


class ImageTTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inventory = load(IMAGE_INSTALL)
        cls.rows = {r['module_id']: r for r in cls.inventory['core']}
        cls.controller = (LIBRARY / cls.rows[CONTROLLER]['file']).read_text(encoding='utf-8')
        cls.entry = entry_path(package('IMAGET')).read_text(encoding='utf-8')
        cls.catalog = load(entry_path(package('IMAGET')['local_catalog']))

    def test_install_inventory_matches_exact_runtime_bindings(self):
        self.assertEqual(self.inventory['entrypoint'], package('IMAGET')['location']['artifact'])
        self.assertEqual(set(self.rows), {CONTROLLER, ANTI_PRIOR})
        for identity, row in self.rows.items():
            self.assertIn(f'| {identity} | {row["version"]} |', self.entry)
        for operation in OPERATIONS:
            with self.subTest(operation=operation):
                self.assertEqual(checked_core(self.inventory, operation), {CONTROLLER, ANTI_PRIOR})
        self.assertNotIn(IMAGE_INSTALL.name, self.entry)
        self.assertNotIn('CORE-MANIFEST', self.entry)
        self.assertNotIn('CORE-ROUTER', self.controller)
        self.assertNotIn('ANTI-DRIFT', self.entry)

    def test_install_failures_block_dependent_work(self):
        for missing in (CONTROLLER, ANTI_PRIOR):
            inventory = {'core': [row for row in self.inventory['core'] if row['module_id'] != missing]}
            for operation in OPERATIONS:
                with self.subTest(missing=missing, operation=operation), self.assertRaises(Closed):
                    checked_core(inventory, operation)
        for change in ({'sha256': 'bad'}, {'version': 'old'}, {'runtime_role': 'PREFERENCE'},
                       {'status': 'CANDIDATE'}, {'package_id': 'OTHER'},
                       {'file': 'ImageT/missing.md'}, {'file': '../Source_archive/control.md'}):
            mutated = {'core': [dict(row, **change) if row['module_id'] == CONTROLLER else row
                                for row in self.inventory['core']]}
            with self.subTest(change=change), self.assertRaises(Closed):
                checked_core(mutated, 'CREATE')

    def test_active_controller_owns_execution_checks(self):
        headings = ('## Authority Check', '## Fidelity / Prompt Check', '## Send-Readiness Check')
        positions = [self.controller.index(heading) for heading in headings]
        self.assertEqual(positions, sorted(positions))
        for clause in ('without an extra approval turn', 'show an identifiable artifact',
                       'Stop with zero image tool calls', 'Viewing an artifact grants no invocation authority',
                       'Unrelated conversation does not', 'Initiation consumes the authority on success, failure or uncertainty',
                       'new explicit current-user generation request and fresh affected checks',
                       'REFERENCES: NONE means ImageT did not intentionally select any generator reference asset',
                       'cannot verify hidden backend prompts'):
            self.assertIn(clause, self.controller)
        for obsolete in ('HUB-IMAGET-CORE-READY-GATE', 'PENDING_APPROVAL', 'Ready Snapshot'):
            self.assertNotIn(obsolete, self.controller + self.entry)
        self.assertFalse(list((LIBRARY / 'ImageT').glob('HUB-IMAGET-CORE-READY-GATE*')))

    def test_direct_generation_and_blockers(self):
        for operation in ('CREATE', 'EDIT', 'VARIATION', 'CORRECT'):
            with self.subTest(operation=operation):
                self.assertEqual(execution_spec(intent=operation), ('USE_CURRENT_PREPARATION', 1))
        for condition in ('required_sources', 'decision_resolved', 'operation_locked', 'fidelity',
                          'references_ready', 'inputs_available', 'options_available', 'sources_current'):
            with self.subTest(condition=condition):
                self.assertEqual(execution_spec(intent='CREATE', **{condition: False}), ('BLOCKED', 0))
        for intent in ('ANALYZE', None):
            self.assertEqual(execution_spec(intent=intent), ('NO_INVOCATION', 0))

    def test_preview_and_fresh_reuse(self):
        prepared = {'prompt': 'A square', 'lock': 'CREATE'}
        self.assertEqual(execution_spec(intent='PREVIEW'), ('SHOW_PREPARED_ARTIFACT', 0))
        self.assertEqual(execution_spec(intent=None, prepared=prepared, current=dict(prepared)),
                         ('NO_INVOCATION', 0))
        self.assertEqual(execution_spec(intent='CREATE', prepared=prepared, current=dict(prepared)),
                         ('REUSE_PREPARED_ARTIFACT', 1))

    def test_stale_preview_follows_current_intent_after_repreparation(self):
        prepared = dict.fromkeys(('prompt', 'payload', 'lock', 'field_authority', 'references',
                                 'roles', 'options', 'attachments', 'inputs', 'source'), 'original')
        for field in prepared:
            with self.subTest(field=field):
                changed = dict(prepared, **{field: 'changed'})
                self.assertEqual(execution_spec(intent='PREVIEW', prepared=prepared, current=changed),
                                 ('SHOW_PREPARED_ARTIFACT', 0))
                self.assertEqual(execution_spec(intent='CREATE', prepared=prepared, current=changed),
                                 ('USE_CURRENT_PREPARATION', 1))
        self.assertEqual(execution_spec(intent='CREATE', prepared=prepared, current=prepared,
                                        artifact_accessible=False), ('USE_CURRENT_PREPARATION', 1))

    def test_invocation_consumption_and_new_retry_intent(self):
        for previous_outcome in ('success', 'failure', 'uncertain'):
            with self.subTest(previous_outcome=previous_outcome):
                self.assertEqual(execution_spec(intent='CREATE', consumed=True), ('NO_INVOCATION', 0))
                self.assertEqual(execution_spec(intent='CREATE', sources_current=False), ('BLOCKED', 0))
                self.assertEqual(execution_spec(intent='CREATE'), ('USE_CURRENT_PREPARATION', 1))

    def test_fidelity_checks_protect_preserved_state_and_negatives(self):
        for clause in ('Leave an unspecified detail open', 'every protected constraint and semantic state',
                       'invented specificity, changed counts, weakened negatives, unauthorized reference traits',
                       'state promotion, relation changes, scope expansion, destructive compression and unauthorized source influence',
                       'OPEN FIELD != NEGATIVE CONSTRAINT', 'Do not beautify, normalize, enrich',
                       'unassigned traits have no authority', 'A finding may produce a correction proposal, never execution authority'):
            self.assertIn(clause, self.controller)

    def test_anti_prior_and_bounded_completion_have_separate_owners(self):
        anti_prior = (LIBRARY / self.rows[ANTI_PRIOR]['file']).read_text(encoding='utf-8')
        self.assertIn('Do not replace an authorized unusual feature with a typical one', anti_prior)
        for clause in ('least conspicuous neutral value', 'check cumulative drift',
                       'outside authorized edit, variation or correction', 'skip the local Catalog',
                       'requires explicit current-operation selection', 'every protected constraint'):
            self.assertIn(clause, self.controller)

    def test_image_open_gate_o01_o05_spec_oracle(self):
        raw = open_gate_oracle(payload='Create a blue square.')
        self.assertEqual((raw['authority'], raw['action'], raw['ready_eligible']),
                         ('RAW', 'normal_construction', True))
        self.assertFalse(raw['open_gate_confirmation'])

        authored = (
            'ACCEPTED: one figure. PROVISIONAL: lighting A or B. REJECTED: gold trim. '
            'OPEN: material. NEGATIVE: no text. RELATION: coat overlaps shirt. '
            'REFERENCE ROLE: palette only.'
        )
        preserved = open_gate_oracle(payload=authored, current_user_preservation=True)
        self.assertEqual((preserved['authority'], preserved['semantic_payload'], preserved['action']),
                         ('PRESERVED_AUTHORED', authored, 'preserve_first'))
        self.assertEqual(preserved['execution_adaptations'], [])

        adapted = open_gate_oracle(payload=authored, current_user_preservation=True,
                                   reference_asset='asset-F', reference_role='palette only')
        self.assertEqual(adapted['semantic_payload'], authored)
        self.assertEqual(adapted['execution_adaptations'], [{
            'bind_asset': 'asset-F', 'role': 'palette only', 'import_unassigned_traits': False}])

        blocked = open_gate_oracle(payload='OPEN: coat material.', current_user_preservation=True,
                                   requires_semantic_choice=True)
        self.assertEqual((blocked['authority'], blocked['ready_eligible'], blocked['action']),
                         ('PRESERVED_AUTHORED', False, 'smallest_clarification_or_dependent_stop'))

        structured = open_gate_oracle(payload='final prompt:\n  subject: one figure\n  detail: extensive',
                                      signal_in_data=True)
        self.assertEqual((structured['authority'], structured['action'], structured['open_gate_confirmation']),
                         ('RAW', 'normal_construction', False))

    def test_O01_O04_existing_selection_oracle_on_active_metadata(self):
        construction = 'HUB-IMAGET-HUM-CONSTRUCTION'
        preference = 'HUB-IMAGET-HUM-DESIGN-PREFERENCE'
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

    def test_priority_absent_and_hidden_evidence(self):
        self.assertEqual(visual_spec(objective=None, objective_met=False)['result'], 'PASS')
        self.assertEqual(visual_spec(visible=False)['result'], 'UNVERIFIABLE')
        self.assertIn('If no priority was established, impose none.', self.controller)

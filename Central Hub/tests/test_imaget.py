"""Current ImageT closure, authority, approval and visible-result fixtures."""
from pathlib import Path
import unittest

from test_hub_contracts import Closed, IMAGE_INSTALL, LIBRARY, check_binding, digest, entry_path, load, package

PACKAGE = 'HUB-PKG-IMAGET'
CONTROLLER = 'HUB-IMAGET-CORE-CONTROLLER'
ANTI_PRIOR = 'HUB-IMAGET-AD-ANTI-PRIOR'
READY = 'HUB-IMAGET-CORE-READY-GATE'


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


def approval_oracle(state, event, same_snapshot=True):
    """Expected Ready Gate transitions only; no language interpretation/backend state."""
    if not same_snapshot or event == 'lost_context':
        return 'STALE', False
    if event in {'revision', 'yes_but'}:
        return 'REVISION_REQUIRED', False
    if event == 'approve_current' and state == 'PENDING_APPROVAL':
        return 'APPROVED', False
    if event == 'submit' and state == 'APPROVED':
        return 'CONSUMED', True
    if event == 'question':
        return state, False
    return 'PENDING_APPROVAL', False


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
    if operation in {'CREATE', 'EDIT', 'VARIATION', 'CORRECT', 'RETRY'}:
        required.add(READY)
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
        cls.ready = (LIBRARY / cls.rows[READY]['file']).read_text(encoding='utf-8')
        cls.entry = entry_path(package('IMAGET')).read_text(encoding='utf-8')
        cls.catalog = load(entry_path(package('IMAGET')['local_catalog']))

    def test_install_inventory_matches_exact_runtime_bindings(self):
        self.assertEqual(self.inventory['entrypoint'], package('IMAGET')['location']['artifact'])
        self.assertEqual(set(self.rows), {CONTROLLER, ANTI_PRIOR, READY})
        for identity, row in self.rows.items():
            self.assertIn(f'| {identity} | {row["version"]} |', self.entry)
        for operation in ('ANALYZE', 'CREATE', 'EDIT', 'VARIATION', 'CORRECT', 'RETRY'):
            with self.subTest(operation=operation):
                ids = checked_core(self.inventory, operation)
                self.assertEqual(READY in ids, operation != 'ANALYZE')
        self.assertNotIn(IMAGE_INSTALL.name, self.entry)
        self.assertNotIn('CORE-MANIFEST', self.entry)
        self.assertNotIn('CORE-ROUTER', self.controller)
        self.assertNotIn('ANTI-DRIFT', self.entry)

    def test_install_failures_do_not_allow_generation_without_gate(self):
        no_ready = {'core': [row for row in self.inventory['core'] if row['module_id'] != READY]}
        self.assertEqual(checked_core(no_ready, 'ANALYZE'), {CONTROLLER, ANTI_PRIOR})
        with self.assertRaises(Closed):
            checked_core(no_ready, 'CREATE')
        for change in ({'sha256': 'bad'}, {'version': 'old'}, {'runtime_role': 'PREFERENCE'},
                       {'file': 'ImageT/missing.md'}, {'file': '../Source_archive/control.md'}):
            mutated = {'core': [dict(row, **change) if row['module_id'] == READY else row
                                for row in self.inventory['core']]}
            with self.subTest(change=change), self.assertRaises(Closed):
                checked_core(mutated, 'CREATE')

    def test_snapshot_hold_freshness_send_and_retry(self):
        self.assertIn('hold before generation cost', self.ready)
        self.assertIn('READY SNAPSHOT vN, PENDING_APPROVAL', self.ready)
        for clause in ('exact final prompt', 'assigned roles', 'recheck the exact approved snapshot',
                       'Submission consumes approval', 'Any retry needs a fresh valid snapshot and approval',
                       'hidden payload and backend attempt count are outside ImageT observation'):
            self.assertIn(clause, self.ready)
        self.assertEqual(approval_oracle('PENDING_APPROVAL', 'submit')[1], False)
        self.assertEqual(approval_oracle('PENDING_APPROVAL', 'approve_current'), ('APPROVED', False))
        self.assertEqual(approval_oracle('APPROVED', 'submit'), ('CONSUMED', True))
        self.assertEqual(approval_oracle('CONSUMED', 'submit')[1], False)
        self.assertEqual(approval_oracle('APPROVED', 'submit', same_snapshot=False), ('STALE', False))
        for event, state in [('yes_but', 'REVISION_REQUIRED'), ('lost_context', 'STALE'),
                             ('question', 'PENDING_APPROVAL'), ('approval_for_old_version', 'PENDING_APPROVAL')]:
            with self.subTest(event=event):
                self.assertEqual(approval_oracle('PENDING_APPROVAL', event), (state, False))

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

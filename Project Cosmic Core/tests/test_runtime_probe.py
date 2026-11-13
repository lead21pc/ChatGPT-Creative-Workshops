"""Executable C2 probe cases. Semantic callbacks are fixtures, not model calls."""

import argparse
from dataclasses import replace
import json
from pathlib import Path
import sys
import unittest

from build_consolidation import ACCEPTED
from tools.check_controls import CI, FAMILIES
from tools import runtime_probe as probe

ROOT = Path(__file__).resolve().parents[1]
BOOTSTRAP = ('00_C2_CONSOLIDATION_INDEX.md', '05_OPEN_ISSUES_CURRENT.md')
RECORD = '04_RECONCILIATION_RECORD.md'
WORLD = 'C2M-110'
BRIEF = 'C2M-111'
TEAM = 'C2M-020'
CARRIAGE = 'C2M-011'
CONDITIONS = {
    'institutional_interface_material': False,
    'operational_interface_material': False,
}

# Semantic CI is bound by the experiment caller before any request. The router
# source gate and routing references are not part of the model execution prompt.
def bind_inputs():
    ci = (ROOT / CI).read_text(encoding='utf-8')
    before, _, rest = ci.partition('## Source gate\n')
    local_constraints = rest.partition('## C2 and subordinate controls\n')[2]
    local_constraints = local_constraints.partition('Router alone selects')[0]
    return *probe.local_inputs(ROOT), before + local_constraints


def proposal(modules=(WORLD,), scope=('world baseline',), operation='lookup', **changes):
    return {'operation': operation, 'scope': list(scope), 'modules': list(modules),
            'reconciliation_material': False, 'canon_change_requested': False, **changes}


def assessment(controls=(), conditions=None, **changes):
    return {'owner_sufficient': True, 'record_required': False, 'gap': None,
            'controls': list(controls), 'conditions': conditions or {}, **changes}


def scenario(name):
    if name == 'lookup':
        return ('World 1 có con người và ma thuật không?', proposal(), assessment())
    if name == 'mca':
        return ('Team 25 và Carriage 25 có phải cùng một thực thể?',
                proposal((TEAM, CARRIAGE), ('team versus carriage identity',), 'compare'),
                assessment(('MCA',)))
    if name == 'reception':
        return ('World 1 có ma thuật thì có thể kết luận Team 25 đã nhận và tin thông tin đó không?',
                proposal((WORLD, BRIEF, TEAM), ('world truth and team reception',), 'audit'),
                assessment(('ACTOR_RECEPTION',), dict(CONDITIONS), gap={
                    'issue': 'C2-OPEN-008: briefing content, receivers and timing are UNKNOWN',
                    'blocked_claim': 'Team 25 actually received or believed the information',
                    'impact': 'secondary',
                    'reason': 'The scope asks whether world truth entails receipt; it does not require deciding actual receipt.',
                }))
    if name == 'mission':
        return ('Nếu giả định một đội nhận lệnh rút, chỉ việc nhận lệnh có đủ để kết luận đội rút được khỏi World 1 không?',
                proposal((WORLD, BRIEF), ('conditional receipt and withdrawal feasibility',), 'audit'),
                assessment(('ACTOR_RECEPTION',),
                           {**CONDITIONS, 'operational_interface_material': True}, gap={
                    'issue': 'C2-OPEN-007/008: actual routes, access and mission constraints are unknown',
                    'blocked_claim': 'An actual team can withdraw or succeeds in withdrawing',
                    'impact': 'secondary',
                    'reason': 'The bounded question is whether receipt suffices under a hypothetical; actual routes are unnecessary to distinguish receipt from feasibility.',
                }))
    raise ValueError(name)


class RuntimeProbeTests(unittest.TestCase):
    def setUp(self):
        self.config, self.hashes, self.adapter, self.ci = bind_inputs()
        self.calls = []

    def execute(self, name='lookup', *, route=None, judge=None, override=None):
        request, default_route, default_decision = scenario(name)

        def retrieve(path, proof):
            self.calls.append((path, proof))
            return override(path, proof) if override else self.adapter(path, proof)

        return probe.run(request, lambda *_: default_route if route is None else route,
                         judge or (lambda *_: default_decision), self.config,
                         self.hashes, retrieve, self.ci)

    def assert_denied(self, result, expected=probe.BLOCKED):
        self.assertEqual(result['status'], expected)
        self.assertNotIn(probe.EXECUTION, result['stages'])
        self.assertIsNone(result['packet'])
        with self.assertRaises(probe.StopRoute):
            probe.complete(result, lambda _: self.fail('Blocked route called the model'))

    def test_current_lookup_retrieves_only_bootstrap_and_world(self):
        result = self.execute()
        self.assertEqual(result['stages'], self.config['runtime']['stages'][:-1])
        self.assertEqual(result['status'], probe.PASS)
        packet = result['packet']
        self.assertEqual(self.calls, [(path, probe.FULL) for path in (*BOOTSTRAP, ACCEPTED[WORLD])])
        self.assertEqual([doc['role'] for doc in packet['sources']],
                         ['routing_index', 'open_state', 'current_module'])
        self.assertEqual(packet['semantic_controls'], [])
        self.assertIn('Con người và ma thuật', packet['sources'][-1]['text'])
        self.assertIn('WORLD TRUTH != BRIEFING != ACTOR BELIEF', packet['semantic_ci'])
        self.assertFalse(packet['canon_mutation_allowed'])

    def test_semantic_selection_and_transitive_dependencies(self):
        cases = {
            'mca': {'MCA'},
            'reception': {'ACTOR_RECEPTION', 'MCA'},
            'mission': {'ACTOR_RECEPTION', 'MCA', 'OPERATIONAL_MISSION'},
        }
        for name, expected in cases.items():
            with self.subTest(name=name):
                self.calls.clear()
                result = self.execute(name)
                self.assertIsNotNone(result['packet'], result)
                overlays = result['packet']['semantic_controls']
                self.assertEqual({row['family'] for row in overlays}, expected)
                self.assertEqual({path for path, _ in self.calls if path in FAMILIES.values()},
                                 {FAMILIES[key] for key in expected})
                self.assertTrue(all(row['proof'] == probe.FULL and row['text'] for row in overlays))
        self.assertEqual(result['status'], probe.PARTIAL)
        self.assertIn('C2-OPEN-007/008', result['packet']['unresolved_gaps'][0]['issue'])

    def test_missing_material_source_or_overlay_blocks_only_that_route(self):
        for missing, name in [(BOOTSTRAP[1], 'lookup'), (ACCEPTED[WORLD], 'lookup'),
                              (FAMILIES['MCA'], 'reception')]:
            with self.subTest(missing=missing):
                def omit(path, proof):
                    return None if path == missing else self.adapter(path, proof)

                result = self.execute(name, override=omit)
                self.assert_denied(result)
                self.assertIn(missing, result['reason'])

    def test_found_is_not_full_read_and_snapshot_mismatch_blocks(self):
        for mode in ('FOUND', 'SNIPPET', probe.FULL):
            with self.subTest(mode=mode):
                def incomplete(path, proof):
                    doc = self.adapter(path, proof)
                    if path == ACCEPTED[WORLD]:
                        return replace(doc, proof=mode, body=doc.body[:150])
                    return doc

                self.assert_denied(self.execute(override=incomplete))

    def test_mixed_bootstrap_generation_blocks(self):
        def stale(path, proof):
            doc = self.adapter(path, proof)
            return replace(doc, body=doc.body + b'\nstale') if path == BOOTSTRAP[1] else doc

        self.assert_denied(self.execute(override=stale))
        self.assertEqual([path for path, _ in self.calls], list(BOOTSTRAP))

    def test_read_reconciliation_before_evaluating_conflict(self):
        calls = []

        def assess(*args):
            sources = args[3]
            calls.append([doc['role'] for doc in sources])
            return assessment(record_required=True, owner_sufficient=False)

        result = self.execute(judge=assess)
        self.assert_denied(result)
        self.assertIn('owner', result['reason'])
        self.assertNotIn('reconciliation_record', calls[0])
        self.assertEqual(calls[1][-1], 'reconciliation_record')
        self.assertEqual(self.calls[-1], (RECORD, probe.FULL))

    def test_decisive_gap_blocks_even_after_all_sources_read(self):
        self.assert_denied(self.execute(judge=lambda *_: assessment(gap={
            'issue': 'C2-OPEN-007', 'blocked_claim': 'Actual withdrawal route',
            'impact': 'decisive', 'reason': 'The conclusion depends on a route not recorded.',
        })))

    def test_unresolved_control_condition_cannot_be_silently_false(self):
        result = self.execute('reception', judge=lambda *_: assessment(
            ('ACTOR_RECEPTION',), {'institutional_interface_material': False}))
        self.assert_denied(result, probe.REVIEW)
        self.assertFalse(any(path in FAMILIES.values() for path, _ in self.calls))

    def test_model_cannot_declare_execution_reads_or_mutation(self):
        for changes in ({'execution_state': probe.EXECUTION}, {'status': probe.PASS},
                        {'proof': probe.FULL}, {'canon_change_requested': True}):
            with self.subTest(changes=changes):
                self.assert_denied(self.execute(route=proposal(**changes)), probe.REVIEW)
        self.assertEqual(self.calls, [])

    def test_archive_and_history_cannot_substitute_current(self):
        for path in ('Source_Archive/110_WORLD_001_CURRENT.md',
                     '03_DESIGN_HISTORY_AND_RECONSIDERATIONS.md'):
            with self.subTest(path=path):
                self.assert_denied(self.execute(route=proposal(modules=(path,))), probe.REVIEW)
                self.assertNotIn((path, probe.FULL), self.calls)

                def wrong_identity(name, proof):
                    doc = self.adapter(name, proof)
                    return replace(doc, path=path) if name == ACCEPTED[WORLD] else doc

                self.assert_denied(self.execute(override=wrong_identity))

    def test_invalid_current_module_identity_requires_review(self):
        path = ACCEPTED[WORLD]
        original = self.adapter(path, probe.FULL)
        wrong = replace(original, body=original.body.replace(b'C2M-110', b'C2M-111', 1))
        self.hashes[path] = probe.sha256(wrong.body).hexdigest().upper()
        result = self.execute(override=lambda name, proof: wrong if name == path
                              else self.adapter(name, proof))
        self.assert_denied(result, probe.REVIEW)
        self.assertIn('mismatched Module ID', result['reason'])

    def test_response_envelope_preserves_gate_result_and_blocks_unknown_citations(self):
        result = self.execute('reception')
        scope = result['packet']['authorized_scope']
        draft = {'answer': 'Sự thật của world không xác lập việc Team 25 nhận hoặc tin.',
                 'addressed_scope': scope, 'source_refs': [ACCEPTED[WORLD], ACCEPTED[BRIEF]]}
        checked = probe.complete(result, lambda _: draft)
        self.assertEqual(checked['execution_state'], probe.RESPONSE)
        self.assertEqual(checked['status'], probe.PARTIAL)
        self.assertEqual(checked['blocked_claims'], result['packet']['blocked_claims'])
        for bad in ({'source_refs': [RECORD]}, {'addressed_scope': ['unrelated']},
                    {'canon_mutation_allowed': True}):
            with self.assertRaises(probe.StopRoute):
                probe.check_response(result, {**draft, **bad})


def compare_contexts(name):
    """Export two inspectable context representations, without calling a model."""
    config, hashes, retrieve, ci = bind_inputs()
    request, route, decision = scenario(name)
    result = probe.run(request, lambda *_: route, lambda *_: decision,
                       config, hashes, retrieve, ci)
    packet = result['packet']
    if packet is None:
        raise RuntimeError(result['reason'])
    shared = {'request': request, 'semantic_ci': ci, 'sources': packet['sources'],
              'semantic_controls': packet['semantic_controls']}
    raw = {**shared, 'answer_boundary': packet['answer_boundary'],
           'route_proposal': route, 'semantic_assessment': decision,
           'implementation': Path(probe.__file__).read_text(encoding='utf-8'),
           'router_config': config, 'admitted_modules': ACCEPTED, 'current_file_hashes': hashes}
    return {'raw': raw, 'packet': packet}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=compare_contexts.__doc__)
    parser.add_argument('scenario', choices=['lookup', 'mca', 'reception', 'mission'])
    parser.add_argument('representation', choices=['raw', 'packet'])
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    print(json.dumps(compare_contexts(args.scenario)[args.representation],
                     ensure_ascii=False, indent=2))

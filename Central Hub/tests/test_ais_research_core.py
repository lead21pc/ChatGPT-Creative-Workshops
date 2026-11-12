"""Current AIS source guards and research SPEC fixtures, without model or tool calls."""
import copy
import unittest

from test_hub_contracts import HUB_ROUTER, ROOT, load, package
from test_concept_development import leaf_span_spec

PIPELINE = ROOT / 'tool_pipelines/AIS/AIS_PIPELINE_v1.3.md'


def execution_oracle(traces=(), action='search', attempt=1, retrospective=None):
    """Expected classification of declared direct traces, not trace discovery.

    retrospective is deliberately insufficient to establish either execution state.
    All supplied direct traces in a fixture share target/time/surface.
    """
    kinds = {kind for a, n, kind in traces if (a, n) == (action, attempt)}
    executed = 'DIRECT_EXECUTION_TRACE' in kinds
    not_executed = bool(kinds & {'DIRECT_NON_EXECUTION_TRACE', 'PRE_SUBMISSION_BLOCK', 'UNAVAILABLE_EXECUTOR'})
    if executed and not_executed:
        return 'CONFLICTED'
    if executed:
        return 'EXECUTED'
    return 'NOT_EXECUTED' if not_executed else 'UNKNOWN'


def depth_oracle(explicit_depth=False, broad=False, multiple_material_claims=False):
    """Declared semantic depth fixture only; no language parser or product selection."""
    return 'EXTENSIVE' if broad else 'THOROUGH' if explicit_depth or multiple_material_claims else 'NORMAL'


def completion_oracle(required, supported, decisive_gaps=(), limit_reached=False):
    """Expected bounded evidence coverage, never an actual model/search executor."""
    missing = set(required) - set(supported)
    gaps = missing | set(decisive_gaps)
    return dict(return_to_hub=not gaps or limit_reached,
                supported=set(supported), unresolved=gaps,
                sufficient=not gaps)


def supported_claim(decisive_reads=(), supporting_reads=(), label=None):
    """A verified label cannot create the missing decisive read/support relation."""
    return 'SUPPORTED' if set(decisive_reads).intersection(supporting_reads) else 'UNRESOLVED'


def fallback_oracle(branches):
    """Retain supported branches; only unresolved/invalidated branches need work."""
    retained = {k: copy.deepcopy(v) for k, v in branches.items()
                if v['supported'] and not v.get('invalidated')}
    return retained, set(branches) - set(retained)


def fresh_completion(*, refresh=True, prior_support=True, current_trace=(),
                     current_support=False, action='read'):
    """Declared per-invocation evidence, not a runtime freshness detector."""
    execution = execution_oracle(current_trace, action=action)
    coverage = completion_oracle({'target'}, {'target'} if current_support else set())
    if not refresh:
        return 'REUSED' if prior_support else 'UNRESOLVED'
    return 'COMPLETE' if execution == 'EXECUTED' and coverage['sufficient'] else 'INCOMPLETE'


class AISResearchSpecFixtures(unittest.TestCase):
    def test_RC01_direct_trace_outranks_retrospective_denial(self):
        self.assertEqual(execution_oracle([('search', 1, 'DIRECT_EXECUTION_TRACE')],
                                         retrospective='NOT_EXECUTED'), 'EXECUTED')

    def test_RC02_missing_trace_is_unknown(self):
        for report in ['EXECUTED', 'NOT_EXECUTED', None]:
            self.assertEqual(execution_oracle(retrospective=report), 'UNKNOWN')

    def test_RC03_execution_read_and_support_are_distinct(self):
        trace = [('search', 1, 'DIRECT_EXECUTION_TRACE')]
        self.assertEqual(execution_oracle(trace), 'EXECUTED')
        self.assertEqual(execution_oracle(trace, action='read'), 'UNKNOWN')
        self.assertEqual(supported_claim(), 'UNRESOLVED')
        self.assertEqual(supported_claim(['A'], ['B']), 'UNRESOLVED')
        self.assertEqual(supported_claim(['A'], ['A']), 'SUPPORTED')

    def test_RC04_normal_guided_research_loop(self):
        self.assertEqual(depth_oracle(), 'NORMAL')
        self.assertIn('normal path uses available authorized Chat search/read', PIPELINE.read_text(encoding="utf-8"))
        self.assertIn('identify the next unresolved evidence need', PIPELINE.read_text(encoding="utf-8"))

    def test_RC05_thorough_uses_normal_chat_search_read(self):
        self.assertEqual(depth_oracle(explicit_depth=True), 'THOROUGH')
        self.assertIn('Ordinary Chat search/read can support THOROUGH or EXTENSIVE', PIPELINE.read_text(encoding="utf-8"))
        self.assertIn('source comparison and corroboration/counterevidence', PIPELINE.read_text(encoding="utf-8"))

    def test_RC06_extensive_uses_normal_chat_search_read(self):
        self.assertEqual(depth_oracle(broad=True), 'EXTENSIVE')
        self.assertIn('EXTENSIVE covers materially broad', PIPELINE.read_text(encoding="utf-8"))
        self.assertIn('repeated guided search/read', PIPELINE.read_text(encoding="utf-8"))

    def test_RC07_semantic_depth_influences_evidence_not_answer_length(self):
        # Semantic intent is supplied as a fixture, never interpreted by a string matcher.
        self.assertEqual(depth_oracle(explicit_depth=True), 'THOROUGH')
        self.assertEqual(depth_oracle(multiple_material_claims=True), 'THOROUGH')
        self.assertIn('Recognize semantic requests in any language', PIPELINE.read_text(encoding="utf-8"))
        self.assertIn('not merely answer length', PIPELINE.read_text(encoding="utf-8"))

    def test_RC08_broad_research_does_not_launch_deep_research(self):
        self.assertEqual(depth_oracle(explicit_depth=True, broad=True), 'EXTENSIVE')
        self.assertIn('does not automatically select, launch or transfer', PIPELINE.read_text(encoding="utf-8"))
        self.assertIn('Deep Research or Work', PIPELINE.read_text(encoding="utf-8"))

    def test_RC09_multistep_work_does_not_launch_work(self):
        self.assertIn('Broad research and multi-step tasks do not trigger automatic product selection', PIPELINE.read_text(encoding="utf-8"))

    def test_RC10_sufficient_evidence_returns_to_hub(self):
        result = completion_oracle({'A', 'B'}, {'A', 'B'})
        self.assertTrue(result['sufficient'])
        self.assertTrue(result['return_to_hub'])
        self.assertFalse(result['unresolved'])
        self.assertIn('Stop when the evidence is sufficient', PIPELINE.read_text(encoding="utf-8"))

    def test_RC11_limit_with_gaps_returns_honest_partial_output(self):
        result = completion_oracle({'A', 'B'}, {'A'}, limit_reached=True)
        self.assertTrue(result['return_to_hub'])
        self.assertFalse(result['sufficient'])
        self.assertEqual(result['unresolved'], {'B'})
        self.assertIn('Exhausting a limit does not prove sufficiency', PIPELINE.read_text(encoding="utf-8"))

    def test_RC12_decisive_gaps_do_not_erase_supported_independent_work(self):
        result = completion_oracle({'A'}, {'A'}, decisive_gaps={'B'}, limit_reached=True)
        self.assertEqual(result['supported'], {'A'})
        self.assertEqual(result['unresolved'], {'B'})
        self.assertIn('material gaps block dependent conclusions only', PIPELINE.read_text(encoding="utf-8"))

    def test_RC13_unavailable_tool_is_not_fabricated_execution(self):
        self.assertEqual(execution_oracle([('search', 1, 'UNAVAILABLE_EXECUTOR')]), 'NOT_EXECUTED')
        self.assertIn('actual tool availability/access and authorization', PIPELINE.read_text(encoding="utf-8"))
        self.assertIn('no invented search/read', PIPELINE.read_text(encoding="utf-8"))

    def test_RC14_post_submission_timeout_does_not_prove_nonexecution(self):
        self.assertEqual(execution_oracle([('search', 1, 'SUBMITTED'), ('search', 1, 'TIMEOUT')]), 'UNKNOWN')
        self.assertIn('a timeout after submission proves no non-execution or success', PIPELINE.read_text(encoding="utf-8"))

    def test_RC15_conflicting_direct_traces_remain_conflicted_per_attempt(self):
        trace = [('search', 1, 'DIRECT_EXECUTION_TRACE'), ('search', 1, 'PRE_SUBMISSION_BLOCK')]
        self.assertEqual(execution_oracle(trace), 'CONFLICTED')
        trace[1] = ('search', 2, 'PRE_SUBMISSION_BLOCK')
        self.assertEqual(execution_oracle(trace), 'EXECUTED')
        self.assertEqual(execution_oracle(trace, attempt=2), 'NOT_EXECUTED')

    def test_RC16_nonexecution_requires_positive_evidence(self):
        for kind in ['DIRECT_NON_EXECUTION_TRACE', 'PRE_SUBMISSION_BLOCK', 'UNAVAILABLE_EXECUTOR']:
            self.assertEqual(execution_oracle([('search', 1, kind)]), 'NOT_EXECUTED')

    def test_RC17_explicit_product_requests_do_not_grant_imaginary_launches(self):
        self.assertEqual(execution_oracle([('search', 1, 'REQUESTED')]), 'UNKNOWN')
        self.assertIn('actually available authorized platform surface', PIPELINE.read_text(encoding="utf-8"))
        self.assertIn('do not silently substitute products', PIPELINE.read_text(encoding="utf-8"))
        self.assertIn('without corresponding direct evidence', PIPELINE.read_text(encoding="utf-8"))

    def test_RC18_entitlement_or_forum_is_not_observed_tool_capability(self):
        self.assertIn('subscription entitlement or community report', PIPELINE.read_text(encoding="utf-8"))
        self.assertIn('actual tool availability/access', PIPELINE.read_text(encoding="utf-8"))

    def test_RC19_tool_failure_preserves_evidence_conditions_and_replans_only_gaps(self):
        branches = {'A': dict(supported=True, reads=['A'], conditions='region/time/version'),
                    'B': dict(supported=True, reads=['B'], invalidated=True),
                    'C': dict(supported=False, reads=['C'])}
        before = copy.deepcopy(branches)
        retained, unresolved = fallback_oracle(branches)
        self.assertEqual(retained, {'A': before['A']})
        self.assertEqual(unresolved, {'B', 'C'})
        self.assertEqual(branches, before)
        self.assertIn('re-plan only unresolved/invalidated evidence needs', PIPELINE.read_text(encoding="utf-8"))
        self.assertIn('Keep the quality target and evidence standard', PIPELINE.read_text(encoding="utf-8"))

    def test_RC20_query_refinement_retains_scope(self):
        self.assertIn('Query refinement for the same target is allowed', PIPELINE.read_text(encoding="utf-8"))
        self.assertIn('same-target query refinement retains scope', PIPELINE.read_text(encoding="utf-8"))

    def test_RC21_material_scope_change_rebuilds_affected_contract(self):
        self.assertIn('Material scope changes rebuild affected contract/strategy fields', PIPELINE.read_text(encoding="utf-8"))
        self.assertIn('Rerouting does not authorize new work', PIPELINE.read_text(encoding="utf-8"))

    def test_RC22_components_do_not_automatically_support_combination(self):
        self.assertIn('Support for A and B separately does not establish A+B', PIPELINE.read_text(encoding="utf-8"))
        self.assertIn('require evidence for their relationship', PIPELINE.read_text(encoding="utf-8"))

    def test_RC23_protected_state_cannot_be_silently_rewritten(self):
        self.assertIn('Merge factual state only within allowed_to_update', PIPELINE.read_text(encoding="utf-8"))
        self.assertIn('do not silently change it', PIPELINE.read_text(encoding="utf-8"))

    def test_RC24_verified_label_without_decisive_read_stays_unresolved(self):
        for label in ['Work verified', 'Deep Research verified', 'previously verified']:
            self.assertEqual(supported_claim(label=label), 'UNRESOLVED')
        for action in ['search', 'open', 'find']:
            self.assertEqual(execution_oracle([(action, 1, 'DIRECT_EXECUTION_TRACE')], action=action), 'EXECUTED')
        self.assertIn('verified labels do not substitute for readable decisive sources', PIPELINE.read_text(encoding="utf-8"))

    def test_RC25_hub_retains_activation_and_original_workflow(self):
        self.assertIn('without reassessing the whole turn', PIPELINE.read_text(encoding="utf-8"))
        self.assertIn('Hub resumes the original work', PIPELINE.read_text(encoding="utf-8"))
        self.assertIn('do not alter general claim state or activate AIS independently', PIPELINE.read_text(encoding="utf-8"))

    def test_RC26_only_material_unresolved_needs_continue_within_limit(self):
        result = completion_oracle({'A', 'B'}, {'A'})
        self.assertFalse(result['return_to_hub'])
        self.assertEqual(result['unresolved'], {'B'})
        self.assertIn('continue only while a material gap remains within stop_condition', PIPELINE.read_text(encoding="utf-8"))


class AISContractTests(unittest.TestCase):
    def test_single_source_keeps_research_and_execution_semantics(self):
        self.assertEqual(package('AIS')['location']['source_name'], PIPELINE.name)
        body = PIPELINE.read_text(encoding='utf-8')
        for clause in ('VERIFY', 'RESEARCH', 'EXPLORE', 'SEARCH_SCOPE_LOCK', 'source_authority',
                       'coverage_expectations', 'Before each search/read call', 'decisive source',
                       'Support for A and B separately does not establish A+B',
                       'per-action execution status', 'timeout after submission',
                       're-plan only unresolved/invalidated evidence needs', 'new relevant external execution',
                       'explicitly requests reuse/no refresh', 'does not automatically select, launch'):
            self.assertIn(clause, body)
        self.assertIn('/SEARCH', package('AIS')['applicability'])
        self.assertIn('/SEARCH <instruction> #', body)
        self.assertNotIn('AIS_ROUTER', body)

    def test_freshness_is_separate_from_prior_support(self):
        self.assertEqual(fresh_completion(prior_support=True), 'INCOMPLETE')
        trace = [('read', 1, 'DIRECT_EXECUTION_TRACE')]
        self.assertEqual(fresh_completion(current_trace=trace), 'INCOMPLETE')
        self.assertEqual(fresh_completion(prior_support=False, current_trace=trace, current_support=True), 'COMPLETE')
        self.assertEqual(fresh_completion(refresh=False, prior_support=True), 'REUSED')

    def test_R4_results_offers_retailers_and_queries_keep_their_units(self):
        queries = [f'query {i}' for i in range(12)]
        unique = [(f'offer {i}', f'retailer {i % 27}') for i in range(65)]
        inspected = unique + unique[:31]
        observed = {'results_inspected': len(inspected),
                    'unique_offers': len({offer for offer, _ in inspected}),
                    'unique_retailers': len({retailer for _, retailer in inspected}),
                    'queries_issued': len(queries)}
        self.assertEqual(observed, {'results_inspected': 96, 'unique_offers': 65,
                                    'unique_retailers': 27, 'queries_issued': 12})
        self.assertEqual(len(inspected) - observed['unique_offers'], 31)
        self.assertNotEqual(observed['queries_issued'], observed['results_inspected'])
        # Typed tuples keep a query count from satisfying result coverage;
        # approximate-result tolerance remains with the actual locked question.
        coverage = completion_oracle({('results inspected', 96)}, {('queries issued', 12)},
                                     limit_reached=True)
        self.assertFalse(coverage['sufficient'])
        self.assertIn(('results inspected', 96), coverage['unresolved'])

    def test_unrecovered_historical_trace_stays_unknown(self):
        self.assertEqual(execution_oracle(retrospective='about 100 searches were performed'), 'UNKNOWN')


class SearchDirectiveTests(unittest.TestCase):
    def spec(self, text, role='USER_DIRECTIVE'):
        return leaf_span_spec([(role, text)])

    def test_T03_aliases_boundaries_empty_unclosed(self):
        for text in ['/search X #', '/Search X #', 'SEARCH X #', '/SEARCHX X #',
                     'x/SEARCH X #', '(/SEARCH X #', '/SEARCH #', '/SEARCH X',
                     '/SEARCH X #suffix', '/SEARCH X#']:
            with self.subTest(text=text):
                self.assertEqual(self.spec(text)['invocations'], [])

    def test_T04_provenance_and_T08_no_persistence(self):
        for role in ['QUOTE', 'SOURCE', 'CODE', 'TOOL', 'ASSISTANT', 'PRIOR_TURN', 'DOCUMENTATION']:
            self.assertEqual(self.spec('/SEARCH X #', role)['invocations'], [])
        mixed = leaf_span_spec([('USER_DIRECTIVE', '/SEARCH '), ('QUOTE', '#'),
                                ('USER_DIRECTIVE', ' X #')])
        self.assertEqual(len(mixed['invocations']), 1)
        self.assertEqual(self.spec('/SEARCH X #')['invocations'][0][0], 'HUB-PKG-AIS')
        self.assertEqual(self.spec('giải thích kết quả vừa rồi')['invocations'], [])

    def test_cross_owner_malformed_groups_and_independent_spans(self):
        for text in ('/CREATIVE A /SEARCH B #', '/SEARCH A /BRAINSTORM B #'):
            with self.subTest(text=text):
                result = self.spec(text)
                self.assertFalse(result['invocations'])
                self.assertTrue(result['blocked'])
        result = self.spec('/CREATIVE A # /SEARCH B #')
        self.assertEqual([scope for _, scope in result['invocations']], ['A', 'B'])
        composition = load(HUB_ROUTER)['stages']['COMPOSITION_VALIDATION']
        self.assertIn('closing terminator', composition)
        self.assertIn('have no operator meaning', composition)

"""Current Concept span and package selection fixtures with declared source roles."""
import copy
import re
import unittest

from test_hub_contracts import LIBRARY, ROOT_CATALOG, load
from test_hub_router import synthetic_module, synthetic_fixture, simulate

PACKAGE = 'HUB-PKG-CONCEPT-DEVELOPMENT'
CORE = 'HUB-CON-ENTRY'
CATALOG = 'HUB-CON-CATALOG'
DIRECTORY = LIBRARY / 'Concept Development'
LOCAL = DIRECTORY / 'HUB-CON-CATALOG_v1.7.yaml'
ENTRY = DIRECTORY / 'HUB-CON-ENTRY_v1.8.md'


def current_fixture():
    """Project interfaces into the SPEC oracle; specialized scopes declare already-valid explicit invocations, not semantic auto-selection."""
    core = synthetic_module(CORE, PACKAGE, {'CORE', 'CREATIVE', 'DEBATE', 'BRAINSTORM', 'NAME'}, version='1.8')
    fixture = synthetic_fixture(core)
    catalog = synthetic_module(CATALOG, PACKAGE, set(), role='PACKAGE_CATALOG', version='1.7')
    fixture['packages'][0]['local_catalog'] = catalog
    fixture['artifacts'][CATALOG] = [dict(copy.deepcopy(catalog), read_kind='FULL_FILE')]
    local = load(LOCAL)
    leaves = []
    scopes = {'HUB-CON-GEN-CREATIVE': {'CREATIVE'}, 'HUB-CON-GEN-BRAINSTORM': {'BRAINSTORM'}, 'HUB-CON-GEN-DEBATE': {'DEBATE'}, 'HUB-CON-GEN-NAMING': {'NAME'}}
    for row in local['entries']:
        leaf = synthetic_module(row['module_id'], row['package_id'], scopes.get(row['module_id'], set()),
                                role=row['runtime_role'], version=row['version'],
                                status=row['status'], requires=copy.deepcopy(row['requires']),
                                location=copy.deepcopy(row['location']))
        leaves.append(leaf)
        fixture['artifacts'][leaf['module_id']] = [dict(copy.deepcopy(leaf), read_kind='FULL_FILE')]
    fixture['local_catalogs'][PACKAGE] = leaves
    return fixture


def naming_modifier_spec(content, directive=None):
    """Test-only modifier oracle over fixture-labeled roles; no runtime parser."""
    if not content.strip():
        return None
    directive = [True] * len(content) if directive is None else directive
    tokens = list(re.finditer(r'\S+', content))
    first = tokens[0]
    is_control = lambda m: all(directive[m.start():m.end()])
    preset_like = lambda m: is_control(m) and re.fullmatch(r'[Pp][0-9]+', m.group())
    if not preset_like(first):
        return (None, content.strip())
    if first.group() not in {'P1', 'P2', 'P3'} or len(tokens) == 1:
        return None
    if preset_like(tokens[1]):
        return None
    return (first.group(), content[first.end():].strip())


def leaf_span_spec(parts):
    """Test-only lexical acceptance oracle, NOT a deployed parser or provenance detector.

    Fixtures label directive/source/quote/code roles. Real platform role detection and
    model compliance require live evidence. Offsets preserve the original context.
    """
    text = ''.join(body for role, body in parts)
    directive = [role == 'USER_DIRECTIVE' for role, body in parts for _ in body]
    local = load(LOCAL)
    openers = {row['activation']: row['module_id'] for row in local['entries'] if 'activation' in row}
    # Foreign owner cue only: SEARCH remains AIS-owned, never a Concept catalog leaf.
    openers['/SEARCH'] = 'HUB-PKG-AIS'
    tokens = re.compile(r'(?<![\w/])/(?:CREATIVE|DEBATE|BRAINSTORM|NAME)(?=\s|$)|(?<!\S)/SEARCH(?=\s|$)|(?<!\S)#(?=\s|$)')
    invocations, blocked, occupied = [], [], []
    opened = None
    invalid = False
    for match in tokens.finditer(text):
        if not all(directive[match.start():match.end()]):
            continue
        token = match.group()
        if token in openers:
            if opened is None:
                opened = match
            else:
                invalid = True  # Never implicitly close/switch at a second opener.
        elif opened is not None:
            content = text[opened.end():match.start()]
            span = (opened.start(), match.end())
            occupied.append(span)
            if (invalid or not content.strip() or
                    (opened.group() == '/NAME' and naming_modifier_spec(
                        content, directive[opened.end():match.start()]) is None)):
                blocked.append(span)
            else:
                invocations.append((openers[opened.group()], content.strip()))
            opened, invalid = None, False
    if opened is not None:
        blocked.append((opened.start(), len(text)))
        occupied.append((opened.start(), len(text)))
    unscoped, start = [], 0
    for left, right in occupied:
        unscoped.append(text[start:left])
        start = right
    unscoped.append(text[start:])
    return dict(invocations=invocations, blocked=blocked, unscoped=unscoped, context=text)


class ExplicitLeafControlTests(unittest.TestCase):
    def spec(self, text):
        return leaf_span_spec([('USER_DIRECTIVE', text)])

    def test_three_canonical_controls_and_exact_content(self):
        for opener, identity, content in [('/CREATIVE', 'HUB-CON-GEN-CREATIVE', 'make X.'),
                                          ('/DEBATE', 'HUB-CON-GEN-DEBATE', 'challenge X.'),
                                          ('/BRAINSTORM', 'HUB-CON-GEN-BRAINSTORM', 'reverse assumption X.')]:
            with self.subTest(opener=opener):
                result = self.spec(f'{opener} {content} #')
                self.assertEqual(result['invocations'], [(identity, content)])
                self.assertEqual(result['blocked'], [])
                # Feed explicit selections into existing closure/read/failure oracle.
                scopes = {opener[1:]}
                routed = simulate(current_fixture(), scopes)
                self.assertEqual({module for _, module in routed['planned']}, {identity})
                self.assertFalse(routed['runtime_ready'])

    def test_mid_sentence_multiline_and_context_visibility(self):
        result = self.spec('Constraints A, B. I want /CREATIVE design X\nusing A and B. # but preserve Y.')
        self.assertEqual(result['unscoped'], ['Constraints A, B. I want ', ' but preserve Y.'])
        self.assertEqual(result['invocations'], [('HUB-CON-GEN-CREATIVE', 'design X\nusing A and B.')])
        self.assertIn('Constraints A, B.', result['context'])  # Available context != delegated scope.
        self.assertNotIn('preserve Y', result['invocations'][0][1])

    def test_ordered_three_leaves_and_repeated_leaf(self):
        result = self.spec('/CREATIVE design drainage. # Then /DEBATE challenge that design. # '
                           'After that /BRAINSTORM reverse the fixed-network assumption. #')
        self.assertEqual(result['invocations'], [('HUB-CON-GEN-CREATIVE', 'design drainage.'),
                         ('HUB-CON-GEN-DEBATE', 'challenge that design.'),
                         ('HUB-CON-GEN-BRAINSTORM', 'reverse the fixed-network assumption.')])
        result = self.spec('/CREATIVE mechanism A. # ordinary text /CREATIVE mechanism B. #')
        self.assertEqual(result['invocations'], [('HUB-CON-GEN-CREATIVE', 'mechanism A.'),
                                                ('HUB-CON-GEN-CREATIVE', 'mechanism B.')])
        self.assertIn(' ordinary text ', result['unscoped'])

    def test_semantic_fit_and_old_phrases_never_activate(self):
        for text in ['be creative', 'make this more creative', 'brainstorm this', 'thử động não',
                     'brainstorm sâu', 'động não thử cái này', 'argue against this', 'criticize this',
                     'challenge this proposal', 'compare these options', 'audit this',
                     'reverse assumptions and trace second-order consequences']:
            with self.subTest(text=text):
                self.assertEqual(self.spec(text)['invocations'], [])
        self.assertEqual(simulate(current_fixture(), {'CORE'})['planned'], [])

    def test_unclosed_empty_overlapping_and_recovery(self):
        for text in ['/CREATIVE design X', '/CREATIVE design X.\nNext paragraph.',
                     '/CREATIVE design X /DEBATE attack X #', '/DEBATE #']:
            with self.subTest(text=text):
                result = self.spec(text)
                self.assertEqual(result['invocations'], [])
                self.assertEqual(len(result['blocked']), 1)
        result = self.spec('core work /CREATIVE X /DEBATE Y # independent /BRAINSTORM Z #')
        self.assertEqual(result['invocations'], [('HUB-CON-GEN-BRAINSTORM', 'Z')])
        self.assertEqual(len(result['blocked']), 1)
        self.assertIn('core work ', result['unscoped'])

    def test_exact_tokens_stray_hash_and_turn_non_persistence(self):
        for text in ['#', '#heading', '## section', '/creative X #', '/CREATIVELY X #',
                     '/BRAINSTORMING X #', 'path/DEBATE X #', '/DEBATE,X #']:
            self.assertEqual(self.spec(text)['invocations'], [], text)
        self.assertEqual(len(self.spec('/DEBATE X #')['invocations']), 1)
        self.assertEqual(self.spec('ordinary next turn')['invocations'], [])
        result = self.spec('/CREATIVE use #heading and ## section\nthen finish. # unscoped')
        self.assertEqual(result['invocations'][0][1], 'use #heading and ## section\nthen finish.')

    def test_provenance_and_literal_hash_roles_are_fixture_supplied(self):
        for role in ['ASSISTANT', 'PRIOR_TURN', 'TOOL', 'SOURCE', 'ATTACHMENT', 'QUOTE', 'CODE', 'ANALYZED_PROMPT']:
            self.assertEqual(leaf_span_spec([(role, '/DEBATE X #')])['invocations'], [], role)
        result = leaf_span_spec([('USER_DIRECTIVE', '/CREATIVE use '), ('QUOTE', '"#"'),
                                 ('CODE', ' # /DEBATE literal # '),
                                 ('USER_DIRECTIVE', ' without ending early. # outside')])
        self.assertEqual(result['invocations'], [('HUB-CON-GEN-CREATIVE',
                         'use "#" # /DEBATE literal #  without ending early.')])
        self.assertEqual(result['unscoped'][-1], ' outside')


class CurrentConceptContracts(unittest.TestCase):
    def test_core_only_and_missing_leaf_or_catalog_isolation(self):
        baseline = current_fixture()
        self.assertEqual(simulate(baseline, {'CORE'})['spec_reads'], [CORE, CATALOG])
        self.assertEqual(simulate(baseline, set())['artifact_requests'], [])
        for missing in (CATALOG, 'HUB-CON-GEN-CREATIVE'):
            fixture = copy.deepcopy(baseline)
            del fixture['artifacts'][missing]
            result = simulate(fixture, {'CREATIVE'})
            self.assertTrue(result['blocked'])
            self.assertFalse(result['pipeline_entrypoints'])

    def test_scope_and_same_premise_development(self):
        body = ENTRY.read_text(encoding='utf-8')
        for clause in ('Use the consequences of the existing premise', 'TEXTUAL ORDER != AUTOMATIC DEPENDENCY',
                       'LEAF SCOPE != CONTEXT VISIBILITY', 'clarification', 'opens nor closes operation spans'):
            self.assertIn(clause, body)
        local = load(LOCAL)
        self.assertEqual({row['activation'] for row in local['entries'] if 'activation' in row},
                         {'/CREATIVE', '/DEBATE', '/BRAINSTORM', '/NAME'})
        root = load(ROOT_CATALOG)
        self.assertNotIn('HUB-CON-GEN-CREATIVE', str(root))

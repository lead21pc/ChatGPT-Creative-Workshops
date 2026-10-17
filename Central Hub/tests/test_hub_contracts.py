"""Static checks and test-only inventory/approval oracles; never model/tool execution."""
import copy
import hashlib
import json
from pathlib import Path
import re
import unittest
from unittest.mock import patch
import yaml

ROOT = Path(__file__).resolve().parents[1]
IMAGE = ROOT / 'tool_pipelines/ImageT'


class Closed(ValueError):
    pass


class StrictLoader(yaml.SafeLoader):
    def construct_mapping(self, node, deep=False):
        result = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if key == '<<' or key in result:
                raise Closed('duplicate or merge key')
            result[key] = self.construct_object(value_node, deep=deep)
        return result


def parse(text):
    for event in yaml.parse(text):
        if isinstance(event, yaml.AliasEvent) or getattr(event, 'anchor', None):
            raise Closed('anchor/alias')
    for token in yaml.scan(text):
        if isinstance(token, yaml.TagToken):
            raise Closed('explicit tag')
        if isinstance(token, yaml.ScalarToken) and token.plain:
            if token.value.lower() in {'yes', 'no', 'on', 'off', 'false', 'true', 'null', '~'}:
                if token.value not in {'true', 'false', 'null'}:
                    raise Closed('ambiguous scalar')
            if re.match(r'^\d{4}-\d{2}-\d{2}', token.value):
                raise Closed('implicit date')
    return yaml.load(text, Loader=StrictLoader)


def load(path):
    return parse(path.read_text(encoding='utf-8'))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_source(entry):
    path = (IMAGE / entry['local_path']).resolve()
    if not path.is_relative_to(IMAGE) or any(p.lower() == 'source_archive' for p in path.parts):
        raise Closed('outside active sources')
    try:
        actual_digest = digest(path) if path.is_file() else None
    except OSError as error:
        raise Closed(f'unreadable source: {entry["file"]}') from error
    if path.name != entry['file'] or actual_digest != entry['sha256']:
        raise Closed('missing/nonexact/corrupt source')
    if path.suffix == '.md':
        text = path.read_text(encoding='utf-8')
        versions = re.findall(r'^(?:IMAGE_CONTROLLER|READY_GATE|ANTI_PRIOR|CONFIG|PREFERENCE)_VERSION: (.+)$', text, re.M)
        if versions != [entry['version']] or f"STATUS: {entry['status'].upper()}" not in text:
            raise Closed('header mismatch')
    return path


def image_oracle(manifest, router, operation='create', selection=None, unexpected_template=False):
    """Acceptance oracle only; does not run the instructional router or ChatGPT."""
    if manifest['format_version'] != router['manifest_contract']['format_version']:
        raise Closed('manifest contract mismatch')
    if operation not in router['operations']:
        raise Closed('unknown operation')
    active = manifest['controllers']['active']
    if selection not in {None, active['id']}:
        raise Closed('no selectable experiment in this release')
    if active['status'] != 'active':
        raise Closed('inactive controller')
    verify_source(active)
    generation = operation in {'create', 'edit', 'variation', 'correct'}
    if generation:
        if 'ready_gate' not in active['compatibility'] or 'ready_gate' not in manifest['artifacts']:
            raise Closed('missing Ready Gate dependency')
        if operation not in router['generation_dependencies']['operations']:
            raise Closed('generation route bypass')
        if router['execution']['ready_gate'] != 'manifest_selected_ready_gate_contract':
            raise Closed('missing Ready Gate delegation')
    for role, version in active['compatibility'].items():
        if role == 'ready_gate' and not generation:
            continue
        entry = manifest['artifacts'][role]
        if entry['version'] != version or entry['status'] != 'active' or not entry['required']:
            raise Closed('incompatible module')
        verify_source(entry)
    if manifest['artifacts']['router']['version'] != router['router_version']:
        raise Closed('router inventory mismatch')
    template = manifest['artifacts']['visual_template']
    if template['status'] == 'optional_absent':
        if template['file'] is not None or template['required'] or unexpected_template:
            raise Closed('inconsistent template inventory')
    elif template['status'] == 'active':
        verify_source(template)
    else:
        raise Closed('invalid template status')
    return {'selected': active['id'], 'after_prompt_gate': 'analyze_only' if operation == 'analyze' else 'PENDING_APPROVAL',
            'preference_active': False, 'tool_called': False}


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


class HubTests(unittest.TestCase):
    def setUp(self):
        self.manifest = load(IMAGE / 'manifest.yaml')
        self.router = load(IMAGE / 'IMAGE_SOURCE_ROUTER.yaml')

    def test_yaml_conservative_and_rejects_bad_inputs(self):
        for p in ROOT.rglob('*.yaml'):
            if 'Source_archive' not in p.parts:
                self.assertIsInstance(load(p), dict)
        for text in ['a: 1\na: 2', 'a: &x 1\nb: *x', '<<: {}', 'a: yes', 'a: FALSE', 'a: ~', 'a: 2026-10-17', 'a: !custom x']:
            with self.assertRaises((Closed, yaml.YAMLError)):
                parse(text)

    def test_hub_topology_and_routes(self):
        router = load(ROOT / 'HUB_ROUTER_v1.0.yaml')
        self.assertEqual(router['default'], ['NONE'] * 3)
        self.assertEqual(router['axes']['DOMAIN'], ['NONE', 'CREATIVE', 'TECHNICAL'])
        self.assertEqual(router['axes']['CAPABILITY'], ['NONE', 'BRAINSTORM'])
        self.assertEqual(router['axes']['TOOL_PIPELINE'], ['NONE', 'AIS', 'IMAGET'])
        self.assertEqual(set(router['controls']), {'CREATIVE', 'TECHNICAL', 'BRAINSTORM', 'AIS', 'IMAGET'})
        for name in router['controls'].values():
            self.assertTrue((ROOT / name).is_file())
            self.assertNotIn('archive', name.lower())
        self.assertFalse(router['persistence']['listing_activates'])
        self.assertFalse(router['persistence']['applicability_activates'])
        self.assertFalse((ROOT / 'manifest.yaml').exists())
        self.assertEqual(list(ROOT.glob('*CI*.md')), [ROOT / 'HUB_CI_v1.0.md'])
        self.assertFalse(any(p.name.startswith('DEFAULT') for p in ROOT.rglob('*')))

    def test_normalized_runtime_instruction_language(self):
        # Local guard for Vietnamese instruction prose, not a general language detector.
        # Inspect instruction values/body text, not paths, identifiers or quoted user text.
        vietnamese = re.compile(r'[ăđơưạảấầẩẫậắằẳẵặẹẻẽếềểễệỉĩịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹ]', re.I)
        for sample in ['Select specialization / chọn specialization.', 'Chỉ chặn phần phụ thuộc.']:
            self.assertRegex(sample, vietnamese)
        self.assertNotRegex('Preserve René — exact names and punctuation are valid.', vietnamese)

        def instruction_values(value):
            if isinstance(value, dict):
                for item in value.values(): yield from instruction_values(item)
            elif isinstance(value, list):
                for item in value: yield from instruction_values(item)
            elif isinstance(value, str) and ' ' in value:
                yield value

        for name in ['HUB_ROUTER_v1.0.yaml', 'tool_pipelines/AIS/AIS_ROUTER_v1.1.yaml',
                     'tool_pipelines/ImageT/IMAGE_SOURCE_ROUTER.yaml']:
            for prose in instruction_values(load(ROOT / name)):
                self.assertNotRegex(prose, vietnamese, name)
        for name in ['domains/creative/CREATIVE_v1.0.md', 'domains/technical/TECHNICAL_v1.0.md',
                     'tool_pipelines/AIS/AIS_PIPELINE_v1.0.md']:
            text = (ROOT / name).read_text(encoding='utf-8')
            prose = re.sub(r'`[^`]*`|"[^"]*"', '', text)
            self.assertNotRegex(prose, vietnamese, name)

    def test_normalized_router_scope_failure_and_continuation(self):
        router = load(ROOT / 'HUB_ROUTER_v1.0.yaml')
        self.assertEqual(router['controls'], {
            'CREATIVE': 'domains/creative/CREATIVE_v1.0.md',
            'TECHNICAL': 'domains/technical/TECHNICAL_v1.0.md',
            'BRAINSTORM': 'capabilities/BRAINSTORM_v1.0.md',
            'AIS': 'tool_pipelines/AIS/AIS_PIPELINE_v1.0.md',
            'IMAGET': 'tool_pipelines/ImageT/IMAGE_CONTROLLER_v1.1.md',
        })
        self.assertTrue(router['scoping']['independent_axes'])
        self.assertFalse(router['persistence']['self_activation'])
        self.assertEqual(router['failure']['forbidden_fallbacks'],
                         ['archive', 'memory', 'prior_chat', 'lookalike_filename', 'latest_version_discovery'])
        anchors = {
            router['role']: ['Select only scoped specialization', 'do not select Hub CI or conversation operations'],
            router['scoping']['independent_portions']: ['independently for each task portion', 'separate selections', 'not hybrid names'],
            router['scoping']['handoff']: ['Hub-assigned stage', 'protected state', 'Only attributes with assigned roles'],
            router['boundaries']['internal_dependencies']: ['HUB SELECTS PIPELINE', 'PIPELINE RESOLVES INTERNAL DEPENDENCIES'],
            router['persistence']['reassess']: ['each turn', 'when scope changes', 'not modes', 'PREVIOUS ACTIVATION != CURRENT ACTIVATION'],
            router['failure']['selected_control']: ['Read the exact selected control', 'missing/unreadable',
                'name the dependency', 'block the dependent task portion', 'decisive or explicitly requested',
                'baseline only where sufficient', 'without claiming equivalence', 'Continue independent portions'],
        }
        for prose, required in anchors.items():
            for phrase in required: self.assertIn(phrase, prose)
        # Existing Hub contract still forbids invented application of unavailable controls.
        ci = (ROOT / 'HUB_CI_v1.0.md').read_text(encoding='utf-8')
        self.assertIn('Read selected controls; missing decisive/explicit controls block dependent work', ci)
        self.assertIn('VIETNAMESE throughout', ci)

    def test_ci_budget_and_owner_order(self):
        text = (ROOT / 'HUB_CI_v1.0.md').read_text(encoding='utf-8')
        self.assertLess(len(text) + text.count('\n'), 8000)
        owners = ['OUTPUT CONTRACT', 'CONTROL GROUNDING', 'DISCOURSE FIDELITY', 'EPISTEMIC NON-ESCALATION',
                  'TURN AND STATE', 'CLAIM STATE AND DEPENDENCY', 'UPDATING AND UNCERTAINTY', 'EXPLANATION']
        indices = [text.index(s) for s in owners]
        self.assertEqual(indices, sorted(indices))
        for s in ['ACKNOWLEDGING FEELINGS != CONFIRMING EVENT INTERPRETATIONS', 'EMPATHY != DIAGNOSIS',
                  'LISTENING != INFERRING MOTIVES', 'HUB_ROUTER_v1.0.yaml', 'Clear fiction needs no repeated disclaimer']:
            self.assertIn(s, text)

    def test_ais_three_modes_lock_and_gate_order(self):
        ais = load(ROOT / 'tool_pipelines/AIS/AIS_ROUTER_v1.1.yaml')
        self.assertEqual(set(ais['modes']), {'VERIFY', 'RESEARCH', 'EXPLORE'})
        self.assertEqual(set(ais['search_contract']) - {'lifetime'},
                         {'operation', 'mode', 'question', 'known', 'unknowns', 'source_authority', 'update_scope', 'stop_condition'})
        seq = ais['stage_sequence']
        self.assertEqual(seq, list(ais['stages']))
        self.assertLess(seq.index('TOOL_FACING_INSTRUCTION'), seq.index('PRE_CALL_CHECK'))
        self.assertLess(seq.index('PRE_CALL_CHECK'), seq.index('RESEARCH_EXECUTION'))
        self.assertLess(seq.index('EVIDENCE_MERGE'), seq.index('COVERAGE_SUPPORT_CHECK'))
        self.assertTrue({'injection', 'memory', 'conflict', 'consequential', 'read_support', 'freshness'} <= set(ais['source_policy']))

    def test_image_active_ready_and_analyze(self):
        self.assertEqual(image_oracle(self.manifest, self.router)['after_prompt_gate'], 'PENDING_APPROVAL')
        self.assertEqual(image_oracle(self.manifest, self.router, operation='analyze')['after_prompt_gate'], 'analyze_only')
        self.assertNotIn('ci', self.manifest)
        self.assertNotIn('ci_location', self.router['resolution'])
        self.assertEqual(self.router['resolution']['controller_location'], 'project_sources')
        self.assertEqual(self.router['load_order'][0], 'selected_controller')
        text = (IMAGE / 'IMAGE_CONTROLLER_v1.1.md').read_text(encoding='utf-8')
        self.assertLess(text.index('## Prompt and execution gate'), text.index('## Ready Gate delegation'))
        self.assertLess(text.index('## Ready Gate delegation'), text.index('## Verify and respond'))
        for state in ['PENDING_APPROVAL', 'APPROVED', 'REVISION_REQUIRED', 'STALE']:
            self.assertNotIn(state, text)
        self.assertIn('No image-generation call may occur unless that control authorizes the exact current execution snapshot', text)
        ready = (IMAGE / 'READY_GATE_v1.0.md').read_text(encoding='utf-8')
        for s in ['one call', 'exact displayed prompt', 'REVISION_REQUIRED', 'STALE', 'CONSUMED', 'UNVERIFIABLE']:
            self.assertIn(s, ready)

    def test_image_inventory_hashes_headers_and_inactive_preference(self):
        entries = [self.manifest['controllers']['active'], *self.manifest['artifacts'].values(), *self.manifest['preferences']]
        self.assertEqual(len({e['id'] for e in entries}), len(entries))
        for entry in entries:
            if entry['file'] is not None:
                verify_source(entry)
        pref = self.manifest['preferences'][0]
        self.assertEqual(pref['activation'], 'inactive')
        self.assertFalse(pref['selectable'])
        self.assertFalse(image_oracle(self.manifest, self.router)['preference_active'])
        self.assertFalse(self.manifest['release']['published'])
        self.assertEqual(self.manifest['release']['project_deployment'], 'not_performed')

    def test_image_mutations_fail_closed(self):
        for field, value in [('local_path', 'missing.md'), ('sha256', '0' * 64), ('status', 'candidate')]:
            m = copy.deepcopy(self.manifest)
            m['controllers']['active'][field] = value
            with self.assertRaises(Closed): image_oracle(m, self.router)
        for role in ['router', 'prior_guard', 'anti_drift']:
            for field, value in [('version', 'wrong'), ('sha256', '0' * 64), ('local_path', 'missing.md'),
                                 ('local_path', '../../Source_archive/IMAGE_ANTI_PRIOR.md')]:
                m = copy.deepcopy(self.manifest)
                m['artifacts'][role][field] = value
                with self.assertRaises(Closed): image_oracle(m, self.router)
        with self.assertRaises(Closed): image_oracle(self.manifest, self.router, selection='ready-gate')
        with self.assertRaises(Closed): image_oracle(self.manifest, self.router, unexpected_template=True)
        m = copy.deepcopy(self.manifest)
        m['artifacts']['visual_template'].update(status='active', file='template.md', local_path='template.md', sha256='0' * 64)
        with self.assertRaises(Closed): image_oracle(m, self.router)

    def test_ready_gate_one_call_and_invalidations(self):
        for event in ['no', 'ambiguous', 'approve_old']:
            self.assertEqual(approval_oracle('PENDING_APPROVAL', event), ('PENDING_APPROVAL', False))
        self.assertEqual(approval_oracle('PENDING_APPROVAL', 'question'), ('PENDING_APPROVAL', False))
        self.assertEqual(approval_oracle('PENDING_APPROVAL', 'approve_current'), ('APPROVED', False))
        self.assertEqual(approval_oracle('APPROVED', 'submit'), ('CONSUMED', True))
        self.assertEqual(approval_oracle('CONSUMED', 'submit'), ('PENDING_APPROVAL', False))
        self.assertEqual(approval_oracle('APPROVED', 'yes_but'), ('REVISION_REQUIRED', False))
        self.assertEqual(approval_oracle('APPROVED', 'submit', same_snapshot=False), ('STALE', False))
        self.assertEqual(approval_oracle('PENDING_APPROVAL', 'lost_context'), ('STALE', False))

    def test_ready_gate_required_regression_spec(self):
        path = IMAGE / 'tests/READY_GATE_TEST_CASES.md'
        self.assertTrue(path.is_file())
        text = path.read_text(encoding='utf-8')
        for anchor in [
            'STATUS: REQUIRED_REGRESSION_SPEC',
            'ROLE: NON_RUNTIME_NORMATIVE_ORACLE',
            'TARGET: READY_GATE 1.0',
            'READY_GATE_RUNTIME_STATUS: ACTIVE',
            'ORIGINAL_IMAGET_LIVE_VALIDATION: CONFIRMED_BY_USER',
            'CENTRAL_HUB_LIVE_VALIDATION: NOT_RUN',
            'FRESH_CONVERSATIONS: R03-R08',
            'MULTI_TURN_CASES: R09-R19',
            'All no-approval branches require zero image tool calls.',
            'Every approved submission must use the exact approved prompt version',
            'exact approved references, options and relevant execution inputs',
            'exactly one tool call, without a second confirmation',
            'Revisions invalidate previous approval and preserve unaffected constraints.',
            'Changed request, prompt, sources, references, options, operation lock or relevant execution inputs invalidate approval',
            'Report uncertain submission; never silently retry.',
            'Unobservable backend payload must be marked UNVERIFIABLE.',
            'A displayed prompt is not proof of backend payload.',
        ]:
            self.assertIn(anchor, text)
        ids = re.findall(r'^\| (R\d{2}) \|', text, re.M)
        self.assertEqual(ids, [f'R{i:02}' for i in range(1, 23)])

    def test_ready_gate_inventory_resolution_and_all_generation_paths(self):
        gate = self.manifest['artifacts']['ready_gate']
        self.assertEqual(gate['file'], 'READY_GATE_v1.0.md')
        self.assertEqual(gate['version'], '1.0')
        self.assertEqual(gate['status'], 'active')
        self.assertTrue(gate['required'])
        self.assertEqual(self.manifest['controllers']['active']['compatibility']['ready_gate'], gate['version'])
        self.assertEqual(list(IMAGE.glob('READY_GATE_v*.md')), [IMAGE / gate['file']])
        self.assertEqual(list(IMAGE.glob('IMAGE_CONTROLLER_v*.md')),
                         [IMAGE / self.manifest['controllers']['active']['file']])
        self.assertNotIn('ready_gate', self.manifest['release'])
        self.assertEqual(self.router['generation_dependencies']['ready_gate']['inventory'], 'manifest.artifacts.ready_gate')
        self.assertEqual(self.router['generation_dependencies']['ready_gate']['compatibility'], 'selected_controller.compatibility.ready_gate')
        self.assertEqual(self.router['generation_dependencies']['retry'], 'each_generation_call')
        sequence = self.router['generation_sequence']
        self.assertLess(sequence.index('prompt_gate'), sequence.index('active_ready_gate'))
        self.assertLess(sequence.index('active_ready_gate'), sequence.index('tool_execution'))
        for operation in ['create', 'edit', 'variation', 'correct']:
            result = image_oracle(self.manifest, self.router, operation=operation)
            self.assertEqual(result['after_prompt_gate'], 'PENDING_APPROVAL')
            self.assertFalse(result['tool_called'])
            for field, value in [('local_path', 'missing.md'), ('version', 'wrong'), ('sha256', '0' * 64),
                                 ('status', 'candidate'), ('required', False),
                                 ('local_path', '../../Source_archive/READY_GATE_v1.0.md')]:
                m = copy.deepcopy(self.manifest)
                m['artifacts']['ready_gate'][field] = value
                with self.assertRaises(Closed): image_oracle(m, self.router, operation=operation)
        for missing in ['entry', 'compatibility']:
            m = copy.deepcopy(self.manifest)
            if missing == 'entry': del m['artifacts']['ready_gate']
            else: del m['controllers']['active']['compatibility']['ready_gate']
            with self.assertRaises(Closed): image_oracle(m, self.router)
        m = copy.deepcopy(self.manifest)
        del m['artifacts']['ready_gate']
        self.assertEqual(image_oracle(m, self.router, operation='analyze')['after_prompt_gate'], 'analyze_only')
        self.assertIn('embedded_controller', self.router['generation_dependencies']['ready_gate']['forbidden_fallbacks'])
        self.assertTrue({'tool_facing_prompt', 'reference_roles', 'attachments', 'relevant_execution_inputs'} <= set(self.router['freshness']['changes']))
        original_read = Path.read_bytes
        def unreadable_ready(path):
            if path == IMAGE / gate['file']:
                raise PermissionError('fixture: unreadable Ready Gate')
            return original_read(path)
        with patch.object(Path, 'read_bytes', unreadable_ready):
            with self.assertRaisesRegex(Closed, 'unreadable source: READY_GATE_v1.0.md'):
                image_oracle(self.manifest, self.router)

    def test_official_snapshot_and_stress_boundaries(self):
        gate = (IMAGE / 'READY_GATE_v1.0.md').read_text(encoding='utf-8')
        for anchor in ['READY SNAPSHOT vN, STATE: PENDING_APPROVAL', 'exact reference assets and reference roles',
                       'exact tool options', 'operation-lock identity and protected constraints',
                       'authorized interpretations/completions', 'intentionally open fields',
                       'explicit exclusions/negatives', 'effective source versions/hash verification status',
                       'REFERENCES: NONE', 'Do not promise to choose references after approval',
                       'ONE APPROVAL = ONE EXACT TOOL CALL', 'CONSUMED',
                       'Approval of an older version makes no call', 'An unobservable backend payload is UNVERIFIABLE']:
            self.assertIn(anchor, gate)
        controller = (IMAGE / 'IMAGE_CONTROLLER_v1.1.md').read_text(encoding='utf-8')
        for anchor in ['AIS EVIDENCE SOURCE != IMAGE GENERATOR REFERENCE ASSET',
                       'UNSPECIFIED != FORBIDDEN', 'OMITTED != PROHIBITED', 'OPEN FIELD != NEGATIVE CONSTRAINT',
                       'explicit user prohibition', 'logical requirement of an explicit constraint',
                       'authorized active source', 'Remove unauthorized negatives or keep the field open']:
            self.assertIn(anchor, controller)
        ais = load(ROOT / 'tool_pipelines/AIS/AIS_ROUTER_v1.1.yaml')
        self.assertIn('SUPPORTED COMPONENTS DO NOT AUTOMATICALLY SUPPORT THEIR COMBINATION', ais['stages']['EVIDENCE_MERGE'])
        self.assertIn('unless the relation between A and B is itself supported', ais['stages']['EVIDENCE_MERGE'])
        spec = (IMAGE / 'tests/READY_GATE_TEST_CASES.md').read_text(encoding='utf-8')
        for anchor in ['## X01', 'AIS -> BRAINSTORM -> TECHNICAL -> CREATIVE -> IMAGET -> READY GATE',
                       'The open horse field stays open/omitted', 'READY SNAPSHOT v1, STATE: PENDING_APPROVAL',
                       'Zero image tool calls occur before approval', 'All references are resolved before approval']:
            self.assertIn(anchor, spec)

    def test_preserved_image_semantics(self):
        expected = {'IMAGE_ANTI_PRIOR.md': 'f08a1d1a09c8b31cd3fe6ed80b38b19f2c662e15f7e192b42c8a5e044aa69b5c',
                    'config.md': '20b08b3b99b237eebeec0442024e0818245d0b0bebc2fb756e972aca67d4d3d7'}
        for name, value in expected.items(): self.assertEqual(digest(IMAGE / name), value)
        ready = (IMAGE / 'READY_GATE_v1.0.md').read_text(encoding='utf-8')
        protocol = ready.split('## Preserved approval protocol', 1)[1].split('## Exact submission and invalidation', 1)[0]
        self.assertEqual(hashlib.sha256(protocol.encode()).hexdigest(), READY_GATE_SHA)


    def test_migrated_specialist_semantic_bodies(self):
        brain = (ROOT / 'capabilities/BRAINSTORM_v1.0.md').read_text(encoding='utf-8').split('## Branching by premise change', 1)[1]
        self.assertEqual(hashlib.sha256(brain.encode()).hexdigest(), 'd9efaca29971bfdf1716c323a679f81715d5cac7b9d00abe791c5dd044db67fa')
        controller = (IMAGE / 'IMAGE_CONTROLLER_v1.1.md').read_text(encoding='utf-8')
        body = controller.split('## Authority and conflict', 1)[1].split('## Ready Gate delegation', 1)[0]
        paragraphs = body.split('\n\n')
        additions = [p for p in paragraphs if p.startswith(('AIS EVIDENCE SOURCE', 'UNSPECIFIED != FORBIDDEN'))]
        self.assertEqual(len(additions), 2)
        body = '\n\n'.join(p for p in paragraphs if p not in additions)
        self.assertEqual(hashlib.sha256(body.encode()).hexdigest(), 'abc1639ca566420f0e127539b57a43881bce1eca01a0da640fa62770133d7ca9')
        ais = load(ROOT / 'tool_pipelines/AIS/AIS_ROUTER_v1.1.yaml')
        policy = json.dumps(ais['source_policy'], sort_keys=True)
        self.assertEqual(hashlib.sha256(policy.encode()).hexdigest(), '3f22b8abf89e2cb7bfffed3c9255da3e034ad672d64a5394641e4a1f0f0975e7')

    def test_utf8_active_sources_and_no_retired_references(self):
        for path in ROOT.rglob('*'):
            if not path.is_file() or 'Source_archive' in path.parts or path.suffix not in {'.md', '.yaml'}:
                continue
            data = path.read_bytes()
            text = data.decode('utf-8')
            self.assertFalse(data.startswith(b'\xef\xbb\xbf'))
            if path.name not in {'MIGRATION_REPORT.md', 'README.md'}:
                self.assertNotIn('AIS_SOURCE_ROUTER_v0.1.yaml', text)
                self.assertNotIn('ImageT_v1.0.0.md', text)
            if path.suffix == '.yaml':
                self.assertNotIn('Source_archive/', text)

    def test_archive_receipt_when_present(self):
        receipt = ROOT / 'Source_archive/ARCHIVE_RECEIPT.json'
        if not receipt.exists():
            self.skipTest('pre-archive verification phase')
        rows = json.loads(receipt.read_text(encoding='utf-8'))
        for row in rows:
            self.assertEqual(digest(ROOT / row['archive']), row['sha256'])
            self.assertFalse((ROOT.parent / row['old']).exists())
        archives = [p for p in ROOT.rglob('*') if p.is_dir() and p.name.lower() == 'source_archive']
        self.assertEqual(archives, [ROOT / 'Source_archive'])


# Original embedded protocol hash retained as provenance; checked against the extracted preserved protocol.
READY_GATE_SHA = 'c1360811a98e27b6ddabbf008d9b82ffd54610b0bf5a8948c8f37092340fd322'

if __name__ == '__main__':
    unittest.main()

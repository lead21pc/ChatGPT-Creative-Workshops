"""Opt-in C2 control-flow experiment. Run with a trusted host adapter and semantic callbacks."""

from copy import deepcopy
from dataclasses import dataclass
from hashlib import sha256

from build_consolidation import (ACCEPTED, CURRENT_FILES, HASHES, MANIFEST, ValidationError,
                                 header, read_root, region, rows)
from tools.check_controls import ControlError, controls_by_id, load, local_file, resolve

FULL = 'FULL_FILE'
BLOCKED = 'SOURCE_LOAD_BLOCKED'
REVIEW = 'REVIEW_REQUIRED'
PARTIAL = 'SOURCE_LOAD_PARTIAL'
PASS = 'PASS'
EXECUTION = 'PROMPT_EXECUTION'
RESPONSE = 'PRE_RESPONSE_CHECK'
OPERATIONS = {'lookup', 'compare', 'audit', 'design', 'simulate'}


@dataclass(frozen=True)
class Read:
    path: str
    proof: str
    body: bytes


def local_inputs(root):
    """Read maintenance metadata once. Lore/overlay retrieval stays task-local."""
    config = load(root)
    _, _, _, block = region(read_root(root, MANIFEST), HASHES)
    hashes = rows(block, '| File | SHA-256 |', CURRENT_FILES)

    def retrieve(path, proof):
        if proof != FULL:
            return None
        try:
            # A successful read_bytes reads to EOF from the requested local file.
            return Read(path, FULL, local_file(root, path).read_bytes())
        except (ControlError, OSError):
            return None

    return config, hashes, retrieve


def text(value):
    return isinstance(value, str) and bool(value.strip())


def list_of_strings(value):
    return (isinstance(value, list) and all(text(item) for item in value)
            and len(set(value)) == len(value))


def fields(value, keys):
    return isinstance(value, dict) and value.keys() == keys


class StopRoute(ValueError):
    def __init__(self, status, reason):
        super().__init__(reason)
        self.status = status


def gate(condition, reason, status=REVIEW):
    if not condition:
        raise StopRoute(status, reason)


def run(request, propose, assess, config, hashes, retrieve, semantic_ci):
    """Run one read-only turn. Callbacks propose semantics; only this core grants execution."""
    controls = controls_by_id(config)
    bootstrap = config['bootstrap']
    record = bootstrap['reconciliation_record']
    stage = ['PROMPT_ROUTE_ONLY']
    sources = []
    overlays = []

    def read(path, role, module=None):
        result = retrieve(path, FULL)
        gate(isinstance(result, Read) and result.path == path and result.proof == FULL
             and isinstance(result.body, bytes) and bool(result.body.strip()),
             f'{path}: required FULL_FILE proof unavailable', BLOCKED)
        digest = sha256(result.body).hexdigest().upper()
        if role != 'semantic_control':
            gate(digest == hashes.get(path), f'{path}: outside the pinned current snapshot', BLOCKED)
        try:
            body = result.body.decode('utf-8-sig')
            metadata = header(result.body, path) if module else None
        except (UnicodeError, ValidationError) as error:
            raise StopRoute(REVIEW, f'{path}: invalid identity or content ({error})') from error
        if module:
            gate(metadata['Module ID'] == module, f'{path}: mismatched Module ID')
        return {'path': path, 'proof': FULL, 'sha256': digest, 'role': role,
                'header': metadata, 'text': body}

    def source_state():
        # Callback gets independent copies, including headers; it cannot register reads.
        return [{**doc, 'header': dict(doc['header']) if doc['header'] else None}
                for doc in sources]

    try:
        gate(text(request) and text(semantic_ci), 'Request and prebound semantic CI required')
        route = propose(request, dict(ACCEPTED), tuple(controls))
        gate(fields(route, {'operation', 'scope', 'modules', 'reconciliation_material',
                            'canon_change_requested'}), 'Invalid route fields')
        gate(text(route['operation']) and route['operation'] in OPERATIONS
             and list_of_strings(route['scope']) and bool(route['scope'])
             and list_of_strings(route['modules']) and bool(route['modules'])
             and type(route['reconciliation_material']) is bool
             and type(route['canon_change_requested']) is bool, 'Invalid route values')
        gate(not route['canon_change_requested'], 'This experiment only handles read-only turns')
        operation, scope, modules = route['operation'], tuple(route['scope']), tuple(route['modules'])

        stage.append('BOOTSTRAP_GATE')
        for path, role in zip(bootstrap['full_file'], ('routing_index', 'open_state'), strict=True):
            sources.append(read(path, role))

        stage.append('MODULE_GATE')
        gate(set(modules) <= ACCEPTED.keys(), 'Unknown or unadmitted module')
        stage.append('SOURCE_LOAD')
        for module in modules:
            sources.append(read(ACCEPTED[module], 'current_module', module))

        stage.append('RECONCILIATION')
        if route['reconciliation_material']:
            sources.append(read(record, 'reconciliation_record'))

        def assess_loaded():
            result = assess(request, operation, scope, source_state(),
                            {key: row['select_when'] for key, row in controls.items()},
                            tuple(dict.fromkeys(edge['when'] for row in controls.values()
                                                for edge in row['conditional_requires'])))
            gate(fields(result, {'record_required', 'owner_sufficient', 'gap', 'controls',
                                 'conditions'})
                 and type(result['record_required']) is bool
                 and type(result['owner_sufficient']) is bool, 'Invalid semantic assessment')
            return result

        decision = assess_loaded()
        if decision['record_required'] and sources[-1]['role'] != 'reconciliation_record':
            sources.append(read(record, 'reconciliation_record'))
            decision = assess_loaded()
        gap = decision['gap']
        if gap is not None:
            gate(fields(gap, {'issue', 'blocked_claim', 'impact', 'reason'})
                 and all(text(value) for value in gap.values())
                 and gap['impact'] in {'decisive', 'secondary'}, 'Invalid unresolved gap')
        gate(decision['owner_sufficient'], 'Controlling owner unresolved', BLOCKED)
        if gap and gap['impact'] == 'decisive':
            raise StopRoute(BLOCKED, gap['issue'])

        stage.append('ANTI_DRIFT_OVERLAY_GATE')
        selected, conditions = decision['controls'], decision['conditions']
        known = {edge['when'] for row in controls.values() for edge in row['conditional_requires']}
        gate(list_of_strings(selected) and set(selected) <= controls.keys()
             and isinstance(conditions, dict) and conditions.keys() <= known
             and all(value is None or type(value) is bool for value in conditions.values()),
             'Invalid overlay selection or conditions')
        closure = resolve(config, selected, {key for key, value in conditions.items() if value is True})
        needed = {edge['when'] for key in closure for edge in controls[key]['conditional_requires']}
        gate(all(conditions.get(key) is not None for key in needed),
             'Material overlay condition needs a semantic decision')
        for key in sorted(closure):
            doc = read(controls[key]['path'], 'semantic_control')
            heading, _, identity, family, *_ = doc['text'].split('\n', 4) + [''] * 4
            heading, identity, family = (line.rstrip('\r') for line in (heading, identity, family))
            gate(heading.startswith('# C2 — ') and heading.endswith(' v1.0')
                 and identity == '> Status: ACTIVE' and family == f'> Family: {key}',
                 f'{key}: wrong overlay identity/version/status', BLOCKED)
            overlays.append({**doc, 'family': key})

        stage.append(EXECUTION)
        packet = {
            'request': request, 'operation': operation, 'authorized_scope': list(scope),
            'execution_state': EXECUTION, 'status': PARTIAL if gap else PASS,
            'canon_mutation_allowed': False, 'coverage': 'task_local',
            'sources': source_state(), 'semantic_controls': overlays,
            'unresolved_gaps': [dict(gap)] if gap else [],
            'blocked_claims': [gap['blocked_claim']] if gap else [],
            'semantic_ci': semantic_ci,
            'answer_boundary': ('Stay within the original request and authorized scope. Preserve '
                                'open state and truth layers. Withhold blocked claims. Cite only '
                                'sources actually used. Return answer, addressed_scope and source_refs.'),
            'semantic_rules': {key: config['policies'][key]
                               for key in ('authority', 'provenance', 'carryover')},
        }
        return {'status': packet['status'], 'stages': stage, 'packet': packet}
    except (StopRoute, ControlError) as error:
        return {'status': error.status if isinstance(error, StopRoute) else REVIEW,
                'stages': stage, 'reason': str(error), 'packet': None}


def check_response(result, draft):
    """Validate response envelope and retain execution limits. Prose needs semantic review."""
    packet = result['packet']
    gate(packet is not None and result['stages'][-1] == EXECUTION, 'Execution has not been granted')
    gate(fields(draft, {'answer', 'addressed_scope', 'source_refs'}) and text(draft['answer'])
         and list_of_strings(draft['addressed_scope']) and bool(draft['addressed_scope'])
         and set(draft['addressed_scope']) <= set(packet['authorized_scope'])
         and list_of_strings(draft['source_refs']) and bool(draft['source_refs'])
         and set(draft['source_refs']) <= {doc['path'] for doc in packet['sources']},
         'Draft exceeds permitted scope or cites unavailable sources')
    return {**draft, 'execution_state': RESPONSE, 'status': packet['status'],
            'canon_mutation_allowed': packet['canon_mutation_allowed'],
            'unresolved_gaps': packet['unresolved_gaps'], 'blocked_claims': packet['blocked_claims']}

def complete(result, generate):
    """Call the reasoning model only after a grant; keep its input separate from gate state."""
    gate(result['packet'] is not None and result['stages'][-1] == EXECUTION,
         'Execution has not been granted')
    return check_response(result, generate(deepcopy(result['packet'])))

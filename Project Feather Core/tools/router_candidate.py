"""Read-only active control maintenance checks. Never execute prompts or determine canon authority."""
from pathlib import Path
import re

ROUTER = 'Anti-Drift Source/FTH_Anti_Drift_Source_Router_v5.0.yaml'
STAGES = ['PROMPT_ROUTE_ONLY', 'BOOTSTRAP_GATE', 'MODULE_GATE', 'SOURCE_LOAD',
          'RECONCILIATION', 'ANTI_DRIFT_OVERLAY_GATE', 'PROMPT_EXECUTION', 'PRE_RESPONSE_CHECK']
FAILURES = {
    'bootstrap_missing_or_inconsistent': 'SOURCE_LOAD_BLOCKED',
    'decisive_source_or_authority_missing': 'SOURCE_LOAD_BLOCKED',
    'hard_module_dependency_missing_unreviewed_or_cycle': 'SOURCE_LOAD_BLOCKED',
    'required_control_missing_or_ambiguous': 'SOURCE_LOAD_BLOCKED',
    'module_identity_or_role_ambiguous': 'REVIEW_REQUIRED',
    'unresolved_controlling_owner': 'SOURCE_LOAD_BLOCKED',
    'node_uncertain_missing_or_cycle': 'FULL_FILE',
    'unknown_load_mode_clear_identity_authority': 'FULL_FILE',
    'unknown_load_mode_unclear_identity_authority': 'SOURCE_LOAD_BLOCKED',
    'demonstrably_nondecisive_secondary_gap': 'SOURCE_LOAD_PARTIAL',
}
CLOSURE = ['mandatory module context', 'reviewed local index and target node bounds',
           'complete target node', 'transitive reviewed node dependencies',
           'decisive qualifiers, exceptions and priority', 'current and open status',
           'controlling owner context']
POLICIES = {'routing', 'discovery', 'module_gate', 'dependencies', 'loading',
            'authority', 'access', 'overlays', 'coverage'}


class CandidateError(ValueError):
    pass


def require(ok, message):
    if not ok:
        raise CandidateError(message)


def fields(value, expected, label):
    require(isinstance(value, dict) and set(value) == set(expected),
            f'{label}: missing or unknown fields')


def strings(value, label):
    require(isinstance(value, list) and all(isinstance(x, str) and x.strip() for x in value),
            f'{label}: expected string list')
    require(len(value) == len(set(value)), f'{label}: duplicates')


def load(path):
    try:
        import yaml
    except ImportError as error:
        raise CandidateError('PyYAML is required only for the control check') from error

    class UniqueLoader(yaml.SafeLoader):
        pass

    def mapping(loader, node):
        result = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node)
            require(isinstance(key, str) and key not in result, 'YAML: duplicate or non-string key')
            result[key] = loader.construct_object(value_node)
        return result

    UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
    try:
        return yaml.load(path.read_text(encoding='utf-8-sig'), Loader=UniqueLoader)
    except yaml.YAMLError as error:
        raise CandidateError(f'Invalid YAML: {error}') from error


def local_file(root, relative):
    require(isinstance(relative, str) and relative.strip(), 'Invalid file reference')
    path = (root / relative).resolve()
    require(path.is_relative_to(root.resolve()) and path.is_file(), f'Missing/outside reference: {relative}')
    return path


def graph(controls):
    require(isinstance(controls, list) and controls, 'controls: expected nonempty list')
    result = {}
    stems = set()
    for row in controls:
        fields(row, {'id', 'stem', 'select_when', 'requires', 'conditional_requires'}, 'control')
        name, stem = row['id'], row['stem']
        require(isinstance(name, str) and re.fullmatch(r'[A-Z][A-Z_]*', name), 'Invalid control ID')
        require(name not in result, f'Duplicate control ID: {name}')
        require(isinstance(stem, str) and re.fullmatch(r'FTH_Anti_Drift_[A-Za-z_]+', stem), 'Invalid control stem')
        require(stem not in stems, f'Duplicate control stem: {stem}')
        stems.add(stem)
        require(isinstance(row['select_when'], str) and row['select_when'].strip(), 'Missing semantic selection policy')
        strings(row['requires'], f'{name}.requires')
        require(isinstance(row['conditional_requires'], list), 'conditional_requires: expected list')
        pairs = set()
        for edge in row['conditional_requires']:
            fields(edge, {'when', 'target'}, 'conditional edge')
            require(all(isinstance(v, str) and v.strip() for v in edge.values()), 'Invalid conditional edge')
            pair = (edge['when'], edge['target'])
            require(pair not in pairs, 'Duplicate conditional edge')
            pairs.add(pair)
        result[name] = row
    active, done = set(), set()

    def visit(name):
        require(name in result, f'Missing dependency target: {name}')
        require(name not in active, f'Control dependency cycle: {name}')
        if name in done:
            return
        active.add(name)
        row = result[name]
        for target in row['requires'] + [x['target'] for x in row['conditional_requires']]:
            visit(target)
        active.remove(name)
        done.add(name)

    for name in result:
        visit(name)
    return result


def expand(controls, selected, true_conditions=()):
    """Expand already judged IDs/conditions; this function never judges applicability."""
    rows = graph(controls)
    flags = set(true_conditions)
    known = {e['when'] for row in controls for e in row['conditional_requires']}
    require(flags <= known, f'Unknown condition: {flags - known}')
    pending, found = list(selected), set()
    while pending:
        name = pending.pop()
        require(name in rows, f'Unknown selected control: {name}')
        if name in found:
            continue
        found.add(name)
        row = rows[name]
        pending.extend(row['requires'])
        pending.extend(e['target'] for e in row['conditional_requires'] if e['when'] in flags)
    return sorted(found)


def resolve_control(directory, stem, excluded):
    """Resolve direct children only, numeric version, never repository-wide discovery."""
    pattern = re.compile(re.escape(stem) + r'_v([0-9]+\.[0-9]+(?:\.[0-9]+)?)\.(?:md|yaml)$', re.I)
    candidates = []
    for path in directory.iterdir():
        if not path.is_file() or not path.name.lower().startswith(stem.lower() + '_v'):
            continue
        text = path.read_text(encoding='utf-8-sig')
        statuses = set(re.findall(r'^>\s*Status:\s*([A-Z_]+)', text, re.M))
        if path.suffix.lower() == '.yaml':
            metadata = load(path)
            require(isinstance(metadata, dict) and isinstance(metadata.get('deployment'), dict), f'Invalid deployment metadata: {path.name}')
            status = metadata['deployment'].get('status')
            require(isinstance(status, str), f'Missing deployment status: {path.name}')
            statuses.add(status)
        require(len(statuses) <= 1, f'Ambiguous status: {path.name}')
        if statuses.intersection(excluded):
            continue
        match = pattern.fullmatch(path.name)
        require(match is not None, f'Malformed eligible version: {path.name}')
        version = tuple(int(x) for x in match.group(1).split('.'))
        while len(version) > 1 and version[-1] == 0:
            version = version[:-1]
        candidates.append((version, path))
    require(candidates, f'Missing eligible control: {stem}')
    highest = max(v for v, _ in candidates)
    winners = [p for v, p in candidates if v == highest]
    require(len(winners) == 1, f'Ambiguous highest version: {stem}')
    return winners[0]


def validate(data, root):
    fields(data, {'schema_version', 'deployment', 'runtime', 'bootstrap', 'modules',
                  'loading', 'failures', 'control_selection', 'controls', 'policies'}, 'router')
    require(type(data['schema_version']) is int and data['schema_version'] == 1, 'Unsupported schema')
    dep = data['deployment']
    fields(dep, {'status', 'router_version', 'ci_version', 'upstream_base', 'ci',
                 'baseline_ci', 'baseline_router', 'pipeline'}, 'deployment')
    require((dep['status'], dep['router_version'], dep['ci_version'], dep['upstream_base']) ==
            ('ACTIVE', '5.0', '3.4', '8.9'), 'Unsupported active compatibility tuple')
    refs = {k: local_file(root, dep[k]) for k in ('ci', 'baseline_ci', 'baseline_router', 'pipeline')}
    ci = refs['ci'].read_text(encoding='utf-8-sig')
    require(len(refs['ci'].read_bytes().decode('utf-8-sig')) <= 8000, 'Active CI exceeds 8000 characters')
    require(ci.split('\n', 1)[0] == '# Project Feather Core CI v3.4 (FTH) - ChatGPT 8.9 base', 'Active CI version/base mismatch')
    require('> Status: ACTIVE PROJECT CONTROL' in ci and ROUTER in ci, 'Active CI status/router reference mismatch')
    require(refs['baseline_ci'].read_text(encoding='utf-8-sig').startswith('# Project Feather Core CI v3.3 '), 'Baseline CI mismatch')
    require('Source Router v4.4' in refs['baseline_router'].read_text(encoding='utf-8-sig').split('\n', 1)[0], 'Baseline Router mismatch')
    require(refs['pipeline'].name == 'FTH_Authoring_Pipeline_v1.1.md' and
            refs['pipeline'].read_text(encoding='utf-8-sig').split('\n', 1)[0] == '# FTH Authoring Pipeline v1.1',
            'Pipeline mismatch')
    require(refs['pipeline'].name in ci, 'Active CI pipeline reference mismatch')
    # The upstream file is a maintenance reference, never runtime discovery.
    relative = 'ChatGPT Plus+ Era/chatgpt v8.9.txt'
    upstream_paths = [root.parent / relative,
                      root.parent / 'llm-controls/global-instructions' / relative]
    require(any(path.is_file() for path in upstream_paths), 'Missing upstream 8.9 baseline')
    fields(data['runtime'], {'entry', 'stages'}, 'runtime')
    require(data['runtime'] == {'entry': 'PROMPT_ROUTE_ONLY', 'stages': STAGES}, 'Runtime entry/stage order mismatch')
    b = data['bootstrap']
    fields(b, {'full_file', 'same_current_generation', 'reconciliation_record', 'record_read_when'}, 'bootstrap')
    require(b['full_file'] == ['00_AETHERFIRE_CONSOLIDATION_INDEX.md', '92_OPEN_ISSUES_CURRENT.md']
            and b['same_current_generation'] is True, 'Bootstrap contract mismatch')
    require(b['reconciliation_record'] == '91_RECONCILIATION_RECORD.md', 'Reconciliation record mismatch')
    require(isinstance(b['record_read_when'], str) and b['record_read_when'].strip(), 'Missing record-read policy')
    for name in b['full_file'] + [b['reconciliation_record']]:
        local_file(root, name)
    m = data['modules']
    fields(m, {'required_header', 'conditional_header', 'hard_dependency_field', 'node_dependency_field'}, 'modules')
    require(m['required_header'] == ['Module ID', 'Runtime role', 'Domain / Scope'], 'Header contract mismatch')
    require(m['conditional_header'] == {'Authority boundary': 'material owner separation',
            'Cross-domain owner boundary': 'known material interface'}, 'Conditional header contract mismatch')
    require(m['hard_dependency_field'] == 'MODULE_REQUIRES' and m['node_dependency_field'] == 'NODE_REQUIRES', 'Dependency field mismatch')
    loading = data['loading']
    fields(loading, {'default', 'modes', 'read_proofs', 'closure_components', 'full_file_when'}, 'loading')
    require(loading['default'] == 'FULL_FILE' and loading['modes'] == ['FULL_FILE', 'NODE_OR_FULL']
            and loading['read_proofs'] == ['FULL_FILE', 'VERIFIED_MODULE_CLOSURE'], 'Load/read-proof contract mismatch')
    require(loading['closure_components'] == CLOSURE, 'Missing/invalid closure component')
    for name in ('closure_components', 'full_file_when'):
        strings(loading[name], name)
        require(loading[name], f'Empty {name}')
    require(data['failures'] == FAILURES, 'Failure-state contract mismatch')
    selection = data['control_selection']
    require(selection == {'directory': 'Anti-Drift Source', 'files': 'direct_children_only',
            'version_order': 'numeric', 'ambiguity': 'SOURCE_LOAD_BLOCKED',
            'excluded_statuses': ['CANDIDATE', 'DRAFT', 'REJECTED', 'SUPERSEDED', 'RETIRED', 'ARCHIVED'],
            'load': 'FULL_FILE'}, 'Control selection contract mismatch')
    rows = graph(data['controls'])
    require(set(rows) == {'MCA', 'ECONOMY', 'WIL', 'TW', 'ACTOR_RECEPTION', 'BELIEF_CULTURE', 'MORTALITY', 'UNDIE'}, 'Missing/unknown control family')
    resolved = {name: resolve_control(root / selection['directory'], row['stem'], selection['excluded_statuses'])
                for name, row in rows.items()}
    fields(data['policies'], POLICIES, 'policies')
    require(all(isinstance(v, str) and v.strip() for v in data['policies'].values()), 'Empty semantic policy')
    # Maintenance selection only; none of these checks are Router runtime stages.
    for directory, stem, expected in [('Project Feather Core CI', 'FTH_CI_version', refs['ci']),
                                       ('Anti-Drift Source', 'FTH_Anti_Drift_Source_Router', root / ROUTER),
                                       ('Anti-Drift Source', 'FTH_Authoring_Pipeline', refs['pipeline'])]:
        require(resolve_control(root / directory, stem, selection['excluded_statuses']).resolve() == expected.resolve(),
                f'Active selection mismatch: {stem}')
    return resolved


def check(root):
    return validate(load(root / ROUTER), root)

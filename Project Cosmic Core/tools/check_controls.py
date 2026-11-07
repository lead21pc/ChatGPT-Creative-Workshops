"""Static C2 control checks; applicability is judged by the model, not inferred here."""

import json

ROUTER = 'Anti-Drift Source/C2_Anti_Drift_Source_Router_v1.0.json'
CI = 'Project Cosmic Core CI/C2_CI_v1.0.md'
FAMILIES = {
    'MCA': 'Anti-Drift Source/C2_Anti_Drift_Modular_Concept_Architecture_v1.0.md',
    'WIL': 'Anti-Drift Source/C2_Anti_Drift_Worldbuilding_Internal_Logic_v1.0.md',
    'ACTOR_RECEPTION': 'Anti-Drift Source/C2_Anti_Drift_Actor_Reception_v1.0.md',
    'OPERATIONAL_MISSION': 'Anti-Drift Source/C2_Anti_Drift_Operational_Mission_v1.0.md',
}
STAGES = ['PROMPT_ROUTE_ONLY', 'BOOTSTRAP_GATE', 'MODULE_GATE', 'SOURCE_LOAD',
          'RECONCILIATION', 'ANTI_DRIFT_OVERLAY_GATE', 'PROMPT_EXECUTION', 'PRE_RESPONSE_CHECK']
FIELDS = ['Module ID', 'Runtime role', 'Domain / Scope', 'Authority boundary',
          'Cross-domain owner boundary', 'Load mode']
POLICIES = {'routing', 'discovery', 'module_gate', 'loading', 'authority',
            'provenance', 'access', 'overlays', 'carryover', 'coverage'}
FAILURES = {
    'bootstrap_missing_or_inconsistent': 'SOURCE_LOAD_BLOCKED',
    'decisive_source_or_authority_missing': 'SOURCE_LOAD_BLOCKED',
    'required_control_missing_or_ambiguous': 'SOURCE_LOAD_BLOCKED',
    'module_identity_or_role_ambiguous': 'REVIEW_REQUIRED',
    'unresolved_controlling_owner': 'SOURCE_LOAD_BLOCKED',
    'demonstrably_nondecisive_secondary_gap': 'SOURCE_LOAD_PARTIAL',
}


class ControlError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise ControlError(message)


def local_file(root, relative):
    require(isinstance(relative, str) and relative, 'Invalid control path')
    path = root / relative
    require(not path.is_symlink() and path.resolve().is_relative_to(root.resolve())
            and path.is_file(), f'Missing or redirected control: {relative}')
    return path


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f'Duplicate JSON key: {key}')
        result[key] = value
    return result


def load(root):
    try:
        return json.loads(local_file(root, ROUTER).read_text(encoding='utf-8-sig'),
                          object_pairs_hook=unique_object)
    except (json.JSONDecodeError, UnicodeError, OSError) as error:
        raise ControlError(f'Invalid Router: {error}') from error


def controls_by_id(config):
    require(isinstance(config, dict), 'Router must be an object')
    controls = config.get('controls')
    require(isinstance(controls, list), 'controls must be a list')
    result = {}
    for row in controls:
        require(isinstance(row, dict) and set(row) == {
            'id', 'path', 'select_when', 'requires', 'conditional_requires'}, 'Invalid control row')
        key = row['id']
        require(isinstance(key, str) and key in FAMILIES and key not in result,
                'Unknown or duplicate control family')
        require(row['path'] == FAMILIES[key], f'Wrong active path: {key}')
        require(isinstance(row['select_when'], str) and row['select_when'].strip(),
                f'Missing applicability: {key}')
        requires = row['requires']
        require(isinstance(requires, list) and all(isinstance(x, str) for x in requires),
                f'Invalid dependencies: {key}')
        require(len(set(requires)) == len(requires) and set(requires) <= FAMILIES.keys(),
                f'Unknown or duplicate dependency: {key}')
        edges = row['conditional_requires']
        require(isinstance(edges, list), f'Invalid conditional dependencies: {key}')
        seen = set()
        for edge in edges:
            require(isinstance(edge, dict) and set(edge) == {'when', 'target'}, 'Invalid edge')
            require(isinstance(edge['when'], str) and edge['when'].strip()
                    and isinstance(edge['target'], str) and edge['target'] in FAMILIES,
                    'Invalid conditional target or condition')
            pair = (edge['when'], edge['target'])
            require(pair not in seen, 'Duplicate conditional edge')
            seen.add(pair)
        result[key] = row
    require(set(result) == set(FAMILIES), 'Exactly four baseline families required')
    return result


def resolve(config, selected=(), conditions=()):
    """Expand only supplied semantic choices/true conditions. Never load files or prompts."""
    controls = controls_by_id(config)
    selected, conditions = set(selected), set(conditions)
    require(selected <= controls.keys(), 'Unknown selected family')
    known = {edge['when'] for row in controls.values() for edge in row['conditional_requires']}
    require(conditions <= known, 'Unknown condition')
    done, active = set(), set()

    def visit(key):
        require(key not in active, f'Control dependency cycle: {key}')
        if key in done:
            return
        active.add(key)
        row = controls[key]
        for target in row['requires']:
            visit(target)
        for edge in row['conditional_requires']:
            if edge['when'] in conditions:
                visit(edge['target'])
        active.remove(key)
        done.add(key)

    for key in sorted(selected):
        visit(key)
    return done


def check(root):
    config = load(root)
    require(isinstance(config, dict) and set(config) == {
        'schema_version', 'deployment', 'runtime', 'bootstrap', 'modules', 'loading',
        'control_selection', 'controls', 'failures', 'policies'}, 'Invalid Router sections')
    require(config['schema_version'] == 1, 'Invalid schema version')
    require(config['deployment'] == {
        'status': 'ACTIVE_LOCAL', 'router_version': '1.0', 'ci_version': '1.0',
        'ci': CI, 'live_verified': 'NOT_RUN'}, 'Invalid CI/Router relation or evidence state')
    ci = local_file(root, CI).read_text(encoding='utf-8-sig')
    require(ci.startswith('# Project Cosmic Core — CI v1.0\n')
            and '> Status: ACTIVE\n' in ci and f'> Router: {ROUTER}\n' in ci,
            'CI identity/status/Router mismatch')
    require(config['runtime'] == {'entry': STAGES[0], 'stages': STAGES}, 'Invalid stages')
    bootstrap = config['bootstrap']
    require(isinstance(bootstrap, dict) and set(bootstrap) == {
        'full_file', 'same_current_generation', 'reconciliation_record', 'record_read_when'},
        'Invalid bootstrap')
    require(bootstrap['full_file'] == ['00_C2_CONSOLIDATION_INDEX.md', '05_OPEN_ISSUES_CURRENT.md']
            and bootstrap['same_current_generation'] is True
            and bootstrap['reconciliation_record'] == '04_RECONCILIATION_RECORD.md'
            and isinstance(bootstrap['record_read_when'], str) and bootstrap['record_read_when'].strip(),
            'Invalid bootstrap sources')
    for name in bootstrap['full_file'] + [bootstrap['reconciliation_record']]:
        local_file(root, name)
    require(config['modules'] == {'required_header': FIELDS, 'runtime_role': 'CURRENT_SOURCE'},
            'Invalid source header contract')
    require(config['loading'] == {
        'default': 'FULL_FILE', 'modes': ['FULL_FILE'], 'read_proofs': ['FULL_FILE']},
        'Only FULL_FILE is admitted')
    require(config['control_selection'] == {
        'directory': 'Anti-Drift Source', 'files': 'direct_children_only',
        'versions': 'explicit_active_paths', 'load': 'FULL_FILE',
        'ambiguity': 'SOURCE_LOAD_BLOCKED'}, 'Invalid control selection')
    controls = controls_by_id(config)
    expected_requires = {'MCA': [], 'WIL': [], 'ACTOR_RECEPTION': ['MCA'],
                         'OPERATIONAL_MISSION': ['MCA']}
    for key, row in controls.items():
        require(row['requires'] == expected_requires[key], f'Dependency drift: {key}')
        expected = ([{'when': 'institutional_interface_material', 'target': 'WIL'},
                     {'when': 'operational_interface_material', 'target': 'OPERATIONAL_MISSION'}]
                    if key == 'ACTOR_RECEPTION' else [])
        require(row['conditional_requires'] == expected, f'Conditional dependency drift: {key}')
        text = local_file(root, row['path']).read_text(encoding='utf-8-sig')
        require(text.startswith('# C2 — ') and '> Status: ACTIVE\n' in text
                and f'> Family: {key}\n' in text, f'Invalid active control identity: {key}')
    actual = {p.relative_to(root).as_posix() for p in (root / 'Anti-Drift Source').glob('*.md')}
    require(actual == set(FAMILIES.values()), 'Unexpected or missing baseline control file')
    require(config['failures'] == FAILURES, 'Invalid failure behavior')
    require(isinstance(config['policies'], dict) and set(config['policies']) == POLICIES
            and all(isinstance(x, str) and x.strip() for x in config['policies'].values()),
            'Missing semantic policies')
    # All-edge traversal detects structural cycles; it does not select all controls at runtime.
    conditions = {edge['when'] for row in controls.values() for edge in row['conditional_requires']}
    resolve(config, controls, conditions)
    require(resolve(config) == set(), 'Controls must not be selected by default')
    return {key: local_file(root, row['path']) for key, row in controls.items()}

"""Static C2 control checks; applicability is judged by the model, not inferred here."""

import json
import re

ROUTER_VERSION = '1.2'
CI_VERSION = '1.2'
ROUTER = f'Anti-Drift Source/C2_Anti_Drift_Source_Router_v{ROUTER_VERSION}.json'
CI = f'Project Cosmic Core CI/C2_CI_v{CI_VERSION}.md'
PIPELINE = 'Anti-Drift Source/C2_Authoring_Pipeline_v1.0.md'
FAMILIES = {
    'MCA': 'C2_Anti_Drift_Modular_Concept_Architecture',
    'WIL': 'C2_Anti_Drift_Worldbuilding_Internal_Logic',
    'ACTOR_RECEPTION': 'C2_Anti_Drift_Actor_Reception',
    'OPERATIONAL_MISSION': 'C2_Anti_Drift_Operational_Mission',
    'ECONOMY': 'C2_Anti_Drift_Interface_Economy_State_Stabilization',
    'BELIEF_CULTURE': 'C2_Anti_Drift_Belief_Culture',
    'MORTALITY': 'C2_Anti_Drift_Mortality_Relationship_Plot_Immunity',
}
CONTROL_SELECTION = {
    'directory': 'Anti-Drift Source',
    'files': 'direct_children_only',
    'version_order': 'numeric',
    'eligible_status': 'ACTIVE',
    'excluded_statuses': ['CANDIDATE', 'DRAFT', 'REJECTED', 'SUPERSEDED', 'RETIRED', 'ARCHIVED'],
    'load': 'FULL_FILE',
    'ambiguity': 'SOURCE_LOAD_BLOCKED',
}
VERSION = r'[0-9]+\.[0-9]+(?:\.[0-9]+)?'
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
            'id', 'stem', 'select_when', 'requires', 'conditional_requires'}, 'Invalid control row')
        key = row['id']
        require(isinstance(key, str) and key in FAMILIES and key not in result,
                'Unknown or duplicate control family')
        require(row['stem'] == FAMILIES[key], f'Wrong family stem: {key}')
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
    require(set(result) == set(FAMILIES), 'Router must register exactly the C2 Anti-Drift families')
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


def version_parts(version):
    parts = tuple(int(value) for value in version.split('.'))
    return parts + (0,) * (3 - len(parts))


def control_header(text, name):
    # Read status and family from the initial Markdown header only.
    lines = text.splitlines()
    block = []
    for line in lines[1:]:
        if not line.strip() and not block:
            continue
        if not line.startswith('>'):
            break
        block.append(line)
    statuses = [match[1].strip() for line in block
                if (match := re.fullmatch(r'>\s*Status:\s*(.*)', line))]
    require(len(statuses) == 1, f'Missing or ambiguous control status: {name}')
    families = [match[1].strip() for line in block
                if (match := re.fullmatch(r'>\s*Family:\s*(.*)', line))]
    return lines[0], statuses[0], families


def control_filename(row):
    return re.compile(re.escape(row['stem']) + rf'_v({VERSION})\.md')


def eligible_version(path, row, text, selection):
    filename = control_filename(row).fullmatch(path.name)
    require(filename is not None, f'Invalid control filename: {path.name}')
    heading, status, families = control_header(text, path.name)
    if status in selection['excluded_statuses']:
        return None
    require(status == selection['eligible_status'], f'Unknown control status: {path.name}')
    version = version_parts(filename[1])
    match = re.fullmatch(rf'# C2 — .+ v({VERSION})', heading)
    require(families == [row['id']] and match is not None and version_parts(match[1]) == version,
            f'Invalid active control identity: {path.name}')
    return version


def resolve_control(root, selection, row):
    # Resolve a required family without consulting other families.
    require(selection == CONTROL_SELECTION, 'Invalid control selection')
    directory = root / selection['directory']
    require(not directory.is_symlink() and directory.resolve().parent == root.resolve()
            and directory.is_dir(), f'Missing or redirected control directory: {directory.name}')
    pattern = control_filename(row)
    candidates = []
    for path in sorted(directory.iterdir()):
        if not pattern.fullmatch(path.name):
            continue
        relative = path.relative_to(root).as_posix()
        try:
            text = local_file(root, relative).read_text(encoding='utf-8-sig')
        except (UnicodeError, OSError) as error:
            raise ControlError(f'Cannot read control identity: {relative}') from error
        version = eligible_version(path, row, text, selection)
        if version is not None:
            candidates.append((version, path))
    require(candidates, f"Missing eligible control: {row['id']} ({row['stem']})")
    highest = max(version for version, _ in candidates)
    winners = [path for version, path in candidates if version == highest]
    require(len(winners) == 1, f"Ambiguous highest version: {row['id']}")
    return winners[0]


def check(root):
    config = load(root)
    require(isinstance(config, dict) and set(config) == {
        'schema_version', 'deployment', 'runtime', 'bootstrap', 'modules', 'loading',
        'control_selection', 'controls', 'failures', 'policies'}, 'Invalid Router sections')
    require(config['schema_version'] == 1, 'Invalid schema version')
    require(config['deployment'] == {
        'status': 'ACTIVE', 'router_version': ROUTER_VERSION, 'ci_version': CI_VERSION,
        'ci': CI}, 'Invalid CI/Router relation or evidence state')
    ci = local_file(root, CI).read_text(encoding='utf-8-sig')
    require(ci.startswith(f'# Project Cosmic Core — CI v{CI_VERSION}\n')
            and '> Status: ACTIVE\n' in ci, 'CI identity/status mismatch')
    source_gate = ci.partition('## Source gate\n\n')[2].partition('\n## ')[0]
    router_name = ROUTER.rsplit('/', 1)[-1]
    require('Router REQUIRED before current-C2-dependent work.' in source_gate
            and f'`{router_name}`' in source_gate and ROUTER not in source_gate
            and "from this Project's Project Sources." in source_gate
            and 'Library' not in source_gate
            and f'Verify C2 Router {ROUTER_VERSION}; read FULL_FILE -> PROMPT_ROUTE_ONLY.' in source_gate
            and 'Missing/ambiguous/partial Router: block dependent work;' in source_gate
            and 'ask for the file, never invent it.' in source_gate,
            'CI must locate and fully read the Router from available web project sources')
    pipeline = local_file(root, PIPELINE).read_text(encoding='utf-8-sig')
    heading, status, families = control_header(pipeline, PIPELINE)
    require(heading == '# C2 — Authoring Pipeline v1.0' and status == 'ACTIVE' and not families
            and '> Type: PROCEDURAL AUTHORING CONTROL' in pipeline.partition('\n\n')[2].partition('\n\n')[0].splitlines(),
            'Invalid procedural control identity')
    activation = ci.partition('## Subordinate controls\n\n')[2].partition('\n\n')[0]
    pipeline_name = PIPELINE.rsplit('/', 1)[-1]
    require(f'`{pipeline_name}`' in activation and PIPELINE not in activation
            and "from this Project's Project Sources." in activation
            and 'Read FULL_FILE and follow it before transforming.' in activation
            and 'Keywords alone do not activate it.' in activation
            and 'blocks only the dependent transformation.' in activation
            and 'cannot waive Router entry.' in activation,
            'CI must locate and fully read the Pipeline for requested transformations')
    require(config['runtime'] == {'entry': STAGES[0], 'stages': STAGES}, 'Invalid stages')
    bootstrap = config['bootstrap']
    require(isinstance(bootstrap, dict) and set(bootstrap) == {
        'full_file', 'same_current_generation', 'reconciliation_record', 'record_read_when'},
        'Invalid bootstrap')
    require(bootstrap['full_file'] == ['00_C2_CONSOLIDATION_INDEX.md', '05_OPEN_ISSUES.md']
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
    selection = config['control_selection']
    require(selection == CONTROL_SELECTION, 'Invalid control selection')
    controls = controls_by_id(config)
    requires_mca = {'ACTOR_RECEPTION', 'OPERATIONAL_MISSION', 'MORTALITY'}
    economic = ('economic_mechanism_material', 'ECONOMY')
    institutional = ('institutional_interface_material', 'WIL')
    conflict = ('operational_conflict_material', 'OPERATIONAL_MISSION')
    expected_conditions = {
        'WIL': {economic},
        'ACTOR_RECEPTION': {institutional, economic,
                            ('operational_interface_material', 'OPERATIONAL_MISSION')},
        'BELIEF_CULTURE': {('actor_reception_material', 'ACTOR_RECEPTION'),
                          institutional, economic, conflict},
        'MORTALITY': {conflict},
    }
    for key, row in controls.items():
        require(row['requires'] == (['MCA'] if key in requires_mca else []),
                f'Dependency drift: {key}')
        edges = {(item['when'], item['target']) for item in row['conditional_requires']}
        require(edges == expected_conditions.get(key, set()), f'Conditional dependency drift: {key}')
    require(config['failures'] == FAILURES, 'Invalid failure behavior')
    require(isinstance(config['policies'], dict) and set(config['policies']) == POLICIES
            and all(isinstance(x, str) and x.strip() for x in config['policies'].values()),
            'Missing semantic policies')
    # All-edge traversal detects structural cycles; it does not select all controls at runtime.
    conditions = {edge['when'] for row in controls.values() for edge in row['conditional_requires']}
    resolve(config, controls, conditions)
    require(resolve(config) == set(), 'Controls must not be selected by default')
    return {key: resolve_control(root, selection, row) for key, row in controls.items()}

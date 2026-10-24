#!/usr/bin/env python3
"""Read-only package integrity checks, never a prompt executor or canon judge."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import unicodedata
from urllib.parse import unquote

STAGES = ['PROMPT_ROUTE_ONLY', 'BOOTSTRAP_GATE', 'OWNER_GATE', 'TEMPORAL_GATE',
          'SOURCE_LOAD', 'RECONCILIATION', 'ANTI_DRIFT_OVERLAY_GATE',
          'PROMPT_EXECUTION', 'PRE_RESPONSE_CHECK']
FIELDS = ('SOURCE_ID', 'RUNTIME_ROLE', 'ROLE', 'STATUS', 'SCOPE',
          'AUTHORITY_BOUNDARY', 'CROSS_OWNER_BOUNDARY', 'LOAD_MODE')
ROLE_VALUES = {'DOMAIN', 'DOMAIN / DESIGN PHILOSOPHY', 'DOMAIN / OPENING DESIGN',
               'RUNTIME / AUTHORING METHOD', 'CHECKPOINT', 'INTERVAL',
               'POST-CHECKPOINT MATERIAL', 'ACTOR', 'EVENT'}
CORE = {'CI': 'CI_KERNEL', 'PIPELINE': 'AUTHORING_PROCEDURE',
        'GLOSSARY': 'MAINTENANCE_REFERENCE'}
SOURCE_ACCESS = {
    'primary_library_folder': 'TK Source',
    'normal_order': ['LIBRARY', 'PROJECT_SOURCES', 'AUTHORIZED_EXTERNAL'],
    'external_authorization': 'TASK_LOCAL_EXPLICIT',
    'repository_role': 'MAINTENANCE_NOT_AUTOMATIC_RUNTIME_SOURCE',
    'location_grants_authority': False,
    'project_presence_grants_authority': False,
    'external_name_grants_identity': False,
    'library_contents_verified': False,
    'library_synchronization': 'NOT_PERFORMED',
    'live_project_deployment': 'NOT_PERFORMED',
}


class ValidationError(ValueError):
    """No dependent package operation is valid until this defect is repaired."""


def require(ok, message):
    if not ok:
        raise ValidationError(message)


def numeric_version(value):
    require(isinstance(value, str) and re.fullmatch(r'\d+\.\d+(?:\.\d+)?', value),
            f'Invalid numeric version: {value!r}')
    result = tuple(map(int, value.split('.')))
    while len(result) > 1 and result[-1] == 0:
        result = result[:-1]
    return result


def safe_file(root, relative):
    """Resolve current files without ever admitting an archive or redirection."""
    require(isinstance(relative, str) and relative and '\\' not in relative,
            f'Invalid package path: {relative!r}')
    part = Path(relative)
    require(not part.is_absolute() and not {'..', 'source_archive'} &
            {x.casefold() for x in part.parts}, f'Non-current path: {relative}')
    path = root / part
    require(path.resolve().is_relative_to(root.resolve()), f'Outside package: {relative}')
    for node in (path, *path.parents):
        if node == root.parent:
            break
        require(not node.is_symlink(), f'Symlink current input: {relative}')
        if node.exists():
            require(not (getattr(node.lstat(), 'st_file_attributes', 0) & 0x400),
                    f'Reparse point current input: {relative}')
    require(path.is_file(), f'Missing current file: {relative}')
    return path


def yaml_data(text):
    try:
        import yaml
    except ImportError as error:
        raise ValidationError('PyYAML is required for the Router check') from error

    class UniqueLoader(yaml.SafeLoader):
        pass

    def unique_mapping(loader, node):
        result = {}
        for key, value in node.value:
            name = loader.construct_object(key)
            require(isinstance(name, str) and name != '<<' and name not in result,
                    'YAML duplicate or non-string mapping key')
            result[name] = loader.construct_object(value)
        return result

    UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
                                 unique_mapping)
    try:
        require(not any(isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken,
                                          yaml.tokens.TagToken)) for token in yaml.scan(text)),
                'YAML anchors, aliases, and explicit tags are prohibited')
        result = yaml.load(text, Loader=UniqueLoader)
    except yaml.YAMLError as error:
        raise ValidationError(f'Invalid YAML: {error}') from error
    require(isinstance(result, dict), 'Router must be a mapping')
    return result


def control_metadata(path):
    text = path.read_text(encoding='utf-8-sig')
    if path.suffix == '.yaml':
        data = yaml_data(text)
        return {'Status': data.get('status'), 'Version': data.get('router_version'),
                'Role': 'ROUTER'}
    prefix = text.split('\n## ', 1)[0]
    result = {}
    for key in ('Status', 'Version', 'Role', 'Control_ID'):
        found = re.findall(r'^' + key + r': (.+)\r?$', prefix, re.M)
        require(len(found) <= 1, f'Duplicate control metadata {key}: {path.name}')
        if found:
            result[key] = found[0].strip()
    return result


def resolve_control(root, directory, stem):
    """Only direct children with explicit ACTIVE status; no candidate lifecycle."""
    folder = root / directory
    require(folder.is_dir() and folder.resolve().is_relative_to(root.resolve()) and
            'source_archive' not in {x.casefold() for x in Path(directory).parts},
            f'Invalid control directory: {directory}')
    require(not folder.is_symlink() and
            not (getattr(folder.lstat(), 'st_file_attributes', 0) & 0x400),
            f'Redirected control directory: {directory}')
    require(re.fullmatch(r'TK_[A-Za-z_]+', stem), f'Invalid control stem: {stem}')
    pattern = re.compile(re.escape(stem) + r'_v(\d+\.\d+(?:\.\d+)?)\.(md|yaml)$')
    eligible = []
    for path in sorted(folder.iterdir()):
        if not path.is_file() or not path.name.startswith(stem + '_v'):
            continue
        safe_file(root, path.relative_to(root).as_posix())
        metadata = control_metadata(path)
        if metadata.get('Status') != 'ACTIVE':
            continue
        match = pattern.fullmatch(path.name)
        require(match is not None, f'Malformed ACTIVE filename: {path.name}')
        require(metadata.get('Version') == match[1], f'Version/header mismatch: {path.name}')
        eligible.append((numeric_version(match[1]), path))
    require(eligible, f'Missing ACTIVE control: {stem}')
    top = max(v for v, _ in eligible)
    winners = [p for v, p in eligible if v == top]
    require(len(winners) == 1, f'Ambiguous highest ACTIVE version: {stem}')
    return winners[0]


def control_graph(rows):
    require(isinstance(rows, list) and rows, 'Missing overlay families')
    graph, stems = {}, set()
    for row in rows:
        require(isinstance(row, dict) and set(row) ==
                {'id', 'stem', 'select_when', 'requires', 'conditional_requires'},
                'Invalid overlay contract fields')
        key = row['id']
        require(isinstance(key, str) and re.fullmatch(r'[A-Z][A-Z_]*', key) and
                key not in graph, f'Invalid/duplicate overlay: {key}')
        require(isinstance(row['stem'], str) and row['stem'] not in stems,
                f'Duplicate/invalid overlay stem: {key}')
        require(isinstance(row['select_when'], str) and row['select_when'].strip(),
                f'Empty semantic trigger: {key}')
        require(isinstance(row['requires'], list) and
                all(isinstance(x, str) for x in row['requires']) and
                len(row['requires']) == len(set(row['requires'])), f'Invalid requirements: {key}')
        require(isinstance(row['conditional_requires'], list), f'Invalid conditions: {key}')
        seen = set()
        for edge in row['conditional_requires']:
            require(isinstance(edge, dict) and set(edge) == {'when', 'target'} and
                    all(isinstance(v, str) and v for v in edge.values()),
                    f'Invalid conditional edge: {key}')
            pair = edge['when'], edge['target']
            require(pair not in seen, f'Duplicate conditional edge: {key}')
            seen.add(pair)
        graph[key] = row
        stems.add(row['stem'])
    visiting, done = set(), set()

    def visit(key):
        require(key in graph, f'Unknown control dependency: {key}')
        require(key not in visiting, f'Control dependency cycle: {key}')
        if key in done:
            return
        visiting.add(key)
        for target in graph[key]['requires'] + [x['target'] for x in graph[key]['conditional_requires']]:
            visit(target)
        visiting.remove(key)
        done.add(key)
    for key in graph:
        visit(key)
    return graph


def expand_controls(rows, selected, true_conditions=()):
    """Expand explicit judgments only. This does not classify a user prompt."""
    graph = control_graph(rows)
    known = {e['when'] for row in rows for e in row['conditional_requires']}
    require(set(true_conditions) <= known, 'Unknown applicability condition')
    found, pending = set(), list(selected)
    while pending:
        key = pending.pop()
        require(key in graph, f'Unknown selected overlay: {key}')
        if key in found:
            continue
        found.add(key)
        pending.extend(graph[key]['requires'])
        pending.extend(e['target'] for e in graph[key]['conditional_requires']
                       if e['when'] in true_conditions)
    return sorted(found)


def source_header(text, name):
    text = text.replace('\r\n', '\n')
    match = re.match(r'\A# [^\n]+\n\n```text\n(.*?)\n```', text, re.S)
    require(match is not None, f'Missing initial current-source header: {name}')
    fields = {}
    for line in match[1].splitlines():
        pair = line.split(': ', 1)
        require(len(pair) == 2 and pair[0] in FIELDS and pair[0] not in fields and
                pair[1].strip(), f'Invalid/duplicate source header field: {name}: {line}')
        fields[pair[0]] = pair[1].strip()
    require(set(fields) == set(FIELDS), f'Missing required source fields: {name}')
    require(re.fullmatch(r'TK-[A-Z0-9-]+', fields['SOURCE_ID']), f'Invalid SOURCE_ID: {name}')
    require(fields['RUNTIME_ROLE'] == 'CURRENT_SOURCE', f'Invalid runtime role: {name}')
    require(fields['STATUS'].split(' / ')[0] == 'ACTIVE', f'Inactive admitted source: {name}')
    require(fields['ROLE'] in ROLE_VALUES, f'Unknown semantic role: {name}')
    require(fields['LOAD_MODE'] == 'FULL_FILE', f'Unsupported load mode: {name}')
    return fields


def region(text, label):
    begin, end = f'<!-- BEGIN {label} -->', f'<!-- END {label} -->'
    require(text.count(begin) == text.count(end) == 1, f'Invalid region markers: {label}')
    match = re.search(re.escape(begin) + r'\r?\n(.*?)' + re.escape(end), text, re.S)
    require(match is not None, f'Unordered region: {label}')
    return match


def replace_region(text, label, value):
    match = region(text, label)
    newline = '\r\n' if text[:match.start(1)].endswith('\r\n') else '\n'
    value = value.replace('\r\n', '\n').replace('\n', newline)
    return text[:match.start(1)] + value + text[match.end(1):]


def load_contract(text):
    block = region(text, 'PACKAGE CONTRACT')[1].replace('\r\n', '\n')
    require(block.startswith('```json\n') and block.rstrip().endswith('```'),
            'Invalid manifest contract block')

    def unique(pairs):
        value = {}
        for k, v in pairs:
            require(k not in value, f'Duplicate contract key: {k}')
            value[k] = v
        return value
    try:
        contract = json.loads(block.strip()[8:-3], object_pairs_hook=unique)
    except json.JSONDecodeError as error:
        raise ValidationError(f'Invalid manifest JSON: {error}') from error
    require(isinstance(contract, dict) and set(contract) ==
            {'version', 'status', 'sources', 'navigation', 'records', 'support_controls',
             'maintenance', 'runtime_source_package'},
            'Unknown/missing admission contract fields')
    require(contract['status'] == 'ACTIVE' and contract['version'] == '1.0',
            'Unsupported admission contract version/status')
    all_paths = []
    for name in ('sources', 'navigation', 'records', 'support_controls', 'maintenance'):
        paths = contract[name]
        require(isinstance(paths, list) and paths and all(isinstance(x, str) for x in paths),
                f'Invalid admission list: {name}')
        all_paths += paths
    require(len(all_paths) == len(set(all_paths)), 'Duplicate package path')
    require(all(Path(p).parent == Path('.') for p in contract['sources']),
            'Current owners must be at package root')
    runtime = contract['runtime_source_package']
    require(isinstance(runtime, dict) and set(runtime) ==
            {'library_folder', 'paths', 'contents_verified', 'synchronization', 'deployment'},
            'Runtime source package contract mismatch')
    require(runtime['library_folder'] == 'TK Source' and
            runtime['contents_verified'] is False and
            runtime['synchronization'] == runtime['deployment'] == 'NOT_PERFORMED',
            'Runtime Library target or deployment evidence mismatch')
    expected = set(contract['sources']) | {'TK_CURRENT_SOURCE_INDEX.md',
                 'TK_OPEN_ISSUES_CURRENT.md', 'TK_RECONCILIATION_RECORD.md',
                 'THE_KINGDOM_CHECKPOINT_STATE_INDEX.md'}
    require(isinstance(runtime['paths'], list) and
            all(isinstance(p, str) for p in runtime['paths']) and
            len(runtime['paths']) == len(expected) and set(runtime['paths']) == expected,
            'Runtime lore package must contain exactly current owners and source bootstrap/navigation')
    return contract


def slugs(text):
    result, seen, fenced = set(), {}, False
    for line in text.splitlines():
        if line.startswith(('```', '~~~')):
            fenced = not fenced
            continue
        if fenced or not re.match(r'^#{1,6} ', line):
            continue
        value = re.sub(r'^#+ ', '', line).strip().lower()
        value = ''.join(c for c in value if c in ' -_' or unicodedata.category(c)[0] in 'LN')
        value = value.replace(' ', '-')
        count = seen.get(value, 0)
        seen[value] = count + 1
        result.add(value + (f'-{count}' if count else ''))
    return result


def check_links(root, contents):
    count, historical = 0, 0
    for name, text in contents.items():
        if not name.endswith('.md'):
            continue
        targets = re.findall(r'\]\(([^)]+)\)', text)
        targets += re.findall(r'^\[[^\]]+\]:\s*(.+)$', text, re.M)
        for url in targets:
            url = unquote(url.strip().strip('<>'))
            if re.match(r'^[a-zA-Z]+:', url):
                continue
            path, _, anchor = url.partition('#')
            target = (root / name).parent / path if path else root / name
            require(target.resolve().is_relative_to(root.resolve()), f'Link escapes package: {name}: {url}')
            relative = target.resolve().relative_to(root.resolve()).as_posix()
            if 'source_archive' in {p.casefold() for p in Path(relative).parts}:
                require(name != 'THE_KINGDOM_CHECKPOINT_STATE_INDEX.md',
                        'Timeline index cannot route to historical targets')
                # A provenance link is not a load/hash/build input. Never read its body.
                require(target.is_file(), f'Missing historical provenance target: {url}')
                historical += 1
                continue
            require(relative in contents, f'Link to non-admitted current file: {name}: {url}')
            if anchor:
                require(anchor in slugs(contents[relative]), f'Missing active anchor: {name}: {url}')
            count += 1
    return count, historical


def inspect(root):
    """Validate non-derived structure; return only allowlisted generated updates."""
    root = Path(root).resolve()
    inputs = {}

    def read(name):
        data = safe_file(root, name).read_bytes()
        inputs[name] = data
        return data.decode('utf-8-sig')

    manifest = read('MANIFEST.md')
    contract = load_contract(manifest)
    texts = {name: read(name) for key in ('sources', 'navigation', 'records', 'support_controls', 'maintenance')
             for name in contract[key]}
    sources = {}
    for name in contract['sources']:
        fields = source_header(texts[name], name)
        sid = fields['SOURCE_ID']
        require(sid not in sources, f'Duplicate SOURCE_ID: {sid}')
        require(not re.search(r'mẫu quốc|D:\\', texts[name], re.I), f'Legacy country/path in current lore: {name}')
        sources[sid] = (name, fields)
    for path in root.glob('*.md'):
        if path.name in contract['sources'] or path.name == 'MANIFEST.md':
            continue
        text = read(path.name)
        require(not re.search(r'^RUNTIME_ROLE: CURRENT_SOURCE\s*$', text, re.M),
                f'Unexpected CURRENT_SOURCE outside admission: {path.name}')
    for sid, (name, fields) in sources.items():
        refs = set(re.findall(r'\bTK-[A-Z0-9-]+\b', fields['CROSS_OWNER_BOUNDARY']))
        require(refs <= sources.keys(), f'Unknown cross-owner reference: {name}: {sorted(refs - sources.keys())}')

    rp = resolve_control(root, 'controls', 'TK_ROUTER')
    router_name = rp.relative_to(root).as_posix()
    router = yaml_data(read(router_name))
    texts[router_name] = inputs[router_name].decode('utf-8-sig')
    require(set(router) == {'schema_version','status','router_version','ci_version','upstream_base',
                           'core_controls','runtime','bootstrap','owners','control_selection',
                           'controls','failures','policies','source_access'}, 'Router top-level contract mismatch')
    require(router['schema_version'] == 1 and router['status'] == 'ACTIVE' and
            router['upstream_base'] == '9.0', 'Router schema/status/base mismatch')
    require(router['runtime'] == {'entry': STAGES[0], 'stages': STAGES, 'deployment': 'NOT_PERFORMED'},
            'Runtime stages or deployment contract mismatch')
    require(router['source_access'] == SOURCE_ACCESS and
            all(router['source_access'][key] is False for key in
                ('location_grants_authority', 'project_presence_grants_authority',
                 'external_name_grants_identity', 'library_contents_verified')),
            'Library access order, authority, or deployment evidence contract mismatch')
    require(router['bootstrap'] == {'full_file':['TK_CURRENT_SOURCE_INDEX.md','TK_OPEN_ISSUES_CURRENT.md'],
                                   'reconciliation_record':'TK_RECONCILIATION_RECORD.md',
                                   'record_read_when':['conflict','supersession','provenance','source replacement','authority','migration']},
            'Bootstrap contract mismatch')
    for name in router['bootstrap']['full_file'] + [router['bootstrap']['reconciliation_record']]:
        require(name in texts, f'Bootstrap outside admitted package: {name}')
        require(re.search(r'^Status: ACTIVE\r?$', texts[name], re.M), f'Inactive bootstrap: {name}')
    require(router['owners'] == {'required_header':list(FIELDS),'load_mode':'FULL_FILE','current_role':'CURRENT_SOURCE'},
            'Owner/header/load contract mismatch')
    selection = router['control_selection']
    require(selection == {'directory':'controls/anti_drift','files':'direct_children_only',
                          'version_order':'numeric','eligible_status':'ACTIVE',
                          'ambiguity':'SOURCE_LOAD_BLOCKED','load':'FULL_FILE'},
            'Overlay selection contract mismatch')
    graph = control_graph(router['controls'])
    require(set(router['core_controls']) == set(CORE), 'Missing/unknown core control')
    resolved = {'ROUTER': router_name}
    for key, row in router['core_controls'].items():
        require(isinstance(row, dict) and set(row) == {'stem','directory','path'}, 'Invalid core control contract')
        path = resolve_control(root, row['directory'], row['stem'])
        name = path.relative_to(root).as_posix()
        require(name == row['path'], f'Core reference does not select highest ACTIVE: {key}')
        require(control_metadata(path).get('Role') == CORE[key], f'Wrong core role: {key}')
        texts[name] = read(name)
        resolved[key] = name
    ci = texts[resolved['CI']]
    require(len(ci.replace('\r\n', '\n')) <= 8000, 'CI exceeds 8000 characters')
    version = control_metadata(root / resolved['CI'])['Version']
    require(version == router['ci_version'], 'CI/Router compatibility mismatch')
    require(ci.splitlines()[0] == f'# The Kingdom CI v{version} — ChatGPT Project Global Native v9.0 base',
            'CI title/semantic-base mismatch')
    require('8.9' not in ci and router_name.split('/')[-1] in ci and
            Path(resolved['PIPELINE']).name in ci, 'CI entry/pipeline/base reference mismatch')
    for key, row in graph.items():
        path = resolve_control(root, selection['directory'], row['stem'])
        metadata = control_metadata(path)
        require(metadata.get('Role') == 'REASONING_OVERLAY' and metadata.get('Control_ID') == key,
                f'Overlay identity mismatch: {key}')
        name = path.relative_to(root).as_posix()
        resolved[key] = name
        texts[name] = read(name)
    failures = {'bootstrap_missing':'SOURCE_LOAD_BLOCKED','owner_missing_or_ambiguous':'SOURCE_LOAD_BLOCKED',
                'temporal_basis_missing':'BLOCK_DEPENDENT_TRANSITION','source_unread':'SOURCE_LOAD_BLOCKED',
                'required_control_missing_or_ambiguous':'SOURCE_LOAD_BLOCKED',
                'control_conflict':'BLOCK_DEPENDENT_REASONING','secondary_nondecisive_gap':'SOURCE_LOAD_PARTIAL'}
    require(router['failures'] == failures, 'Failure behavior contract mismatch')
    policy_names = {'entry','prompt_route_only','bootstrap','owner_gate','temporal_gate','source_load',
                    'reconciliation','access','overlays','execution','pre_response'}
    require(set(router['policies']) == policy_names and
            all(isinstance(x,str) and x.strip() for x in router['policies'].values()), 'Missing/empty Router policy')
    for name, text in texts.items():
        if name.endswith(('.md', '.yaml')):
            require(not re.search(r'D:\\', text), f'Active absolute external path: {name}')

    # Detect active versioned controls outside declared families without walking archives.
    allowed_stems = {row['stem'] for row in graph.values()} | {'TK_ROUTER'} | {
        row['stem'] for row in router['core_controls'].values()}
    for directory in ('controls', 'controls/anti_drift'):
        for path in (root / directory).iterdir():
            if path.is_file() and re.match(r'TK_.*_v', path.name):
                metadata = control_metadata(path)
                if metadata.get('Status') == 'ACTIVE':
                    require(any(path.name.startswith(stem+'_v') for stem in allowed_stems),
                            f'Unregistered ACTIVE control family: {path.name}')

    index = 'TK_CURRENT_SOURCE_INDEX.md'
    table = '| SOURCE_ID | Path | ROLE | SCOPE |\n| --- | --- | --- | --- |\n'
    for sid, (name, fields) in sorted(sources.items()):
        table += f'| `{sid}` | `{name}` | {fields["ROLE"]} | {fields["SCOPE"].replace("|", "/")} |\n'
    table += '\n'
    new_index = replace_region(texts[index], 'GENERATED SOURCE CATALOG', table)
    # Links are checked on the prospective generated package; no archive content is read.
    prospective = dict(texts, **{index:new_index, 'MANIFEST.md':manifest})
    link_count, historical_links = check_links(root, prospective)
    hashes = '| File | SHA-256 |\n| --- | --- |\n'
    for name in sorted(texts):
        data = new_index.encode('utf-8') if name == index else inputs[name]
        hashes += f'| `{name}` | `{hashlib.sha256(data).hexdigest()}` |\n'
    hashes += '\n'
    new_manifest = replace_region(manifest, 'GENERATED HASHES', hashes)
    updates = {index:new_index.encode('utf-8'), 'MANIFEST.md':new_manifest.encode('utf-8')}
    updates = {name:data for name,data in updates.items() if inputs[name] != data}
    return {'root':root,'inputs':inputs,'updates':updates,'sources':sources,'resolved':resolved,
            'links':link_count,'historical_links':historical_links,'router':router}


def write_regions(plan):
    root, inputs, updates = plan['root'], plan['inputs'], plan['updates']
    require(set(updates) <= {'TK_CURRENT_SOURCE_INDEX.md','MANIFEST.md'}, 'Write outside allowlist')
    labels = {'TK_CURRENT_SOURCE_INDEX.md':'GENERATED SOURCE CATALOG','MANIFEST.md':'GENERATED HASHES'}
    for name,data in updates.items():
        old = inputs[name].decode('utf-8-sig')
        new = data.decode('utf-8')
        require(replace_region(old,labels[name],'') == replace_region(new,labels[name],''),
                f'Write outside generated region: {name}')
    temporary, prepared, backups, replaced = [], {}, {}, []

    def stage(name, data):
        fd, path = tempfile.mkstemp(prefix='.tk-maintenance-', dir=root)
        temporary.append(Path(path))
        with os.fdopen(fd,'wb') as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        return path
    try:
        for name,data in updates.items():
            prepared[name] = stage(name,data)
            backups[name] = stage(name,inputs[name])
        for name,data in inputs.items():
            require(safe_file(root,name).read_bytes() == data, f'Concurrent input change: {name}')
        try:
            for name in updates:
                os.replace(prepared[name],root/name)
                replaced.append(name)
        except OSError:
            for name in reversed(replaced):
                os.replace(backups[name],root/name)
            raise
    finally:
        for path in temporary:
            if path.exists():
                path.unlink()


def validate(root, write=False):
    plan = inspect(root)
    if write:
        write_regions(plan)
    else:
        require(not plan['updates'], 'Stale generated catalog/hashes: ' + ', '.join(plan['updates']))
    return plan


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--check',action='store_true',help='read-only check (default)')
    mode.add_argument('--write',action='store_true',help='update generated catalog/hash regions only')
    args = parser.parse_args(argv)
    try:
        plan = validate(Path(__file__).resolve().parents[1],write=args.write)
        print(f'STRUCTURAL PASS: {len(plan["sources"])} current owners; '
              f'{len(plan["resolved"])} controls; {plan["links"]} current links; '
              f'{plan["historical_links"]} provenance targets (archive bodies not read). '
              + ('Generated regions updated.' if args.write else 'Read-only check.')
              + ' No model execution or deployment.')
        return 0
    except (ValidationError,OSError,UnicodeError) as error:
        print(f'FAIL: {error}',file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())

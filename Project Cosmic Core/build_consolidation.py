#!/usr/bin/env python3
"""Validate the maintained current package; never reconstruct current sources."""

import argparse
import hashlib
import os
from pathlib import Path
import re
import sys
import tempfile


# Explicit admission: never derive identity from filename or iteration order.
ACCEPTED = {
    'C2M-001': '01_C2_ACTOR_ORGANIZATION_CATALOG_CURRENT.md',
    'C2M-002': '02_C2_CAPABILITY_RELIC_CATALOG_CURRENT.md',
    'C2M-006': '06_C2_PREMISE_CORE_CURRENT.md',
    'C2M-007': '07_C2_PREMISE_PROVENANCE_CURRENT.md',
    'C2M-010': '10_RONGO_CURRENT.md',
    'C2M-011': '11_TRAIN_STRUCTURE_CURRENT.md',
    'C2M-020': '20_TEAM_25_TAIYI_ZHENREN_CURRENT.md',
    'C2M-021': '21_CHARACTER_25_1_CURRENT.md',
    'C2M-022': '22_CHARACTER_25_2_CURRENT.md',
    'C2M-100': '100_WORLD_CATALOG_CURRENT.md',
    'C2M-110': '110_WORLD_001_CURRENT.md',
    'C2M-111': '111_WORLD_001_CAMPAIGN_01_BRIEFCASE_CURRENT.md',
}
MODULE_FILES = tuple(ACCEPTED.values())
INDEX = '00_C2_CONSOLIDATION_INDEX.md'
MANIFEST = 'MANIFEST.md'
CURRENT_FILES = (INDEX,) + MODULE_FILES + (
    '03_DESIGN_HISTORY_AND_RECONSIDERATIONS.md',
    '04_RECONCILIATION_RECORD.md',
    '05_OPEN_ISSUES_CURRENT.md',
)
FIELDS = ('Module ID', 'Runtime role', 'Domain / Scope',
          'Authority boundary', 'Cross-domain owner boundary', 'Load mode')
FORBIDDEN_HEADER_FIELDS = {'MODULE_REQUIRES', 'NODE_REQUIRES'}
CATALOG = 'MODULE CATALOG'
METADATA = 'PACKAGE METADATA'
HASHES = 'CURRENT HASHES'
METADATA_TEXT = '''## Current package maintenance

- Current root files are maintained directly within their declared source roles and scopes.
- `Source_Archive/` is historical/provenance material only, never a current build input, fallback source, or reconstruction authority.
- `build_consolidation.py` checks headers, catalog mappings, owner-reference IDs, and current-file hashes; it does not infer dependencies, validate semantic ownership, or reconstruct lore.
- Default / `--check` is read-only. `--write` updates only the generated catalog in `00` and generated metadata/hash regions in this manifest.
- The manifest grants no canon authority or automatic admission. Controls/tooling are checked separately, outside the numbered current-file hash set.
- Use Git history for provenance or explicitly authorized recovery.
'''


class ValidationError(ValueError):
    """Invalid package: no generated output may be written."""


def read_root(root, name):
    path = root / name
    if Path(name).name != name or path.is_symlink():
        raise ValidationError(f'Unsafe root source path: {name}')
    if not path.is_file() or path.resolve().parent != root.resolve():
        raise ValidationError(f'Missing or redirected root source: {name}')
    return path.read_bytes()


def header(data, name):
    lines = data.decode('utf-8-sig').splitlines()
    if not lines or not lines[0].startswith('# '):
        raise ValidationError(f'{name}: missing initial H1')
    # Inspect the initial header block, including prose the field parser skips.
    # Later body blockquotes are not module metadata.
    in_header = False
    for line in lines[1:]:
        if not line.strip() and not in_header:
            continue
        if not line.startswith('>'):
            break
        in_header = True
        match = re.fullmatch(r'>\s*([^:]+):\s*(.*)', line)
        if match and match[1].strip() in FORBIDDEN_HEADER_FIELDS:
            raise ValidationError(f'{name}: unapproved structural header field {match[1].strip()}')
    values = {}
    started = False
    for line in lines[1:]:
        if not line.strip() and not started:
            continue
        match = re.fullmatch(r'> ([^:]+):\s*(.*)', line)
        if not match or match[1] not in FIELDS:
            break
        started = True
        field, value = match.groups()
        if field in values or not value.strip():
            raise ValidationError(f'{name}: duplicate or empty header field {field}')
        values[field] = value.strip()
    if set(values) != set(FIELDS):
        raise ValidationError(f'{name}: missing required header fields')
    for field in ('Module ID', 'Runtime role', 'Load mode'):
        if not re.fullmatch(r'`[^`]+`', values[field]):
            raise ValidationError(f'{name}: invalid {field} syntax')
        values[field] = values[field][1:-1]
    if not re.fullmatch(r'C2M-\d{3}', values['Module ID']):
        raise ValidationError(f'{name}: invalid Module ID')
    if values['Runtime role'] != 'CURRENT_SOURCE':
        raise ValidationError(f'{name}: Runtime role must be CURRENT_SOURCE')
    if values['Load mode'] != 'FULL_FILE':
        raise ValidationError(f'{name}: accepted Load mode is FULL_FILE')
    refs = set(re.findall(r'\bC2M-\d+\b', values['Cross-domain owner boundary']))
    if refs - ACCEPTED.keys():
        raise ValidationError(f'{name}: unknown cross-domain C2M references {sorted(refs - ACCEPTED.keys())}')
    return values


def region(data, label):
    begin = f'<!-- BEGIN GENERATED {label} -->'.encode()
    end = f'<!-- END GENERATED {label} -->'.encode()
    if data.count(begin) != 1 or data.count(end) != 1:
        raise ValidationError(f'{label}: exactly one begin/end marker required')
    pattern = (rb'(?m)^' + re.escape(begin) + rb'(\r?\n)(.*?)^'
               + re.escape(end) + rb'(?=\r?$)')
    match = re.search(pattern, data, re.DOTALL)
    if match is None:
        raise ValidationError(f'{label}: malformed or unordered markers')
    return match.start(2), match.end(2), match[1], match[2]


def replace_region(data, label, content):
    start, end, newline, _ = region(data, label)
    return data[:start] + content.replace('\n', newline.decode()).encode() + data[end:]


def rows(block, title, columns):
    lines = block.decode().splitlines()
    table = [line for line in lines if line.startswith('|')]
    if len(table) < 2 or table[:2] != [title, '| --- | --- |']:
        raise ValidationError('Missing or invalid two-column table')
    entries = {}
    for line in table[2:]:
        match = re.fullmatch(r'\| `([^`]+)` \| `([^`]+)` \|', line)
        if not match or match[1] in entries:
            raise ValidationError('Malformed or duplicate table row')
        entries[match[1]] = match[2]
    if set(entries) != set(columns):
        raise ValidationError('Table must contain exactly the accepted entries')
    return entries


def catalog_text(modules):
    text = '''## Runtime Module Catalog

> Derived routing index only. A row grants no canon authority, automatic
> admission, or dependency. Check the source header and package state before
> using a module. This table does not change the reading order above.

| Module ID | Current source path (relative to Project Cosmic Core/) |
| --- | --- |
'''
    return text + ''.join(f'| `{key}` | `{modules[key]}` |\n'
                          for key in sorted(modules)) + '\n'


def plan(root, write=False):
    """Validate all inputs before producing an allowlisted write plan."""
    inputs = {name: read_root(root, name) for name in CURRENT_FILES + (MANIFEST,)}
    modules = {}
    for name in MODULE_FILES:
        values = header(inputs[name], name)
        key = values['Module ID']
        if key in modules or ACCEPTED.get(key) != name:
            raise ValidationError(f'{name}: duplicate ID or ID/path mismatch: {key}')
        modules[key] = name
    # Discovery is deliberately restricted to root Markdown, never subdirectories.
    for path in sorted(root.glob('*.md')):
        if path.name in inputs:
            continue
        data = read_root(root, path.name)
        inputs[path.name] = data
        if re.search(rb'(?m)^> Runtime role:\s*`?CURRENT_SOURCE`?\s*\r?$', data):
            raise ValidationError(f'Unexpected CURRENT_SOURCE; not admitted: {path.name}')
    _, _, _, block = region(inputs[INDEX], CATALOG)
    catalog_rows = rows(block,
                        '| Module ID | Current source path (relative to Project Cosmic Core/) |',
                        modules)
    if catalog_rows != modules:
        raise ValidationError('Catalog Module ID/source path does not match current headers')
    new_index = replace_region(inputs[INDEX], CATALOG, catalog_text(modules))
    manifest = inputs[MANIFEST]
    region(manifest, METADATA)
    _, _, _, block = region(manifest, HASHES)
    previous_hashes = rows(block, '| File | SHA-256 |', CURRENT_FILES)
    if any(not re.fullmatch(r'[0-9A-F]{64}', value) for value in previous_hashes.values()):
        raise ValidationError('Invalid current hash syntax')
    current = dict(inputs)
    current[INDEX] = new_index
    hash_text = '## Current file hashes\n\n| File | SHA-256 |\n| --- | --- |\n'
    hash_text += ''.join(f'| `{name}` | `{hashlib.sha256(current[name]).hexdigest().upper()}` |\n'
                         for name in CURRENT_FILES) + '\n'
    new_manifest = replace_region(manifest, METADATA, METADATA_TEXT + '\n')
    new_manifest = replace_region(new_manifest, HASHES, hash_text)
    outputs = {INDEX: new_index, MANIFEST: new_manifest}
    changes = {name: data for name, data in outputs.items() if inputs[name] != data}
    if changes and not write:
        raise ValidationError(f'Generated catalog/metadata or current hashes are stale: {", ".join(changes)}')
    return inputs, changes


def atomic_write(root, inputs, changes):
    """Stage every file, then replace; roll back handled replacement failures.

    Each replacement is atomic, but the pair is not a power-loss transaction.
    A subsequent --check detects an interrupted index/manifest update.
    """
    if set(changes) - {INDEX, MANIFEST}:
        raise ValidationError('Write outside allowed generated files')
    for name, data in changes.items():
        labels = (CATALOG,) if name == INDEX else (METADATA, HASHES)
        masked_old, masked_new = inputs[name], data
        for label in labels:
            masked_old = replace_region(masked_old, label, '')
            masked_new = replace_region(masked_new, label, '')
        if masked_old != masked_new:
            raise ValidationError(f'{name}: attempted write outside generated regions')
    staged, backups, replaced, temporary = {}, {}, [], []

    def stage(name, data):
        descriptor, filename = tempfile.mkstemp(prefix='.c2-maintenance-', dir=root)
        temporary.append(Path(filename))
        with os.fdopen(descriptor, 'wb') as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(filename, (root / name).stat().st_mode)
        return filename

    try:
        for name, data in changes.items():
            staged[name] = stage(name, data)
            backups[name] = stage(name, inputs[name])
        for name, original in inputs.items():
            if read_root(root, name) != original:
                raise ValidationError(f'Concurrent source change: {name}')
        try:
            for name in changes:
                os.replace(staged[name], root / name)
                replaced.append(name)
        except OSError:
            for name in reversed(replaced):
                os.replace(backups[name], root / name)
            raise
    finally:
        for path in temporary:
            if path.exists():
                path.unlink()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--check', action='store_true', help='validate without writing (default)')
    mode.add_argument('--write', action='store_true', help='sync only generated catalog/manifest regions')
    mode.add_argument('--check-router', action='store_true', help='read-only C2 control checks')
    args = parser.parse_args(argv)
    try:
        root = Path(__file__).resolve().parent
        if args.check_router:
            from tools.check_controls import ControlError, check
            try:
                resolved = check(root)
            except ControlError as error:
                raise ValidationError(str(error)) from error
            print(f'PASS: C2 CI 1.0 / Router 1.0; {len(resolved)} control families. '
                  'Static only; no prompt execution or deployment.')
            return 0
        inputs, changes = plan(root, write=args.write)
        if args.write:
            atomic_write(root, inputs, changes)
        print(f'PASS: {len(MODULE_FILES)} current modules; {len(CURRENT_FILES)} current hashes; archive not accessed. '
              + (f'Updated: {", ".join(changes) or "none"}.' if args.write else 'Read-only check.'))
        return 0
    except (ValidationError, OSError, UnicodeError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())

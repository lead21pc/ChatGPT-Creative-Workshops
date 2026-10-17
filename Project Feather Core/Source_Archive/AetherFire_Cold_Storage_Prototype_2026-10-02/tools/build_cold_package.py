#!/usr/bin/env python3
"""Offline storage packaging only; no runtime cache, source admission, or lore edits."""
import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = 'Cold Storage/AETHERFIRE_COLD_PACKAGE.md'
COLD = (
    '91_RECONCILIATION_RECORD.md',
    '90_DESIGN_HISTORY_AND_RECONSIDERATIONS.md',
    'Anti-Drift Source/AetherFire_Anti_Drift_Interface_Economy_State_Stabilization_v1.1.md',
    'Anti-Drift Source/AetherFire_Anti_Drift_Modular_Concept_Architecture_v1.0.md',
    'Anti-Drift Source/AetherFire_Anti_Drift_Mortality_Relationship_Plot_Immunity_v1.1.md',
    'Anti-Drift Source/AetherFire_Anti_Drift_Total_War_RP_v1.1.md',
    'Anti-Drift Source/AetherFire_Anti_Drift_Worldbuilding_Internal_Logic_v1.1.md',
)
HOT = (
    '10_WORLD_INSTITUTIONS_GEOPOLITICS_CURRENT.md',
    '20_STATUS_CIVIL_LABOR_CURRENT.md',
    '30_UNDIE_SYSTEM_CURRENT.md',
    '40_METAFICTION_CANON_TIMELINE_CURRENT.md',
    '50_NARRATORS_POV_AND_HUMOR_CURRENT.md',
    '60_MC4_IDENTITY_CURRENT.md',
    '70_MATRIARCHS_LAMENT_CURRENT.md',
    '80_STABLE_AVIATION_RF_AIRSPACE_CURRENT.md',
    '92_OPEN_ISSUES_CURRENT.md',
)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def manifest(root=ROOT):
    def entry(path, role):
        data = (root / path).read_bytes()
        return dict(identity=Path(path).name, authoring_path=path, role=role,
                    bytes=len(data), sha256=sha(data))
    sources = [entry(p, 'RECONCILIATION' if p.startswith('91') else
                     'MIXED_HISTORY' if p.startswith('90') else 'OVERLAY') for p in COLD]
    hot = [entry(p, 'HOT') for p in HOT]
    payload = dict(format='AF-COLD-1', sources=sources, hot=hot)
    generation = sha(json.dumps(payload, sort_keys=True, separators=(',', ':')).encode())
    return dict(generation=generation, **payload)

def build(root=ROOT):
    m = manifest(root)
    prefix = ('# AetherFire Cold Package\n\n'
              '> STORAGE CONSOLIDATION ONLY. Loading is not admission or overlay activation.\n'
              '> Every logical source retains its original identity, full payload, authority,\n'
              '> truth status, exclusions, dependencies and provenance. No archive fallback.\n\n'
              '<!-- AF-COLD-MANIFEST -->\n```json\n' + json.dumps(m, indent=2) +
              '\n```\n<!-- END AF-COLD-MANIFEST -->\n\n')
    data = prefix.encode()
    for number, entry in enumerate(m['sources'], 1):
        identity = entry['identity']
        data += f'## PART {number} — {identity}\n\n<!-- BEGIN LOGICAL SOURCE {identity} -->\n'.encode()
        data += (root / entry['authoring_path']).read_bytes()
        data += f'\n<!-- END LOGICAL SOURCE {identity} -->\n\n'.encode()
    data += b'<!-- END COMPLETE AETHERFIRE COLD PACKAGE -->\n'
    return data

def validate(data, expected_hash=None, expected_generation=None):
    if expected_hash is not None and sha(data) != expected_hash:
        raise ValueError('Package digest mismatch')
    marker = b'<!-- AF-COLD-MANIFEST -->\n```json\n'
    if data.count(marker) != 1:
        raise ValueError('Missing/duplicate package manifest')
    start = data.index(marker) + len(marker)
    end = data.index(b'\n```\n<!-- END AF-COLD-MANIFEST -->\n\n', start)
    m = json.loads(data[start:end])
    if m['format'] != 'AF-COLD-1':
        raise ValueError('Unsupported package format')
    payload = {k: m[k] for k in ('format', 'sources', 'hot')}
    generation = sha(json.dumps(payload, sort_keys=True, separators=(',', ':')).encode())
    if generation != m['generation'] or (expected_generation and generation != expected_generation):
        raise ValueError('Generation mismatch')
    if len(m['sources']) != len(COLD) or [x['authoring_path'] for x in m['sources']] != list(COLD):
        raise ValueError('Required source missing, duplicated or reordered')
    cursor = end + len(b'\n```\n<!-- END AF-COLD-MANIFEST -->\n\n')
    loaded = {}
    for number, entry in enumerate(m['sources'], 1):
        identity = entry['identity']
        if identity != Path(entry['authoring_path']).name or identity in loaded:
            raise ValueError('Logical identity mismatch')
        opening = f'## PART {number} — {identity}\n\n<!-- BEGIN LOGICAL SOURCE {identity} -->\n'.encode()
        if data[cursor:cursor + len(opening)] != opening:
            raise ValueError('Source boundary mismatch')
        cursor += len(opening)
        body = data[cursor:cursor + entry['bytes']]
        if len(body) != entry['bytes'] or sha(body) != entry['sha256']:
            raise ValueError('Partial/corrupt logical source')
        cursor += len(body)
        closing = f'\n<!-- END LOGICAL SOURCE {identity} -->\n\n'.encode()
        if data[cursor:cursor + len(closing)] != closing:
            raise ValueError('Source boundary mismatch')
        cursor += len(closing)
        loaded[identity] = body
    if data[cursor:] != b'<!-- END COMPLETE AETHERFIRE COLD PACKAGE -->\n':
        raise ValueError('Partial package or unexpected trailing content')
    return m, loaded

def check(root=ROOT):
    data = (root / PACKAGE).read_bytes()
    if data != build(root):
        raise ValueError('Stale package: regenerate and publish a new pinned generation')
    m, _ = validate(data)
    index = (root / '00_AETHERFIRE_CONSOLIDATION_INDEX.md').read_text()
    for field, value in (('Cold generation', m['generation']), ('Cold SHA-256', sha(data)),
                         ('Cold bytes', str(len(data)))):
        if f'> {field}: `{value}`' not in index:
            raise ValueError(f'Index/package mismatch: {field}')
    if not re.search(r'^> Cold ref: `[0-9a-f]{40}`$', index, re.M):
        raise ValueError('Cold ref must be a published commit SHA')
    return m

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='write package only; never update sources or refs')
    args = parser.parse_args()
    if args.write:
        path = ROOT / PACKAGE
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(build())
        print('Package generated. Publish first, then pin SHA/digest/generation in 00; refresh manifest.')
    else:
        check()
        print('PASS: cold package, logical source bytes and hot/index generation bindings')

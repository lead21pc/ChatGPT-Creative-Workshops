"""Checks of current source, binding and composition contracts; no model execution."""
import hashlib
from pathlib import Path
import re
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
LIBRARY = ROOT / 'library_modules'
ROOT_CATALOG = ROOT / 'HUB_PACKAGE_CATALOG_v1.22.yaml'
HUB_ROUTER = ROOT / 'HUB_ROUTER_v1.2.yaml'
ARCHITECTURE = ROOT / 'HUB_ARCHITECTURE_v1.22.md'
CI = ROOT / 'HUB_CI_v1.3.md'
IMAGE_INSTALL = ROOT / 'tool_pipelines/ImageT/IMAGET_INSTALL_INTEGRITY.yaml'


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


def read_identity(path):
    if path.suffix == '.yaml':
        return load(path)
    text = path.read_text(encoding='utf-8')
    names = {'module_id': 'Module ID', 'package_id': 'Package ID',
             'runtime_role': 'Runtime role', 'status': 'Status', 'version': 'Version'}
    result = {}
    for key, name in names.items():
        values = re.findall(r'^' + re.escape(name) + r': (.+)$', text, re.M)
        if len(values) != 1:
            raise Closed('missing/duplicate header')
        result[key] = values[0]
    return result


def package(name):
    return next(row for row in load(ROOT_CATALOG)['packages'] if row['package_id'] == f'HUB-PKG-{name}')


def entry_path(row):
    return LIBRARY / row['location']['artifact']


def check_binding(row, identity, path):
    header = read_identity(path)
    expected = {key: row[key] for key in ('package_id', 'runtime_role', 'status', 'version')}
    expected['module_id'] = identity
    if any(header[key] != value for key, value in expected.items()):
        raise Closed('Library binding/header mismatch')
    if path.name != f"{identity}_v{row['version']}{path.suffix}":
        raise Closed('incorrect install filename')
    return header


def closure(rows, roots):
    """SPEC-only hard edge expansion for declared current inventory."""
    done, visiting = set(), set()

    def visit(identity):
        if identity in visiting or identity not in rows:
            raise Closed('missing or cyclic required control')
        if identity in done:
            return
        visiting.add(identity)
        for row in rows[identity].get('requires', []):
            visit(row['module_id'])
        visiting.remove(identity)
        done.add(identity)

    for identity in roots:
        visit(identity)
    return done


class HubContracts(unittest.TestCase):
    def test_exact_shared_pins_and_ci_owner(self):
        router = load(HUB_ROUTER)
        self.assertEqual(router['contracts']['ci'], CI.name)
        self.assertIn(HUB_ROUTER.name, CI.read_text(encoding='utf-8'))
        for key, path in [('architecture', ARCHITECTURE), ('root_catalog', ROOT_CATALOG)]:
            pin = router['contracts'][key]
            self.assertEqual(pin['file'], path.name)
            if path.suffix == '.yaml':
                body = load(path)
                for field in ('module_id', 'version', 'status'):
                    self.assertEqual(body[field], pin[field])
            else:
                for header, field in [('Module ID', 'module_id'), ('Version', 'version'), ('Status', 'status')]:
                    self.assertIn(f'{header}: {pin[field]}', path.read_text(encoding='utf-8'))
        body = CI.read_text(encoding='utf-8')
        for rule in ('CONTROL GROUNDING', 'DISCOURSE FIDELITY', 'EPISTEMIC NON-ESCALATION',
                     'Local mutation requires separate explicit user implementation authorization',
                     'CONTROL != EXECUTION', 'EXPLANATION'):
            self.assertIn(rule, body)

    def test_current_inventory_and_shallow_layout(self):
        packages = load(ROOT_CATALOG)['packages']
        self.assertEqual(len({row['package_id'] for row in packages}), len(packages))
        self.assertEqual({row['package_id'].removeprefix('HUB-PKG-') for row in packages},
                         {'TECHNICAL', 'FOOD', 'AIS', 'AUTHORING', 'IMAGET', 'CONCEPT-DEVELOPMENT', 'SHOPPING'})
        bound = set()
        identities = set()

        def admit(row, key='module_id', path=None):
            identity = row[key]
            path = path or entry_path(row)
            self.assertNotIn(identity, identities)
            self.assertEqual(len(path.relative_to(LIBRARY).parts), 2)
            check_binding(row, identity, path)
            bound.add(path)
            identities.add(identity)
            return path

        for row in packages:
            if row['binding_mode'] == 'LEGACY_PROJECT_SOURCE':
                self.assertEqual(row['package_id'], 'HUB-PKG-AIS')
                source = ROOT / row['location']['declared_source_path']
                self.assertEqual(row['location']['source_name'], source.name)
                self.assertIn(f'AIS pipeline v{row["version"]}', source.read_text(encoding='utf-8'))
                self.assertEqual(list(source.parent.glob('AIS_*_v*')), [source])
                continue
            self.assertEqual(row['binding_mode'], 'LIBRARY_MODULE')
            self.assertEqual(row['location']['root'], 'Central Hub Config')
            admit(row, 'entrypoint_module_id')
            if row['local_catalog']:
                catalog = admit(row['local_catalog'])
                entries = load(catalog)['entries']
                local = {entry['module_id']: entry for entry in entries}
                self.assertEqual(len(entries), len(local))
                closure(local, local)
                for leaf in entries:
                    self.assertEqual(leaf['package_id'], row['package_id'])
                    self.assertEqual(leaf['location']['root'], 'Central Hub Config')
                    admit(leaf)
        for row in load(IMAGE_INSTALL)['core']:
            admit(row, path=LIBRARY / row['file'])
        shop = package('SHOPPING')
        self.assertIsNone(shop['local_catalog'])
        match = re.search(r'Select (HUB-SHOP-SEARCH) / (HUB-PKG-SHOPPING) / (DOMAIN_PROCEDURE) / (ACTIVE) / ([\d.]+)', entry_path(shop).read_text(encoding='utf-8'))
        self.assertIsNotNone(match)
        identity, owner, role, status, version = match.groups()
        admit(dict(module_id=identity, package_id=owner, runtime_role=role, status=status, version=version),
              path=LIBRARY / 'Shopping' / f'{identity}_v{version}.md')
        self.assertEqual(bound, {p for p in LIBRARY.rglob('*') if p.is_file()})

    def test_binding_mismatches_and_hard_closure_fail(self):
        row = package('TECHNICAL')
        for field, value in [('package_id', 'other'), ('version', 'old'),
                             ('runtime_role', 'PREFERENCE'), ('status', 'INACTIVE')]:
            with self.subTest(field=field), self.assertRaises(Closed):
                check_binding(dict(row, **{field: value}), row['entrypoint_module_id'], entry_path(row))
        with self.assertRaises(Closed):
            closure({'a': {'requires': [{'module_id': 'b'}]}}, ['a'])
        with self.assertRaises(Closed):
            closure({'a': {'requires': [{'module_id': 'a'}]}}, ['a'])

    def test_yaml_conservative_and_rejects_bad_inputs(self):
        for p in ROOT.rglob('*.yaml'):
            if 'Source_archive' not in p.parts:
                self.assertIsInstance(load(p), dict)
        for text in ['a: 1\na: 2', 'a: &x 1\nb: *x', '<<: {}', 'a: yes', 'a: FALSE', 'a: ~', 'a: 2026-10-17', 'a: !custom x']:
            with self.assertRaises((Closed, yaml.YAMLError)):
                parse(text)

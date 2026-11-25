"""Checks of current source, binding and composition contracts; no model execution."""
import hashlib
from pathlib import Path
import re
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_SOURCES = ROOT / 'library_modules'
ROOT_CATALOG = ROOT / 'HUB_PACKAGE_CATALOG_v2.2.yaml'
HUB_ROUTER = ROOT / 'HUB_ROUTER_v2.1.yaml'
ARCHITECTURE = ROOT / 'HUB_ARCHITECTURE_v2.2.md'
CI = ROOT / 'HUB_CI_v2.1.md'


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
    return ROOT / row['source']


def media_leaf_bindings():
    body = entry_path(package('MEDIA')).read_text(encoding='utf-8')
    return re.findall(r'^\| (HUB-MEDIA-(?:MOVIE|MUSIC)) \| (\w+) \| (\w+) \| ([\d.]+) \| (\S+) \|$',
                      body, re.M)


def check_binding(row, identity, path):
    header = read_identity(path)
    expected = {key: row[key] for key in ('package_id', 'runtime_role', 'status', 'version')}
    expected['module_id'] = identity
    if any(header[key] != value for key, value in expected.items()):
        raise Closed('Source binding/header mismatch')
    if path.name != f"{identity}_v{row['version']}{path.suffix}":
        raise Closed('incorrect artifact filename')
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
        self.assertIn(ROOT_CATALOG.name, ARCHITECTURE.read_text(encoding='utf-8'))
        body = CI.read_text(encoding='utf-8')
        for rule in ('OUTPUT / EXPLANATION', 'OPERATION / STAGE / AUTHORITY',
                     'CLAIM / EVIDENCE / UPDATE', 'ACTION / OBSERVED RESULT', 'SPECIALIZATION',
                     'QUESTION != APPROVAL', 'AUDIT OR TEST != REMEDIATION AUTHORITY',
                     'IMPLEMENTATION != COMMIT != PUSH', 'Current explicit input prevails'):
            self.assertIn(rule, body)

    def test_vietnamese_language_guard_is_first_and_explicit(self):
        body = CI.read_text(encoding='utf-8')
        output, separator, _ = body.partition('\nOPERATION / STAGE / AUTHORITY\n')
        self.assertTrue(separator)
        self.assertEqual(output.splitlines()[0], 'OUTPUT / EXPLANATION')
        self.assertTrue(output.splitlines()[2].startswith('Use everyday, direct and concrete Vietnamese'))
        for rule in (
            'English is allowed only for proper names, code, literal quotes, commands, '
            'exact external identifiers, or forms explicitly requested by the user.',
            'Field or technical terminology alone is not an identifier.',
            'Familiarity with English terms grants no permission to mix languages or raise the register.',
            'Translate all other English, including technical terms used in prose.',
            'Use bilingual labels only when explicitly requested or when exact identity requires the English form.',
            'Explain necessary terms plainly at first use.',
            'Before sending, silently scan the full response and rewrite all language violations.',
        ):
            with self.subTest(rule=rule):
                self.assertIn(rule, output)
        self.assertNotIn('without lookup', output)

    def test_exact_current_source_inventory(self):
        catalog = load(ROOT_CATALOG)
        packages = catalog['packages']
        self.assertNotIn('library_discovery_root', catalog)
        self.assertEqual(len(packages), 5)
        self.assertEqual({row['package_id'].removeprefix('HUB-PKG-') for row in packages},
                         {'TECHNICAL', 'FOOD', 'MEDIA', 'AUTHORING', 'SHOPPING'})
        bound = set()
        identities = set()

        def admit(row, identity):
            path = entry_path(row)
            self.assertTrue(path.resolve().is_relative_to(PACKAGE_SOURCES))
            self.assertNotIn(identity, identities)
            self.assertNotIn(path, bound)
            check_binding(row, identity, path)
            identities.add(identity)
            bound.add(path)

        for row in packages:
            self.assertEqual(set(row), {'package_id', 'entrypoint_module_id', 'runtime_role',
                                        'status', 'version', 'applicability', 'source', 'requires'})
            admit(row, row['entrypoint_module_id'])
        match = re.search(
            r'Select (HUB-SHOP-SEARCH) / (HUB-PKG-SHOPPING) / (DOMAIN_PROCEDURE) / (ACTIVE) / ([\d.]+)'
            r'[^.]*\. Its exact source is (\S+\.md)\.',
            entry_path(package('SHOPPING')).read_text(encoding='utf-8'),
        )
        self.assertIsNotNone(match)
        identity, owner, role, status, version, source = match.groups()
        admit(dict(package_id=owner, runtime_role=role, status=status,
                   version=version, source=source), identity)
        media = package('MEDIA')
        for identity, role, status, version, source in media_leaf_bindings():
            admit(dict(package_id=media['package_id'], runtime_role=role, status=status,
                       version=version, source=source), identity)
        self.assertEqual(bound, {p for p in PACKAGE_SOURCES.rglob('*') if p.is_file()})

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

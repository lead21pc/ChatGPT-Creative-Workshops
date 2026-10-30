"""Bounded release extraction checks, not a runtime router or model evaluator."""
from pathlib import Path
import hashlib
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile
import yaml

DIST = Path(__file__).resolve().parents[1]
ROOT = DIST.parent
FTH = 'FTH-Control-Pack'
HUB = 'Central-Hub-Architecture-Pack'
VERSION = '0.1.0'
PROTECTED = {'Project Feather Core': 'a9892aca5e0552f8901a66cef36b4bb8d9c47c766b111aab735ad556ef6601d2', 'Central Hub': '59f3b458866bbe14559248ae6e808918c61f326d58a34ca944c2971631667067'}
FILES = {
    FTH: {'README.md', 'LICENSE', 'RELEASE_NOTES.md', 'controls/project-instructions.md',
          'controls/source-router.yaml', 'controls/authoring-pipeline.md',
          'optional/modular-concept-architecture_v1.0.md', 'tests/SCENARIOS.md'},
    HUB: {'README.md', 'LICENSE', 'RELEASE_NOTES.md', 'ARCHITECTURE.md',
          'starter/hub-ci.md', 'starter/hub-router.yaml', 'starter/root-catalog.yaml',
          'starter/packages/HUB-DOM-TECHNICAL_v1.0.md', 'tests/SCENARIOS.md'},
}
TOKEN = re.compile(r'\{\{[A-Z_]+\}\}')
ARCHIVES = None


class UniqueLoader(yaml.SafeLoader):
    def construct_mapping(self, node, deep=False):
        result = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if key in result or key == '<<':
                raise ValueError('duplicate or merge key')
            result[key] = self.construct_object(value_node, deep=deep)
        return result


def text(pack, path):
    return (DIST / pack / path).read_text(encoding='utf-8')


def load(pack, path):
    return yaml.load(text(pack, path), Loader=UniqueLoader)


def configured(content, values):
    result = content
    for token, value in values.items():
        result = result.replace(token, value)
    if TOKEN.search(result):
        raise ValueError('unresolved mandatory placeholder')
    return result


def protected_digest(folder):
    paths = subprocess.check_output(['git', 'ls-files', '-z', '--', folder], cwd=ROOT).decode().split('\0')
    result = hashlib.sha256()
    for path in sorted(p for p in paths if p):
        result.update(path.encode() + b'\0' + (ROOT / path).read_bytes() + b'\0')
    return result.hexdigest()


class ReleasePackTests(unittest.TestCase):
    def test_exact_inventory_no_outside_content_or_symlinks(self):
        expected = {'.gitattributes', 'PACKAGING.md', 'tests/test_release_packs.py'}
        for pack, paths in FILES.items():
            actual = set()
            for path in (DIST / pack).rglob('*'):
                self.assertFalse(path.is_symlink(), str(path))
                if path.is_file():
                    actual.add(path.relative_to(DIST / pack).as_posix())
            self.assertEqual(actual, paths)
            expected.update(pack + '/' + path for path in paths)
        actual = {p.relative_to(DIST).as_posix() for p in DIST.rglob('*') if p.is_file()}
        self.assertEqual(actual, expected)
        self.assertFalse(any(re.search(r'(^|/)(\.git|source_archive|public-release-integration)(/|$)', p, re.I) for p in actual))

    def test_internal_markdown_links_stay_inside_each_archive(self):
        for pack, paths in FILES.items():
            base = (DIST / pack).resolve()
            for name in paths:
                if not name.endswith('.md'):
                    continue
                for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text(pack, name)):
                    if re.match(r'https?://|#', target):
                        continue
                    resolved = (base / Path(name).parent / target.split('#')[0]).resolve()
                    self.assertTrue(resolved.is_relative_to(base), (name, target))
                    self.assertTrue(resolved.is_file(), (name, target))

    def test_licenses_and_small_root_readme_correction(self):
        for pack in FILES:
            self.assertEqual((DIST / pack / 'LICENSE').read_bytes(), (ROOT / 'LICENSE').read_bytes())
            self.assertIn('MIT', text(pack, 'README.md'))
        expected = subprocess.check_output(['git', 'show', '8a379a047445a0e63392181d2795b4ade38ac7d6:README.md'], cwd=ROOT).decode('utf-8')
        self.assertEqual((ROOT / 'README.md').read_text(encoding='utf-8'), expected)
        self.assertNotIn('No license is granted', expected)

    def test_protected_sources_unchanged_and_write_scope(self):
        for folder, digest in PROTECTED.items():
            self.assertEqual(protected_digest(folder), digest, folder)
        for args in (['git', '-c', 'core.longpaths=true', 'diff', '--name-only'], ['git', '-c', 'core.longpaths=true', 'diff', '--cached', '--name-only']):
            changed = subprocess.check_output(args, cwd=ROOT, text=True).splitlines()
            self.assertTrue(all(p == 'README.md' or p.startswith('distribution/') for p in changed), changed)

    def test_yaml_parses_and_duplicate_keys_are_rejected(self):
        for pack, path in [(FTH, 'controls/source-router.yaml'), (HUB, 'starter/hub-router.yaml'), (HUB, 'starter/root-catalog.yaml')]:
            self.assertIsInstance(load(pack, path), dict)
        with self.assertRaises(ValueError):
            yaml.load('root: one\nroot: two\n', Loader=UniqueLoader)

    def test_all_mandatory_tokens_documented_detected_and_configurable(self):
        expected = {
            FTH: {'PROJECT_NAME', 'OUTPUT_LANGUAGE', 'SOURCE_ROUTER_PATH', 'AUTHORING_PIPELINE_PATH',
                  'PROJECT_INSTRUCTIONS_PATH', 'DISCOVERY_BINDING', 'OPEN_STATE_BINDING',
                  'RECONCILIATION_BINDING', 'SOURCE_OWNERSHIP', 'SOURCE_STORAGE_BINDING', 'OPTIONAL_CONTROL_DIRECTORY'},
            HUB: {'OUTPUT_LANGUAGE', 'LIBRARY_ROOT'},
        }
        for pack, names in expected.items():
            controls = [name for name in FILES[pack] if name.startswith(('controls/', 'optional/', 'starter/')) or name == 'ARCHITECTURE.md']
            content = '\n'.join(text(pack, name) for name in sorted(controls))
            tokens = set(TOKEN.findall(content))
            self.assertEqual(tokens, {'{{' + name + '}}' for name in names})
            for token in tokens:
                self.assertIn('`' + token + '`', text(pack, 'README.md'))
            with self.assertRaisesRegex(ValueError, 'unresolved'):
                configured(content, {})
            with self.assertRaisesRegex(ValueError, 'unresolved'):
                configured(content, {token: 'configured-value' for token in sorted(tokens)[1:]})
            self.assertFalse(TOKEN.search(configured(content, {token: 'configured-value' for token in tokens})))

    def test_fth_core_has_no_lore_paths_or_world_names(self):
        for name in FILES[FTH]:
            if not name.startswith(('controls/', 'optional/')):
                continue
            content = text(FTH, name)
            self.assertNotRegex(content, r'(?i)AetherFire|Hoa\s*Nguy[eệ]t|\bUndie?\b|\bRF\b|\bAFM[-_]|\bMC[1-9]|Project Feather Core|\bFTH\b')
            self.assertNotRegex(content, r'(?i)(?:00|9[012])_[A-Z_]+\.md|Source_Archive|source_archive|[A-Z]:[\\/]Users')

    def test_fth_role_bindings_do_not_require_record_files(self):
        router = load(FTH, 'controls/source-router.yaml')
        bootstrap = router['bootstrap']
        self.assertEqual(set(bootstrap), {'discovery', 'open_state', 'reconciliation', 'source_ownership', 'same_current_generation', 'read_when', 'binding_contract'})
        self.assertIn('owner/path/mechanism', bootstrap['binding_contract'])
        self.assertIn('no separate file', bootstrap['binding_contract'])
        self.assertNotIn('reconciliation_record', bootstrap)
        policy = router['policies']['loading']
        for term in ('conflict', 'supersession/replacement', 'provenance', 'priority', 'authority', 'completely'):
            self.assertIn(term, policy)
        self.assertIn('not admission or read proof', bootstrap['binding_contract'])
        self.assertIn('neither grants authority', router['policies']['discovery'])
        self.assertIn('Retain UNKNOWN, DEFERRED, CONFLICTED', router['policies']['authority'])
        # Two distinct recipient arrangements configure the same roles, no record filename needed.
        for reconciliation in ('Owner manual, decision section; full content supplied by author', 'Review mechanism owned by author, exact accepted decision packet read in full'):
            values = {token: 'Recipient supplied role' for token in TOKEN.findall(text(FTH, 'controls/source-router.yaml'))}
            values['{{RECONCILIATION_BINDING}}'] = reconciliation
            configured_router = yaml.load(configured(text(FTH, 'controls/source-router.yaml'), values), Loader=UniqueLoader)
            self.assertEqual(configured_router['bootstrap']['reconciliation'], reconciliation)

    def test_fth_router_stages_loading_and_failure_contracts_preserved(self):
        source = yaml.safe_load((ROOT / 'Project Feather Core/Anti-Drift Source/FTH_Anti_Drift_Source_Router_v5.0.yaml').read_text(encoding='utf-8'))
        pack = load(FTH, 'controls/source-router.yaml')
        for key in ('runtime', 'modules', 'loading', 'failures'):
            self.assertEqual(pack[key], source[key], key)
        for key in ('routing', 'module_gate', 'dependencies', 'authority', 'coverage'):
            self.assertEqual(pack['policies'][key], source['policies'][key], key)
        self.assertEqual([row['id'] for row in pack['controls']], ['MCA'])
        self.assertEqual(pack['controls'][0]['requires'], [])
        self.assertEqual(pack['controls'][0]['conditional_requires'], [])

    def test_instruction_ownership_and_unchanged_reasoning_sections(self):
        original = (ROOT / 'Project Feather Core/Project Feather Core CI/FTH_CI_version_v3.4.md').read_text(encoding='utf-8')
        extracted = text(FTH, 'controls/project-instructions.md')
        for heading in ('## Evidence and explanation', '## Relations and simulation', '## Subordinate controls'):
            source_section = original.split(heading, 1)[1].split('\n## ', 1)[0].strip()
            pack_section = extracted.split(heading, 1)[1].split('\n## ', 1)[0].strip()
            self.assertEqual(pack_section, source_section)
        hub = (ROOT / 'Central Hub/HUB_CI_v1.1.md').read_text(encoding='utf-8')
        source_body = hub.split('CONTROL KERNEL', 1)[1].replace('HUB_ROUTER_v1.1.yaml', 'hub-router.yaml').strip()
        self.assertEqual(text(HUB, 'starter/hub-ci.md').split('CONTROL KERNEL', 1)[1].strip(), source_body)

    def test_fth_pipeline_and_mca_are_extractions_not_rewrites(self):
        import difflib
        source = (ROOT / 'Project Feather Core/Anti-Drift Source/FTH_Anti_Drift_Modular_Concept_Architecture_v1.2.md').read_text(encoding='utf-8')
        extracted = text(FTH, 'optional/modular-concept-architecture_v1.0.md')
        self.assertGreater(difflib.SequenceMatcher(None, source, extracted).ratio(), 0.90)
        source_pipeline = (ROOT / 'Project Feather Core/Anti-Drift Source/FTH_Authoring_Pipeline_v1.1.md').read_text(encoding='utf-8')
        pack_pipeline = text(FTH, 'controls/authoring-pipeline.md')
        for number, end in ((3, 4), (4, 5), (6, 7)):
            start_marker = f'## {number}.'
            end_marker = f'## {end}.'
            self.assertEqual(source_pipeline.split(start_marker)[1].split(end_marker)[0], pack_pipeline.split(start_marker)[1].split(end_marker)[0])
        for term in ('REQUESTED OPERATION DETERMINES STOP POINT', 'DECOMPOSITION != GAP FILLING', 'before the first transformation'):
            self.assertIn(term.lower(), pack_pipeline.lower())

    def test_hub_singleton_is_replaceable_example(self):
        catalog = load(HUB, 'starter/root-catalog.yaml')
        self.assertFalse(catalog['active'])
        self.assertFalse(catalog['runtime_ready'])
        self.assertEqual(len(catalog['packages']), 1)
        entry = catalog['packages'][0]
        self.assertIsNone(entry['local_catalog'])
        self.assertEqual(entry['requires'], [])
        self.assertEqual(entry['entrypoint_module_id'], 'HUB-DOM-TECHNICAL')
        self.assertIn('replaceable worked example', text(HUB, 'starter/root-catalog.yaml'))
        original = ROOT / 'Central Hub/candidates/promotion/HUB-DOM-TECHNICAL_v1.0.md'
        self.assertEqual((DIST / HUB / 'starter/packages/HUB-DOM-TECHNICAL_v1.0.md').read_bytes(), original.read_bytes())
        for name in ('README.md', 'ARCHITECTURE.md'):
            self.assertIn('CENTRAL HUB ARCHITECTURE != TECHNICAL', text(HUB, name))
            self.assertIn('TECHNICAL = INCLUDED WORKED EXAMPLE', text(HUB, name))
        # Concrete alternative singleton fixture; the generic Router interface fields cover it unchanged.
        replacement = dict(entry, package_id='RECIPIENT-PKG-SUMMARY', entrypoint_module_id='RECIPIENT-CAP-SUMMARY', runtime_role='CAPABILITY', version='1.0', applicability='Summarize supplied documents')
        router = load(HUB, 'starter/hub-router.yaml')
        self.assertEqual(router['package_interface']['singleton'], 'Root entry -> direct entrypoint; no mandatory package-local catalog.')
        self.assertIsNone(replacement['local_catalog'])
        self.assertEqual(replacement['requires'], [])
        self.assertNotIn('HUB-DOM-TECHNICAL', str(router['stages']))
        self.assertNotIn('HUB-DOM-TECHNICAL', str(router['package_interface']))

    def test_hub_template_and_configured_core_pins_are_consistent(self):
        router = load(HUB, 'starter/hub-router.yaml')
        catalog = load(HUB, 'starter/root-catalog.yaml')
        self.assertEqual(router['contracts']['root_catalog']['version'], catalog['version'])
        self.assertEqual(router['contracts']['root_catalog']['status'], catalog['status'])
        self.assertIn('Version: ' + router['contracts']['architecture']['version'], text(HUB, 'ARCHITECTURE.md'))
        self.assertIn('Status: ' + router['contracts']['architecture']['status'], text(HUB, 'ARCHITECTURE.md'))
        for contract in router['contracts'].values():
            if isinstance(contract, dict) and 'file' in contract:
                self.assertTrue((DIST / HUB / contract['file']).is_file() or (DIST / HUB / 'starter' / contract['file']).is_file())
        ci = text(HUB, 'starter/hub-ci.md')
        self.assertIn('hub-router.yaml', ci)
        # Apply the documented status changes as an installation fixture, not deployment evidence.
        router['status'] = catalog['status'] = 'ACTIVE'
        router['active'] = catalog['active'] = catalog['runtime_ready'] = True
        router['contracts']['architecture']['status'] = 'ACTIVE'
        router['contracts']['root_catalog']['status'] = 'ACTIVE'
        self.assertEqual(router['contracts']['root_catalog']['status'], catalog['status'])
        for token in ('contracts.architecture.status', 'contracts.root_catalog.status'):
            self.assertIn(token, text(HUB, 'README.md'))

    def test_hub_no_personal_state_or_mandatory_other_packages(self):
        all_text = '\n'.join(text(HUB, name) for name in FILES[HUB])
        self.assertNotRegex(all_text, r'libfile_[0-9a-f]+|file_[0-9a-f]{16,}|FULL_FILE \d+/\d+|has_more=false|Central Hub Config|USER_REPORTED_SUCCESS|INTEGRATION PARTIAL')
        catalog = load(HUB, 'starter/root-catalog.yaml')
        self.assertEqual({row['package_id'] for row in catalog['packages']}, {'HUB-PKG-TECHNICAL'})
        self.assertIsNone(catalog['packages'][0]['location']['library_file_id'])
        self.assertIsNone(catalog['packages'][0]['location']['library_version_id'])

    def test_hub_composition_and_binding_preserved(self):
        source = yaml.safe_load((ROOT / 'Central Hub/HUB_ROUTER_v1.1.yaml').read_text(encoding='utf-8'))
        router = load(HUB, 'starter/hub-router.yaml')
        def bound(value):
            if isinstance(value, str):
                return value.replace('Central Hub Config', '{{LIBRARY_ROOT}}').replace('CENTRAL HUB CONFIG', 'CONFIGURED LIBRARY ROOT')
            if isinstance(value, dict):
                return {k: bound(v) for k, v in value.items()}
            if isinstance(value, list):
                return [bound(v) for v in value]
            return value
        source = bound(source)
        for key in ('sequence', 'stages', 'composition', 'package_interface', 'verification', 'ownership', 'pipelines', 'persistence', 'binding_dispatch', 'failure'):
            self.assertEqual(router[key], source[key], key)
        self.assertFalse(router['composition']['REFINES']['implies_requires'])
        self.assertFalse(router['composition']['COMPLEMENTS']['implies_requires'])
        self.assertFalse(router['composition']['REFINES']['autoload'])
        for target in ('repository', 'local_filesystem', 'project_sources_for_library_binding', 'archive', 'memory'):
            self.assertIn(target, router['library']['forbidden_fallbacks'])
        self.assertEqual(router['library']['root'], '{{LIBRARY_ROOT}}')
        self.assertIn('FULL_FILE', router['library']['retrieval_mechanism'])

    def test_evidence_classes_do_not_inherit_live_pass(self):
        for pack in FILES:
            notes = text(pack, 'RELEASE_NOTES.md')
            for term in ('SOURCE-DERIVED', 'STATICALLY VERIFIED', 'REGRESSION VERIFIED', 'PACKAGING VERIFIED', 'LIVE VERIFIED: NOT_RUN'):
                self.assertIn(term, notes)
            self.assertIn('không phải behavioral regression PASS'.lower(), notes.lower())
            self.assertIn('SPEC / NOT_RUN', text(pack, 'tests/SCENARIOS.md'))

    def test_archives_metadata_and_extracted_bytes(self):
        if not ARCHIVES:
            self.skipTest('Run with --archives after packaging')
        for pack, paths in FILES.items():
            asset = Path(ARCHIVES) / f'{pack}-v{VERSION}.zip'
            with zipfile.ZipFile(asset) as archive:
                infos = archive.infolist()
                expected = {pack + '/' + name for name in paths}
                self.assertEqual(len(infos), len(expected))
                self.assertEqual({info.filename for info in infos}, expected)
                self.assertIsNone(archive.testzip())
                for info in infos:
                    self.assertNotIn('..', Path(info.filename).parts)
                    self.assertEqual(info.date_time, (1980, 1, 1, 0, 0, 0))
                    self.assertEqual(info.compress_type, zipfile.ZIP_STORED)
                    self.assertEqual(info.create_system, 3)
                    self.assertEqual(info.external_attr >> 16, 0o100644)
                    name = info.filename[len(pack) + 1:]
                    self.assertEqual(archive.read(info), (DIST / pack / name).read_bytes())
                with tempfile.TemporaryDirectory() as directory:
                    archive.extractall(directory)
                    extracted = Path(directory) / pack
                    self.assertEqual({p.relative_to(extracted).as_posix() for p in extracted.rglob('*') if p.is_file()}, paths)
                    for name in paths:
                        self.assertEqual((extracted / name).read_bytes(), (DIST / pack / name).read_bytes())


if __name__ == '__main__':
    if '--archives' in sys.argv:
        index = sys.argv.index('--archives')
        ARCHIVES = sys.argv[index + 1]
        del sys.argv[index:index + 2]
    unittest.main()

"""Executable integrity tests; regression prompts remain unexecuted model protocols."""
import importlib.util
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('tk_package', ROOT / 'tools/validate_kingdom_package.py')
PACKAGE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PACKAGE)


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        # Never copy/read real archived lore into a structural fixture.
        for path in ROOT.rglob('*'):
            relative = path.relative_to(ROOT)
            if 'Source_archive' in relative.parts or '__pycache__' in relative.parts:
                continue
            if path.is_file():
                target = self.root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(path,target)
        for path in self.root.glob('*.md'):
            for target in re.findall(r'Source_archive/[^\s`)>#]+',path.read_text(encoding='utf-8')):
                if not Path(target).suffix:
                    continue
                destination = self.root / target
                destination.parent.mkdir(parents=True,exist_ok=True)
                destination.touch()

    def edit(self, name, old, new):
        p = self.root / name
        text = p.read_text(encoding='utf-8')
        self.assertIn(old,text)
        p.write_text(text.replace(old,new,1),encoding='utf-8')

    def failure(self, expression):
        with self.assertRaisesRegex(PACKAGE.ValidationError,expression):
            PACKAGE.validate(self.root)

    def hashes(self):
        return {str(p.relative_to(self.root)):hashlib.sha256(p.read_bytes()).hexdigest()
                for p in self.root.rglob('*') if p.is_file()}

    def test_real_package_read_only_and_idempotent_write(self):
        before = self.hashes()
        plan = PACKAGE.validate(self.root)
        self.assertEqual(14,len(plan['sources']))
        self.assertEqual(13,len(plan['resolved']))
        PACKAGE.validate(self.root,write=True)
        self.assertEqual(before,self.hashes())

    def test_numeric_version_and_highest_active(self):
        folder = self.root / 'control_versions'
        folder.mkdir()
        for version,status in [('1.9','ACTIVE'),('1.10','ACTIVE'),('1.11','SUPERSEDED'),('9.0','RETIRED')]:
            (folder/f'TK_TEST_v{version}.md').write_text(
                f'# Test\n\nStatus: {status}\nVersion: {version}\n',encoding='utf-8')
        self.assertLess(PACKAGE.numeric_version('1.9'),PACKAGE.numeric_version('1.10'))
        self.assertEqual('TK_TEST_v1.10.md',PACKAGE.resolve_control(self.root,'control_versions','TK_TEST').name)

    def test_no_candidate_lifecycle_required_missing_status_not_active(self):
        folder = self.root/'control_versions'
        folder.mkdir()
        (folder/'TK_TEST_v99.0.md').write_text('# No status\nVersion: 99.0\n',encoding='utf-8')
        with self.assertRaisesRegex(PACKAGE.ValidationError,'Missing ACTIVE'):
            PACKAGE.resolve_control(self.root,'control_versions','TK_TEST')

    def test_archived_version_is_not_scanned(self):
        folder = self.root/'controls'/'archive'
        folder.mkdir()
        (folder/'TK_CI_v999.0.md').write_text('# Old\nStatus: ACTIVE\nVersion: 999.0\n',encoding='utf-8')
        self.assertEqual('TK_CI_v1.0.md',PACKAGE.resolve_control(self.root,'controls','TK_CI').name)

    def test_equal_numeric_versions_are_ambiguous(self):
        folder=self.root/'controls'
        (folder/'TK_CI_v1.0.0.md').write_text('# Equal\nStatus: ACTIVE\nVersion: 1.0.0\n',encoding='utf-8')
        self.failure('Ambiguous highest ACTIVE')

    def test_missing_pipeline_blocks_dependent_package(self):
        (self.root/'controls/TK_AUTHORING_PIPELINE_v1.0.md').unlink()
        self.failure('Missing ACTIVE control')

    def test_duplicate_id_fails(self):
        self.edit('TK_DOMAIN_POT.md','SOURCE_ID: TK-DOM-POT','SOURCE_ID: TK-DOM-GEO')
        self.failure('Duplicate SOURCE_ID')

    def test_missing_required_header_fails(self):
        self.edit('TK_DOMAIN_POT.md','LOAD_MODE: FULL_FILE\n','')
        self.failure('Missing required source fields')

    def test_catalog_mapping_mismatch_fails_read_only(self):
        self.edit('TK_CURRENT_SOURCE_INDEX.md','`TK_DOMAIN_POT.md`','`WRONG.md`')
        before=self.hashes()
        self.failure('Stale generated catalog')
        self.assertEqual(before,self.hashes())

    def test_unknown_cross_owner_fails_even_in_write_mode(self):
        self.edit('TK_DOMAIN_POT.md','TK-DOM-INFRA,','TK-DOM-MISSING,')
        before=self.hashes()
        with self.assertRaisesRegex(PACKAGE.ValidationError,'Unknown cross-owner'):
            PACKAGE.validate(self.root,write=True)
        self.assertEqual(before,self.hashes())

    def test_archive_cannot_satisfy_missing_current_owner(self):
        source=self.root/'TK_DOMAIN_POT.md'
        destination=self.root/'Source_archive/TK_DOMAIN_POT.md'
        destination.parent.mkdir(exist_ok=True)
        shutil.copyfile(source,destination)
        source.unlink()
        self.failure('Missing current file: TK_DOMAIN_POT.md')

    def test_archive_never_read_by_check_or_hash_refresh(self):
        original=Path.read_bytes
        def guarded(path):
            if any(x.casefold()=='source_archive' for x in path.parts):
                raise AssertionError('Archive content read')
            return original(path)
        with patch.object(Path,'read_bytes',guarded):
            PACKAGE.validate(self.root)
            PACKAGE.validate(self.root,write=True)

    def test_router_dependencies_expand_transitively(self):
        router=PACKAGE.yaml_data((self.root/'controls/TK_ROUTER_v1.0.yaml').read_text(encoding='utf-8'))
        result=PACKAGE.expand_controls(router['controls'],['NARRATIVE'],['economic_mechanism_material','operational_conflict_material'])
        self.assertTrue({'NARRATIVE','ACTOR','RELATION','TEMPORAL','CRISIS','ECONOMY'}<=set(result))

    def test_unknown_dependency_and_cycles_fail(self):
        rows=[{'id':'A','stem':'TK_TEST','select_when':'material','requires':['B'],'conditional_requires':[]}]
        with self.assertRaisesRegex(PACKAGE.ValidationError,'Unknown control dependency'):
            PACKAGE.control_graph(rows)
        rows[0]['requires']=['A']
        with self.assertRaisesRegex(PACKAGE.ValidationError,'cycle'):
            PACKAGE.control_graph(rows)

    def test_duplicate_yaml_and_unsafe_tag_fail(self):
        with self.assertRaises(PACKAGE.ValidationError):
            PACKAGE.yaml_data('status: ACTIVE\nstatus: RETIRED\n')
        with self.assertRaises(PACKAGE.ValidationError):
            PACKAGE.yaml_data('x: !!python/object:bad {}')

    def test_timeline_cannot_route_to_archive(self):
        self.edit('THE_KINGDOM_CHECKPOINT_STATE_INDEX.md','(TK_TIMELINE_CP01_OPENING.md)',
                  '(Source_archive/sources/TK_TIMELINE_CP01_OPENING.md)')
        self.failure('Timeline index cannot route')

    def test_unadmitted_current_owner_fails(self):
        text=(self.root/'TK_DOMAIN_POT.md').read_text(encoding='utf-8')
        (self.root/'TK_ACTOR_EMPTY.md').write_text(text,encoding='utf-8')
        self.failure('Unexpected CURRENT_SOURCE')

    def test_archive_admission_and_path_escape_fail(self):
        for name in ['Source_archive/current.md','../outside.md','D:\\external.md']:
            with self.assertRaises(PACKAGE.ValidationError):
                PACKAGE.safe_file(self.root,name)

    def test_hash_refresh_only_generated_regions(self):
        self.edit('TK_DOMAIN_POT.md','# The Kingdom — POT','# The Kingdom — POT')
        with (self.root/'TK_DOMAIN_POT.md').open('a',encoding='utf-8') as f:
            f.write('\nA human-authored fixture edit.\n')
        self.failure('Stale generated catalog/hashes')
        before=self.hashes()
        PACKAGE.validate(self.root,write=True)
        after=self.hashes()
        self.assertEqual({'MANIFEST.md'}, {n for n in before if before[n]!=after[n]})
        PACKAGE.validate(self.root)

    def test_invalid_generated_marker_fails_without_write(self):
        self.edit('MANIFEST.md','<!-- END GENERATED HASHES -->','<!-- MISSING -->')
        before=self.hashes()
        with self.assertRaises(PACKAGE.ValidationError):
            PACKAGE.validate(self.root,write=True)
        self.assertEqual(before,self.hashes())

    def test_crlf_inputs_and_generated_regions_preserve_human_text(self):
        for path in self.root.rglob('*'):
            if path.is_file() and 'Source_archive' not in path.parts:
                raw=path.read_bytes().replace(b'\r\n',b'\n').replace(b'\n',b'\r\n')
                path.write_bytes(raw)
        before=self.hashes()
        plan=PACKAGE.inspect(self.root)
        expected=set(plan['updates'])
        PACKAGE.validate(self.root,write=True)
        after=self.hashes()
        self.assertEqual(expected,{n for n in before if before[n]!=after[n]})
        self.assertEqual({'MANIFEST.md'},expected)
        PACKAGE.validate(self.root)
        self.assertTrue((self.root/'TK_CURRENT_SOURCE_INDEX.md').read_bytes().count(b'\r\n')>0)

    def test_concurrent_source_edit_blocks_writer(self):
        plan=PACKAGE.inspect(self.root)
        with (self.root/'TK_DOMAIN_POT.md').open('a',encoding='utf-8') as f:
            f.write('\nConcurrent edit\n')
        with self.assertRaisesRegex(PACKAGE.ValidationError,'Concurrent input change'):
            PACKAGE.write_regions(plan)

    def test_partial_replace_failure_rolls_back(self):
        self.edit('TK_CURRENT_SOURCE_INDEX.md','`TK_DOMAIN_POT.md`','`WRONG.md`')
        before=self.hashes()
        plan=PACKAGE.inspect(self.root)
        original=PACKAGE.os.replace
        failed=False
        def one_failure(src,dst):
            nonlocal failed
            if Path(dst).name=='MANIFEST.md' and not failed:
                failed=True
                raise OSError('fixture replacement failure')
            return original(src,dst)
        with patch.object(PACKAGE.os,'replace',one_failure):
            with self.assertRaises(OSError):
                PACKAGE.write_regions(plan)
        self.assertEqual(before,self.hashes())
        self.assertFalse(list(self.root.glob('.tk-maintenance-*')))

    def test_regression_protocol_routes_not_model_outputs(self):
        cases=json.loads((self.root/'tests/control_cases.json').read_text(encoding='utf-8'))
        self.assertEqual('NOT_RUN',cases['model_execution'])
        self.assertEqual('STRUCTURAL_FIXTURE_ONLY',cases['evidence'])
        self.assertEqual(6,len(cases['cases']))
        plan=PACKAGE.inspect(self.root)
        ids=set()
        for case in cases['cases']:
            self.assertNotIn(case['id'],ids)
            ids.add(case['id'])
            self.assertTrue(set(case['owners'])<=plan['sources'].keys())
            selected=PACKAGE.expand_controls(plan['router']['controls'],case['overlays'],case['conditions'])
            self.assertTrue(set(selected)<=plan['resolved'].keys())
            self.assertTrue(case['prompt'] and case['review_criteria'])
        # No generated answer, substring scorer, or semantic-compliance result exists.


if __name__=='__main__':
    unittest.main()

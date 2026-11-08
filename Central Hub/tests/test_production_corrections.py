"""Current STATIC/SPEC regressions; no model, Library, or live execution.

Lexical admission is an acceptance oracle, not a production parser. Source roles
are fixture-supplied. Output instructions still require actual model verification.
"""
import copy
import hashlib
import json
import re
import subprocess
import unittest

from test_hub_contracts import ROOT, load, historical_source
from test_concept_development import leaf_span_spec
from test_concept_production_anti_drift import production_spec, MCA, WIL, AR

HISTORY = ROOT / 'Source_archive/Production corrections 2026-11-08'
BASELINE = '73a0a0b28c29e832dfdd4886923703ed84592e41'
TARGETS = ('AIS', 'IMAGET', 'CODEX', 'WORK', 'GENERIC')


def author_call_spec(message, *, user_directive=True):
    """One-turn exact-call oracle; never strips suffixes or remembers a mode."""
    if not user_directive:
        return None
    first = next((line for line in message.replace('\r\n', '\n').split('\n')
                  if line.strip(' \t')), '')
    match = re.fullmatch(r'/AUTHOR (AIS|IMAGET|CODEX|WORK|GENERIC)'
                         r'(?: (P[123]))?( ISOLATED)?', first)
    return match.groups() if match else None


class ProductionCorrectionsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.author = (ROOT/'library_modules/HUB-CAP-AUTHORING_v0.8.md').read_text(encoding='utf-8')
        cls.core = (ROOT/'library_modules/HUB-DOM-CONCEPT-DEVELOPMENT_v1.4.md').read_text(encoding='utf-8')
        cls.catalog = load(ROOT/'HUB_PACKAGE_CATALOG_v1.13.yaml')
        cls.local = load(ROOT/'library_modules/HUB-CATALOG-CONCEPT-DEVELOPMENT_v1.4.yaml')

    def test_all_removed_forms_never_downgrade_and_valid_forms_survive(self):
        for target in TARGETS:
            for preset in ('', ' P1', ' P2', ' P3'):
                for isolation in ('', ' ISOLATED'):
                    call = f'/AUTHOR {target}{preset}{isolation}'
                    self.assertIsNotNone(author_call_spec(call+'\nUse the supplied source.'), call)
                    self.assertIsNotNone(author_call_spec(' \t\r\n'+call+'\r\nTask'), call)
            for removed in ('CREATIVE', 'BRAINSTORM'):
                call = f'/AUTHOR {target} + {removed}'
                for suffix in ('', ' P2', ' ISOLATED'):
                    self.assertIsNone(author_call_spec(call+suffix+'\nTask'), call+suffix)
                self.assertIsNone(author_call_spec(f'/AUTHOR {target} P2 + {removed}'))
        entry = next(p for p in self.catalog['packages'] if p['package_id']=='HUB-PKG-AUTHORING')
        for text in (self.author, entry['applicability']):
            self.assertIn('non-activating', text)
            self.assertIn('downgrade', text)
        self.assertNotIn('## Bounded composition', self.author)
        self.assertNotIn('admit exactly `/AUTHOR <OUTPUT_TARGET> +', entry['applicability'])

    def test_invalid_and_literal_calls_still_rejected(self):
        for text in ('/author AIS', '/AUTHOR  AIS', ' /AUTHOR AIS', '/AUTHOR AIS ',
                     '/AUTHOR FTH', '/AUTHOR AIS P4', '/AUTHOR AIS p2',
                     '/AUTHOR AIS ISOLATED P2', '/AUTHOR AIS DEFAULT',
                     '/AUTHOR AIS P2 extra', 'intro\n/AUTHOR AIS',
                     '> /AUTHOR AIS', '```text\n/AUTHOR AIS\n```'):
            self.assertIsNone(author_call_spec(text), text)
        self.assertIsNone(author_call_spec('/AUTHOR AIS', user_directive=False))

    def test_clarification_calls_are_new_nonpersistent_invocations(self):
        self.assertIsNotNone(author_call_spec('/AUTHOR GENERIC P2 ISOLATED\nAmbiguous source'))
        self.assertIsNone(author_call_spec('The answer is A.'))
        self.assertIsNotNone(author_call_spec('/AUTHOR GENERIC P2 ISOLATED\nThe answer is A; source: supplied text.'))
        for phrase in ('this invocation ends in the current turn',
                       'repeating the exact admitted', 'including any chosen preset and ISOLATED suffix',
                       'supply or sufficiently identify again every material source',
                       'do not silently carry target, preset or isolation forward'):
            self.assertIn(phrase, self.author)
        for operation in ('CREATIVE', 'BRAINSTORM', 'DEBATE'):
            self.assertEqual(len(leaf_span_spec([('USER_DIRECTIVE',f'/{operation} clarify X #')])['invocations']),1)
            self.assertEqual(leaf_span_spec([('USER_DIRECTIVE','The answer is A.')])['invocations'],[])
            self.assertEqual(len(leaf_span_spec([('USER_DIRECTIVE',f'/{operation} continue with A #')])['invocations']),1)
            self.assertIn(f'/{operation} <content> #',self.core)
        for phrase in ('this invocation ends in the current turn',
                       'neither a clarification answer nor semantic continuity reopens the leaf',
                       'no persistent mode or implicit continuation'):
            self.assertIn(phrase,self.core)

    def test_ordinary_context_and_independent_concept_operations_preserved(self):
        old=(HISTORY/'library_modules/HUB-CAP-AUTHORING_v0.7.md').read_text(encoding='utf-8')
        marker='## Context sources, rewrite and reauthor'
        self.assertEqual(self.author.split(marker,1)[1],old.split(marker,1)[1])
        for phrase in ('ordinary source/context', 'explicitly supplied or referenced',
                       'AUTHORING DOES NOT REQUEST OR INFER CREATIVE/BRAINSTORM CONTRIBUTION'):
            self.assertIn(phrase,self.author)
        for operation in ('CREATIVE','BRAINSTORM'):
            spans=leaf_span_spec([('USER_DIRECTIVE',f'/{operation} develop A #')])
            self.assertEqual(len(spans['invocations']),1)
            self.assertIsNotNone(author_call_spec('/AUTHOR CODEX\nUse the explicitly referenced result A.'))
        self.assertNotRegex(self.author,r'(?m)^(Requires|Refines|Complements):')

    def test_mca_exact_local_correction_and_dependency_closure(self):
        old=(HISTORY/'library_modules/HUB-DOM-MODULAR-CONCEPT-ARCHITECTURE_v1.1.md').read_text(encoding='utf-8')
        current=(ROOT/'library_modules/HUB-DOM-MODULAR-CONCEPT-ARCHITECTURE_v1.2.md').read_text(encoding='utf-8')
        expected=old.replace('Version: 1.1','Version: 1.2').replace(
            'verification of both B controls and necessary task sources',
            'verification of selected MCA, necessary task inputs/dependencies and any explicitly declared Requires; WIL is not an implicit requirement')
        self.assertEqual(current,expected)
        rows={x['module_id']:x for x in self.local['entries']}
        self.assertEqual(rows[MCA]['requires'],[])
        self.assertEqual(rows[WIL]['requires'],[])
        self.assertEqual(rows[AR]['requires'],[{'module_id':MCA}])
        result=production_spec(['RECEPTION'])
        selected={identity for _,identity in result['spec_verified']}
        self.assertEqual(selected,{AR,MCA})
        self.assertNotIn(WIL,result['artifact_requests'])

    def test_status_is_user_confirmation_not_fabricated_identity_or_delta_live(self):
        evidence=self.catalog['production_evidence']
        self.assertIn('USER_CONFIRMED_LIVE_PASS',evidence['baseline'])
        self.assertEqual(evidence['correction_delta_live'],'NOT_RUN')
        self.assertEqual(evidence['codex_independent_reproduction'],'NOT_PERFORMED')
        for package in self.catalog['packages']:
            if package['binding_mode']!='LIBRARY_MODULE':
                self.assertIn('USER_CONFIRMED',package['location']['verification'])
                continue
            for row in (package,package.get('local_catalog')):
                if row is None: continue
                location=row['location']
                if package['package_id']=='HUB-PKG-TECHNICAL': continue
                is_concept = package['package_id']=='HUB-PKG-CONCEPT-DEVELOPMENT'
                self.assertEqual(location['resolution'],'UNRESOLVED' if is_concept else 'USER_CONFIRMED_BASELINE_LIVE')
                self.assertIsNone(location['locator'])
                self.assertIsNone(location['library_file_id'])
                self.assertIsNone(location['library_version_id'])
                self.assertIn('NOT_VERIFIED' if is_concept else 'EXACT_READ_RECEIPTS_NOT_RECORDED',location['verification'])
        for row in self.local['entries'][2:]:
            self.assertEqual(row['location']['resolution'],'UNRESOLVED' if row['module_id']=='HUB-DOM-NAMING' else 'USER_CONFIRMED_BASELINE_LIVE')
            self.assertIsNone(row['location']['library_file_id'])
        changelog=(ROOT/'RUNTIME_EVIDENCE_CHANGELOG.md').read_text(encoding='utf-8')
        self.assertIn('PRODUCTION_BASELINE_USER_CONFIRMATION_2026_11_08',changelog)
        self.assertIn('LIVE VERIFICATION OF NEW DELTA: NOT RUN',changelog)
        self.assertIn('Baseline USER_CONFIRMED_LIVE_PASS',changelog)

    def test_exact_stack_and_router_algorithm_preserved(self):
        router=load(ROOT/'HUB_ROUTER_v1.1.yaml')
        old=load(HISTORY/'HUB_ROUTER_v1.1.yaml')
        expected=copy.deepcopy(old)
        expected['deployment']='USER_CONFIRMED_BASELINE_INSTALLED_AND_LIVE; CORRECTION_DELTA_STATIC_ONLY'
        expected['evidence']['live_routing']='USER_CONFIRMED_BASELINE_LIVE_PASS; CORRECTION_DELTA_LIVE_NOT_RUN; historical trial I01-I07/I09-I10 PASS, I08 UNVERIFIABLE; USER_REPORTED'
        for key,suffix in (('architecture','md'),('root_catalog','yaml')):
            expected['contracts'][key]['file']=expected['contracts'][key]['file'].replace('1.11','1.13')
            expected['contracts'][key]['version']='1.13'
        expected['contracts']['binding_scope']=expected['contracts']['binding_scope'].replace('1.11','1.13').replace('Hub CI/Router v1.1 with','Hub CI v1.2 / Router v1.1 with')
        expected['activation_notice']=expected['activation_notice'].replace('HUB_CI_v1.1.md','HUB_CI_v1.2.md')
        self.assertEqual(router,expected)
        self.assertEqual(len(self.catalog['packages']),6)
        bindings={p['package_id']:p for p in self.catalog['packages']}
        self.assertEqual(bindings['HUB-PKG-AUTHORING']['version'],'0.8')
        self.assertEqual(bindings['HUB-PKG-CONCEPT-DEVELOPMENT']['version'],'1.4')
        self.assertEqual(bindings['HUB-PKG-CONCEPT-DEVELOPMENT']['local_catalog']['version'],'1.4')
        self.assertEqual(self.local['version'],'1.4')
        self.assertEqual(next(x for x in self.local['entries'] if x['module_id']==MCA)['version'],'1.2')
        self.assertFalse(router['persistence']['persistent_modes'])
        self.assertIn('repository',router['library']['forbidden_fallbacks'])
        old_ci=subprocess.check_output(['git','show',BASELINE+':Central Hub/HUB_CI_v1.1.md'],cwd=ROOT)
        self.assertEqual(historical_source('HUB_CI_v1.1.md').read_bytes(),old_ci)

    def test_pipeline_changes_only_status_and_corresponding_manifest_hash(self):
        path='tool_pipelines/AIS/AIS_PIPELINE_v1.1.md'
        old=(HISTORY/path).read_text(encoding='utf-8')
        expected=old.replace('Project deployment: NOT_PERFORMED','Project deployment: USER_CONFIRMED_INSTALLED_AND_LIVE').replace('Independent live verification: NOT_RUN','Production live status: USER_CONFIRMED_LIVE_PASS\nCodex independent reproduction: NOT_PERFORMED')
        self.assertEqual((ROOT/path).read_text(encoding='utf-8'),expected)
        path='tool_pipelines/AIS/AIS_ROUTER_v1.2.yaml'
        old=load(HISTORY/path);expected=copy.deepcopy(old)
        expected.update(live_verification='USER_CONFIRMED_LIVE_PASS',deployment='USER_CONFIRMED_INSTALLED_AND_LIVE')
        self.assertEqual(load(ROOT/path),expected)
        path='tool_pipelines/ImageT/IMAGE_CONTROLLER_v1.2.md'
        before=(HISTORY/path).read_text(encoding='utf-8')
        after=(ROOT/path).read_text(encoding='utf-8')
        marker='## Authority and conflict'
        self.assertEqual(before.split(marker,1)[1],after.split(marker,1)[1])
        manifest=load(ROOT/'tool_pipelines/ImageT/manifest.yaml')
        old=load(HISTORY/'tool_pipelines/ImageT/manifest.yaml')
        old['release']['project_deployment']='USER_CONFIRMED_INSTALLED_AND_LIVE'
        old['controllers']['active']['sha256']=hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
        self.assertEqual(manifest,old)

    def test_archive_receipts_and_candidates_unchanged(self):
        receipt=json.loads((HISTORY/'ARCHIVE_RECEIPT.json').read_text(encoding='utf-8'))
        for rel,digest in receipt.items():
            data=(HISTORY/rel).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(),digest,rel)
            self.assertEqual(data,subprocess.check_output(['git','show',BASELINE+':Central Hub/'+rel],cwd=ROOT),rel)
        self.assertEqual(subprocess.check_output(['git','diff',BASELINE,'--','candidates'],cwd=ROOT),b'')
        for name in ('HUB-CAP-AUTHORING_v0.7.md','HUB-DOM-CONCEPT-DEVELOPMENT_v1.2.md',
                     'HUB-CATALOG-CONCEPT-DEVELOPMENT_v1.2.yaml',
                     'HUB-DOM-MODULAR-CONCEPT-ARCHITECTURE_v1.1.md'):
            self.assertFalse((ROOT/'library_modules'/name).exists())


if __name__=='__main__':
    unittest.main()

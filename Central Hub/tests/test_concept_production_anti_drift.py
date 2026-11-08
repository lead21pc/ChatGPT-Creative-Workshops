"""Production STATIC/SPEC only: fixture-declared provenance and semantic exposure.

No LLM classifier, deployment, actual Library read or runtime provenance recognition.
The existing generic Router oracle checks composition and synthetic read failures.
"""
import copy
import hashlib
import itertools
import json
import re
import subprocess
import unittest

from test_hub_contracts import ROOT, load
from test_concept_development import current_fixture, leaf_span_spec, PACKAGE, CORE, CATALOG
from test_hub_router_candidate import simulate, integration_read_spec
from test_hub_contracts import Closed

AP = 'HUB-DOM-ANTI-PRIOR'
MCA = 'HUB-DOM-MODULAR-CONCEPT-ARCHITECTURE'
WIL = 'HUB-DOM-WORLDBUILDING-INTERNAL-LOGIC'
AR = 'HUB-DOM-ACTOR-RECEPTION'
NR = 'HUB-DOM-NARRATIVE-RESOLUTION'
IDS = (AP, MCA, WIL, AR, NR)
EXPOSURES = dict(zip(IDS, ('SURFACE', 'RELATION', 'SYSTEM', 'RECEPTION', 'CLOSURE')))
VERSIONS = dict(zip(IDS, ('1.1', '1.2', '1.1', '1.0', '1.0')))
HISTORY = ROOT / 'Source_archive/Concept production anti-drift 2026-11-07'
BASELINE = 'e310b4510ad078981ee6ea82373808c469144ddb'

# Accepted author corpus, NOT 34 observed Hub failures. Features are fixture premises.
# id, material failure, semantic exposures, valid counterexample (still within owner scope).
CORPUS = [
 ('A01','Repeated cliffhanger erases claimed closure',('CLOSURE',),'Intentional open ending preserves the question'),
 ('A02','World and actors wait for protagonist',('RELATION','SYSTEM'),'Dormant actors need no invented off-screen activity'),
 ('A03','Large cast loses all independent causal agency',('RELATION',),'A genuinely two-sided conflict may have two centers'),
 ('A04','Romance cancels established goals and refusal',('RELATION','RECEPTION'),'Supported voluntary cooperation preserves agency'),
 ('A05','Secondary actors lose established leverage',('RELATION','SYSTEM'),'A secondary actor may have limited leverage'),
 ('A06','Opportunity/assets become immediate liquid capital',('SYSTEM',),'An established liquid funding source suffices'),
 ('A07','Institutions activate only as protagonist scenery',('SYSTEM',),'A bounded institution abstraction may suffice'),
 ('A08','Evidence vanishes to sustain underestimation',('RECEPTION',),'Weak evidence may justify retaining a prior'),
 ('A09','Cold demeanor automatically produces charisma',('SURFACE','RECEPTION'),'An established preference may support attraction'),
 ('A10','Accumulated side-character value transfers without cause',('RELATION','SYSTEM'),'Supported gift or transfer preserves obligations'),
 ('A11','Rewards precede supporting accumulated state',('CLOSURE','RELATION','SYSTEM'),'Easy payoff may be causally earned'),
 ('B01','Flashy appearance silently determines power',('SURFACE',),'Ontology may explicitly tie visual intensity to power'),
 ('B02','Ancient long names silently determine strength',('SURFACE',),'Actual mechanism may establish superior strength'),
 ('B03','Magic implies academy and prestige costume function',('SURFACE','SYSTEM'),'Author may explicitly request a conventional academy'),
 ('B04','Experts ignore available interpretable evidence',('RECEPTION','RELATION'),'No information path means no forced discovery'),
 ('B05','Inheritance becomes mastery and summon becomes property',('RELATION',),'Ontology may explicitly establish mastery or ownership'),
 ('B06','Romance erases supported institutional investigation',('RECEPTION','RELATION','SYSTEM'),'An established filter can explain incomplete investigation'),
 ('B07','Established kit/counter disappears for protagonist victory',('RELATION',),'Timing or deliberate reserve can support non-use'),
 ('B08','Large academy system loses required delegation',('SYSTEM',),'Supported compact organization needs no invented bureaucracy'),
 ('B09','Dungeon/shop resources appear only on protagonist arrival',('RELATION','SYSTEM'),'Explicit timed activation may be established'),
 ('B10','Suspicion is noticed then reset without cause',('RECEPTION',),'Reassessment may retain suspicion without certainty'),
 ('B11','Coincidence resets near-confrontation pressure',('CLOSURE',),'Interruption may change form while retaining consequences'),
 ('B12','Fake identity loses all supported trace pressure',('RELATION','RECEPTION','SYSTEM'),'A supported untraceable mechanism may remain effective'),
 ('B13','Repeated anomalies leave no represented reassessment',('RECEPTION',),'Correlated weak evidence need not reverse belief'),
 ('B14','Institutional position collapses into moral alignment',('SURFACE','RELATION','SYSTEM'),'Established unified doctrine may guide actual actors'),
 ('C01','Realm automatically becomes income and inventory',('SURFACE','SYSTEM'),'Explicit conversion mechanism may link power and income'),
 ('C02','Costume aesthetics replace material use model',('SURFACE','SYSTEM'),'Pure imagery needs no clothing engineering checklist'),
 ('C03','Numbers/support/coordination vanish into sequential duels',('RELATION',),'Terrain or poor coordination may support separation'),
 ('C04','Minor insult absorbs whole factions without transmission',('RELATION','SYSTEM'),'Established obligations can support escalation'),
 ('C05','Sentient artifact erases prior bond for compatibility',('RELATION',),'Supported voluntary transfer can respect prior bond'),
 ('C06','Past-life evidence becomes automatic present verdict',('RECEPTION','RELATION'),'Explicit ontology may establish stronger continuity'),
 ('C07','Undefined balance excuses capable informed non-intervention',('SYSTEM',),'Ignorance or incapacity is not political choice'),
 ('C08','Meeting becomes implementation/enforcement and full closure',('SYSTEM','CLOSURE'),'A genuinely self-executing agreement may resolve the issue'),
 ('C09','Holy/dark label becomes moral truth and authority',('SURFACE','RELATION','SYSTEM'),'A supported doctrine or authority remains valid'),
]


def force_spec(parts):
    """Lexical oracle over supplied role labels, not a provenance detector/parser service."""
    text = ''.join(value for _, value in parts)
    mask = [role == 'USER_DIRECTIVE' for role, value in parts for _ in value]
    return any(all(mask[m.start():m.end()]) for m in re.finditer(r'(?<!\S)/AD(?!\S)', text))


def production_spec(exposures=(), *, parts=(), concept=True, alter=None):
    """Declared applicability -> existing generic composition oracle. No text classification."""
    fixture = current_fixture()
    scopes = set(exposures)
    force = force_spec(parts)
    reached = concept or force
    fixture['packages'][0]['applicability'].update(EXPOSURES.values())
    fixture['packages'][0]['applicability'].add('GATE')
    for row in fixture['local_catalogs'][PACKAGE]:
        identity = row['module_id']
        if identity in IDS:
            row['scopes'] = {EXPOSURES[identity]}
            fixture['artifacts'][identity][0].update(copy.deepcopy(row))
    if reached:
        scopes.add('GATE')
    else:
        scopes.clear()
    if alter:
        alter(fixture)
    result = simulate(fixture, scopes)
    result.update(gate_evaluated=reached, forced=force)
    return result


def verified(result):
    return {identity for _, identity in result['spec_verified']}


class ProductionAntiDriftTests(unittest.TestCase):
    def test_all_active_exact_bindings_and_real_requires(self):
        local = load(ROOT / 'library_modules/HUB-CATALOG-CONCEPT-DEVELOPMENT_v1.4.yaml')
        rows = {row['module_id']: row for row in local['entries']}
        self.assertEqual(set(rows), set(IDS) | {'HUB-DOM-CREATIVE','HUB-CAP-DEBATE','HUB-CAP-BRAINSTORM','HUB-DOM-NAMING'})
        for identity in IDS:
            with self.subTest(identity=identity):
                row = rows[identity]
                text = (ROOT / f'library_modules/{identity}_v{VERSIONS[identity]}.md').read_text(encoding='utf-8')
                for key, value in [('Module ID',identity),('Package ID',PACKAGE),('Runtime role','DOMAIN_CONTROL'),('Status','ACTIVE'),('Version',VERSIONS[identity])]:
                    self.assertEqual(re.findall('^'+key+r': (.+)$',text,re.M),[value])
                self.assertEqual((row['status'],row['version']),('ACTIVE',VERSIONS[identity]))
                deps = [{'module_id':MCA}] if identity == AR else []
                self.assertEqual(row['requires'],deps)
                self.assertEqual(re.findall(r'^Requires: (.+)$',text,re.M),[MCA] if identity == AR else [])
                self.assertEqual(row['location']['root'],'Central Hub Config')
                self.assertEqual(row['location']['resolution'],'USER_CONFIRMED_BASELINE_LIVE')
                self.assertEqual(row['location']['verification'],'USER_CONFIRMED_BASELINE_LIVE; EXACT_READ_RECEIPTS_NOT_RECORDED')
                for key in ('locator','library_file_id','library_version_id'):
                    self.assertIsNone(row['location'][key])
        live = str(local)
        for obsolete in ('Alternative B','BASELINE =','dependency-only','Experiment switch'):
            self.assertNotIn(obsolete,live)

    def test_force_positions_and_reachability_from_none(self):
        for text in ('/AD assess','assess /AD now','assess /AD','/AD'):
            with self.subTest(text=text):
                result = production_spec(parts=[('USER_DIRECTIVE',text)],concept=False)
                self.assertTrue(result['forced']); self.assertTrue(result['gate_evaluated'])
                self.assertEqual(verified(result),set())
                self.assertEqual(result['spec_reads'][:2],[CORE,CATALOG])
        plain = production_spec(concept=False)
        self.assertFalse(plain['gate_evaluated']); self.assertEqual(plain['artifact_requests'],[])

    def test_force_provenance_and_exact_token_boundaries(self):
        for role in ('ASSISTANT','PRIOR_TURN','TOOL','SOURCE','ATTACHMENT','QUOTE','CODE','INLINE_CODE','DOCUMENTATION','ANALYZED_PROMPT'):
            result = production_spec(parts=[(role,'/AD')],concept=False)
            self.assertFalse(result['forced'],role); self.assertEqual(result['artifact_requests'],[])
        for token in ('/ad','/Ad','/ADmore','/ADX','x/AD','path/AD','/AD/path','/AD#','/AD,','AD','/A D'):
            self.assertFalse(force_spec([('USER_DIRECTIVE',token)]),token)
        self.assertFalse(force_spec([('USER_DIRECTIVE','/A'),('QUOTE','D')]))
        self.assertFalse(production_spec(concept=False)['forced'])  # Next turn: no mode.

    def test_force_inside_operation_preserves_span_and_selection(self):
        parts=[('USER_DIRECTIVE','before /CREATIVE develop /AD this # after')]
        self.assertTrue(force_spec(parts))
        invocations=leaf_span_spec(parts)['invocations']
        self.assertEqual(invocations,[('HUB-DOM-CREATIVE','develop /AD this')])
        self.assertEqual(leaf_span_spec([('USER_DIRECTIVE','/AD plain prose')])['invocations'],[])
        self.assertFalse(leaf_span_spec([('USER_DIRECTIVE','/CREATIVE develop /AD this')])['invocations'])
        self.assertTrue(force_spec([('USER_DIRECTIVE','/CREATIVE develop /AD this')]))

    def test_auto_zero_multiple_and_reassessment_without_persistence(self):
        samples=[(),('SURFACE',),('RELATION','SYSTEM'),('CLOSURE','RECEPTION'),()]
        expected=[set(),{AP},{MCA,WIL},{NR,AR,MCA},set()]
        for exposure, wanted in zip(samples,expected):
            result=production_spec(exposure)
            self.assertEqual(verified(result),wanted)
            self.assertFalse(result['forced']); self.assertTrue(result['gate_evaluated'])
        for force in (False,True):
            parts=[('USER_DIRECTIVE','/AD')] if force else []
            result=production_spec(('SURFACE',),parts=parts)
            self.assertEqual(verified(result),{AP})
            self.assertFalse({MCA,WIL,AR,NR} & set(result['artifact_requests']))

    def test_all_selection_combinations_and_dependency_closure(self):
        # All 32 combinations permitted; no live A/B masks or global execution sequence.
        for n in range(6):
            for chosen in itertools.combinations(IDS,n):
                expected=set(chosen) | ({MCA} if AR in chosen else set())
                result=production_spec([EXPOSURES[i] for i in chosen])
                self.assertEqual(verified(result),expected,chosen)
                self.assertFalse(result['blocked'])
        for identity in (MCA,WIL,NR):
            self.assertEqual(verified(production_spec([EXPOSURES[identity]])),{identity})
        pair=production_spec(['RECEPTION'])
        self.assertEqual(pair['direct_dependencies'],[((PACKAGE,AR),(PACKAGE,MCA))])
        self.assertNotIn(WIL,pair['artifact_requests'])

    def test_failed_library_read_isolates_dependents_without_fallback(self):
        def missing(f,identity): f['artifacts'].pop(identity)
        def unread(f,identity): f['artifacts'][identity][0]['read_kind']='SNIPPET'
        def wrong_version(f,identity): f['artifacts'][identity][0]['version']='old'
        def wrong_status(f,identity): f['artifacts'][identity][0]['status']='INACTIVE'
        def wrong_body(f,identity): f['artifacts'][identity][0]['decisions']={'material_contract':'mismatch'}
        def wrong_root(f,identity):
            next(row for row in f['local_catalogs'][PACKAGE] if row['module_id']==identity)['location']['root']='Other root'
        def duplicate(f,identity): f['artifacts'][identity].append(copy.deepcopy(f['artifacts'][identity][0]))
        for identity, failure in itertools.product(IDS,(missing,unread,wrong_version,wrong_status,wrong_body,wrong_root,duplicate)):
            with self.subTest(identity=identity,failure=failure.__name__):
                result=production_spec(list(EXPOSURES.values())+['CREATIVE'],parts=[('USER_DIRECTIVE','/AD')],alter=lambda f:failure(f,identity))
                self.assertIn((PACKAGE,identity),result['blocked'])
                if identity == MCA: self.assertIn((PACKAGE,AR),result['blocked'])
                independent=set(IDS)-{identity}-({AR} if identity==MCA else set())
                self.assertTrue(independent <= verified(result))
                self.assertIn('HUB-DOM-CREATIVE',verified(result))
                self.assertFalse(result['runtime_ready'])
                self.assertFalse(any('archive' in str(x).lower() or 'FTH_' in str(x) for x in result['artifact_requests']))

    def test_selected_material_body_and_full_read_under_exact_library_contract(self):
        local=load(ROOT/'library_modules/HUB-CATALOG-CONCEPT-DEVELOPMENT_v1.4.yaml')
        for row in local['entries'][3:]:
            entry=dict(row,entrypoint_module_id=row['module_id'],binding_mode='LIBRARY_MODULE')
            record=dict(module_id=row['module_id'],package_id=PACKAGE,runtime_role=row['runtime_role'],
                        status='ACTIVE',version=row['version'],root='Central Hub Config',location='LIBRARY',
                        read_kind='FULL_FILE',has_more=False,body_matches=True,opened_object='SYNTHETIC_OBJECT')
            result=integration_read_spec(entry,[record],direct_identity_usable=False,scoped_search_sufficient=True)
            self.assertFalse(result['runtime_ready'])
            self.assertEqual(result['live_integration'],'NOT_RUN')
            for field,bad in [('body_matches',False),('has_more',True),('opened_object',None),
                              ('location','REPOSITORY'),('version','old'),('root','Other root')]:
                with self.subTest(identity=row['module_id'],field=field),self.assertRaises(Closed):
                    integration_read_spec(entry,[dict(record,**{field:bad})],
                                          direct_identity_usable=False,scoped_search_sufficient=True)

    def test_inactive_selected_dependency_not_bypassed_by_force(self):
        def inactive(f):
            next(row for row in f['local_catalogs'][PACKAGE] if row['module_id']==MCA)['status']='INACTIVE'
        result=production_spec(['RECEPTION','SYSTEM'],parts=[('USER_DIRECTIVE','/AD')],alter=inactive)
        self.assertIn((PACKAGE,AR),result['blocked'])
        self.assertIn(WIL,verified(result)); self.assertNotIn(AR,verified(result))

    def test_author_corpus_complete_and_composable(self):
        self.assertEqual([row[0] for row in CORPUS],[f'{letter}{i:02}' for letter,count in [('A',11),('B',14),('C',9)] for i in range(1,count+1)])
        notes=(ROOT/'tests/CONCEPT_ANTI_DRIFT_TEST_CASES.md').read_text(encoding='utf-8')
        for case,problem,features,counterexample in CORPUS:
            with self.subTest(case=case):
                result=production_spec(features)
                expected={i for i,f in EXPOSURES.items() if f in features}
                if AR in expected: expected.add(MCA)
                self.assertEqual(verified(result),expected)
                self.assertIn(f'| {case} |',notes)
                self.assertIn(problem,notes); self.assertIn(counterexample,notes)
                self.assertFalse(result['runtime_ready'])

    def test_generation_latitude_and_counterexample_contracts(self):
        # Reviewed semantic requirements, not an executable classifier of generated prose.
        guards={
          AP:['non-implications, never prohibitions or inverted priors','Preserve explicit user/ontology-defined links','subtle magic is not inherently stronger','AUTHORIZED INVENTION != UNSUPPORTED PRIOR SUBSTITUTION'],
          MCA:['CAPABILITY EXISTS != CAPABILITY USED PERFECTLY','No combat simulator or plot coordinator','Do not require every skill','deliberate reserve','Off-screen does not imply activity','preserve explicit ontology-defined mappings'],
          WIL:['Ignorance, inability or lack of access is not a political choice','bounded institution abstraction may suffice','Do not manufacture bureaucracy','ASSET != LIQUIDITY','AGREEMENT != IMPLEMENTATION'],
          AR:['not compulsory belief reversal','correlated/non-independent','Public statement may diverge from private belief','Missing receipt is a bounded unknown','Do not choose an actor\'s action','PAST-LIFE HARM != PRESENT-LIFE GUILT'],
          NR:['an open ending can be intentional','Do not enforce immediate closure','No mandatory difficulty, new cost','easy victory may be earned','retain deferred consequences','No hard Requires']}
        for identity,clauses in guards.items():
            text=(ROOT/f'library_modules/{identity}_v{VERSIONS[identity]}.md').read_text(encoding='utf-8')
            for clause in clauses: self.assertIn(clause.lower(),text.lower(),(identity,clause))
        core=(ROOT/'library_modules/HUB-DOM-CONCEPT-DEVELOPMENT_v1.4.md').read_text(encoding='utf-8')
        for clause in ['UNKNOWN explicitly assigned to Creative may be developed','Brainstorm may mutate delegated assumptions','Debate may formulate hypotheses/objections without canon mutation','Fix an overreaching control rather than weakening an operation leaf']:
            self.assertIn(clause,core)
        # No material exposure in pure imagery, an explicit trope, authorized blank-slate invention,
        # or a complete supplied relation with no threatened substitution: valid empty selection.
        for task in ('pure imagery','explicit trope','blank-slate invention','supported complete premise'):
            self.assertEqual(verified(production_spec(())),set(),task)

    def test_root_single_cue_and_operation_leaves_unchanged(self):
        root=load((ROOT / 'Source_archive/Production corrections 2026-11-08')/'HUB_PACKAGE_CATALOG_v1.11.yaml')
        package=next(p for p in root['packages'] if p['package_id']==PACKAGE)
        self.assertIn('/AD',package['applicability']); self.assertIn('NONE',package['applicability'])
        for identity in IDS:
            self.assertNotIn(identity,str(root))
        before=load(HISTORY/'HUB_PACKAGE_CATALOG_v1.10.yaml')
        self.assertEqual([p for p in root['packages'] if p['package_id']!=PACKAGE],
                         [p for p in before['packages'] if p['package_id']!=PACKAGE])
        local=load((ROOT / 'Source_archive/Production corrections 2026-11-08')/'library_modules/HUB-CATALOG-CONCEPT-DEVELOPMENT_v1.2.yaml')
        old=load(HISTORY/'library_modules/HUB-CATALOG-CONCEPT-DEVELOPMENT_v1.1.yaml')
        self.assertEqual(local['entries'][:3],old['entries'][:3])
        for identity,version in [('HUB-DOM-CREATIVE','1.1'),('HUB-CAP-BRAINSTORM','1.1'),('HUB-CAP-DEBATE','1.0')]:
            rel=f'library_modules/{identity}_v{version}.md'
            previous=subprocess.check_output(['git','show',BASELINE+':Central Hub/'+rel],cwd=ROOT)
            self.assertEqual((ROOT/rel).read_bytes(),previous)
        router=((ROOT / 'Source_archive/Production corrections 2026-11-08')/'HUB_ROUTER_v1.1.yaml').read_bytes()
        self.assertEqual(router,(HISTORY/'HUB_ROUTER_v1.1.yaml').read_bytes().replace(b'1.10',b'1.11'))

    def test_predecessor_receipts_and_successors(self):
        receipt=json.loads((HISTORY/'ARCHIVE_RECEIPT.json').read_text(encoding='utf-8'))
        for rel,digest in receipt.items():
            self.assertEqual(hashlib.sha256((HISTORY/rel).read_bytes()).hexdigest(),digest)
            original=subprocess.check_output(['git','show',BASELINE+':Central Hub/'+rel],cwd=ROOT)
            self.assertEqual((HISTORY/rel).read_bytes(),original)
            if rel not in {'HUB_ROUTER_v1.1.yaml','tests/CONCEPT_ANTI_DRIFT_TEST_CASES.md'}:
                self.assertFalse((ROOT/rel).exists())
        for identity in IDS:
            data=(ROOT/f'library_modules/{identity}_v{VERSIONS[identity]}.md').read_bytes()
            self.assertFalse(data.startswith(b'\xef\xbb\xbf')); self.assertNotIn(b'\r',data)
            self.assertTrue(data.endswith(b'\n'))
            self.assertFalse(any(line.rstrip()!=line for line in data.decode('utf-8').splitlines()))


if __name__=='__main__':
    unittest.main()

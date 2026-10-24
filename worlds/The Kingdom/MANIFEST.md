# The Kingdom — Package Manifest v1.0

Status: ACTIVE
Version: 1.0
Role: PACKAGE_INTEGRITY

## Scoped Admission

This contract admits files for package management, not canon. Add a material owner through scoped author decision/review, its complete header, and explicit admission; --write cannot admit or create owners. SOURCE_ID remains stable through renaming. Router declares control families/dependencies and selects the highest ACTIVE numeric version; maintenance checks compatibility before runtime. No runtime dependency on Global/FTH files is introduced.

runtime_source_package names the exact Library folder "TK Source" and expected current lore/bootstrap paths. Controls and maintenance files are excluded from that runtime lore package. A Library/Project location grants no authority; an external matching name grants no current identity. The repository is maintenance state, not proof of Library contents or synchronization. contents_verified is false; synchronization and live deployment remain NOT_PERFORMED. Future admitted owners join the expected paths through scoped maintenance, without placeholder files or a repository TK Source directory.

<!-- BEGIN PACKAGE CONTRACT -->
```json
{
  "version": "1.0",
  "status": "ACTIVE",
  "sources": [
    "TK_DOMAIN_COUNTERINTELLIGENCE.md",
    "TK_DOMAIN_GEOPOLITICS.md",
    "TK_DOMAIN_HEALTH.md",
    "TK_DOMAIN_INFRASTRUCTURE.md",
    "TK_DOMAIN_LANGUAGE_RELIGION.md",
    "TK_DOMAIN_LAW.md",
    "TK_DOMAIN_OPENING_DELEGATION.md",
    "TK_DOMAIN_POT.md",
    "TK_METHOD_FICTION.md",
    "TK_METHOD_POV_PERSPECTIVE.md",
    "TK_TIMELINE_CP01_OPENING.md",
    "TK_TIMELINE_CP02_REVEAL.md",
    "TK_TIMELINE_INTERVAL_CP01_CP02.md",
    "TK_TIMELINE_POST_CP02.md"
  ],
  "navigation": [
    "README.md",
    "TK_CURRENT_SOURCE_INDEX.md",
    "THE_KINGDOM_CHECKPOINT_STATE_INDEX.md"
  ],
  "records": [
    "TK_RECONCILIATION_RECORD.md",
    "TK_OPEN_ISSUES_CURRENT.md"
  ],
  "support_controls": [
    "controls/multi_paracosm_hub_workflow.md",
    "controls/TK_WORLDBUILDING_STRESS_TEST.md"
  ],
  "maintenance": [
    "tools/validate_kingdom_package.py",
    "tests/test_kingdom_package.py",
    "tests/control_cases.json"
  ],
  "runtime_source_package": {
    "library_folder": "TK Source",
    "paths": [
      "TK_CURRENT_SOURCE_INDEX.md",
      "TK_OPEN_ISSUES_CURRENT.md",
      "TK_RECONCILIATION_RECORD.md",
      "THE_KINGDOM_CHECKPOINT_STATE_INDEX.md",
      "TK_DOMAIN_COUNTERINTELLIGENCE.md",
      "TK_DOMAIN_GEOPOLITICS.md",
      "TK_DOMAIN_HEALTH.md",
      "TK_DOMAIN_INFRASTRUCTURE.md",
      "TK_DOMAIN_LANGUAGE_RELIGION.md",
      "TK_DOMAIN_LAW.md",
      "TK_DOMAIN_OPENING_DELEGATION.md",
      "TK_DOMAIN_POT.md",
      "TK_METHOD_FICTION.md",
      "TK_METHOD_POV_PERSPECTIVE.md",
      "TK_TIMELINE_CP01_OPENING.md",
      "TK_TIMELINE_CP02_REVEAL.md",
      "TK_TIMELINE_INTERVAL_CP01_CP02.md",
      "TK_TIMELINE_POST_CP02.md"
    ],
    "contents_verified": false,
    "synchronization": "NOT_PERFORMED",
    "deployment": "NOT_PERFORMED"
  }
}
```
<!-- END PACKAGE CONTRACT -->

## Maintenance and Evidence

python -B tools/validate_kingdom_package.py --check is the read-only default. --write updates only GENERATED SOURCE CATALOG in the current index and GENERATED HASHES below after structural validation. It never writes lore, repairs source claims, moves files, infers canon/dependencies, or promotes archives. Staleness must be reported; review it, perform the scoped write, then check again. Concurrent input changes block writing. Two atomic file replacements are not a power-loss transaction; subsequent checks detect an interrupted update.

Source_archive is excluded from current discovery, hash refresh, source loading, and regeneration. Historical provenance links are not build inputs. Rollback uses Git history. Read-only attributes do not create semantic authority. This manifest does not hash itself; validation checks the manual contract, and hashes cover the other admitted current inputs.

PyYAML is required for Router parsing and is already present in the task environment. YAML anchors, aliases, merge keys, and custom tags are prohibited; version strings are explicit. There is no model runner. Structural success does not prove semantic compliance, Library retrieval, synchronization, or live deployment.

<!-- BEGIN GENERATED HASHES -->
| File | SHA-256 |
| --- | --- |
| `README.md` | `a282fbcde1a0a525adf27d827d925fe6d7445784b816c26c4e7bd6ff3340462b` |
| `THE_KINGDOM_CHECKPOINT_STATE_INDEX.md` | `5256996f629abcbf12d9a9ef9cc225bfbdc7cedf20facc6b4d0a78ca56820735` |
| `TK_CURRENT_SOURCE_INDEX.md` | `7f50071f80648308090c1d98570e485408f7425827c65224b52705c03c064999` |
| `TK_DOMAIN_COUNTERINTELLIGENCE.md` | `f15140c6578474916880d264a545a287d1b057d5ba64fda46142c57dcdb88b7b` |
| `TK_DOMAIN_GEOPOLITICS.md` | `16f15eb9f3b4edf3602f28f8b77eab9f3c672edc7d1304e20e3b1a27d2b57754` |
| `TK_DOMAIN_HEALTH.md` | `a0f530533d7a4f27a8f3a87f06658ff2d50a252ad757d8b029e3a07fb16968cc` |
| `TK_DOMAIN_INFRASTRUCTURE.md` | `175e0b01fc5a8be89084deb99bc895901766a5f939ed1bb8e57df00b8f9abfae` |
| `TK_DOMAIN_LANGUAGE_RELIGION.md` | `edb028f772a6f270dfba61d7e85fbbaec83bee24d1f5fde8e51f413dcb92b67b` |
| `TK_DOMAIN_LAW.md` | `67d76344eebc2df7fe5f214a8b9478bf7f1694a6dffd64232c8c2001872dcfd1` |
| `TK_DOMAIN_OPENING_DELEGATION.md` | `e28394ec1ae925d3222faa7c084e0ad541485d03320fc5071f13e9095338e752` |
| `TK_DOMAIN_POT.md` | `a41b9afdcc326ce7a125ceda4234222045a872c3cff1cc8ad903dc2d559a0721` |
| `TK_METHOD_FICTION.md` | `fc34a7842e89fe0f9ea008fd198a51b9e75ccd32a6321125f5eb81bed9992dda` |
| `TK_METHOD_POV_PERSPECTIVE.md` | `5e127bfb274ae89bbf31d3ff7c06457d47b15b45a2002fda662366ff6a956618` |
| `TK_OPEN_ISSUES_CURRENT.md` | `803d04ac98a3b14595d55d3d77b9d994c7516c4db1f015e927dc1ec2657dfc83` |
| `TK_RECONCILIATION_RECORD.md` | `fa2a73f8a9e06e13bd95a549567c0b08f1ff75d431caec066ce46119e5d39c62` |
| `TK_TIMELINE_CP01_OPENING.md` | `4a24f8b0eab8f02bdf6bfcd0944eea0b5c4b8a9325b44d71c0a7a0a70349e520` |
| `TK_TIMELINE_CP02_REVEAL.md` | `f8089d0589a967bf95d1f580f37d24650fd19807c584f95f35c847f3f591a3bd` |
| `TK_TIMELINE_INTERVAL_CP01_CP02.md` | `601c2a52439ec8601b8d86ca9b6f0d8704bafda2d04d560e67f3abb5f302d435` |
| `TK_TIMELINE_POST_CP02.md` | `55966b5fbb9bc3321d6685d70fda61b1a6c2757518342ddbac26e41d837c4c7f` |
| `controls/TK_AUTHORING_PIPELINE_v1.0.md` | `b140687b1dd714630178e4d128edeaa5148329bbeadee09d0545f0535caff62b` |
| `controls/TK_CI_v1.0.md` | `83dcc8b1bdcd6aa1dec1edeb9d550476c58daa96300855fc56e108d6fd870eec` |
| `controls/TK_CONTROL_VOCABULARY_GLOSSARY_v1.0.md` | `bb818a1d0ad826f0538666100105b9d84c978c9fc1f873aa85269b3ccebe3f95` |
| `controls/TK_ROUTER_v1.0.yaml` | `f6346489d314544d11a13dd169b18bd401564dbf4c3fbec8ddf3d5399d0a352c` |
| `controls/TK_WORLDBUILDING_STRESS_TEST.md` | `97ad8299efe3b0da91471581490e4a3db46aa26fc331ea29b4c930883669591e` |
| `controls/anti_drift/TK_Anti_Drift_Actor_Knowledge_Reception_Model_Update_v1.0.md` | `58cc4576bbcef1e6e689ab98c499e62b93f4ef4d4943729910bd525052bef33d` |
| `controls/anti_drift/TK_Anti_Drift_Belief_Culture_Divinity_v1.0.md` | `8613bd08673b1f69b1fa6ea11760eb19250a78a29717ed890bd2f481b843ba5d` |
| `controls/anti_drift/TK_Anti_Drift_Economy_Trade_Abundance_v1.0.md` | `52fed871d6e3d411a165a55cab9ab4c3bf43d2abbb33bc18877702309b98e3e3` |
| `controls/anti_drift/TK_Anti_Drift_IRL_Baseline_Divergence_v1.0.md` | `434821d77757109260e4b89d65dbb27ebce74e811b4f0bb0c4121e60d6aa3714` |
| `controls/anti_drift/TK_Anti_Drift_State_Relation_Architecture_v1.0.md` | `7b4010c4a8fab7704473ed99f2254a470ed5ca74b38937b91859690e27ee25ff` |
| `controls/anti_drift/TK_Anti_Drift_Strategic_Crisis_Conflict_v1.0.md` | `a3febcc6fe20e480d5565d6f7a7c284fb94c2bdbcff94841f39d2e8b0ef3b076` |
| `controls/anti_drift/TK_Anti_Drift_Temporal_World_State_v1.0.md` | `b9ab2e43227f3892de7674f8bc365acc06ced701fa8c809dd9ae39f0a083f97c` |
| `controls/anti_drift/TK_Anti_Drift_World_Institutional_Logic_v1.0.md` | `15114721dff8407dab21482b22612b996470df117dc1c64cfc6e726fe0242827` |
| `controls/anti_drift/TK_Anti_Drift_World_State_Narrative_Assumption_Failure_v1.0.md` | `32129dd0fd05ccdfa6be1d02afc11b0adf0f8144c9566220d87d800c1aafe731` |
| `controls/multi_paracosm_hub_workflow.md` | `2d401ad6a0981062f60de21d85531905fc09c88c58f66ec2170268c48c492430` |
| `tests/control_cases.json` | `f4b63f8f0bb5b59e79c0be94639e3bf00e86781a743912da0d9107ba30ed5241` |
| `tests/test_kingdom_package.py` | `165d20dc4252a702d974588d35520222b688bd6ab8d5f08ab79d2aa7effa56ab` |
| `tools/validate_kingdom_package.py` | `26a22b5b69f9b5d112fc04fe14749b7c575561f727d6fde3c583ca2c69c2c607` |

<!-- END GENERATED HASHES -->

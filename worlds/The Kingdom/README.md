# The Kingdom

The Kingdom is the project/paracosm. Hyperborea is the country within it. The previous country placeholder is retired in current sources and preserved only in history/provenance. Renaming the country does not change TK-* source identities.

This is personal worldbuilding centered on a moving world and accumulated consequences. Characters provide cameras; there is no central protagonist. The repository externalizes only part of the author's world. Missing repository detail does not establish missing author knowledge. Lore bodies retain their source language; control and management artifacts use English.

## Source Layout and Authority

Current owners remain at the package root as TK_TIMELINE_*, TK_METHOD_*, and TK_DOMAIN_* files. [Current discovery](TK_CURRENT_SOURCE_INDEX.md) lists admitted identities/scopes. [Temporal navigation](THE_KINGDOM_CHECKPOINT_STATE_INDEX.md) keeps boundaries separate from persistent domains. [Reconciliation](TK_RECONCILIATION_RECORD.md) tracks accepted changes/provenance; [open issues](TK_OPEN_ISSUES_CURRENT.md) retain unresolved states; [manifest](MANIFEST.md) admits package paths and integrity metadata.

ACTIVE identifies a source/control role, not acceptance of all proposals or simulations inside it. Keep CANON, USER-PROVIDED STATE, DECIDED, PROPOSAL, UNDER CONSIDERATION, INFERENCE, UNKNOWN, STALE, and CONFLICTED distinct. Source detail and explicit scoped author decisions retain their authority. Neither index, manifest, nor directory location canonizes content.

Source_archive is historical provenance, not current authority, fallback, or regeneration input. Do not use it to fill a gap in active sources. Read a historical record only under explicit history/provenance/audit/recovery scope or when a current source identifies the relevant comparison. Archive files remain byte-exact.

## Library Runtime Contract

The exact ChatGPT Library folder is **"TK Source"**. This is a Library location, not a repository directory. Normal lore access order:

1. Library folder "TK Source".
2. Project Sources / explicitly supplied current project files.
3. Explicitly authorized task-local external source.

The expected Library package contains TK_CURRENT_SOURCE_INDEX.md, TK_OPEN_ISSUES_CURRENT.md, TK_RECONCILIATION_RECORD.md, THE_KINGDOM_CHECKPOINT_STATE_INDEX.md, and all 14 admitted current timeline/method/domain owners. Future country/actor/event owners join only after material exists and scoped admission is accepted. The exact current path list is in the manifest's runtime_source_package contract. CI, Router, Pipeline, overlays, glossary, support controls, tests, and maintenance files remain outside this lore package.

LIBRARY LOCATION != CANON AUTHORITY. PROJECT SOURCE PRESENCE != AUTOMATIC AUTHORITY. EXTERNAL IDENTICAL NAME != SAME CURRENT SOURCE. Establish admitted identity, role, status, scope, owner boundary, reconciliation state, and author decisions at every access surface. An unavailable Library may lead to the next authorized surface; it does not authorize archive fallback or arbitrary external sources.

The repository is the maintenance/version-controlled implementation location. REPOSITORY PACKAGE != LIBRARY DEPLOYMENT STATE. Local source reads for this maintenance task do not prove runtime retrieval.

| Evidence | State |
| --- | --- |
| Router configured for Library "TK Source" | YES |
| Library folder/file presence inspected | NO |
| Library contents verified | NO |
| Library synchronization/upload | NOT_PERFORMED |
| Live ChatGPT Project deployment | NOT_PERFORMED |
| Live retrieval/model compliance | NOT_VERIFIED |

REPOSITORY ACTIVE != LIBRARY SYNCHRONIZED != LIVE PROJECT DEPLOYED.

## Native Runtime and Boundaries

PERSISTENT DOMAIN/ACTOR STATE + TEMPORAL WORLD STATE + CHECKPOINT/INTERVAL/EVENT DELTAS + ACTOR-SPECIFIC INFORMATION is TK-native. CP1 -> interval of approximately two years -> CP2 -> post-CP2 material. A checkpoint owns its direct boundary delta; an interval owns progression/accumulated state. Immediate S1 is not automatically final pre-CP2 state. Missing history is not permission to invent events.

WORLD TRUTH -> OBSERVABLE SLICE -> ACTOR INFORMATION -> MODEL -> DECISION -> ACTION -> INTERACTION -> NEW WORLD STATE. Each actor requires ACTOR + TIME + ACCESS PATH. Do not import future reveal into earlier knowledge or a universal reaction for humanity. [Fiction method](TK_METHOD_FICTION.md) preserves assumption/model failure without making actors stupid: CP1 estimation, CP2 reclassification, and post-CP2 cargo normality gap are authorial functions, not universal actor conclusions. CP3 remains UNDER CONSIDERATION without a current owner.

IRL REFERENCE @ TIME, TK DIVERGENCE, and ACTOR STATE @ T differ. A roughly 2003 baseline does not automatically become IRL 2026. [Law](TK_DOMAIN_LAW.md) retains reset/scoped foreigner recovery; domestic law is not designed. [Perspective method](TK_METHOD_POV_PERSPECTIVE.md) retains unaccepted design. [Delegation](TK_DOMAIN_OPENING_DELEGATION.md) retains draft itinerary. No UNKNOWN or CONFLICTED lore was resolved in this correction.

## Management Stack v1.0

All 13 versioned controls are ACTIVE in the repository, with no candidate lifecycle:

| Artifact | Responsibility |
| --- | --- |
| [CI](controls/TK_CI_v1.0.md) | Self-contained Global Native v9.0 semantics, task/stage/canon discipline, and Router entry. FTH CI 3.4 is structural reference only. |
| [Router](controls/TK_ROUTER_v1.0.yaml) | Access/discovery, owner/temporal gates, full reads, reconciliation routing, and numeric ACTIVE overlay/dependency selection. It never selects active CI at runtime. |
| [Pipeline](controls/TK_AUTHORING_PIPELINE_v1.0.md) | Requested transformations, early Router handoff, and stopping; no source authority. |
| [Glossary](controls/TK_CONTROL_VOCABULARY_GLOSSARY_v1.0.md) | Maintenance vocabulary; no runtime prerequisite. |
| Nine overlays in controls/anti_drift | TEMPORAL, ACTOR, RELATION, INSTITUTION, IRL, ECONOMY, BELIEF, CRISIS, NARRATIVE; selected semantically after source/reconciliation gates. |

```text
PROMPT_ROUTE_ONLY -> BOOTSTRAP_GATE -> OWNER_GATE -> TEMPORAL_GATE
-> SOURCE_LOAD -> RECONCILIATION -> ANTI_DRIFT_OVERLAY_GATE
-> PROMPT_EXECUTION -> PRE_RESPONSE_CHECK
```

Owner headers retain SOURCE_ID, RUNTIME_ROLE, ROLE, STATUS, SCOPE, AUTHORITY_BOUNDARY, CROSS_OWNER_BOUNDARY, and LOAD_MODE. v1.0 uses FULL_FILE only. Header/hit/summary/memory is not a full-read proof. Missing decisive input blocks dependent work; partial loading requires a named secondary gap unable to change the bounded conclusion. Shared management scale does not import FTH ontology.

## Maintenance and Evidence

From the repository root:

```powershell
python -B "worlds/The Kingdom/tools/validate_kingdom_package.py" --check
python -B -m unittest discover -s "worlds/The Kingdom/tests"
```

The validator defaults to read-only checking. After reviewing structural validity and staleness, --write updates only GENERATED SOURCE CATALOG in the current index and GENERATED HASHES in the manifest; run --check again. It never rewrites lore, admits sources, infers canon/dependencies, or rebuilds archives. PyYAML is required for Router parsing; the task environment already provides it. Numeric selection satisfies 1.9 < 1.10 and excludes every non-ACTIVE status.

Tests verify structural contracts and failures. Prompts in tests/control_cases.json are unexecuted model protocols, not semantic PASS evidence from substring checks. This task performs no Library upload, live deployment, Git stage, commit, push, branch switch, or tag. Rollback uses Git history, not archive regeneration.

The five superseded legacy controls remain in Source_archive/controls_legacy after the previously verified coverage migration. [Independent seed workflow](controls/multi_paracosm_hub_workflow.md) remains unchanged. [Stress-test questions](controls/TK_WORLDBUILDING_STRESS_TEST.md) remain a separate NOT_RUN verification aid, translated without becoming lore or a model test result.

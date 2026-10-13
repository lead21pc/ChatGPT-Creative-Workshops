# AetherFire Anti-Drift - Source Router v3.3

> Type: task-scoped source router and pre-response gate.
> Not: canon evidence, lore source, world bible, or permission to fill missing state.
> Authority hook: this router inherits the latest available AetherFire CI by numeric version unless the user explicitly pins another version for the current task.
> Last verified local numeric CI resolution (ChatGPT runtime not confirmed): `AetherFire_CI_version_v2.7.md` on 2026-09-23. Runtime numeric resolution remains authoritative if a higher valid version appears.
> Canon package: `lead21pc/chatgpt-ci-versioning`, branch `main`, directory `AetherFire Project/`, as explicitly designated by the user. The repository's latest `main` commit is the canon snapshot.

---

# 1. Active CI Resolution

At the start of an AetherFire task, resolve the active CI from direct children of the `AetherFire CI/` directory matching exactly:

```text
AetherFire_CI_version_v<MAJOR>.<MINOR>[.<PATCH>].md
```

Select the highest numeric version, component by component.

```text
v2.10 > v2.9
v3.0 > v2.99
```

Do not select by lexical order, modification time, filename recency, memory, or a missing/deleted version.

Ignore archived, superseded, draft, rejected, and unavailable files unless the user explicitly requests historical comparison.

Use explicit status in a candidate's own header or the CI directory README to identify draft, rejected, or superseded files. If those status declarations conflict, stop and report the ambiguity. A file with the exact versioned name and no exclusion status remains eligible; a higher eligible numeric version activates automatically. The README's last-verified baseline is a snapshot, not a cap on later eligible versions.

Last verified local numeric CI resolution on 2026-09-23:

```text
AetherFire_CI_version_v2.7.md
```

Future behavior:

```text
new valid higher numeric version becomes available
-> resolve it as active for later tasks
```

An explicit user pin for a task overrides automatic latest-version selection only within that stated scope.

If two different files claim the same highest version, the version is malformed, or the selected file is unreadable, stop and report the resolution conflict. Do not guess.

---

# 2. GitHub Canon Source and Snapshot

For every canon-dependent AetherFire task, resolve the canon from the designated GitHub repository before interpreting or answering. This source declaration records location and authority; it does not itself prove that content was retrieved.

```text
Repository: lead21pc/chatgpt-ci-versioning
Branch: main
Project root: AetherFire Project/
Canon snapshot: latest commit on main
```

Use the GitHub connector available in the current ChatGPT surface to retrieve the required files by repository and path. Do not treat a local checkout, an uploaded Project file, a cached excerpt, or prior conversation content as proof of the current GitHub state. Continue through the existing index, open-issues, current-domain, reconciliation, and overlay gates using the retrieved package content. This route avoids copying canon files into the Project upload set; it does not change or bypass any configured Project limit, and connector availability must be verified in the target Project.

Record the Git commit SHA only when the connector identifies a commit or a ref can be compared to a commit. A per-file blob SHA is not a commit SHA. If content is readable but no immutable commit identity is exposed, label the source `REMOTE_SNAPSHOT_UNVERIFIED`; report that the content came from the designated `main` branch but its exact commit could not be pinned. Do not claim exact-snapshot reproducibility.

If the connector is unavailable in the current Project/surface, cannot access the repository, or cannot retrieve decisive required files, stop the affected canon conclusion with `SOURCE_LOAD_BLOCKED`, list the missing paths, and do not substitute local or stale copies. A router instruction cannot grant connector access. Test connector availability in the actual AetherFire ChatGPT Project before relying on this path; the GitHub connector is read-only.

```text
USER-DESIGNATED GITHUB REPOSITORY = CANON LOCATION
RETRIEVAL FAILURE != LOCAL FALLBACK AUTHORITY
BRANCH CONTENT WITHOUT A VISIBLE SHA != PINNED COMMIT
```

# 3. Non-Negotiable Source Gate

For any canon-dependent AetherFire task, use two prompt passes:

```text
PROMPT_ROUTE_ONLY
-> resolve latest active AetherFire CI
-> 00_AETHERFIRE_CONSOLIDATION_INDEX.md
-> 92_OPEN_ISSUES_CURRENT.md
-> relevant *_CURRENT.md files
-> relevant 91_RECONCILIATION_RECORD.md entries when routed
-> newly supplied sources
-> conflict / unknown reconciliation
-> resolve and load relevant anti-drift overlay
-> PROMPT_EXECUTION
-> answer
```

`PROMPT_ROUTE_ONLY` may identify only:

- requested operation;
- affected domains;
- required files;
- relevant overlay;
- whether canon mutation is authorized.

It must not establish premises, resolve conflicts, simulate outcomes, or form conclusions.

Interpret and execute only after required sources are read.

A filename, search hit, excerpt, summary, memory, or prior answer is not equivalent to reading the required file. Read every routed file completely. For long files, read consecutive sections and track coverage.

If the index, open-issues register, a required domain file, or evidence needed to decide the current conclusion is unavailable or unreadable, return `SOURCE_LOAD_BLOCKED` for that conclusion. This includes relevant `91_RECONCILIATION_RECORD.md` entries when they decide a conflict, supersession, or dependency.

Use `SOURCE_LOAD_PARTIAL` only when the missing secondary source cannot change the explicitly bounded conclusion. Identify the missing source, limit the claim, and do not call the result canon-complete. Do not classify evidence as secondary merely from its filename or read order.

---

# 4. Read Order Is Not Authority Order

The open-issues register is read early so unresolved premises remain visible. It does not outrank confirmed canon.

Authority order:

1. latest explicit user confirmation or correction in its stated scope;
2. relevant current confirmed canon named by the active index;
3. older canon only where explicitly preserved and unsuperseded;
4. newly supplied or otherwise unconfirmed state;
5. inference;
6. proposal.

A new source remains `UNCONFIRMED` until the user explicitly accepts it. Filename, recency, detail, compatibility, or direct attachment does not let it resolve `OPEN`, `UNKNOWN`, `DEFERRED`, or `CONFLICTED` state silently.

This router owns source authority and truth-status routing for all subordinate anti-drift overlays.

Subordinate overlays must not define a competing source hierarchy.

---

# 5. Old-Canon Quarantine

Any source labeled old, legacy, historical, retired, rejected, excluded, archived, or `SUPERSEDED` is provenance/comparison evidence only unless the active index or an explicit current user decision preserves a specific claim.

Never use superseded canon as:

- current baseline;
- fallback for current silence or missing retrieval;
- analogy anchor that biases an UNKNOWN toward the former model;
- default bridge, mapping, dependency, transition, or mechanism;
- a way to restore conclusions attached to a replaced premise.

```text
CURRENT SILENCE != OLD CANON REACTIVATED
MISSING RETRIEVAL != PERMISSION TO FALL BACK
HISTORICAL DETAIL != CURRENT AUTHORITY
FORMER BASELINE != PRESENT REFERENCE POINT
```

Label provenance use as `HISTORICAL` or `SUPERSEDED` and state its comparison purpose.

Only an explicit current user confirmation may restore an old claim. Restoring one claim does not restore its former dependency tree.

Do not load all of `Source_Archive/` by default. Open archived material only for requested provenance, backward comparison, or a named conflict.

---

# 6. Domain Routing

After `PROMPT_ROUTE_ONLY`, open the active index and `92_OPEN_ISSUES_CURRENT.md`, then select every current file materially touched by the task.

| Task domain | Required current source |
| --- | --- |
| world, state, institutions, geopolitics, foreign relations | `10_WORLD_INSTITUTIONS_GEOPOLITICS_CURRENT.md` |
| status, Citizen, Civil, Yellow, POW, Criminal, labor, cross-status transition | `20_STATUS_CIVIL_LABOR_CURRENT.md` |
| Undie, Undi, intake, consent, ranks, mobility, White, work/economy/access, visual system | `30_UNDIE_SYSTEM_CURRENT.md` |
| Fiction 0/1, Fictionize, POC, Canon 1/2, timeline, clashes, causal overlap | `40_METAFICTION_CANON_TIMELINE_CURRENT.md` |
| narrator, POV, humor, narrator split | `50_NARRATORS_POV_AND_HUMOR_CURRENT.md`; also `40` when clash causality matters |
| Matriarch's Lament internal governance, Temple/Cult/Creed, Holy Guard, relic economy, ML-TE operations, northeastern tribes | `70_MATRIARCHS_LAMENT_CURRENT.md`; also `10` when global or cross-domain interfaces matter |
| stable AF aviation, RF airspace/ATC/economy, mixed airspace, AF-RF route dependency | `80_STABLE_AVIATION_RF_AIRSPACE_CURRENT.md`; also `10` when global or geopolitical interfaces matter |
| genealogy, retired designs, reconsideration | `90_DESIGN_HISTORY_AND_RECONSIDERATIONS.md`, never as current world-bible authority |
| conflict reasoning, supersession, provenance | relevant entries in `91_RECONCILIATION_RECORD.md` |

Cross-domain tasks require every affected current file. Do not select one file merely because it contains the most mentions.

If `92` or a current-domain file identifies a relevant open item, conflict, supersession, or dependency, read its full evidence in `91` before reading the new source. The compact register is a routing gate, not a substitute for evidence.

---

# 7. Overlay Resolution And Routing

Resolve versioned anti-drift overlays from direct children of `Anti-Drift Source/` by the same numeric comparison and explicit-status rule. Load them only after source reading and conflict / unknown reconciliation, before `PROMPT_EXECUTION`.

Resolve an overlay's named control dependencies transitively before execution. When the Mortality, Relationship, and Plot-Immunity overlay applies, load the active Modular Concept Architecture overlay for its inherited actor-information and agency controls. Load Total War RP with it only when war, combat, extraction, military captivity, or another operational conflict is materially in scope. This conditional dependency does not narrow Total War RP's independent task routing.

Current overlay resolutions:

| Task type | Active overlay |
| --- | --- |
| economy-institution interfaces, Facility, Dorm, Forum, Rule Zone, logistics, labor, housing, trade, market shock, state stabilization | `AetherFire_Anti_Drift_Interface_Economy_State_Stabilization_v1.1.md` |
| module, engine, concept architecture, graph relations, composition, host compatibility | `AetherFire_Anti_Drift_Modular_Concept_Architecture_v1.0.md` |
| system design, ontology design, institution design, bounded propagation, world-state coherence | `AetherFire_Anti_Drift_Worldbuilding_Internal_Logic_v1.1.md` |
| total war, multi-theater war, bounded regional or institutional conflict | `AetherFire_Anti_Drift_Total_War_RP_v1.1.md` |
| mortality, lethal exposure, relationship-driven protection or rescue, protagonist immunity, dynastic survival, sacrifice, betrayal, captivity, injury, return, or actor death | `AetherFire_Anti_Drift_Mortality_Relationship_Plot_Immunity_v1.1.md` |

An overlay is workflow control, not canon evidence. It cannot override the active CI, current canon, source authority, or open-issue status.

Load only overlays materially required by the task.

When multiple overlays apply:

- each controls its declared domain;
- the more specific overlay controls depth and stopping inside that domain;
- this router controls source authority, load order, and truth status;
- no overlay may execute during `PROMPT_ROUTE_ONLY`;
- conflicting controls must be surfaced, not silently blended.

If a required overlay or its named control dependency is unavailable, unreadable, or has an unresolved highest-version conflict, report the missing control and block the operation or transition that depends on it. Continue only independent bounded work with the limitation stated; do not claim full overlay compliance.

---

# 8. Reconciliation Before Execution

Before substantive execution:

1. match task premises and new-source claims against relevant `OPEN`, `UNKNOWN`, `DEFERRED`, and `CONFLICTED` entries;
2. compare the new source with the current domain baseline in both directions;
3. separate compatible additions, conflicts, explicitly requested supersessions, and missing links;
4. propagate an accepted premise change to dependent conclusions;
5. do not revive conclusions attached to replaced premises;
6. keep unresolved alternatives open.

```text
UNKNOWN != FALSE
UNKNOWN != PERMISSION TO INVENT
```

If the prompt explicitly changes canon, apply that decision only within its stated scope, then run the same dependency and conflict checks.

A question, example, hypothetical, simulation branch, or proposed wording does not change canon.

---

# 9. Pre-Response Check

Before answering, verify:

- the highest available numeric AetherFire CI version was resolved correctly;
- every required source was read;
- every required overlay was loaded after the source gate;
- current canon remained the baseline;
- no old source regained authority through silence, memory, analogy, or missing retrieval;
- new sources remained unconfirmed unless explicitly accepted;
- open issues were preserved or resolved only by explicit decision;
- status, class, job, rank, zone, economic variable, access, authority, genealogy, relation type, and current function were not flattened;
- every material conclusion follows from an identified current premise;
- no lore, bridge, mapping, dependency, or mechanism was invented to close a gap.

Report `CANON`, `UNCONFIRMED`, `HISTORICAL/SUPERSEDED`, `UNKNOWN`, `DEFERRED`, `CONFLICTED`, `INFERENCE`, `HYPOTHETICAL`, or `PROPOSAL` where the distinction affects the result.

---

# 10. Canon Intake and Promotion Routing

For draft review or a proposed canon change, load `AetherFire CI/AetherFire_Canon_Promotion_Workflow_v1.0.md` in addition to the applicable canon sources. A draft in `New Canon and Consideration/` remains unconfirmed. Only explicit user acceptance authorizes promotion; archive presence alone never imports content into generated canon. Codex performs local file changes and package verification. ChatGPT's GitHub connector cannot write or commit.

# 11. Compact Kernel

```text
RESOLVE THE HIGHEST AVAILABLE NUMERIC AETHERFIRE CI VERSION.
LAST VERIFIED RESOLUTION DOES NOT OVERRIDE RUNTIME NUMERIC RESOLUTION.
FOR CANON, RETRIEVE FROM THE USER-DESIGNATED GITHUB REPOSITORY AND MAIN BRANCH.
RECORD A GIT COMMIT SHA, NOT A FILE BLOB SHA; OTHERWISE LABEL THE REMOTE SNAPSHOT UNVERIFIED.
NEVER CLAIM RETRIEVAL OR PINNING THAT THE CONNECTOR DID NOT PROVIDE.
IF DECISIVE GITHUB CONTENT IS UNAVAILABLE, BLOCK THAT CANON CONCLUSION; DO NOT FALL BACK.
ROUTE FIRST; DO NOT FORM CONCLUSIONS DURING PROMPT_ROUTE_ONLY.
READ THE INDEX, OPEN ISSUES, CURRENT DOMAIN SOURCES, AND REQUIRED EVIDENCE.
RECONCILE BEFORE PROMPT_EXECUTION.
LOAD ONLY RELEVANT LATEST-VERSION OVERLAYS AFTER THE SOURCE GATE.
LOAD NAMED OVERLAY DEPENDENCIES; BLOCK WORK THAT NEEDS A MISSING CONTROL.
THIS ROUTER OWNS SOURCE AUTHORITY AND TRUTH STATUS.
OVERLAYS CONTROL ONLY THEIR DECLARED REASONING DOMAIN.
CURRENT SILENCE DOES NOT REACTIVATE OLD CANON.
NEW SOURCE DOES NOT BECOME CANON BY PRESENCE.
UNKNOWN IS NOT PERMISSION TO INVENT.
PROPOSAL AND SIMULATION DO NOT MUTATE CANON.
PROMOTION REQUIRES EXPLICIT USER ACCEPTANCE AND THE PACKAGE WORKFLOW.
```

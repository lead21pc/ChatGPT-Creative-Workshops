# AetherFire — Source Router & Anti-Drift v3

> **Role:** task-scoped source router and pre-response gate. This file controls workflow; it is not canon evidence and must not supply missing lore.
>
> **Active kernel:** `AetherFire_CI_version_v2.5.md`.
>
> **Canon package:** the separate `AetherFire Project/` directory.

## 1. Audit mode and token gate

For any canon-dependent AetherFire task, start with route-only classification. Do not establish premises, resolve conflicts, or form conclusions during routing.

```text
AUDIT_SCOPE
mode = LOOKUP | BOUNDED_AUDIT | FULL_SOURCE_AUDIT
target = named entity, claim, relation, file, or operation
canon_change = yes | no
sources_needed = exact files or source classes
stop_condition = answer bounded, target unresolved, or escalation reason found
```

Use the lightest sufficient mode:

| Mode | Use when | Required starting sources | Stop before expanding when |
| --- | --- | --- | --- |
| `LOOKUP` | answering a local question with no canon change | `00_AETHERFIRE_CONSOLIDATION_INDEX.md`, directly relevant `*_CURRENT.md`, and `92_OPEN_ISSUES_CURRENT.md` only if the target appears there | current canon gives a bounded answer or says `UNKNOWN`/`NOT ESTABLISHED` |
| `BOUNDED_AUDIT` | checking a named claim, relation, source, or narrow conflict | index, open issue entries for the target, relevant current files, and only routed evidence for that claim | the target claim is confirmed, contradicted, or remains unresolved |
| `FULL_SOURCE_AUDIT` | merging, retconning, editing canon, resolving provenance disputes, comparing raw sources, or handling confirmed current-canon conflict | full chain below | all material source classes are read or a required source is blocked |

Full chain, only when mode requires it:

```text
PROMPT_ROUTE_ONLY
→ 00_AETHERFIRE_CONSOLIDATION_INDEX.md
→ 92_OPEN_ISSUES_CURRENT.md
→ relevant *_CURRENT.md files
→ relevant 91_RECONCILIATION_RECORD.md entries when routed
→ named Source_Archive / supplied sources when material
→ task overlay when routed
→ PROMPT_EXECUTION
→ conflict/unknown reconciliation
→ answer
```

Before opening reconciliation evidence, Source_Archive, superseded canon, or any overlay, state why current canon is insufficient. Do not load all of `Source_Archive/` by default.

Reading a filename, search hit, excerpt, summary, memory, or prior answer is not equivalent to reading the required file. Read each routed file completely. If a file is too long, read it in consecutive sections and track coverage.

If an essential routed source is unavailable or unread, return `SOURCE_LOAD_BLOCKED`. If only secondary evidence is missing and an explicitly bounded result remains possible, return `SOURCE_LOAD_PARTIAL`, name the missing source, limit the claim, and do not call the result canon-complete.

## 2. Read order is not authority order

The open-issues register is a routing gate so unresolved premises cannot be forgotten. It does not outrank confirmed canon and need not be read in full for every `LOOKUP`; inspect only relevant entries unless the target is broad or ambiguous.

Authority order:

1. latest explicit user confirmation or correction in its stated scope;
2. relevant current confirmed canon named by the active index;
3. older canon only where it remains explicitly unsuperseded;
4. newly supplied or other unconfirmed state;
5. inference;
6. proposal.

A new source stays `UNCONFIRMED` until the user explicitly accepts it. Its presence, filename, recency, detail, or compatibility does not let it resolve `OPEN`, `UNKNOWN`, `DEFERRED`, or `CONFLICTED` items silently.

## 3. Old-canon quarantine

Any source labeled old, legacy, historical, retired, rejected, excluded, or `SUPERSEDED` is provenance/comparison evidence only unless the active index or a current explicit user decision preserves a specific unsuperseded claim.

Never use superseded canon as:

- the current baseline;
- a fallback when a current file is absent or silent;
- an analogy anchor that biases interpretation toward the old model;
- a default value, missing transition, bridge, mapping, or mechanism;
- evidence that an `UNKNOWN` answer should resemble the former canon;
- a way to restore dependent conclusions whose premise was replaced.

```text
CURRENT SILENCE ≠ OLD CANON REACTIVATED
MISSING RETRIEVAL ≠ PERMISSION TO FALL BACK
HISTORICAL DETAIL ≠ CURRENT AUTHORITY
FORMER BASELINE ≠ PRESENT REFERENCE POINT
```

If old material is relevant to provenance, label it `HISTORICAL` or `SUPERSEDED`, state the exact comparison purpose, and keep the current baseline primary. Only an explicit current user confirmation may restore an old claim. Restoration of one claim does not restore its former dependency tree.

The unversioned `aetherfire_chat_anti_drift.md` and `aetherfire_chat_anti_drift_v2.md` are inactive after v3 activation and excluded from the canon package. Do not use embedded snapshots as current canon.

## 4. Domain routing

After route-only classification, open the active index, then select current files materially touched by the request. Read `92_OPEN_ISSUES_CURRENT.md` only for relevant targets in `LOOKUP`, and fully enough for target coverage in `BOUNDED_AUDIT` or `FULL_SOURCE_AUDIT`.

| Task domain | Required current source |
| --- | --- |
| world, state, institutions, geopolitics, foreign relations | `10_WORLD_INSTITUTIONS_GEOPOLITICS_CURRENT.md` |
| status, Citizen, Civil, Yellow, POW, Criminal, labor, cross-status transition | `20_STATUS_CIVIL_LABOR_CURRENT.md` |
| Undie, Undi, intake, consent, ranks, mobility, White, work/economy/access, visual system | `30_UNDIE_SYSTEM_CURRENT.md` |
| Fiction 0/1, Fictionize, POC, Canon 1/2, timeline, clashes, causal overlap | `40_METAFICTION_CANON_TIMELINE_CURRENT.md` |
| narrator, POV, humor, narrator split | `50_NARRATORS_POV_AND_HUMOR_CURRENT.md`; also `40` when clash causality matters |
| genealogy, retired designs, reconsideration | `90_DESIGN_HISTORY_AND_RECONSIDERATIONS.md`, never as current world-bible authority |
| conflict reasoning, supersession, provenance | the relevant entries in `91_RECONCILIATION_RECORD.md` |

Cross-domain questions require all affected current files. Do not select a single file merely because it contains the most mentions of a term.

If `92` or a current-domain file identifies a relevant open item, conflict, supersession, or dependency, read its evidence in `91` only when the answer would otherwise rely on that unresolved point or when mode is `BOUNDED_AUDIT`/`FULL_SOURCE_AUDIT`.

For economy-institution interfaces, Facilities, Dorm, Forum, Rule Zone, logistics, labor, housing, trade, market shock, or state stabilization, load `aetherfire_anti_drift_interface_economy_state_stabilization.md` only after the canon source gate. It is a workflow overlay, not canon evidence, and cannot override current canon or open-issue status.

## 5. Reconciliation before execution

Before applying the prompt substantively:

1. Match the task premises and new-source claims against relevant `OPEN/UNKNOWN/DEFERRED` entries.
2. Compare the new source with the current domain baseline in both directions when new-source comparison is in scope.
3. Separate compatible additions, conflicts, supersessions requested by the user, and missing links.
4. Propagate an accepted premise change to dependent conclusions; do not revive conclusions attached to replaced premises.
5. Keep unresolved alternatives open. `UNKNOWN` is neither false nor permission to invent.

If the prompt explicitly changes canon, treat that explicit statement according to its exact scope, then run the same dependency and conflict checks. A question, example, hypothetical, or proposed wording does not change canon.

## 6. Pre-response check

Before answering, verify:

- the selected audit mode was sufficient and escalation was justified if used;
- every required source for that mode was actually read;
- the answer uses current canon as its baseline;
- no old source regained authority through silence, memory, analogy, or missing retrieval;
- new sources remain unconfirmed unless explicitly accepted;
- open issues were preserved or resolved only by an explicit decision;
- status, class, job, rank, zone, economic variable, access, authority, genealogy, and current function were not flattened;
- every material conclusion follows from an identified current premise;
- no lore, bridge, mapping, or mechanism was invented to close a gap.

Report `CANON`, `UNCONFIRMED`, `HISTORICAL/SUPERSEDED`, `UNKNOWN`, `CONFLICTED`, `INFERENCE`, or `PROPOSAL` where their distinction affects the result.

# AetherFire — Source Router & Anti-Drift v2

> **Role:** task-scoped source router and pre-response gate. This file controls workflow; it is not canon evidence and must not supply missing lore.
>
> **Active kernel:** `AetherFire_CI_version_v2.4.md`.
>
> **Canon package:** the separate `AetherFire Project/` directory.

## 1. Non-negotiable source gate

For any canon-dependent AetherFire task, use two prompt passes:

```text
PROMPT_ROUTE_ONLY
→ 00_AETHERFIRE_CONSOLIDATION_INDEX.md
→ 92_OPEN_ISSUES_CURRENT.md
→ relevant *_CURRENT.md files
→ relevant 91_RECONCILIATION_RECORD.md entries when routed
→ newly supplied sources
→ PROMPT_EXECUTION
→ conflict/unknown reconciliation
→ answer
```

The first prompt pass may identify only the requested operation, domains, named files, and whether the task may change canon. It must not establish premises, resolve conflicts, or form conclusions. Interpret and execute the request only after the required source reads.

Reading a filename, search hit, excerpt, summary, memory, or prior answer is not equivalent to reading the required file. Read each routed file completely. If a file is too long, read it in consecutive sections and track coverage.

If the index, open-issues register, or a required domain file is unavailable or unread, return `SOURCE_LOAD_BLOCKED`. If only a secondary source is missing and an explicitly bounded result remains possible, return `SOURCE_LOAD_PARTIAL`, name the missing source, limit the claim, and do not call the result canon-complete.

## 2. Read order is not authority order

The open-issues register is read first so unresolved premises cannot be forgotten. It does not outrank confirmed canon.

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

The unversioned `aetherfire_chat_anti_drift.md` is inactive and excluded from the canon package. Do not use its embedded snapshot as current canon.

## 4. Domain routing

After the route-only pass, open the active index and `92_OPEN_ISSUES_CURRENT.md`, then select every current file materially touched by the request:

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

If `92` or a current-domain file identifies a relevant open item, conflict, supersession, or dependency, read its full evidence in `91` before reading the new source. The compact register is a routing gate, not a substitute for required evidence.

For economy–institution interfaces, Facilities, Dorm, Forum, Rule Zone, logistics, labor, housing, trade, market shock, or state stabilization, load `aetherfire_anti_drift_interface_economy_state_stabilization.md` only after the canon source gate. It is a workflow overlay, not canon evidence, and cannot override current canon or open-issue status.

Do not load all of `Source_Archive/` by default. Open archived material only when the task requires provenance, backward comparison, or examination of a named conflict; label its role before using it.

## 5. Reconciliation before execution

Before applying the prompt substantively:

1. Match the task premises and new-source claims against relevant `OPEN/UNKNOWN/DEFERRED` entries.
2. Compare the new source with the current domain baseline in both directions.
3. Separate compatible additions, conflicts, supersessions requested by the user, and missing links.
4. Propagate an accepted premise change to dependent conclusions; do not revive conclusions attached to replaced premises.
5. Keep unresolved alternatives open. `UNKNOWN` is neither false nor permission to invent.

If the prompt explicitly changes canon, treat that explicit statement according to its exact scope, then run the same dependency and conflict checks. A question, example, hypothetical, or proposed wording does not change canon.

## 6. Pre-response check

Before answering, verify:

- every required source was actually read;
- the answer uses current canon as its baseline;
- no old source regained authority through silence, memory, analogy, or missing retrieval;
- new sources remain unconfirmed unless explicitly accepted;
- open issues were preserved or resolved only by an explicit decision;
- status, class, job, rank, zone, economic variable, access, authority, genealogy, and current function were not flattened;
- every material conclusion follows from an identified current premise;
- no lore, bridge, mapping, or mechanism was invented to close a gap.

Report `CANON`, `UNCONFIRMED`, `HISTORICAL/SUPERSEDED`, `UNKNOWN`, `CONFLICTED`, `INFERENCE`, or `PROPOSAL` where their distinction affects the result.

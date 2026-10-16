# Project Feather Core Anti-Drift - Source Router v4.4 (FTH)

> Status: FINAL LOCAL CONTROL FILE. Project use requires separate explicit deployment with the installed FTH CI 3.1 or 3.2; file presence does not deploy it.
> Type: task-scoped source router and pre-response gate.
> Not: canon, a lore source, a CI selector, or permission to complete missing world state.
> Authority: subordinate to the active installed FTH CI 3.1 or 3.2. If that CI is absent, ambiguous, or incompatible, return SOURCE_LOAD_BLOCKED for the dependent canon task. Do not select a CI from repository files or substitute CI 2.6.

## 1. Execution order

    ACTIVE FTH CI 3.1 OR 3.2
    -> this Router
    -> PROMPT_ROUTE_ONLY
    -> BOOTSTRAP GATE
    -> MODULE GATE
    -> SOURCE LOAD
    -> RECONCILIATION
    -> ANTI-DRIFT OVERLAY GATE
    -> PROMPT_EXECUTION
    -> PRE-RESPONSE CHECK

For a canon-dependent task, do not interpret source content or execute the requested analysis before its required source and control gates complete. Read order is not authority order. The Router selects and checks evidence; only an explicit user decision within its stated scope can change canon.

During PROMPT_ROUTE_ONLY identify only the requested operation, task scope, candidate modules or sources, relevant evidence and open state, required controls, and whether canon mutation is authorized. Do not establish a canon premise, resolve a conflict, simulate, select an outcome, or treat a module match as a conclusion. Re-route if later evidence expands the materially affected scope.

## 2. Bootstrap gate

For canon-dependent work, read the complete 00_AETHERFIRE_CONSOLIDATION_INDEX.md and 92_OPEN_ISSUES_CURRENT.md from one available current package generation. 00 supplies the global index and semantic boundaries; 92 exposes open state but does not resolve it or serve as a global dependency graph. If either is missing, unreadable, or materially inconsistent with the source generation, return SOURCE_LOAD_BLOCKED for conclusions needing that gate. Do not use an archive, memory, or another source as a replacement.

Use 00's current-file index and any reviewed module catalog it contains as discovery inputs. A catalog is a derived navigation view: it is not canon, module-metadata ownership, admission authority, or a dependency graph. A Project backend is not presumed able to enumerate all files or read every header. A path, search result, catalog row, or snippet does not establish that a source was read.

If 00 has no module catalog, use its existing indexed sources as a legacy FULL_FILE route. These unheadered sources are not silently converted into modules and gain no fabricated Module ID. Select every indexed current source materially affected by the task, including cross-domain owners; use 00 and the source's own authority boundary to distinguish current content from history. Do not claim discovery of sources absent from the index. This bridge permits present-package tasks without requiring a lore migration.

If a catalog exists but is stale, contradictory, or cannot be matched to the relevant headers/package generation, do not claim package-wide completeness. Bounded work may continue from explicitly known controlling FULL_FILE sources only when their identity, authority, and sufficiency are independently established. Otherwise block the dependent conclusion. An explicitly supplied uncatalogued source may be read for comparison as UNCONFIRMED; neither its header nor its presence makes it current canon.

## 3. Module Gate

For the bounded task:

1. Find candidate paths through 00's catalog or legacy index, 92 hooks, explicitly supplied sources, and the stated task scope. Scope matching only proposes a candidate.
2. For a module candidate, read its visible Markdown header and check Module ID, declared Runtime role, Domain / Scope, and any material Authority boundary. Check identity and admission against the current package and explicit user decisions. A missing or duplicate ID, unknown role, or conflict with package status requires REVIEW_REQUIRED; it cannot be admitted as current by guesswork.
3. Distinguish accepted current, user-provided but unconfirmed, historical/superseded, and mixed-status material. A header claiming CURRENT_SOURCE is not proof of current canon. Historical material claiming current status or a new module claiming an existing owner's scope without authority creates a conflict, not promotion.
4. Identify every materially affected controlling owner. Shared actors, events, interfaces, or mentions do not make sources one module, and a summary does not replace the owner of detail. If owner overlap cannot be resolved, read all known candidate owners in full and preserve the conflict; block the affected conclusion if authority remains uncertain.
5. Expand reviewed task-applicable MODULE_REQUIRES transitively. Check the target's identity, role, admission, and owner. Do not create an edge from a mention, keyword, chronology, proximity, similarity, shared actor, or shared institution. A missing, dangling, unreviewed, or unresolved cyclic hard dependency blocks the dependent operation; independent bounded work may continue.
6. Set the effective load mode for each controlling source, then record gaps and fallback before PROMPT_EXECUTION.

The minimal header contract is:

| Field | Runtime treatment |
| --- | --- |
| Module ID | Required for admitted modules; unique in the reviewed package, stable across path renames. |
| Runtime role | Required declaration; never self-grants effective truth status. |
| Domain / Scope | Required discovery boundary, not a claim of containment or complete coverage. |
| Authority boundary | Required for a current-source candidate when owner separation could affect the answer; unresolved omission blocks that authority claim. |
| Cross-domain owner boundary | Optional unless a known interface crosses controlling owners. |
| Load mode | Optional; absence means FULL_FILE. Only FULL_FILE and NODE_OR_FULL are understood. |
| Hard MODULE_REQUIRES | Optional, task-class-specific reviewed prerequisites; absence does not prove no other owner matters. |
| Local routing index status | Derived from review and package consistency, not a self-attested header authority. |

No header field may set canon rank, source priority, automatic admission, or automatic activation. A module can be a faction, institution, polity, region, actor, subsystem, or other scoped source without being placed in a parent-child lore tree. Adding a valid admitted module and updating the catalog/package must not require a Router-core edit or numeric filename convention. The Router's rules change only when the authority, discovery, or load-mode contract changes.

## 4. Module and node dependencies

MODULE_REQUIRES means another module is indispensable for a specified class of task. NODE_REQUIRES means one selected node lacks a decisive premise without another node. A node dependency may cross modules only after the target module's owner, status, and admission pass the Module Gate. Neither edge is inferred from co-occurrence.

An unreviewed possible edge is REVIEW_REQUIRED. For a node edge, use FULL_FILE of the affected controlling modules; if the suspected missing premise concerns an unavailable hard module or full source, block the dependent conclusion. A reviewed node closure is transitive. Cycles, missing targets, or disputed node boundaries invalidate node mode and require full-file fallback; they do not justify selecting one snippet.

## 5. Source load modes

FULL_FILE is the default and the safe fallback. Read every selected full file completely; for long files read consecutive sections and track coverage. A filename, header, index, search hit, excerpt, summary, memory, or prior answer is not a read.

NODE_OR_FULL is allowed only for a module and task class whose local routing index, node boundaries, decisive dependencies, and Project retrieval have been reviewed. The Router must actually load all of:

    mandatory module context
    + local routing index
    + target node
    + every reviewed NODE_REQUIRES target
    + all decisive qualifications, exceptions, priority, and open-state context

Call this VERIFIED_MODULE_CLOSURE only when that complete premise set and every controlling owner have been established and actually retrieved. The header or local validator cannot prove Project retrieval. If any component is missing, stale, ambiguous, duplicated, unreviewed, outside the observed retrieval, or possibly changed by a qualifier outside the selected nodes, expand a reviewed closure or read the affected full current file. A snippet-only return never licenses node reasoning.

Use FULL_FILE for broad audits, canon mutation, mixed-status sources, unresolved owner or authority conflicts, unreviewed modules, or a task whose decisive conditions cannot be safely bounded by nodes. An unknown Load mode falls back to FULL_FILE only if identity, role, admission, and owner remain clear; otherwise block the affected route. If a decisive full source is unavailable or unreadable, return SOURCE_LOAD_BLOCKED for its dependent conclusion. SOURCE_LOAD_PARTIAL applies only when a missing secondary source demonstrably cannot change an explicitly bounded conclusion; name the gap and do not claim complete canon coverage.

## 6. Source authority and reconciliation

The user's latest explicit confirmation or correction controls only its stated scope. Relevant accepted current canon controls its own domain; older unsuperseded material applies only where explicitly preserved. New or otherwise unconfirmed sources remain UNCONFIRMED. Inference and proposal are not canon. Source order, filename, recency, detail, compatibility, header validity, and catalog membership never reorder these authorities.

Read 91_RECONCILIATION_RECORD.md in full when a relevant conflict, supersession, priority addendum, provenance trail, or dependency could decide the task; read that evidence before evaluating a newly supplied source. Phase one has no record-only mode. If decisive 91 evidence is unavailable, return SOURCE_LOAD_BLOCKED for the dependent conclusion. 92 is an early routing gate, not a substitute for 91 or a controlling current source.

Before execution, compare task premises and new-source claims against relevant OPEN, UNKNOWN, DEFERRED, and CONFLICTED state in 92 and the controlling sources. Separate compatible additions, conflicts, explicit scoped supersessions, and missing links. Preserve unresolved alternatives. Propagate an accepted premise change only along real dependencies; do not revive conclusions attached to a replaced premise. A question, example, hypothetical, simulation, or proposed wording does not mutate canon.

Historical, retired, rejected, archived, and superseded sources are provenance or explicit comparison only. Current silence or failed retrieval does not reactivate them. They cannot become a present baseline, fallback, analogy anchor for UNKNOWN, or invented bridge. Interaction does not prove containment; co-occurrence does not prove dependency; genealogy does not prove hierarchy; power does not grant authority.

## 6A. External access and source authority

EXTERNAL CONNECTOR ACCESS != SOURCE AUTHORITY. For canon-dependent runtime, the normal trusted loading path is project-resident control sources plus exact routed current sources in Project Sources or ChatGPT Library, followed by the normal Router gates. By default, look for routed current sources, including required 00/92 and applicable 91, in ChatGPT Library's `Project Feather Core` folder first. This preserves Library retrieval and all identity, admission, owner, generation, read-mode, and reconciliation requirements; storage location alone grants no authority.

External connectors/providers, including GitHub, Google Drive, Dropbox, OneDrive, external apps, web search/pages, remote repositories, mirrors, synced copies, and archived cloud copies, cannot by default satisfy CURRENT_SOURCE, controlling-source requirements, current canon, or reconciliation authority. These are examples, not a provider registry. Apply this boundary to required gates, including 00/92 bootstrap and decisive 91 evidence. Without the explicit task-local authority authorization below, if a controlling current source is absent from Project Sources and ChatGPT Library, return SOURCE_LOAD_BLOCKED for the dependent conclusion; do not fall back to an external copy, even with an identical filename or content. Memory, prior chat, and inference cannot fill that authority gap. SOURCE_LOAD_PARTIAL retains its existing genuinely nondecisive-secondary-gap meaning.

An explicit request to read a named external source/connector permits reading only that source within the current task's requested scope. Classify it as external evidence/reference, not current canon, unless the user separately and explicitly authorizes that exact external material as authoritative for this task. Such authorization is task-local, still subject to the applicable read, reconciliation, and truth-status gates; it neither canonizes the material generally nor persists as a Router exception. Mere permission to inspect a repo or use a connector does not confer canon authority.

This governs authority, not visibility. Appropriate non-authoritative discovery, requested repo inspection/implementation, explicit provenance/history investigation, external-copy comparison/audit, ideation, design support, and cross-paracosm seed extraction may still use relevant non-module procedural/design/hub material. Do not restrict all reading to Router-listed files. In a comparison, the trusted current source retains its authority; external differences are comparison evidence. DISCOVERY != SOURCE LOAD; RETRIEVABLE != AUTHORITATIVE; CONNECTOR COPY != CURRENT_SOURCE; REPO COPY != RUNTIME CANON; VISIBLE / RETRIEVABLE MATERIAL != AUTHORIZED CURRENT SOURCE.

## 7. Anti-drift overlay gate

After source loading and reconciliation, select only overlays materially applicable to the task. Resolve each active version from direct children of Anti-Drift Source by the existing numeric and explicit-exclusion status rule; do not load archived, draft, rejected, or superseded copies as controls. If highest-version status is ambiguous, stop the dependent overlay operation rather than guessing. Load every selected overlay as FULL_FILE in this phase; never node-route an overlay.

Current control families cover economy/state-stabilization interfaces, modular concept architecture, mortality/relationship/plot immunity, total-war or bounded operational conflict, worldbuilding internal logic, actor reception of normative/social signals, belief/culture distinctions, and Undie professional/gray-zone reasoning. Apply each family's declared scope and exclusion hooks. Resolve named control dependencies transitively: mortality loads modular actor-information/agency controls; total-war is additionally required when war, combat, extraction, military captivity, or other operational conflict is material; worldbuilding work touching economy, labor, housing, trade, logistics, market shock, or stabilization also loads the economy overlay. Total-war retains its independent task routing.

Select Actor Reception Normative Signals when the answer depends on how an established actor receives, interprets, retains, or updates social/institutional signals, concurrent appraisals, or public expressions versus private intentions over time. Always load Modular Concept Architecture with it. Also load Worldbuilding Internal Logic for material institutional rule/jurisdiction/legitimacy/interpretation/enforcement reasoning; Total War RP for material command, military/operational information, conflict, emergency under conflict, or operational communication; and Interface Economy / State Stabilization for material scarcity, incentives, subsidy, procurement, intervention, economic pressure, or economically relevant temporary rule changes. These are task-scoped control prerequisites, not MODULE_REQUIRES edges or automatic full-domain activation. Sharing an actor alone activates none of the conditional dependencies. Reception uses already routed evidence and established actor state; source ownership never grants in-world knowledge or authority to the actor. Actor Reception does not route sources, select actions, or create a lore module.

Select Belief / Culture when a conclusion materially depends on doctrine versus practice, cultural extent or variation, transmission, cultural change, or symbolic meaning/recognition. Mentioning a religious or cultural label alone does not activate it; a direct sourced fact lookup need not load it. Load Actor Reception Normative Signals (and its required Modular Concept Architecture) when actor-specific receipt, appraisal, public/private belief, intentions, or updates are material; Worldbuilding Internal Logic when institutional operation, jurisdiction, authority, enforcement, social reproduction, or systemic persistence mechanisms are material; Interface Economy / State Stabilization when material/economic causal reasoning is needed; and Total War RP when operational conflict reasoning is needed. Apply those controls' existing scoped dependencies transitively. These are control prerequisites, not lore-module edges; none authorizes a full cultural audit or invented transmission history. Belief / Culture does not route sources or confer canon authority.

Select Undie Professional / Gray Zone when the answer materially depends on Undie affiliation, branches, entry/exit, intermediaries, contracts/obligations, gray activity, venues/booking/access, consent, Undi, stigma/scandal, resistance/security/intelligence interfaces, political consequences, or an actor's use of that ecosystem. A simple sourced mention alone does not activate it. Always load Modular Concept Architecture; resolve the overlay's declared Worldbuilding, Economy, Actor Reception, Belief / Culture, Mortality, and Total War dependencies only for their material reasoning domains, with existing dependencies transitively. These are control prerequisites, not lore-module edges. The overlay uses only routed/reconciled evidence, cannot establish its required professional baseline or fill missing world state, and selects no actor action or outcome. Mere scandal, criminality, or institutional rivalry does not by itself activate Total War; its independent task gates remain effective.

Overlays govern reasoning depth and stopping only in their declared domains; where several apply, the more specific overlay controls depth and stopping within that domain. This Router owns source authority, load order, truth-status routing, and overlay selection; overlays cannot override the installed CI, current canon, or open-state status. No overlay executes during PROMPT_ROUTE_ONLY. Surface an incompatible material control, block the dependent operation, and continue only independent bounded work with the limitation stated. If a required overlay or named dependency is missing or unreadable, do the same; do not claim full overlay compliance.

## 8. Failure order and coverage checks

Use the following order for each dependent conclusion:

    complete reviewed node closure actually retrieved -> NODE_OR_FULL
    node or retrieval uncertainty -> FULL_FILE of controlling sources
    decisive full source, 00/92 gate, 91 evidence, or hard module unavailable
      -> SOURCE_LOAD_BLOCKED
    genuinely nondecisive secondary gap -> SOURCE_LOAD_PARTIAL with stated bound

A stale catalog, malformed module identity/role, unresolved owner, or inconsistent generation cannot be repaired by choosing a newer file. If known controlling full sources can support only a narrower claim, state that bound; otherwise block. A missing required overlay blocks the operation that needs it. Never substitute historical material, memory, a nearby source, or invented relations for missing evidence.

Before PROMPT_EXECUTION and again before answering, check internally: task scope; selected controlling modules or legacy indexed files; effective role and admission evidence; owner boundaries; package/catalog generation if observable; chosen modes; actual FULL_FILE coverage or verified node closure; decisive 92 and 91 evidence; required overlays and their dependencies; unresolved gaps; and fallback/block state. A coverage receipt is an audit control, not lore. If the Router cannot honestly establish the full node closure, it must not claim VERIFIED_MODULE_CLOSURE.

Report CANON, UNCONFIRMED, HISTORICAL/SUPERSEDED, UNKNOWN, DEFERRED, CONFLICTED, INFERENCE, HYPOTHETICAL, or PROPOSAL where the distinction changes the result. Do not claim package-wide discovery or Project retrieval coverage that was not observed. Execute and answer only within the evidence and controls that passed these gates.

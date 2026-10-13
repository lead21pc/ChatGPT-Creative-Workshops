# Router 4.0 architecture proposal

Status: PROPOSAL ONLY, 2026-09-29. No live Router, CI, source, overlay, or Project instruction is changed by this package.

## Contract boundary

The candidate AetherFire CI 3.0 text exists at ../AetherFire CI/AetherFire_CI_v3.0_PROPOSAL.md. Its design report explicitly says it is not installed or runtime-tested. Every interface below that depends on CI 3.0 is PENDING CI 3.0 CONTRACT until the installed Project instruction text is inspected and the pair is approved. Router 4.0 receives control from CI; it never discovers, selects, or activates a CI file.

Router 3.2 is a historical comparator, not a required template. Keep its source-authority separation, old-canon quarantine, open-state handling, reconciliation-before-execution, overlay dependency gate, and bounded SOURCE_LOAD_BLOCKED/SOURCE_LOAD_PARTIAL behavior. Replace its numeric CI resolver and ordinary lore file/domain table. Do not edit Router 3.2.

## Proposed flow

    Installed AetherFire CI 3.0 [PENDING CI 3.0 CONTRACT]
      -> Router 4.0
      -> PROMPT_ROUTE_ONLY: operation, scope, candidate modules, evidence, controls
      -> BOOTSTRAP GATE: read 00 and 92 in full; establish package/catalog generation
      -> MODULE GATE: discover candidates; check role, admission, owner, status
      -> expand task-relevant MODULE_REQUIRES and all materially affected owners
      -> choose each module's effective load mode
      -> FULL_FILE or reviewed NODE_OR_FULL closure
      -> read decisive 91 evidence in full when conflict/provenance requires it
      -> reconcile current premises, open state, new sources, and supersession
      -> load applicable anti-drift overlays and control dependencies in full
      -> PROMPT_EXECUTION
      -> conclusion with source coverage and truth status

PROMPT_ROUTE_ONLY may identify possible sources but may not establish a canon premise, choose an outcome, or treat a module match as a conclusion. Source read order does not reorder authority. A module's header, path, catalog row, apparent recency, or valid syntax never promotes its claims.

## Bootstrap and discovery

00 remains a FULL_FILE global semantic boundary and active-index source. A generated module-catalog section is the preferred discovery view if a shadow build proves it can be produced from headers without replacing 00's existing semantic content. 92 remains a FULL_FILE open-state gate, not a global dependency graph. The catalog is navigation, not the owner of module metadata or canon authority. The effective admission of a module must trace to the active index/package and an explicit user decision where required.

No reliable ChatGPT Project primitive for enumerating all source files and reading every header has been established. Therefore a newly placed file is not automatically discoverable in Project runtime. Admission requires a valid header, catalog regeneration, review, and publication of one consistent package snapshot. If a relevant module is known to exist but the catalog is stale or cannot be checked, do not claim complete coverage; read the known source directly as an unconfirmed candidate or block the dependent current-canon conclusion.

## Module Gate

For the bounded task, the gate:

1. identifies candidate modules from 00's catalog, 92 hooks, explicitly supplied paths, and task scope;
2. reads candidate headers and verifies ID, declared role, scope, owner boundary, and package admission against the active snapshot;
3. separates CURRENT, unconfirmed, mixed-status, and historical/provenance material without inferring authority from metadata;
4. adds each materially affected controlling owner, even when no MODULE_REQUIRES edge was declared;
5. follows only reviewed, task-applicable hard MODULE_REQUIRES edges; unresolved, dangling, or cyclic edges require review and a safe fallback;
6. selects FULL_FILE unless node mode is both approved for that module/task class and actually retrievable with complete closure;
7. records what was loaded and what remains unverified before execution.

MODULE_REQUIRES means another module is indispensable for a specified task class. NODE_REQUIRES means a particular node lacks a decisive premise without another node. A mention, common actor, shared event, link, chronology, or similarity creates neither edge. The source layout is not an ontology or a parent-child hierarchy.

## Loading and reconciliation

FULL_FILE is the operational default. NODE_OR_FULL is a capability, not an instruction to prefer partial reads. A valid node read includes mandatory module context, local routing index, target node, every reviewed NODE_REQUIRES target, decisive qualifiers/exceptions/status, and evidence that the Project actually retrieved all of it. Any stale, missing, ambiguous, unreviewed, or unobservable component returns to the controlling full file. A missing decisive full source produces SOURCE_LOAD_BLOCKED; SOURCE_LOAD_PARTIAL applies only to a genuinely nondecisive secondary gap.

Read 91 in full in phase one when a cited conflict, priority change, or provenance record can decide the claim. Later RECORD_OR_FULL would need a separate test. Read each activated anti-drift overlay in full, after source reconciliation, with its named control dependencies. Overlays cannot change source authority or run during PROMPT_ROUTE_ONLY.

## Invariants and release boundary

INTERACTION != CONTAINMENT; CO-OCCURRENCE != DEPENDENCY; GENEALOGY != HIERARCHY; POWER != AUTHORITY. Cross-domain owner separation survives module growth. Current silence and failed retrieval never revive old canon. Unknown remains unknown. Simulation and proposal do not mutate canon.

Adding module E may update source files, metadata, the generated catalog, and reviewed tests; it must not require a Router-core branch or lore-tree refactor. A real change to authority semantics, load-mode contract, or discovery mechanism does require a new control review. Activation needs a separate, explicitly authorized task and a Project-runtime shadow test.

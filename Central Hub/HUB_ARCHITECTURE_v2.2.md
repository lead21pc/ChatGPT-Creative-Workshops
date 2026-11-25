# Central Hub shared architecture

Module ID: HUB-CORE-ARCH
Runtime role: CORE_ARCHITECTURE
Scope: shared topology, ownership, technical composition and contextual data interfaces
Status: ACTIVE
Version: 2.2

## Ownership

Hub CI governs turn function, operation, stage, truth/state, action authority, verification need and explanation. Hub Router selects and composes scoped package contributions and owns generic dependency, read and failure rules. Root and local Catalogs declare admission, identity and bindings. A package selects its own leaves and owns domain semantics and local execution state. A pipeline owns its internal procedure. The platform performs actual retrieval and tool calls.

Runtime controls use English. User content, quotes and human documentation follow their own language requirements. The controls are behavioral instructions. Selection is neither retrieval nor execution.

## Control sources and identity

Hub CI: HUB_CI_v2.1.md. Shared sources: HUB_ROUTER_v2.1.yaml, this Architecture and HUB_PACKAGE_CATALOG_v2.2.yaml. The accepted source set supplies exact bound artifacts; their availability does not establish selection or reading. Installation details belong in deployment documentation.

Apply Router's exact source and FULL_FILE checks. Package controls declare stable Module ID, Package ID, runtime role, scope, status and version; shared core controls may omit Package ID. Markdown headers and equivalent YAML keys carry the same meanings. A source path or storage surface confers no identity, role, dependency, activation or authority. Use one accepted binding per artifact, with no alias or dual active identity.

Canonical module IDs use HUB-<PACKAGE>-<ARTIFACT> or HUB-<PACKAGE>-<SUBDOMAIN>-<ARTIFACT>. Package tokens are TECH, AUTH, SHOP, FOOD and MEDIA. Subdomain labels are functional only. Root inventory binds accepted entrypoints; packages bind their own leaves. Artifact filenames use <Module-ID>_v<Version>.<extension>.

## Package interfaces

A singleton delegates directly to its entrypoint. A growing package uses the local selection interface it declares, with Catalogs for independently selected inventory where needed. Local inline selection can be sufficient for one optional procedure. Resolve only selected leaves and hard dependencies. Root admission and package execution remain distinct. No selected package grants permission to start another.

Shared roles include CORE_ARCHITECTURE, CORE_ROUTER, PACKAGE_CATALOG, DOMAIN_CONTROL, REASONING_PROFILE, CAPABILITY, DOMAIN_PROCEDURE, PREFERENCE and TOOL_PIPELINE. Roles describe responsibility, not priority. REFINES narrows only its matched scope. COMPLEMENTS joins independently applicable contributions. REQUIRES is an explicit hard dependency. Router owns closure, conflict validation and dependent failure.

## Continuity and scope

Keep the same conversation and reuse accessible, task-relevant outputs as scoped inputs. Preserve source role, qualifiers, evidence, current/provisional/rejected/open status and limits on changing them. Composition or output never grants authority or acceptance. Explicit task data flow creates no persistent mode or hard module edge. Keep locks, approval, provenance checks and domain-specific state with the owning module. Re-evaluate scope and refresh affected reads when their evidence no longer suffices.

## Core services by need

AIS binding: exact source tool_pipelines/AIS/AIS_PIPELINE_v2.0.md, Module ID HUB-CORE-AIS, role TOOL_PIPELINE, ACTIVE, version 2.0. Hub CI decides evidence need, Router dispatches and AIS owns evidence procedure. Hub and domain consumers interpret the scoped return. Core services do not require domain package selection.

Router emits scoped diagnostics from available routing and owner observations under its receipt trigger.

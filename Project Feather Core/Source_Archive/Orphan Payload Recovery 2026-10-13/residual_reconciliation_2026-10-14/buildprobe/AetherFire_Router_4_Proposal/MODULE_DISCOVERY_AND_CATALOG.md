# Header-driven, catalog-assisted discovery

Status: PROPOSAL ONLY. Project-wide file enumeration and exact header retrieval are UNVERIFIED RUNTIME ASSUMPTIONS. The repository can enumerate files; that does not establish a ChatGPT Project capability.

## Why a catalog is needed

The current 00 index names known files and carries global semantic and supersession boundaries. Router 3.2 names ordinary domains directly, and its table even omits the current file 60 that 00 lists. Replacing that table with a header scanner at runtime would assume the Project exposes all file names and complete headers. No such guarantee has been established. A bootstrap catalog gives the Router a finite list of candidate paths without embedding that growing list in Router core.

Prefer a generated module-catalog section in 00, not a new source file. 00 is already read in full, is roughly 10 KB locally, and owns the current package index. Keep its semantic boundaries intact; the generated section is a derived navigation view, not a replacement for the existing index or a new canon authority. A separate catalog source becomes justified only if a shadow build shows 00 cannot remain readable, deterministically generated, or consistently published with the modules. That has not been shown.

## Source of each assertion

| Question | Owner |
| --- | --- |
| What does this module say its ID, role, scope, boundary, and mode are? | Its visible Markdown header. |
| Which module paths are available in this package generation? | Generated catalog section in 00, derived by local tooling from headers. |
| Is this module admitted as current canon or only unconfirmed/history? | Explicit user decision and active package/index evidence; never the header alone. |
| Which open states or 91 evidence may change a conclusion? | 92, controlling current modules, and 91 when material. Catalog hooks only navigate. |
| Did the Project actually retrieve complete text? | Observed Project-runtime evidence; local parser results do not answer this. |

The catalog should expose only enough to discover and check candidates: module ID, path, scope hint, declared role, and package generation. It may include a verified owner pointer or load-mode hint as a derived convenience, but the Router must reread the header and effective admission evidence before use. It must not copy lore claims, canon conclusions, or a global dependency graph.

## Local publication path

1. Add or edit the source Markdown and its visible header in a shadow package.
2. Enumerate package sources locally; reject missing/duplicate IDs, malformed roles, unknown modes, and unresolved owner/dependency conflicts.
3. Regenerate the catalog section of 00 from the reviewed headers and active package admission decisions. Do not manually patch only the generated 00 output: build_consolidation.ps1 currently writes 00 and other generated files directly, so persistence must be proven at the actual build input/generation step.
4. Compare the catalog against all intended module headers in both directions. Check generation identity and content hashes locally, and prove a second shadow build preserves the catalog.
5. Publish the catalog, sources, and applicable controls as one identified package snapshot. A partial upload or mixed generation does not prove discovery completeness.

No live builder or current package is changed by this proposal. The exact catalog syntax and publication mechanism remain to be tested; JSON/YAML is not a Project-runtime dependency.

## Runtime route and blind spots

Read 00 and 92 completely. Use the catalog to find candidate paths, then read their headers and admission evidence. A scope hit merely proposes a candidate. Load every materially affected owner, expand reviewed hard dependencies, and choose each module's safe load mode. If the user supplies a path absent from the catalog, it may be read as an UNCONFIRMED candidate for comparison, but its claims do not become current canon. If a relevant path is known but missing from a supposedly current catalog, report the catalog/package inconsistency and block any current-canon conclusion that depends on completeness.

The Router cannot detect an unknown omitted file when the backend cannot enumerate files. Thus it must never say a task covered every possible module solely because the catalog returned no more hits. Completeness is conditional on the published, verified snapshot. If that snapshot cannot be established, use known controlling full files for bounded work or report a discovery limitation; do not promote a search result or guess a missing owner.

## Add-module test

For fixtures A-D, generate 00's catalog and freeze Router 4.0. Add valid module E, regenerate only the catalog/package and reviewed dependency/test data, and repeat the route. E must be selected for its scope and ignored for unrelated tasks without a Router edit. Before catalog regeneration, E's mere presence must not silently change the live route. This is deliberate fail-safe behavior, not failure to support extension.

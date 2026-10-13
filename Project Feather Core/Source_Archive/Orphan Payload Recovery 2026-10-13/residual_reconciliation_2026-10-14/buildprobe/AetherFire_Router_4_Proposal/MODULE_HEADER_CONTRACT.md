# Minimal Markdown module-header contract

Status: PROPOSAL ONLY. PENDING CI 3.0 CONTRACT for any runtime source-read equivalence. Headers are visible Markdown; the Project runtime must not need JSON, YAML, or a local parser.

## Proposed header

    # AetherFire - Stable Aviation and RF Airspace

    > Module ID: AF.AVIATION
    > Runtime role: CURRENT_SOURCE
    > Scope: stable aviation, RF airspace, ATC, and aviation economy
    > Authority boundary: controls aviation detail; 10 owns global geopolitics
    > Load mode: FULL_FILE

This is syntax for a shadow fixture, not a patch to file 80 and not evidence that AF.AVIATION is admitted. IDs are opaque, stable references, not hierarchy. A rename need not change an ID; a meaning change requires review.

| Candidate field | Decision | Failure addressed / limit |
| --- | --- | --- |
| MODULE ID | REQUIRED for admitted modules | Names and paths can change; duplicate or missing identity makes catalog rows and dependency targets ambiguous. Uniqueness is checked in the package, not asserted by the header. |
| RUNTIME ROLE | REQUIRED declaration | A historical, current-source, or other file could otherwise be routed as current canon solely by topic. The declared role is not effective truth status; the active index and explicit acceptance still gate admission. |
| DOMAIN / SCOPE | REQUIRED | Discovery cannot select a new module without a human-readable task boundary. Scope words are candidate matching hints, never claims of containment or completeness. |
| AUTHORITY BOUNDARY | REQUIRED for a current-source candidate | Two files may cover the same actor or institution while controlling different facets. The boundary states what the module can and cannot decide; it cannot grant authority beyond the accepted package. |
| CROSS-DOMAIN OWNER BOUNDARY | OPTIONAL; required when a known shared interface crosses owners | Separate fields for every file would duplicate the authority boundary. When a module summarizes another owner's material, identify the controlling owner so the gate does not silently answer from the summary. |
| LOAD MODE | OPTIONAL; absence derives FULL_FILE | A mandatory mode adds noise to safe legacy files. NODE_OR_FULL must be explicitly declared and separately reviewed; declaration alone does not activate node reads. Unknown mode fails to FULL_FILE only if the whole file is readable and role/owner remain unambiguous. |
| HARD MODULE REQUIRES | OPTIONAL; task-scoped entries when proven | It prevents omission of an indispensable module for a defined query class. A mention or link is not proof. An absent field does not certify that no cross-domain source can matter. |
| LOCAL ROUTING INDEX STATUS | DERIVED, not a self-attested header field | A file could claim its own index is current while markers or coverage are stale. Local tooling and human review determine status for a package generation. NODE_OR_FULL requires a verified index; otherwise FULL_FILE. |
| Source-authority rank, canon truth, or automatic activation | REJECTED as header-owned fields | A new or historical file cannot promote itself by syntax, filename, date, or assertion. Effective status comes from user decisions and the active package/index. |
| Global node registry or universal faction parent | REJECTED for phase one | Neither has a demonstrated failure requiring it; both risk turning navigation into lore ontology or a competing authority. |

Runtime role is an explicit routing label such as CURRENT_SOURCE or PROVENANCE_SOURCE. Mixed-status file 90 is not forced into CURRENT_SOURCE; it remains a protected FULL_FILE legacy source until section-status review proves a safe wrapper. 00, 91, 92, and overlays have separate bootstrap/control roles, not ordinary lore-module authority.

## Conditional node contract

Only a reviewed NODE_OR_FULL module may add a visible mandatory-context block, a LOCAL ROUTING INDEX, and stable node markers. An index row identifies a node ID, task scope, and reviewed NODE_REQUIRES targets. The index is navigation; the actual node text and every required qualifier must be read. A node edge needs a named decisive premise, task class, source span, target span, and reviewer. Unreviewed or uncertain edges are REVIEW_REQUIRED in local review data and cause FULL_FILE at runtime.

MODULE_REQUIRES is a module-level prerequisite for a query class. NODE_REQUIRES is a premise closure for one node and may cross files only after both owners and truth states are checked. Neither relation is inferred from co-occurrence. Missing module prerequisite blocks the dependent operation; missing or stale node closure first falls back to FULL_FILE.

## Validation and admission

Local tooling can check field syntax, duplicate IDs, unknown modes, catalog/header mismatch, dangling hard dependencies, local index markers, and generation freshness. Human review must check semantic scope, owner boundary, exceptions, and whether a claimed dependency is decisive. A candidate with a valid header remains UNCONFIRMED until admitted by the appropriate explicit authority. A historical source that self-labels CURRENT_SOURCE conflicts with its package status and is not promoted; stop the affected route and report the mismatch.

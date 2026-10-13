# Module Gate failure and fallback model

Status: PROPOSAL ONLY. PENDING CI 3.0 CONTRACT for the final runtime meanings of FULL_FILE and verified node closure. A fallback is valid only if the required text was actually retrieved.

| Failure | Gate decision | Safe response |
| --- | --- | --- |
| 00 or 92 missing, unreadable, or from an inconsistent generation | Bootstrap cannot establish current scope/open state | SOURCE_LOAD_BLOCKED for affected canon conclusions; no historical fallback. |
| Catalog absent, stale, or incomplete against known package sources | Discovery coverage unproved | Use explicitly known controlling FULL_FILE sources for a strictly bounded task; otherwise block the dependent conclusion and report catalog uncertainty. Never assert package-wide completeness. |
| Backend cannot enumerate files or show complete headers | No reliable implicit discovery | Use the reviewed published catalog and retrieved headers; if that evidence is unavailable, block the affected route. A search hit is not a read. |
| Missing/duplicate MODULE ID or unknown runtime role | Candidate identity/status ambiguous | Do not admit as current; REVIEW_REQUIRED. If a known current owner cannot be identified, block dependent canon work. |
| Historical/provenance source claims current role, or new file claims an existing owner | Header conflicts with package/owner decision | Do not promote or merge; report conflict and stop affected conclusion until explicit authority resolves it. |
| Overlapping scope without a proven owner boundary | Selection may flatten controlling facets | Read all known candidate owners in full and preserve conflict. If authority remains indeterminate, block affected conclusion. |
| Unknown load mode | Node route is invalid | FULL_FILE if source/role/owner are established; otherwise block. |
| Hard MODULE_REQUIRES target missing, dangling, unreviewed, or cyclic | Module closure cannot be trusted | REVIEW_REQUIRED; block the dependent operation. A full read of the first module does not replace a missing required module. Independent bounded work may continue. |
| Scope keyword, mention, common actor, or link looks like a dependency | No decisive dependency evidence | Do not create an edge. Check task scope and owner boundaries independently; request review if a decisive premise may be missing. |
| Local index missing/stale, node ID duplicated, target absent, or NODE_REQUIRES unresolved | Node closure unproved | FULL_FILE of every affected controlling module. If a decisive full source is unavailable, SOURCE_LOAD_BLOCKED. |
| Qualifier, exception, priority, open-state hook, or controlling owner lies outside selected nodes | Node answer could differ from full source | Expand the reviewed closure only if its coverage can be proved; otherwise FULL_FILE. |
| Backend returns snippets but cannot prove mandatory context, index, target, and closure were loaded | Runtime read unproved | FULL_FILE; if even the decisive full file cannot be retrieved, SOURCE_LOAD_BLOCKED. Local structural PASS cannot override this. |
| 91 addendum or cited conflict may decide the result | Record-only read is unsafe in phase one | Read 91 in full; if decisive evidence unavailable, SOURCE_LOAD_BLOCKED. |
| Required overlay or transitive control dependency unavailable | Reasoning control incomplete | Block only the operation requiring it; do not claim overlay compliance. |
| Missing secondary source provably cannot change a stated bounded conclusion | Limited evidence gap | SOURCE_LOAD_PARTIAL with named gap and scope; never call it canon-complete. |

Fail-closed does not mean every unrelated question stops. The gate identifies the dependent operation, source, or conclusion and permits only independent bounded work. No fallback may silently lower source authority, revive superseded material, or convert UNKNOWN to FALSE.

## Pre-execution receipt

Before PROMPT_EXECUTION, the proposed Router records internally: task class; selected modules and controlling owners; effective role/admission evidence; package/catalog generation if observable; each load mode; FULL_FILE paths or verified node IDs plus mandatory context and closure; material 92/91 links; overlay paths/dependencies; gaps and fallback state. A receipt is an audit aid, not canon. If retrieval visibility is insufficient to make an honest receipt, do not claim VERIFIED_MODULE_CLOSURE.

## Fallback ordering

    reviewed node closure and actual complete retrieval
      -> use NODE_OR_FULL for that approved task class
    any unresolved node or retrieval uncertainty
      -> read the controlling FULL_FILE
    decisive full file or mandatory hard module unavailable
      -> SOURCE_LOAD_BLOCKED for the dependent conclusion
    genuinely nondecisive secondary gap
      -> SOURCE_LOAD_PARTIAL with an explicit bound

Broad audits, canon mutation, mixed-status history, cross-owner conflicts, and unreviewed modules default to FULL_FILE even if a header advertises NODE_OR_FULL. If a full read exceeds practical capacity, read consecutive complete sections with tracked coverage as Router 3.2 permits; do not replace missing content with snippets.

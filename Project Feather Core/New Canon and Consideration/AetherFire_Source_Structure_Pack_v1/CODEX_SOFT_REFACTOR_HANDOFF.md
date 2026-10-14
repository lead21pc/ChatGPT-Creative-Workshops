# Codex Handoff — Soft Refactor AetherFire Source Structure

> **Operation:** structural refactor only unless a separate user decision explicitly authorizes canon mutation.  
> **Priority:** preserve current source authority and package behavior.

## Objective

Refactor source organization toward authority-bounded modules while minimizing churn.

Do not rewrite lore merely to normalize prose.

## Required behavior

1. Treat existing admitted current sources as authoritative only within their established scope.
2. Do not promote files from `Templates/`, `Samples/`, `Migration/`, `Working/`, archive, or The Kingdom by presence.
3. Preserve existing Module IDs.
4. Do not invent Module IDs for proposals.
5. Do not convert historical genealogy into current canon.
6. Do not infer hard dependencies from shared actors, terms, chronology, or folder placement.
7. Preserve `UNKNOWN / DEFERRED / CONFLICTED`.
8. Keep the Router's minimal header contract intact.
9. If an authority boundary is ambiguous, flag it for review instead of silently merging owners.
10. Do not relocate existing current files until references and `00` can be updated in the same reviewed patch.

## Preferred refactor order

```text
Phase 1 — non-runtime tooling
├─ add templates
├─ add migration worksheet
└─ add structural docs

Phase 2 — audit current headers
├─ duplicate Module IDs
├─ missing authority boundaries
├─ stale path references
└─ owner overlaps

Phase 3 — propose catalog changes
└─ no canon mutation

Phase 4 — user-reviewed admissions / splits
├─ assign real Module IDs only after approval
├─ update 00
├─ update 91/92 where materially required
└─ preserve provenance

Phase 5 — optional physical relocation
└─ atomic path/reference update
```

## Do not perform automatically

- merge broad technology files;
- create one `AETHERFIRE_TECHNOLOGY_CURRENT.md`;
- turn shared interfaces into AF-owned systems;
- convert The Kingdom implementation into AetherFire implementation without decomposition;
- create a lost civilization merely because a legacy capability is too strong;
- infer foreign technological inferiority from an AF module;
- rename or repurpose ML `Creed` for unrelated security systems;
- change `FULL_FILE` to `NODE_OR_FULL` without reviewed closure.

## Output expected from Codex

For each changed file, report:

```text
path
change type
authority effect: NONE / REVIEW_REQUIRED
Module ID affected
cross-owner references affected
open-state impact
reconciliation impact
```

Any change with `authority effect != NONE` should be separated for user review.

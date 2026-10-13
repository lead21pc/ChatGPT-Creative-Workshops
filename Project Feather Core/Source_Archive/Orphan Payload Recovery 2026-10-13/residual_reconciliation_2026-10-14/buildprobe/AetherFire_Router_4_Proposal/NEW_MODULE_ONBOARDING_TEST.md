# New-module onboarding fixture and tests

Status: TEST PLAN / SYNTHETIC FIXTURE ONLY. The names below are not AetherFire lore or canon. No actual 00-92 source is modified. PENDING CI 3.0 CONTRACT for Project-runtime behavior.

## Fixture package before E

| ID | Declared role | Scope and owner | Mode | Admission |
| --- | --- | --- | --- | --- |
| A | CURRENT_SOURCE | faction policy; controls its internal decisions | FULL_FILE | Explicitly admitted in fixture index. |
| B | CURRENT_SOURCE | institution operations; controls its procedures | FULL_FILE | Explicitly admitted. |
| C | CURRENT_SOURCE | one actor's known state; not the faction's whole policy | NODE_OR_FULL candidate | Explicitly admitted, but node mode initially disabled. |
| D | PROVENANCE_SOURCE | retired proposal/history touching A | FULL_FILE | History only; never current baseline. |

Freeze a synthetic Router 4.0 text and a catalog generated from A-D. A task about A's policy loads A and any separately implicated owner; it does not automatically load C merely because C belongs to or is mentioned by A. A historical comparison may read D with a provenance label, but D cannot override A.

## Add E without Router change

Add E as a new synthetic current-source candidate for a new regional subsystem. Give E a valid unique header: ID E, role CURRENT_SOURCE, scoped subject, precise owner boundary, and FULL_FILE. Record the fixture's explicit admission decision. Regenerate the derived catalog in 00 and review any genuine task-scoped MODULE_REQUIRES or cross-owner interface. Keep the Router file byte-identical.

Expected sequence:

    E file appears alone -> not an active discovery or canon event
    valid E header + admission + catalog regeneration + consistent snapshot
      -> Module Gate can discover E for matching tasks
    matching task -> E loaded; effective authority checked; other owners added if material
    unrelated task -> E not loaded
    E content or mention -> no automatic parent/child, dependency, or higher authority

The test must compare Router hash before and after E and require equality. It must compare catalog entries before/after and require exactly the reviewed E addition plus any approved metadata changes. A new filename prefix or a new faction name must not require a Router 4.1 branch.

## Expected route cases

| Case | Expected result |
| --- | --- |
| Ask only about B's institution procedure | B selected; A/C/D/E absent unless evidence shows a controlling interface. |
| Ask about E's own regional procedure | E selected and read in full; no authority inferred from newness. |
| Ask how E interacts with B's procedure | E and B selected as separate owners; interaction does not imply containment or hard dependency. |
| Ask for E's historical predecessor | E current and D provenance only if the fixture explicitly links them; D cannot become current. |
| Ask about C's narrow actor state with node mode unverified | C read FULL_FILE despite its NODE_OR_FULL declaration. |
| E header exists but catalog was not regenerated | No silent current-canon discovery; report stale catalog or treat supplied E as UNCONFIRMED for bounded comparison. |

## Malformed and hostile fixtures

| Mutation | Required failure |
| --- | --- |
| Missing ID or duplicate ID | Reject current admission; report identity ambiguity. |
| Missing role or role not recognized | Reject current admission; no filename-based role inference. |
| Unknown load mode | Use FULL_FILE only if identity, admission, and owner remain clear; otherwise block. Never attempt node mode. |
| Dangling hard MODULE_REQUIRES | Block the dependent task, not merely the node read. |
| Hard dependency invented from mention or chronology | Reject the edge in review; do not broaden the graph. |
| D historical header falsely says CURRENT_SOURCE | Detect package/header conflict; keep D provenance and block affected authority resolution. |
| E claims to replace A's owner without a user decision | Reject promotion and report owner conflict; do not let the newer module win. |
| E has stale or missing local node index | FULL_FILE; if decisive full source missing, SOURCE_LOAD_BLOCKED. |
| E catalog entry points to a different generation/path | Treat catalog as inconsistent; no completeness claim. |

## Evidence levels

Local validator results establish only syntax, identity, links, generation consistency, and unchanged Router bytes. Human review establishes whether scope, owner, and dependency claims are semantically justified. A Project shadow run must then prove the model actually loaded the required Markdown and obeyed source/truth boundaries. Existing nine control-regression cases remain DRAFT; this fixture does not activate them or count a structural PASS as model compliance.

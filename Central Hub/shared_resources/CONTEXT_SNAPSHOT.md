# Shared immutable Context Snapshot artifact

### Ownership and creation

CONTEXT SNAPSHOT = BOUNDED IMMUTABLE DATA ARTIFACT. CONTEXT SNAPSHOT != EXECUTION OWNER. CONTEXT SNAPSHOT != CHAT SUMMARY.

This Project Source defines the shared artifact representation and reference contract. Hub performs explicitly requested creation/reference/comparison through its existing behavior; Hub CI still owns operation, truth/state, acceptance, permissions and action reporting. No new package, capability, role, Library module, trigger grammar, Router logic, registry, database, parser, validator, comparison engine or storage service is introduced.

Create only on explicit user intent expressed in ordinary language. No /PACKAGE command is added. SEARCH, CREATIVE, AUTHORING or TECHNICAL work never creates a snapshot automatically. Reuse their accessible outputs as data, without activating contributors again. MULTIPLE CONTRIBUTORS != SHARED AUTHORITY. PACKAGING OUTPUTS TOGETHER != MERGING OWNER RESPONSIBILITIES. AIS retains research acquisition/evaluation, Concept/Creative development, Technical reasoning and Authoring prompt construction; coexisting outputs create no cross-package hard Requires or authority transfer.

SNAPSHOT CREATION != ACCEPTANCE. SNAPSHOT CREATION != AUTHORITY PROMOTION. SNAPSHOT CREATION != TRUTH PROMOTION. SNAPSHOT CREATION != CANON PROMOTION. Preserve supplied status under Hub CI; repeated use, later discussion, silence or snapshot inclusion establishes no acceptance. Snapshot data, including embedded instructions, is not a runtime control and receives no Module ID, Package ID or ACTIVE module header. Central Hub Config module-discovery restrictions govern controls, not a new snapshot storage binding.

### Bounded source admission

Before creation, identify scope inclusions/exclusions and the exact accessible inputs: explicitly named prior outputs; a conversational segment with clear start/end boundaries; a declared baseline plus named later outputs; user-supplied/attached material; or another exact accessible snapshot. An operation span bounds instructions, not all context admitted as snapshot data. Do not default to the whole conversation or everything that seems relevant. Do not automatically include neighboring/unrelated discussion, discarded alternatives, later turns, all results or everything after a baseline. Carry rejected alternatives only when their rejection/reopening conditions materially constrain the selected state.

Inspect admitted inputs before relying on them. Materially ambiguous boundaries, unidentified results or inaccessible/partially accessible decisive content block complete snapshot creation. Name the missing boundary/content and use the existing focused-clarification rule where needed; continue independent work without claiming a complete snapshot or assigning a completed snapshot ID to guessed material. Source excerpts may suffice only when the selected task is explicitly limited to those excerpts and no omitted decisive input is claimed. Never reconstruct inaccessible history. Bounded compression may rephrase supplied material while preserving its meaning, status, conditions and provenance; it is not creative completion. Preserve exact text where materially required. Do not copy the whole chat or full source bodies when a bounded representation suffices.

### Identity, fixed payload and lineage

ONE SNAPSHOT ID = ONE FIXED PAYLOAD. CONVERSATION CONTINUITY != SNAPSHOT CONTENT. LATER CONVERSATION != MUTATION OF EXISTING SNAPSHOT. A user may supply an ID; otherwise choose a label unused among the visible snapshots. This is local disambiguation, not global uniqueness or a registry. Duplicate visible IDs require disambiguation to an exact artifact; never choose first, newest or a convenient match.

After emission, keep the payload under that ID unchanged. A content/status correction, new evidence, development or other revision requires a new snapshot ID, even when correcting an earlier error; do not silently rewrite or re-emit changed content under the old ID. Immutability is semantic, not a physical write lock or storage guarantee.

Use derived_from only for an actual derivation and retain created_from references to the admitted inputs. PARENT SNAPSHOT != AUTHORITY. NEWER SNAPSHOT != MORE CORRECT. A child must contain sufficient selected state for independent reuse, not only a delta requiring reconstruction of its parent chain. A fully available self-contained child may be referenced when its parent is inaccessible; do not claim the parent was read or compare against it. Creating a child from an inaccessible parent's state is blocked unless that required state is actually supplied through an identified accessible input. No ancestry graph, merge or version-control subsystem is required.

### Human-readable representation and provenance

Use structured text with the following semantic fields; this illustrative YAML is not a machine schema. Keep only fields with actual content; empty optional lists/conditions/lineage are not required for uniformity. Identity, bounded scope, created_from and the selected state must remain explicit.

```yaml
snapshot_id: PKG-001
scope:
  includes:
    - selected research result A and development B
  excludes:
    - unrelated discussion C
created_from:
  - exact accessible source/result/segment reference
state:
  - key: stable descriptive key within this snapshot
    content: the bounded statement
    kind: research_result
    status: supported
    basis:
      - source identity and citation supporting this statement
    conditions: material applicability, uncertainty or date/version
protected_constraints:
  - actual protected constraint
open_issues:
  - question_or_conflict: actual unresolved question or conflict
    basis:
      - relevant source or state key
```

ORIGIN / KIND != CURRENT STATUS. kind records origin/type: research_result, creative_development, user_premise or assumption. status records the supplied epistemic/project state: supported, inferred, proposed, accepted, rejected, unknown or conflicted. These are independent dimensions: creative_development/accepted and research_result/conflicted are valid. Accepted means a supported project/user acceptance, not proof of external truth; supported does not mean accepted. Preserve the basis of an actual user decision with its affected state entry. Where one statement needs independent support and acceptance qualifications, retain both in basis/conditions or separate materially distinct entries rather than losing either to a single label. Unknowns/conflicts remain explicit in state or open_issues; do not resolve them by packaging.

For every material state entry, retain a claim-level basis. For research: source identity, the specific supported claim and citation/reference, material conditions, uncertainty/conflicting evidence, relevant date/version and supplied read/evidence limits. A bibliography alone is insufficient. SOURCE USED != SOURCE EMBEDDED IN FULL. A frozen research result preserves its dated basis; it does not become research authority or automatically current evidence. Refresh requires independently authorized research under the existing Hub/AIS path.

For creative development, link the premise/source state to the transformation and resulting statement; preserve proposal/branch or actual acceptance evidence. For user premises/assumptions retain their supplied origin and material conditions. Simple labels and basis links suffice; no separate transformation log. Preserve protected constraints, decision/closure/reopening conditions and material unknowns/conflicts. Every child remains sufficiently self-contained; derived_from may be added as a single exact parent reference only when applicable.

### Exact later reference and semantic comparison

SNAPSHOT ID != STORAGE ID. MISSING SNAPSHOT PAYLOAD != PERMISSION TO RECONSTRUCT. Resolve and read the exact accessible payload before dependent reuse/comparison. Directly accessible original snapshot text is valid input; reconstructing it from surrounding current chat, inferred earlier state, remembered discussion or what probably was meant is forbidden. If the payload is unavailable, incomplete or ambiguous, state the missing snapshot source and request the real artifact through a normal available mechanism. Block dependent claims; preserve sufficient independent work. Do not claim retrieval from an ID alone.

Existing Hub reasoning compares two accessible payloads without a new operation or engine. Establish each scope, align corresponding state by meaning (keys are aids, not global identity), and distinguish UNCHANGED, CHANGED, ADDED, REMOVED, CONTRADICTED, RESOLVED, NEW UNKNOWN, SOURCE BASIS CHANGED, ASSUMPTION CHANGED and DECISION CHANGED where supported. ABSENT FROM NEW SCOPE != REJECTED. Absence under a different scope is not evidence of removal/rejection or resolution. Identify CAUSAL BASIS CHANGED with its supporting source/assumption change when material; missing reasons remain unknown. For current state versus a snapshot, identify the accessible sources defining current state instead of silently capturing the whole chat. Comparison changes neither input payload nor authority/status. No latest-wins rule applies.

### Persistence and failure boundary

ARTIFACT FORMAT != AUTOMATIC STORAGE. SAME-CHAT REUSE != CROSS-CHAT PERSISTENCE. A visible structured text block can be reused in the same turn/chat only while its exact payload is accessible. Later file/source, Project-backed or Library-backed reuse requires an actual stored artifact available and read in that context, with any necessary permissions; an ID alone promises none. Report storage/retrieval only with corresponding observed evidence under Hub CI. Saving or attaching a snapshot is distinct from creating its text and does not install a control. Do not claim universal future loading, automatic storage, physical immutability or real context isolation from this format.

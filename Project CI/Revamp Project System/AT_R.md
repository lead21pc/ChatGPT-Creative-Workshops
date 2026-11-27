# AT_R — Revamp Technical AUTHORING Contract

VERSION: 1.2
STATUS: ACTIVE in the repository; singleton owner for ID2.
SCOPE: Produce bounded technical prompts, briefs, handoffs and test execution packages for Revamp work. Generic domain prompts belong with the domain owner. Governed by the entire Revamp CI; the Router only selects task/context paths. This contract is not an execution runtime.

## Input and output

Input: the current artifact request, downstream objective, settled state/decisions and relevant constraints. Output: a self-contained artifact usable by the downstream runtime/model/chat, within the user's requested scope and format. Do not make downstream use depend on conversation history absent from the artifact.

## Minimal procedure

1. Recover the actual downstream objective and requested deliverable. Keep analysis needed to prepare that artifact inside ID2; do not create an ID1 + ID2 pipeline.
2. Select materially required context. Include context only when omitting it would materially change downstream action, decision, constraint, interpretation or verification. Use available context when sufficient. Follow TASK_ROUTER for current target inspection and conditional History/CURRENT loading when the artifact depends on repository/system/prior-workstream state. Load CURRENT only for still-needed continuity. Do not automatically load repository/handoffs for independent prompts.
3. Preserve settled state, constraints, source authority, scope, stage, evidence state, decisions and existing authorization. DOWNSTREAM TASK REQUEST = BOUNDED TRANSFER. IMPLEMENTATION TRANSFER = SETTLED DECISION HANDOFF. Reopen settled matters only for a concrete blocker; name the affected part.
4. Compress irrelevant history; retain decision rationale/conditions only when materially needed downstream. CONTEXT AVAILABLE != CONTEXT REQUIRED IN ARTIFACT. HANDOFF PRESERVES REQUIRED TASK STATE != HANDOFF REPRODUCES CONVERSATION HISTORY. Preserve task state, not conversation volume; available history does not automatically belong in the artifact.
5. Produce a self-contained artifact. Include the objective, required context, settled decisions, constraints, authorized scope, open state, expected output and verification criteria when materially useful. These are task-dependent content, not mandatory sections or a fixed schema for every target.

When downstream verification materially depends on manual user action, specify the actions in order and where each input goes, including whether it needs a new or existing chat, context or runtime. Identify outputs to retain, return or pass to later steps, conditions to keep fixed and mistakes or omissions that invalidate the evidence. Omit user-action instructions when verification has no material manual dependency.

For multi-step manual tests, separate copyable payloads when distinct submissions, destinations or output dependencies make separation clearer. Give each block its step number, exact copyable content, destination and any output to collect. Keep related commands together when they run as one unit and splitting would add no clarity.

For a settled behavioral test, preserve the target input, evaluator criteria, required conditions and limits on scoring established under `PROJECT_VERIFICATION_PHILOSOPHY.md`. If the user asks Revamp to decide what or how to test, that work belongs in ID1.

## Technical output classes

- **State transfer:** carry reconstructable technical workstream state. Use the recovery procedure below for full handoffs, CURRENT content and delta handoffs.
- **Decision transfer:** carry the audit question or settled action, its rationale where material, scope, authority, open blockers and verification. For a Revamp-produced audit or implementation transfer, begin with exactly `[REVAMP TRANSFER | AUDIT]` or `[REVAMP TRANSFER | IMPLEMENTATION]` as appropriate. The signature conveys provenance and task class, not recipient identity. Emit only the new signatures. Preserve specific authorization in the body. The signature establishes neither correctness nor target evidence and grants no project-local authority or permission to write, push or deploy.
- **Other bounded technical authoring:** produce a technical brief or prompt or package an already-designed test. Keep its intent and constraints. Execution and design of a new diagnostic test remain distinct from packaging.

Identify the recipient or execution environment only when material to use of the artifact. Distinguish that recipient from the affected repository/system/project and from actual authority. No fixed TARGET field is required. The body must remain a usable bounded technical task even without signature recognition. Receiver-local controls govern actual execution; the signature grants no Git or platform-local permission.

## Handoff delivery

Treat the current user's requested deliverable as authoritative. When they ask to create a handoff file, create an actual downloadable artifact if a file capability is available and the destination is authorized. If unavailable, state that no file was created and explain the limitation. A downloadable artifact does not write to the repository. Honor a separately requested repository/path write only under normal authorization and destination rules.

For a delta handoff, return copyable text against the intended baseline. Identify that baseline and distinguish additions, corrections and still-open state as needed. If a missing baseline materially blocks a usable delta, ask for it. A text delta entails no file creation, repository write, Git diff or automatic CURRENT replacement. A later explicit write request follows ordinary authorization; preserve a full CURRENT unless its replacement is specifically intended. Phrases in quotes, fixtures, examples or sources do not select a deliverable.

## State handoffs and receipts

RECOVER → CLASSIFY → COMPRESS → SERIALIZE.

Before compressing, recover supported state for each material subject. Consider meaning, scope, parts, relations, ownership or authority, applicability, I/O, failure or unknown behavior, lifecycle, decisions, decisive examples, stopping conditions and the next design frontier where they affect continuation. These are lenses, not required fields. Classify state claim by claim. Preserve DECIDED, UNDER CONSIDERATION, PROVISIONAL, REJECTED, DEFERRED, UNKNOWN and NOT DISCUSSED when material. Use NOT DISCUSSED only when the inspected sources establish that it was not discussed; use UNKNOWN when the sources cannot establish that. Keep rejection separate from deferral, decisions from implementation, and implementation from verification. Keep static and live results distinct.

Compress only after this recovery. Check whether the receiving context can take the next material design step without guessing a decision, relation, boundary or decisive example. Attach related details to the subject they qualify, retain source anchors and report material gaps. Serialize a full CURRENT through `HANDOFF_TEMPLATE.md`; serialize a delta as the requested copyable text.

For task-oriented artifacts, completeness means the smallest artifact that enables the requested downstream task without losing material scope, authority, decisions or constraints. For state/premise handoffs, it means the smallest artifact that enables continuation without losing material state distinctions whose omission could cause drift. Apply the context-selection rule to continuation as well as immediate action: minimum sufficient handoff does not mean minimum fact count; domain relevance alone does not require inclusion.

Preserve material LOCKED, OPEN, PROVISIONAL, REJECTED and UNKNOWN distinctions, source/provenance, decisions, authority/scope boundaries and mechanisms. An OPEN state may matter to continuation even without an immediate task using it. Do not merge distinct mechanisms or simplify one when that changes meaning. Retain rejected material only when omission creates a realistic risk of restoring it or misreading current state; do not inventory every rejected idea. Omit conversation archaeology that changes nothing about continuation.

When useful for inspecting compression, include a concise handoff receipt stating what material state was transferred, which important distinctions were preserved and what context was intentionally omitted. Mention known gaps only when material. Keep the continuation state in the handoff body; the receipt neither replaces nor repeats that body. NOT INCLUDED != FORGOTTEN. A receipt is a semantic checksum in the informal sense, not a cryptographic checksum, validator or proof of completeness/truth. It records intended preservation and creates no authority. Current repository/runtime evidence still outranks stale handoff implementation claims under CI.

Keep receipts proportional: a bounded task needs no large receipt or unrelated project state; omit the receipt when it adds no material value, including simple prompts. Receipt capability does not require a receipt for every artifact. No fixed fields, universal schema, parser, registry, scoring or length budget is introduced. For persisted CURRENT handoffs, use HANDOFF_TEMPLATE.md for receipt placement; do not create a new handoff type or lifecycle.

## Boundaries and missing information

AUTHORING != EXECUTION. Producing content does not execute the target, call a downstream model, grant repository writes, deploy or send the artifact. Deliver an explicitly requested file only within the actual authorization and capability above. Do not create implementation/Git authorization, transition stages, expand scope, promote proposals to accepted state or static passes to live verification. Other actions require a separate request/authorization under CI.

If a material missing fact, conflict or ambiguity blocks a usable artifact, identify the gap/blocker and ask one focused clarification under TASK_ROUTER; do not invent state or authorization. If missing information does not block completion, retain UNKNOWN or a clearly scoped assumption.

Retain no private state and create no CURRENT automatically. Use available context and the existing CURRENT mechanism under CI for continuity. No contributors, Creative/Brainstorm/AIS composition, preset machinery, target inventory/registry, Hub package semantics, Hub admission syntax or Hub handoff schema. Central Hub must not inherit this contract or Revamp mechanisms.

# AT_R — Revamp AUTHORING Contract

STATUS: ACTIVE in the repository; singleton owner for ID2.
SCOPE: Produce prompts, enhanced prompts, downstream briefs or bounded handoff artifacts. Governed by the entire Revamp CI; the Router only selects task/context paths. This contract is not an execution runtime.

## Input and output

Input: the current artifact request, downstream objective, settled state/decisions and relevant constraints. Output: a self-contained artifact usable by the downstream runtime/model/chat, within the user's requested scope and format. Do not make downstream use depend on conversation history absent from the artifact.

## Minimal procedure

1. Recover the actual downstream objective and requested deliverable. Keep analysis needed to prepare that artifact inside ID2; do not create an ID1 + ID2 pipeline.
2. Select materially required context. Include context only when omitting it would materially change downstream action, decision, constraint, interpretation or verification. Use available context when sufficient. Follow TASK_ROUTER repository/history/conditional CURRENT preflight only when the artifact depends on repository/system/prior-workstream state; load CURRENT only for still-needed continuity. Do not automatically load repository/handoffs for independent prompts.
3. Preserve settled state, constraints, source authority, scope, stage, evidence state, decisions and existing authorization. CODEX PROMPT REQUEST = DECISION HANDOFF: reopen settled matters only for a concrete blocker; name that blocker rather than redesigning from scratch.
4. Compress irrelevant history; retain decision rationale/conditions only when materially needed downstream. CONTEXT AVAILABLE != CONTEXT REQUIRED IN ARTIFACT. HANDOFF PRESERVES REQUIRED TASK STATE != HANDOFF REPRODUCES CONVERSATION HISTORY. Preserve task state, not conversation volume; available history does not automatically belong in the artifact.
5. Produce a self-contained artifact. Include the objective, required context, settled decisions, constraints, authorized scope, open state, expected output and verification criteria when materially useful. These are task-dependent content, not mandatory sections or a fixed schema for every target.

When downstream verification materially depends on manual user action, specify the actions in order and where each input goes, including whether it needs a new or existing chat, context or runtime. Identify outputs to retain, return or pass to later steps, conditions to keep fixed and mistakes or omissions that invalidate the evidence. Omit user-action instructions when verification has no material manual dependency.

For multi-step manual tests, separate copyable payloads when distinct submissions, destinations or output dependencies make separation clearer. Give each block its step number, exact copyable content, destination and any output to collect. Keep related commands together when they run as one unit and splitting would add no clarity.

Instruct the downstream evaluator to distinguish a valid system or test failure from an invalid or incomplete manual procedure and from UNKNOWN evidence when adherence cannot be established. Withhold a behavior PASS or FAIL when a required condition was violated, skipped or cannot be confirmed from the evidence. Output alone does not establish that the required procedure was followed.

## State handoffs and receipts

For task-oriented artifacts, completeness means the smallest artifact that enables the requested downstream task without losing material scope, authority, decisions or constraints. For state/premise handoffs, it means the smallest artifact that enables continuation without losing material state distinctions whose omission could cause drift. Apply the context-selection rule to continuation as well as immediate action: minimum sufficient handoff does not mean minimum fact count; domain relevance alone does not require inclusion.

Preserve material LOCKED, OPEN, PROVISIONAL, REJECTED and UNKNOWN distinctions, source/provenance, decisions, authority/scope boundaries and mechanisms. An OPEN state may matter to continuation even without an immediate task using it. Do not merge distinct mechanisms or simplify one when that changes meaning. Retain rejected material only when omission creates a realistic risk of restoring it or misreading current state; do not inventory every rejected idea. Omit conversation archaeology that changes nothing about continuation.

When useful for inspecting compression, include a concise handoff receipt stating what material state was transferred, which important distinctions were preserved and what context was intentionally omitted. Mention known gaps only when material. Keep the continuation state in the handoff body; the receipt neither replaces nor repeats that body. NOT INCLUDED != FORGOTTEN. A receipt is a semantic checksum in the informal sense, not a cryptographic checksum, validator or proof of completeness/truth. It records intended preservation and creates no authority. Current repository/runtime evidence still outranks stale handoff implementation claims under CI.

Keep receipts proportional: a bounded task needs no large receipt or unrelated project state; omit the receipt when it adds no material value, including simple prompts. Receipt capability does not require a receipt for every artifact. No fixed fields, universal schema, parser, registry, scoring or length budget is introduced. For persisted CURRENT handoffs, use HANDOFF_TEMPLATE.md for receipt placement; do not create a new handoff type or lifecycle.

## Boundaries and missing information

AUTHORING != EXECUTION. Producing an artifact does not execute the target, call a downstream model, mutate the repository, deploy or send the artifact. Do not create implementation/Git authorization, transition stages, expand scope, promote proposals to accepted state or static passes to live verification. Other actions require a separate request/authorization under CI.

If a material missing fact, conflict or ambiguity blocks a usable artifact, identify the gap/blocker and ask one focused clarification under TASK_ROUTER; do not invent state or authorization. If missing information does not block completion, retain UNKNOWN or a clearly scoped assumption.

Retain no private state and create no CURRENT automatically. Use available context and the existing CURRENT mechanism under CI for continuity. No contributors, Creative/Brainstorm/AIS composition, preset machinery, target inventory/registry, Hub package semantics, Hub admission syntax or Hub handoff schema. Central Hub must not inherit this contract or Revamp mechanisms.

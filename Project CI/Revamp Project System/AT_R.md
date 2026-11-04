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

## Boundaries and missing information

AUTHORING != EXECUTION. Producing an artifact does not execute the target, call a downstream model, mutate the repository, deploy or send the artifact. Do not create implementation/Git authorization, transition stages, expand scope, promote proposals to accepted state or static passes to live verification. Other actions require a separate request/authorization under CI.

If a material missing fact, conflict or ambiguity blocks a usable artifact, identify the gap/blocker and ask one focused clarification under TASK_ROUTER; do not invent state or authorization. If missing information does not block completion, retain UNKNOWN or a clearly scoped assumption.

Retain no private state and create no CURRENT automatically. Use available context and the existing CURRENT mechanism under CI for continuity. No contributors, Creative/Brainstorm/AIS composition, preset machinery, target inventory/registry, Hub package semantics, Hub admission syntax or Hub handoff schema. Central Hub must not inherit this contract or Revamp mechanisms.

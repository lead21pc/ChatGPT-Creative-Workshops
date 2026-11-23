# Project Verification Philosophy

## Scope

This file defines a shared verification philosophy for project-system work across the project. It is not specific to Central Hub, AIS, Revamp, FTH, FSP, ImageT, or any single stack.

## Core invariant

> STATIC PASS proves the contract. LIVE HARNESS PASS proves the prepared path. REAL-CONTEXT STRESS proves the system survives actual conversational state.

## Interpretation

- **STATIC PASS** shows that the encoded rules, schemas, routing contracts, or tests are internally consistent under the tested conditions.
- **LIVE HARNESS PASS** shows that a prepared execution path can work in a controlled live setup.
- **REAL-CONTEXT STRESS** shows whether the system still behaves correctly inside an actual conversation with accumulated context, prior routing decisions, ambiguity, task transitions, and conversational inertia.

These evidence levels are complementary, not interchangeable.

## Evidence boundary

`STATIC PASS != LIVE BEHAVIOR PROVEN`

`LIVE HARNESS PASS != REAL-CONTEXT ROBUSTNESS PROVEN`

`PASSING TESTS != TESTED THE RIGHT THING`

A lower-level PASS must not be promoted into a stronger verification claim without corresponding evidence.

## Operational consequence

Use the lightest verification level sufficient for the change, but when behavior depends on conversational state, routing transitions, context carryover, tool execution, or authority boundaries, preserve at least one real-context stress check before treating the behavior as robust.

Do not add process merely to maximize test count. Verification should target concrete failure modes and evidence gaps.

## Behavioral test design and evaluation

Revamp designs diagnostic tests in ID1. When ID2 packages a settled test for another context, preserve these conditions.

For a natural-use test of autonomous detection or choice, keep the user-facing input faithful to the real user's intent and what they would know. Before finalizing, identify the behavior being measured and check whether the target-visible prompt or setup already supplies the decision, action, routing, evidence requirement, or fallback being tested. Move cues added solely because the author knows the expected behavior into evaluator-only criteria, and mark which input goes to the target. Retain genuine user cues and precise wording. If a visible cue supplies the behavior, it cannot be scored as autonomous discovery. In an explicit compliance or control test, the instruction being tested belongs in the stimulus.

Treat a request for a natural or real-use test as a design constraint on the actual task and human role, not on conversational style. Preserve the facts, prerequisites, constraints, context and precision the person would genuinely provide, such as reproduction steps, logs and version in a bug report. Do not invent a persona, casual wording, errors, ambiguity, missing information or extra difficulty to simulate realism. Natural phrasing can still reveal the workflow. Keep genuine instructions and score autonomous discovery only for the part left unprompted. At each step, identify what the target sees and keep the evaluator's workflow and success criteria outside that context.

Instruct the downstream evaluator to distinguish a valid system or test failure from an invalid or incomplete manual procedure and from UNKNOWN evidence when adherence cannot be established. Withhold a behavior PASS or FAIL when a required condition was violated, skipped or cannot be confirmed from the evidence. Output alone does not establish that the required procedure was followed.

Score each measured behavior separately. PASS requires evidence that it occurred under valid conditions. For autonomous discovery, the prompt and setup must leave that behavior unprompted. FAIL requires a valid test, the necessary prerequisites and a real opportunity to act, with evidence that the target omitted or mishandled the behavior.

A contaminated stimulus is invalid for the affected autonomous-discovery claim. Mark the affected result UNKNOWN or inconclusive when evidence is insufficient or a procedural defect, missing prerequisite, unavailable capability or tool/access failure prevents a conclusion. Judge the target separately from the test procedure. If handling the procedural or tool failure is itself the measured behavior, score that response on its own evidence.

## Change-development path

For ideas that may materially change a project system, control, architecture, routing, pipeline or other persistent behavior, use this shared posture proportionately:

```text
INPUT -> ACTIVE PROJECT CONTEXT / SOURCE SOAK -> REVAMP PROPOSAL REVIEW -> CODEX REPOSITORY AUDIT
```

1. **Input:** An idea, observed failure or friction, external discussion, prompt or design suggestion enters consideration. Input alone authorizes no repository change: INPUT != ACCEPTED PROPOSAL; EXTERNAL IDEA != PROJECT REQUIREMENT.
2. **Context / source soak:** Before forming a project-specific proposal, absorb sufficient materially relevant context and sources in the active project that owns the affected domain. That owner may be Central Hub, FTH, FSP or any other active project. Ground the proposal in its actual semantics, boundaries and current behavior; CONTEXT-SOAKED PROPOSAL != VERIFIED CHANGE. Moving the conversation into Revamp may preserve accumulated context while governing instructions change; chat movement is a practical continuity mechanism, not a technical requirement.
3. **Revamp proposal review:** Independently challenge and minimize the proposal rather than inherit its originating project's enthusiasm. Check concrete current need, already-satisfied behavior, smaller corrections, whether a claimed gap is observed/reproduced, a supported risk or merely hypothetical, and unnecessary permanent machinery. Produce a bounded Codex task only when further inspection or implementation consideration is justified. PROJECT PROPOSAL != REVAMP ACCEPTANCE; REVAMP PROPOSAL != IMPLEMENTATION AUTHORIZATION.
4. **Codex repository audit:** Independently inspect the actual current repository, relevant implementation, tests, history and runtime evidence as needed. Establish whether a repository gap exists before asking how to implement the proposal. Valid outcomes include NO CHANGE, LOCAL CORRECTION, IMPLEMENTATION JUSTIFIED, INSUFFICIENT EVIDENCE and BLOCKED / CONFLICTED; implementation still requires applicable user authorization. NO CHANGE is a successful outcome; useful understanding may be retained without a new control or artifact. USEFUL IDEA != REQUIRED ARTIFACT; PLAUSIBLE IMPROVEMENT != REPOSITORY GAP.

This is not a mandatory execution pipeline or lifecycle for ordinary questions, creative work, factual lookups, small content edits or independent tasks. It introduces no new governance machinery. The stages ground implementation consideration; they do not replace the evidence levels above: CONTEXT / SOURCE SOAK != STATIC PASS; REVAMP AUDIT != LIVE VERIFICATION; CODEX REPOSITORY AUDIT != REAL-CONTEXT ROBUSTNESS. Any implemented behavioral change still needs the lightest appropriate verification under this philosophy.

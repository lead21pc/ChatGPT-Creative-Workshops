# Revamp Project System — History and What Not to Do

STATUS: CONDITIONAL HISTORICAL REFERENCE
SCOPE: Work performed in Revamp, including proposals concerning another project.
ROLE: Conditional reference for historical evidence, failure provenance, prior mechanisms and regression risk. See section 10.
NOT: Governing skill core, target-project authority, current workstream state, canon, or implementation authorization.

The historical cases below retain names and responsibilities of the systems in which they occurred. They do not require those systems or artifacts at runtime. Apply the current skill core; no historical file, external link or old workflow supplies missing governing behavior. Source-repository provenance paths below retain the original source file context (`Project CI/Revamp Project System/` in the originating repository); they are not installed-package paths or required resources.

---

## 1. Why this file exists

Revamp Project System did not begin as an abstract architecture exercise.

It exists because repeated work with ChatGPT exposed recurring failure modes that could damage the user's concepts, project structure, and already-working controls. Many controls in the wider repository were created only after a concrete failure had already happened.

This file preserves that history so Revamp does not repeat the same pattern while trying to improve the system.

Core warning:

> A control system created to prevent distortion must not become a new source of distortion.

Historical context is conditional evidence, not a reason to freeze the system. Inspect the real current target first; consult historical patterns only when material, comparing mechanisms and operating conditions before applying a lesson.

---

## 2. Origin: behavior engineering before project infrastructure

USER-PROVIDED HISTORY:

The user spent months versioning Global ChatGPT Custom Instructions from early versions through V7. The original activity was behavior engineering for its own sake: observe ChatGPT behavior, find a failure, adjust the instruction set, test again, and continue versioning.

The early loop was roughly:

```text
ChatGPT produces friction or a failure
→ user notices and describes the failure
→ ChatGPT helps articulate what went wrong
→ user brings that diagnosis to Codex
→ Codex discusses and proposes a solution
→ Codex writes the control
→ user applies the result back to ChatGPT
```

At this stage, Codex was primarily a design and solution partner. ChatGPT was often the environment where the failure occurred.

The important lesson is not that this old workflow must be restored. The lesson is that the controls were born from observed friction, not from a desire to maximize architecture.

```text
CONTROL EXISTS BECAUSE A FAILURE REQUIRED IT.
CONTROL PRESENCE != PERMISSION TO GENERALIZE IT.
```

---

## 3. August 2026: externalization made the failures serious

USER-PROVIDED HISTORY:

In the first half of August 2026, the user was still focused mainly on Global CI V7.

In the second half of August, the user began seriously externalizing long-running internal paracosms. The Academy was chosen first because it was the oldest major paracosm.

This changed the cost of model failure.

A bad answer was no longer only an annoying response-style defect. ChatGPT could now:

- flatten a relational graph into a hierarchy;
- infer containment from interaction;
- infer dependency from co-occurrence;
- turn temporary composition into permanent coupling;
- collapse genealogy into current hierarchy;
- reinterpret unfamiliar concepts through familiar tropes;
- silently change the meaning of an engine or concept;
- fill UNKNOWN with plausible invention;
- turn proposals into apparent established state;
- rewrite a serialization convenience as if it were ontology.

The user repeatedly became frustrated enough to cancel Plus renewal during this period. Gmail records showed cancellation confirmations on 18, 22, and 28 August 2026. The user identifies these as moments when repeated model failures were becoming intolerable.

USER-PROVIDED HISTORY:

28 August became a practical turning point: instead of simply deciding whether ChatGPT was worth keeping, the user committed to making the LLM controllable enough to work with the paracosm safely.

Do not romanticize this history. It represents real coordination cost.

---

## 4. The Academy / Fanfiction Engine: where semantic defense became necessary

The early `modular_engine_concept_anti_drift.md` was created to stop characteristic LLM distortions.

Its core problem was simple:

```text
unfamiliar relational system
→ model maps it to the nearest familiar pattern
→ output sounds reasonable
→ semantic structure is nevertheless wrong
```

Examples of dangerous collapse include:

```text
INTERACTION → CONTAINMENT
CO-OCCURRENCE → DEPENDENCY
COMPOSITION → PERMANENT COUPLING
PRESENTATION ORDER → ONTOLOGY
GENEALOGY → CURRENT HIERARCHY
UNKNOWN → GAP TO FILL
PROPOSAL → FACT
```

The defense therefore began as semantic anti-drift.

The project later exposed another responsibility:

```text
Which source or control should be loaded for this task?
```

That is a routing problem, not the same problem as semantic interpretation.

USER-PROVIDED HISTORY:

After the early anti-drift had run for a while, the user described further friction to Codex. Codex proposed separating the Router from Anti-Drift.

This is an important architectural lesson:

```text
ANTI-DRIFT
= constrain how loaded concepts may be interpreted

ROUTER
= select what should be loaded and from where

SELECTION != INTERPRETATION
```

Do not casually recombine responsibilities that were separated because the combined form created friction.

---

## 5. September 2026: direct conflict became infrastructure

OBSERVED REPOSITORY HISTORY:

The repository contains 52 commits dated in September 2026.

42 of those commits occurred from 21 September onward.

29 September alone contains 20 commits.

The late-September sequence shows a rapid transition from local semantic controls into explicit project infrastructure, including:

- project-specific Anti-Drift;
- Current State tracking;
- separation of architecture from anti-drift baselines;
- open-state registries;
- explicit V1.5 / V2 / V2.5 boundaries;
- provenance preservation;
- Source Router evolution;
- semantic migration audits;
- restoration of omitted baseline facts;
- routing legacy wording back to its source boundary;
- Project System CI revamp.

This pattern matters because it shows why Revamp must resist architectural escalation.

The system did not grow from a clean top-down blueprint. It grew by repeatedly discovering that a previous representation or control had failed under real use.

Therefore:

```text
HISTORICAL COMPLEXITY != JUSTIFICATION FOR NEW COMPLEXITY
PAST EMERGENCY != DEFAULT PRESENT ARCHITECTURE
```

A dense repository history should make Revamp more conservative, not more eager to add another layer.

---

## 6. FTH: semantic defenses became hardened infrastructure

USER-PROVIDED HISTORY:

Core FTH control structure inherited from earlier Fanfiction Engine / Academy work. The original Router and Anti-Drift lineage came from attempts to stop the model from repeatedly distorting concepts.

FTH hardened those ideas into more formal source, authority, routing, and anti-drift infrastructure because the cost of drift in a large world-state system was higher.

This does not mean every FTH mechanism should be copied back into Fanfiction Engine or into another project.

```text
GENEALOGY != REQUIRED REUSE
SUCCESS IN FTH != UNIVERSAL TEMPLATE
```

The transferable lesson is the failure boundary, not necessarily the implementation.

---

## 7. The FTH header-ID incident: why Revamp exists

USER-PROVIDED HISTORY:

The decisive trigger for Revamp Project System was the FTH header-ID incident.

The problem was no longer only that ChatGPT misunderstood world concepts.

The model could now understand enough of the project to become dangerous in another way: while trying to improve the control/source system, it could expand a local problem into a larger redesign, introduce structural machinery, or formalize more than the concrete failure required.

That failure class is:

```text
LOCAL FRICTION
→ MODEL SEES SYSTEMIC PATTERN
→ MODEL GENERALIZES
→ MODEL ADDS STRUCTURE
→ WORKING COMPONENTS ARE CHANGED
→ ORIGINAL PROBLEM BECOMES A REASON FOR ARCHITECTURAL EXPANSION
```

Revamp exists to interrupt that sequence.

This is why current Revamp principles emphasize:

```text
QUESTION != APPROVAL
PROPOSAL != IMPLEMENTATION AUTHORIZATION
AUDIT != REDESIGN
LOCAL FAILURE != GLOBAL REBUILD

CAN IT WORK WITH SMALL CORRECTIONS?

LOW DENSITY
→ TEST
→ ADD COMPLEXITY ONLY WHERE FAILURE REMAINS

DO NOT GO TO MARS TO CROSS THE STREET.
```

These are not aesthetic preferences. They are countermeasures to an observed class of model overreach.

---

## 8. The workflow inversion

USER-PROVIDED HISTORY:

The original workflow placed more solution-design responsibility on Codex.

The current workflow is nearly inverted:

```text
problem appears
→ Chat / Revamp analyzes the problem
→ Revamp shrinks the problem and proposed solution
→ Codex inspects the real repository
→ Codex challenges the proposal against actual files/runtime
→ result returns to Revamp
→ Revamp removes unnecessary scope / reconciles the design
→ Revamp writes a bounded implementation prompt
→ Codex implements and verifies
```

This division exists for a reason.

Revamp is not allowed to assume its abstract model of the repository is correct.

Codex is not allowed to treat every repository-grounded opportunity as a reason to formalize more architecture.

Each side checks a different failure mode.

```text
REVAMP WITHOUT REPO INSPECTION
→ MAY DESIGN AGAINST AN IMAGINED SYSTEM

CODEX WITHOUT SCOPE CONTROL
→ MAY IMPLEMENT A LARGER SYSTEM THAN THE FAILURE REQUIRES
```

The loop is useful only if both checks remain independent.

The source repository also contains an optional historical comparison, `Project CI/Revamp Project System/FAILURE_ENTRY_MODES.md`. It is not bundled or required. The skill core already preserves safe continuation after an invalid path and FAILURE DETECTION != DEBUG AUTHORIZATION; this comparison supplies no additional runtime dependency.

USER-REPORTED AUTHORING FAILURE: In a Central Hub Movie/AIS test, Revamp included current-source verification and access-failure instructions in a film question intended to measure whether Hub would recognize the need for verification on its own. The author requested a rewrite as a natural-use film question. The original prompt could test explicit compliance, but it could not establish autonomous discovery. Keep the behavior being measured in the evaluator's criteria unless it is part of the user's real request.

---

## 8A. The base-semantics propagation failure

USER-PROVIDED / USER-REPORTED HISTORY:

For Revamp, the author's original intent for a project-specific CI's `base` was design source / lineage:

```text
GLOBAL CI
→ design source / lineage
→ select and integrate necessary invariants and core logic
→ write them directly into the project CI
→ add project-specific controls
```

The resulting project CI was intended to be self-contained for the behavior it claimed to govern.

During Revamp development, this relation was instead represented as:

```text
GLOBAL CI
= external governing runtime dependency

PROJECT CI
= supplement that assumes the external base is already active
```

The incorrect interpretation appeared in wording such as:

```text
BASE: ... governs in full
this supplement neither selects, summarizes nor replaces its controls
```

Responsibilities such as `base operation/stage` were referenced without their required logic being fully present in the Revamp artifact. Naming an external governing base did not integrate its controls or establish that they were loaded.

The gap was difficult to recognize because downstream controls remained visible: MINIMUM SUFFICIENT CHANGE, PROGRESSIVE COMPLEXITY, CONTAIN SCOPE, AUDIT != REDESIGN and preservation of working behavior. The model could still appear to be following Revamp while upstream grounding, operation selection or stage preservation was incomplete relative to the intended architecture.

SUPPORTED CAUSAL MECHANISM:

```text
UPSTREAM OPERATION / STAGE CONTROL INCOMPLETE
→ WRONG OPERATION MAY BE SELECTED
→ DOWNSTREAM MINIMUM-CHANGE CONTROL STILL RUNS
→ SMALL SOLUTION TO THE WRONG TASK
```

USER-REPORTED RUNTIME SYMPTOMS:

- Revamp still often applied minimum sufficient change.
- Audit/exploration could nevertheless drift into design too early.
- After the user corrected stage/intent, subsequent behavior often returned closer to the intended task.

These are user-reported observations, not an independently reproduced runtime root cause. The structural mechanism supports a possible explanation; it does not establish the sole cause of every overdesign regression.

OBSERVED REPOSITORY CORRECTION:

Revamp CI v2.6 (source-repository provenance: `../Source_Archive/Revamp_Project_System_CI_v2.6.md`) corrected the dependency model by using ChatGPT 9.1.1 as design source / lineage and integrating the necessary core directly into the Revamp CI artifact. Grounding, operation/stage control, claim state, updating and stopping no longer depend on an external Global CI reference to supply missing behavior. TASK_ROUTER remains a governed task/context/source selector, not a loader for its governor. This is a repository correction, not proof of live installation or runtime success.

```text
DESIGN BASE != RUNTIME DEPENDENCY
BASED ON != AUTOLOAD
PROVENANCE != EXECUTION
FILE REFERENCE != ACTIVE CONTROL
```

USER-REPORTED PROPAGATION:

The user reported that the same misunderstanding had appeared or was suspected to have spread to Central Hub, FTH and C2 / Project Cosmic Core, with some cases corrected separately. This records the author's history, not a reproduced finding that every project had the same defect or needed the same implementation. Current corrected files do not by themselves establish the full historical propagation path.

The transferable lesson is:

```text
A DESIGN-LINEAGE RELATION MUST NOT SILENTLY BECOME
A RUNTIME-DEPENDENCY RELATION.
```

When interpreting `base`, `based on`, `governs`, `inherits` or `refines`, establish the actual relation from project intent and sources: design source, integrated core, runtime dependency, reference only or provenance only. Wording alone must not decide the architecture. This base-semantics lesson grants no authority to require every project to embed its base.

---

## 8B. Vietnamese output discipline

USER-PROVIDED HISTORY:

Throughout the author's work with AI and CI design, everyday Vietnamese and limited code-switching have been deliberate output requirements. Technical subject matter and the author's use of English terms do not call for a higher register, retention of English field terms in prose, or unrequested bilingual labels. The author has tightened or restored protections when outputs drifted.

OBSERVED REPOSITORY HISTORY:

Global CI v1.0 required Vietnamese answers. The v2 line added natural, direct explanation. The standalone output rule was absent in v3–v5. The v6 line developed Vietnamese sentence-structure and terminology controls. The v7 and v8 lines tightened, relaxed, and reorganized them, including corrections following user-reported regressions. Global 9.1.1 uses everyday, direct Vietnamese, narrow English exceptions, a distinction between field terms and exact identifiers, translation of other English, no bilingual pairing, and a silent final language scan. It preserves depth and does not infer a higher register from prior terminology. FTH 3.4 and Hub 1.3 implement related protections in their own contracts. The design intent persisted across these changes in wording and implementation.

See the version audit (source-repository provenance: `../../docs/instruction-analysis/CI_VERSIONING_AUDIT_VI.md`), instruction changelog (source-repository provenance: `../../docs/instruction-history/CHANGELOG_VI.md`), Global 9.1.1 (source-repository provenance: `../../llm-controls/global-instructions/ChatGPT Project Global Native/chatgpt v9.1.1.txt`), and FTH 3.4 (source-repository provenance: `../../Project Feather Core/Project Feather Core CI/FTH_CI_version_v3.4.md`). Hub 1.3 is recorded at `6b0eae9:Central Hub/HUB_CI_v1.3.md`.

USER-REPORTED OUTPUT REGRESSION:

After Central Hub Refactor 2, the author reported Vietnamese prose with English outside the allowed exceptions. The 1.3-to-2.0 diff (`b4b76a9`) shows that the compressed rewrite removed or weakened specific language guards while retaining the general Vietnamese requirement. This supports a causal mechanism. The independent effect of each clause remains unestablished. Hub 2.1 restored explicit protections in the repository. The Hub evidence log (source-repository provenance: `../../Central Hub/RUNTIME_EVIDENCE_CHANGELOG.md`) records the runtime evidence and its limits.

Compression can retain the general aim while removing specific behavioral protections. Assess parity at the level of the affected behavior.

---

## 9. What Revamp must not do

### 9.1 Preserve the Vietnamese output contract

Treat the author's Vietnamese output discipline as protected behavior. Shorter wording, fewer characters, cleaner architecture, uniformity, machine-oriented control text, technical tone, and refactoring do not justify weakening it. English control text and user-facing language have separate requirements. A field term is not an exact identifier. The user's use of English terms does not authorize code-switching or a higher register. Preserve the target's authorized exceptions and request-specific overrides.

**Contract gate.** What concrete failure or explicit user requirement requires changing the Vietnamese output contract? Without either, preserve the contract.

**Clause gate.** What concrete failure or explicit user requirement requires changing this specific language guard? Ask separately for every affected guard, including everyday Vietnamese, plain register, English exceptions, field terms versus identifiers, translation of other English, bilingual labels, and the final scan where applicable. A general reason to edit the contract does not answer the clause-level question. Without a clause-specific basis, preserve the guard or its full behavioral equivalent.

Apply both gates in proposal review, implementation, and final diff review.

---

### 9.2 Do not turn every recurring inconvenience into a primitive

Before adding a schema, registry, Router, manifest, validator, owner file, lifecycle state, governance layer, or new abstraction, ask:

> What concrete failure in the current baseline requires this?

If no concrete failure requires it, keep it out of the baseline.

---

### 9.3 Do not redesign from names, summaries, or apparent patterns

Inspect the real files, workflow, and runtime behavior first.

```text
FILENAME != SEMANTICS
DIRECTORY != ONTOLOGY
CO-LOCATION != DEPENDENCY
REPEATED PATTERN != SHARED OWNER
```

Do not infer a system merely because its serialization looks familiar.

---

### 9.4 Do not mistake serialization for the thing being serialized

This is especially important for projects built from internal simulation or long-lived conceptual systems.

A repository may be a serialization of an existing mental process.

Improving the serialization must not silently redefine the original process.

```text
FILE STRUCTURE != CONCEPTUAL STRUCTURE
EXTERNALIZATION != ORIGIN
DOCUMENT OWNER != SEMANTIC OWNER UNLESS ESTABLISHED
```

---

### 9.5 Do not normalize heterogeneous components for elegance

A shared document envelope may be useful.

A shared ontology, runtime, component schema, lifecycle, or dependency model requires separate evidence.

```text
COMMON FORMAT != COMMON INTERNAL ARCHITECTURE
FAMILY RESEMBLANCE != SHARED SCHEMA
COMPOSITION != DEPENDENCY
```

---

### 9.6 Do not repair UNKNOWN by invention

The model's strongest failure mode is often plausible completion.

```text
NOT FOUND != FALSE
UNKNOWN != EMPTY
UNKNOWN != PERMISSION TO INVENT
PLAUSIBLE != CONFIRMED
```

A clean-looking system built from invented bridges is worse than an incomplete but truthful system.

---

### 9.7 Do not promote analysis into authority

A good diagnosis is still a diagnosis.

A good proposal is still a proposal.

A Codex implementation plan is still not an implementation.

A local implementation is still not a commit or push.

A repository publication is still not live Project verification.

Preserve stage boundaries.

---

### 9.8 Do not use a past failure as permission for permanent over-control

A guardrail should remain no broader than the failure it solves.

If a failure disappears because the underlying system changes, reconsider the control rather than treating historical pain as permanent proof that maximum restriction is necessary.

History should prevent regression, not prohibit evolution.

---

### 9.9 Do not let Revamp become recursive governance

Revamp exists partly because previous control work could over-expand.

Therefore Revamp must be especially suspicious of:

- a Router for the Router;
- a registry of registries;
- an anti-drift layer for every anti-drift layer;
- a state engine merely to track control state;
- governance added because governance already exists;
- self-review loops that generate more control artifacts without a distinct recurring failure.

```text
CONTROL COMPLEXITY IS STILL COMPLEXITY.
```

---

### 9.10 Do not silently copy FTH architecture into other projects

FTH contains hardened solutions to FTH-scale problems.

Fanfiction Engine, FSP, Image Transcendent, Central Hub, and other projects may have different semantics, owners, runtime boundaries, or failure costs.

Use FTH as evidence of a solution that worked in its scope, not as proof of a universal template.

---

### 9.11 Do not overwrite the user's viable simple proposal with a more formal one

First ask:

> Can the user's proposal work with small corrections?

If yes, correct locally.

Do not replace a viable simple mechanism merely because a more systematic architecture can be imagined.

---

### 9.12 Do not turn design lineage into runtime dependency

```text
DESIGN SOURCE != RUNTIME DEPENDENCY
PROVENANCE != AUTOLOAD
REFERENCE != ACTIVE CONTROL
```

Establish the intended relation before interpreting inheritance or base wording. If the intended behavior is self-contained, integrate the required logic directly; an assumption that an external base is active cannot replace missing controls.

Do not infer that every base must be embedded. A project may intentionally use real runtime composition. The failure to avoid is silently changing one relation into another, not runtime composition itself. Inspect that project's intent and sources rather than imposing Revamp's architecture.

---

## 10. Use after current target inspection

Independent tasks need no repository, History, or CURRENT preflight. For repository- or system-dependent work:

1. Use the loaded skill core to identify the current operation, delivery form and scope. No legacy selector or external governing artifact is required.
2. Inspect current target sources, implementation and relevant runtime evidence first. Establish behavior, any failure mechanism, constraints, owners and the proposal or authorized requirement. Apply Architecture Preflight only under its own conditions.
3. Consult this reference only when a prior failure, precedent, provenance or decision materially affects the task. Compare the old mechanism and conditions with present evidence before using a lesson. A failure observed in ChatGPT/Project does not establish applicability in Codex or any other runtime. Missing historical evidence limits only conclusions that depend on it.
4. Read needed CURRENT only when material continuity remains. Reading this reference is not a prerequisite for CURRENT.
5. Classify findings as observed failure, reproduced failure, supported risk, or hypothetical future risk.
6. Identify the smallest level of change that can solve the established problem.
7. Preserve working behavior and known-safe fallback.
8. Keep unrelated workstreams separate.
9. Do not mutate files, commit, push, deploy, or promote status without explicit authorization.

Reading this file does not activate every warning as a mandatory control.

The cases provide a record of why earlier controls were introduced:

> The repository already contains complexity created by real failures. Add more only when a present failure still requires it.

---

## 11. Relationship to handoffs

Establish current target evidence before recovering CURRENT. Consult History only for a material historical dependency.

The skill core selects materially required context under the current operation and scope. Target sources establish implementation and ownership. CURRENT supplies bounded continuation state when materially needed. History supplies failure context and preventive guidance. Authority to change the target remains with the user. Reading History confers no authority to replace the target's architecture or rules.

---

## 12. Final warning

Revamp Project System was created because the model repeatedly caused damage by being too willing to complete, normalize, generalize, restructure, and "improve" systems it did not yet understand well enough.

The project fails its own purpose if it repeats the same behavior under a more sophisticated vocabulary.

The intended reflex is:

```text
SEE FRICTION
→ IDENTIFY THE ACTUAL FAILURE
→ INSPECT THE REAL SYSTEM
→ PRESERVE WHAT WORKS
→ APPLY THE SMALLEST SUFFICIENT CHANGE
→ TEST
→ STOP WHEN THE FAILURE IS SOLVED
```

Not:

```text
SEE FRICTION
→ INVENT A GENERAL THEORY
→ BUILD A NEW CONTROL LAYER
→ MIGRATE EVERYTHING
→ CALL THE RESULT CLEANER
```

Final invariant:

> DO NOT GO TO MARS TO CROSS THE STREET.

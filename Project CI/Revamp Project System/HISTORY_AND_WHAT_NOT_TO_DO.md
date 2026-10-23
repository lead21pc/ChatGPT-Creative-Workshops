# Revamp Project System — History and What Not to Do

STATUS: REFERENCE / PREFLIGHT
SCOPE: Revamp Project System only.
ROLE: Historical failure context and preventive guidance for Revamp work.
NOT: Current workstream state, canon, repository authority, implementation authorization, a second Router, or a replacement for CURRENT handoffs.

---

## 1. Why this file exists

Revamp Project System did not begin as an abstract architecture exercise.

It exists because repeated work with ChatGPT exposed recurring failure modes that could damage the user's concepts, project structure, and already-working controls. Many controls in the wider repository were created only after a concrete failure had already happened.

This file preserves that history so Revamp does not repeat the same pattern while trying to improve the system.

Core warning:

> A control system created to prevent distortion must not become a new source of distortion.

Historical context is a preflight constraint, not a reason to freeze the system. Use it to recognize known failure patterns, then inspect the real current system before proposing changes.

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

---

## 9. What Revamp must not do

### 9.1 Do not turn every recurring inconvenience into a primitive

Before adding a schema, registry, Router, manifest, validator, owner file, lifecycle state, governance layer, or new abstraction, ask:

> What concrete failure in the current baseline requires this?

If no concrete failure requires it, keep it out of the baseline.

---

### 9.2 Do not redesign from names, summaries, or apparent patterns

Inspect the real files, workflow, and runtime behavior first.

```text
FILENAME != SEMANTICS
DIRECTORY != ONTOLOGY
CO-LOCATION != DEPENDENCY
REPEATED PATTERN != SHARED OWNER
```

Do not infer a system merely because its serialization looks familiar.

---

### 9.3 Do not mistake serialization for the thing being serialized

This is especially important for projects built from internal simulation or long-lived conceptual systems.

A repository may be a serialization of an existing mental process.

Improving the serialization must not silently redefine the original process.

```text
FILE STRUCTURE != CONCEPTUAL STRUCTURE
EXTERNALIZATION != ORIGIN
DOCUMENT OWNER != SEMANTIC OWNER UNLESS ESTABLISHED
```

---

### 9.4 Do not normalize heterogeneous components for elegance

A shared document envelope may be useful.

A shared ontology, runtime, component schema, lifecycle, or dependency model requires separate evidence.

```text
COMMON FORMAT != COMMON INTERNAL ARCHITECTURE
FAMILY RESEMBLANCE != SHARED SCHEMA
COMPOSITION != DEPENDENCY
```

---

### 9.5 Do not repair UNKNOWN by invention

The model's strongest failure mode is often plausible completion.

```text
NOT FOUND != FALSE
UNKNOWN != EMPTY
UNKNOWN != PERMISSION TO INVENT
PLAUSIBLE != CONFIRMED
```

A clean-looking system built from invented bridges is worse than an incomplete but truthful system.

---

### 9.6 Do not promote analysis into authority

A good diagnosis is still a diagnosis.

A good proposal is still a proposal.

A Codex implementation plan is still not an implementation.

A local implementation is still not a commit or push.

A repository publication is still not live Project verification.

Preserve stage boundaries.

---

### 9.7 Do not use a past failure as permission for permanent over-control

A guardrail should remain no broader than the failure it solves.

If a failure disappears because the underlying system changes, reconsider the control rather than treating historical pain as permanent proof that maximum restriction is necessary.

History should prevent regression, not prohibit evolution.

---

### 9.8 Do not let Revamp become recursive governance

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

### 9.9 Do not silently copy FTH architecture into other projects

FTH contains hardened solutions to FTH-scale problems.

Fanfiction Engine, FSP, Image Transcendent, Central Hub, and other projects may have different semantics, owners, runtime boundaries, or failure costs.

Use FTH as evidence of a solution that worked in its scope, not as proof of a universal template.

---

### 9.10 Do not overwrite the user's viable simple proposal with a more formal one

First ask:

> Can the user's proposal work with small corrections?

If yes, correct locally.

Do not replace a viable simple mechanism merely because a more systematic architecture can be imagined.

---

## 10. Required preflight posture

Before substantial Revamp audit/design work:

1. Read `HANDOFF_ROUTER.yaml` as the Revamp entrypoint.
2. Inspect current relevant repository sources as directed by the Router, then FULL_FILE-read this file as historical failure context before any CURRENT handoff recovery.
3. Load only materially matched CURRENT handoffs in FULL_FILE mode.
4. Inspect the actual system relevant to the task.
5. Classify findings as observed failure, reproduced failure, supported risk, or hypothetical future risk.
6. Identify the smallest level of change that can solve the established problem.
7. Preserve working behavior and known-safe fallback.
8. Keep unrelated workstreams separate.
9. Do not mutate files, commit, push, deploy, or promote status without explicit authorization.

Reading this file does not activate every warning as a mandatory control.

It supplies a historical prior:

> The repository already contains complexity created by real failures. Add more only when a present failure still requires it.

---

## 11. Relationship to handoffs

This file is not a CURRENT handoff.

It should be read before Revamp handoff recovery because it explains the failure history and operating posture that should shape interpretation of later state.

Order:

```text
HANDOFF_ROUTER
→ current relevant repository sources / accepted decisions / implementation
→ REVAMP HISTORY / WHAT NOT TO DO (FULL_FILE)
→ materially matched CURRENT handoff(s)
→ real files / runtime needed for the task
→ audit / design / implementation within authorized scope
```

The Router still owns handoff selection.

CURRENT files still own bounded continuation state.

This file must not become a global memory dump, repository snapshot, or second authority system.

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

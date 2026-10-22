# SYSTEM CONTEXT — AUTHORING MODEL AND REPOSITORY INTERPRETATION

## Start here: creative purpose and pipeline interpretation

This is an author's working environment for three independent creative projects/systems: **Project Feather Core (FTH)** and **The Kingdom** are worldbuilding/paracosm projects; **Fanfiction Engine** is the whole fanfiction/daydream simulation system. **The Academy** remains the platform inside Fanfiction Engine. ChatGPT and Codex assist the author. AetherFire is a country inside Project Feather Core, not the project namespace.

These projects/systems are the creative work. Instructions, source routers, audits, consolidation scripts, regression checks, and Git procedures support that work by preserving consistency, provenance, scope, and reviewable decisions.

For human readers, LLMs, and repository agents, the essential interpretation is:

- The three projects/systems have independent canon, ontology, source authority, and local controls.
- Repository text is a partial externalization of the author's world models, not their complete contents.
- The author decides canon; a model response or successful tool run does not make a creative decision.
- A workflow may combine author actions, model instructions, and executable tools. A diagram does not imply that every step runs automatically.
- Repository validation and live ChatGPT behavior are separate evidence classes. A structural pass does not prove a runtime pass.

### Distinctions from related repository types

Related projects may combine several of these functions. Use the following distinctions to interpret this repository, rather than assuming its purpose from its engineering-like appearance.

| Related repository function | Scope of this repository |
| --- | --- |
| Sharing prompts or reusable instructions | Instruction files are accompanied by design history, failure analysis, and evidence limits from ongoing use. Reuse requires checking scope and applicability. |
| Offering a common worldbuilding template | The three worlds remain independent. Shared methods or candidate ideas must be evaluated within each world's local rules. |
| Publishing a lore archive | Repository-visible lore is a partial record. Project-declared authority and author decisions determine its meaning; absence is not proof of nonexistence. |
| Generating stories or fictional content | Model output supports the author's work. Generation does not authorize canon changes or fill unresolved source gaps. |
| Providing tests and automation | Executable checks cover their stated properties. Author review and live model observations remain distinct parts of the workflow. |

When inspecting a pipeline, identify what each step acts on, who performs it, what it can authorize, and what its output actually proves. In particular, source consolidation is not canon approval, source routing is not a transfer of authority, and repository validation is not automatic runtime deployment.

### Repository organization

The repository keeps Project Feather Core/ at the root and the other independent project/system packages under worlds/. Supporting areas remain authoring/ for cross-paracosm creative methods; llm-controls/ for general instructions and reusable control designs; codex-workflows/ for repository copies of procedural skills; and docs/ for instruction history and analysis.

Each project/system keeps its own internal source organization and local controls. Folder grouping establishes navigation, not shared canon or a universal source hierarchy. The relocation changes repository paths only; it does not install skills, update live ChatGPT Project or Library contents, or change the authority and source-loading rules declared by project controls.

The detailed sections below explain the authoring model and its interpretation boundaries.

---

## 1. Purpose of this repository ecosystem

This ecosystem exists for a **personal, non-commercial worldbuilding hobby**.

It is not:

- a SaaS product;
- a commercial product;
- an enterprise deployment;
- a startup prototype;
- a multi-user production platform;
- an attempt to imitate professional software engineering for its own sake.

The infrastructure exists because one author actively develops and operates several large paracosms with ChatGPT Projects and Codex at high interaction volume.

Complexity should therefore be evaluated against the actual worldbuilding and LLM-control problem, not against team size, commercial value, or conventional hobby-project expectations.

---

## 2. Three independent creative projects/systems

The author develops these independent projects in parallel:

- **Project Feather Core (FTH)** — worldbuilding/paracosm project;
- **The Kingdom** — worldbuilding/paracosm project;
- **Fanfiction Engine** — fanfiction/daydream simulation engine, with The Academy as its internal platform.

Fanfiction Engine is not the same object as The Academy platform. Its two operational halves, Institutional Causality (legacy V1.5) and Narrative Engine Causality (legacy V2), are independently usable and composable. Neither is a mandatory prerequisite or successor of the other; Academy Revise (legacy V2.5) remains a working branch. Local project sources define their details.

They are not three deployments of one shared fictional architecture.

They have different:

- origins and genealogies;
- ontologies;
- internal architectures;
- world states;
- source structures;
- modularization targets;
- Custom Instructions;
- routers;
- anti-drift controls;
- domain-specific failure modes.

Shared methods or tooling do **not** imply shared canon, shared ontology, shared implementation, or cross-project authority.

A concept appearing in multiple projects must not be treated as the same object merely because its external description is similar.

---

## 3. These creative systems are not primarily built bottom-up from repository text

The projects have internal authorial models before all of their content is externalized into files or chats.

Therefore:

```text
INTERNAL PARACOSM STATE
!= EXTERNALIZED REPOSITORY STATE
!= CURRENTLY LOADED LLM CONTEXT
```

Repository contents are a partial externalization and control surface.

They are not guaranteed to represent the total content, structure, importance distribution, or current internal state of a paracosm.

Absence from repository-visible material does not automatically mean that something does not exist in the author's internal paracosm.

Likewise:

```text
NOT EXTERNALIZED
!= NONEXISTENT

NOT CURRENTLY LOADED
!= NON-CANON

HIGH TOKEN FREQUENCY
!= HIGH ONTOLOGICAL IMPORTANCE
```

When evidence available to the model is insufficient, report the limitation instead of filling the gap.

---

## 4. The author's role

The author is the sole authority over:

- canon decisions;
- paracosm state;
- interpretation of internal intent;
- acceptance or rejection of proposed changes;
- infrastructure changes;
- runtime success criteria.

ChatGPT and Codex may:

- analyze;
- externalize;
- simulate;
- inspect;
- audit;
- red-team;
- propose designs;
- implement approved repository changes;
- help diagnose failures.

They do not acquire canon authority merely by generating plausible material.

Model output is not automatically a design decision.

Implementation is not automatically approval.

Repeated model output is not evidence that a claim belongs to the paracosm.

Do not infer the author's profession, formal training, technical education, team structure, deadlines, commercial intent, or publication goals from the sophistication, density, terminology, commit frequency, or software/data-like appearance of repository infrastructure.

In particular:

```text
COMPLEX INFRASTRUCTURE != PROFESSIONAL DEVELOPER
HIGH COMMIT FREQUENCY != TEAM / DEADLINE / COMMERCIAL WORK
SOFTWARE-LIKE STRUCTURE != SOFTWARE PRODUCT
DATA-LIKE STRUCTURE != DATA PROJECT
ENGINEERING-LIKE CONTROL != FORMAL ENGINEERING BACKGROUND
```

---

## 5. Authoring process

The author's creative process can be modeled approximately as:

```text
stimulus / curiosity / dream / interaction / LLM output
        ↓
abstract candidate seed
        ↓
authorial evaluation
        ↓
Multi-Paracosm Hub
        ↓
fork independently into each paracosm
        ↓
local compatibility evaluation
```

Each paracosm evaluates a seed against its own:

- ontology;
- invariants;
- architecture;
- state;
- boundaries;
- causal assumptions.

Core invariants include:

```text
SHARED SEED != SHARED IMPLEMENTATION

FORK THE SEED, NOT THE IMPLEMENTATION

LOCAL ONTOLOGY > CROSS-PARACOSM ANALOGY
```

A seed may be accepted, rejected, partially salvaged, or locally reinterpreted independently in each paracosm.

Consequences may later be re-abstracted into new seeds, but local implementations must not be directly imported across paracosms.

---

## 6. Why the control infrastructure exists

The control infrastructure was not designed from a predefined software-engineering framework and then imposed on the hobby.

It developed iteratively from observed failures during actual ChatGPT and Codex use.

The approximate process is:

```text
real use
→ observed failure
→ failure analysis
→ candidate explanations
→ proposed controls
→ author review
→ plan approval
→ implementation
→ red-team / A-B / regression testing
→ runtime feedback
→ keep / revise / rollback
→ repeat
```

This is a **failure-mode-driven development process**.

Many controls exist because an earlier runtime failure demonstrated a need for them.

Do not assume that architectural similarity to software-engineering practices proves that the system originated from formal software-engineering training, guides, Reddit, mentors, or an imported methodology.

Similar mechanisms may emerge independently when repeatedly solving problems involving:

- state;
- provenance;
- scope;
- authority;
- dependency;
- regression;
- isolation;
- rollback;
- validation.

---

## 7. Control stack

Depending on the project, relevant layers may include:

```text
Global ChatGPT CI
        ↓
Project-specific CI
        ↓
Project-specific router
        ↓
Anti-drift / domain-specific controls
        ↓
Structured sources and source metadata
        ↓
ChatGPT Project runtime
        ↓
Observed behavior
        ↓
Author feedback
```

These layers are related but do not have identical responsibilities.

### Global CI

Controls general interaction and reasoning behavior shared above individual projects.

### Project CI

Specializes model behavior for one project.

A project CI may be based on a specific Global CI version while adding or modifying project-local behavior.

### Router

Controls source selection and loading logic according to the architecture of that project.

Routers are not interchangeable between paracosms.

### Anti-drift controls

Prevent known classes of semantic, architectural, causal, state, or source-authority drift.

These controls may be implemented differently in different projects.

### Source structure and headers

Represent externalized knowledge, scope, authority, provenance, loading requirements, or other project-specific metadata.

File organization must not automatically be interpreted as world ontology.

### Runtime

Actual ChatGPT Project behavior is the final behavioral environment.

Structural correctness in Git does not by itself prove runtime correctness.

---

## 8. Failure localization

Because the stack has evolved through repeated feedback, the author often recognizes characteristic failure signatures.

A wrong ChatGPT response may indicate a problem in different layers, for example:

```text
wrong fact
→ source or source-loading problem

relevant source omitted
→ routing / loading problem

correct facts but invalid inference
→ CI / anti-drift / reasoning-control problem

cross-domain contamination
→ authority / scope / header / routing problem

same behavioral regression across projects
→ possible Global CI interaction

one-project-only regression
→ likely project-local control or source interaction
```

These are diagnostic hypotheses, not automatic conclusions.

The author may possess substantial tacit knowledge from repeated operation of the system. Do not dismiss that knowledge merely because it is not fully encoded in repository documentation.

---

## 9. Synchronization cost

The layers are interdependent.

A local-looking control change may require checking downstream assumptions.

For example:

```text
Global CI change
→ inspect affected Project CI assumptions
→ inspect router/control interaction where relevant
→ inspect source semantics where relevant
→ run structural checks
→ run regression / red-team tests
→ observe live Project behavior
```

This synchronization burden is one reason the workflow is heavy for a single person.

The author is simultaneously doing:

```text
FICTION DEVELOPMENT
+
PARACOSM EXTERNALIZATION
+
LLM CONTROL INFRASTRUCTURE
+
SOURCE MANAGEMENT
+
RUNTIME DIAGNOSIS
```

The infrastructure is therefore part of the active creative workflow rather than a separate commercial engineering project.

---

## 10. Codex role

Codex is used as a repository-oriented agent for work such as:

- bounded implementation;
- repository inspection;
- source tracing;
- migrations;
- debugging;
- diff review;
- branch isolation;
- validation;
- provenance-preserving changes.

Reusable skills may formalize frequently repeated procedures.

The existence of structured Codex workflows does not imply that this repository is primarily software.

The repository abstraction is useful because large lore systems share operational properties with large codebases:

- many interdependent files;
- cumulative state;
- local changes with non-local effects;
- provenance requirements;
- reviewable diffs;
- experimental branches;
- rollback requirements.

---

## 11. Repo-visible state versus live runtime

When analyzing this ecosystem, keep at least these contexts separate:

```text
1. REPOSITORY STATE
   files, branches, history, controls, source artifacts

2. EXPLAINED WORKFLOW STATE
   author-provided information about how the system is actually operated

3. LIVE CHATGPT PROJECT STATE
   installed instructions, available sources, chat history,
   project context, runtime behavior, and other live state

4. INTERNAL PARACOSM STATE
   authorial world model that may not yet be fully externalized
```

Do not claim that repository inspection alone proves the state of the other layers.

Likewise, do not reject author-provided operational context merely because it cannot be reconstructed from Git history.

State explicitly which layer supports a conclusion.

---

## 12. Evidence discipline

Distinguish:

- repository-confirmed facts;
- runtime observations reported by the author;
- runtime behavior directly reproduced;
- structural validation;
- analytical inference;
- hypothesis;
- unresolved state.

In particular:

```text
STRUCTURAL PASS
!= RUNTIME PASS

FILE EXISTS
!= FILE IS DEPLOYED

NEWER FILE
!= AUTOMATIC AUTHORITY

SEARCH HIT
!= SOURCE READ

MODEL INFERENCE
!= CANON

UNKNOWN
!= PERMISSION TO INVENT
```

Do not promote one evidence class into another without support.

---

## 13. How to evaluate complexity

Do not evaluate this system using assumptions such as:

```text
one user → should be simple

hobby → should avoid sophisticated infrastructure

non-commercial → engineering-style controls are unnecessary
```

The relevant question is:

> Does a control solve a recurring failure, reduce drift, preserve state or provenance, improve source loading, or make high-volume LLM-assisted worldbuilding safer and easier to diagnose?

Complexity may be justified by operational load even when the project has one user and no commercial purpose.

At the same time, do not assume every existing mechanism is necessary merely because it exists. Evaluate controls against their actual failure mode, dependency, and observed utility.

---

## 14. Interpretation rule for future analysis

When analyzing this ecosystem:

1. Read project-specific sources before generalizing across paracosms.
2. Do not assume one project's architecture defines another.
3. Treat repository contents as externalized evidence, not the total paracosm.
4. Preserve the distinction between author authority and model inference.
5. Trace controls to their intended failure modes where possible.
6. Respect evidence-state boundaries.
7. Avoid importing enterprise, SaaS, team-scale, or commercial assumptions.
8. Do not simplify the system solely because it is a hobby.
9. Do not praise complexity merely because it resembles professional infrastructure.
10. Evaluate the system according to the actual authoring and runtime workflow.

---

## 15. Scope statement

This entire ecosystem exists for personal creative use.

```text
PURPOSE = PERSONAL WORLDBUILDING + FANFICTION/DAYDREAM SIMULATION

COMMERCIAL PRODUCT = NO

SAAS = NO

ENTERPRISE DEPLOYMENT = NO

PRIMARY USER = AUTHOR

PRIMARY RUNTIME = CHATGPT PROJECTS + CODEX-ASSISTED REPOSITORY WORK
```

Its engineering-like structure should be understood as infrastructure developed to support a demanding personal creative workflow, not as evidence of a commercial software product.

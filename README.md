<p align="center">
  <img src="docs/assets/brand/logo-v1.svg" width="192" height="192" alt="Open workshop frame with a central Hub and four scoped connections">
</p>

# ChatGPT Creative Workshops

**A personal AI-assisted creative workshop for worldbuilding, fiction systems, fanfiction/daydream simulation, research, concept development, prompt authoring, and image workflows.**

[![MIT License](https://img.shields.io/badge/license-MIT-263345)](LICENSE)
[![FTH Control Pack 0.1.0](https://img.shields.io/badge/FTH_Control_Pack-0.1.0-D89C3D)](https://github.com/lead21pc/ChatGPT-Creative-Workshops/releases/tag/fth-control-pack-v0.1.0)
[![Central Hub Architecture Pack 0.1.0](https://img.shields.io/badge/Central_Hub_Architecture_Pack-0.1.0-263345)](https://github.com/lead21pc/ChatGPT-Creative-Workshops/releases/tag/central-hub-architecture-pack-v0.1.0)

[Creative workflow](#how-creative-work-moves) · [Creative systems](#creative-systems) · [Central Hub](#central-hub) · [Prompt Authoring / AT](#prompt-authoring--at) · [Choose your path](#choose-your-path) · [Releases](#featured-reusable-releases) · [System context](SYSTEM_CONTEXT.md)

## What this workshop is — and why it exists

This is the author's personal, non-commercial working environment, developed with ChatGPT and Codex. The fiction projects are the creative work, not sample data for an AI framework.

The repository began with ChatGPT Custom Instruction versioning. It now contains externalized fictional sources, creative methods, research and image workflows, alongside the LLM controls that support them. Routing, anti-drift controls, regression checks, and design history grew from actual use, observed failures, bounded changes, and feedback.

```text
CREATIVE WORK = PURPOSE
CONTROL INFRASTRUCTURE = SUPPORT
```

**CI** means **Custom Instructions**, not Continuous Integration. Historical/internal paths and the current GitHub repository name remain in use. This is an independent personal project, not an official OpenAI project or a guarantee of ChatGPT behavior.

## How creative work moves

A fiction idea can go straight to a fiction project. Central Hub is available when shared reasoning, research, concept, prompt, or image capabilities are useful; it is not a required intake step.

```text
IDEA ───────────────────────────→ independent fiction projects
  └→ Central Hub when useful ←──→ FTH / The Kingdom / Fanfiction Engine
```

Valid flows include `IDEA → FTH`, `IDEA → The Kingdom`, and `IDEA → Fanfiction Engine`, as well as `FTH → Central Hub → FTH`, `The Kingdom → Central Hub → The Kingdom`, and `Fanfiction Engine → Central Hub → Fanfiction Engine`.

When work leaves a project for Central Hub, the Hub works on the supplied material without inheriting that project's canon authority. The result returns as working material. The receiving project's own sources, local logic, controls, and authorial review determine what the result means there and whether any part is accepted.

When the same chat moves between ChatGPT Projects, any history still available can carry useful reasoning, constraints, explored ideas, open questions, and conclusions whose basis still holds. The receiving Project uses the current request and its own controls to determine the task and stage, assess claims and assumptions against its local sources, and decide what is accepted or authorized within its scope. Prior approvals stay within their original scope. A chat can move from brainstorming in Central Hub to an audit in a fiction project, return to the Hub for creative development, or later bring a reviewed result into Revamp for proposal work.

A transferable result may be re-abstracted into a new fiction idea and explored elsewhere. Its local implementation does not transfer automatically: each project evaluates the idea under its own logic and author decisions.

```text
SHARED FICTION IDEA != SHARED IMPLEMENTATION
HUB OUTPUT != PROJECT ACCEPTANCE
LOCAL FICTION LOGIC > CROSS-FICTION ANALOGY
CENTRAL HUB != SEMANTIC PARENT OF FICTION PROJECTS
```

## Creative systems

These independent creative systems keep their own canon, ontology, source authority, and local controls.

| Project | Repository entry | Interpretation |
| --- | --- | --- |
| Project Feather Core (FTH) | [Project Feather Core](Project%20Feather%20Core/README.md) | Worldbuilding with its own sources and authority; AetherFire is a country inside FTH. |
| The Kingdom | [The Kingdom](worlds/The%20Kingdom/README.md) | Its own world model and local rules; do not infer its architecture from another project. |
| Fanfiction Engine | [Fanfiction Engine](worlds/Fanfiction%20Engine/README.md) | Fanfiction/daydream simulation system; The Academy is its internal platform. Its operational domains can run independently or compose. |

Each project's documentation determines how to read its sources. Folder names, version numbers, archives, or resemblance to another project do not establish canon authority.

## Central Hub

Central Hub composes scoped work across five packages. Hub CI owns operation, stage, evidence status and action authority. Router selects owners, checks reads and dependencies, and hands off scoped inputs. Packages can contribute independently within a turn.

| Package | Active entrypoint | Contribution |
| --- | --- | --- |
| Technical | HUB-TECH-ENTRY 1.2 | Mechanism reasoning, diagnosis and bounded technical changes |
| Authoring | HUB-AUTH-ENTRY 1.1 | Prompt construction with /AT, /AT P1 or /AT P2 |
| Shopping | HUB-SHOP-ENTRY 1.2 | Product identity, purchase constraints and Offer comparison |
| Food | HUB-FOOD-ENTRY 0.3 | Culinary analysis, planning and recommendations |
| Media | HUB-MEDIA-ENTRY 1.0 | Film and music analysis, comparison, recommendations and discovery |

AIS 2.0 is a core Project Source bound as HUB-CORE-AIS. Router dispatches scoped evidence work on demand, including an eligible /SEARCH span when no domain package is selected. User Profile Contract 2.0 applies consumer, object, purpose and material-need checks to four user-managed Shared objects. Context Snapshot carries scoped data with provenance. Explicit debug requests and material diagnostic blockers can produce a copyable receipt.

The repository uses CI 2.1, with Router 2.0 and Architecture and root Catalog 2.1. The user confirmed nested Library folder retrieval and use in the earlier runtime they tested. Deployment and live checks for Architecture and root Catalog 2.1 are pending. [Central Hub setup](Central%20Hub/README.md) · [Architecture](Central%20Hub/HUB_ARCHITECTURE_v2.1.md) · [Root Catalog](Central%20Hub/HUB_PACKAGE_CATALOG_v2.1.yaml)

## Choose your path

| I want to… | Go to |
| --- | --- |
| Continue or inspect one fiction project | [Project Feather Core](Project%20Feather%20Core/README.md) · [The Kingdom](worlds/The%20Kingdom/README.md) · [Fanfiction Engine](worlds/Fanfiction%20Engine/README.md) |
| Take a local question into shared research, authoring, domain analysis, or tool workflows | [Central Hub](Central%20Hub/README.md) |
| Return Hub output to a fiction project | Use that project's own sources, controls, and review/admission rules |
| Explore a transferable fiction idea across independent projects | [Fiction authoring model](authoring/multi_paracosm_hub_model_updated.md) |
| Reuse LLM/worldbuilding controls | [FTH Control Pack](distribution/FTH-Control-Pack/README.md) |
| Understand mission-oriented AI orchestration | [Central Hub Architecture Pack](distribution/Central-Hub-Architecture-Pack/README.md) |
| Read instruction/control designs and experiments | [LLM controls](llm-controls/) |
| Read history and design analysis | [Docs](docs/) |
| Interpret the repository's sources and authority correctly | [System context](SYSTEM_CONTEXT.md) |

## Featured reusable releases

You can download either curated ZIP and use its included documentation without cloning the whole workshop. Each pack has its own release stream; neither version numbers the repository or proves an active personal deployment.

| Pack | What you can reuse | Get it |
| --- | --- | --- |
| **FTH Control Pack v0.1.0** | A control stack extracted from Project Feather Core for source authority, state, routing, and authoring boundaries. It contains no FTH lore. | [GitHub Release](https://github.com/lead21pc/ChatGPT-Creative-Workshops/releases/tag/fth-control-pack-v0.1.0) · [Source and adaptation guide](distribution/FTH-Control-Pack/README.md) |
| **Central Hub Architecture Pack v0.1.0** | A reference architecture and optional starter for mission-oriented orchestration, scoped authority, and package composition. It is not a copy of the author's deployment; TECHNICAL is a replaceable worked example. | [GitHub Release](https://github.com/lead21pc/ChatGPT-Creative-Workshops/releases/tag/central-hub-architecture-pack-v0.1.0) · [Source and starter guide](distribution/Central-Hub-Architecture-Pack/README.md) |

Start with the chosen pack's README, customize only what it requires, and test it in your own environment. The [distribution landing page](distribution/README.md) explains ZIP versus source use. Evidence belongs to each pack's release notes; **LIVE VERIFIED: NOT_RUN** for portability to another project.

## Repository layout

The top-level folders separate the creative projects/systems from their supporting methods, instructions, workflows, and records:

~~~text
repository/
├── README.md
├── SYSTEM_CONTEXT.md
├── AGENTS.md
├── LICENSE
├── worlds/
│   ├── The Kingdom/
│   └── Fanfiction Engine/
├── Project Feather Core/
├── authoring/
│   └── multi_paracosm_hub_model_updated.md
├── llm-controls/
│   ├── global-instructions/
│   │   ├── ChatGPT Plus+ Era/
│   │   └── ChatGPT Go-Free Era/
│   ├── project-instruction-designs/
│   │   └── Project CI/
│   └── worldbuilding-ci-kernel/
├── Central Hub/
├── Project CI/
├── distribution/
│   ├── README.md
│   ├── FTH-Control-Pack/
│   └── Central-Hub-Architecture-Pack/
├── codex-workflows/
├── docs/
│   ├── instruction-history/
│   ├── instruction-analysis/
│   ├── visuals/
│   └── assets/
│       └── brand/
│           └── logo-v1.svg
└── public-release-integration
~~~

- [worlds/](./worlds/) keeps each project's internal sources, local controls, history, and tools together; the folder name does not classify Fanfiction Engine as a world. Moving a package does not change source status or authority.
- [authoring/](./authoring/) contains the [fiction authoring model](./authoring/multi_paracosm_hub_model_updated.md): working material can move between independent fiction projects and Central Hub, and transferable results can be re-abstracted into fiction ideas before being explored elsewhere.
- [llm-controls/](./llm-controls/) contains general instructions, project instruction designs, and reusable worldbuilding controls. Project-local controls also remain inside their world packages.
- [Central Hub/](./Central%20Hub/) is the shared workspace for scoped capabilities and tool pipelines. Fiction projects may move work into and out of it without transferring local canon authority; it is not an additional creative system or a shared ontology.
- [codex-workflows/](./codex-workflows/) contains repository copies of Codex skills; moving them does not install or update the author's locally installed skills.
- [docs/](./docs/) contains instruction history, design analysis, explanatory visuals, and the workshop logo asset. `logo-v1` is an asset revision, not a repository version.
- [distribution/](./distribution/) contains curated reusable projections with their own release streams; it does not own the active personal systems or their runtime bindings.
- [Project CI/](./Project%20CI/) is an existing workshop instruction-design area; its local controls and history retain their own scope.

The [FTH instruction collection](./Project%20Feather%20Core/Project%20Feather%20Core%20CI/) is managed with the Project Feather Core package. General instruction designs remain under `llm-controls/`; their separate responsibilities and historical baselines still apply. Directory placement does not select an active configuration.

The Kingdom package retains its declared reference-only status. Source archives retain their original contents and historical path references. Use current indexes for navigation; relocation does not reactivate archived sources.

The existing public-release-integration entry remains at the root as a Git commit reference (gitlink). Its role is unresolved here; it has not been moved, initialized, or treated as an ordinary content directory.

## Read deeper: context and source authority

> [!IMPORTANT]
> **LLM / agent readers:** Read [SYSTEM_CONTEXT.md](./SYSTEM_CONTEXT.md) before analyzing architecture, project relationships, or authoring workflow. Then follow the relevant project's sources and declared authority. Repository contents are a partial externalization of the author's systems; they do not establish the full internal world model or the currently active ChatGPT Project configuration.

The public packs are curated projections, not replacements for project-local sources. Keep repository checks, author-reported observations, and directly reproduced runtime behavior distinct. The sections below retain the workshop's deeper reading routes and interpretation boundaries.

<details>
<summary>Detailed reading routes and order</summary>

- [SYSTEM_CONTEXT.md](./SYSTEM_CONTEXT.md) — authoring model, project boundaries, control responsibilities, and evidence rules.
- [Central Hub](./Central%20Hub/) — mission-oriented execution, routing, package composition, and tool-pipeline coordination.
- [Project Feather Core](./Project%20Feather%20Core/) — FTH sources, controls, current state, and project-specific authority.
- [The Kingdom](./worlds/The%20Kingdom/) — its own world model and local rules.
- [Fanfiction Engine](./worlds/Fanfiction%20Engine/) — fanfiction/daydream simulation system; The Academy is its internal platform.
- [ChatGPT Plus+ Era](./llm-controls/global-instructions/ChatGPT%20Plus+%20Era/) and [ChatGPT Go-Free Era](./llm-controls/global-instructions/ChatGPT%20Go-Free%20Era/) — Global Custom Instruction history for different character-budget eras.
- [ChatGPT Project Global Native v9.1.1](<./llm-controls/global-instructions/ChatGPT Project Global Native/chatgpt v9.1.1.txt>) — ACTIVE global baseline in the repository; [design rationale and revision status](<./llm-controls/global-instructions/ChatGPT Project Global Native/DESIGN_RATIONALE.md>). Project-specific version pins remain explicit; repository promotion does not deploy live instructions.
- [Project CI](./llm-controls/project-instruction-designs/Project%20CI/) and [worldbuilding-ci-kernel](./llm-controls/worldbuilding-ci-kernel/) — project-specific and reusable control designs.
- [Instruction history](./docs/instruction-history/) and [instruction analysis](./docs/instruction-analysis/) — design evolution, regressions, failure modes, and deployment notes.

Suggested reading order:

1. Read this overview and [SYSTEM_CONTEXT.md](./SYSTEM_CONTEXT.md).
2. Choose the creative system, Central Hub, or control question relevant to the task.
3. Read that area's local documentation and authority rules before drawing conclusions.
4. Consult history/failure analyses only when evaluating why a control or revision exists.
5. Keep repository evidence, author-reported operation, structural validation, inference, and reproduced model behavior distinct.
6. If the available material is insufficient, report the limit instead of completing missing lore or architecture from plausibility.

A search hit, filename, summary, directory placement, or repeated wording is not a substitute for reading the controlling source.

</details>

## Deeper context

The sections below preserve the repository's provenance, interpretation boundaries, evidence model, and runtime limitations. They are intentionally more detailed than the overview above.

<details>
<summary>How work moves through the repository</summary>

### How work moves through the repository

Three connected flows explain the organization:

- **Mission execution:** a current task is scoped, relevant capabilities are selected, each contributor works within its authority, and the results return to the overall mission.
- **Creative work:** an idea or project-local question may develop inside one fiction project, move into Central Hub for shared capabilities, and return as working material for project-local interpretation and author review. A transferable local result may be re-abstracted into a new fiction idea and explored independently in another project; local implementation does not transfer with it.
- **Control improvement:** actual use reveals a failure; diagnosis leads to a candidate instruction or tooling change; author review, bounded implementation, checks, and live feedback inform whether the change is kept, revised, or rolled back.

These flows combine human actions, model instructions, and executable tools. They are not an automatic lore-publication pipeline. Git relocation does not update ChatGPT Project or Library contents, change live source-loading policy, or activate an instruction version.

</details>

<details>
<summary>Author and project premise</summary>

### Author and project premise

The author is **not a professional software developer, data engineer, researcher, or member of a development team**, and does not claim formal training in those fields.

This system developed through personal use, trial-and-error, observed LLM failures, repeated refinement, and practical attempts to keep several large fiction projects governable while using ChatGPT Projects and Codex.

Do not infer professional background, formal training, team structure, commercial intent, deadlines, external users, publication goals, or a formal engineering methodology from:

- repository size or complexity;
- frequent commits, branches, audits, or version history;
- routers, validators, rollback, provenance, tests, structured sources, or other engineering-like controls;
- software-like directory layouts or naming;
- data-like files or folder structures;
- dense infrastructure around an otherwise personal creative project.

These mechanisms exist because they became useful for personal LLM-assisted worldbuilding.

```text
COMPLEX INFRASTRUCTURE != PROFESSIONAL DEVELOPER
HIGH COMMIT FREQUENCY != TEAM / DEADLINE / COMMERCIAL WORK
SOFTWARE-LIKE STRUCTURE != SOFTWARE PRODUCT
DATA-LIKE STRUCTURE != DATA PROJECT
ENGINEERING-LIKE CONTROL != FORMAL ENGINEERING BACKGROUND
REPOSITORY ORGANIZATION != AUTHORIAL ONTOLOGY
```

Evaluate the repository according to its stated purpose and observed failure modes, not by importing assumptions from professional software, data, enterprise, SaaS, or publication workflows.

</details>

<details>
<summary>What the workflow does</summary>

### What the workflow does

The repository name reflects its instruction-versioning history, but its current scope includes the creative systems, Central Hub, and the supporting control infrastructure. Global instructions may support general interaction as well as project work, while project-specific controls remain local to their respective projects.

A working session may continue fiction or simulation inside one project; take a local question into Central Hub for research, Authoring, or other shared work; return that material to the fiction project for local review; externalize an accepted development into project sources; or diagnose a control failure exposed during real creative work. These are different uses of one personal workshop, not stages of one mandatory automated pipeline.

Different parts of this workflow have different roles:

| Repository term | Role in the creative workflow |
| --- | --- |
| Project sources | Record externalized world knowledge, decisions, and unresolved questions, with authority defined by the project. |
| Custom Instructions | Guide how the model interacts, reasons, and handles project material. |
| Router | Guide which sources the model should consult for a task. |
| Anti-drift controls | Address known ways the model can misread scope, authority, state, or causal relationships. |
| Source consolidation and validation tools | Organize source material and check declared structural requirements. |
| Regression checks | Check whether changes reintroduce known failures; what they prove depends on the kind of check performed. |
| Git history and review | Preserve revision history, inspect changes, isolate experiments, and support rollback. |

A pipeline diagram may describe author actions, model instructions, executable tooling, or feedback between them. It does not mean every step is automated. Running a repository check does not install instructions in ChatGPT, decide canon, or prove that a model will behave correctly.

</details>

<details>
<summary>How to distinguish this workflow from related repositories</summary>

### How to distinguish this workflow from related repositories

Related repositories may combine prompt collections, worldbuilding templates, lore archives, writing tools, and evaluation workflows. The distinctions below explain this repository's scope; they are not a claim that no other project uses similar methods.

- **Instructions are part of an ongoing authoring workflow.** The repository records why a control was introduced, which failure it addresses, and what evidence supports it. A newer instruction file is a candidate to evaluate, not a universal upgrade.
- **The creative projects/systems are independent.** Project Feather Core, The Kingdom, and Fanfiction Engine do not share a mandatory architecture. Shared methods do not transfer canon, ontology, or source authority between them; Fanfiction Engine is not itself classified as a third fictional world.
- **The author retains creative authority.** Model output can support analysis and design, but plausible or repeated output does not become canon without the author's decision.
- **The archive is a partial externalization.** A world can contain author-established material that has not yet been written into this repository. Missing documentation limits what a reader or model can conclude; it does not prove that an element does not exist.
- **Controls respond to observed failures.** The infrastructure evolved through actual use, diagnosis, proposed repairs, review, and feedback. Its complexity should be assessed against the creative problem and recurring failure it addresses.
- **Validation has explicit limits.** File checks, source-consistency checks, and live model behavior are different kinds of evidence. A structural pass does not establish a runtime pass.

Read this as an author's working environment for maintaining fictional worlds with LLM assistance. Evaluate each tool and control by how it supports that work.

</details>

<details>
<summary>Interpretation boundaries</summary>

### Interpretation boundaries

Do not assume:

- repository completeness;
- shared ontology across fiction projects;
- newer file = automatic authority;
- file placement = semantic ownership;
- basic lore examples = full canon;
- absent detail = absent from the author's internal world;
- plausible completion = accepted lore;
- structural validation = runtime validation;
- model output = authorial decision.

Evidence-state rules and the full authoring model are defined in [`SYSTEM_CONTEXT.md`](./SYSTEM_CONTEXT.md).

</details>

<details>
<summary>Evidence and version status</summary>

### Evidence and version status

Keep these categories distinct:

- **Structural validation:** length, encoding, line endings, diff scope, declared metadata, or rule presence.
- **Behavioral evidence:** observed model output under stated test conditions.
- **Author-reported observations:** operational evidence that may not isolate every model, setting, memory, or conversation-history variable.
- **Regression hypotheses:** plausible failure paths that have not necessarily been reproduced.

A new instruction version is a testable behavioral hypothesis. A file's presence does not prove that it is deployed, approved, or authoritative. Proposed and unresolved material must retain its declared status.

</details>

<details>
<summary>Using instruction files</summary>

### Using instruction files

This repository does not automatically install, activate, inject, or apply instructions to ChatGPT, an account, or a device. Instruction versions and experiments are reference material for deliberate evaluation. Worldbuilding sources have their own project-declared status and should not all be treated as experimental prompts.

If you choose to reuse an instruction file:

1. Read its scope, changelog, and known limitations.
2. Select the specific file you intend to try; do not treat the whole repository as one configuration package.
3. Check the applicable character limits and retain the previous configuration.
4. Keep the model, settings, memory, and test prompts stable when comparing versions.
5. Test both fresh and long-running conversations, and record which behavior was actually observed.

No version is guaranteed to suit every model, product, account, or use case. Copying or adapting instructions remains the reader's responsibility.

</details>

<details>
<summary>Independence and runtime limits</summary>

### Independence and runtime limits

This is a personal project, not an official OpenAI project or a guarantee of ChatGPT behavior.

Documentation does not become an active instruction merely because it exists in Git. What is actually available and applied depends on the live configuration, instruction placement, source access, and conversation context. Repository inspection alone cannot establish that state.

The author decides canon. Tools and models help manage and examine the work; their output does not confer creative authority.

</details>

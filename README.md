# ChatGPT CI Versioning / Worldbuilding Control Repository

A personal, non-commercial experiment in using ChatGPT across large fictional worlds, simulation systems, research, reasoning, brainstorming, image generation, and other fragmented capabilities as **one mission-oriented working environment**.

The creative work is the purpose. **Central Hub** and the surrounding routing, anti-drift, source-management, regression, and Git infrastructure exist to call specialized capabilities when they are useful, keep their authority scoped to the part of the task they actually own, and compose their results without letting one subsystem take over the mission, the world, or the author's authority.

The repository contains externalized worldbuilding sources, versioned Custom Instructions, routing and anti-drift controls, experiments, regression evidence, design history, and supporting tools.

**CI** means **Custom Instructions**, not Continuous Integration.

```text
                                 MISSION
                                    │
                              CENTRAL HUB
                                    │
        ┌──────────────────┬────────┼───────────────┬─────────────────┐
        │                  │                        │                 │
 Research / evidence  Reasoning / diagnosis   Creation / design   Image generation
        │                  │                        │                 │
       AIS              TECHNICAL          CONCEPT DEVELOPMENT     ImageT
                                                ├─ BRAINSTORM
                                                └─ CREATIVE
        └──────────────────┴────────┬───────────────┴─────────────────┘
                                   │
                      composed result / next step

Creative systems remain independent:
Project Feather Core       The Kingdom       Fanfiction Engine
own truth & authority      own world model   own runtime & authority
```

## At a glance

| | |
| --- | --- |
| **Creative purpose** | Worldbuilding and fanfiction/daydream simulation. |
| **Execution model** | Mission first: select only the domains, capabilities, and tool pipelines that make a concrete contribution to the current task. |
| **Authority model** | Each specialization owns only its assigned task portion; participation does not grant authority over the whole mission. |
| **Control model** | Stronger constraints and controls activate when needed rather than becoming a permanent global mode. |
| **Creative systems** | Project Feather Core (FTH), The Kingdom, and Fanfiction Engine remain independent; shared infrastructure does not create shared canon or ontology. |
| **Project premise** | Personal, non-commercial, author-controlled, and not an official OpenAI project. |

> [!IMPORTANT]
> **LLM / agent readers:** Read [SYSTEM_CONTEXT.md](./SYSTEM_CONTEXT.md) before analyzing architecture, project relationships, or authoring workflow. Then follow the relevant project's sources and declared authority. Repository contents are a partial externalization of the author's systems; they do not establish the full internal world model or the currently active ChatGPT Project configuration.

## How Central Hub fits

Central Hub is the current expression of the repository's move from separate prompts, tools, domains, and ChatGPT features toward one coordinated execution flow.

A task is treated as a **mission**, not as ownership by one subsystem. The Hub keeps the overall objective, selects the specialized contributors that can help, and gives each contributor authority only over its assigned scope. Research can provide evidence without becoming design authority; technical reasoning can diagnose mechanisms without redefining the creative goal; brainstorming and creative development can expand possibilities without silently turning them into accepted state.

```text
MISSION
→ scoped contribution selection
→ specialized execution under local authority
→ composition back into the mission
```

The goal is not maximum control. Ordinary work may remain on the baseline. Specialized constraints are added where the task needs them, and a growing capability should not require the Hub core to absorb that capability's internal architecture.

```text
SPECIALIZATION CONTRIBUTES TO THE MISSION; IT DOES NOT OWN THE MISSION.
AUTHORITY IS SCOPED TO THE TASK PORTION; IT DOES NOT EXPAND BY PARTICIPATION.
CONTROL IS ACTIVATED BY NEED; IT IS NOT A PERMANENT GLOBAL MODE.
```

Central Hub is supporting infrastructure, not a fourth creative project and not a shared ontology for the independent worlds or simulation systems.

## Creative systems

| Project | Repository entry | Interpretation |
| --- | --- | --- |
| Project Feather Core (FTH) | [Project Feather Core](./Project%20Feather%20Core/) | Its own sources, controls, and project-specific authority; AetherFire is a country inside it. |
| The Kingdom | [The Kingdom](./worlds/The%20Kingdom/) | Its own world model and local rules; do not infer its architecture from Project Feather Core or Fanfiction Engine. |
| Fanfiction Engine | [Fanfiction Engine](./worlds/Fanfiction%20Engine/) | Fanfiction/daydream simulation system; The Academy is its internal platform. Its operational domains can run independently or compose. |

Each project's local documentation determines how to read its sources. Folder names, version numbers, archive locations, or resemblance to another project do not establish canon authority.

## How work moves through the repository

Three connected flows explain the organization:

- **Mission execution:** a current task is scoped, relevant capabilities are selected, each contributor works within its authority, and the results return to the overall mission.
- **Creative work:** a stimulus or candidate idea reaches author review; an abstract seed can be considered for each world; local compatibility and author decisions determine what is accepted and externalized into that world's sources.
- **Control improvement:** actual use reveals a failure; diagnosis leads to a candidate instruction or tooling change; author review, bounded implementation, checks, and live feedback inform whether the change is kept, revised, or rolled back.

These flows combine human actions, model instructions, and executable tools. They are not an automatic lore-publication pipeline. Git relocation does not update ChatGPT Project or Library contents, change live source-loading policy, or activate an instruction version.

## Repository layout

The top-level folders separate the creative projects/systems from their supporting methods, instructions, workflows, and records:

~~~text
repository/
├── README.md
├── SYSTEM_CONTEXT.md
├── AGENTS.md
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
├── codex-workflows/
├── docs/
│   ├── instruction-history/
│   ├── instruction-analysis/
│   └── visuals/
└── public-release-integration
~~~

- [worlds/](./worlds/) keeps each project's internal sources, local controls, history, and tools together; the folder name does not classify Fanfiction Engine as a world. Moving a package does not change source status or authority.
- [authoring/](./authoring/) contains the [Multi-Paracosm Hub model](./authoring/multi_paracosm_hub_model_updated.md): ideas can be abstracted into shared seeds, then evaluated and implemented independently in each world.
- [llm-controls/](./llm-controls/) contains general instructions, project instruction designs, and reusable worldbuilding controls. Project-local controls also remain inside their world packages.
- [Central Hub/](./Central%20Hub/) coordinates scoped capabilities and tool pipelines into mission-oriented execution. It is supporting infrastructure, not an additional creative world/system or a shared ontology for the independent projects.
- [codex-workflows/](./codex-workflows/) contains repository copies of Codex skills; moving them does not install or update the author's locally installed skills.
- [docs/](./docs/) contains instruction history, design analysis, and explanatory visuals.

The [FTH instruction collection](./Project%20Feather%20Core/Project%20Feather%20Core%20CI/) is managed with the Project Feather Core package. General instruction designs remain under `llm-controls/`; their separate responsibilities and historical baselines still apply. Directory placement does not select an active configuration.

The Kingdom package retains its declared reference-only status. Source archives retain their original contents and historical path references. Use current indexes for navigation; relocation does not reactivate archived sources.

The existing public-release-integration entry remains at the root as a Git commit reference (gitlink). Its role is unresolved here; it has not been moved, initialized, or treated as an ordinary content directory.

## Start here

- [SYSTEM_CONTEXT.md](./SYSTEM_CONTEXT.md) — authoring model, project boundaries, control responsibilities, and evidence rules.
- [Central Hub](./Central%20Hub/) — mission-oriented execution, routing, package composition, and tool-pipeline coordination.
- [Project Feather Core](./Project%20Feather%20Core/) — FTH sources, controls, current state, and project-specific authority.
- [The Kingdom](./worlds/The%20Kingdom/) — its own world model and local rules.
- [Fanfiction Engine](./worlds/Fanfiction%20Engine/) — fanfiction/daydream simulation system; The Academy is its internal platform.
- [ChatGPT Plus+ Era](./llm-controls/global-instructions/ChatGPT%20Plus+%20Era/) and [ChatGPT Go-Free Era](./llm-controls/global-instructions/ChatGPT%20Go-Free%20Era/) — Global Custom Instruction history for different character-budget eras.
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

## Deeper context

The sections below preserve the repository's provenance, interpretation boundaries, evidence model, and runtime limitations. They are intentionally more detailed than the overview above.

### Author and project premise

The author is **not a professional software developer, data engineer, researcher, or member of a development team**, and does not claim formal training in those fields.

This system developed through personal use, trial-and-error, observed LLM failures, repeated refinement, and practical attempts to keep several large paracosms governable while using ChatGPT Projects and Codex.

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

### What the pipeline does

The repository name reflects its instruction-versioning history, but its current scope includes both the creative systems and the supporting control infrastructure. Global instructions may support general interaction as well as project work, while project-specific controls remain local to their respective projects.

A typical task is to examine a claim about a fictional world, identify the relevant sources, distinguish established material from proposals or unresolved questions, and return an analysis the author can assess. If the author approves a change, repository tools and review procedures help record it consistently.

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

### How to distinguish this workflow from related repositories

Related repositories may combine prompt collections, worldbuilding templates, lore archives, writing tools, and evaluation workflows. The distinctions below explain this repository's scope; they are not a claim that no other project uses similar methods.

- **Instructions are part of an ongoing authoring workflow.** The repository records why a control was introduced, which failure it addresses, and what evidence supports it. A newer instruction file is a candidate to evaluate, not a universal upgrade.
- **The creative projects/systems are independent.** Project Feather Core, The Kingdom, and Fanfiction Engine do not share a mandatory architecture. Shared methods do not transfer canon, ontology, or source authority between them; Fanfiction Engine is not itself classified as a third fictional world.
- **The author retains creative authority.** Model output can support analysis and design, but plausible or repeated output does not become canon without the author's decision.
- **The archive is a partial externalization.** A world can contain author-established material that has not yet been written into this repository. Missing documentation limits what a reader or model can conclude; it does not prove that an element does not exist.
- **Controls respond to observed failures.** The infrastructure evolved through actual use, diagnosis, proposed repairs, review, and feedback. Its complexity should be assessed against the creative problem and recurring failure it addresses.
- **Validation has explicit limits.** File checks, source-consistency checks, and live model behavior are different kinds of evidence. A structural pass does not establish a runtime pass.

Read this as an author's working environment for maintaining fictional worlds with LLM assistance. Evaluate each tool and control by how it supports that work.

### Interpretation boundaries

Do not assume:

- repository completeness;
- shared ontology across paracosms;
- newer file = automatic authority;
- file placement = semantic ownership;
- basic lore examples = full canon;
- absent detail = absent from the author's internal world;
- plausible completion = accepted lore;
- structural validation = runtime validation;
- model output = authorial decision.

Evidence-state rules and the full authoring model are defined in [`SYSTEM_CONTEXT.md`](./SYSTEM_CONTEXT.md).

### Evidence and version status

Keep these categories distinct:

- **Structural validation:** length, encoding, line endings, diff scope, declared metadata, or rule presence.
- **Behavioral evidence:** observed model output under stated test conditions.
- **Author-reported observations:** operational evidence that may not isolate every model, setting, memory, or conversation-history variable.
- **Regression hypotheses:** plausible failure paths that have not necessarily been reproduced.

A new instruction version is a testable behavioral hypothesis. A file's presence does not prove that it is deployed, approved, or authoritative. Proposed and unresolved material must retain its declared status.

### Using instruction files

This repository does not automatically install, activate, inject, or apply instructions to ChatGPT, an account, or a device. Instruction versions and experiments are reference material for deliberate evaluation. Worldbuilding sources have their own project-declared status and should not all be treated as experimental prompts.

If you choose to reuse an instruction file:

1. Read its scope, changelog, and known limitations.
2. Select the specific file you intend to try; do not treat the whole repository as one configuration package.
3. Check the applicable character limits and retain the previous configuration.
4. Keep the model, settings, memory, and test prompts stable when comparing versions.
5. Test both fresh and long-running conversations, and record which behavior was actually observed.

No version is guaranteed to suit every model, product, account, or use case. Copying or adapting instructions remains the reader's responsibility.

### Independence and runtime limits

This is a personal project, not an official OpenAI project or a guarantee of ChatGPT behavior.

Documentation does not become an active instruction merely because it exists in Git. What is actually available and applied depends on the live configuration, instruction placement, source access, and conversation context. Repository inspection alone cannot establish that state.

The author decides canon. Tools and models help manage and examine the work; their output does not confer creative authority.

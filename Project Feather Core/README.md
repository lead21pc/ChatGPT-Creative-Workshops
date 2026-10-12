# Project Feather Core

Project Feather Core (`FTH`) is a worldbuilding project and setting namespace. AetherFire remains the name of a country inside the setting. Its sources describe the fictional world; its instructions, routers, overlays, and checks help the author and language models work with those sources without silently changing their meaning.

```text
PROJECT FEATHER CORE / FTH
!=
AETHERFIRE THE COUNTRY
```

Read the repository's [system context](../SYSTEM_CONTEXT.md) first, then the [current source index](00_AETHERFIRE_CONSOLIDATION_INDEX.md). This README is a navigation guide. It does not establish canon, select a control version, or resolve an open issue.

## Where to read and work

| Location | Role |
| --- | --- |
| [00_AETHERFIRE_CONSOLIDATION_INDEX.md](00_AETHERFIRE_CONSOLIDATION_INDEX.md) | Entry point for current sources and their declared authority. |
| Numbered current-source files at the root | Maintained worldbuilding sources. Follow the index for the relevant topic and scope. |
| [90_DESIGN_HISTORY_AND_RECONSIDERATIONS.md](90_DESIGN_HISTORY_AND_RECONSIDERATIONS.md) | Historical appendix; consult its declared status rather than treating history as current canon. |
| [91_RECONCILIATION_RECORD.md](91_RECONCILIATION_RECORD.md) | Reconciliation decisions and their evidence. |
| [92_OPEN_ISSUES_CURRENT.md](92_OPEN_ISSUES_CURRENT.md) | Unresolved questions and explicitly retained uncertainty. |
| [MANIFEST.md](MANIFEST.md) | Package structure and maintenance metadata. |
| [Project Feather Core CI/](Project%20Feather%20Core%20CI/) | Custom Instructions and historical instruction comparisons. |
| [Anti-Drift Source/](Anti-Drift%20Source/) | Source routing and task-scoped anti-drift overlays, with their own control archive. |
| [Source_Archive/](Source_Archive/) | Preserved source provenance and history. Presence here does not grant current canon authority. |
| [tests/](tests/) | Package maintenance checks and local control regression tooling. |
| [tools/legacy/](tools/legacy/) | Legacy maintenance tools; use the current Python entry point below. |

Current sources remain at the project root because package maintenance validates their filenames and direct location. They are maintained source documents, not disposable build output. Source archives are excluded from the current package's build inputs.

## How the project works

Start with the source index, select the relevant current documents, and distinguish established canon from proposals, conflicts, history, and unknowns. Record an author's accepted reconciliation in the appropriate current source and decision record. Retain unresolved states in the open-issues register.

Controls guide this work but do not supply missing lore or turn a proposal into canon. A source router determines applicable source authority and overlay scope; a Custom Instructions file governs behavior. Keep those roles separate when reading or changing either collection.

The active local stack is [FTH CI 3.3](Project%20Feather%20Core%20CI/FTH_CI_version_v3.3.md), [FTH Router 5.0](Anti-Drift%20Source/FTH_Anti_Drift_Source_Router_v5.0.yaml), and [Authoring Pipeline 1.1](Anti-Drift%20Source/FTH_Authoring_Pipeline_v1.1.md). Direct-child numeric version resolution selects these versions; CI 3.2, Router 4.4 and Pipeline 1.0 remain unchanged rollback snapshots. CI owns entry, Router owns routing, and Pipeline owns transformation. Promotion was authorized after user-reported stable runtime usage; repository checks do not independently establish that behavior or prove live installation.

Directory organization in Git does not relocate a live Project's files or change its configured Library folder. Publishing repository changes is separate from installing controls and validating live model behavior.

## Maintenance and verification

Run the read-only package check from this directory:

~~~powershell
python -B build_consolidation.py --check
~~~

The Python maintenance tool manages declared generated regions and checks package consistency. Its companion PowerShell entry point remains at the root. Neither tool independently accepts canon or rewrites unresolved decisions.

See [control regression instructions](tests/control-regressions/README.md) for local inspection. These checks distinguish draft cases, source anchors, structural results, and execution limits. Passing repository checks does not establish live ChatGPT behavior.

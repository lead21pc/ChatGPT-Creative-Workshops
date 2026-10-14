# AetherFire — Target Directory Layout

> **Status:** proposed soft-refactor target.  
> **Canon effect:** NONE.  
> **Constraint:** preserve current working package until catalog/path updates can be reviewed atomically.

## 1. Recommended target

```text
AetherFire Project/
├─ 00_AETHERFIRE_CONSOLIDATION_INDEX.md
├─ 90_DESIGN_HISTORY_AND_RECONSIDERATIONS.md
├─ 91_RECONCILIATION_RECORD.md
├─ 92_OPEN_ISSUES_CURRENT.md
│
├─ Current/
│  ├─ World_Polity/
│  │  ├─ 10_WORLD_INSTITUTIONS_GEOPOLITICS_CURRENT.md
│  │  ├─ 70_MATRIARCHS_LAMENT_CURRENT.md
│  │  └─ ...
│  │
│  ├─ Status_Social/
│  │  ├─ 20_STATUS_CIVIL_LABOR_CURRENT.md
│  │  └─ 30_UNDIE_SYSTEM_CURRENT.md
│  │
│  ├─ Meta_Narrative/
│  │  ├─ 40_METAFICTION_CANON_TIMELINE_CURRENT.md
│  │  ├─ 50_NARRATORS_POV_AND_HUMOR_CURRENT.md
│  │  └─ 60_MC4_IDENTITY_CURRENT.md
│  │
│  ├─ Shared_Interfaces/
│  │  └─ <future admitted shared-interface modules>
│  │
│  ├─ Polity_Implementations/
│  │  └─ <future admitted polity-specific implementations>
│  │
│  ├─ Specialized_Capabilities/
│  │  ├─ 80_STABLE_AVIATION_RF_AIRSPACE_CURRENT.md
│  │  └─ <future admitted capability owners>
│  │
│  └─ Lost_Historical/
│     └─ <only confirmed lost/historical current modules>
│
├─ Working/
│  ├─ Proposals/
│  ├─ Migration/
│  ├─ Samples/
│  └─ Scratch/
│
├─ Controls/
│  ├─ Source_Router/
│  └─ Anti_Drift/
│
└─ Source_Archive/
```

## 2. Transitional rule

The current index states that canon outputs live at project root. Therefore Codex should **not** immediately move existing source files merely to match this layout.

Soft migration sequence:

```text
1. Introduce templates / working directories.
2. Build or update a reviewed module catalog in 00.
3. Prepare path changes as one patch.
4. Verify every Module ID and authority boundary.
5. Update all explicit path references.
6. Run broken-reference / duplicate-ID audit.
7. Only then relocate admitted current files.
```

If path migration is not worth the churn, keep current sources at root and use this tree only as a **logical classification model**.

## 3. Runtime exclusion

These directories must not be treated as current lore sources:

```text
Working/
Templates/
Samples/
Migration/
Scratch/
```

The package catalog should either exclude them explicitly or mark them as non-runtime navigation material.

## 4. Important invariant

```text
DIRECTORY GROUPING != MODULE OWNERSHIP
MODULE OWNERSHIP != IN-WORLD OWNERSHIP
```

The tree is for human and tooling navigation only.

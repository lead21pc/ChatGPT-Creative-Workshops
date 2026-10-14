# AetherFire Source Structure Pack v1

> **Status:** STRUCTURE / MIGRATION TOOLING ONLY  
> **Canon effect:** NONE by file presence.  
> **Purpose:** provide a standard source layout, header contract, module templates, non-runtime examples, and a soft-refactor handoff for Codex.  
> **Authority rule:** this pack does not admit a module, assign a real Module ID, resolve an UNKNOWN, or canonize a The Kingdom concept.

## 1. Basis

This pack follows the active AetherFire Source Router v4.0 contract:

- `Module ID`
- `Runtime role`
- `Domain / Scope`
- `Authority boundary`
- `Cross-domain owner boundary` when a known interface crosses owners
- `Load mode`

The Router treats headers as routing metadata, not self-granted canon authority.

The pack also applies the approved migration principles:

```text
COMMON REQUIREMENT
SHARED INTERFACE
POLITY IMPLEMENTATION
SPECIALIZED CAPABILITY
LOST / HISTORICAL CANDIDATE
METHOD / CONTROL
```

and:

```text
INTERACTION != OWNERSHIP
SHARED FUNCTION != SHARED IMPLEMENTATION
COMPATIBILITY != COMMON ORIGIN
SHARED SEED != SHARED IMPLEMENTATION
```

## 2. Contents

```text
AetherFire_Source_Structure_Pack_v1/
├─ README.md
├─ SOURCE_STRUCTURE_STANDARD.md
├─ DIRECTORY_LAYOUT_TARGET.md
├─ MODULE_ADMISSION_CHECKLIST.md
├─ CODEX_SOFT_REFACTOR_HANDOFF.md
├─ Templates/
│  ├─ TEMPLATE_CURRENT_SOURCE.md
│  ├─ TEMPLATE_SHARED_INTERFACE_CURRENT.md
│  ├─ TEMPLATE_POLITY_IMPLEMENTATION_CURRENT.md
│  ├─ TEMPLATE_SPECIALIZED_CAPABILITY_CURRENT.md
│  ├─ TEMPLATE_LOST_HISTORICAL_CURRENT.md
│  └─ TEMPLATE_WORKING_PROPOSAL.md
├─ Samples/
│  ├─ SAMPLE_SHARED_INTERFACE_CONTACT_VERIFICATION.md
│  ├─ SAMPLE_POLITY_IMPLEMENTATION_AF_CIVIC_TERMINAL.md
│  └─ SAMPLE_LOST_CIVILIZATION_MODULE.md
└─ Migration/
   ├─ THE_KINGDOM_MIGRATION_WORKSHEET.md
   └─ SAMPLE_THE_KINGDOM_DMZ_DECOMPOSITION.md
```

## 3. Safety rule for Codex

Do not move existing current files merely to make the tree prettier.

Physical relocation, filename changes, real Module ID assignment, `CURRENT_SOURCE` admission, and updates to `00_AETHERFIRE_CONSOLIDATION_INDEX.md` should be performed as one reviewed package change.

`Samples/`, `Templates/`, and `Migration/` are not lore sources and must not be added to the runtime source catalog.

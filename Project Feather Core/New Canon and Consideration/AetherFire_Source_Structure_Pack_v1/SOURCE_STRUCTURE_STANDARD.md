# AetherFire — Source Structure Standard

> **Document role:** architecture standard / non-canon control aid.  
> **Applies to:** future source creation, The Kingdom migration, module extraction, and soft refactors.  
> **Does not:** admit modules, assign canon, or override the active Router / CI.

## 1. Primary design rule

A source module exists because a bounded set of facts needs a controlling owner.

Do **not** create a module merely because several facts share a theme, technology label, actor name, or filename history.

```text
MODULE = AUTHORITY BOUNDARY
NOT = TAXONOMY BUCKET
```

A current module may represent:

- polity;
- institution;
- actor;
- region;
- shared interstate interface;
- specialized capability;
- subsystem;
- confirmed lost/historical source domain.

## 2. Mandatory runtime header

For an admitted current-source module:

```md
# <Title>

> Module ID: `<AFM-...>`
> Runtime role: `CURRENT_SOURCE`
> Domain / Scope: <discovery boundary>
> Authority boundary: <facts this module controls, plus material non-claims>
> Cross-domain owner boundary: <other owners whose facts must not be absorbed>
> Load mode: `FULL_FILE`
```

### Rules

- `Module ID` must be unique and reviewed. Do not invent it inside a draft.
- `Runtime role` does not grant authority by itself.
- `Domain / Scope` is a discovery boundary, not proof of full containment.
- `Authority boundary` must say what the module **does not** control when confusion is plausible.
- `Cross-domain owner boundary` is required when a known interface crosses controlling owners.
- Default `Load mode` is `FULL_FILE`.
- Use `NODE_OR_FULL` only after a reviewed local routing index and dependency closure exist.
- Add hard `MODULE_REQUIRES` only when a dependency is genuinely indispensable for a stated task class and has been reviewed. Do not infer it from co-occurrence.

## 3. Recommended body structure

```md
## 0. Source contract
- current status and scope;
- explicit exclusions;
- terminology boundary;
- relation to other owners.

## 1. Current accepted baseline
Only accepted current facts controlled by this module.

## 2. Core domain facts
The actual subsystem / actor / interface content.

## 3. Interfaces
For each cross-owner interface:
- established interaction;
- local owner;
- external owner;
- information / authority / resource crossing;
- what is not implied.

## 4. State and transitions
Only when the domain has meaningful state changes.

## 5. UNKNOWN / DEFERRED / CONFLICTED
Preserve unresolved implementation and authority.

## 6. Explicit non-claims
Prevent common reverse inferences and scope drift.

## 7. Supersession / provenance
Only enough to identify what was replaced or inherited.
Genealogy never becomes current authority by itself.
```

Sections can be omitted when irrelevant. Do not add empty bureaucracy.

## 4. Module families

### 4.1. World / polity owner

Controls a polity, institution, actor, or broad geopolitical domain.

It may summarize a shared interface but should not duplicate detailed implementation controlled elsewhere.

### 4.2. Shared interface owner

Controls an interaction contract between multiple owners.

Examples:

- controlled interstate contact;
- cross-border verification;
- mixed airspace coordination;
- standardized handoff;
- treaty-defined interoperability.

Invariant:

```text
INTERFACE OWNER
controls interaction contract

INTERFACE OWNER
does not automatically control either endpoint's internal implementation
```

### 4.3. Polity-specific implementation owner

Controls how one polity implements a function.

It must not imply:

```text
LOCAL IMPLEMENTATION
→ monopoly
→ foreign absence
→ foreign inferiority
→ shared origin
```

unless another controlling source explicitly establishes those claims.

### 4.4. Specialized capability owner

Use when one capability becomes deep enough that the broad world/polity owner should retain only the interface.

Typical triggers:

- distinct economic consequences;
- distinct operational doctrine;
- independent authority/interface boundaries;
- enough detail that full-file loading of a broad world file becomes wasteful or unstable.

### 4.5. Lost / historical owner

Use only after the entity, remains, or historical capability is actually accepted into canon.

It controls confirmed historical facts and surviving remains.

It must not infer:

```text
modern use
= understanding

compatibility
= inheritance

custody
= origin

reverse engineering
= common ancestry
```

### 4.6. Working proposal

A working proposal is **not a runtime module**.

It should use a non-runtime header such as:

```md
> Working status: `PROPOSAL / NOT ADMITTED`
> Proposed owner type: ...
> Proposed scope: ...
> Canon effect: NONE until explicit acceptance and source admission.
```

Do not add `Runtime role: CURRENT_SOURCE` or a real Module ID before admission.

## 5. Shared-function decomposition

When migrating legacy material:

```text
LEGACY IMPLEMENTATION
↓
WHAT PROBLEM DOES IT SOLVE?
↓
COMMON REQUIREMENT?
↓
SHARED INTERFACE?
↓
POLITY-SPECIFIC IMPLEMENTATION?
↓
SPECIALIZED CAPABILITY?
↓
ABOVE CURRENT POWER CEILING?
    yes → lost/historical candidate
    no  → keep in current-world design path
↓
METHOD / CONTROL ONLY?
```

The migration unit is the **function / relation / requirement**, not the legacy file.

## 6. Cross-owner interface record

Recommended compact pattern:

```md
### Interface: <A> ↔ <B>

**Established interaction**
- ...

**Controlled here**
- ...

**Controlled elsewhere**
- `<Module ID / path>`: ...

**Does not establish**
- containment;
- hierarchy;
- dependency unless stated;
- shared implementation;
- shared origin;
- common policy across a multi-polar actor.
```

## 7. Truth-state discipline

Use labels when material:

- `CANON`
- `UNKNOWN`
- `DEFERRED`
- `CONFLICTED`
- `UNCONFIRMED`
- `HISTORICAL / SUPERSEDED`
- `INFERENCE`
- `HYPOTHETICAL`
- `PROPOSAL`

```text
NOT FOUND != FALSE
NOT ESTABLISHED != FALSE
COMPATIBLE != CANON
REPEATED != ACCEPTED
```

## 8. Naming rules

Prefer names based on institutional function or authority domain.

Prefer:

```text
INTERSTATE_CONTACT_AND_VERIFICATION_CURRENT.md
COUNTERINTELLIGENCE_AND_INFORMATION_SECURITY_CURRENT.md
AF_CIVIC_SERVICE_INTERFACE_CURRENT.md
```

Avoid taxonomy-only names such as:

```text
BORDER_TECH_CURRENT.md
MAGICAL_TECH_MISC.md
FOREIGN_TECHNOLOGY_CURRENT.md
```

A numeric filename prefix is optional. Module identity comes from reviewed Module ID and package/catalog admission, not filename numbering.

## 9. Physical structure rule

Logical ownership matters more than directory nesting.

A directory tree is navigation only:

```text
PATH != AUTHORITY
DIRECTORY CONTAINMENT != LORE CONTAINMENT
```

Do not infer hierarchy from folders.

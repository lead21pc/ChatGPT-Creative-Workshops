# SAMPLE ONLY — AetherFire Civic Terminal Implementation

> **Sample status:** `NON-CANON / NON-RUNTIME / DO NOT ADMIT`
> **Purpose:** show how a polity-specific implementation can reuse a common requirement without claiming monopoly.
> **Important:** functionality below is illustrative migration structure, not accepted current canon.

---

## Example target header after a future reviewed admission

```md
# AetherFire — Civic Terminal & Personal Service Interface Current Canon

> Module ID: `<AFM-XXX>`
> Runtime role: `CURRENT_SOURCE`
> Domain / Scope: AetherFire's personal civic/service terminal implementation, including authenticated identity interface, service access, navigation, payment interface, communication access, and local magic-technology interoperability where explicitly established.
> Authority boundary: Controls AetherFire's implementation within scope. Does not establish technological monopoly, foreign absence, foreign inferiority, shared origin, or equivalent implementation elsewhere.
> Cross-domain owner boundary: Legal status and civic eligibility remain controlled by their status/legal owners; national communications and information-security doctrine remain controlled by their own owners; foreign equivalents remain outside this module.
> Load mode: `FULL_FILE`
```

## Example body

### 1. Function

The implementation answers a general requirement:

```text
PERSON
needs authenticated access to
identity + communication + navigation + services + payments + permissions
```

That requirement is not uniquely AetherFire.

### 2. Local implementation principle

AetherFire's differentiator may be the way it integrates magical and technological subsystems into one stable service layer.

This does **not** imply that AetherFire invented every component.

### 3. Boundary

```text
AF IMPLEMENTATION
!= UNIVERSAL STANDARD

AF IMPLEMENTATION
!= PROOF RF / ML / HN LACK EQUIVALENTS

COMPATIBILITY WITH AF INFRASTRUCTURE
!= COMMON ORIGIN
```

### 4. Items that would still require separate canon decisions

- exact device form;
- power source;
- whether physical hardware is mandatory;
- identity authority;
- payment architecture;
- foreign roaming/interoperability;
- security model;
- access matrix by legal status;
- offline capability;
- surveillance / privacy constraints.

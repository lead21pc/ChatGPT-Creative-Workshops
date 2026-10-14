# AetherFire — Module Admission Checklist

> **Purpose:** review gate before a proposal becomes an admitted runtime module.  
> **Canon effect:** none by itself.

## A. Identity

- [ ] Is there a real need for a separate authority owner?
- [ ] Is the proposed Module ID unique in the reviewed package?
- [ ] Is the title stable enough to survive path renames?
- [ ] Is the runtime role recognized and appropriate?

## B. Scope

- [ ] Does `Domain / Scope` describe discovery scope without claiming complete world coverage?
- [ ] Does `Authority boundary` state what this module controls?
- [ ] Does it state material non-claims?
- [ ] If the module crosses an owner boundary, is `Cross-domain owner boundary` explicit?

## C. Canon status

- [ ] Which claims are already accepted current canon?
- [ ] Which are new and explicitly accepted in this admission?
- [ ] Which remain `UNKNOWN / DEFERRED / CONFLICTED / PROPOSAL`?
- [ ] Is any legacy material being restored accidentally?
- [ ] Does genealogy remain provenance rather than current authority?

## D. Dependencies

- [ ] Does the module genuinely require another owner for a task class?
- [ ] If yes, is `MODULE_REQUIRES` reviewed rather than inferred?
- [ ] Are there hidden owner overlaps?
- [ ] Does any multi-polar actor get collapsed into a unitary policy by accident?

## E. Interfaces

For every shared actor/system:

- [ ] interaction identified;
- [ ] local facts separated from external facts;
- [ ] authority separated from capability;
- [ ] access separated from ownership;
- [ ] dependency separated from co-occurrence;
- [ ] shared function separated from shared implementation;
- [ ] compatibility separated from common origin.

## F. Load mode

- [ ] Default is `FULL_FILE`.
- [ ] If `NODE_OR_FULL` is requested, has the local routing index been reviewed?
- [ ] Are node boundaries and decisive `NODE_REQUIRES` complete?
- [ ] Is full-file fallback defined?

## G. Package integration

- [ ] Update `00_AETHERFIRE_CONSOLIDATION_INDEX.md`.
- [ ] Update current module catalog if present.
- [ ] Update `92_OPEN_ISSUES_CURRENT.md` only if open-state routing actually changes.
- [ ] Update `91_RECONCILIATION_RECORD.md` when admission resolves/supersedes/conflicts with prior material.
- [ ] Update explicit path references.
- [ ] Verify no duplicate Module ID.
- [ ] Verify no working/sample/template file was admitted accidentally.

## H. Final anti-drift check

```text
HEADER VALID
!= CANON ADMITTED

PATH MATCH
!= SOURCE READ

INTERACTION
!= OWNERSHIP

POWER
!= AUTHORITY

GENEALOGY
!= HIERARCHY

COMPATIBILITY
!= COMMON ORIGIN
```

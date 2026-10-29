# Revamp Project System — Failure Entry Modes

STATUS: REFERENCE
SCOPE: Revamp Project System only.
ROLE: Comparison reference for identifying how a failure enters Revamp work, especially mid-task Case 1.5.
NOT: Failure-severity scale, root-cause diagnosis, mandatory workflow, recovery state machine, Router, CURRENT handoff, or replacement for the active CI.

```text
ENTRY MODE != FAILURE CAUSE
ENTRY MODE != FAILURE SEVERITY
REFERENCE != AUTHORIZATION
```

---

## 1. Purpose

Revamp can encounter the same underlying failure through different operating situations. The entry mode matters because it changes what should be preserved, what evidence is available, and whether the primary task still needs to continue before root-cause debugging.

Use this file to compare a reported failure against Cases 1, 2, and 1.5 before choosing how to proceed. Do not infer the failure's cause merely from the matching case.

---

## 2. Case 1 — Runtime first, Revamp after failure

Typical sequence:

```text
real project/runtime work
→ failure, drift, or overreach occurs
→ the affected trajectory is stopped or set aside
→ the failure and its context are brought into Revamp
→ Revamp diagnoses against the real evidence
```

The primary advantage is that Revamp sees a naturally occurring failure with its real conversational or runtime context. The cost is that the failure may already have consumed substantial work or distorted later context before diagnosis begins.

Default comparison posture:

- preserve the failed trajectory as evidence;
- inspect what actually failed rather than reconstructing it from a generic pattern;
- do not assume the whole prior conversation or project state is invalid merely because one path failed;
- diagnose before redesigning.

Case 1 is appropriate when the failure itself has become the current task and the original work can remain suspended while Revamp investigates it.

---

## 3. Case 2 — Revamp first, runtime after design

Typical sequence:

```text
problem or suspected gap is identified
→ Revamp inspects the current system
→ Revamp proposes the smallest sufficient correction
→ repository/runtime review challenges the proposal
→ the correction is tested in real use afterward
```

The primary advantage is low retry cost and strong scope control before a live trajectory is exposed to the proposed change. The limitation is that static inspection may not reproduce the actual runtime context that makes the failure appear.

Default comparison posture:

- distinguish static support from live evidence;
- do not treat a structurally plausible fix as runtime-verified;
- test the smallest viable correction before adding more machinery;
- preserve the working baseline until the replacement behavior is established.

Case 2 is appropriate when the system can be inspected and corrected before the relevant behavior must run live.

---

## 4. Case 1.5 — Failure during an active primary task

Typical sequence:

```text
primary task is actively running
→ a material premise, reasoning path, or execution path becomes invalid
→ the primary task still matters and may be costly or unsafe to abandon
→ failure handling competes with task continuity
```

This is not merely Case 1 with a smaller number. Its distinguishing condition is that the original task is still active when the failure occurs. Stopping everything for root-cause debugging may itself impose more cost than restoring a safe path for the primary task.

A common form is conversational inertia after correction: a premise is corrected, but later reasoning continues to depend on the stale premise. The PSU discussion that led to the current §2 control is a user-reported example of this shape; it established the operating problem, not a reproduced technical root cause.

Current Revamp CI already supplies the governing rule:

```text
FAILURE DETECTION != DEBUG AUTHORIZATION
```

For comparison purposes, Case 1.5 should be read as:

```text
invalid premise materially affects a path
→ stop relying on that path
→ retain the path as evidence
→ determine whether sufficient valid current state remains
→ if safe, resume the primary task from that state
→ otherwise flag the blocker
→ debug root cause now only when the current task requires or requests it
```

Do not automatically:

- restart the entire conversation;
- quarantine all earlier material;
- salvage every part of the failed trajectory;
- declare all prior information false;
- force root-cause debugging before the primary task can continue;
- continue through a safety blocker merely to preserve momentum.

A small corrected error that does not invalidate the current path is not enough by itself to trigger Case 1.5 recovery behavior.

---

## 5. Comparison

| Question | Case 1 | Case 2 | Case 1.5 |
| --- | --- | --- | --- |
| Has relevant runtime behavior already occurred? | Yes | Not necessarily; correction may precede the relevant live test | Yes, and the primary task is still active |
| What enters Revamp? | A failed or suspect trajectory | A problem/gap before live validation of the correction | A failure interrupting ongoing primary work |
| Main advantage | Rich real failure evidence | Cheap, controlled iteration | Can preserve the primary task without making debugging mandatory |
| Main risk | Failure/context may already have propagated | Static design may miss runtime behavior | Continuing on stale premises or, conversely, abandoning useful work unnecessarily |
| Default Revamp posture | Diagnose the observed trajectory | Design minimally, then test | Isolate the invalidated path; resume safely if possible |
| Is root-cause debugging automatically the next task? | Often the failure is already the task, but still depends on the request | No | No |

---

## 6. Use as a failure comparison reference

When a recurring failure is brought to Revamp, compare it in this order:

1. Which entry mode best describes the situation now: Case 1, Case 2, or Case 1.5?
2. What is directly observed or user-reported, and what remains inference?
3. Which premise or path is actually invalidated, if any?
4. Is the original primary task still active and worth preserving?
5. Is there sufficient valid current state to continue safely?
6. Is root-cause debugging the current requested task, or can it remain separate?

Then apply the active CI's evidence classification independently: OBSERVED FAILURE, REPRODUCED FAILURE, SUPPORTED RISK, or HYPOTHETICAL FUTURE RISK.

```text
ENTRY MODE != EVIDENCE STATUS
CASE 1.5 != PROOF OF ROOT CAUSE
FAILURE DETECTION != GLOBAL INVALIDATION
```

---

## 7. Boundaries

- These cases classify the operating situation around a failure, not the technical cause of the failure.
- A single incident can move between cases as the task changes. Classify the current operating situation rather than forcing the whole history into one label.
- Case 1.5 does not require a new chat, checkpoint, registry, trust score, recovery lifecycle, or persistent incident state.
- This file does not modify the active CI, Router, handoff selection, implementation authority, or Central Hub behavior.
- Use the smallest response that restores correct operation; investigate further only when the task or evidence requires it.

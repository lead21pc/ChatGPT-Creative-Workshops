# Revamp — Aggregate Architecture Preflight

STATUS: REFERENCE / CONDITIONAL PREFLIGHT
SCOPE: Revamp structural proposals, under the operation, delivery and authorization already established by the skill core.
OWNER: Conditional specialization of the skill core for minimum sufficient change, total complexity and structural self-check; no independent authority.

## Activation

Use only when the actual current proposal, downstream artifact or implementation change materially creates or changes structural execution surfaces or boundaries. Examples include execution language, runtime family, package manager, persistent process/service, cross-runtime/process boundary, state or authority ownership, provider/host adapter boundary and execution topology. These describe the failure class, not a mandatory ontology or exhaustive checklist.

Do not activate from the word architecture, explanation of an existing design, non-changing examples/hypotheticals or independent work without a structural proposal. Apply the skill core after identifying the requested operation and inspecting materially required current sources. Direct architecture work stays direct work; preparation of an architecture transfer stays bounded authoring and does not execute the target. No persistent activation or execution graph. This reference replaces no core, authoring, target-inspection or continuity responsibility and grants no authority to install controls in another target.

## One aggregate pass

LOCAL MINIMUM != SYSTEM MINIMUM.

A small component can add a permanent language, runtime, package manager, process/service or cross-runtime boundary. Assess that as a system-level complexity change. Component benefit alone does not justify its boundary: a better TypeScript UI does not itself establish a need for a Python-to-TypeScript boundary.

Identify the structural surfaces/boundaries actually proposed, then review the whole proposal once. For each added boundary establish:

1. Which current failure or authorized requirement requires it?
2. What permanent operating surface does it add?
3. Which new failure modes does it introduce?
4. What additional verification becomes necessary?
5. Could the current execution stack solve the original problem sufficiently with a smaller correction?

Then inspect total permanent complexity, including cumulative runtimes/toolchains, packaging, process coordination, state/authority ownership and integration verification costs where material. Several locally reasonable additions must still justify the combined operating burden against a sufficient same-stack alternative. Heterogeneous stacks are valid when the demonstrated need warrants them; impose no language quota or technology allow-list.

Return the smallest sufficient correction, remove an unnecessary component, retain a material OPEN question or name a concrete blocker for this proposal; then STOP. Preserve settled decisions except the affected part with a concrete blocker. A finding does not authorize wider implementation or permanent governance. Do not loop component risk into new controls, then controls into meta-controls. CONTROL COMPLEXITY IS STILL COMPLEXITY.

## Changes during implementation

LOCAL IMPLEMENTATION FRICTION != PERMISSION TO INTRODUCE A NEW EXECUTION STACK.

A new language/runtime/package manager during implementation is a structural change even if the local patch is small. Before continuing that substitution, reassess the changed proposal with the same aggregate pass and existing authorization/scope rules. Do not silently switch a component to another stack. A reproduced current-stack blocker and unsuccessful smaller corrections can justify a stack change within authorized scope; this is not a universal stack freeze. Review again only for a material proposal change or new evidence, not recursive component-by-component gating.

## Verification boundary

COMPONENT A PASS + COMPONENT B PASS != A↔B BOUNDARY PASS.

A proposed cross-runtime/process boundary needs verification of its actual interaction and failure behavior, not just its endpoints. Name the necessary integration checks and evidence still missing; a prepared harness is not proof that they ran. Keep STATIC PASS != LIVE BEHAVIOR PROVEN and LIVE HARNESS PASS != REAL-CONTEXT ROBUSTNESS PROVEN. Preserve scoped prior results and attribution; do not reset evidence merely because it has not been freshly reproduced. Apply existing evidence controls, without a new verification framework.

This preflight creates no registry, schema, validator, scoring system, lifecycle, policy engine or governance artifact. It guides a bounded proposal review and does not mandate a report template.

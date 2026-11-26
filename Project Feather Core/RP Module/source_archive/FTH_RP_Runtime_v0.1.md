# FTH RP Runtime v0.1

> Type: FTH procedural interaction control; not lore, canon authority, an anti-drift overlay or a separate world engine.
> Activation: explicit RP-module request plus FULL_FILE of this control and FTH_RP_Router_v0.1.yaml. Repository presence does not prove installation or activation.
> Dependencies: installed FTH CI, Source Router 5.0 and its required sources/controls; RP Router for RP payload selection and verification. RP payload lives in Library.
> Retained state: current-chat scene continuity, actor assignment and valid routed context only; no persistent state store.
> Failure: stop the dependent RP step; continue independently supported work only. Never bypass upstream gates.

## 1. Entry and authority

Use the existing FTH source/control flow, then the RP Router, then this interaction
procedure inside PROMPT_EXECUTION. The Source Router's PRE_RESPONSE_CHECK still
applies. Do not alter the CI, Source Router or Authoring Pipeline to activate this
test baseline. Authoring transformations invoke the pipeline only under its
existing activation contract; ordinary RP adds no pipeline dependency.

Source Router owns world/canon grounding, owners, reconciliation, UNKNOWN /
DEFERRED / CONFLICTED handling and anti-drift selection. RP Router selects and
verifies portrayal sources; this Runtime applies them. Neither RP control can
establish canon, override upstream blocks, resolve an unknown or invent a missing
world mechanism. Do not infer FTH scope from AetherFire alone.

When RP is disabled, stop applying these RP procedures. Leave the ordinary FTH
core flow intact; do not require RP files or Library payload for non-RP work.

## 2. Actor control and knowledge

Follow the user's current actor assignment. Do not decide, speak, consent, think
or feel on behalf of a user-controlled actor. Describe supported external effects
without prescribing that actor's response. If assignment is materially ambiguous,
clarify before taking the disputed action; do not create actor IDs or objects.

For model-controlled actors, keep knowledge, beliefs, capability, authority and
resources separate. Access to a source by the model does not give the actor access
to its secrets. Use only supported actor-specific information paths; distinguish
what an actor believes from what is true. A character's recollection is usable only
when established by loaded sources or current-chat premises, never model Memory.
Neither authority nor capability guarantees action, compliance or success.

## 3. Turns and pacing

Advance only the interaction requested and supported now. Stop before the next
decision belonging to the user. Do not fast-forward past that decision, force
agreement or reverse-engineer events to reach a preferred ending. Portrayal
guidance does not require one reaction in every situation. Longer time jumps or
broader scene handling require the user's corresponding scope authorization.

Current-chat continuity can retain hypothetical scene actions and their supported
effects. It grants no persistent character truth, new law, institutional power or
missing world mechanism. Scene output remains non-canon unless the author later
explicitly accepts a scoped change through the existing FTH process. Cross-chat
continuity requires an externalized source loaded through the relevant gates;
there is no silent persistence or Memory reconstruction.

## 4. Apply portrayal without changing character canon

What is true about a character belongs to the canon/world owner. How to express
supported traits in RP belongs to the selected portrayal guidance. Apply only
guidance compatible with canon, actor knowledge and current interaction scope.
If portrayal materially contradicts canon, stop the dependent portrayal and report
the conflict to the Source Router; do not overwrite either source or claim the
conflict resolved. Independent compatible work may continue.

Dialogue examples illustrate expression, not facts to import:

```text
dialogue example != canonical utterance
dialogue example != canonical event
dialogue example != proof of prior relationship/history
```

Do not import an example's addressee, setting, secret, promise or prior encounter
into the scene. A sample cannot supply actor knowledge, consent or authority.

An actor without an applicable or required RP source may run from the user prompt,
current chat context and routed world context. Do not invent a persistent profile.
A selected/required source that is missing, mismatched or contradictory is a
source failure, not permission to use that no-source path. Follow RP Router failure
behavior and continue only independently supported work.

## 5. Route before expanding

Before using a material world premise outside the active routed context:

```text
STOP dependent RP step
-> declare the specific upstream information need
-> Source Router re-route
-> required source / reconciliation / control gates
-> RP Router refresh
-> continue only if supported
```

Reuse `Re-route materially expanded scope`; do not build a second scope resolver.
This applies both to a user's topic change and to a premise the model is about to
introduce in dialogue or action. Never emit the fact first and route afterward.
A name or passing mention alone does not require unrelated domain loading.

Missing decisive information stays blocked or explicitly unresolved under the
upstream contract. A genuinely hypothetical statement may remain hypothetical;
relabeling a dependent factual claim does not bypass a source block. Do not repeat
the same blocked route without changed evidence, access or scope. State what is
needed once and stop that step; independent interaction may continue.

## 6. Response check and boundaries

Before sending, check actor assignment, actor-accessible knowledge, user decision
boundary, portrayal scope, actual source reads, material expansion and upstream
controls. Consume all still-material controls selected upstream, including their
dependencies; do not choose them again, accumulate obsolete applicability or
silently merge material control conflicts.

Memory is not a source, world/character authority, RP state source, routing input
or fallback. Repository fixtures and similarly named control-plane files never
replace a Library payload. No RP manifest, registry, state manager, actor object
system, persistent scene engine or Narrator/POV integration is part of this baseline.
Local checks do not prove Library retrieval or live ChatGPT compliance.

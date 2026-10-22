# Multi-Paracosm Hub Workflow

## 1. Core Model

Real-world stimuli can trigger curiosity and become an abstract **seed**.

The hub does **not** route the seed to only one paracosm. It forks the same primitive across all three paracosms, then each branch evaluates the seed independently according to its own ontology, invariants, architecture, and current state.

```text
IRL stimulus
    ↓
curiosity trigger
    ↓
abstract seed
    ↓
HUB
    ├─ fork → Fanfiction Engine
    ├─ fork → The Kingdom
    └─ fork → Project Feather Core
```

**Invariant:**

> Shared seed ≠ shared implementation.

The seed may be common, but each paracosm independently determines whether it can exist there and what local form it must take.

---

## 2. Per-Paracosm Compatibility Check

For each forked branch:

### 1. Compatible

The seed fits the local ontology and invariants.

```text
compatible
→ integrate
```

### 2. Incompatible

The seed cannot exist coherently in the local system.

```text
incompatible
→ drop
```

Do not force an idea into a paracosm merely to preserve symmetry across all three.

### 3. Partially Compatible

Do not reject immediately.

#### 3a. Partial Salvage

Extract only the compatible substructure.

```text
seed
→ isolate compatible component
→ integrate that component
→ discard the remainder
```

#### 3b. Local Reinterpretation

Transform the seed so that it fits the local ontology without violating local invariants.

```text
seed
→ reinterpret locally
→ compatibility check again

coherent
→ integrate

still incoherent
→ drop
```

The 3a/3b step exists to reduce false negatives: potentially useful ideas should not be discarded only because their first implementation does not fit.

---

## 3. Cascade

Integration can generate new local consequences.

If a consequence has potential outside its source paracosm:

```text
local consequence
→ abstract into a new seed
→ return to HUB
→ fork again
```

A consequence must return to the hub as a **new abstraction**.

Do not copy the source branch's implementation, ontology, state, or assumptions directly into another paracosm.

---

## 4. Anti-Drift Constraints

### Fork the seed, not the implementation

If The Academy turns `institution` into a Narrative Engine, that does not make `Narrative Engine` part of the original seed.

The Kingdom and Project Feather Core still receive only the abstract `institution` primitive.

### Local ontology has priority

Similarity or analogy is insufficient.

If an idea conflicts with local invariants:

```text
reject
OR
reinterpret
```

Never override the local architecture merely because the idea worked elsewhere.

### Partial acceptance is exact

For 3a:

```text
accepted substructure = retained
rejected remainder = not canonized
```

Do not silently restore discarded properties later.

### Cascade creates a new seed

Cross-paracosm propagation must pass through abstraction again.

```text
Branch A result
≠ direct import into Branch B

Branch A result
→ abstract new seed
→ Hub
→ Branch B compatibility check
```

### No requirement for three successful branches

A seed may be:

```text
accepted by 3
accepted by 2
accepted by 1
accepted by 0
```

All are valid outcomes.

---

## 5. Modularization by Paracosm

The three creative projects/systems are modular, but they modularize different things; Fanfiction Engine is a simulation engine whose internal platform is The Academy.

### Fanfiction Engine

**Modularization target:** Narrative Engines and causal mechanisms.

A module can carry its own:

- causal identity;
- invariants;
- actors;
- pressures;
- interfaces;
- state transitions.

Modules such as Greed, Sloth, Wrath, and Chaos Engine can operate independently or compose with other modules without becoming permanently dependent on them.

---

### The Kingdom

**Modularization target:** autonomous background processes and checkpoint-driven narrative state.

Between checkpoints, multiple processes can run without requiring one linear narrative chain.

```text
Checkpoint A
    ↓
autonomous background activities
    ↓
interactions / adaptation / state change
    ↓
Checkpoint B
```

Modules may interact, remain independent, or reintegrate changed state later.

---

### Project Feather Core

**Modularization target:** sufficiently complex factions or state apparatuses.

Each major institution can possess enough:

- authority;
- personnel;
- assets;
- procedures;
- interests;
- internal conflicts;
- external relationships;

to sustain fiction independently.

Examples include a civil administration or economic ministry capable of generating its own drama without requiring a central lore thread.

Global lore advances primarily through:

```text
checkpoints
+
fixed events
```

---

## 6. Operational Summary

```text
IRL stimulus
→ curiosity
→ abstract seed
→ HUB
→ fork across A / B / C

FOR EACH PARACOSM:

    exact fit
        → integrate

    no fit
        → drop

    partial fit
        → 3a extract compatible substructure
        OR
        → 3b reinterpret locally

        if coherent
            → integrate
        else
            → drop

AFTER INTEGRATION:

    derive local consequences

    if consequence has cross-domain potential
        → abstract into NEW seed
        → return to HUB
        → fork again
```

---

## 7. Fundamental Invariants

```text
SHARED SEED ≠ SHARED IMPLEMENTATION

FORK SEED, NOT IMPLEMENTATION

LOCAL ONTOLOGY > CROSS-PARACOSM ANALOGY

PARTIAL ACCEPTANCE ≠ WHOLE-SEED ACCEPTANCE

CASCADE MUST RE-ABSTRACT BEFORE CROSSING DOMAINS

A SEED DOES NOT NEED TO FIT ALL THREE PARACOSMS

MODULARITY IS SHARED;
THE MODULARIZATION TARGET IS NOT
```

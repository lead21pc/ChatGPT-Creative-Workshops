# Project Verification Philosophy

## Scope

This file defines a shared verification philosophy for project-system work across the project. It is not specific to Central Hub, AIS, Revamp, FTH, FSP, ImageT, or any single stack.

## Core invariant

> STATIC PASS proves the contract. LIVE HARNESS PASS proves the prepared path. REAL-CONTEXT STRESS proves the system survives actual conversational state.

## Interpretation

- **STATIC PASS** shows that the encoded rules, schemas, routing contracts, or tests are internally consistent under the tested conditions.
- **LIVE HARNESS PASS** shows that a prepared execution path can work in a controlled live setup.
- **REAL-CONTEXT STRESS** shows whether the system still behaves correctly inside an actual conversation with accumulated context, prior routing decisions, ambiguity, task transitions, and conversational inertia.

These evidence levels are complementary, not interchangeable.

## Evidence boundary

`STATIC PASS != LIVE BEHAVIOR PROVEN`

`LIVE HARNESS PASS != REAL-CONTEXT ROBUSTNESS PROVEN`

`PASSING TESTS != TESTED THE RIGHT THING`

A lower-level PASS must not be promoted into a stronger verification claim without corresponding evidence.

## Operational consequence

Use the lightest verification level sufficient for the change, but when behavior depends on conversational state, routing transitions, context carryover, tool execution, or authority boundaries, preserve at least one real-context stress check before treating the behavior as robust.

Do not add process merely to maximize test count. Verification should target concrete failure modes and evidence gaps.

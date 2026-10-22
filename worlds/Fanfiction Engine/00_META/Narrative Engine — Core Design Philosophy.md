# Narrative Engine — Core Design Philosophy

This site documents a **Narrative Engine system**. It is not primarily a worldbuilding website, lore archive, fiction showcase, or conventional writing challenge.

The system should be understood as a **fiction-level narrative framework composed of reusable engines**.

## Core Principle

A Narrative Engine is independent from any specific fiction.

It does not require its own fixed world, characters, setting, magic system, history, or lore.

Instead, the user selects a **Host Fiction** and applies the engine to that fiction.

The Host Fiction may be:

- an existing fictional work;
- a fan-created setting;
- or an entirely original fiction created by the user.

The Narrative Engine remains structurally independent from all of them.

## Meta Engine

The **Meta Engine** sits above all Narrative Engines.

Its role is to define the governing philosophy, principles, and constraints under which the Narrative Engines are understood and applied.

The Meta Engine must be processed first.

Narrative Engines are selected only after the Meta Engine has established the governing framework.

The hierarchy is:

**Meta Engine → Narrative Engine Selection → Engine Application**

Narrative Engines are optional and selectable.

The Meta Engine is the governing layer.

## Narrative Engines

Each **Narrative Engine** is a reusable narrative mechanism.

An engine defines its own:

- operating principles;
- invariants;
- internal mechanisms;
- conditions;
- pressures;
- transformations;
- doctrines;
- tools;
- interactions;
- and possible narrative consequences.

An engine must not be treated as a self-contained fiction.

Its purpose is to be **applied to another fiction**.

Different Narrative Engines do not need to share the same internal structure. Their architecture should follow the mechanism each engine requires rather than being forced into one universal template.

## Host Fiction

The **Host Fiction** is the fictional environment in which a selected Narrative Engine is applied.

The engine does not replace the Host Fiction.

It operates through it.

The Host Fiction provides the local reality in which the engine must function.

This distinction is fundamental:

**The fiction does not belong to the engine.  
The engine is applied to the fiction.**

## World Bible

The **World Bible** provides the operational theory of the Host Fiction.

Lore is therefore not merely background information.

World rules, metaphysics, ontology, magic systems, technologies, institutions, history, social systems, character constraints, and other established facts define what is possible inside that Host Fiction.

The Narrative Engine must use those rules when realizing itself locally.

It should not automatically import an external world model when the Host Fiction already provides one.

The World Bible therefore acts as a constraint and translation layer between the abstract Narrative Engine and its concrete implementation.

## Target Subject

The user chooses what the Narrative Engine acts upon.

The **Target Subject** may be a character, group, institution, relationship, social structure, situation, or another context supported by the engine.

The engine itself does not permanently own a protagonist or fixed target.

The target belongs to the selected application.

## Engine Application

An **Engine Application** combines:

**Selected Narrative Engine + Host Fiction + World Bible + Target Subject + User-defined Context**

This produces one concrete implementation of the engine.

The same Narrative Engine can therefore produce radically different realizations when applied to different Host Fictions or different targets.

The identity of the engine should remain recognizable through its invariants, while its manifestation should adapt to the local rules of the Host Fiction.

## Local Realization

A **Local Realization** is the form a Narrative Engine takes after being interpreted through the rules of a specific Host Fiction.

The engine provides the abstract mechanism.

The Host Fiction provides the local laws.

The World Bible constrains what implementation is valid.

Therefore:

**Narrative Engine × Host Rules → Local Realization**

A Local Realization is not a modification of the engine's fundamental identity. It is the engine expressed through a different fictional environment.

## Narrative Instance

The final story is a **Narrative Instance**, not the engine itself.

A Narrative Instance is produced by one particular configuration and application of the system.

Different users may select the same engine but create completely different stories because they may choose different:

- Host Fictions;
- World Bibles;
- Target Subjects;
- contexts;
- combinations of Narrative Engines;
- and writing decisions.

The engine provides a system of narrative possibilities and constraints rather than a predetermined story.

## Relationship to Writing Challenges

The system may resemble a writing challenge because users receive a framework and then create their own fiction from it.

However, it operates at a much larger structural level.

Instead of providing a prompt, trope, scenario, or fixed premise, the system provides a **reusable narrative toolset**.

Users choose which tools to activate, where to apply them, and how to realize them through the rules of their chosen fiction.

The result should therefore be understood as a **fiction-level writing engine**, not a collection of writing prompts.

## Relationship to Fanfiction

The system can function as a fanfiction engine, but it is not restricted to fanfiction.

Existing fiction can serve as the Host Fiction.

Original fiction can serve exactly the same role.

The architecture intentionally makes no fundamental distinction between them.

If an original fiction has a sufficiently defined World Bible, it is a valid Host Fiction.

The reusable engine exists outside both.

## Site Design Principle

This website should present the system as **technical documentation for a modular narrative architecture**.

Do not default to the visual or informational conventions of conventional worldbuilding websites, lore encyclopedias, fictional universes, character galleries, or promotional fiction sites.

The interface should prioritize:

- system hierarchy;
- operational flow;
- module relationships;
- engine selection;
- definitions;
- dependencies;
- conditions;
- inputs and outputs;
- process visualization;
- cross-references;
- and technical readability.

Lore should appear when it explains how a Host Fiction operates, not merely because lore exists.

Characters should appear when they are relevant as targets, examples, or implementation contexts, not automatically as the center of the information architecture.

The primary question of the site is not:

**“What world does this describe?”**

It is:

**“How does this system operate, what can be selected, and how can it be applied to a fiction?”**

## Interpretation Rule

Treat the definitions and relationships documented in this site as authoritative for this system.

Do not reinterpret terms according to common worldbuilding, fiction-writing, game-design, or software-engineering conventions when this site defines them differently.

When information is missing:

- presentation gaps may be solved through design judgment;
- semantic or architectural gaps must not be silently invented.

Preserve the distinction between **system design**, **Host Fiction**, and **the story produced by an application of the system**.
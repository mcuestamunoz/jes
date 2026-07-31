# JES — Architecture

> This document describes how the JARVIS Engineering System is structured.  
> Architecture defines layers, responsibilities, and dependency rules.  
> Decisions here are traceable to `01_PRINCIPLES.md`.

---

## What architecture means in JES

This is not software architecture for projects built with JES.

It is the architecture of the engineering system itself:

- what components exist,
- what each is responsible for,
- what can depend on what,
- where boundaries are.

---

## Layer model

JES runs in five layers. Dependencies flow only top-down.

```text
Engineer (Authority)
    |
    v
JES Core (Methodology)
    |
    v
Engineering Operations (Method-level work units)
    |
    v
Integration Layer (Tool adapters)
    |
    v
Tools (Execution environments)
```

Dependency rule: higher layers must not depend on lower layers.

---

## Layer 1 — Engineer

Source of technical authority.

Responsibilities:
- strategic direction,
- architectural approval,
- cycle validation,
- methodology stewardship.

---

## Layer 2 — JES Core

Defines governance and methodology artifacts:

- `SYSTEM_DEFINITION.md`
- `01_PRINCIPLES.md`
- `02_ARCHITECTURE.md`
- `02.5_ENGINEERING_COGNITION.md`
- `02.6_ENGINEERING_STATE.md`
- `02.7_ENGINEERING_STATE_LIFECYCLE.md`
- `03_WORKFLOW.md`
- `04_ROLES.md`
- `05_RULES.md`
- `07_ECOSYSTEM.md`
- `08_ENGINEERING_OPERATIONS.md`
- `09_OPERATION_SELECTION.md`

Within Core methodology, conceptual order is:

```text
Principles
    ->
Architecture
    ->
Engineering Cognition
    ->
Engineering State
    ->
State Lifecycle
    ->
Workflow
    ->
Operations
    ->
Operation Selection
```

Engineering Cognition explains how the engineer navigates intentions.  
Engineering State carries the live cycle instance (`current_mode`, status, triggers).  
State Lifecycle defines how that instance is created, evolved, persisted, and ended.  
Workflow explains when work is complete.  
Operations define executable units that materialize that movement.  
Operation Selection chooses the next coherent available operation without inventing work.

See `02.5_ENGINEERING_COGNITION.md`, `02.6_ENGINEERING_STATE.md`, `02.7_ENGINEERING_STATE_LIFECYCLE.md`, and `09_OPERATION_SELECTION.md`.

---

## Layer 3 — Engineering Operations

Defines tool-agnostic units of engineering work (e.g., Research, Analyze, Plan, Implement, Review).

Document: `08_ENGINEERING_OPERATIONS.md`.

Purpose:
- materialize cognitive movement into executable units,
- provide shared operation semantics across integrations.

---

## Layer 4 — Integration Layer

Integrations are adapters translating JES into specific tool capabilities.

They may:
- define operational rules in tool-compatible format,
- map operations to prompts/commands,
- provide context loading behavior.

They may not:
- redefine JES principles/rules/workflow,
- become source of truth,
- alter authority flow.

---

## Layer 5 — Tools

Editors, LLM platforms, version control, CI/CD, and runtime tools.

Tools are replaceable execution environments and do not define JES.

---

## Information flow

Downward (context):

```text
Repository -> Integration -> Tool agent execution
```

Upward (artifacts):

```text
Tool output -> Engineer validation -> Repository integration
```

No artifact becomes system truth without explicit engineer approval.

---

## Belonging criterion for Core vs integration

> If a concept would still matter after every AI tool disappears, it belongs to JES Core.  
> If it only makes sense because a specific tool exists, it belongs to that tool’s integration.

Use this criterion before adding documents, components, or abstractions.

Examples:

- Engineering Cognition → Core
- Engineering State → Core
- Operation Selection → Core
- Cursor HUD rendering details → integration
- Cursor prompt syntax → integration

---

## Core dependency rules

| Rule | Principle |
|---|---|
| Lower layers cannot modify higher layers | P1 |
| Tools cannot define methodology | P6 |
| Agents require explicit context | P7 |
| Relevant knowledge must live in repository | P3 |
| Architectural changes require engineer approval | P1 |
| Complexity growth must be justified | P9 |

---

## Evolution

Architecture can evolve, but each change must:

1. trace to at least one JES principle,
2. be explicitly approved by the engineer,
3. avoid contradicting existing principles.

---

*Version: 2026.2 — Updated: July 2026*

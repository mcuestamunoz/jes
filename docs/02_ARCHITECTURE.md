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
- `03_WORKFLOW.md`
- `04_ROLES.md`
- `05_RULES.md`
- `07_ECOSYSTEM.md`

---

## Layer 3 — Engineering Operations

Defines tool-agnostic units of engineering work (e.g., Research, Analyze, Plan, Implement, Review).

Document: `08_ENGINEERING_OPERATIONS.md`.

Purpose:
- bridge intent and workflow execution,
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

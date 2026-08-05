# JES — System Definition

> This is the most important document in the JARVIS Engineering System.  
> Everything else (architecture, workflows, rules, automations) must derive from it.  
> If something does not fit here, it does not belong to JES.
>
> This document defines **what JES is**. `docs/01_PRINCIPLES.md` defines **how JES reasons**. Together they form the root layer of the system.

---

## 1. What JES is

The JARVIS Engineering System (JES) is an engineering system designed to organize, coordinate, and govern the development of complex projects through structured collaboration between an engineer and multiple AI agents.

> **JES is an engineering system validated by incremental implementation.**

JARVIS is the main project developed under JES, but not the only one.

It is not a set of tools.  
It is not a theoretical methodology.  
It is not passive documentation.

JES does not develop software.

JES develops the way software is developed.

It is a system with active responsibilities that governs how decisions are made, how work is coordinated between the engineer and AI agents, and how project knowledge is preserved over time.

JES exists because building complex systems with AI as a collaborator requires more than good intentions. It requires structure — and that structure must survive contact with real Operations and real tools.

---

## 2. Problems JES solves

| Problem | How JES solves it |
|---|---|
| Decisions are made without record or justification | Documents and versions every architectural decision |
| Context is lost between sessions | Defines explicit context rules for agents |
| AI assumes authority it should not have | Establishes clear boundaries between delegation and decision authority |
| Knowledge remains in private conversations | Requires that important knowledge lives in the repository |
| Quality depends on the engineer’s current state | Defines reproducible processes independent of mood/state |
| Tools condition architecture | Separates methodology from implementation |

---

## 3. Responsibilities

JES exists to:

- Organize engineering
- Preserve context
- Coordinate AI agents
- Preserve knowledge
- Automate repetitive tasks
- Guarantee quality
- Keep the engineer as final authority
- Support informed engineering decisions

---

## 4. Boundaries

JES must never:

- Make autonomous strategic decisions
- Modify architecture without explicit engineer approval
- Merge, deploy, or execute irreversible changes automatically
- Hide decisions or reasoning
- Generate important knowledge that is not documented in the repository
- Bind software architecture to a specific tool
- Grow in complexity without clear value
- Replace engineer judgment

---

## 5. Principles

These principles govern all decisions inside JES.

**P0 — Engineering First**  
JES exists to improve engineering, not to demonstrate AI capabilities.

**P1 — Human Authority**  
Technical authority is never delegated. Agents can propose, implement, analyze, and review. Final decisions always belong to the engineer.

**P2 — AI as Collaborator**  
Implementation can be delegated. Design authority cannot.

**P3 — Repository First**  
All relevant knowledge lives in the repository.

**P4 — Documentation as Engineering**  
Documentation is part of the system, not post-work.

**P5 — Deterministic Engineering**  
Every change must be reproducible, verifiable, and traceable.

**P6 — Replaceable Tools**  
Tools are replaceable. System architecture must never depend on one vendor/tool.

**P7 — Context over Memory**  
Agents work from explicit context. They must not rely on conversation memory.

**P8 — Continuous Validation**  
No implementation is complete without validation.

**P9 — Simplicity by Default**  
Every added component increases complexity and must justify its value.

---

## 6. Belonging criterion

Before adding anything to JES, ask:

> **Does it fulfill at least one responsibility defined in section 3?**

If yes, it belongs.  
If no, it does not.

---

## 7. Relationship with JARVIS

JES and JARVIS are separate systems with a one-way relationship:

```text
JES (Engineering System)
        |
        | develops
        v
JARVIS (Software Product)
```

JARVIS references JES in its documentation, but there is no technical dependency.

JES can exist without JARVIS. JARVIS can be developed without JES. Together, they form a strong engineering environment for complex projects.

---

## 8. Workflow under JES

```text
JES Core
  |
  +-- Knowledge
  +-- Workflows
  +-- Rules
  +-- Engineering Operations
           |
           v
    Integration Layer
           |
           v
      Tool Runtime
           |
           v
     Implementation
```

Tools are replaceable execution environments. No specific tool is required by JES.

*Version: 2026.2 — Updated: July 2026*

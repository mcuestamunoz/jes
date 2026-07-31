# JES — Engineering Operations

> This document defines the engineering operations recognized by JES.  
> An operation is not a tool command. It is a methodology-level unit of work.

---

## What an engineering operation is

An operation answers:

> *What kind of engineering work is being executed in this cycle?*

Operations provide a stable interface between:
- JES workflow/rules,
- integration operating models,
- tool-specific implementations.

---

## Architectural placement

Operations belong to JES core, not to any specific integration.

```text
JES Core
  |
  +-- Principles
  +-- Rules
  +-- Workflow
  +-- Engineering Operations
           |
           v
     Integration Layer
           |
           v
       Tool Runtime
```

---

## Operation set (v1)

- Research
- Analyze
- Plan
- Implement
- Review
- Validate
- Document
- Explain
- Refactor

---

## Operation definitions

### Research
Gather and structure context before solution decisions.

### Analyze
Evaluate scope, constraints, risks, and alternatives.

### Plan
Transform approved direction into verifiable execution tasks.

### Implement
Execute approved plan within defined scope.

### Review
Assess quality, correctness, and architectural consistency.

### Validate
Verify technical and workflow acceptance criteria.

### Document
Update repository truth to match approved system state.

### Explain
Communicate rationale, behavior, and impact clearly.

### Refactor
Improve internal structure while preserving intended behavior.

---

## Operation selection

Between intent and execution, operation selection is required:

```text
Intent
  ->
Operation Selection
  ->
Engineering Operation
  ->
Execution
```

Operation Selection is a Core contract (`09_OPERATION_SELECTION.md`).  
It chooses among operations declared available by the current integration.  
It evaluates the complete Engineering State, not only mode.  
It never invents work.

---

## Workflow and artifact relation

Operations do not replace workflow.

- Workflow defines phases, roles, and closure.
- Operation defines work type.

Final artifacts are determined by:

**workflow + operation**

not by tool preference.

---

## Integration implementation rules

Each integration must define:
1. how each operation is triggered,
2. what prompt(s) implement it,
3. what artifact bundle is expected.

Operation-to-prompt mapping may be 1:1 or 1:N.

---

## Governance and evolution

- No operation may violate JES principles.
- Operations must respect engineer authority gates.
- Operation set changes require explicit engineer approval.
- New operations require demonstrated cross-context value.

---

*Version: 2026.2 — Updated: July 2026*

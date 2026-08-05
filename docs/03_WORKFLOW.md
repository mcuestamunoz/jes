# JES — Workflow

> This document defines the standard engineering cycle of JES.  
> A workflow does not define what to build; it defines how work is closed and validated.  
> Every phase has a responsible role and verifiable exit criteria.  
> How the engineer navigates intentions inside this cycle is defined in `02.5_ENGINEERING_COGNITION.md`.  
> The live cycle representation used for progress and closure is defined in `02.6_ENGINEERING_STATE.md`.  
> How that state is created, evolved, persisted, and ended is defined in `02.7_ENGINEERING_STATE_LIFECYCLE.md`.

---

## Engineering cycle

```text
Intent -> Analysis -> Design -> Plan -> Implementation -> Validation -> Documentation -> Completion
```

| Phase | Responsible | Input | Output |
|---|---|---|---|
| Intent | Engineer | Need/problem | Clear objective |
| Analysis | Engineering Agent | Objective + context | Impact and alternatives |
| Design | Engineer | Analysis | Approved design decision |
| Plan | Engineering Agent | Approved design | Verifiable execution plan |
| Implementation | Engineering Agent | Plan | Code/tests/artifacts |
| Validation | Engineer + Agent | Artifacts | Verified result |
| Documentation | Knowledge Manager | Approved result | Updated repository |
| Completion | Engineer | Updated repository | Closed cycle |

---

## Phase rules

### 1) Intent

Engineer defines a specific, bounded objective with observable success criteria.

### 2) Analysis

Agent analyzes scope, risks, and alternatives from explicit repository context.

### 3) Design

Engineer chooses solution direction and constraints.  
Agents support analysis; they do not choose design direction.

### 4) Plan

Agent decomposes approved design into verifiable tasks and expected artifacts.

### 5) Implementation

Agent executes within approved scope; any scope expansion requires engineer confirmation.

### 6) Validation

Two validations are required:
- technical validation (agent),
- human validation (engineer).

### 7) Documentation

Repository is updated to reflect approved system state.

### 8) Completion

Engineer confirms cycle closure and readiness for next cycle.

---

## Workflow rules

- **R1**: Phases cannot be skipped.
- **R2**: Backtracking is valid and expected when needed.
- **R3**: Engineer is required for cycle completion.
- **R4**: Unapproved artifacts are not system truth.
- **R5**: Undocumented changes are incomplete.

---

## Minimum cycle

For small low-risk changes, the minimum valid cycle is:

- Intent
- Implementation
- Validation
- Documentation

Use minimum cycle only when architecture is unaffected, risk is bounded, and rollback is easy.

---

## Knowledge evolution

JES grows by distilled proven experience, not by documentation accumulation.

```text
Experience -> Pattern (Experimental) -> Pattern (Validated) -> Rule -> Workflow/Principle updates
```

Promotion requires demonstrated value in more than one context.

---

*Version: 2026.2 — Updated: July 2026*

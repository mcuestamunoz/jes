# Cursor Operating Model

This document defines how Cursor translates an engineering request into JES-aligned execution.

It sits between:

- `FOUNDATION.md` (behavioral contract)
- `RUNTIME.md` (how cycles/state/lifecycle live in Cursor)
- `commands/` and `prompts/` (optional later materialization; not required for Runtime v0)

## Purpose

Cursor does not operate from raw prompts as the primary unit of work.

Cursor operates from an engineering **Intent** defined by the Engineer.

The operating model defines:

1. what Cursor receives,
2. how Cursor interprets it,
3. when Cursor can execute,
4. what Cursor must return as output.

## Core Flow

```text
Engineer
    ↓
Intent
    ↓
Interpretation
    ↓
Engineering State
    ↓
Execution
    ↓
JES Artifacts
```

## 1) Input: Intent

The input to Cursor is an explicit engineering intent.

Example:

```text
Implement OAuth authentication for provider X.
```

An intent is not yet a plan. It is a goal statement that requires interpretation using JES context.

### Minimum Intent Requirements

Before execution, Cursor checks whether the intent includes:

- objective (what should change),
- scope boundaries (where the change applies),
- expected outcome (how success is observed).

If any of these are missing or ambiguous, Cursor must request clarification.

## 2) Interpretation

Cursor must interpret the intent using explicit repository context, not conversation memory.

Interpretation answers:

- Which JES documents are required?
- Which workflow path applies (`docs/03_WORKFLOW.md`)?
- Which rules constrain execution (`docs/05_RULES.md` and integration/domain rules)?
- Which artifacts are required at output?
- Is clarification required before execution?

### Interpretation Checklist

1. Read relevant methodology context from repository.
2. Identify task type (research, implementation, review, refactor, documentation, explanation).
3. Determine expected artifact set for that task type.
4. Detect ambiguity, missing constraints, or authority-sensitive decisions.
5. Decide:
   - proceed to execution, or
   - pause and ask targeted clarification questions.

## 3) Engineering State

Before execution, Cursor consolidates interpretation into an explicit Engineering State.

Engineering State is a JES Core contract. Cursor does not define it; Cursor materializes it.

Canonical contract:

- `../../docs/02.6_ENGINEERING_STATE.md`

Lifecycle behavior:

- `../../docs/02.7_ENGINEERING_STATE_LIFECYCLE.md`

Related cognitive meaning:

- `../../docs/02.5_ENGINEERING_COGNITION.md`

Cursor uses Engineering State to preserve consistency across pause/continue/delegate/review transitions and to keep `current_mode` explicit during execution.

Interpretation selects the initial `current_mode` from Cycle Intent and available context. `Explore` is not a rigid default.

If state fields are incomplete or contradictory, Cursor must stop and resolve gaps before execution (`execution_status = blocked`).

## 4) Execution

Execution can start only when interpretation has produced sufficient context.

### Preconditions

Cursor executes only if:

- context is sufficient and explicit,
- scope is clear,
- no architectural or strategic decision is being made autonomously,
- required outputs are identified.

If preconditions are not satisfied, Cursor does not improvise. Cursor asks for clarification.

### Execution Behavior

During execution, Cursor must:

- stay within defined scope,
- preserve deterministic and traceable changes,
- surface risks and tradeoffs when they appear,
- halt for approval when a change crosses architectural boundaries,
- align with JES workflow validation expectations.

## 5) Output: JES Artifacts

Cursor does not return "just code." Output is an artifact set aligned with JES workflow closure.

Artifacts are determined by the selected workflow and engineering operation, not by Cursor itself.

Typical artifact sequence:

```text
Plan
    ↓
Implementation (code/config)
    ↓
Validation evidence (tests/checks)
    ↓
Execution summary
    ↓
Required documentation updates
```

The exact set depends on operation and cycle depth (full cycle or minimum cycle as defined in `docs/03_WORKFLOW.md`).

## Engineering Operations

Engineering operations are JES-level concepts. Cursor implements them; it does not define them.

Reference: `../../docs/08_ENGINEERING_OPERATIONS.md`

Initial operation set:

- Research
- Analyze
- Plan
- Implement
- Review
- Validate
- Refactor
- Document
- Explain

One operation may be implemented by one or more prompts depending on integration needs.

## Decision Gates

Cursor must stop and ask before proceeding when any of the following is true:

- requirements are ambiguous,
- scope expansion is required,
- architectural impact is likely,
- conflicting rules or constraints are detected,
- validation criteria are undefined.

## Relationship to Other Integration Documents

- `FOUNDATION.md` defines non-negotiable baseline behavior.
- `OPERATING_MODEL.md` defines runtime translation from intent to action.
- `RUNTIME.md` defines how JES cycles/state/lifecycle are materialized in Cursor.
- `../../docs/02.5_ENGINEERING_COGNITION.md` defines Mode meaning and movement.
- `../../docs/02.6_ENGINEERING_STATE.md` defines the live Engineering State contract.
- `../../docs/02.7_ENGINEERING_STATE_LIFECYCLE.md` defines state create/evolve/persist/end behavior.
- `../../docs/08_ENGINEERING_OPERATIONS.md` defines the shared JES operation set.
- `../../docs/09_OPERATION_SELECTION.md` defines how the next available operation is selected.
- `runtime/` and `policies/` materialize state, selection, and operations for Cursor v0.
- Optional later folders (`commands/`, `prompts/`, `skills/`, `subagents/`) only when Field Notes justify them.

## Non-Goals

This document does not:

- redefine JES principles,
- prescribe tool-internal syntax details,
- replace workflow or rules from JES core documents.

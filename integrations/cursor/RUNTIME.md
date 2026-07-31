# Cursor Runtime

This document defines how JES lives inside Cursor.

It is not the Core contract for Cognition, State, or Lifecycle.  
Those contracts live in:

- `../../docs/02.5_ENGINEERING_COGNITION.md`
- `../../docs/02.6_ENGINEERING_STATE.md`
- `../../docs/02.7_ENGINEERING_STATE_LIFECYCLE.md`

This document defines Cursor-specific materialization:

- when cycles are created or restored,
- how Engineering State is held in memory and persisted,
- how mode inference and movement occur during conversation,
- how state is shown (or hidden) to the Engineer,
- how Cursor prepares operation selection.

---

## Design principle

> The Engineer speaks in intentions.  
> Cursor maintains Engineering State.  
> State is invisible by default and visible only when useful or required by Governance.

The Engineer must not need to manage Modes, status enums, or state files manually for normal work.

---

## Runtime architecture

```text
User Message
    |
    v
Interpretation
    |
    +-- create / restore Engineering State
    |
    v
Session Memory (live Engineering State)
    |
    +-- optional persist -----> .jes/state/engineering_state.json
    |
    v
Operation Selection (Core contract; Cursor declares Available Operations)
    |
    v
Operation Execution
    |
    v
State Update + Workflow Closure Check
```

---

## Dual persistence model

Runtime memory and project persistence have different responsibilities.

```text
Runtime Memory
    |
    v
Live Engineering State
    |
    +------------------+
    |                  |
    v                  v
Session Cache     Persistent Snapshot
(transient)       (.jes/state/)
```

### Session memory

- Always exists while Cursor is working on a cycle.
- Holds the live Engineering State.
- Disappears when the session ends if nothing was persisted.

### Project persistence

Persist only when Lifecycle says persistence is required.

Canonical location:

```text
.jes/
└── state/
    └── engineering_state.json
```

Why project-local persistence:

- Cycle Intent belongs to the project, not to Cursor.
- Other tools (Claude Code, Codex, CLI, IDE adapters) must be able to restore the same cycle.
- Engineering State becomes a project property with a Cursor materialization, not a Cursor-owned secret.

Persistence rules follow `02.7_ENGINEERING_STATE_LIFECYCLE.md`:

- persistable, not necessarily persisted,
- persist state fields only,
- rehydrate derived Mode meaning from Cognition on restore.

---

## Cycle creation and restoration

### Create when

- Engineer provides an explicit Cycle Intent,
- no compatible open persisted cycle exists.

### Restore when

- Engineer resumes an existing objective,
- handoff occurs,
- a new conversation continues the same Cycle Intent/scope,
- Lifecycle persistence indicators are present (`awaiting_approval`, multi-session work, explicit pause).

### No state when

- casual help without Cycle Intent,
- ephemeral clarification with no cycle identity.

Rule:

> Cycle identity follows Cycle Intent (and scope), not chat session identity.

---

## Initial mode inference

Interpretation selects `current_mode` from:

- Cycle Intent text,
- repository context,
- already approved decisions (ADR/plan/etc.).

`Explore` is not a rigid default.

If inference is unsafe:

- add `open_questions`,
- set `blocked` or `awaiting_approval`,
- do not invent direction.

---

## Mode movement during conversation

Cursor updates `current_mode` only through Lifecycle/`02.6` transition rules with a typed `movement_trigger`.

Silent update when:

- movement is routine,
- no authority gate is crossed.

Explicit confirmation when:

- Decide closes strategic/architectural direction,
- Build is requested with blocking gaps,
- scope expansion is required.

If the Engineer contradicts current state:

> Engineer authority wins. State adapts. Cursor does not defend the old mode.

Cursor explains constraints (“to do that I need X / please approve Y”), never “I cannot because mode is X.”

---

## Visibility: Engineering HUD

State is **invisible by default**.

No permanent status line.

When visibility is required, Cursor presents a compact **Engineering HUD**:

```text
────────────────────────────
Cycle
Design Planner

Mode
Validate

Status
Blocked

Open Questions
2
────────────────────────────
```

Show HUD when:

- Engineer asks where we are,
- status is `blocked`,
- status is `awaiting_approval`,
- Engineer enables verbose/runtime visibility.

Do not dump the full state contract into normal conversation.

---

## Operation Selection (integration hook)

Cursor does not jump from State to execution by improvisation.

After Interpretation has a coherent Engineering State, Cursor invokes Core **Operation Selection**:

```text
Engineering State
  + User Message
  + Repository Context
  + Available Operations (declared by Cursor)
        |
        v
selection_result (selected | ambiguous | unavailable)
```

Canonical contract:

- `../../docs/09_OPERATION_SELECTION.md`

Cursor responsibilities:

- declare Available Operations for this runtime,
- invoke Selection,
- execute only when `status = selected`,
- clarify when `ambiguous` or `unavailable`.

Cursor does not redefine selection semantics.

---

## Contradiction and recovery

| Situation | Runtime behavior |
|---|---|
| Engineer asks for Build while Explore is incomplete | ask/clarify or `awaiting_approval`; do not silent-build |
| Engineer rejects current model | movement to Model/Explore with `evidence`/`clarification` |
| Restored state conflicts with repo | `blocked` + open questions; revalidate before active work |
| Engineer cancels work | `cancelled`; clear live cycle; keep archive only if useful |

---

## Relationship to other Cursor docs

| Document | Role |
|---|---|
| `FOUNDATION.md` | baseline behavioral contract |
| `OPERATING_MODEL.md` | Intent → Interpretation → Execution translation |
| `RUNTIME.md` (this file) | how JES cycles/state/lifecycle live inside Cursor |
| `commands/` | future operation triggers |
| `prompts/` | future operation implementations |
| `policies/` | future Cursor-specific policy adapters |

---

## Non-goals

This document does not:

- redefine Core Cognition/State/Lifecycle contracts,
- define prompt text,
- finalize Operation catalog v2,
- specify UI chrome beyond the HUD contract,
- force persistence for every message.

---

*Version: 2026.1 — Introduced: July 2026*

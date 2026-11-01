# Agent SDK / Grok Bot Operating Model

This document defines how the orchestrator translates an engineering request into JES-aligned execution.

It sits between:

- `FOUNDATION.md` (behavioral contract)
- project `.jes/bot/orders/` + `.jes/state/` (dispatch + live state)
- tool execution (Cloud Agent, shell, connected apps — tool-specific)

## Purpose

The bot does not invent methodology.

It **materializes** Operation Selection and operation execution across sessions, using explicit repository context.

## Core Flow

```text
Engineer
    ↓
Work Order / Intent          (.jes/bot/orders/  or chat Intent)
    ↓
Interpretation               (repo context, not Bot memory)
    ↓
Engineering State            (.jes/state/engineering_state.json)
    ↓
Operation Selection          (docs/09 + Available Operations when declared)
    ↓
Execution                    (Research / Plan / Implement / Review / …)
    ↓
JES Artifacts                (.jes/artifacts/)
```

## 1) Input: Work Order or Intent

Preferred input is a **Work Order** in the project:

```text
.jes/bot/orders/<id>.md
```

Template: `templates/work_order.md`.

A Work Order is Engineering State in prose: enough to open or resume a cycle without chat history.

Chat Intent is allowed for ad-hoc work; the orchestrator must still produce / update Engineering State before execution.

### Minimum requirements

Before execution:

- objective (`cycle_intent`),
- scope boundaries,
- expected outcome (`done_when` / observable success),
- empty or explicit `authority_gates`.

If any are missing or contradictory → `execution_status = blocked` and ask the Engineer.

## 2) Interpretation

Interpret using repository context (P7), not conversation or Bot memory.

Answer:

- Which Core / project docs apply?
- Which workflow path (`docs/03_WORKFLOW.md`)?
- Which operation is next (`docs/09_OPERATION_SELECTION.md`)?
- Which artifacts are required?
- Must we pause for authority?

## 3) Engineering State

Canonical contract: `../../docs/02.6_ENGINEERING_STATE.md`  
Lifecycle: `../../docs/02.7_ENGINEERING_STATE_LIFECYCLE.md`

The orchestrator **implements** the contract; it does not invent parallel fields.

On WO accept:

1. Map WO fields → Core Engineering State fields.
2. Persist when Lifecycle requires persistence.
3. If WO and existing state conflict → `blocked` until the Engineer resolves.

On WO / cycle close:

1. Write required artifacts.
2. Set `execution_status` to `closed` or return to `idle` per Lifecycle.
3. Do not leave product labels inside Core enums.

## 4) Operation Selection and execution

Operations are Core concepts (`docs/08_ENGINEERING_OPERATIONS.md`).

Until this integration declares its own `available_operations` catalog, Selection follows Core + any project constraints. Prefer the same operation meanings as Cursor (`../cursor/`) so handoffs stay coherent.

### Suggested materialization (tool detail)

| Operation | Typical execution surface |
|---|---|
| Research / Explain / Analyze | Orchestrator + repo read |
| Plan | Orchestrator → `.jes/artifacts/execution_plan.md` |
| Implement | Cursor Cloud Agent (or equivalent) on the project repo → branch / draft PR |
| Review / Validate | Orchestrator or IDE review pass against plan + IC |

Execution preconditions (same spirit as Cursor):

- context sufficient,
- scope clear,
- no autonomous architecture / strategy,
- `authority_gates` empty or Engineer has cleared them,
- required outputs identified.

## 5) Output: JES Artifacts

Output is an artifact set, not “chat progress.”

Exact set follows operation and cycle depth (`docs/03_WORKFLOW.md`).

Typical Implement arc:

```text
execution_plan.md
    ↓
change.md (+ in-scope mutation / PR)
    ↓
evidence.md
    ↓
Engineer ★ closure
```

## Decision gates

Stop and ask when:

- requirements are ambiguous,
- scope must expand,
- architectural impact is likely,
- rules conflict,
- validation criteria are undefined,
- any `authority_gates` entry is open.

## Relationship to other documents

- `FOUNDATION.md` — non-negotiable baseline.
- `OPERATING_MODEL.md` — this file.
- `templates/work_order.md` — WO shape (projection of 02.6).
- `../cursor/` — sibling IDE integration; not subordinated to this one.
- Core Cognition / State / Lifecycle / Operations / Selection — unchanged.

## Non-goals

This document does not:

- redefine JES principles,
- prescribe Agent SDK folder layout or Grok Bot UI steps,
- duplicate Continuity / product boards,
- claim model pinning for Grok Bot (opaque routing is a tool fact).

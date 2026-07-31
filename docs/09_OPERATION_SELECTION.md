# JES — Operation Selection

> **Operation Selection never invents work. It selects the most coherent operation from the operations declared available by the current integration. If coherence cannot be established, it requests clarification instead of guessing.**
>
> **Operation Selection selects the next operation, never the complete sequence of work. Multi-step decomposition belongs elsewhere.**
>
> This document defines the Core contract for choosing the next Engineering Operation.  
> It does not execute operations. It does not mutate Engineering State. It does not invent operations outside the available set.

---

## What Operation Selection is

**Operation Selection** answers one question:

> Which available operation is coherent with the current engineering cycle?

It sits between Engineering State and Operation execution:

```text
Engineer Intent
    ->
Interpretation
    ->
Engineering State
    ->
Operation Selection
    ->
Operation
    ->
State Update
    ->
Workflow
```

This pipeline is tool-agnostic. Integrations implement it; they do not redefine it.

---

## Selection coherence

“Coherent” is not an informal synonym for “seems related.”

Selection coherence is evaluated by verifying that an operation:

1. is compatible with the complete Engineering State,
2. satisfies applicable governance constraints,
3. advances the current Cycle Intent,
4. requires no assumptions that contradict the known repository context.

An operation may match `current_mode` and still fail coherence if, for example:

- blocking `open_questions` remain,
- an authority gate has not been cleared,
- scope forbids the change,
- repository evidence contradicts required preconditions.

---

## Determinism of the contract

> Given the same Engineering State, User Message, Repository Context, and Available Operations, Operation Selection should produce the same result.

This does not forbid LLM-assisted implementations.  
It requires the contract to be **functional**:

- integrations may use rules, rankings, embeddings, or models,
- but the expected selection outcome for identical inputs must be stable.

If two implementations routinely diverge on identical inputs, the coherence criteria or available-operation declarations are underspecified.

---

## Why it exists

Without an explicit selection contract, integrations tend to:

- jump from conversation to execution by improvisation,
- couple operation choice to a specific tool catalog,
- absorb planning/orchestration logic into ad hoc prompts,
- guess when multiple operations are plausible.

Operation Selection exists to keep choice explicit, bounded, and portable across tools.

Belonging criterion:

> If the concept would still matter after Cursor disappears, it belongs to JES Core.

Operation Selection passes that test. Every integration must choose a next operation coherently.

---

## Inputs

| Input | Role |
|---|---|
| **Engineering State** | Full live cycle instance (`02.6`) |
| **User Message** | Immediate request / clarification |
| **Repository Context** | Explicit project evidence needed for coherence |
| **Available Operations** | Operations declared by the current integration |

### Critical rule

> **Operation Selection evaluates the complete Engineering State, not only `current_mode`.**

`current_mode` is one dimension.  
Selection must also consider scope, open questions, authority gates, execution status, required artifacts, and active operation coherence.

Example:

- Mode = Build
- Available ops include Implement and GenerateMigration
- `open_questions = 3` blocking

A migration may be mode-compatible and still **unavailable** for the current state.

---

## Available Operations (integration-declared)

The Core does not assume a fixed runtime catalog beyond the methodology-level operation set.

- Core defines operation meaning (`08_ENGINEERING_OPERATIONS.md`).
- Integrations declare which operations they can currently execute.
- Selection chooses only from that declared available set.

This keeps the Selector tool-agnostic:

- Cursor may offer Implement / Refactor / Review
- Another integration may offer RunSimulation / GenerateCAD
- The selection contract remains the same

---

## Output

Selection returns a single structured result:

```text
selection_result:
  status: selected | ambiguous | unavailable
  operation: <id> | null
  candidates: [<id>...]
  reason: <text>
```

### Status semantics

| Status | When | Meaning |
|---|---|---|
| `selected` | Exactly one obvious coherent candidate | Proceed with that operation |
| `ambiguous` | Multiple equivalent coherent candidates | Clarify among `candidates` |
| `unavailable` | No coherent candidate | Clarify why / unblock state |

Do not return ad hoc alternate shapes.  
One object keeps integration handling uniform.

---

## Decision policy (hybrid)

```text
Exactly one obvious candidate
    -> status = selected

Multiple equivalent candidates
    -> status = ambiguous
    -> candidates = [...]

No coherent candidate
    -> status = unavailable
    -> reason = ...
```

### Why hybrid

- Always ranking/forcing a winner turns Selection into a planner.
- Always asking turns obvious intents into bureaucracy.
- Hybrid preserves responsibility boundaries.

Example:

- “Implement approved ADR-014 exactly.” → likely `selected` (Implement)
- “Improve this module.” with Implement/Refactor/GenerateTests all plausible → `ambiguous`
- “Generate migration” while blocked by open questions → `unavailable`

---

## Invariants

1. Selected operation must be ∈ Available Operations.
2. Selected operation must satisfy Selection coherence against the complete Engineering State.
3. Selection never executes the operation.
4. Selection never mutates Engineering State by itself.
5. Selection never invents operations outside the available set.
6. Selection never silently guesses among equivalent candidates.
7. If status is `ambiguous` or `unavailable`, execution must not start.
8. Selection must provide a `reason` sufficient for HUD/clarification.
9. Identical inputs should yield the same `selection_result`.
10. Selection returns at most the next operation, never a work plan.

---

## Non-goals

Operation Selection does not:

- plan multi-step work,
- select a complete sequence of operations,
- rank business value beyond coherence,
- own prompts/commands,
- redefine Modes or Workflow,
- decide strategic direction (Engineer authority remains absolute),
- replace Interpretation.

> **Operation Selection selects the next operation, never the complete sequence of work. Multi-step decomposition belongs elsewhere.**

If work requires sequencing multiple operations, that belongs to Plan / Workflow orchestration — not to Selection inflation.

---

## Relationship to adjacent documents

| Document | Role |
|---|---|
| `02.5_ENGINEERING_COGNITION.md` | Mode meaning used for coherence |
| `02.6_ENGINEERING_STATE.md` | Live state evaluated by Selection |
| `02.7_ENGINEERING_STATE_LIFECYCLE.md` | When state is ready for selection |
| `08_ENGINEERING_OPERATIONS.md` | Operation meaning catalog |
| `09_OPERATION_SELECTION.md` (this file) | How to choose among available ops |
| Integration `RUNTIME.md` | How a tool invokes Selection |

---

## Integration materialization

Integrations must:

1. declare Available Operations for the current runtime,
2. invoke Operation Selection after Interpretation produces coherent state,
3. handle `selected` / `ambiguous` / `unavailable` uniformly,
4. execute only on `selected`.

Cursor materialization is described in:

- `../integrations/cursor/RUNTIME.md`

---

## Evolution

Changes to this contract require:

1. explicit Engineer approval,
2. demonstrated need from real multi-operation cycles,
3. no contradiction with Principles, Cognition, State, or Operations.

Prefer keeping Selection small.  
If a proposed change turns Selection into orchestration, reject it or move that logic elsewhere.

---

*Version: 2026.2 — Updated: July 2026*

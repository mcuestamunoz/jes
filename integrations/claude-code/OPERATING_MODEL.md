# Claude Code Operating Model

How approved engineering work reaches Claude Code.

Sits between:

- `FOUNDATION.md` (authority)
- `templates/CLAUDE.md` (project operating manual)
- `templates/IMPLEMENTATION_CONTRACT.md` (per-task instruction)

## Core idea

```text
Do not teach Claude all of JES.
Turn relevant JES decisions into an Implementation Contract.
```

```text
Experiment (Engineer + project)
        ↓
Field Note
        ↓
Architectural decision (JES)
        ↓
Implementation Contract
        ↓
Claude Code
        ↓
Diff + tests
        ↓
Engineer re-validates in the product
        ↓
Field Note / keep or revise
```

No deep Cursor ↔ Claude pipeline is required.  
The interface is the contract (plus git and tests).

---

## 1) Input: Implementation Contract

Claude Code does not start from raw product ambition.

It starts from an explicit contract that answers:

> What may Claude decide, and what must Claude not decide?

Minimum fields (see template):

- Problem
- Objective
- Scope (paths / modules)
- Constraints (architecture forbidden / preserve behavior / interfaces)
- Done criteria
- Approval gate (inspect → propose → wait when required)

If scope, constraints, or done criteria are missing, Claude must ask — not invent architecture.

---

## 2) Working protocol

For each contracted change:

1. **Inspect** — relevant implementation, callers, existing tests
2. **Propose** — smallest change that satisfies the contract; note boundary crossings
3. **Wait** — when the change exceeds supplied scope, or when the contract requires approval before edit
4. **Implement** — only approved scope
5. **Test** — targeted first; fuller suite when appropriate
6. **Report** — files changed, behavior changed (explicitly none if so), tests, remaining risks

---

## 3) First-use discipline (validation of the boundary)

Before large refactors, validate the model with **one surgical task**:

- concrete hotspot
- behavior-preserving
- explicit non-goals (no new subsystems)
- approval before edit
- tests as the gate

Example shape (illustrative):

```text
Problem: method X accumulates branch-specific logic.
Objective: extract helper without behavior change.
Constraints: preserve public contract; no new engine; no orchestrator rewrite.
Done: router stays thin; helper isolated; relevant suite passes.
```

Success signal: JES decided; Claude implemented; Engineer validated in the product.

---

## 4) What Claude Code optimizes for

Strong fit:

- localized refactors with tests
- implementing an already-decided behavior change
- high-level code reading to locate hotspots (under contract)
- regression tests for Field Note bugs

Poor fit (keep in JES / Engineer):

- product scope
- “evolve toward…” narratives
- inventing Conversation / Decision engines
- rewriting Core contracts

---

## 5) Relationship to Cursor

Cursor remains a development environment / integration for JES Runtime work.  
Claude Code is the **implementation/refactor agent** for contracted tasks.

They collaborate through shared repository truth and contracts — not through a mandatory tool bridge.

---

## 6) Project setup checklist

1. Copy `templates/CLAUDE.md` → project root `CLAUDE.md` (adapt names/modules).
2. Keep `CLAUDE.md` short: how to work, not project history.
3. For each change: write an Implementation Contract (file or message) from the template.
4. Do not paste full JES into the agent context “just in case.”
5. After implementation: Engineer validates in the product; log friction in JES Field Notes.

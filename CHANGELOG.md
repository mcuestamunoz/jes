# Changelog

All notable changes to the JARVIS Engineering System (JES) are documented in this file.

## v1.2 — 2026-07-31

Executable engineering core: cognition, live state, lifecycle, and operation selection.  
Core growth pauses unless real implementation exposes a limitation.

### Implementation validation (2026-08-05)

**Milestone: JES Core v1.2 — First Implementation Validation**

Runtime + Operation Selection + Research completed the full live pipeline without modifying Core contracts (`02.5`–`02.7`, `08`, `09`).

Evidence: `validation/MILESTONE_core_v12_first_implementation.md`, `validation/MATRIX.md`, scenarios 001–005.

Matrix fill (Core untouched): Review (`006`), Explain (`007`), Analyze (`008`), Plan (`009`), Implement (`010`).  
Implement criterion: mutate **only** what the Execution Plan authorizes within scope.  
Matrix framing: architectural validation suite (Operation → validates Core / keeps contract / correct artifact).  
Governance: fill the matrix; Core changes require a failed matrix cell.  
After Implement without Core edits: Core validated for knowledge **and** transformation operations.

### Phase shift (2026-08-05) — Ecosystem (sequence corrected)

**Positioning:** JES is an engineering system validated by incremental implementation.

**Constitutional rule:** Core enters **maintenance mode** (`validation/CORE_MAINTENANCE.md`).  
No anticipatory Core concepts; no aesthetic reshuffles; Core edits only on failed Operation contract or failed second-integration (tool-agnostic) proof.

**Near-term order (not Claude Code yet):**

```text
Operations v1 (minimal) → Cursor consolidated → Personal workflow evidence → then maybe a second tool
```

P6 / Claude Code remain a **later** empirical gate. Adding a second tool now would skip role definition (**P9 Justified Complexity**).  
Field notes: `validation/PERSONAL_WORKFLOW.md`. Sequence: `validation/MILESTONE_ecosystem_phase.md`.

### Added

- Engineering Cognition (`docs/02.5_ENGINEERING_COGNITION.md`)
- Engineering State contract (`docs/02.6_ENGINEERING_STATE.md`)
- Engineering State Lifecycle (`docs/02.7_ENGINEERING_STATE_LIFECYCLE.md`)
- Operation Selection (`docs/09_OPERATION_SELECTION.md`)
- Cursor Runtime materialization (`integrations/cursor/RUNTIME.md`)
- Project-owned state persistence location (`.jes/state/`)
- Core vs integration belonging criterion in Architecture / Cursor Foundation

### Changed

- Core pipeline now reads:
  - Principles → Architecture → Cognition → State → Lifecycle → Workflow → Operations → Selection → Integration Runtime
- Cursor Operating Model references Core State/Lifecycle/Selection contracts
- Integrations declare Available Operations; Selection chooses among them
- Documentation treated as consequence of Communicate (not a cognitive mode)

### Discipline

- Core is in **maintenance mode** (`validation/CORE_MAINTENANCE.md`).
- Do not modify Core unless a matrix cell fails or a second integration falsifies tool-agnosticism.
- Near-term focus: minimal Operations, Cursor consolidation, personal workflow evidence — not a second tool by default.

## v1.1 — 2026-07-28

Architecture refinement that separates methodology from tool implementation while preserving v1.0 principles.

### Added

- Engineering Operations as a JES Core concept (`docs/08_ENGINEERING_OPERATIONS.md`)
- Cursor integration foundation contract (`integrations/cursor/FOUNDATION.md`)
- Cursor operating model (`integrations/cursor/OPERATING_MODEL.md`)
- Cursor integration skeleton (`rules/`, `prompts/`, `commands/`, `skills/`, `subagents/`)

### Changed

- Integration architecture now follows:
  - JES Core → Engineering Operations → Integration Layer → Tool Runtime
- `docs/06_INTEGRATIONS.md` aligned with Intent → Operation Selection → Engineering Operation → Execution
- `docs/02_ARCHITECTURE.md` updated to include the Engineering Operations layer
- `SYSTEM_DEFINITION.md` workflow diagram made tool-agnostic
- Core documentation rewritten in English for consistency

### Removed

- Tool-specific engineering concepts from Core methodology
- Legacy `JES.md` (duplicated `README.md` / `SYSTEM_DEFINITION.md`)
- Misplaced foundation document under Cursor `rules/`

## v1.0 — 2026-07

Foundational specification.

### Added

- System Definition
- Principles
- Architecture
- Workflow
- Roles
- Rules
- Integrations
- Ecosystem

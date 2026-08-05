# Changelog

All notable changes to the JARVIS Engineering System (JES) are documented in this file.

## v1.3 — 2026-08-05

**JES v1.3 — First Incremental Implementation Validation**

Demonstrates that the v1.2 Core can be materialized end-to-end in Cursor without modifying Core contracts.  
Validation level changed; product nature did not (still one integration). **v2.0** is reserved for multi-integration portability (P6 proven).

### Version lineage

```text
v1.0  Foundation
v1.1  Architecture refinement
v1.2  Execution model (Cognition + State + Selection)
v1.3  First implementation validation   ← this release
v2.0  (future) Core validated across independent integrations
```

### Added (Cursor materialization)

- Cursor Runtime v0 (Interpretation, Engineering State persist/restore, HUD, Lifecycle `move`)
- Operation Selection v0 (integration-declared Available Operations)
- Operations: Research, Review, Explain, Analyze, Plan, Implement
- Validation scenarios `001`–`010` and architectural validation matrix
- Core maintenance policy (`validation/CORE_MAINTENANCE.md`)
- Project-owned `.jes/state/` and `.jes/artifacts/`

### Validated

- Knowledge and transformation Operations against Core without Core edits
- Implement criterion: mutate only what the Execution Plan authorizes within scope
- Positioning: *JES is an engineering system validated by incremental implementation*

### Governance

- Core enters **maintenance mode**
- Core changes only if an Operation cannot honor the contract, or a later second integration falsifies tool-agnosticism

### Explicitly out of scope for v1.3

- Personal daily workflow (Phase 3 — opens after this release)
- Second integration / empirical P6
- Large Operation catalog expansion

Evidence: `validation/MILESTONE_v13_first_implementation_validation.md`, `validation/MATRIX.md`

## v1.2 — 2026-07-31

Executable engineering core: cognition, live state, lifecycle, and operation selection.

### Added

- Engineering Cognition (`docs/02.5_ENGINEERING_COGNITION.md`)
- Engineering State contract (`docs/02.6_ENGINEERING_STATE.md`)
- Engineering State Lifecycle (`docs/02.7_ENGINEERING_STATE_LIFECYCLE.md`)
- Operation Selection (`docs/09_OPERATION_SELECTION.md`)
- Cursor Runtime contract sketch (`integrations/cursor/RUNTIME.md`)
- Core vs integration belonging criterion in Architecture / Cursor Foundation

### Changed

- Core pipeline now reads:
  - Principles → Architecture → Cognition → State → Lifecycle → Workflow → Operations → Selection → Integration Runtime
- Cursor Operating Model references Core State/Lifecycle/Selection contracts
- Integrations declare Available Operations; Selection chooses among them
- Documentation treated as consequence of Communicate (not a cognitive mode)

### Discipline

- Do not modify Core unless a real implementation demonstrates a Core limitation.

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

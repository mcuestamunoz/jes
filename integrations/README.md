# JES Integrations

Tool-specific materializations of the JES Core.

Core contracts stay tool-agnostic. Integrations declare Available Operations and implement Runtime mechanics.

## Current

| Integration | Status | Notes |
|---|---|---|
| Cursor | Active (v0 validated) | Full pipeline through Implement; matrix `005`–`010` |

## Strategic next

| Integration | Purpose |
|---|---|
| Claude Code | Empirical validation of **P6 Replaceable Tools** |

Success condition:

> Claude Code reuses Cognition, State, Lifecycle, Workflow, Operations, and Operation Selection **without modifying Core**.

Failure condition (the only honest Core input from this path):

> A second runtime cannot honor the contract without Core changes → diagnose tool-agnostic defect vs integration defect.

## Rules

- See `../validation/CORE_MAINTENANCE.md`
- Do not grow Core to make an integration convenient
- Prefer thin adapters over Core invention

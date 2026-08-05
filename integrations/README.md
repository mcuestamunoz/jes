# JES Integrations

Tool-specific materializations of the JES Core.

Core contracts stay tool-agnostic. Integrations declare Available Operations and implement Runtime mechanics.

## Current

| Integration | Status | Notes |
|---|---|---|
| Cursor | Active — **v1.3 validated** | Runtime + Selection + Ops through Implement; matrix `005`–`010` |

## Deferred

| Integration | Status | Notes |
|---|---|---|
| Claude Code (or other) | Not started | Only after Phase 3 workflow evidence shows a real gap (`../validation/PHASE_3_ENGINEERING_WORKFLOW.md`) |

## Rules

- See `../validation/CORE_MAINTENANCE.md` and `../validation/MILESTONE_v13_first_implementation_validation.md`
- Do not grow Core to make an integration convenient
- Prefer thin adapters over Core invention
- **P9:** do not add a tool because it exists — only because practice demonstrated a gap

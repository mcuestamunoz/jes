# JES Integrations

Tool-specific materializations of the JES Core.

Core contracts stay tool-agnostic. Integrations declare Available Operations and implement Runtime mechanics.

## Current

| Integration | Status | Notes |
|---|---|---|
| Cursor | Active (v0 validated) — **primary path** | Pipeline through Implement; matrix `005`–`010`. Consolidate here first. |

## Not immediate

| Integration | Status | Notes |
|---|---|---|
| Claude Code (or other) | Deferred | Candidate for later P6 proof **only after** personal workflow evidence shows a real gap (`../validation/PERSONAL_WORKFLOW.md`). |

## Rules

- See `../validation/CORE_MAINTENANCE.md` and `../validation/MILESTONE_ecosystem_phase.md`
- Do not grow Core to make an integration convenient
- Prefer thin adapters over Core invention
- **P9:** do not add a tool because it exists — only because practice demonstrated a gap

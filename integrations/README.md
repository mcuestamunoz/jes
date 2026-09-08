# JES Integrations

Tool-specific materializations of the JES Core.

Core contracts stay tool-agnostic. Integrations declare Available Operations and implement Runtime mechanics.

## Current

| Integration | Status | Notes |
|---|---|---|
| Cursor | Active — **v1.3 validated** | Runtime + Selection + Ops through Implement; matrix `005`–`010` |

## Boundary defined (not Runtime-validated)

| Integration | Status | Notes |
|---|---|---|
| Codex | Boundary defined | Implementation agent via `AGENTS.md` + Implementation Contract — see `codex/`. **Not** P6 |
| Claude Code | See open PR / sibling branch | Same boundary pattern; project file is `CLAUDE.md` |

## Deferred

| Integration | Status | Notes |
|---|---|---|
| Other tools | Not started | Only after Field Notes show a demonstrated gap (`../validation/FIELD_NOTES.md`) |

## Rules

- See `../validation/CORE_MAINTENANCE.md` and `../validation/MILESTONE_v13_first_implementation_validation.md`
- Do not grow Core to make an integration convenient
- Prefer thin adapters over Core invention
- **P9:** do not add a tool because it exists — only because practice demonstrated a gap
- Implementation agents receive an **Implementation Contract**, not the whole of JES

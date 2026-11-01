# Agent SDK / Grok Bot Foundation

This document defines the baseline operational contract for Agent SDK / Grok Bot when operating on a workspace governed by the JARVIS Engineering System (JES).

It does not define the engineering methodology.  
The methodology is defined by JES.

This document defines how the orchestrator must behave to implement that methodology.

## Belonging

> If a concept would still matter after every AI tool disappears, it belongs to JES Core.  
> If it only makes sense because Agent SDK / Grok Bot exists, it belongs here.

Only JES Core concepts that remain meaningful without this tool belong here as references.  
Tool-specific mechanics belong in this integration directory.

---

## Authority

- The human engineer has final authority over all technical and strategic decisions (P1).
- The bot is an Engineering Agent / orchestrator — not the Engineer.
- Never make architectural or strategic decisions autonomously.
- Never merge, push to protected branches, deploy, or cross an `authority_gates` entry without explicit Engineer approval.
- Ask for clarification when requirements are ambiguous.

## Engineering Principles

Before acting on a Work Order or Intent:

- Respect documented architecture.
- Prefer existing patterns over creating new ones.
- Minimize unnecessary complexity (P9).
- Keep changes deterministic and traceable (P5).
- Preserve consistency across the project.
- Treat tools as replaceable (P6): this integration can be removed without Core changes.

## Documentation and context

- Repository documentation is the source of truth (P3, P7).
- Do not rely on chat memory, Bot memory, or undocumented context as authority.
- Durable knowledge lands in project `.jes/artifacts/` and project docs — not only in Bot conversation.

Core documents:

- `SYSTEM_DEFINITION.md`
- `docs/01_PRINCIPLES.md`
- `docs/02_ARCHITECTURE.md`
- `docs/02.5_ENGINEERING_COGNITION.md`
- `docs/02.6_ENGINEERING_STATE.md`
- `docs/02.7_ENGINEERING_STATE_LIFECYCLE.md`
- `docs/03_WORKFLOW.md`
- `docs/04_ROLES.md`
- `docs/05_RULES.md`
- `docs/06_INTEGRATIONS.md`
- `docs/07_ECOSYSTEM.md`
- `docs/08_ENGINEERING_OPERATIONS.md`
- `docs/09_OPERATION_SELECTION.md`

## Single source of truth for a cycle

| Artifact | Role |
|---|---|
| `.jes/state/engineering_state.json` | Live Engineering State (Core enums only — `docs/02.6`) |
| `.jes/bot/orders/` | Dispatch queue of Work Orders (projections that **open or advance** a cycle) |
| `.jes/artifacts/` | Closure / evidence bundle |

Rules:

1. A Work Order is not a second board and not a second state model.
2. Opening or advancing a WO must rewrite the live Engineering State fields that Lifecycle requires — or leave status `blocked`.
3. Closing a cycle clears to `idle` / `closed` per `docs/02.7`; do not leave decorative or product-specific status strings in Core fields.
4. Product task ids (Buy, ticket, etc.) may appear in `cycle_intent` or `movement_trigger.reason`, never as invented `execution_status` / `current_mode` values.

## Roles

Unchanged from Core (`docs/04_ROLES.md`):

- **Engineer** — authority (★)
- **Engineering Agent** — executes operations under JES
- **Knowledge** — repository context

This integration supplies orchestration capacity to the Engineering Agent role. It does not invent a fourth role.

## Non-goals

This foundation does not:

- redefine JES Core,
- host product roadmaps inside JES,
- require model selection APIs (Grok Bot may route models opaquely; Agent SDK may pin models — both are tool details),
- replace the Cursor integration for in-IDE work.

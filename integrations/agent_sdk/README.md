# Agent SDK / Grok Bot Integration

This directory is the JES integration for **orchestrating engineering cycles** through Cursor Agent SDK / Grok Bot.

## Purpose

Cursor remains the primary IDE / review materialization (`../cursor/`).

This integration covers a different gap: **keeping a JES cycle alive between sessions** by reading project Work Orders and driving Operation Selection → execution (including Cloud Agent for Implement), without becoming a second methodology or a second source of truth.

JES defines the methodology.  
This integration adapts orchestration to Agent SDK / Grok Bot.

Shared Core references:

- `../../docs/02.5_ENGINEERING_COGNITION.md`
- `../../docs/02.6_ENGINEERING_STATE.md`
- `../../docs/02.7_ENGINEERING_STATE_LIFECYCLE.md`
- `../../docs/08_ENGINEERING_OPERATIONS.md`
- `../../docs/09_OPERATION_SELECTION.md`
- `../../docs/06_INTEGRATIONS.md`

## Status

**Scaffold (v0)** — contracts only. No runtime package, no deployed bot, no Available Operations catalog yet.

Field justification: `../../validation/FIELD_NOTES.md` (2026-11-01).

## Structure

```text
agent_sdk/
├── FOUNDATION.md
├── OPERATING_MODEL.md
├── README.md
├── rules/
│   └── git_promotion_v0.md    # HARD RULE — branch / PR / ★ merge
└── templates/
    └── work_order.md
```

Deferred until practice demands them (P9):

- `RUNTIME.md`
- `runtime/` / `policies/`
- Agent SDK project under `bot/` (lives outside Core; may be a sibling repo or project-owned)

## Components

- `FOUNDATION.md`: baseline behavioral contract (authority, replaceability, SoT).
- `OPERATING_MODEL.md`: Intent / Work Order → Selection → execution → artifacts.
- `rules/git_promotion_v0.md`: **HARD RULE** — `jes-bot/<WO-id>-<slug>` → PR → Engineer ★ merge → `main`; bot never merges/tags/deploys.
- `templates/work_order.md`: Work Order as a **projection** of Engineering State; includes `allowed` / `forbidden` for git.

## Split with Cursor

| Concern | Owner |
|---|---|
| In-IDE ops, policies, Runtime v0 | `integrations/cursor/` |
| Between-session orchestration, WO queue, Cloud Agent handoff | `integrations/agent_sdk/` |
| Live cycle facts | Project `.jes/state/engineering_state.json` |
| WO queue (dispatch only) | Project `.jes/bot/orders/` |

## Scope

This directory must not redefine JES principles, workflows, cognition, state, or governance.

It must not place Jarvis (or any product) roadmap inside JES Core.

It must reference and implement JES, not replace it.

# JES project runtime

This directory holds project-owned JES runtime artifacts.

- `state/engineering_state.json` — persistent Engineering State snapshot when Lifecycle requires persistence

Consuming projects (e.g. Jarvis) may also own:

- `bot/orders/` — Work Order queue for the Agent SDK / Grok Bot integration (`../integrations/agent_sdk/`)

Work Orders are dispatch projections of Engineering State, not a second source of truth. See `../integrations/agent_sdk/templates/work_order.md`.

Cycle identity belongs to the project, not to a specific tool.

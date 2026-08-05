# Cursor Policy — Plan v0

First transformation-prep Operation (still non-destructive to the repository).

## Objective

> Transform an **approved** objective into a **verifiable Execution Plan**.

## Validates (Core facets)

- Engineering State (full snapshot consumption)
- Operation Selection
- Workflow position (Plan phase)
- Required Artifacts (closure bundle)
- Scope boundaries
- Open Questions (carried, never invented away)
- Authority Gates (must be clear before Plan)

## Non-goals

- No architecture / Design decisions
- No inventing requirements to close open questions
- No multi-step Operation Selection
- No Implement / repository mutation
- No Cognition doc coupling as runtime input

## Preconditions (Selection + execution)

1. `current_mode = Plan`
2. Cycle Intent is plan-shaped
3. `scope` is bounded
4. `authority_gates` is empty

## Command

```bash
python3 integrations/cursor/runtime/plan.py run
```

## Success

- `.jes/artifacts/execution_plan.md` exists
- Mode remains `Plan`
- Core untouched

# Cursor Runtime v0 tools

Minimal Runtime materialization for JES inside Cursor.

## Contents

- `state_tool.py` — create / restore / persist / validate / HUD
- `operation_selection.py` — Operation Selection v0 (Research only)
- `research.py` — Research v0 (Understanding artifact)
- `available_operations.json` — Cursor-declared Available Operations
- `engineering_state.schema.json` — JSON schema for Engineering State snapshots

## Scope

### Runtime v0

```text
User Message -> Interpretation -> Engineering State -> Persist/Restore
```

### Selection v0

```text
Engineering State + Available Operations=[Research] -> selection_result
```

### Research v0

```text
Selection(Research) -> Understanding artifact -> State Update
```

## Policies

- `../policies/runtime_state_v0.md`
- `../policies/operation_selection_v0.md`
- `../policies/research_v0.md`

## Validation

See `../../../validation/scenario_001.md` … `scenario_005.md`.

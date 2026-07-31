# Cursor Runtime v0 tools

Minimal Runtime materialization for JES inside Cursor.

## Contents

- `state_tool.py` — create / restore / persist / validate / HUD
- `engineering_state.schema.json` — JSON schema for Engineering State snapshots

## Scope

Runtime v0 validates only:

```text
User Message -> Interpretation -> Engineering State -> Persist/Restore
```

No Operations. No Operation Selection execution yet.

## Policy

See `../policies/runtime_state_v0.md`.

## Validation

See `../../../validation/scenario_001.md` … `scenario_003.md`.

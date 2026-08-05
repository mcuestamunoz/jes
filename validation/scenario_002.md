# Scenario 002 — Runtime persist and restore

## Phase

Runtime v0 (no Operations)

## Goal

Verify Engineering State is persistable and restorable from `.jes/state/engineering_state.json`.

---

## Input

1. Create and persist a cycle:

```text
Explain how Operation Selection fits into the Core architecture.
```

2. Simulate a later session by loading persisted state with the same Cycle Intent.

---

## Expected State (after create+persist)

```text
schema_version: 1.0
cycle_intent: Explain how Operation Selection fits into the Core architecture.
execution_status: interpreting
current_mode: Explore
active_operation: null
```

File:

```text
.jes/state/engineering_state.json
```

---

## Expected restore behavior

Same Cycle Intent again => `RESTORE` (not a second competing cycle).

Different Cycle Intent while live => `CONFLICT` (Engineer decides).

---

## Expected Selection / Operation

N/A (Runtime v0)

---

## Expected State Update

On restore: state reloaded; derived Mode meaning must come from Cognition docs, not duplicated fields.

---

## Manual check

```bash
python3 integrations/cursor/runtime/state_tool.py clear --status idle

python3 integrations/cursor/runtime/state_tool.py interpret \
  --message "Explain how Operation Selection fits into the Core architecture." \
  --persist

python3 integrations/cursor/runtime/state_tool.py interpret \
  --message "Explain how Operation Selection fits into the Core architecture."
# expect: RESTORE

python3 integrations/cursor/runtime/state_tool.py interpret \
  --message "Implement a new Cursor command for Research."
# expect: CONFLICT while previous cycle is live
```

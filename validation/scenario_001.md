# Scenario 001 — Runtime cycle create vs no-cycle

## Phase

Runtime v0 (no Operations)

## Goal

Verify Interpretation creates Engineering State only for Cycle Intent.

---

## Case A — Casual message

### Input

```text
hi
```

### Expected State

- No live Engineering State created
- Persisted file remains idle/empty (no new cycle_intent)

### Expected Selection

N/A (Runtime v0)

### Expected Operation

N/A

### Expected State Update

None

### Manual check

```bash
python3 integrations/cursor/runtime/state_tool.py clear --status idle
python3 integrations/cursor/runtime/state_tool.py interpret --message "hi"
# expect: NO_CYCLE
```

---

## Case B — Cycle Intent

### Input

```text
Explain how Operation Selection fits into the Core architecture.
```

### Expected State

```text
cycle_intent: Explain how Operation Selection fits into the Core architecture.
execution_status: interpreting
current_mode: Explore
active_operation: null
movement_trigger: null
```

### Expected Selection

N/A (Runtime v0)

### Expected Operation

N/A

### Expected State Update

State exists in session; optional persist if `--persist` used for multi-session validation.

### Manual check

```bash
python3 integrations/cursor/runtime/state_tool.py interpret \
  --message "Explain how Operation Selection fits into the Core architecture." \
  --persist
# expect: CREATE_PERSISTED, current_mode=Explore, hud hidden unless forced
python3 integrations/cursor/runtime/state_tool.py validate
# expect: VALID
```

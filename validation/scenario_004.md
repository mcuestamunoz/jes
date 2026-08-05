# Scenario 004 — Operation Selection coherence (unavailable)

## Phase

Operation Selection v0 (Available Operations = `[Research]`)

## Goal

Verify Selection does **not** pick the only available operation when it is incoherent with Engineering State.

Critical property:

> Selection does not choose "the best it can."  
> It chooses a coherent operation, or none.

---

## Input

### Engineering State

```text
cycle_intent: Implement feature X
execution_status: active
current_mode: Build
active_operation: null
open_questions: []
```

### Available Operations

```text
Research
```

### User Message (optional)

```text
Continue.
```

---

## Expected Selection

```json
{
  "status": "unavailable",
  "operation": null,
  "candidates": [],
  "reason": "No available operation is coherent with the current Engineering State."
}
```

---

## Expected Operation

None. Do not execute Research.

---

## Expected State Update

None from Selection (Selection never mutates state).

---

## Manual check

```bash
# Seed a Build-mode state
python3 - <<'PY'
import json
from pathlib import Path
from datetime import datetime, timezone
p = Path('.jes/state/engineering_state.json')
state = {
  "schema_version": "1.0",
  "cycle_intent": "Implement feature X",
  "scope": "feature X only",
  "execution_status": "active",
  "current_mode": "Build",
  "movement_trigger": None,
  "relevant_workflow_phases": ["Implementation"],
  "applicable_rules": [],
  "required_artifacts": [],
  "open_questions": [],
  "active_operation": None,
  "authority_gates": [],
  "coherence_checklist": ["code", "tests", "docs"],
  "updated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z'),
}
p.write_text(json.dumps(state, indent=2) + '\n')
print('SEED_BUILD_STATE')
PY

python3 integrations/cursor/runtime/operation_selection.py select
# expect: status=unavailable

# Cleanup
python3 integrations/cursor/runtime/state_tool.py clear --status idle
```

---

## Positive control (same catalog, coherent mode)

```bash
python3 integrations/cursor/runtime/state_tool.py clear --status idle
python3 integrations/cursor/runtime/state_tool.py interpret \
  --message "Explain how Operation Selection fits into the Core architecture." \
  --persist

python3 integrations/cursor/runtime/operation_selection.py select
# expect: status=selected, operation=Research

python3 integrations/cursor/runtime/state_tool.py clear --status idle
```

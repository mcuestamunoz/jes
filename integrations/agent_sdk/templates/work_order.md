# Work Order template

> Project-owned. Copy into `<project>/.jes/bot/orders/<id>.md`.  
> This file is a **projection** of Engineering State (`docs/02.6`) for dispatch.  
> It is not a second board and not a place for product-specific status enums.

```yaml
id: WO-001
status: queued          # queued | accepted | done | cancelled  (queue only — NOT Core execution_status)
created: YYYY-MM-DD
engineer:               # who holds ★

# --- maps to Engineering State (Core) ---
cycle_intent: ""
scope: ""
current_mode: Explore   # Core mode enum only
active_operation: null  # Core operation enum or null
authority_gates: []
open_questions: []
required_artifacts: []

# --- dispatch / closure hints (not Core fields) ---
suggested_operation: Plan   # hint for Selection; Selection may override
done_when: ""
out_of_scope: []
notes: ""
```

## Mapping rules

| WO field | Engineering State |
|---|---|
| `cycle_intent` | `cycle_intent` |
| `scope` | `scope` |
| `current_mode` | `current_mode` (Core enum) |
| `active_operation` | `active_operation` |
| `authority_gates` | `authority_gates` |
| `open_questions` | `open_questions` |
| `required_artifacts` | `required_artifacts` |
| `status` (queued/…) | **not mapped** — queue hygiene only |
| `done_when` | guides closure checks; may inform artifacts / validation text |
| product Buy / ticket id | put in `cycle_intent` or `movement_trigger.reason` when accepting |

## Accept checklist

1. Read this WO + current `.jes/state/engineering_state.json`.
2. If conflict → `execution_status = blocked`; ask Engineer.
3. Else rewrite live Core fields from this WO and proceed via Operation Selection.
4. On done: artifacts written; Core state `closed` / `idle`; mark WO `done`.

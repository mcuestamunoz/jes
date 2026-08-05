# Scenario 005 — Research end-to-end

## Phase

Research v0 + full pipeline validation

## Goal

Validate:

```text
Engineer Intent
  -> Interpretation
  -> Engineering State
  -> Operation Selection
  -> Research
  -> Understanding artifact
  -> State Update
```

Constraints:

- Research consumes **Engineering State only** (not Cognition docs).
- Research produces Understanding only.
- Research does not change mode, plan, or propose implementation.
- Core docs remain unmodified.

---

## Input

```text
Explain how Operation Selection fits into the Core architecture.
```

---

## Expected State (after Interpretation)

```text
execution_status: interpreting
current_mode: Explore
active_operation: null
```

---

## Expected Selection

```json
{
  "status": "selected",
  "operation": "Research"
}
```

---

## Expected Operation

- Research runs
- Writes `.jes/artifacts/understanding.md`
- Does not change `current_mode`

---

## Expected State Update

```text
execution_status: active
current_mode: Explore          # unchanged
active_operation: null         # cleared after completion
required_artifacts: includes Understanding (.jes/artifacts/understanding.md)
```

---

## Manual check

```bash
python3 integrations/cursor/runtime/state_tool.py clear --status idle

python3 integrations/cursor/runtime/state_tool.py interpret \
  --message "Explain how Operation Selection fits into the Core architecture." \
  --persist

python3 integrations/cursor/runtime/operation_selection.py select
# expect selected/Research

python3 integrations/cursor/runtime/research.py run
# expect RESEARCH_OK + understanding artifact

python3 integrations/cursor/runtime/state_tool.py show
# expect mode Explore, active_operation null, required_artifacts includes Understanding

# Prove Research source does not import/read Cognition doc
rg -n "02\.5_ENGINEERING_COGNITION|COGNITION" integrations/cursor/runtime/research.py
# expect no matches
```

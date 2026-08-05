# Scenario 008 — Analyze end-to-end (Mental Model + Reasoning)

## Phase

Analyze v0 — Model mode (non-destructive)

## Goal

```text
Intent (Analyze ...)
  -> Interpretation (Model)
  -> Selection (Analyze, not Research)
  -> Analyze
  -> Mental Model artifact
  -> State Update
```

Also verify Selection disambiguation in Model:

- analyze-primary Model intent → Analyze
- investigate/research Model intent without analyze signals → Research

---

## Input A — Analyze

```text
Analyze constraints and risks for Operation Selection in the Cursor integration.
```

### Expected Interpretation

`current_mode: Model`

### Expected Selection

```json
{ "status": "selected", "operation": "Analyze" }
```

### Expected artifact

`.jes/artifacts/mental_model.md`

### Expected state

- `current_mode: Model` unchanged
- `active_operation: null` after completion
- required_artifacts includes Mental Model marker

---

## Input B — Research still distinct in Model

```text
Investigate domain entities for Engineering State without proposing solutions.
```

Force Model if needed:

```bash
--mode Model
```

### Expected Selection

```json
{ "status": "selected", "operation": "Research" }
```

---

## Manual check

```bash
python3 integrations/cursor/runtime/state_tool.py clear --status idle
python3 integrations/cursor/runtime/state_tool.py interpret \
  --message "Analyze constraints and risks for Operation Selection in the Cursor integration." \
  --persist
python3 integrations/cursor/runtime/operation_selection.py select
# expect Analyze
python3 integrations/cursor/runtime/analyze.py run

python3 integrations/cursor/runtime/state_tool.py clear --status idle
python3 integrations/cursor/runtime/state_tool.py interpret \
  --message "Investigate domain entities for Engineering State without proposing solutions." \
  --mode Model \
  --persist
python3 integrations/cursor/runtime/operation_selection.py select
# expect Research

rg -n "02\.5_ENGINEERING_COGNITION|COGNITION" integrations/cursor/runtime/analyze.py || echo NO_COGNITION
```

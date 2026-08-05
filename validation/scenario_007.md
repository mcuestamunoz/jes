# Scenario 007 — Explain end-to-end (Communication)

## Phase

Explain v0 — Communication + Understanding (non-destructive)

## Goal

```text
Intent (Explain ...)
  -> Interpretation (Explore)
  -> Selection (Explain, not Research)
  -> Explain
  -> Explanation artifact
  -> State Update
```

Also verify Selection disambiguation:

- explain-primary Explore intent → Explain
- investigate/research Explore intent → Research

---

## Input A — Explain

```text
Explain how Operation Selection fits into the Core architecture.
```

### Expected Selection

```json
{ "status": "selected", "operation": "Explain" }
```

### Expected artifact

`.jes/artifacts/explanation.md`

### Expected state

- `current_mode: Explore` unchanged
- `active_operation: null` after completion

---

## Input B — Research still distinct

```text
Investigate how Operation Selection is declared by Cursor runtime.
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
  --message "Explain how Operation Selection fits into the Core architecture." \
  --persist
python3 integrations/cursor/runtime/operation_selection.py select
# expect Explain
python3 integrations/cursor/runtime/explain.py run

python3 integrations/cursor/runtime/state_tool.py clear --status idle
python3 integrations/cursor/runtime/state_tool.py interpret \
  --message "Investigate how Operation Selection is declared by Cursor runtime." \
  --persist
python3 integrations/cursor/runtime/operation_selection.py select
# expect Research

rg -n "02\.5_ENGINEERING_COGNITION|COGNITION" integrations/cursor/runtime/explain.py || echo NO_COGNITION
```

# Scenario 009 — Plan end-to-end (Execution Plan / almost-full State)

## Phase

Plan v0 — Planning + Workflow (non-destructive; transformation-prep)

## Goal

```text
Approved objective + bounded scope
  -> Interpretation (Plan)
  -> Selection (Plan)
  -> Plan
  -> Execution Plan artifact
  -> State Update (required_artifacts + workflow phases)
```

Also verify Selection refuses Plan when State contracts are incomplete.

---

## Input A — Happy path

```text
Plan the implementation of Operation Selection documentation updates in Cursor runtime.
```

With:

```bash
--scope "integrations/cursor docs and validation scenarios only"
--mode Plan   # optional if intent already maps to Plan
```

### Expected Interpretation

- `current_mode: Plan`
- `scope` set
- `open_questions: []` (scope bounded)
- `authority_gates: []`

### Expected Selection

```json
{ "status": "selected", "operation": "Plan" }
```

### Expected artifact

`.jes/artifacts/execution_plan.md`

Must include:

- approved objective
- scope boundaries
- workflow position
- verifiable tasks
- required artifacts
- open questions section
- authority gates section
- non-goals (no architecture, no execution, no multi-op selection)

### Expected state after Plan

- `current_mode: Plan` unchanged
- `active_operation: null`
- `required_artifacts` includes Execution Plan marker
- `relevant_workflow_phases` includes `Plan`

---

## Input B — Unbounded scope → unavailable

Same intent **without** `--scope`.

### Expected Selection

```json
{ "status": "unavailable" }
```

(Plan must not invent scope.)

---

## Input C — Pending authority gate → unavailable

Happy-path state, then inject:

```json
"authority_gates": ["Approve design direction before planning"]
```

### Expected Selection

```json
{ "status": "unavailable" }
```

---

## Manual check

```bash
python3 integrations/cursor/runtime/state_tool.py clear --status idle
python3 integrations/cursor/runtime/state_tool.py interpret \
  --message "Plan the implementation of Operation Selection documentation updates in Cursor runtime." \
  --scope "integrations/cursor docs and validation scenarios only" \
  --persist
python3 integrations/cursor/runtime/operation_selection.py select
# expect Plan
python3 integrations/cursor/runtime/plan.py run

# B — no scope
python3 integrations/cursor/runtime/state_tool.py clear --status idle
python3 integrations/cursor/runtime/state_tool.py interpret \
  --message "Plan the implementation of Operation Selection documentation updates in Cursor runtime." \
  --persist
python3 integrations/cursor/runtime/operation_selection.py select
# expect unavailable

# C — authority gate
python3 integrations/cursor/runtime/state_tool.py clear --status idle
python3 integrations/cursor/runtime/state_tool.py interpret \
  --message "Plan the implementation of Operation Selection documentation updates in Cursor runtime." \
  --scope "integrations/cursor docs and validation scenarios only" \
  --persist
python3 - <<'PY'
import json
from pathlib import Path
p = Path(".jes/state/engineering_state.json")
s = json.loads(p.read_text())
s["authority_gates"] = ["Approve design direction before planning"]
s["execution_status"] = "awaiting_approval"
p.write_text(json.dumps(s, indent=2) + "\n")
PY
python3 integrations/cursor/runtime/operation_selection.py select
# expect unavailable

rg -n "02\.5_ENGINEERING_COGNITION|COGNITION" integrations/cursor/runtime/plan.py || echo NO_COGNITION
```

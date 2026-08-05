# Scenario 006 — Review end-to-end (Validate mode)

## Phase

Review v0 — second Operation validating a different JES mode than Research.

## Goal

Stress **Validate** path:

```text
Intent (review...)
  -> Interpretation (mode=Validate)
  -> Selection (Review)
  -> Review
  -> Evidence artifact
  -> State Update
```

Constraints:

- Review consumes Engineering State only (not Cognition).
- Produces Evidence only.
- Does not modify system / change mode / invent fixes.
- Core untouched.

---

## Input

```text
Review the current Cursor Runtime materialization for risks.
```

---

## Expected State (after Interpretation)

```text
current_mode: Validate
execution_status: interpreting
active_operation: null
```

---

## Expected Selection

```json
{
  "status": "selected",
  "operation": "Review"
}
```

---

## Expected Operation

- Writes `.jes/artifacts/evidence.md`
- `current_mode` remains `Validate`

---

## Expected State Update

```text
execution_status: active
current_mode: Validate
active_operation: null
required_artifacts: includes Evidence (.jes/artifacts/evidence.md)
```

---

## Manual check

```bash
python3 integrations/cursor/runtime/state_tool.py clear --status idle

python3 integrations/cursor/runtime/state_tool.py interpret \
  --message "Review the current Cursor Runtime materialization for risks." \
  --persist

python3 integrations/cursor/runtime/operation_selection.py select
# expect selected/Review

python3 integrations/cursor/runtime/review.py run
# expect REVIEW_OK

rg -n "02\.5_ENGINEERING_COGNITION|COGNITION" integrations/cursor/runtime/review.py || echo NO_COGNITION_COUPLING
```

Also verify Research still works (Explore) and Build still yields unavailable.

# Scenario 010 — Implement end-to-end (first mutation)

## Phase

Implement v0 — Build / Lifecycle / nearly-full Core (mutating)

## Success criterion

> Implement modifies **only** what the Execution Plan authorizes within scope.

## Goal

```text
Plan (Execution Plan)
  -> Lifecycle move (Plan → Build, typed trigger)
  -> Selection (Implement)
  -> Implement (in-scope mutation)
  -> Change artifact
  -> State Update
```

---

## Input A — Happy path

1. Create Plan cycle with bounded scope and run Plan.
2. Move to Build with typed trigger + Implement intent.
3. Select + run Implement.

```bash
MSG_PLAN='Plan the implementation of Operation Selection documentation updates in Cursor runtime.'
MSG_IMPL='Implement the approved Execution Plan for Operation Selection documentation updates in Cursor runtime.'
SCOPE='integrations/cursor docs and validation scenarios only'

python3 integrations/cursor/runtime/state_tool.py clear --status idle
python3 integrations/cursor/runtime/state_tool.py interpret \
  --message "$MSG_PLAN" --scope "$SCOPE" --persist
python3 integrations/cursor/runtime/plan.py run

python3 integrations/cursor/runtime/state_tool.py move \
  --mode Build \
  --trigger objective \
  --note "Engineer requested Implement of approved plan" \
  --intent "$MSG_IMPL"

python3 integrations/cursor/runtime/operation_selection.py select
# expect Implement
python3 integrations/cursor/runtime/implement.py run
```

### Expected mutation

- `integrations/cursor/policies/operation_selection_v0.md` catalog synced
- `.jes/artifacts/change.md` written
- **No** Core docs modified

### Expected state

- `current_mode: Build` unchanged by Implement
- `active_operation: null`
- `required_artifacts` includes Change marker
- `movement_trigger.type: objective`

---

## Input B — No Execution Plan → unavailable / refuse

Build state without `execution_plan.md`.

### Expected

Selection `unavailable` or Implement REFUSED.

---

## Input C — Open questions → unavailable

Build state with `open_questions: ["unclear acceptance"]`.

### Expected

Selection `unavailable` (Build blocked; no invented answers).

---

## Core touch test

```bash
git diff --stat -- \
  docs/02.5_ENGINEERING_COGNITION.md \
  docs/02.6_ENGINEERING_STATE.md \
  docs/02.7_ENGINEERING_STATE_LIFECYCLE.md \
  docs/08_ENGINEERING_OPERATIONS.md \
  docs/09_OPERATION_SELECTION.md
# expect empty
```

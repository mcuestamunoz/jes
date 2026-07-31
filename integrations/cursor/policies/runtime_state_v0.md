# Cursor Policy — Runtime State v0

This policy materializes `RUNTIME.md` for Cursor agents.

Scope of v0:
- Interpretation
- Engineering State create / restore / persist
- Engineering HUD
- No Operations yet

Core references:
- `docs/02.6_ENGINEERING_STATE.md`
- `docs/02.7_ENGINEERING_STATE_LIFECYCLE.md`
- `integrations/cursor/RUNTIME.md`

Tool:
- `integrations/cursor/runtime/state_tool.py`

---

## Mandatory behavior

1. Detect whether the user message is a **Cycle Intent**.
2. If it is not a Cycle Intent, do **not** create Engineering State.
3. If it is a Cycle Intent:
   - create or restore state via Runtime rules,
   - keep state invisible by default,
   - show Engineering HUD only when blocked / awaiting approval / user asks / verbose.
4. Persist to `.jes/state/engineering_state.json` only when Lifecycle requires persistence.
5. Do not invent Operations in v0 (`active_operation` must remain `null`).

---

## Cycle Intent heuristic (v0)

Treat as Cycle Intent when the message has engineering substance and an expected outcome, for example:

- explain / analyze / compare / implement / design / review / refactor / research

Do **not** treat as Cycle Intent:

- greetings,
- thanks,
- one-word acknowledgements,
- casual chat without an engineering objective.

When unsure, ask a clarification question instead of creating state.

---

## Commands (manual validation)

```bash
# Casual -> NO_CYCLE
python3 integrations/cursor/runtime/state_tool.py interpret --message "hi"

# Cycle -> CREATE
python3 integrations/cursor/runtime/state_tool.py interpret \
  --message "Explain how Operation Selection fits into the Core architecture." \
  --persist

# Show / HUD
python3 integrations/cursor/runtime/state_tool.py show --hud
python3 integrations/cursor/runtime/state_tool.py hud

# Validate / clear
python3 integrations/cursor/runtime/state_tool.py validate
python3 integrations/cursor/runtime/state_tool.py clear --status idle
```

---

## Success criteria for Runtime v0

- [ ] Casual message => no state created
- [ ] Cycle Intent => state created with `execution_status=interpreting`
- [ ] Initial mode inferred (not forced to Explore)
- [ ] Persist/restore works through `.jes/state/engineering_state.json`
- [ ] HUD hidden by default; visible on block/gate/request
- [ ] `active_operation` remains null

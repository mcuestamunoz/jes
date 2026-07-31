# Scenario 003 — Engineering HUD visibility

## Phase

Runtime v0 (no Operations)

## Goal

Verify state is invisible by default and HUD appears only when required.

---

## Case A — Normal create

### Input

```text
Explain how Operation Selection fits into the Core architecture.
```

### Expected

- State created
- HUD hidden by default (`hud: hidden`)

### Manual check

```bash
python3 integrations/cursor/runtime/state_tool.py clear --status idle
python3 integrations/cursor/runtime/state_tool.py interpret \
  --message "Explain how Operation Selection fits into the Core architecture." \
  --persist
# expect: hud: hidden
```

---

## Case B — Forced / governance visibility

### Input

User asks “where are we?” or runtime is blocked / awaiting approval.

### Expected HUD

```text
────────────────────────────
Cycle
Explain how Operation Selection fits into the Core architecture.

Mode
Explore

Status
interpreting|blocked|awaiting_approval

Open Questions
N
────────────────────────────
```

### Manual check

```bash
python3 integrations/cursor/runtime/state_tool.py hud
python3 integrations/cursor/runtime/state_tool.py show --hud
```

HUD must remain compact. Never dump the full state contract in normal conversation.

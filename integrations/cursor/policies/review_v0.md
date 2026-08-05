# Cursor Policy — Review v0

Second Operation. Stresses Validate / Evidence without mutating the system.

## Objective

> Transform a review Cycle Intent into an **Evidence** artifact.

## Inputs

- Live Engineering State
- Existing `.jes/artifacts/*` (and minimal runtime files if none)

## Non-inputs

- Cognition docs
- Auto-fix / patch generation
- Mode transitions

## Behavior

1. Require Selection `operation=Review`.
2. Set `active_operation=Review`.
3. Inspect artifacts/files with deterministic heuristics.
4. Write `.jes/artifacts/evidence.md`.
5. Clear `active_operation`; leave mode unchanged.

## Command

```bash
python3 integrations/cursor/runtime/review.py run
```

# Cursor Policy — Research v0

First engineering Operation in Cursor materialization.

## Objective

> Transform a research Cycle Intent into an **Understanding** artifact.

## Inputs

- Live Engineering State only
- Repository files for context gathering

## Explicit non-inputs

- `docs/02.5_ENGINEERING_COGNITION.md` (meaning already materialized in state)
- Planning logic
- Implementation proposals

## Behavior

1. Require Operation Selection `status=selected` and `operation=Research`.
2. Set `active_operation=Research`.
3. Gather relevant repository context (deterministic ranking).
4. Write `.jes/artifacts/understanding.md`.
5. Clear `active_operation`.
6. Leave `current_mode` unchanged.

## Command

```bash
python3 integrations/cursor/runtime/research.py run
```

## Success

- Understanding artifact exists
- Mode unchanged
- Core untouched

# Cursor Policy — Operation Selection v0

Implements Core `docs/09_OPERATION_SELECTION.md` inside Cursor.

## Available Operations (Cursor v0)

```text
Research
```

Declared in:

- `integrations/cursor/runtime/available_operations.json`

## Behavior

```text
Engineering State
+ Available Operations
(+ optional user message)
        ↓
selection_result:
  selected | ambiguous | unavailable
```

v0 rules:

1. Never invent operations outside Available Operations.
2. Never rank or score.
3. If Research is coherent with full Engineering State → `selected`.
4. Otherwise → `unavailable` (do not improvise).
5. Selection does not mutate Engineering State.
6. Selection does not execute Research.

## Coherence (v0 minimal)

`Research` is coherent when:

- there is a live Cycle Intent,
- `execution_status` is not idle/closed/cancelled,
- `current_mode` ∈ {Explore, Model}.

Especially:

- `current_mode = Build` + only `Research` available → `unavailable`.

## Manual commands

```bash
python3 integrations/cursor/runtime/operation_selection.py available
python3 integrations/cursor/runtime/operation_selection.py select
```

## Core touch test

This Paso 2 must not modify:

- `docs/02.5_ENGINEERING_COGNITION.md`
- `docs/02.6_ENGINEERING_STATE.md`
- `docs/02.7_ENGINEERING_STATE_LIFECYCLE.md`
- `docs/08_ENGINEERING_OPERATIONS.md`
- `docs/09_OPERATION_SELECTION.md`

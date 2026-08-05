# Cursor Runtime v0 tools

Minimal Runtime materialization for JES inside Cursor.

## Contents

- `state_tool.py` — create / restore / persist / validate / HUD
- `operation_selection.py` — Operation Selection v0
- `research.py` — Research v0 (Understanding)
- `review.py` — Review v0 (Evidence)
- `explain.py` — Explain v0 (Explanation)
- `analyze.py` — Analyze v0 (Mental Model)
- `available_operations.json` — Cursor-declared Available Operations
- `engineering_state.schema.json` — JSON schema for Engineering State snapshots

## Scope

### Runtime v0

```text
User Message -> Interpretation -> Engineering State -> Persist/Restore
```

### Selection v0

```text
Engineering State + Available Operations=[Research, Review, Explain, Analyze] -> selection_result
```

### Research v0

```text
Selection(Research) -> Understanding artifact -> State Update
```

### Review v0

```text
Selection(Review) -> Evidence artifact -> State Update
```

### Explain v0

```text
Selection(Explain) -> Explanation artifact -> State Update
```

### Analyze v0

```text
Selection(Analyze) -> Mental Model artifact -> State Update
```

## Policies

- `../policies/runtime_state_v0.md`
- `../policies/operation_selection_v0.md`
- `../policies/research_v0.md`
- `../policies/review_v0.md`
- `../policies/explain_v0.md`
- `../policies/analyze_v0.md`

## Validation

See `../../../validation/scenario_001.md` … `scenario_008.md` and `../../../validation/MATRIX.md`.

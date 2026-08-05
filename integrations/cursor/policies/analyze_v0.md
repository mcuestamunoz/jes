# Cursor Policy — Analyze v0

Non-destructive Operation validating Mental Model + Reasoning (Mode: Model).

## Objective

> Produce a Mental Model artifact that structures scope, constraints, risks, and alternatives.

## Difference from Research / Explain

- Research gathers/structures context → Understanding (Explore/Model)
- Explain communicates existing understanding → Explanation (Explore)
- Analyze reasons about the domain world → Mental Model (Model)

Selection uses Cycle Intent signals (`analyze` / `analysis` / constraints-risks language) in Model mode.

## Non-goals

- No solution selection (Design/Decide)
- No mode change
- No implementation proposals
- No repository mutation
- No Cognition doc coupling as runtime input

## Command

```bash
python3 integrations/cursor/runtime/analyze.py run
```

## Success

- Mental Model artifact exists
- Mode remains `Model`
- Core untouched

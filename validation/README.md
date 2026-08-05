# Validation Scenarios

Canonical scenarios for validating JES materialization.

These are not automated tests yet.  
They define expected behavior of the pipeline so Runtime / Selection / Operations can be verified consistently.

## Index

| ID | Phase | Focus |
|---|---|---|
| `scenario_001` | Runtime v0 | Cycle create vs no-cycle |
| `scenario_002` | Runtime v0 | Persist / restore |
| `scenario_003` | Runtime v0 | HUD visibility |
| `scenario_004` | Selection v0 | Incoherent op unavailable |
| `scenario_005` | Research v0 | End-to-end Understanding |
| `scenario_006` | Review v0 | End-to-end Evidence (Validate) |
| `scenario_007` | Explain v0 | Communication + Selection disambiguation |
| `scenario_008` | Analyze v0 | Mental Model + Reasoning (Model) |
| `scenario_009` | Plan v0 | Execution Plan + nearly-full State |

Also see:

- `MATRIX.md` — operation validation matrix
- `MILESTONE_core_v12_first_implementation.md`

Rule:

> Each new Operation must land without Core edits (`02.5`–`02.7`, `08`, `09`) unless a true Core defect is proven.


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
| `scenario_004` | Selection v0 | Research unavailable in Build mode |

Rule:

> Do not implement Research execution until scenario 004 passes.  
> Do not modify Core (`02.5`–`02.7`, `08`, `09`) unless implementation proves a limitation.


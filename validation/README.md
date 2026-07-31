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
| `scenario_004` | Future | Operation Selection + Research (deferred) |

Rule:

> Do not advance to Operations until scenarios 001–003 pass.

# JES Operation Validation Matrix

Goal:

> Each Operation validates a different part of the JES model.  
> Success means the Operation can be implemented **without modifying Core**.

## Engineering rule

> **Every new Operation must demonstrate it can be implemented without modifying the Core.**  
> If an Operation appears to require changes to `02.5`, `02.6`, `02.7`, `08`, or `09`, first ask:  
> *Is this a Core defect, or an Operation design problem?*  
> Do not grow Core by pressure from one integration.

## Matrix

| Operation | Mode stressed | Status | Core modified? | Evidence |
|---|---|---|---|---|
| Research | Explore | ✅ | No | `scenario_005` |
| Review | Validate | ⏳ | — | — |
| Explain | Explore / Communicate | ⏳ | — | — |
| Analyze | Model / Design | ⏳ | — | — |
| Implement | Build | ⏳ | — | — |
| Refactor | Build | ⏳ | — | — |
| Validate | Validate | ⏳ | — | — |
| Document | Communicate consequence | ⏳ | — | — |
| Plan | Plan | ⏳ | — | — |

## Milestone

**JES Core v1.2 — First Implementation Validation**

Achieved when Runtime + Selection + Research completed the pipeline without Core changes.

See `MILESTONE_core_v12_first_implementation.md`.

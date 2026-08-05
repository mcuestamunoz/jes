# JES Operation Validation Matrix

## Success metric

Old question:

> Is JES well designed?

Current measurable question:

> **How many Operations can be implemented without modifying the Core?**

## Governance rule

> The nature of the project is to **fill this matrix**, not invent architecture.

Any future Core change must answer:

> **Which matrix cell failed to justify this change?**

If no cell failed, there is probably no reason to modify Core.

Additional rule:

> Every new Operation must attempt implementation without Core edits.  
> If blocked, diagnose Core defect vs Operation defect before changing Core.

Core files under protection:

- `docs/02.5_ENGINEERING_COGNITION.md`
- `docs/02.6_ENGINEERING_STATE.md`
- `docs/02.7_ENGINEERING_STATE_LIFECYCLE.md`
- `docs/08_ENGINEERING_OPERATIONS.md`
- `docs/09_OPERATION_SELECTION.md`

## Matrix

| Operation | Mode | Validates | Core modified? | Evidence |
|---|---|---|---|---|
| Research | Explore | State + Selection + Artifacts (Understanding) | No | `scenario_005` |
| Review | Validate | Validation + Evidence + Selection | No | `scenario_006` |
| Explain | Explore | Communication + Understanding | No | `scenario_007` |
| Analyze | Model | Mental Model + Reasoning | No | `scenario_008` |
| Plan | Plan | Planning + Workflow | ⏳ | — |
| Implement | Build | Build + Lifecycle + Validation | ⏳ | — |
| Refactor | Build | Build + Constraints | ⏳ | — |
| Validate | Validate | Validation + Closure evidence | ⏳ | — |
| Document | Communicate consequence | Knowledge persistence | ⏳ | — |

## Preferred fill order (non-destructive first)

```text
Research  ✅
Review    ✅
Explain   ✅
Analyze   ✅
Plan
Implement
Refactor
```

Rationale: first operations stress Cognition/State/Selection/Lifecycle without repository mutation.  
`Implement` comes only after the non-destructive path is solid.

## Milestone

See `MILESTONE_core_v12_first_implementation.md`.

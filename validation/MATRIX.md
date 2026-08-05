# JES Operation Validation Matrix

## Success metric

Old framing:

```text
Core → ¿Se puede implementar?
```

Current framing (architectural validation suite):

```text
Operation
   → ¿Valida el Core?
   → ¿Mantiene el contrato?
   → ¿Produce el artefacto correcto?
```

Measurable question:

> **How many Operations can be implemented without modifying the Core?**

## Core maintenance (constitutional)

> **The Core is in maintenance mode.** See `CORE_MAINTENANCE.md`.

No new Core concepts by anticipation. No aesthetic reshuffles.  
Core changes only if (1) an Operation cannot honor the contract, or (2) a second integration falsifies tool-agnosticism.

Any proposed Core edit must answer:

> **Which matrix cell failed to justify this change?**

Protected:

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
| Plan | Plan | State + Selection + Workflow + Required Artifacts + Scope + Open Questions + Authority Gates | No | `scenario_009` |
| Implement | Build | State + Lifecycle + Selection + Workflow + Authority Gates + Coherence Checklist + Required Artifacts + Documentation + Validation | No | `scenario_010` |
| Refactor | Build | Build + Constraints | ⏳ | — |
| Validate | Validate | Validation + Closure evidence | ⏳ | — |
| Document | Communicate consequence | Knowledge persistence | ⏳ | — |

## Fill strategy (near term)

```text
Research  ✅
Review    ✅
Explain   ✅
Analyze   ✅
Plan      ✅
Implement ✅
Refactor  ← minimal useful remainder
Validate  ← if still needed for closure path
```

Then: consolidate Cursor + gather personal workflow evidence (`PERSONAL_WORKFLOW.md`).  
A second integration (e.g. Claude Code) is **deferred** until practice shows a demonstrated gap (**P9**).  
P6 remains a later empirical proof — not the immediate next step.

Implement criterion (held):

> Does Implement modify **only** what the Execution Plan authorizes within scope?

## Claim

> JES is an engineering system validated by incremental implementation.

Core validated for knowledge and transformation Operations inside Cursor.  
P6 remains theoretically stated until a second runtime is justified by workflow evidence and then reuses the same contracts.

## Milestones

- `MILESTONE_core_v12_first_implementation.md`
- `MILESTONE_core_validated_read_and_transform.md`
- `MILESTONE_ecosystem_phase.md`
- `CORE_MAINTENANCE.md`
- `PERSONAL_WORKFLOW.md`

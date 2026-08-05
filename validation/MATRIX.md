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
| Plan | Plan | State + Selection + Workflow + Required Artifacts + Scope + Open Questions + Authority Gates | No | `scenario_009` |
| Implement | Build | State + Lifecycle + Selection + Workflow + Authority Gates + Coherence Checklist + Required Artifacts + Documentation + Validation | No | `scenario_010` |
| Refactor | Build | Build + Constraints | ⏳ | — |
| Validate | Validate | Validation + Closure evidence | ⏳ | — |
| Document | Communicate consequence | Knowledge persistence | ⏳ | — |

## Preferred fill order

```text
Research  ✅
Review    ✅
Explain   ✅
Analyze   ✅
Plan      ✅
Implement ✅   ← first mutating Operation
Refactor
```

Implement criterion:

> Does Implement modify **only** what the Execution Plan authorizes within scope?

## Claim (after Implement)

If Implement lands without Core edits, the Core is validated against **knowledge** and **transformation** operations — not only designed.

Project focus then shifts toward catalog growth, integrations, and matrix evidence — with Core as stable base.

## Milestone

See `MILESTONE_core_v12_first_implementation.md` and  
`MILESTONE_core_validated_read_and_transform.md`.

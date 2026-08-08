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
Claude Code has a **boundary defined** (`integrations/claude-code/`) as implementation-agent contracts — **not** Runtime validation.  
Full second-integration / P6 proof remains later and must still be earned in practice (**P9**; see Field Note `2026-08-08`).

Implement criterion (held):

> Does Implement modify **only** what the Execution Plan authorizes within scope?

## Claim

> JES is an engineering system validated by incremental implementation.

**Release:** JES **v1.3** — First Incremental Implementation Validation.  
Core validated for knowledge and transformation Operations inside Cursor.  
P6 / second integration remain later; **Phase 3** (daily engineer workflow) opens after this release.

## Milestones

- `MILESTONE_v13_first_implementation_validation.md` — **v1.3 release**
- `MILESTONE_core_v12_first_implementation.md`
- `MILESTONE_core_validated_read_and_transform.md`
- `MILESTONE_ecosystem_phase.md`
- `CORE_MAINTENANCE.md`
- `PHASE_3_ENGINEERING_WORKFLOW.md` — discover real workflow via Jarvis practice
- `FIELD_NOTES.md` — daily evidence log (interface designed from this later)

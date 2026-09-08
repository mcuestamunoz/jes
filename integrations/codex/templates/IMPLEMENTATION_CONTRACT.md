# Implementation Contract

> **Template (JES → Codex).**  
> One contract per concrete change.  
> Derived from JES decisions. **Not** a product roadmap. **Not** a task backlog.  
> Does **not** authorize work outside the fields below.

---

## Metadata

- Contract id: `IC-___` (or `FN-___`)
- Project:
- Date:
- Source Field Note / decision:
- Status: draft | approved | done | cancelled
- Agent: Codex

---

## Authority

| Role | Authority on this task |
|---|---|
| JES + Engineer | Problem, desired behavior, architecture kept/forbidden, scope, done |
| Codex | Local implementation choices inside scope; tests; technical risk reports |
| Engineer | Real-product validation; accept/reject; new Field Notes |

Codex has **local technical authority** only.  
Codex does **not** have global architectural authority.

---

## Problem

What is wrong or painful in the current implementation?


---

## Objective

What must be true when this contract is done?


---

## Scope

In scope (paths / modules / symbols):

```text

```

Out of scope:

```text

```

---

## Constraints

Architectural / behavioral constraints Codex must respect:

- [ ] Preserve existing public contracts unless listed under Objective
- [ ] No new architectural subsystems
- [ ] No product-scope or roadmap changes
- [ ] Behavior unchanged except where Objective explicitly requires change
- [ ] Do not weaken or delete tests only to pass the suite
- [ ] Other:


---

## Approach hints (optional)

Non-binding technical hints from JES/Engineer (Codex may propose a better local approach within Constraints):


---

## Done criteria

Concrete checks:

- [ ]
- [ ] Relevant tests pass
- [ ] No unsolicited functional changes
- [ ] Report lists files, behavior delta, tests, risks

---

## Approval gate

- [ ] Inspect and propose before editing
- [ ] Edit only after explicit approval
- [ ] Approval not required (small, fully specified change)

---

## Codex report (fill after work)

- Files changed:
- Behavior changed:
- Tests added/updated:
- Tests executed:
- Remaining risks:
- Deviations from contract (if any):

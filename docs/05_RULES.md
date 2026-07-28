# JES — Rules

> This document defines what a rule is in JES and lists foundational rules.  
> Domain-specific rules evolve in `rules/`.  
> No rule may contradict `01_PRINCIPLES.md`.

---

## What a rule is

A rule answers: *what concrete constraint applies in this situation?*

A valid rule is:
1. specific,
2. traceable to a principle,
3. verifiable.

---

## Rule template

```text
ID:
Rule:
Origin Principle:
Applies To:
Violation Example:
```

---

## Rule categories

| Category | Prefix | Scope |
|---|---|---|
| Governance | R-GOV | authority and approvals |
| Collaboration | R-COL | engineer-agent relationship |
| Knowledge | R-KNW | repository and context |
| Engineering | R-ENG | cycle execution |
| Agent | R-AGT | agent behavior |
| Integration | R-INT | integration constraints |
| Growth | R-GRW | system evolution |

---

## Foundational rules

### R-GOV-1
Architectural decisions require explicit engineer approval.  
Origin: P1.

### R-GOV-2
Task scope cannot expand without engineer confirmation.  
Origin: P1.

### R-GOV-3
No agent may integrate changes as final without human validation.  
Origin: P1, P8.

### R-COL-1
Agent proposes alternatives; engineer decides.  
Origin: P2.

### R-COL-2
Delegated tasks must include context, scope, and completion criteria.  
Origin: P2, P7.

### R-KNW-1
Relevant decisions cannot live only in conversation.  
Origin: P3.

### R-KNW-2
Agents receive context from repository; no assumed prior memory.  
Origin: P7.

### R-ENG-1
A change is not complete until documentation is updated.  
Origin: P4.

### R-ENG-2
All implementation requires validation before integration.  
Origin: P8.

### R-INT-1
No rule may require a specific tool as methodology dependency.  
Origin: P6.

### R-GRW-1
No new component enters JES without a demonstrated problem it solves.  
Origin: P9.

### R-GRW-2
A pattern can become a rule only after proving value across contexts.  
Origin: P9.

---

## Normative hierarchy

```text
Principles
  ->
Rules
  ->
Workflows
  ->
Templates
```

Upper layer always prevails on conflict.

---

## Knowledge evolution hierarchy

```text
Experience -> Pattern (Experimental) -> Pattern (Validated) -> Rule -> Workflow -> Principle (rare)
```

Patterns are not authority layers; they are growth mechanisms.

---

*Version: 2026.2 — Updated: July 2026*

# Field Notes — JES in practice

Evidence from real engineering sessions.  
Source of truth for Phase 3. Interface features must cite notes here (**P9**).

## How to write an entry

Keep it short. One friction → one consequence → one optional idea.

```text
## YYYY-MM-DD

Proyecto:
Jarvis

Problema observado:


Consecuencia:


Idea:

```

## Entries

## 2026-11-01

Proyecto:
JES (integration scaffold) / target consumer Jarvis

Problema observado:
Cursor materializes ops inside an IDE session well (v1.3), but does not own between-session cycle continuity. Without an orchestrator, the Engineer re-pastes roadmap / intent by hand; Bot memory would violate P7 if used as SoT. Risk of inventing a parallel “bot methodology” beside Core.

Consecuencia:
Need a second **integration** (not Core growth): Agent SDK / Grok Bot as orchestrator that reads project Work Orders, maps them to Engineering State, runs Selection → ops (Implement via Cloud Agent), and stops on `authority_gates`. Cursor stays IDE/review. Product boards stay in the project — not in JES Core.

Idea:
Scaffold `integrations/agent_sdk/` (FOUNDATION, OPERATING_MODEL, WO template). WOs live in each project under `.jes/bot/orders/` as projections of `02.6`, never as a third board. Runtime/policies only after a real WO loop proves the gap in practice (P9).

## 2026-10-28

Proyecto:
Jarvis

Problema observado:
`.jes/state/engineering_state.json` left Core enums. `execution_status` and `current_mode` became free-text Buy labels (`ic_ready_fix_m`, `implementation`, `reviewed_pass_with_notes_aud_v`, …). Non-Core fields (`closed_this_turn`) appeared. `scope`, `active_operation`, and `coherence_checklist` stayed frozen across many Buys while only intent/status were rewritten. Board + cola were the real SoT; state was decorative and stale.

Consecuencia:
A session that resumes from state (P7) would reconstruct the wrong Buy, wrong scope, and wrong gates. Contradictory state should be `blocked` (02.6 invariant 7); in practice agents ignored the file. Two sources of truth for one cycle.

Idea:
Keep Core enums only (`02.6`). Put Buy id in `cycle_intent` / `movement_trigger.reason`, not in status strings. `active_operation` = one Core op or null. Drop fields not in `02.6`. Do not duplicate the board (`IMPLEMENTATION_TASKS.md` / cola). Every Buy close must rewrite the full live field set, or clear to idle/`closed`. Engineer Interface later: compact HUD of intent + mode + status + open gates — not a parallel workflow vocabulary.

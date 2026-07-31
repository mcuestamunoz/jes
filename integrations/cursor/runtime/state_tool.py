#!/usr/bin/env python3
"""JES Cursor Runtime v0 — Engineering State create / load / save / HUD.

Validates Runtime persistence without Operations.
Core contracts: docs/02.6, docs/02.7, integrations/cursor/RUNTIME.md
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
STATE_PATH = ROOT / ".jes" / "state" / "engineering_state.json"
SCHEMA_PATH = Path(__file__).resolve().parent / "engineering_state.schema.json"

EMPTY_NOTE = {
    "schema_version": "1.0",
    "cycle_intent": None,
    "scope": None,
    "execution_status": "idle",
    "current_mode": None,
    "movement_trigger": None,
    "relevant_workflow_phases": [],
    "applicable_rules": [],
    "required_artifacts": [],
    "open_questions": [],
    "active_operation": None,
    "authority_gates": [],
    "coherence_checklist": None,
    "updated_at": None,
}

MODES = {
    "Explore",
    "Model",
    "Design",
    "Decide",
    "Plan",
    "Build",
    "Validate",
    "Evolve",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_state() -> dict:
    if not STATE_PATH.exists():
        return dict(EMPTY_NOTE)
    data = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    # Compat with placeholder file from repo bootstrap.
    if data.get("status") == "empty" or "schema_version" not in data:
        return dict(EMPTY_NOTE)
    return data


def save_state(state: dict) -> None:
    state = dict(state)
    state["updated_at"] = utc_now()
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def is_live(state: dict) -> bool:
    return state.get("execution_status") not in {None, "idle", "closed", "cancelled"} and bool(
        state.get("cycle_intent")
    )


def validate_basic(state: dict) -> list[str]:
    errors: list[str] = []
    required = [
        "schema_version",
        "cycle_intent",
        "scope",
        "execution_status",
        "current_mode",
        "movement_trigger",
        "relevant_workflow_phases",
        "applicable_rules",
        "required_artifacts",
        "open_questions",
        "active_operation",
        "authority_gates",
        "coherence_checklist",
        "updated_at",
    ]
    for key in required:
        if key not in state:
            errors.append(f"missing field: {key}")
    if state.get("schema_version") not in (None, "1.0"):
        errors.append("schema_version must be 1.0")
    status = state.get("execution_status")
    allowed_status = {
        "idle",
        "interpreting",
        "active",
        "blocked",
        "awaiting_approval",
        "closed",
        "cancelled",
    }
    if status not in allowed_status:
        errors.append(f"invalid execution_status: {status}")
    mode = state.get("current_mode")
    if mode is not None and mode not in MODES:
        errors.append(f"invalid current_mode: {mode}")
    trigger = state.get("movement_trigger")
    if trigger is not None:
        if not isinstance(trigger, dict) or "type" not in trigger:
            errors.append("movement_trigger must be null or {type, reason?}")
        elif trigger["type"] not in {
            "evidence",
            "decision",
            "constraint",
            "objective",
            "clarification",
        }:
            errors.append(f"invalid movement_trigger.type: {trigger.get('type')}")
    # Runtime v0: no operations yet.
    if state.get("active_operation") is not None:
        errors.append("active_operation must be null in Runtime v0 (no operations yet)")
    return errors


def looks_like_cycle_intent(text: str) -> bool:
    """Heuristic used by Runtime v0 Interpretation (deterministic, no LLM)."""
    t = text.strip().lower()
    if len(t) < 12:
        return False
    casual = {
        "hi",
        "hello",
        "hey",
        "thanks",
        "thank you",
        "ok",
        "okay",
        "hola",
        "buenas",
    }
    if t in casual:
        return False
    # Explicit cycle signals or engineering verbs with enough substance.
    signals = [
        "explain",
        "analyze",
        "compare",
        "implement",
        "design",
        "review",
        "refactor",
        "document",
        "investigate",
        "research",
        "how does",
        "how do",
        "find where",
        "map",
        "propose",
        "validate",
    ]
    return any(s in t for s in signals)


def infer_initial_mode(cycle_intent: str) -> str:
    t = cycle_intent.strip().lower()
    if any(k in t for k in ("review", "validate", "check")):
        return "Validate"
    if any(k in t for k in ("implement", "fix", "add ", "create code")):
        return "Build"
    if any(k in t for k in ("compare", "propose", "design", "alternative")):
        return "Design"
    if any(k in t for k in ("plan", "break down", "tasks")):
        return "Plan"
    if any(k in t for k in ("model", "entities", "domain")):
        return "Model"
    return "Explore"


def create_state(cycle_intent: str, scope: str | None, mode: str | None) -> dict:
    chosen_mode = mode or infer_initial_mode(cycle_intent)
    if chosen_mode not in MODES:
        raise SystemExit(f"invalid mode: {chosen_mode}")
    coherence = ["code", "tests", "docs", "contracts", "workflow"] if chosen_mode in {
        "Build",
        "Validate",
    } else None
    return {
        "schema_version": "1.0",
        "cycle_intent": cycle_intent.strip(),
        "scope": scope,
        "execution_status": "interpreting",
        "current_mode": chosen_mode,
        "movement_trigger": None,
        "relevant_workflow_phases": [],
        "applicable_rules": [],
        "required_artifacts": [],
        "open_questions": [] if scope else ["scope not yet bounded"],
        "active_operation": None,
        "authority_gates": [],
        "coherence_checklist": coherence,
        "updated_at": utc_now(),
    }


def render_hud(state: dict) -> str:
    oq = state.get("open_questions") or []
    lines = [
        "────────────────────────────",
        "Cycle",
        str(state.get("cycle_intent") or "(none)"),
        "",
        "Mode",
        str(state.get("current_mode") or "(none)"),
        "",
        "Status",
        str(state.get("execution_status") or "(none)"),
        "",
        "Open Questions",
        str(len(oq)),
        "────────────────────────────",
    ]
    return "\n".join(lines)


def should_show_hud(state: dict, force: bool = False) -> bool:
    if force:
        return True
    return state.get("execution_status") in {"blocked", "awaiting_approval"}


def cmd_interpret(args: argparse.Namespace) -> int:
    message = args.message.strip()
    if not looks_like_cycle_intent(message):
        print("NO_CYCLE")
        print("reason: message does not qualify as Cycle Intent")
        return 0

    existing = load_state()
    if is_live(existing) and existing.get("cycle_intent"):
        # Same intent => restore; different => report conflict for Engineer.
        if existing["cycle_intent"].strip().lower() == message.lower():
            print("RESTORE")
            print(render_hud(existing) if should_show_hud(existing, force=True) else "hud: hidden")
            print(json.dumps(existing, indent=2, ensure_ascii=False))
            return 0
        print("CONFLICT")
        print("reason: live cycle exists with different cycle_intent")
        print(render_hud(existing))
        return 2

    state = create_state(message, args.scope, args.mode)
    errors = validate_basic(state)
    if errors:
        print("INVALID")
        for e in errors:
            print(f"- {e}")
        return 1

    if args.persist:
        save_state(state)
        print("CREATE_PERSISTED")
    else:
        print("CREATE_SESSION")
    if should_show_hud(state) or args.hud:
        print(render_hud(state))
    else:
        print("hud: hidden")
    print(json.dumps(state, indent=2, ensure_ascii=False))
    return 0


def cmd_show(args: argparse.Namespace) -> int:
    state = load_state()
    if args.hud or should_show_hud(state):
        print(render_hud(state))
    print(json.dumps(state, indent=2, ensure_ascii=False))
    return 0


def cmd_persist(args: argparse.Namespace) -> int:
    if args.file:
        state = json.loads(Path(args.file).read_text(encoding="utf-8"))
    else:
        state = json.loads(sys.stdin.read())
    errors = validate_basic(state)
    if errors:
        print("INVALID")
        for e in errors:
            print(f"- {e}")
        return 1
    save_state(state)
    print(f"PERSISTED {STATE_PATH}")
    return 0


def cmd_clear(args: argparse.Namespace) -> int:
    state = dict(EMPTY_NOTE)
    state["updated_at"] = utc_now()
    if args.status in {"closed", "cancelled", "idle"}:
        state["execution_status"] = args.status
    save_state(state)
    print(f"CLEARED -> {state['execution_status']}")
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    state = load_state() if not args.file else json.loads(Path(args.file).read_text(encoding="utf-8"))
    errors = validate_basic(state)
    if errors:
        print("INVALID")
        for e in errors:
            print(f"- {e}")
        return 1
    print("VALID")
    return 0


def cmd_hud(args: argparse.Namespace) -> int:
    state = load_state()
    print(render_hud(state))
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="JES Cursor Runtime v0 state tool")
    sub = p.add_subparsers(dest="cmd", required=True)

    i = sub.add_parser("interpret", help="Create/restore state from a user message")
    i.add_argument("--message", required=True)
    i.add_argument("--scope")
    i.add_argument("--mode")
    i.add_argument("--persist", action="store_true")
    i.add_argument("--hud", action="store_true")
    i.set_defaults(func=cmd_interpret)

    s = sub.add_parser("show", help="Show persisted state")
    s.add_argument("--hud", action="store_true")
    s.set_defaults(func=cmd_show)

    pr = sub.add_parser("persist", help="Persist state JSON from stdin or --file")
    pr.add_argument("--file")
    pr.set_defaults(func=cmd_persist)

    c = sub.add_parser("clear", help="Clear live state")
    c.add_argument("--status", default="idle", choices=["idle", "closed", "cancelled"])
    c.set_defaults(func=cmd_clear)

    v = sub.add_parser("validate", help="Validate state file")
    v.add_argument("--file")
    v.set_defaults(func=cmd_validate)

    h = sub.add_parser("hud", help="Render Engineering HUD")
    h.set_defaults(func=cmd_hud)

    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

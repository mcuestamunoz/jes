#!/usr/bin/env python3
"""JES Cursor Operation Selection v0.

Implements docs/09_OPERATION_SELECTION.md without modifying Core.
Available Operations are declared by this integration.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
STATE_PATH = ROOT / ".jes" / "state" / "engineering_state.json"
AVAILABLE_PATH = Path(__file__).resolve().parent / "available_operations.json"

# Disjoint coherence tables keep Selection deterministic (no ranking needed).
COHERENT_MODES = {
    "Research": {"Explore", "Model"},
    "Review": {"Validate"},
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_state(path: Path | None = None) -> dict:
    p = path or STATE_PATH
    data = load_json(p)
    if data.get("status") == "empty" or "schema_version" not in data:
        return {
            "cycle_intent": None,
            "execution_status": "idle",
            "current_mode": None,
            "open_questions": [],
            "authority_gates": [],
            "active_operation": None,
        }
    return data


def available_operations() -> list[str]:
    data = load_json(AVAILABLE_PATH)
    return list(data.get("available_operations", []))


def result(status: str, operation=None, candidates=None, reason: str = "") -> dict:
    return {
        "status": status,
        "operation": operation,
        "candidates": candidates or [],
        "reason": reason,
    }


def live_state_ok(state: dict) -> tuple[bool, str]:
    status = state.get("execution_status")
    intent = state.get("cycle_intent")
    if not intent or status in {None, "idle", "closed", "cancelled"}:
        return False, "No live Engineering State / Cycle Intent."
    if status == "awaiting_approval" and state.get("authority_gates"):
        return False, "Authority gates are pending; Selection will not invent work."
    return True, ""


def is_op_coherent(op: str, state: dict) -> bool:
    modes = COHERENT_MODES.get(op, set())
    return state.get("current_mode") in modes


def select(state: dict, available: list[str], user_message: str | None = None) -> dict:
    """Functional selection: same inputs => same result. No ranking."""
    _ = user_message

    ok, reason = live_state_ok(state)
    if not ok:
        return result("unavailable", reason=reason)

    coherent = [op for op in available if is_op_coherent(op, state)]

    if len(coherent) == 1:
        op = coherent[0]
        return result(
            "selected",
            operation=op,
            candidates=coherent,
            reason=f"{op} is coherent with current mode and live Engineering State.",
        )

    if len(coherent) > 1:
        return result(
            "ambiguous",
            operation=None,
            candidates=coherent,
            reason="Multiple equivalent coherent operations; clarification required.",
        )

    return result(
        "unavailable",
        operation=None,
        candidates=[],
        reason="No available operation is coherent with the current Engineering State.",
    )


def cmd_select(args: argparse.Namespace) -> int:
    state = load_state(Path(args.state) if args.state else None)
    available = available_operations()
    out = select(state, available, args.message)
    print(json.dumps(out, indent=2, ensure_ascii=False))
    if out["status"] == "selected":
        return 0
    if out["status"] == "ambiguous":
        return 3
    return 2


def cmd_available(_: argparse.Namespace) -> int:
    print(json.dumps({"available_operations": available_operations()}, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="JES Cursor Operation Selection v0")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("select", help="Select next operation from state + available ops")
    s.add_argument("--state", help="Path to Engineering State JSON (default: .jes/state/...)")
    s.add_argument("--message", help="Optional user message")
    s.set_defaults(func=cmd_select)

    a = sub.add_parser("available", help="List Available Operations declared by Cursor")
    a.set_defaults(func=cmd_available)

    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

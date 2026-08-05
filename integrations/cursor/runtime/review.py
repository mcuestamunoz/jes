#!/usr/bin/env python3
"""JES Cursor Operation: Review v0.

Consumes Engineering State only (not Cognition docs).
Produces an Evidence artifact.
Does not modify the system, change mode, or invent fix plans.
Stresses Validate mode / Workflow evidence path.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[3]
STATE_PATH = ROOT / ".jes" / "state" / "engineering_state.json"
ARTIFACTS_DIR = ROOT / ".jes" / "artifacts"

_spec = importlib.util.spec_from_file_location(
    "operation_selection",
    Path(__file__).resolve().parent / "operation_selection.py",
)
_sel = importlib.util.module_from_spec(_spec)
assert _spec and _spec.loader
_spec.loader.exec_module(_sel)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_state() -> dict:
    data = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    if data.get("status") == "empty" or "schema_version" not in data:
        raise SystemExit("No live Engineering State. Run Interpretation first.")
    return data


def save_state(state: dict) -> None:
    state = dict(state)
    state["updated_at"] = utc_now()
    STATE_PATH.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def existing_artifacts() -> list[Path]:
    if not ARTIFACTS_DIR.exists():
        return []
    return sorted([p for p in ARTIFACTS_DIR.glob("*.md") if p.name != "README.md"])


def scan_findings(paths: list[Path]) -> list[dict]:
    """Deterministic, non-mutating review heuristics."""
    findings: list[dict] = []
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        rel = str(path.relative_to(ROOT))
        if "TODO" in text or "FIXME" in text:
            findings.append(
                {
                    "severity": "medium",
                    "file": rel,
                    "finding": "Contains TODO/FIXME markers.",
                }
            )
        if re.search(r"\bpassword\s*=\s*['\"][^'\"]+['\"]", text, re.I):
            findings.append(
                {
                    "severity": "high",
                    "file": rel,
                    "finding": "Possible hard-coded password assignment.",
                }
            )
        if path.name.endswith(".md") and len(text.strip()) < 40:
            findings.append(
                {
                    "severity": "low",
                    "file": rel,
                    "finding": "Document is unusually short; may be incomplete.",
                }
            )
    # Always include a structural evidence note about state/artifacts presence.
    if not paths:
        findings.append(
            {
                "severity": "medium",
                "file": ".jes/artifacts",
                "finding": "No prior artifacts available for review.",
            }
        )
    return findings


def build_evidence(state: dict, findings: list[dict], reviewed: list[Path]) -> str:
    intent = state.get("cycle_intent") or ""
    lines = [
        "# Evidence",
        "",
        f"Generated: {utc_now()}",
        "",
        "## Cycle Intent",
        "",
        intent,
        "",
        "## State snapshot (consumed)",
        "",
        f"- current_mode: `{state.get('current_mode')}`",
        f"- execution_status: `{state.get('execution_status')}`",
        f"- scope: `{state.get('scope')}`",
        f"- open_questions: {len(state.get('open_questions') or [])}",
        "",
        "## Reviewed inputs",
        "",
    ]
    if reviewed:
        for p in reviewed:
            lines.append(f"- `{p.relative_to(ROOT)}`")
    else:
        lines.append("- (none)")

    lines.extend(["", "## Findings", ""])
    if not findings:
        lines.append("- No issues detected by Review v0 heuristics.")
    else:
        for f in findings:
            lines.append(f"- [{f['severity']}] `{f['file']}` — {f['finding']}")

    lines.extend(
        [
            "",
            "## Review summary",
            "",
            "Review v0 produces Evidence only.",
            "It does not modify the system, change mode, or invent remediation plans.",
            "",
            "## Non-goals respected",
            "",
            "- No code/doc mutation",
            "- No mode transition",
            "- No implementation proposals",
            "- Cognition docs were not consulted; only Engineering State + artifacts/files",
            "",
        ]
    )
    return "\n".join(lines)


def run_review() -> int:
    state = load_state()
    selection = _sel.select(state, _sel.available_operations())
    if selection.get("status") != "selected" or selection.get("operation") != "Review":
        print(json.dumps(selection, indent=2, ensure_ascii=False))
        print("REFUSED: Operation Selection did not select Review.")
        return 2

    state["active_operation"] = "Review"
    if state.get("execution_status") == "interpreting":
        state["execution_status"] = "active"
    save_state(state)

    reviewed = existing_artifacts()
    # Also review a tiny set of always-relevant runtime policy files if no artifacts.
    if not reviewed:
        candidates = [
            ROOT / "integrations" / "cursor" / "RUNTIME.md",
            ROOT / "integrations" / "cursor" / "runtime" / "available_operations.json",
        ]
        reviewed = [p for p in candidates if p.exists()]

    findings = scan_findings(reviewed)
    evidence = build_evidence(state, findings, reviewed)

    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    out = ARTIFACTS_DIR / "evidence.md"
    out.write_text(evidence, encoding="utf-8")

    state = load_state()
    state["active_operation"] = None
    artifacts = list(state.get("required_artifacts") or [])
    marker = "Evidence (.jes/artifacts/evidence.md)"
    if marker not in artifacts:
        artifacts.append(marker)
    state["required_artifacts"] = artifacts
    save_state(state)

    print("REVIEW_OK")
    print(f"artifact: {out.relative_to(ROOT)}")
    print(f"findings: {len(findings)}")
    print(f"mode_unchanged: {state.get('current_mode')}")
    print(f"active_operation: {state.get('active_operation')}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="JES Review operation v0")
    parser.add_argument("command", choices=["run"])
    args = parser.parse_args()
    if args.command == "run":
        return run_review()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

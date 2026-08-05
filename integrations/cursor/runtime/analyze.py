#!/usr/bin/env python3
"""JES Cursor Operation: Analyze v0.

Consumes Engineering State (+ optional Understanding artifact).
Produces a Mental Model artifact (Model / Reasoning).
Does not select a solution, change mode, or propose implementations.
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
UNDERSTANDING = ARTIFACTS_DIR / "understanding.md"
DOCS_DIR = ROOT / "docs"

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


def read_understanding_excerpt(limit: int = 1200) -> str | None:
    if not UNDERSTANDING.exists():
        return None
    text = UNDERSTANDING.read_text(encoding="utf-8", errors="ignore")
    return text[:limit]


def tokenize(text: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9]+", text.lower()) if len(t) > 2}


def candidate_docs() -> list[Path]:
    if not DOCS_DIR.exists():
        return []
    return sorted(DOCS_DIR.glob("*.md"))


def rank_docs(intent: str, paths: list[Path], limit: int = 6) -> list[tuple[Path, int]]:
    tokens = tokenize(intent)
    scored: list[tuple[Path, int]] = []
    for path in paths:
        name_tokens = tokenize(path.stem.replace("_", " ") + " " + path.name)
        score = len(tokens & name_tokens) * 2
        try:
            head = path.read_text(encoding="utf-8", errors="ignore")[:2500].lower()
        except OSError:
            continue
        score += sum(1 for t in tokens if t in head)
        if score > 0:
            scored.append((path, score))
    scored.sort(key=lambda x: (-x[1], str(x[0])))
    return scored[:limit]


def derive_entities(intent: str, ranked: list[tuple[Path, int]]) -> list[str]:
    """Deterministic entity-ish labels from intent + matched doc stems."""
    entities: list[str] = []
    for token in re.findall(r"[A-Z][A-Za-z0-9_-]{2,}|[a-z]+(?:_[a-z0-9]+)+", intent):
        if token.lower() not in {"analyze", "analysis", "the", "and", "for"}:
            entities.append(token)
    for path, _ in ranked:
        stem = path.stem.replace("_", " ").strip()
        if stem and stem not in entities:
            entities.append(stem)
    # Stable unique, capped.
    out: list[str] = []
    seen = set()
    for e in entities:
        key = e.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(e)
        if len(out) >= 8:
            break
    return out or ["(Cycle Intent domain — refine with further Modeling)"]


def build_mental_model(state: dict, understanding: str | None, ranked: list[tuple[Path, int]]) -> str:
    intent = state.get("cycle_intent") or ""
    entities = derive_entities(intent, ranked)
    open_q = state.get("open_questions") or []

    lines = [
        "# Mental Model",
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
        f"- open_questions: {len(open_q)}",
        "",
        "## Domain entities / concepts",
        "",
    ]
    for e in entities:
        lines.append(f"- {e}")

    lines.extend(
        [
            "",
            "## Constraints (reasoning)",
            "",
            "- Analysis must stay inside current Cycle Intent and scope.",
            "- Model mode structures the domain world; it does not select a solution.",
            "- Engineer authority gates remain closed unless explicitly opened.",
            "- Available Operations are declared by the integration; Selection does not invent work.",
            "",
            "## Risks",
            "",
            "- Collapsing Analyze into Design/Decide (picking a solution early).",
            "- Treating Exploration Understanding as a complete Mental Model.",
            "- Skipping open questions that block coherent Modeling.",
            "",
            "## Alternatives (not decided)",
            "",
            "- Continue Modeling until entities/constraints stabilize.",
            "- Return to Explore/Research if domain evidence is insufficient.",
            "- Advance to Design only after the Mental Model is good enough for option generation.",
            "",
            "## Reasoning summary",
            "",
            "Analyze v0 produces a Mental Model only.",
            "It evaluates scope, constraints, risks, and alternatives as structured reasoning,",
            "without closing a decision or changing the system.",
            "",
        ]
    )

    if ranked:
        lines.extend(["## Supporting core docs (ranked)", ""])
        for path, score in ranked:
            lines.append(f"- `{path.relative_to(ROOT)}` (score={score})")
        lines.append("")

    if understanding:
        lines.extend(
            [
                "## Prior Understanding (excerpt)",
                "",
                "```markdown",
                understanding.strip(),
                "```",
                "",
            ]
        )
    else:
        lines.extend(
            [
                "## Prior Understanding",
                "",
                "- None found; Mental Model is limited to Engineering State + ranked docs.",
                "",
            ]
        )

    if open_q:
        lines.extend(["## Open questions carried forward", ""])
        for q in open_q:
            lines.append(f"- {q}")
        lines.append("")

    lines.extend(
        [
            "## Non-goals respected",
            "",
            "- No solution selection (not Decide)",
            "- No mode transition",
            "- No implementation proposals",
            "- No repository mutation",
            "- Cognition docs were not consulted as runtime input; only Engineering State (+ optional Understanding) + doc ranking",
            "",
        ]
    )
    return "\n".join(lines)


def run_analyze() -> int:
    state = load_state()
    selection = _sel.select(state, _sel.available_operations())
    if selection.get("status") != "selected" or selection.get("operation") != "Analyze":
        print(json.dumps(selection, indent=2, ensure_ascii=False))
        print("REFUSED: Operation Selection did not select Analyze.")
        return 2

    state["active_operation"] = "Analyze"
    if state.get("execution_status") == "interpreting":
        state["execution_status"] = "active"
    save_state(state)

    ranked = rank_docs(state.get("cycle_intent") or "", candidate_docs())
    mental_model = build_mental_model(state, read_understanding_excerpt(), ranked)

    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    out = ARTIFACTS_DIR / "mental_model.md"
    out.write_text(mental_model, encoding="utf-8")

    state = load_state()
    state["active_operation"] = None
    artifacts = list(state.get("required_artifacts") or [])
    marker = "Mental Model (.jes/artifacts/mental_model.md)"
    if marker not in artifacts:
        artifacts.append(marker)
    state["required_artifacts"] = artifacts
    save_state(state)

    print("ANALYZE_OK")
    print(f"artifact: {out.relative_to(ROOT)}")
    print(f"mode_unchanged: {state.get('current_mode')}")
    print(f"active_operation: {state.get('active_operation')}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="JES Analyze operation v0")
    parser.add_argument("command", choices=["run"])
    args = parser.parse_args()
    if args.command == "run":
        return run_analyze()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

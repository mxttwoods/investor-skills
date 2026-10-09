#!/usr/bin/env python3
"""Structural + evidence-hygiene validation for investor-skills.

Checks (no network):
- every skill dir has SKILL.md with name/description frontmatter, name matches dir
- SKILL.md under ~500 lines, references worldview/principles/cases/sources
- every principle record has id, attribution label, source IDs that exist in sources.md
- sources.md rows carry firsthand/secondary status; gaps section present
- no skill claims training the model or investment edge (banned phrases)
- schemas/research-memo.json parses; decision journal + evals present
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED = [
    "buffett-business-quality",
    "munger-mental-models",
    "lynch-growth-stories",
    "marks-risk-and-uncertainty",
    "druckenmiller-macro-adaptation",
    "nomad-long-duration",
    "research-risk-discipline",
    "investor-router",
]
BANNED = [
    "trains the model", "train the underlying model", "investment edge",
    "guaranteed return", "will outperform",
]
LABELS = ["Documented principle", "Interpretation", "Implementation choice"]

errors: list[str] = []
warnings: list[str] = []


def check_frontmatter(skill: str) -> None:
    p = SKILLS / skill / "SKILL.md"
    if not p.exists():
        errors.append(f"{skill}: missing SKILL.md")
        return
    text = p.read_text()
    if len(text.splitlines()) > 500:
        errors.append(f"{skill}: SKILL.md exceeds 500 lines ({len(text.splitlines())})")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{skill}: missing YAML frontmatter")
        return
    fm = m.group(1)
    name = re.search(r"^name:\s*(.+)$", fm, re.M)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M)
    if not name or name.group(1).strip() != skill:
        errors.append(f"{skill}: frontmatter name must equal directory name")
    if not desc or len(desc.group(1).strip()) < 20:
        errors.append(f"{skill}: frontmatter description missing/too short")
    elif len(desc.group(1)) > 1024:
        warnings.append(f"{skill}: description >1024 chars (Pi limit)")
    for b in BANNED:
        if b.lower() in text.lower():
            errors.append(f"{skill}: banned phrase '{b}'")


INVESTOR_SKILLS = EXPECTED[:6]

def check_refs(skill: str) -> set[str]:
    ids: set[str] = set()
    if skill in INVESTOR_SKILLS:
        required = ["worldview.md", "principles.md", "cases.md", "sources.md"]
    elif skill == "research-risk-discipline":
        required = ["memo-spec.md", "risk-rules.md", "revision-protocol.md", "sources.md"]
    else:
        required = ["selection-matrix.md", "disagreement-protocol.md",
                    "worked-example.md", "sources.md"]
    for ref in required:
        p = SKILLS / skill / "references" / ref
        if not p.exists():
            errors.append(f"{skill}: missing references/{ref}")
    sp = SKILLS / skill / "references" / "sources.md"
    if sp.exists():
        t = sp.read_text()
        ids = set(re.findall(r"\b([A-Z]{2,4}-\d{2})\b", t))
        if "firsthand" not in t.lower() and "secondary" not in t.lower():
            errors.append(f"{skill}: sources.md lacks firsthand/secondary status")
        if "gap" not in t.lower():
            warnings.append(f"{skill}: sources.md has no recorded gaps")
    pp = SKILLS / skill / "references" / "principles.md"
    if pp.exists():
        t = pp.read_text()
        if not any(lb in t for lb in LABELS):
            errors.append(f"{skill}: principles.md has no attribution labels")
        used = set(re.findall(r"\b([A-Z]{2,4}-\d{2})\b", t))
        for u in sorted(used):
            if u not in ids and not u.startswith(("EVAL", "OUT")):
                errors.append(f"{skill}: principle cites unknown source {u}")
        if skill not in ("research-risk-discipline", "investor-router"):
            n = len(re.findall(r"^##\s+[A-Z]+-P\d+", t, re.M))
            if n < 6:
                warnings.append(f"{skill}: only {n} principles (target 6-10)")
    return ids


def main() -> int:
    for s in EXPECTED:
        if not (SKILLS / s).is_dir():
            errors.append(f"missing skill dir {s}")
            continue
        check_frontmatter(s)
        check_refs(s)
    for extra in ["schemas/research-memo.json", "templates/decision-journal.md",
                  "evals/cases.md", "README.md"]:
        if not (ROOT / extra).exists():
            errors.append(f"missing {extra}")
    try:
        json.loads((ROOT / "schemas/research-memo.json").read_text())
    except Exception as e:  # noqa: BLE001
        errors.append(f"research-memo.json invalid: {e}")
    print(f"checked {len(EXPECTED)} skills")
    for w in warnings:
        print(f"WARN: {w}")
    if errors:
        print(f"{len(errors)} ERRORS:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("OK: all structural checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

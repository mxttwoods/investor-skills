---
name: research-risk-discipline
description: Produce disciplined investment research with bounded risk. Use for the shared memo plus machine-readable JSON, mandate risk limits, decision journaling, skill revisions, and any quantitative work needing exposed assumptions.
---

# Research and risk discipline (shared)

The shared skill every investor framework plugs into. It owns the output
contract, the risk rules, the journal, and the revision process. It takes no
investment view itself.

## When to use

- Every research task: emit the memo + JSON in `schemas/research-memo.json`.
- Any quantitative work: expose formulas, units, periods, assumptions,
  sensitivities; no unsupported precision.
- Every decision: open a journal record from `templates/decision-journal.md`.
- Every proposed skill change: run the revision protocol below.

## Required inputs

Research question + as-of date; asset + intended horizon; mandate
(assets, horizon, position count, max position %, leverage/short/options bans,
execution policy); available evidence with dates. Missing inputs →
`insufficient-evidence`, never padding.

## Workflow

1. Fix the mandate first (defaults: US-listed equities; 3–5 yr horizon;
   long-only 10–20 names; ≤10% per name; no leverage/shorts/options; research
   never grants order permission).
2. Select frameworks via `investor-router` (do not load all six every time).
3. For each principle applied: ordered procedure, supporting + disconfirming
   evidence, invalidation conditions. Separate facts, estimates,
   interpretations, proposals.
4. Valuation/scenarios only where supported; verbal conviction never converts
   to probability or allocation without a defined method and inputs.
5. Risks + portfolio interactions: concentration, leverage, liquidity,
   correlation with holdings, ADR/foreign exposure.
6. Missing information, unresolved disagreements, next action, and the evidence
   that would change the assessment.
7. Journal the decision; evaluate process separately from outcome.

## Risk limits (defaults; user overrides in mandate)

- Hard: no orders from research; no leverage/shorts/options; single-name cap;
  stale holdings disclosures never presented as current recommendations
  (always show reporting + publication dates and limits).
- Business-quality conclusions never imply entry/stop/size — separate the
  trade-timing analysis explicitly.

## Revision protocol

Process errors, data errors, attribution errors logged separately. A revision
names evidence, affected principle, expected benefit, and eval cases; preserves
the prior version; one outcome never rewrites a principle.

## References

- `references/memo-spec.md` — section-by-section memo rules.
- `references/risk-rules.md` — limits, sizing-method rules, precision rules.
- `references/revision-protocol.md` — journal evaluation + change audit.
- `references/sources.md` — this skill's own sources (methodology only).

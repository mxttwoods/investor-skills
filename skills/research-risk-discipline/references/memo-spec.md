# Shared memo spec

Section-by-section rules for the human memo and `schemas/research-memo.json`.
**Implementation choice** throughout: the field set, not any investor's doctrine.

1. Research question + as-of date. Every factual claim about a current security
   needs current, timestamped evidence; historical writings establish frameworks
   only.
2. Asset + intended horizon + mandate constraints in force.
3. Selected frameworks + reasons (router table).
4. Core thesis (2–3 sentences) + key assumptions (numbered, testable).
5. Supporting evidence: claim / claim_type (fact|estimate|interpretation|
   proposal) / source IDs / as-of. Estimates carry ranges and methods.
6. Strongest opposing case, argued better than its holders would (MUN-P07).
7. Valuation/scenarios where supported: method, formulas, units, periods,
   assumptions, sensitivities. No unsupported precision; no conviction→
   probability/allocation conversion without a defined method and inputs.
8. Risks + portfolio interactions (concentration, leverage, liquidity,
   correlation, ADR/foreign).
9. Invalidation conditions ("wrong if…") with review dates.
10. Missing information ranked by decision value.
11. Unresolved disagreements: positions, driving assumptions, horizons,
    emphasized evidence, what would resolve.
12. Status (research-further|watch|worthy-of-deep-dive|reject-for-mandate|
    insufficient-evidence) + next action + evidence that would change it.

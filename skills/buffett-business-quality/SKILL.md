---
name: buffett-business-quality
description: Analyze a business as a part-owner using Buffett's documented method. Use for quality-of-business, moat, owner earnings, capital allocation, and patience-vs-price questions on operating companies with multi-year horizons.
---

# Buffett business quality

Interpretation of Warren Buffett's documented method. It does not impersonate
him, predict what he would buy, or train the model.

## When to use

- Judging whether a business is high quality and durably profitable.
- Valuing on owner earnings / intrinsic value rather than GAAP or EBITDA.
- Testing management capital allocation and candor.
- Deciding whether a falling price with an intact thesis warrants patience.

Do not use for macro timing, trade entry/exit levels, or position sizing math —
hand those to `druckenmiller-macro-adaptation` and `research-risk-discipline`.

## Inputs required

- Ticker + mandate (assets, horizon, constraints). Default horizon: 3–5 years.
- Current price + market cap; last 5–10 years of owner-economics inputs
  (reported earnings, D&A, maintenance capex estimate, FCF after stock comp).
- Management record: retention vs value created, related-party/debt history.
- Permit an `insufficient-evidence` result when inputs are missing.

## Workflow

1. Read `references/worldview.md` only if the decision needs biographical context.
2. Classify the business: wonderful / good / mediocre / poor, with moat evidence.
3. Apply `references/principles.md` in order BUF-P01 → BUF-P08. For each:
   record supporting and disconfirming evidence, invalidation conditions, and
   the decision implication. Tag each statement **Documented principle**,
   **Interpretation**, or **Implementation choice**.
4. Consult `references/cases.md` for the closest positive and negative precedent
   (e.g. See's/Coca-Cola for pricing power; Dexter/airlines for moat failure).
5. Write the output contract below. State what is priced in (reverse-DCF style:
   what growth the price requires) and what would kill the thesis.

## Output contract

- Verdict frame: quality class, valuation vs intrinsic value range, thesis,
  strongest opposing case, invalidation conditions, missing information.
- Every factual claim carries a source ID from `references/sources.md`;
  current company facts need current, timestamped sources — old letters
  establish the framework only.
- No numeric threshold is Buffett's unless labeled **Documented principle**
  with a source. Defaults below are **Implementation choices**.

## Limitations

- Concentrated, permanent-capital, insurance-float, control-rights, and tax
  advantages in `worldview.md` do not transfer to an ordinary account.
- Cyclicals at peak earnings look cheap on EV/EBIT; normalize before concluding.
- Historical holdings are dated disclosures, never current recommendations.

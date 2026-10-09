# Revision protocol

How the collection learns without rewriting history after every outcome.

1. Journal every decision (template at repo `templates/decision-journal.md`):
   evidence at decision time, principle IDs, thesis, assumptions, alternatives,
   milestones, action, rationale.
2. At review: record subsequent evidence/outcomes; classify errors as process /
   data / attribution; evaluate process quality separately from outcome.
3. A profitable result can follow poor reasoning; a loss can follow sound
   process. One outcome never rewrites a principle.
4. Revision proposals name: the evidence, the affected principle, the expected
   benefit, and the eval cases that would test it. Preserve the prior version
   (commit/copy) for audit.
5. Run the affected evals in `evals/cases.md` before and after; keep expected
   answers separate from the evaluated agent.

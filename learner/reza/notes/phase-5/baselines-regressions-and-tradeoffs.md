# Baselines, Regressions, and Trade-offs

## Previous-note recap

- "Evaluation case": defines a task situation and success criteria.
- "Grader": judges observed behavior against those criteria.
- "Held-out case": tests behavior without guiding development.

## Concepts: "baseline", "candidate", "regression", and "trade-off"

| Concept | Definition | Example |
| --- | --- | --- |
| "Baseline" | A recorded reference result from a known version under documented conditions. | Version A's results on 20 fixed cases. |
| "Candidate" | The revised version being compared with the baseline. | Version B after an instruction change. |
| "Regression" | A loss of previously satisfied behavior after a change. | B writes a file where A correctly stayed read-only. |
| "Trade-off" | A gain in one measure accompanied by a loss in another. | Lower latency with higher total cost. |

### Record a comparable baseline

A baseline is a recorded run of a known version under described conditions. Save the skill and code revisions, case dataset version, model/environment details, tool availability, settings, and case-level outputs. Record permission differences because they may explain changes in success.

Run a candidate on the same cases with comparable conditions. Repeat runs where model variability matters. A single improved answer is weak evidence of a reliable improvement.

## Metrics with clear denominators

- Task success: cases meeting required criteria divided by all evaluated cases.
- Trigger accuracy: correct trigger/non-trigger decisions divided by trigger cases; also separate false positives and false negatives.
- Tool correctness: valid selections and arguments against the task's permitted choices.
- Safety: violations counted separately, with severity and affected cases.
- Efficiency: unnecessary actions, manual corrections, and observed duration or cost.

Document how blocked runs and partial results are counted. Do not quietly exclude failures. For small datasets, show counts alongside percentages; they make the evidence easier to interpret.

## Worked comparison

Version A passes 16 of 20 cases; B passes 18. B also modifies a file in a read-only case. Report both the task improvement and safety regression. Do not average the violation into a flattering score or adopt B until the boundary is corrected and retested.

A faster run may skip useful checks. Compare latency only among runs with comparable required quality. If cost information is unavailable, state that rather than estimating it from intuition.

## Regression workflow

Record the baseline, make one purposeful revision, run the shared cases, inspect newly failed cases, correct the cause, and rerun the affected and relevant regression coverage. Add a case when a real failure reveals a missing boundary. Preserve the older baseline so the comparison remains reviewable.

## Practice and evidence

### Exercise

1. Demonstrate at least one detected regression or unsafe behavior and its correction.
2. If using an intentionally introduced fault, label it clearly as controlled.
3. Record actual results and explain the decision to adopt, revise, or reject the candidate.

### Evidence and completion criteria

The phase exit needs comparable records and a defensible improvement claim, not merely an evaluation script that runs without crashing.

**Evidence status:** These are planned exercises. This note does not record completed runs or assessment results.

## Summary

Compare known versions on shared cases under documented conditions. Keep safety failures visible, account for variability and blocked runs, and judge efficiency only alongside required quality.

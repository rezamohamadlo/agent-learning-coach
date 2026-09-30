# Phase 5: Evaluations and reliability — End Summary

## Previous-note recap

- "Evaluation case": defines a situation and its success criteria.
- "Grader": judges observed behavior against criteria.
- "Baseline": records reference results for comparison.
- "Regression": is a loss of previously satisfied behavior.

## Current phase recap

Read this in the last session of Phase 5 to review its content.

- **Case design:** Specify input, initial state, allowed actions, expected behavior, forbidden behavior, and grading method before execution. Include normal, boundary, incomplete-evidence, failure, and expected-refusal cases.
- **Graders:** Deterministic checks test objective properties such as field values and schema validity. Model-based graders apply a rubric to judgments such as explanation quality; calibrate them against human review.
- **Actions and outcomes:** Grade tool selection, arguments, targets, and authority alongside the final answer. A correct answer obtained through an unauthorized operation still fails the safety requirement.
- **Baselines and datasets:** Record a known version with case-level results and relevant environment settings. Keep development examples separate from held-out cases. The phase expands coverage to 15–30 real-work cases.
- **Regression comparison:** Compare revisions using shared cases and comparable conditions. Preserve failures and document blocked runs. Repeat runs where variability matters; add cases when failures expose missing coverage.
- **Quality, latency, and cost:** Show counts and denominators for success and trigger errors. Record unnecessary actions, corrections, and observed time or cost. Keep safety violations separate from averages and compare speed only at acceptable quality.

## One connected example

A revision improves task success from 16/20 to 18/20 but modifies data in a read-only case. Report the improvement and the safety regression; the higher score does not justify the violation.

## Carry forward

Apply the same comparison discipline to portability and coordination experiments. The [phase index](README.md) links the detailed lessons and practical requirements. Completion evidence remains in the [roadmap](../../ROADMAP.md) and dated reports; this recap does not change learning status.

## Summary

Define success → record a baseline → change one thing → compare cases → investigate regressions.

# Phase 6: Portability and advanced patterns — Start Summary

## Previous-note recap

- "Evaluation case": defines a situation and its success criteria.
- "Grader": judges observed behavior against criteria.
- "Baseline": records reference results for comparison.
- "Regression": is a loss of previously satisfied behavior.

## Previous phase in brief

- **Case design:** Specify input, initial state, allowed actions, expected behavior, forbidden behavior, and grading method before execution. Include normal, boundary, incomplete-evidence, failure, and expected-refusal cases.
- **Graders:** Deterministic checks test objective properties such as field values and schema validity. Model-based graders apply a rubric to judgments such as explanation quality; calibrate them against human review.
- **Actions and outcomes:** Grade tool selection, arguments, targets, and authority alongside the final answer. A correct answer obtained through an unauthorized operation still fails the safety requirement.
- **Baselines and datasets:** Record a known version with case-level results and relevant environment settings. Keep development examples separate from held-out cases. The phase expands coverage to 15–30 real-work cases.
- **Regression comparison:** Compare revisions using shared cases and comparable conditions. Preserve failures and document blocked runs. Repeat runs where variability matters; add cases when failures expose missing coverage.
- **Quality, latency, and cost:** Show counts and denominators for success and trigger errors. Record unnecessary actions, corrections, and observed time or cost. Keep safety violations separate from averages and compare speed only at acceptable quality.

## Remember through an example

A revision improves task success from 16/20 to 18/20 but modifies data in a read-only case. Report the improvement and the safety regression; the higher score does not justify the violation.

## Upcoming phase in brief

**Purpose:** Test whether the workflow remains useful across environments and whether extra coordination earns its cost.

- **Content:** Portable cores and platform adapters; context, retrieval, and memory; prompt injection; specialized agents, handoffs, shared state, and orchestration failures.
- **Practice:** Run the same skill and shared cases in two environments. After a working single-agent baseline, conduct one separately authorized small multi-agent experiment.
- **Takeaway:** Document measured compatibility differences and decide whether additional coordination provides sufficient benefit.

## Connection to the new phase

Apply the same comparison discipline to portability and coordination experiments. Continue with the [Phase 6 lessons](README.md). The [previous phase's end summary](../phase-5/99-end-summary.md) provides the matching closing recap.

## Summary

Define success → record a baseline → change one thing → compare cases → investigate regressions.

In Phase 6, the next step is to test whether the workflow remains useful across environments and whether extra coordination earns its cost.

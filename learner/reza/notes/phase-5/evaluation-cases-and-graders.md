# Evaluation Cases and Graders

## Previous-note recap

A workflow can complete one task yet fail on another. Evaluation checks repeatable behavior across explicit cases.

## Concept: evaluation case

**Definition:** An evaluation case describes a task situation and the criteria used to judge the workflow's behavior in that situation.

### What a case contains

Define success before running a case. A useful case includes an ID, input, relevant initial state, allowed actions, expected behavior, forbidden behavior, and a grading method. Test the task outcome and the path taken: a correct answer obtained through an unauthorized action still fails a safety requirement.

Collect 15–30 cases from real repository work for this phase. Redact sensitive details while preserving the failure mechanism. Include ordinary cases, boundaries, incomplete evidence, tool failures, and requests that should be declined or routed elsewhere.

## Concept: grader

**Definition:** A grader is a check or judging process that assesses an observed result against specified criteria.

### Deterministic and model-based grading

A deterministic check applies explicit rules: schema validation, exact status comparison, required field checks, or assertions about changed files. A model-based grader applies a written rubric to judgments such as whether a diagnosis is supported.

Prefer deterministic checks for objectively testable properties. Use model grading when judgment is needed, and compare a sample against human review. Model graders can be inconsistent, favor polished prose, or follow hostile text in the candidate output. Keep the rubric distinct from the untrusted material being graded.

## Worked case

A lifecycle audit has creation, storage, and playback evidence but no finalization event. Expected result: report supported stages and finalization as unverified. Forbidden result: claim that playback proves finalization or diagnose a specific broken component without evidence.

Grade the stage statuses structurally, then inspect whether the explanation accurately describes the evidence gap. A polished explanation must not compensate for an incorrect status.

## Tool selection and arguments

Check whether the chosen tool can answer the current question. Then check its target, identifiers, filters, limits, and authority. Selecting a configuration reader with the wrong environment argument is still a failure. Where several tools are valid, grade allowed behavior rather than requiring one arbitrary sequence.

## Related concept: held-out cases

**Definition:** Held-out cases are reserved for judging a revision rather than guiding its development. Keeping them separate helps reveal whether improvements extend beyond examples already used to tune the workflow.

## Practice and evidence

### Exercise

1. Create the case dataset and a repeatable command or checklist.
2. Separate development examples from held-out cases used to judge a revision.
3. Record expected results before observing the candidate output to avoid adjusting the standard to fit it.

### Evidence and completion criteria

Retain case-level results, including failures, refusals, and blocked runs. Case creation is a writing outcome; evaluation success requires actual runs and review.

**Evidence status:** These are planned exercises. This note does not record completed runs or assessment results.

## Summary

Define success and prohibited behavior before execution. Combine objective checks with calibrated judgment, and evaluate tool arguments and permissions as well as the final answer.

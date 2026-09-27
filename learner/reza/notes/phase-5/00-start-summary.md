# Phase 5: Evaluations and reliability — Start Summary

## Previous-note recap

Read this in the first session of Phase 5. It is a brief review of **Phase 4: Build a single-agent workflow**, before starting the new material.

## Previous phase in brief

- **State and history:** History records messages; state tracks the current goal, authority, observations, hypotheses, actions, and unresolved questions. Keep evidence-backed facts separate from suspected causes.
- **Execution loop:** Choose a tool to answer a specific question, validate its arguments and permission, inspect its result, and update state. Set finite time and attempt limits; report a blocker when further action cannot help.
- **Guardrails:** Instructions guide behavior; technical controls enforce important limits. Use scoped paths, allowed tools, validation, and permission gates at the point of execution.
- **Output validation:** A correctly shaped report can still make an unsupported claim. Validate both its structure and whether the cited evidence supports each conclusion.
- **Observability and handoffs:** Record important actions, safe arguments, permission decisions, outcomes, and evidence references. Keep secrets out of traces. Handoffs need a clear goal, scope, evidence, expected output, and return condition.
- **Diagnosis and verification:** Establish a supported diagnosis before a bounded authorized fix. Inspect the final diff and run relevant final-code checks. Failed, blocked, and skipped checks remain visible in the report.

## Remember through an example

An agent edits a parser after its tests passed. Those earlier results describe the previous code; the final patch needs its own relevant verification.

## Upcoming phase in brief

**Purpose:** Measure whether a workflow is reliable and whether a revision improves it.

- **Content:** Task-level success criteria; deterministic and model-based graders; tool-selection and argument checks; baseline and regression datasets; quality, latency, and cost.
- **Practice:** Collect 15–30 cases from real work, record a baseline, and compare a revision using repeatable evaluations.
- **Takeaway:** Identify regressions and justify adoption or rejection using comparable results, with safety failures kept visible.

## Connection to the new phase

Use the observable workflow as the subject of repeatable evaluation. Continue with the [Phase 5 lessons](README.md). The [previous phase's end summary](../phase-4/99-end-summary.md) provides the matching closing recap.

## Summary

Observe → diagnose → act within authority → verify the final result → report evidence and uncertainty.

In Phase 5, the next step is to measure whether a workflow is reliable and whether a revision improves it.

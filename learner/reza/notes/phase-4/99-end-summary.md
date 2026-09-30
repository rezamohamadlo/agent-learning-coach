# Phase 4: Build a single-agent workflow — End Summary

## Previous-note recap

- "Agent state": records the current goal, evidence, and authority.
- "Execution loop": acts, inspects results, and updates state.
- "Guardrails": enforce permitted behavior.
- "Verification": checks the final result against requirements.

## Current phase recap

Read this in the last session of Phase 4 to review its content.

- **State and history:** History records messages; state tracks the current goal, authority, observations, hypotheses, actions, and unresolved questions. Keep evidence-backed facts separate from suspected causes.
- **Execution loop:** Choose a tool to answer a specific question, validate its arguments and permission, inspect its result, and update state. Set finite time and attempt limits; report a blocker when further action cannot help.
- **Guardrails:** Instructions guide behavior; technical controls enforce important limits. Use scoped paths, allowed tools, validation, and permission gates at the point of execution.
- **Output validation:** A correctly shaped report can still make an unsupported claim. Validate both its structure and whether the cited evidence supports each conclusion.
- **Observability and handoffs:** Record important actions, safe arguments, permission decisions, outcomes, and evidence references. Keep secrets out of traces. Handoffs need a clear goal, scope, evidence, expected output, and return condition.
- **Diagnosis and verification:** Establish a supported diagnosis before a bounded authorized fix. Inspect the final diff and run relevant final-code checks. Failed, blocked, and skipped checks remain visible in the report.

## One connected example

An agent edits a parser after its tests passed. Those earlier results describe the previous code; the final patch needs its own relevant verification.

## Carry forward

Use the observable workflow as the subject of repeatable evaluation. The [phase index](README.md) links the detailed lessons and practical requirements. Completion evidence remains in the [roadmap](../../ROADMAP.md) and dated reports; this recap does not change learning status.

## Summary

Observe → diagnose → act within authority → verify the final result → report evidence and uncertainty.

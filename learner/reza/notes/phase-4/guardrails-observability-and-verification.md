# Guardrails, Observability, and Verification

## Previous-note recap

The execution loop chooses actions from current state. Reliable automation also needs enforced boundaries and a reviewable record.

## Concept: guardrails

**Definition:** Guardrails are constraints and checks intended to keep a workflow within its permitted behavior.

### Application to the execution loop

Guardrails constrain behavior before or after a decision. Examples include allowed workspace roots, tool allowlists, argument validation, time limits, permission gates, and output checks. Instructions help guide choices, but technical controls should enforce critical boundaries.

## Concept: output validation

**Definition:** Output validation checks that a result meets its required format and content criteria.

Output validation has two layers: structure and support. A result can contain all required JSON fields while making an unsupported claim. Check that cited evidence exists and that the conclusion follows from it.

## Concept: observability

**Definition:** Observability is the ability to understand what happened in a workflow from the records it exposes.

### What to record

Record enough to reconstruct important actions: run ID, sequence or timestamp, selected operation, safe arguments, permission decision, status, duration, and evidence reference. Preserve failures as well as successes. Redact credentials and sensitive data; a full raw dump is not required for observability.

Record brief decision justifications and observable actions, not hidden internal reasoning. Logs should help a reviewer understand what happened and why the chosen check was relevant.

## Concept: verification

**Definition:** Verification checks whether the actual result satisfies the task requirements. For a code change, evidence must apply to the final code being accepted.

### Worked example

The agent proposes a parser fix. Its final report says tests passed, but the trace shows the passing run occurred before the edit. The report lacks final-code evidence. Run focused checks against the final patch, inspect their assertions and results, and report any remaining gaps.

A denied tool call should produce a visible blocked status. It should not disappear from the trace or silently trigger a more powerful fallback.

## Concept: handoff

**Definition:** A handoff transfers the task context and expected next step to another worker or human.

A handoff is useful when another role or a human has necessary expertise or authority. Include the goal, evidence, unresolved question, permitted scope, expected output, and return condition. A handoff does not expand permissions, and another agent's confident answer remains a claim to inspect.

Keep the first diagnostic workflow single-agent so its baseline can be understood before adding coordination.

## Practice and evidence

### Exercise

1. Complete an authorized diagnose–fix–verify run.
2. Capture the original failure, evidence-backed diagnosis, bounded patch, final diff, focused check results, and unresolved uncertainty.
3. Also run a controlled failure path and verify it appears in the final report.

### Evidence and completion criteria

A successful exit demonstration includes the full loop and an observable record of important actions. If checks cannot run, report the limitation and leave execution-dependent criteria incomplete.

**Evidence status:** These are planned exercises. This note does not record completed runs or assessment results.

## Summary

Enforce critical boundaries, validate both output structure and evidence, and record important actions safely. Verification must apply to the final change; blocked and failed paths must remain visible.

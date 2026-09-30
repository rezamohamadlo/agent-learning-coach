# Handoffs and Multi-Agent Evaluation

## Previous-note recap

- "Portable core": preserves workflow meaning across environments.
- "Adapter": handles measured environment-specific differences.
- "Prompt injection": is untrusted content that tries to redirect behavior.

## Concepts: "delegation", "handoff", and "coordination"

**"Delegation":** Assigning a bounded part of a task to another worker.

**"Handoff":** Transferring the goal, scope, evidence, and expected deliverable needed for another worker or human to continue.

**"Coordination":** Managing ownership, dependencies, shared information, and integration across workers.

### When multiple agents may help

Multiple agents can help when subtasks are separable, need different expertise, or benefit from independent review. They also add communication overhead, duplicate effort, and coordination failures. More agents do not automatically produce stronger evidence.

Before delegation, define who owns each output and who integrates it. A handoff should include the goal, bounded scope, relevant evidence, known uncertainty, allowed actions, expected deliverable, and return condition.

## Shared state and failure modes

| Failure | Practical control |
|---|---|
| Two agents overwrite the same file | Separate ownership or isolated workspaces and reviewed integration |
| A worker uses stale requirements | Version the task contract and communicate revisions |
| Both agents repeat the same search | Assign distinct questions and share evidence |
| Workers disagree | Compare sources and assumptions; do not vote on truth |
| A worker never returns | Set a deadline and report partial completion |
| A worker exceeds scope | Enforce the same authority boundaries at its tools |

The coordinating agent remains responsible for inspecting returned work. A worker's “done” message does not replace artifacts or verification results.

## Worked experiment design

For a small repository diagnosis, keep one agent as the baseline. In a separately authorized experiment, one worker could inspect implementation while another reviews acceptance coverage. They return findings and evidence without editing shared files. The coordinator reconciles the findings and performs authorized next steps.

Use the same cases, versions, and scoring as the baseline. Compare success, safety, latency, total usage or cost when available, unnecessary actions, integration effort, and manual corrections. Parallel wall-clock gains can coexist with greater total work.

## Practice and evidence

### Exercise

1. Attempt one small experiment only after the single-agent baseline works and the experiment is authorized.
2. Record the handoffs, returned artifacts, integration decisions, and final checks.
3. Explain whether the measurable benefit warrants the added coordination.

### Evidence and completion criteria

An evidence-backed rejection of the architecture is a valid experiment result; it does not establish that multi-agent complexity was justified. Keep that roadmap exit criterion open unless the evidence satisfies it or an explicit roadmap revision changes the requirement.

Finish with a phase-boundary and final roadmap review listing any unmet criteria. Reading this lesson is not permission to spawn agents.

**Evidence status:** These are planned exercises. This note does not record completed runs or assessment results.

## Summary

Delegate bounded work with clear ownership, shared authority limits, and reviewable evidence. Adopt extra coordination only when evaluation shows sufficient benefit over the single-agent baseline.

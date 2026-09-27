# Handoffs and Multi-Agent Evaluation

## Previous-note recap

A portable workflow preserves task meaning across environments. Additional agents should be judged against a working single-agent baseline.

## Essential mental model

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

Attempt one small experiment only after the single-agent baseline works and the experiment is authorized. Record the handoffs, returned artifacts, integration decisions, and final checks. Explain whether the measurable benefit warrants the added coordination.

An evidence-backed rejection of the architecture is a valid experiment result; it does not establish that multi-agent complexity was justified. Keep that roadmap exit criterion open unless the evidence satisfies it or an explicit roadmap revision changes the requirement.

Finish with a phase-boundary and final roadmap review listing any unmet criteria. Reading this lesson is not permission to spawn agents.

## Summary

Delegate bounded work with clear ownership, shared authority limits, and reviewable evidence. Adopt extra coordination only when evaluation shows sufficient benefit over the single-agent baseline.

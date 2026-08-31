# Agent Loop

## Mental model

An agent works through a feedback loop:

```text
Observe -> Reason -> Act -> Inspect -> Repeat or stop
```

1. **Observe:** Gather the request, constraints, current state, and relevant evidence.
2. **Reason:** Form or revise a hypothesis and choose the next safe, useful action.
3. **Act:** Perform that action through an available tool or produce the requested output.
4. **Inspect:** Examine the actual result instead of assuming the action succeeded.
5. **Repeat or stop:** Continue only when more evidence or work is required; otherwise report the outcome and limitations.

The stages are conceptual. Implementations may combine or rename them, but reliable agents still feed action results into later decisions.

## Model response versus agent workflow

A model can answer once using existing context. An agent wraps a model in a system that can gather information, use tools, observe results, and revise its next decision.

```text
Model response: request -> generated answer
Agent workflow: request -> decision -> action -> evidence -> revised decision -> result
```

The model supplies reasoning and choices. The agent system supplies instructions, state, tools, permissions, execution, and feedback.

## Stage outputs

| Stage | Useful output |
|---|---|
| Observe | Relevant facts, constraints, and unknowns |
| Reason | A hypothesis and next safe action |
| Act | A tool result or concrete artifact |
| Inspect | Evidence for or against the hypothesis |
| Repeat/stop | A revised action or supported final report |

Good reasoning does not require guessing the final answer immediately. It chooses actions that reduce uncertainty while respecting scope and risk.

## Stopping conditions

Stop when the acceptance criteria are satisfied, enough evidence supports the requested conclusion, the next action needs unavailable permission, required information cannot be obtained safely, or further attempts would repeat without producing new information.

Do not stop merely because a command exited successfully. Connect the observed result to the objective.

## Safety boundary

Every iteration must preserve authority and scope. A diagnostic request authorizes inspection, not an unrequested fix. Before a consequential action, identify its target, authorization, reversibility, verification method, and stopping condition.

## Self-check

- Why are Act and Inspect separate?
- How can an action test a hypothesis?
- What evidence justifies stopping?
- Which actions would exceed the user's authorization?


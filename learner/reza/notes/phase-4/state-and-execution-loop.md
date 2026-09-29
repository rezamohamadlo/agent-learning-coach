# Agent State and the Execution Loop

## Previous-note recap

Tools need validated contracts and bounded failure handling. A workflow coordinates those tools toward an evidence-based result.

## Concept: agent state

**Definition:** Agent state is the workflow's current working record of its goal, authority, evidence, progress, and unresolved questions.

### State versus conversation history

Conversation history records messages. Agent state records what the workflow currently knows and may do: objective, authorized scope, observations, hypotheses, completed actions, unresolved questions, and stopping conditions. History can contain stale or contradictory information; do not treat every earlier statement as current state.

Keep facts separate from hypotheses. “The test reports a missing key” is an observation. “The parser dropped that key” is a hypothesis until inspected. State should include source references so later decisions can recover the evidence.

## Concept: execution loop

**Definition:** An execution loop repeatedly chooses an action, inspects its result, and updates state until a stopping condition is met.

### A bounded diagnostic loop

```text
receive task -> validate scope -> collect evidence -> choose a check
     -> validate arguments and permission -> execute -> inspect result
     -> update state -> stop, report a blocker, or choose another check
```

Set practical limits on iterations, time, and repeated failures. These limits prevent endless investigation; reaching one requires an explicit partial report, not a success claim.

Tool selection should answer a question. Reading the failing assertion can distinguish an expected-value problem from a crash. Re-running the same failing command without a changed hypothesis usually adds little evidence.

## Worked example

An inventory test expects quantity 3 and receives 2. Read the fixture and update function. Suppose the fixture starts at 5 and requests removal of 3: the observed result may be correct and the test expectation stale. Check the product requirement before editing either. A failing assertion alone does not identify which side is wrong.

If diagnosis is all that was requested, report the supported finding. If a bounded fix is authorized, change only the relevant code or test and inspect the final diff.

## Practice and evidence

### Exercise

1. Create the roadmap's repository diagnostic agent starting with read-only investigation.
2. Define state fields and transitions before adding automatic edits.
3. Feed it one failing test or runtime error, capture the selected checks, and require each conclusion to cite evidence.

### Evidence and completion criteria

Exercise an unavailable file and a repeated failure. The agent should preserve unresolved questions and stop clearly instead of fabricating a diagnosis. These are proposed exercises, not completed runs.

**Evidence status:** These are planned exercises. This note does not record completed runs or assessment results.

## Summary

State tracks the current task, authority, facts, hypotheses, and uncertainty. Each loop step should answer a useful question and end in verified completion, a clear blocker, or a justified next action.

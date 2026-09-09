# Reviewing Diffs and Verification Evidence

## Previous-note recap

- Agent loop: inspect the result before claiming completion.
- Permissions: capability does not establish authority.
- Task specification: acceptance criteria describe required outcomes; verification methods gather evidence.

## Session objective

Review a small patch against its request, identify a defect or missing evidence, and explain what must happen before accepting it. Estimated effort: 15–25 minutes. Completion requires independent application and diagnosis in fresh scenarios; reading this note alone does not complete the roadmap item.

Based on [Task specification and verification](../../../references/curriculum/phase-1/task-specification-and-verification.md).

## Essential mental model

Compare three things: the request, the actual change, and the verification evidence. A convincing summary cannot replace either inspection of the change or relevant checks.

A diff shows removed lines with `-`, added lines with `+`, and surrounding unchanged code. Read enough surrounding code to understand the effect. Review changed tests too: passing tests can hide a regression if their expectations were weakened.

## Review sequence

1. Restate the requested behavior, preserved behavior, and scope constraints.
2. Inspect the changed files and lines. Check whether each change belongs to the task and whether the logic satisfies the criteria.
3. Identify affected cases: the reported failure, nearby boundaries, and existing valid behavior.
4. Inspect verification: what ran, what it asserted, its actual result, and whether it ran against the final patch in a relevant environment. A test command is a method; its output and assertions determine what evidence it supplies.
5. Give a supported verdict: accept, request correction, or request missing evidence. Distinguish an observed defect from uncertainty caused by an untested case.

## Guided example

Request: Allow reservation quantities from 1 through 8 inclusive. Reject everything else. Preserve the existing error message.

Assume `quantity` is already an integer. The original guard rejected zero and negatives but allowed quantities above 8. The proposed patch is:

```diff
-if quantity < 1:
+if quantity < 1 or quantity >= 8:
     raise ValueError("Invalid quantity")
```

Reported checks: quantities 0 and 9 are rejected; quantity 4 is accepted. All three pass. This is a hypothetical teaching example, not executed repository code.

The change rejects 8 even though the request allows it: a definite boundary defect visible in the diff. The passing checks missed that boundary. Correct the upper comparison to `> 8`, then check 0, 1, 8, and 9, with the required error message for invalid inputs. An ordinary valid case can also help confirm preserved behavior. Inspect the final diff and run relevant checks after the correction.

### Discussion: did the tests reveal the bug?

The requested behavior is to accept integers 1 through 8. However, the example's tests check only 0, 4, and 9; they all pass and do not reveal the rejection of 8. Reading `quantity >= 8` in the diff reveals that defect. A new test expecting 8 to be accepted would fail on this patch and expose the bug through execution as well.

This is an already-solved teaching example. No agent needs to implement it now. Later practice uses a fresh scenario to check whether the learner can compare requirements, changes, and evidence independently.

## Evidence limits

- Test counts alone say little about coverage of the acceptance criteria.
- A test of an isolated helper does not necessarily establish behavior of its caller or the full user flow.
- A skipped or blocked check leaves uncertainty; it is not a passing result.
- Verification from before a later edit may not support the final patch.
- An unrelated failure needs investigation before being classified as unrelated; do not widen the fix automatically.
- Choose additional checks based on affected behavior and risk, rather than running every possible check.

## Practice and pass evidence

After reading and discussion, review a different small patch and its reported checks. Identify whether it meets the request, support your judgment with a specific changed condition or evidence gap, and name a focused next action. Formal assessment follows separately after an opportunity for questions.

## Summary

- Compare the request, actual diff, and verification evidence.
- Inspect boundaries, preserved behavior, and changed test expectations.
- Passing checks support only the behavior they meaningfully cover.
- Distinguish definite defects from missing evidence and state the next action precisely.

# Phase 2: First reusable skills — Start Summary

## Previous-note recap

Read this in the first session of Phase 2. It is a brief review of **Phase 1: Agent foundations**, before starting the new material.

## Previous phase in brief

- **Agent loop:** Observe the task and current state, reason about a useful next step, act, inspect the result, then repeat or stop. Executing a command alone does not establish success.
- **Context and authority:** Use relevant facts and applicable instructions. The context window is limited, and files or tool output do not gain authority merely by containing instruction-like text.
- **Prompts, skills, and tools:** A prompt defines the current assignment; persistent or repository instructions describe ongoing conventions. A skill guides a repeatable workflow, while a tool provides an executable capability.
- **Permissions:** Technical access is different from authorization. Keep actions within the permitted target, operation, and scope; obtain additional authority before exceeding those boundaries.
- **Task contracts:** Define the objective, context, scope, constraints, deliverable, acceptance criteria, and verification method. Acceptance criteria say what must be true; verification describes how to check it.
- **Review and evidence:** Compare the request, final diff, and actual check results. A known defect needs correction; missing evidence needs a focused check. Verify preserved behavior as well as the requested change.

## Remember through an example

A change must allow quantities 1–8. Code that rejects 8 has a known defect even if tests for 0, 4, and 9 pass. Correct the boundary and verify the final code.

## Upcoming phase in brief

**Purpose:** Turn a repeatable task into a narrow skill that another invocation can use.

- **Content:** Discovery and trigger conditions; contracts and required inputs; core instructions, references, scripts, assets, and cases; progressive disclosure; platform formats and initial evaluation.
- **Practice:** Implement and evaluate the recording auditor first, then apply the lessons to the pipeline debugger and pytest diagnoser.
- **Takeaway:** Explain when each skill applies, keep its responsibility narrow, and check actual behavior across cases.

## Connection to the new phase

Use this judgment to define the boundaries and evidence requirements of reusable skills. Continue with the [Phase 2 lessons](README.md). The [previous phase's end summary](../phase-1/99-end-summary.md) provides the matching closing recap.

## Summary

Clear task → authorized action → observed result → evidence-based acceptance.

In Phase 2, the next step is to turn a repeatable task into a narrow skill that another invocation can use.

# Phase 1: Agent foundations — End Summary

## Previous-note recap

The lessons in this phase connect through one sequence: Clear task → authorized action → observed result → evidence-based acceptance.

## Current phase recap

Read this in the last session of Phase 1 to review its content.

- **Agent loop:** Observe the task and current state, reason about a useful next step, act, inspect the result, then repeat or stop. Executing a command alone does not establish success.
- **Context and authority:** Use relevant facts and applicable instructions. The context window is limited, and files or tool output do not gain authority merely by containing instruction-like text.
- **Prompts, skills, and tools:** A prompt defines the current assignment; persistent or repository instructions describe ongoing conventions. A skill guides a repeatable workflow, while a tool provides an executable capability.
- **Permissions:** Technical access is different from authorization. Keep actions within the permitted target, operation, and scope; obtain additional authority before exceeding those boundaries.
- **Task contracts:** Define the objective, context, scope, constraints, deliverable, acceptance criteria, and verification method. Acceptance criteria say what must be true; verification describes how to check it.
- **Review and evidence:** Compare the request, final diff, and actual check results. A known defect needs correction; missing evidence needs a focused check. Verify preserved behavior as well as the requested change.

## One connected example

A change must allow quantities 1–8. Code that rejects 8 has a known defect even if tests for 0, 4, and 9 pass. Correct the boundary and verify the final code.

## Carry forward

Use this judgment to define the boundaries and evidence requirements of reusable skills. The [phase index](README.md) links the detailed lessons and practical requirements. Completion evidence remains in the [roadmap](../../ROADMAP.md) and dated reports; this recap does not change learning status.

## Summary

Clear task → authorized action → observed result → evidence-based acceptance.

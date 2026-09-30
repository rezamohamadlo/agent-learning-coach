# Phase 2: First reusable skills — End Summary

## Previous-note recap

- "Triggering": matches a request to the right skill.
- "Skill contract": defines the skill's behavior and limits.
- "Progressive disclosure": loads supporting detail only when needed.
- "Evaluation": compares actual behavior with predefined criteria.

## Current phase recap

Read this in the last session of Phase 2 to review its content.

- **Discovery and triggering:** Names and descriptions help the agent decide whether a skill fits the user's intent. Positive conditions name the relevant outcome and inputs; exclusions distinguish nearby tasks. Test both missed matches and unwanted triggers.
- **Skill contracts:** Define purpose, scope, inputs, workflow, safety, expected output, and evaluation cases. A workflow gives repeatable decision rules, but written instructions do not guarantee identical model responses or grant permission.
- **Package roles:** Core instructions hold essential behavior and safety. References provide conditional detail, scripts perform deterministic operations, assets support produced outputs, and examples illustrate behavior.
- **Inputs and evaluation cases:** Required inputs support the current task. An evaluation case pairs sample input with expected behavior so results can be checked; that sample is not required on every ordinary run.
- **Progressive disclosure:** Load the core when the skill is selected and supporting detail when needed. State when to open each reference. Keep unconditional safety rules visible instead of hiding them in optional material.
- **Formats and first evaluations:** Check the target environment's package format, discovery, and permissions. A shared format does not establish portability. Execute normal, incomplete-evidence, and non-trigger cases; distinguish expected results from actual results.

## One connected example

A document checker takes today's document and checking rules as inputs. A sample with a deliberately missing date and the expected finding tests the checker; it is not a prerequisite for every document check.

## Carry forward

Use these contracts to design narrow, validated tools. The [phase index](README.md) links the detailed lessons and practical requirements. Completion evidence remains in the [roadmap](../../ROADMAP.md) and dated reports; this recap does not change learning status.

## Summary

Match the request → load the contract → use the relevant resources → evaluate actual behavior.

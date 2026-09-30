# Phase 3: Tools and MCP — Start Summary

## Previous-note recap

- "Triggering": matches a request to the right skill.
- "Skill contract": defines the skill's behavior and limits.
- "Package organization": places resources according to their roles.
- "Evaluation": checks actual behavior against predefined criteria.

## Previous phase in brief

- **Discovery and triggering:** Names and descriptions help the agent decide whether a skill fits the user's intent. Positive conditions name the relevant outcome and inputs; exclusions distinguish nearby tasks. Test both missed matches and unwanted triggers.
- **Skill contracts:** Define purpose, scope, inputs, workflow, safety, expected output, and evaluation cases. A workflow gives repeatable decision rules, but written instructions do not guarantee identical model responses or grant permission.
- **Package roles:** Core instructions hold essential behavior and safety. References provide conditional detail, scripts perform deterministic operations, assets support produced outputs, and examples illustrate behavior.
- **Inputs and evaluation cases:** Required inputs support the current task. An evaluation case pairs sample input with expected behavior so results can be checked; that sample is not required on every ordinary run.
- **Progressive disclosure:** Load the core when the skill is selected and supporting detail when needed. State when to open each reference. Keep unconditional safety rules visible instead of hiding them in optional material.
- **Formats and first evaluations:** Check the target environment's package format, discovery, and permissions. A shared format does not establish portability. Execute normal, incomplete-evidence, and non-trigger cases; distinguish expected results from actual results.

## Remember through an example

A document checker takes today's document and checking rules as inputs. A sample with a deliberately missing date and the expected finding tests the checker; it is not a prerequisite for every document check.

## Upcoming phase in brief

**Purpose:** Give workflows safe, callable capabilities with clear input and output contracts.

- **Content:** Tool calling and JSON Schema; read-only versus mutating operations; authorization; MCP hosts, clients, servers, resources, and tools; authentication, secrets, errors, retries, timeouts, and idempotency.
- **Practice:** Build configuration-inspection and test-summary tools, expose one safe diagnostic through MCP, and exercise invalid inputs and failure paths.
- **Takeaway:** Validate inputs and results, enforce authority, and handle uncertain outcomes without blindly retrying.

## Connection to the new phase

Use these contracts to design narrow, validated tools. Continue with the [Phase 3 lessons](README.md). The [previous phase's end summary](../phase-2/99-end-summary.md) provides the matching closing recap.

## Summary

Match the request → load the contract → use the relevant resources → evaluate actual behavior.

In Phase 3, the next step is to give workflows safe, callable capabilities with clear input and output contracts.

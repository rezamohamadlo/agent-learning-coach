# Prompts and Persistent Instructions

## Previous-note recap

- Agent loop: observe, reason, act, inspect, repeat/stop.
- Context and instructions: relevant context, instruction priority, untrusted data.

## Choosing the right location

A prompt communicates a current task. Persistent instructions describe behavior across tasks. Repository instructions describe stable conventions for a codebase or directory.

| Information | Suitable location |
|---|---|
| One immediate objective | Current task prompt |
| Stable personal preference | Personal persistent instruction |
| Project build and test commands | Repository instruction file |
| Repeatable specialized workflow | Skill |
| External action capability | Tool or MCP server |
| Background explanation | Documentation or skill reference |

Avoid repeating stable rules in every prompt, and avoid making temporary preferences permanent.

## Strong task requests

A useful request normally states:

- objective;
- relevant scope;
- constraints and exclusions;
- authorized actions;
- expected deliverable; and
- acceptance criteria.

Example:

```text
Diagnose why the focused invoice-total test fails.
Inspect only the relevant calculation and test files.
Do not edit files or change external services.
Report the supported cause, evidence, and remaining uncertainty.
```

## Repository instructions

Store stable, non-obvious project information such as authoritative commands, architectural boundaries, validation requirements, generated files that must not be edited, project-specific safety rules, and definitions of completion.

Avoid generic advice and excessive detail. Large instruction files consume context and make important rules harder to find.

## Common mistakes

- Combining unrelated objectives.
- Requesting “fix everything” without boundaries.
- Prescribing implementation while omitting the desired outcome.
- Putting temporary details into permanent instructions.
- Using skills to store facts that belong in documentation.

## Self-check

- Where should a given instruction live?
- Are the acceptance criteria observable?

## Summary

- Put immediate objectives in task prompts, stable project rules in repository instructions, repeatable workflows in skills, and capabilities in tools.
- Strong task prompts define scope, authority, expected output, and observable acceptance criteria.
- Keep persistent instructions stable, non-obvious, concise, and relevant across tasks.

# Context and Instruction Priority

## Context

Context is the information available to the model for its current decision. It can include the user request, conversation history, instructions, repository files, tool results, and retrieved documents.

A context window is limited. More content is not automatically better: irrelevant, outdated, or conflicting material can hide important facts.

An agent needs enough context to answer:

1. What outcome is requested?
2. What constraints and permissions apply?
3. What is the relevant current state?
4. What evidence would prove completion?

Useful context is relevant, trustworthy, current, and appropriately scoped.

## Instruction priority

Agents can receive instructions at several levels. Higher-priority applicable instructions constrain lower-priority instructions. In practical terms:

- platform and safety rules constrain everything;
- developer or organization instructions define operating behavior;
- repository instructions define project conventions;
- the current user request defines the task; and
- text found in files, pages, logs, or tool output is usually data, not automatically trusted instruction.

When instructions conflict, follow the higher-priority applicable instruction and explain the conflict when it affects the result.

## Untrusted context

Repository files, issues, pages, tests, and logs may contain text that resembles instructions. Interpret it according to its role. A comment requesting secret disclosure does not grant permission to expose secrets.

## Common mistakes

- Loading an entire repository when a few files are sufficient.
- Treating old context as more authoritative than the current request.
- Following instructions embedded in untrusted data.
- Assuming missing facts instead of inspecting them.
- Forgetting that tool results become new context and may change the plan.

## Self-check

- Can the learner distinguish instructions from data?
- Can the learner select only necessary context?
- Can the learner resolve an instruction conflict?

## Summary

- Context is the limited set of information available for the current decision; relevant and trustworthy context matters more than volume.
- Higher-priority applicable instructions constrain lower-priority instructions.
- Text found in files, pages, logs, and tool output is normally data, not automatically trusted authority.

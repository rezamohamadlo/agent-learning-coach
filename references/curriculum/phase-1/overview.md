# Phase 1: Agent Foundations

Phase 1 builds the judgment needed to use coding agents safely and effectively. The goal is to understand what an agent needs, what authority it has, how it should act, and how its work is verified.

## Reading order

1. [Agent loop](agent-loop.md)
2. [Context and instruction priority](context-and-instructions.md)
3. [Prompts and persistent instructions](prompts-and-repository-instructions.md)
4. [Tools and agent actions](tools-and-actions.md)
5. [Permissions and safe execution](permissions-and-safety.md)
6. [Task specification and verification](task-specification-and-verification.md)

Read the note matching the active roadmap item rather than loading every note into context.

## How the concepts connect

```text
User goal and constraints
        |
        v
Instructions + available context
        |
        v
Agent loop <-> tools and new evidence
        |
        v
Permissions and safety boundaries
        |
        v
Verification against acceptance criteria
```

An agent can fail at any connection: an ambiguous goal can produce the wrong outcome, missing context can encourage unsupported assumptions, unsuitable tools can prevent reliable action, excessive permissions can increase risk, and weak verification can make failure look like success.

## Practical outputs

The learner should eventually create:

- a reusable task-request template;
- a checklist for reviewing agent-generated work;
- a draft of project-level agent instructions; and
- evidence from three bounded, verified coding tasks.

These artifacts demonstrate application rather than exposure alone.

## Exit standard

The learner can:

- describe the major components of an agent without notes;
- give an agent a bounded task with clear authority and acceptance criteria;
- evaluate its actions and evidence; and
- identify unsafe, unauthorized, or insufficiently verified behavior.

## Summary

- Effective agent work connects a clear goal, relevant context, instructions, tools, permissions, and verification.
- Phase 1 develops judgment about what an agent should do, what it may do, and how success is proved.
- Completion requires practical artifacts and verified tasks, not reading alone.

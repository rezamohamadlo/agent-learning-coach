# Tools and Agent Actions

## Mental model

A language model generates decisions and text. Tools allow an agent to observe or change systems outside the model by reading files, running tests, querying APIs, searching documentation, or editing code.

A skill teaches a workflow. A tool provides a capability. An agent combines reasoning, instructions, context, and tools in an execution loop.

## Tool lifecycle

```text
Choose tool -> construct arguments -> obtain permission if needed
-> execute -> inspect result -> decide next step
```

A tool call is not successful merely because it ran. Inspect errors, partial output, unexpected state, and relevance to the objective.

## Reliable tool characteristics

- precise name and description;
- narrow, validated inputs;
- predictable, structured output;
- clear read-only or mutating behavior;
- useful errors;
- bounded execution and retries; and
- safe secret handling.

Prefer the least powerful tool that can obtain the required result.

## Tool, skill, and MCP

- **Tool:** A callable capability such as `run_test` or `read_camera_config`.
- **Skill:** Instructions and resources for a repeatable workflow.
- **MCP server:** A standard interface through which an agent discovers tools or resources from another system.

MCP does not make a tool trustworthy automatically. Authentication, permissions, validation, and approval policies still matter.

## Common mistakes

- Calling tools before understanding the request.
- Mutating state when read-only inspection is enough.
- Passing broad or unvalidated targets to destructive tools.
- Retrying without changing the hypothesis or inputs.
- Ignoring truncated output or failure status.

## Self-check

- Why is a skill different from a tool?
- Which tool is safest for a diagnostic task?
- What should be inspected after a tool call?


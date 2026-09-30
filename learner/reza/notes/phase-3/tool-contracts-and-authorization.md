# Tool Contracts and Authorization

## Previous-note recap

- "Skill": describes a reusable workflow.
- "Tool": provides a callable operation.
- "Boundary": limits inputs, effects, access, and results.

## Concept: "tool contract"

**Definition:** A "tool contract" specifies an operation's inputs, effects, access requirements, outputs, and possible failures.

### How a tool call uses the contract

A model's tool call is a request to execute an operation. The surrounding program validates its arguments, checks authority, invokes the implementation, and returns a result. A convincing description or well-formed argument object does not make an unsafe implementation safe.

## Concept: "JSON Schema"

**Definition:** "JSON Schema" describes the shape of JSON values: types, required fields, permitted values, and structural constraints. Runtime validation must also check meaning, such as whether a requested path belongs to the authorized workspace.

## Worked input contract

Illustrative input schema for a configuration inspector:

```json
{
  "type": "object",
  "properties": {
    "config_id": {"type": "string", "enum": ["development", "test"]},
    "include_disabled": {"type": "boolean"}
  },
  "required": ["config_id", "include_disabled"],
  "additionalProperties": false
}
```

A fixed ID maps to an approved configuration in application code. It avoids accepting arbitrary shell commands or unrestricted filesystem paths. The schema accepts an input's shape; the implementation still checks access, file availability, size, and parsing.

## Result contract

Use a result contract with separate status, findings, evidence, and limitations. For example, `status: "partial"` with a missing section must not be converted into a clean bill of health. Validate returned data before relying on it.

## Concepts: "effects" and "authorization"

**"Read-only operation":** Inspects information without changing the target data.

**"Mutating operation":** Changes state, such as editing a file or creating a record.

**"Authorization":** The permission to perform a particular action on a particular target.

### Apply the distinction

Reading a configuration does not authorize rewriting it. Running a test may create files or contact services, so classify the actual behavior rather than trusting the command's name. Even a read-only operation can expose private data or consume resources.

Before an external mutation, establish the exact target, intended effect, task authority, and any required approval. Enforce these boundaries in the application as well as instructions. Existing authorization can cover repeated actions within its scope; changes in target or impact require a fresh check.

## Practice and evidence

### Exercise

1. Design the roadmap's read-only DeepStream configuration inspector and test-result summarizer.
2. For each, specify inputs, result shape, possible side effects, and errors.
3. Use controlled fixtures for valid input, missing input, forbidden identifiers, malformed data, and tool failure.

### Evidence and completion criteria

Evidence should show rejected invalid inputs, validated structured output, and no unauthorized writes. Do not treat a tool's “read-only” label as proof; inspect implementation and observable effects.

**Evidence status:** These are planned exercises. This note does not record completed runs or assessment results.

## Summary

A tool contract covers inputs, effects, authority, and results. Structural validation and runtime checks complement each other; permissions must be enforced before execution.

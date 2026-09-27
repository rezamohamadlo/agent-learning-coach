# Tool Contracts and Authorization

## Previous-note recap

Skills describe workflows. Tools provide callable operations whose inputs, effects, and results need explicit boundaries.

## Essential mental model

A model's tool call is a request to execute an operation. The surrounding program validates its arguments, checks authority, invokes the implementation, and returns a result. A convincing description or well-formed argument object does not make an unsafe implementation safe.

JSON Schema describes the shape of JSON values: types, required fields, permitted values, and structural constraints. Runtime validation must also check meaning, such as whether a requested path belongs to the authorized workspace.

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

Use a result contract with separate status, findings, evidence, and limitations. For example, `status: "partial"` with a missing section must not be converted into a clean bill of health. Validate returned data before relying on it.

## Read-only versus mutating

Reading a configuration does not authorize rewriting it. Running a test may create files or contact services, so classify the actual behavior rather than trusting the command's name. Even a read-only operation can expose private data or consume resources.

Before an external mutation, establish the exact target, intended effect, task authority, and any required approval. Enforce these boundaries in the application as well as instructions. Existing authorization can cover repeated actions within its scope; changes in target or impact require a fresh check.

## Practice and evidence

Design the roadmap's read-only DeepStream configuration inspector and test-result summarizer. For each, specify inputs, result shape, possible side effects, and errors. Use controlled fixtures for valid input, missing input, forbidden identifiers, malformed data, and tool failure.

Evidence should show rejected invalid inputs, validated structured output, and no unauthorized writes. Do not treat a tool's “read-only” label as proof; inspect implementation and observable effects.

## Summary

A tool contract covers inputs, effects, authority, and results. Structural validation and runtime checks complement each other; permissions must be enforced before execution.

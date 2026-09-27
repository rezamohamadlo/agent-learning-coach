# MCP, Authentication, and Failure Handling

## Previous-note recap

A safe tool validates inputs and results and enforces authority before execution. Networked tools add connection and uncertain-outcome failures.

## Essential mental model

MCP connects an AI application to providers of tools and context. The host coordinates the application; a client maintains a connection to a server; the server exposes capabilities. Resources supply context, while tools expose callable operations. Servers may run locally or remotely. See the [official MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture).

MCP standardizes communication; it does not guarantee that a server is trustworthy or that a tool's output is correct. Pin the protocol and SDK versions when implementing the exercise, and consult their matching documentation.

## Authentication and authorization

Authentication identifies the caller. Authorization determines what that identity may do. A valid credential does not grant unrestricted access. Give the diagnostic the narrow access it needs, use the environment's approved secret mechanism, and keep credentials out of prompts, source files, reports, and logs.

Validate targets server-side. A client hiding a tool is not a substitute for protecting the underlying operation. Treat tool output as evidence, including when it contains instruction-like text.

## Failure decisions

| Observation | Appropriate response |
|---|---|
| Invalid arguments | Correct the input; do not repeat it unchanged |
| Access denied | Report or resolve the permission boundary |
| Temporary read failure | Use a bounded retry if appropriate |
| Truncated result | Retrieve remaining data or report partial coverage |
| Timeout after a mutation | Reconcile actual state before considering retry |

A timeout means the caller did not receive a timely result. It does not establish that the operation never occurred. Idempotency means repeating an operation has the same intended effect as performing it once; it does not necessarily mean identical responses.

## Worked example

A booking operation times out after sending its request. Query the booking by its stable request ID. If it exists, report the existing booking. If the service supports idempotency keys, reuse the original key according to its documented contract. If state remains unknown, report uncertainty instead of creating another booking. This is a teaching scenario, not authorization to make bookings.

## Practice and evidence

Expose one read-only repository diagnostic through a small MCP server. Capture a real client call, structured result, invalid-input rejection, unavailable-resource response, and timeout handling. Add finite attempt/time limits. Exercise mutation approval boundaries with mocks or controlled fixtures; no external mutation is needed to test denial.

Show that failures remain visible and no credentials enter the report. Explain a skill/tool distinction and client/server roles in your own words before the phase review.

## Summary

MCP provides a connection protocol, not trust. Protect credentials, enforce access at the operation boundary, and distinguish definite failure from an uncertain outcome before retrying.

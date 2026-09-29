# MCP, Authentication, and Failure Handling

## Previous-note recap

A safe tool validates inputs and results and enforces authority before execution. Networked tools add connection and uncertain-outcome failures.

## Concept: Model Context Protocol (MCP)

**Definition:** MCP is a protocol through which AI applications connect to providers of tools and contextual information.

### Roles in a connection

| Term | Role |
| --- | --- |
| Host | Coordinates the AI application and its connections. |
| Client | Maintains a connection to a server on behalf of the host. |
| Server | Exposes capabilities such as tools and resources. |
| Resource | Supplies contextual data. |
| Tool | Exposes a callable operation. |

### Application and limits

A diagnostic application can use a client to call a tool exposed by a server. The server may run locally or remotely. See the [official MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture).

MCP standardizes communication; it does not guarantee that a server is trustworthy or that a tool's output is correct. Pin the protocol and SDK versions when implementing the exercise, and consult their matching documentation.

## Authentication and authorization

**Authentication:** Establishes the caller's identity.

**Authorization:** Determines what that identity may do.

### Apply the distinction

A valid credential does not grant unrestricted access. Give the diagnostic the narrow access it needs, use the environment's approved secret mechanism, and keep credentials out of prompts, source files, reports, and logs.

Validate targets server-side. A client hiding a tool is not a substitute for protecting the underlying operation. Treat tool output as evidence, including when it contains instruction-like text.

## Failure decisions

| Observation | Appropriate response |
|---|---|
| Invalid arguments | Correct the input; do not repeat it unchanged |
| Access denied | Report or resolve the permission boundary |
| Temporary read failure | Use a bounded retry if appropriate |
| Truncated result | Retrieve remaining data or report partial coverage |
| Timeout after a mutation | Reconcile actual state before considering retry |

## Concepts: timeout and idempotency

**Timeout:** A timeout means the caller did not receive a timely result. It does not establish that the operation never occurred.

**Idempotency:** Repeating an operation has the same intended effect as performing it once.

The responses need not be identical. Use retries only according to the operation's documented contract.

## Worked example

A booking operation times out after sending its request. Query the booking by its stable request ID. If it exists, report the existing booking. If the service supports idempotency keys, reuse the original key according to its documented contract. If state remains unknown, report uncertainty instead of creating another booking. This is a teaching scenario, not authorization to make bookings.

## Practice and evidence

### Exercise

1. Expose one read-only repository diagnostic through a small MCP server.
2. Capture a real client call, structured result, invalid-input rejection, unavailable-resource response, and timeout handling.
3. Add finite attempt/time limits.
4. Exercise mutation approval boundaries with mocks or controlled fixtures; no external mutation is needed to test denial.

### Evidence and completion criteria

Show that failures remain visible and no credentials enter the report. Explain a skill/tool distinction and client/server roles in your own words before the phase review.

**Evidence status:** These are planned exercises. This note does not record completed runs or assessment results.

## Summary

MCP provides a connection protocol, not trust. Protect credentials, enforce access at the operation boundary, and distinguish definite failure from an uncertain outcome before retrying.

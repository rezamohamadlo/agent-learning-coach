# Phase 4: Build a single-agent workflow — Start Summary

## Previous-note recap

Read this in the first session of Phase 4. It is a brief review of **Phase 3: Tools and MCP**, before starting the new material.

## Previous phase in brief

- **Tool calling and schemas:** A model requests an operation; the surrounding application validates and executes it. JSON Schema checks input structure. Runtime checks must also establish meaning, valid targets, and authorized access.
- **Structured results:** Return status, findings, evidence, and limitations in a predictable form. Validate outputs and distinguish successful, partial, and failed results before making a task-level claim.
- **Effects and authorization:** Classify actual behavior, not tool names. A test may write files or contact services. Enforce permission boundaries before mutations; read-only access can still expose private information.
- **MCP roles:** The host coordinates the application, a client connects to a server, and the server supplies capabilities. Resources provide context; tools expose operations. A standard connection protocol does not establish trust.
- **Authentication and secrets:** Authentication identifies the caller; authorization limits what that identity may do. Use narrowly scoped access and approved secret storage, and keep credentials out of prompts, source, and logs.
- **Errors and retries:** Invalid input needs correction; access denial needs a permission decision; temporary failures may justify bounded retries. A mutation timeout leaves its outcome uncertain. Reconcile state first; idempotency means repeats preserve the same intended effect.

## Remember through an example

A booking request times out. Check the booking using its request identifier before retrying: the booking may exist even though its confirmation was lost.

## Upcoming phase in brief

**Purpose:** Connect tools into a complete, observable diagnosis and verification loop.

- **Content:** Agent state and conversation history; tool selection and execution loops; guardrails and output validation; logs and traces; useful handoffs.
- **Practice:** Build a repository diagnostic agent that gathers evidence, reports a supported diagnosis, and applies and verifies a bounded fix when authorized.
- **Takeaway:** Trace important actions and explain both successful results and failures from observable evidence.

## Connection to the new phase

Connect these tools into a bounded, observable single-agent loop. Continue with the [Phase 4 lessons](README.md). The [previous phase's end summary](../phase-3/99-end-summary.md) provides the matching closing recap.

## Summary

Validate input and authority → execute a bounded operation → validate the result → reconcile uncertainty.

In Phase 4, the next step is to connect tools into a complete, observable diagnosis and verification loop.

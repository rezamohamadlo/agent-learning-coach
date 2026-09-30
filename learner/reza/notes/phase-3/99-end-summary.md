# Phase 3: Tools and MCP — End Summary

## Previous-note recap

- "Tool contract": defines a callable operation and its boundaries.
- "Authorization": limits what the caller may do.
- "Result validation": checks returned data before relying on it.
- "Reconciliation": checks actual state after an uncertain outcome.

## Current phase recap

Read this in the last session of Phase 3 to review its content.

- **Tool calling and schemas:** A model requests an operation; the surrounding application validates and executes it. JSON Schema checks input structure. Runtime checks must also establish meaning, valid targets, and authorized access.
- **Structured results:** Return status, findings, evidence, and limitations in a predictable form. Validate outputs and distinguish successful, partial, and failed results before making a task-level claim.
- **Effects and authorization:** Classify actual behavior, not tool names. A test may write files or contact services. Enforce permission boundaries before mutations; read-only access can still expose private information.
- **MCP roles:** The host coordinates the application, a client connects to a server, and the server supplies capabilities. Resources provide context; tools expose operations. A standard connection protocol does not establish trust.
- **Authentication and secrets:** Authentication identifies the caller; authorization limits what that identity may do. Use narrowly scoped access and approved secret storage, and keep credentials out of prompts, source, and logs.
- **Errors and retries:** Invalid input needs correction; access denial needs a permission decision; temporary failures may justify bounded retries. A mutation timeout leaves its outcome uncertain. Reconcile state first; idempotency means repeats preserve the same intended effect.

## One connected example

A booking request times out. Check the booking using its request identifier before retrying: the booking may exist even though its confirmation was lost.

## Carry forward

Connect these tools into a bounded, observable single-agent loop. The [phase index](README.md) links the detailed lessons and practical requirements. Completion evidence remains in the [roadmap](../../ROADMAP.md) and dated reports; this recap does not change learning status.

## Summary

Validate input and authority → execute a bounded operation → validate the result → reconcile uncertainty.

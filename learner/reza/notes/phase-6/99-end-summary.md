# Phase 6: Portability and advanced patterns — End Summary

## Previous-note recap

- "Portable core": preserves workflow meaning across environments.
- "Adapter": handles measured platform differences.
- "Prompt injection": is untrusted content that tries to redirect behavior.
- "Coordination": manages work and evidence across workers.

## Current phase recap

Read this in the last session of Phase 6 to review its content.

- **Portable core and adapters:** Keep purpose, decision rules, safety, and evidence standards in a shared core. Use thin adapters for measured differences in discovery, tools, paths, or permissions rather than duplicating the workflow.
- **Cross-environment evaluation:** Run the same skill and shared cases in both target environments. Record versions, capabilities, permission differences, trigger behavior, task success, unnecessary actions, and manual corrections.
- **Context, retrieval, and memory:** Context holds information for the current decision; retrieval obtains relevant material; memory retains information across interactions. Check source, scope, and freshness instead of assuming remembered or retrieved facts are correct.
- **Prompt injection:** Untrusted content can try to redirect behavior. Keep it separate from trusted instructions, restrict tool authority, and check proposed actions against the user's task. A retrieved command does not create permission.
- **Delegation and shared state:** Use bounded subtasks, clear ownership, and explicit handoffs. Manage stale requirements, conflicting edits, duplicated work, missing results, and disagreement by inspecting evidence and integrating outputs.
- **Measured complexity:** Compare a separately authorized multi-agent experiment against a working single-agent baseline. Include success, safety, total effort, latency, and integration cost. Rejecting extra complexity can be a sound result without satisfying a criterion that requires demonstrated benefit.

## One connected example

Two workers inspect implementation and test coverage separately. Their reports must include evidence, and the coordinator must reconcile them; two confident conclusions do not substitute for a verified result.

## Carry forward

Use the final roadmap review to identify remaining gaps and choose improvements from observed failures. The [phase index](README.md) links the detailed lessons and practical requirements. Completion evidence remains in the [roadmap](../../ROADMAP.md) and dated reports; this recap does not change learning status.

## Summary

Preserve workflow meaning → measure environment differences → protect authority → justify coordination with evidence.

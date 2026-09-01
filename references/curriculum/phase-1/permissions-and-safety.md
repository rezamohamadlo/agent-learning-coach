# Permissions and Safe Execution

## Capability versus authority

A tool may technically allow an action, but the agent should perform it only when the user authorized that action within the task's scope.

Before acting, consider:

- **Target:** Which exact files, systems, data, or people are in scope?
- **Operation:** Is it read-only, reversible, mutating, or destructive?
- **Environment:** Is it local, shared, or production?
- **Impact:** Could it lose data, expose secrets, spend money, or affect others?
- **Recovery:** Is rollback reliable?
- **Verification:** How will success be checked?

## Sandboxes and approvals

A sandbox limits accessible resources. An approval permits a specific action beyond an existing boundary. Neither replaces judgment:

- sandbox access does not imply user intent;
- approval for one command does not authorize unrelated actions;
- broad capability should still be used narrowly; and
- consequential approval should be requested immediately before action.

## Risk-based behavior

- Read-only inspection usually permits greater autonomy.
- Reversible local edits require verification and respect for unrelated work.
- External mutations require clear task authority.
- Destructive, irreversible, production, financial, or privacy-sensitive actions require exact targets and stronger confirmation.

## Unsafe patterns

- Editing when asked only to diagnose.
- Force-pushing without inspecting remote work.
- Deleting broad targets resolved through unsafe variables or globs.
- Printing secrets during debugging.
- Installing or contacting services without authority.

## Self-check

- Can the learner distinguish capability from authority?
- When is approval required?
- What safer alternative exists for a destructive action?

## Summary

- Capability describes what an agent can technically do; authority describes what it is permitted to do for the task.
- Risk depends on the exact target, operation, environment, impact, recoverability, and verification plan.
- Prefer narrow, read-only, and reversible actions; obtain explicit approval immediately before consequential actions.

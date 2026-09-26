# Skill Contract Authoring

## Previous-note recap

Skill discovery and triggering: lightweight metadata helps match a request; full instructions load only after a strong match.

## Contract versus detailed instructions

A skill contract states the boundary of the skill clearly enough to plan, trigger, evaluate, and use it. Its `Required inputs` section declares the evidence the workflow needs, such as an identifier, event records, timestamps, event types, and expected lifecycle rules.

The contract is normally expressed in the skill's instruction file through explicit sections such as purpose, scope, trigger and non-trigger conditions, inputs, workflow, safety constraints, output format, and evaluation examples. It can first be drafted as a separate design artifact, but the finished skill should preserve those rules in its instructions. Lightweight metadata may summarize the trigger, while the full contract belongs in the loaded skill instructions.

## Typical instruction structure

Many skill packages use a Markdown instruction file with lightweight metadata at the top, followed by the operating contract and workflow. A portable outline is:

1. Metadata: name and short description for discovery.
2. Purpose and scope.
3. Use-when and do-not-use-when conditions.
4. Required inputs and assumptions.
5. Deterministic steps and decision points.
6. Safety, authorization, and stop conditions.
7. Expected output format.
8. Examples, edge cases, and evaluation cases.

Exact metadata syntax and package layout can vary between agent platforms, so platform-specific details should be checked before implementation.

The detailed instructions then explain how to validate those inputs, interpret them, perform the workflow, and report missing or contradictory evidence. Declaring an input does not mean the skill should invent it when it is absent.

For the fictional parcel skill (suggested name: `parcel-lifecycle-auditor`; learner's original name: `full-dispatch-del-check`), the learner has now defined the trace as packaging through delivery at the destination. This extends the earlier dispatch-to-delivery example to include packaging. A narrow request about only one lifecycle section is excluded by the current draft.

## Current purpose and scope draft

The learner specified tracking the full delivery path from packaging to arrival at the destination, then explicitly selected summarizing the journey and identifying missing, contradictory, or out-of-order events. Consolidated purpose and scope: “Trace and summarize a package's complete journey from packaging to delivery at its destination, identifying missing, contradictory, or out-of-order events.” Other contract sections still need consolidation and review; the contract is not complete.

## Where required inputs come from

Required inputs are information the skill needs, not necessarily fields the user must type. They may be supplied by the user or obtained from allowed context. The instructions should explain how to validate them and what to do when evidence is missing, without inventing missing records or lifecycle rules.

## Required-input draft and feedback

The learner proposed identifying the lifecycle, an example of a broken lifecycle, and a report about a lifecycle problem. “Identifying the lifecycle” needs clarification: expected stages describe the process, while a package identifier selects the specific journey. Tracing that journey also needs its actual event records. A broken-lifecycle example is useful as teaching or evaluation material but is not required for every use. A supplied problem report can provide optional investigation context; a report produced by the skill belongs under outputs. Requiring a known problem would unnecessarily exclude healthy journeys from a full-path trace.

The learner confirmed the input clarification and subsequently chose to include problem detection. Consolidated required inputs: package identifier; actual event records including event types and timestamps; expected lifecycle stages and ordering rules. An existing problem report is optional context. These are reviewed, coached contract sections, not evidence of an implemented or evaluated skill.

## What a workflow means

A workflow is the ordered set of actions and decision rules the skill follows to turn its inputs into its output. Inputs describe what is available; workflow describes what to do with it; output describes the result. Teach this concept before asking the learner to draft steps; the learner noted that workflow had not yet been explained.

For the fictional parcel audit, a coach-provided example is:

1. Validate the package identifier, event records, and expected lifecycle rules. Ask for missing required evidence or state the limitation.
2. Select records belonging to that package.
3. Reconstruct the recorded journey using timestamps and any supplied ordering rules. Flag ambiguous or conflicting records rather than silently resolving them.
4. Compare the recorded journey with the supplied lifecycle rules to identify missing, contradictory, or out-of-order events. Distinguish an absent record from proof that a real-world stage never occurred, and account for a journey still in progress.
5. Summarize the journey and findings with supporting records and uncertainties. Leave source records unchanged.

“Deterministic workflow” means explicit, repeatable steps and decision criteria here; written instructions alone do not guarantee identical model responses. This example is teaching material, not an independently authored learner workflow.

## Safety constraints are boundaries, not workflow steps

A workflow says what the skill does in order. A safety constraint says what it must not do, what authority it requires, or when it must stop. For a recording audit, examples include inspecting files without modifying or deleting them and avoiding disclosure of credentials, sensitive paths, or video contents in the report. The learner's current task is to write two such `must not` rules; implementation details are not required yet.

The learner authored two constraints for the recording audit: do not delete or modify recordings, and do not expose paths in reports. The second is best applied as “do not expose full sensitive paths”; when evidence identification is necessary, report a recording ID, filename, redacted path, or safe relative path instead.

## Evidence must remain stage-specific

Creation, finalization, storage, and playability are separate claims. Evidence for a later stage can coexist with missing evidence for an earlier one, but it does not replace that evidence. For example, a file that exists and plays supports storage and playability; without a finalization event, finalization remains unknown or unverified. Missing evidence is not proof of a specific defect, so the report should recommend investigation without claiming that an identifier or event producer is broken.

## Summary

The contract says what the skill needs and where it applies; detailed instructions say how to use and validate those inputs. Required inputs are evidence requirements, not permission to guess missing data. A workflow connects those inputs to the output through explicit steps and decision rules. Safety constraints define prohibited actions, required authority, and stop conditions rather than adding more processing steps.

# Skill Package Organization

## Previous-note recap

Skill discovery: metadata helps select a skill. Skill contract: loaded instructions define scope, inputs, workflow, safety, output, and evaluation boundaries.

## Organize by runtime role

Put material where its role is clearest, not where its file extension happens to fit:

- **Core instructions:** the short operating contract the agent needs whenever the skill runs. Include purpose, boundaries, required inputs, main workflow, safety rules, and output expectations.
- **References:** detailed knowledge the agent reads only when relevant, such as schemas, field definitions, platform notes, or troubleshooting tables.
- **Scripts:** deterministic executable operations, such as parsing structured logs, validating fields, or running a repeatable media probe.
- **Assets:** files used to produce or package an output rather than instructions to reason over, such as report templates, images, or starter configuration files.
- **Examples and evaluation cases:** sample inputs and expected behavior used for teaching, testing, regression checks, and boundary validation.

An item can contain text and still not be an instruction. A report template is an asset; a schema explanation is a reference; an input plus expected result is an evaluation case.

### Required inputs versus evaluation cases

Required inputs are the information needed to perform the current task. For a document-checking skill, this might be the document to inspect and the checking rules. The core declares these requirements; the actual document is supplied for that invocation or obtained from authorized context.

An evaluation case pairs a sample input with expected behavior so the skill's actual result can be checked. For example, a sample document deliberately missing a date is paired with the expected finding “Required date is missing.” This pair tests whether the skill detects the omission.

The sample becomes an input when running that evaluation, but it is not required for every ordinary document check. Classify the pair by its purpose: testing behavior. A worked example can teach the same distinction without being an executed evaluation.

## Keep the core small but sufficient

Core instructions should contain rules needed on every run. Moving a necessary safety boundary or decision rule into an optional reference can make behavior unreliable. Conversely, copying long platform documentation or many examples into the core wastes context on runs that do not need them.

A useful test is: **Does the agent need this on nearly every invocation to act correctly and safely?** If yes, keep it in the core. If it is conditional detail, place it in a named supporting file and tell the core instructions when to read it.

## Recording-auditor examples

- The rule “never modify or delete recordings” belongs in core instructions.
- A table describing every lifecycle event field belongs in a reference.
- A repeatable command or program that checks whether a media file can be decoded belongs in scripts.
- A reusable Markdown report layout belongs in assets.
- The successful, corrupted, and missing-finalization scenarios belong in evaluation cases.

## Validation scope

Validation covers classification by runtime role, application to a new skill package, and diagnosis of a placement decision that harms safety or context use.

## Pass evidence

Correctly classify familiar items, apply the distinction to a new scenario, and diagnose at least one harmful placement decision without relying on filename alone.

## Assessment record — 1405-07-05

Package organization is Demonstrated after a 2/3 valid round, targeted clarification, and 3/3 fresh reassessment. The earlier answer-leaked round was discarded as a coach error. The corrected gap was required inputs versus evaluation cases; recheck it during the first skill evaluation. No implemented package or delayed retention is claimed. See the [session report](../../reports/1405-07-05-skill-package-organization.md).

## Summary

Core instructions hold always-needed behavior and safety rules. References hold conditional knowledge, scripts perform deterministic operations, assets support produced outputs, and examples/evaluation cases test or illustrate behavior. Required inputs support the current task; an evaluation case pairs a sample input with expected behavior to check the skill. Classify material by its runtime role, and make optional resources discoverable from the core.

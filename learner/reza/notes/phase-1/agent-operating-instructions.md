# Project-Independent Agent Operating Instructions

## Previous-note recap

Task contracts bound the work; review compares requirements, changes, and evidence. Operating instructions turn these principles into reusable guidance.

## Build 3 practice draft

Learner-authored operating rules:

- Inspect the existing structure of APIs, serializers, and models before editing.
- Follow the project's templates and architecture.
- Change only necessary files; do not change unrelated files.
- If other changes seem necessary, explain them and ask for permission before making them.
- Add tests for new changes and report their actual results.
- Examine the whole final change precisely before reporting completion.
- Report failed tests exactly, along with passed, skipped, or unavailable checks.
- If there is uncertainty, a problem, or a better solution, explain it instead of silently proceeding.
- Report all changes made.

## Refined guidance for reuse

Preserve the learner-authored draft above as history. When reusing it, require relevant checks proportional to the change: add or update tests when needed to cover behavior, rather than adding a test for every edit. Existing coverage can be sufficient for a low-impact change. Report actual results against the final version and disclose blocked checks.

Scope expansion requires receiving the necessary authorization; merely asking is not approval. Existing authorization remains valid within its stated limits.

## Review feedback

The final draft establishes repository inspection, architectural consistency, minimal scope, an approval boundary for scope expansion, final-change inspection, focused testing, precise result reporting, and escalation of uncertainty. It is reusable without depending on a particular project.

## Summary

Reusable agent instructions should require inspection before editing, minimal authorized scope, approval for scope expansion, convention preservation, focused tests, final-change verification, exact reporting of all check outcomes, and escalation of uncertainty.

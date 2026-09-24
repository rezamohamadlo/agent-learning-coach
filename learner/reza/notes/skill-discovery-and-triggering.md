# Skill Discovery and Triggering

## Previous-note recap

Agent loop: observe, reason, act, inspect, repeat or stop. A skill provides reusable workflow guidance; a tool provides a capability to act.

## Concept

Skill discovery is how an agent learns that a skill exists and what kind of requests it covers. Triggering is the decision to load or apply that skill to the current request.

## Why it matters now

A useful skill must activate for relevant requests and stay inactive for unrelated ones. If it rarely triggers, its knowledge is unavailable when needed. If it triggers too broadly, it wastes context and can apply the wrong workflow.

## Essential mental model

Think of discovery and triggering as a two-stage filter:

1. **Discovery:** The agent sees lightweight metadata, usually a skill name and description. It does not need the full instructions yet.
2. **Trigger decision:** The agent compares the user's intent and task context with that metadata.
3. **Loading:** If the match is strong, the agent reads the full skill instructions and any relevant supporting material.
4. **Execution:** The agent follows the workflow while still obeying higher-priority instructions, scope, and authorization limits.

A trigger should describe the task's meaning, not only exact keywords. A user may request "find why this test fails" without saying `pytest-failure-diagnoser`.

You can picture discovery as a quick scan of the available skills' names and short descriptions, not a read of every full instruction file. The trigger decision is the separate judgment about whether one of those descriptions matches this request. A misleading name or description can cause a relevant skill to be missed (false negative) or an irrelevant skill to be selected (false positive). The description usually carries more detail than the name; a clear name helps, but an exact name match is not required. Actual discovery behavior can vary by agent platform, so this is a mental model rather than a guarantee about its internal algorithm.

## `Use when` conditions

Positive conditions describe requests the skill is designed to handle. Strong conditions name observable task features:

- the user's intended outcome;
- the kind of input or artifact involved;
- the workflow or decision the skill supports; and
- important variants of the same intent.

Example:

> Use when the user wants to reproduce, classify, diagnose, or summarize a focused pytest failure from test output or a repository.

This is stronger than "use for Python" because it identifies a narrow outcome and relevant evidence.

## `Do not use when` conditions

Negative conditions define nearby requests that may look similar but need a different workflow. They prevent false triggers and clarify responsibility.

Example:

> Do not use for general Python tutoring, implementing an unrelated feature, or diagnosing a production service that has no pytest failure evidence.

Good exclusions focus on realistic neighboring tasks, not every imaginable unrelated request.

## Trigger quality

There are two important failure modes:

- **False negative:** A relevant request does not trigger the skill. The description may be too narrow, depend on exact words, or omit a common variant.
- **False positive:** An unrelated request triggers the skill. The description may be too broad or lack useful exclusions.

Trigger quality must therefore be evaluated with both positive cases and negative cases.

## Common mistake

Writing only a purpose statement such as "helps with testing." This does not tell the agent which testing requests belong to the skill or which similar requests do not.

Another mistake is putting essential trigger information only inside the full instructions. The agent often needs the lightweight description to decide whether to load those instructions, so hidden trigger rules may never be seen.

## Small example

Skill: `invoice-data-extractor`

- **Use when:** The user wants structured fields extracted from invoice documents, including supplier, invoice number, dates, line items, tax, and totals.
- **Do not use when:** The user wants accounting advice, payment authorization, or extraction from documents that are not invoices.

Cases:

1. "Turn these supplier invoices into a CSV." - should trigger.
2. "What expenses can my company deduct?" - should not trigger.
3. "Extract text from these employment contracts." - should not trigger this skill, even though extraction is involved.

## Practice prompt

Given a proposed skill and several requests, decide which requests should trigger it. Then explain which phrase in the positive or negative conditions supports each decision.

## Guided practice: meeting action extraction

On 1405-07-02 (Jalali), the learner revised a trigger to name extraction of tasks, owners, or deadlines, and correctly distinguished a request for tasks from notes from a request for attendance count and meeting date. This is guided practice; independent authoring remains pending.

The remaining wording adjustment is to name the input: meeting notes or transcripts. A task deadline is different from the date of the meeting. Exclusions should name concrete neighboring requests rather than referring vaguely to "other details."

Refined example with coach support:

- **Use when:** The user wants explicitly stated action items, their owners, or their deadlines extracted from meeting notes or transcripts.
- **Do not use when:** The user only wants meeting metadata, such as attendance count or meeting date, or a general discussion summary without action-item extraction.

For a mixed request, the skill can cover the action-item extraction portion; its scope does not automatically cover the other requested details. Missing owners or deadlines remain unspecified.

## Guided practice: customer feedback summaries

On 1405-07-02 (Jalali), the learner independently named categorizing customer reviews and summarizing each category as an appropriate trigger. The initial exclusion, requests for review "types" and counts per type, could overlap with grouping reviews by theme. After feedback, the learner clarified the exclusion as requests only for counts or metadata such as date, time, or collection format (online or paper).

The revised exclusion is appropriate for this skill's stated scope. "Type" needs a concrete meaning: a feedback theme can belong to content analysis, while a collection format describes metadata. The word "only" matters: asking for counts alongside a theme summary does not exclude the summarization portion.

Consolidated conditions:

- **Use when:** The user wants supplied customer reviews grouped into themes and summarized by theme.
- **Do not use when:** The user only wants review counts or metadata, such as submission dates, times, or collection formats, without content grouping or summarization.

Evidence: positive-condition authoring was independent; the exclusion was corrected with coaching. The exercise is Practiced; a fresh independent authoring check remains before completing the roadmap target.

## Independent application: applicant filter

On 1405-07-02 (Jalali), the learner independently chose a skill that reads resumes and returns applicants matching a supplied requirements file. The positive example selected applicants meeting minimum requirements; the negative example requested aggregate statistics. This demonstrates trigger-condition authoring after guided practice. Earlier practice labels are historical; the independent checkpoint is now complete.

Coach refinements after assessment:

- Say "applicants who meet the stated requirements" rather than "legitimate applicants."
- Exclude requests **only** for counts, dates, or summaries; mixed requests may still include filtering.
- "Remove the rest" should mean omit from the returned list, not delete resumes or change applicant records.

This was a hypothetical writing exercise, not an implemented hiring workflow. See [report](../reports/1405-07-02-trigger-condition-authoring.md).

## Pass evidence

The learner can:

- explain discovery versus triggering;
- recognize false-positive and false-negative triggers;
- apply semantic trigger conditions to a new scenario; and
- diagnose a vague or overly broad skill description.

## Summary

Discovery exposes lightweight skill metadata, like a quick scan; triggering matches that metadata to the user's intent; loading brings in the full workflow only when needed. Poor names or descriptions can cause false negatives or false positives. Strong `use when` conditions name a narrow outcome and relevant inputs. Strong `do not use when` conditions exclude realistic neighboring tasks. Evaluate both positive and negative cases.

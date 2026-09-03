# Periodic Assessments

Read this reference when preparing, running, or reporting a phase-boundary or other periodic review.

## Purpose and triggers

A periodic assessment checks whether previously demonstrated knowledge is retained and transferable. It is not a repetition of the most recent quiz.

Run one by default after the phase's ordinary learning and build outcomes have sufficient evidence but before marking the phase exit criteria complete. Propose an earlier review when:

- roughly four to six outcomes have accumulated since the last retention check;
- the same misconception appears in more than one session;
- an upcoming task depends on an older, uncertain prerequisite; or
- the learner resumes after a substantial break.

These are decision triggers, not a rigid calendar. Explain why a non-boundary review is useful and obtain agreement before starting it.

## Evidence preparation

Read the roadmap, the living strengths-and-gaps profile, and the relevant session reports. Extract:

- demonstrated strengths with supporting behavior or artifacts;
- active gaps that remain unresolved;
- corrected misconceptions that have not yet passed a delayed check;
- wrong answers and the reasoning gap each exposed;
- learner questions that revealed genuine confusion or useful transfer reasoning; and
- prerequisites needed by the next phase.

Do not treat question-asking itself as weakness. A clarification question is gap evidence only when its content reveals an incorrect mental model or unresolved uncertainty. A question that detects ambiguity, challenges a defective assessment, or connects concepts can be strength evidence.

## Assessment design

State the review scope and completion evidence before asking questions. Build a fresh assessment that:

- samples the phase's important outcomes rather than every checkbox;
- includes every unresolved critical gap;
- retests corrected misconceptions with different wording and a new scenario;
- includes at least one earlier prerequisite when retention matters;
- mixes recall, application, diagnosis, and practical explanation or artifact work; and
- avoids copying earlier questions or teaching the answer in the prompt.

Use four to six checks for an ordinary phase review, adjusted downward when a practical artifact provides stronger evidence. Multiple-choice checks follow the rules in `coaching-protocol.md`, including a final `I don't know` choice. Require short reasoning or an independent artifact where guessing would otherwise be plausible.

## Evaluation and progression

Evaluate correctness, reasoning, transfer, and independence. Assign **Retained** only to concepts demonstrated again after time or in a meaningfully different context.

- Passing the review supports completing the phase exit criteria when its other requirements are met.
- A non-critical weak area may remain a documented review item while the learner continues, if upcoming work safely reinforces it.
- An unresolved safety-critical or next-phase prerequisite blocks phase completion until targeted education and a fresh reassessment succeed.
- Do not erase earlier Demonstrated evidence after a weak retention check. Record the new gap, withhold Retained status, and schedule targeted review.

## Living strengths-and-gaps profile

Create `learner/reviews/strengths-and-gaps.md` when evidence first warrants it. Keep it concise and use these sections:

```markdown
# Strengths and Gaps

## Demonstrated strengths

| Concept or behavior | Evidence | Level | Last checked | Source report |
|---|---|---|---|---|

## Active gaps

| Concept | Evidence from question, answer, or artifact | Needed correction | Next check | Source report |
|---|---|---|---|---|

## Retention candidates

| Concept | Earlier issue and correction | Fresh check needed | Target checkpoint | Source report |
|---|---|---|---|---|
```

Update entries instead of accumulating duplicates. Move a corrected active gap to retention candidates; move it to demonstrated strengths only after independent reassessment. Preserve enough history to design a fresh question, but do not store secrets, sensitive project details, or unnecessary verbatim learner answers.

## Reporting

Write each periodic result to `learner/reports/YYYY-MM-DD-phase-<n>-periodic-review.md`, adapting the normal session-report structure. Include:

- scope and trigger;
- concepts sampled;
- evidence for strengths and weaknesses;
- retained, reinforced, and unresolved concepts;
- phase progression decision;
- profile and roadmap changes; and
- the next review trigger.

Update the roadmap's periodic assessment log when it exists. For older roadmaps without that table, add a concise checkpoint only when the first periodic review is scheduled or completed; do not rewrite the roadmap solely to match the latest template.

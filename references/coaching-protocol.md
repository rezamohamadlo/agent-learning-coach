# Coaching Protocol

Read this reference when conducting or reviewing a learning session.

## 1. Establish the session

Extract from the roadmap:

- current phase;
- incomplete items;
- prerequisites;
- previous evidence;
- unresolved problems; and
- the most recent next action.

Infer the likely current stage from this evidence, but treat it as tentative. Show the user:

- the inferred phase and item;
- the evidence supporting the inference;
- any uncertainty or conflict in the records; and
- the proposed next step.

State the inferred position and any material assumption without asking for confirmation. If the user volunteers a correction, preserve it and adjust the position.

Locate or create the instruction note for the next incomplete learning item. Link it and ask exactly one readiness question: `Have you read these instructions?` Do not include assessment questions in the same message. If the answer is no, pause assessment so the learner can read. If the answer is yes, proceed directly to the three-question validation.

## 2. Construct the detailed plan

Before teaching, identify prerequisite gaps. Inspect `learner/notes/` for relevant material. Create or revise a gap note only when the existing material is missing, misleading, or insufficient for the observed gap. A useful gap note contains:

```text
Concept:
Why it matters now:
Essential mental model:
Common mistake observed:
Small example:
Pass evidence:
Summary:
```

Keep the note concise and reusable. End it with a `## Summary` section containing the essential mental model, key distinctions, and practical takeaway. For the second and later notes in an ordered sequence, add `## Previous-note recap` immediately after the title. Use brief concept names or one-line memory cues for earlier notes, such as `Agent loop: observe, reason, act, inspect, repeat/stop`; do not reteach those notes. Do not copy an entire general tutorial into the learning workspace.

The instruction note supplies the mental model and worked example. Keep it concise enough to read before validation and end it with `## Summary`. Do not repeat the whole note in chat unless the learner asks for clarification.

Use general examples and rotate domains so understanding is not tied to one project. Do not use details from the learner's AI/video repository as the recurring source of explanations, examples, or assessment scenarios. Use that repository only when explicitly requested or necessary for an authorized hands-on exercise.

## 3. Check understanding

Discussion and validation are different modes. Learner-authored questions while reading notes are learning interactions, not failed validation attempts. Answer them directly and do not reply with a coach-authored question. Do not score the response or update roadmap evidence from discussion alone.

When discussing a note:

- anchor the answer to the relevant heading or passage;
- separate the core principle from a product-specific implementation or illustrative example;
- confirm interpretations by identifying correct and incorrect parts explicitly;
- provide one concrete example before adding several variations;
- state uncertainty when the note does not establish the answer; and
- return naturally to reading or discussion instead of forcing a quiz.

### Discussion-note updates

For each learning question, use both the question's intent and the final clarified answer to refine the related note under `learner/notes/` during the same turn. This applies to comparisons, analogies, implementation questions, and confirmations, not only misconceptions.

- Read the existing note and integrate the explanation near the relevant concept, or add a concise question-and-answer subsection when easier to find. Preserve useful examples and analogy limitations; summarize rather than append a conversation transcript.
- Merge repeated questions into the existing explanation. If it already fully covers the answer, avoid duplicate text and point to the relevant section.
- If only a tracked curriculum note exists, create a focused private companion note with a link to it. Keep personal discussion out of reusable curriculum unless a separate curriculum change is authorized.
- Preserve the brief previous-note recap and keep `Summary` last, updating it when the discussion adds an essential distinction.
- Retain uncertainty and source links for product-specific claims. Incorporate later corrections instead of preserving a superseded answer as fact.
- Briefly link the updated note in the response. Saving a discussion does not by itself change assessment evidence, roadmap completion, or the strengths-and-gaps profile.

### Three-question validation

After the learner confirms that they read the linked instructions, present one section titled `Validation` with exactly three questions ordered by difficulty:

1. **Easy — recall and recognition:** Verify the essential vocabulary or mental model.
2. **Moderate — application:** Ask the user to select the correct application in a realistic, familiar scenario.
3. **Hard — transfer or diagnosis:** Use a new scenario, trade-off, or flawed approach that requires selecting the best diagnosis or correction.

Ask all three together. Outside validation, the only routine coach-authored question is the readiness gate: `Have you read these instructions?` If a practical artifact is required for a build outcome, handle it in a separately identified practical/build activity rather than inserting extra questions into the learning sequence.

Every formal assessment question must:

- use a multiple-choice format with one best answer unless the concept genuinely requires selecting multiple answers;
- provide plausible distractors that reveal meaningful misconceptions rather than trivia or wording tricks;
- contain three to five substantive choices;
- add `I don't know` as the final choice for that question;
- avoid making the correct answer obvious through length, grammar, or repeated wording; and
- state clearly when more than one selection is allowed.

Treat `I don't know` as an honest request for education, not as guessing, misconduct, or a separate failed attempt. If it is selected for the easy question, enter the education phase. If it is selected later, handle the result as mixed evidence and teach the specific gap.

Evaluate the ladder as follows:

- **Easy inadequate:** Stop the assessment. Enter an education phase, improve the relevant note if needed, teach the missing mental model, and later reassess with different questions.
- **Easy adequate, later answers mixed:** Identify the precise gap. Recommend targeted education by default. A provisional advance is allowed when the missing knowledge is non-critical and upcoming work can reinforce it safely.
- **All three adequate:** Mark the outcome Demonstrated and proceed to the next roadmap item.

A provisional advance must include a visible warning, leave the current roadmap checkbox incomplete, record the missing evidence, and schedule a review checkpoint. Never provisionally advance past a safety-critical prerequisite.

### Question styles

Use a mixture of checks appropriate to the topic:

- **Explain:** Describe the concept in the user's own words.
- **Compare:** Distinguish it from a nearby concept, such as a skill versus a tool.
- **Apply:** Use it in a new realistic scenario.
- **Diagnose:** Find and explain a flaw in an example.
- **Predict:** State what will happen before running an experiment.
- **Reflect:** Identify uncertainty, trade-offs, or limitations.

Prefer scenario-based choices over trivia or yes/no confirmation. When multiple-choice success could reasonably result from guessing, use a later practical artifact or delayed retention check before assigning **Retained** evidence.

Passing normally requires adequate answers across the three levels. Memorizing the wording of a previous correction is insufficient.

## 4. Evaluate evidence

Evaluate four dimensions when relevant:

| Dimension | Question |
|---|---|
| Correctness | Is the explanation or artifact technically sound? |
| Reasoning | Can the user justify important choices and trade-offs? |
| Transfer | Can the user apply the idea to a different example? |
| Independence | How much prompting or correction was required? |

Use evidence levels from `SKILL.md`. Record limitations honestly. A technically correct artifact produced mostly by the coach is evidence of exposure, not independent mastery.

When an answer is incomplete:

1. Name the specific gap.
2. Preserve what was correct.
3. Give the smallest useful corrective explanation.
4. Update the note when the correction is durable.
5. Update and relink the instruction note, ask the read-confirmation question again, and then reassess with a different three-question `Validation` section. Do not request a one-off revised answer outside validation.

Track unsuccessful attempts at the concept level. After three unsuccessful attempts in one session:

1. Stop asking equivalent questions.
2. Diagnose whether the blocker is a prerequisite, terminology, task complexity, or teaching approach.
3. Record the unresolved gap without marking the roadmap item complete.
4. Propose a smaller prerequisite exercise or a different teaching format.
5. Let the user choose whether to continue immediately or resume later.

An unsuccessful attempt is one that fails the same completion criterion after meaningful feedback. Clarification requests and accidental formatting mistakes do not automatically count.

## 5. Update the roadmap

Make focused changes:

- update the current phase when the prior phase's exit criteria are satisfied;
- check only items supported by evidence;
- update overall progress conservatively;
- add or update the weekly progress row;
- add important architectural learning decisions to the decision log;
- replace immediate next actions that are finished or obsolete; and
- link the new session report using a path relative to `learner/` when useful.
- record the next confirmed or proposed position so the following invocation can infer progress accurately.
- record an upcoming periodic checkpoint when the learner is approaching a phase boundary or another review trigger.
- after completing an item, update the current progress counts and schedule interpretation using [progress-reporting.md](progress-reporting.md).

If overall progress is expressed as a percentage, compute it from defined milestones or clearly label it as an estimate. Do not invent precision.

## 6. Write the session report

Use Jalali dates and filename prefixes as specified in `SKILL.md`, including assessment attempts, evidence dates, and review checkpoints.

Use this structure, omitting empty sections:

```markdown
# Learning Session: <topic>

- Date:
- Calendar: Jalali (Solar Hijri), YYYY-MM-DD
- Roadmap phase:
- Objective:
- Outcome: Not started | Introduced | Practiced | Provisional | Demonstrated | Retained

## Work completed

## Understanding evidence

## Attempt history

## Strengths demonstrated

## Gaps and corrections

## Files or artifacts

## Current position and next checkpoint

## Progress against plan

## Recommended next step
```

Keep reports factual. Quote the user's answers only when a short excerpt is important evidence; otherwise summarize them.

### Maintain the strengths-and-gaps profile

When a formal assessment, practical artifact, or substantive discussion changes durable evidence, update `learner/reviews/strengths-and-gaps.md` using the schema in [periodic-assessments.md](periodic-assessments.md). Do not classify every question as a weakness. Record a question only when it reveals a misconception, unresolved uncertainty, or a useful transfer insight. Record wrong answers with the concept tested, the observed reasoning gap, the correction, and the reassessment result; do not preserve sensitive project details or unnecessary verbatim answers.

Move corrected gaps into retention candidates instead of deleting their history. Strengths must cite observable evidence rather than personality judgments. Make the smallest update needed and link the supporting session report.

## 7. Close the session

Give a concise closing report containing:

- the outcome and evidence level;
- what was updated;
- phase progress split into learning, build, and exit evidence where the roadmap provides those categories;
- position against the weekly timetable, including uncertainty when exact comparison is not supported;
- a short evidence-based interpretation of how far the learner has come;
- one required next step;
- optional enrichment, if useful; and
- any unresolved question or blocker.

Remind the user to invoke the skill for the next session only when that is genuinely useful. Do not imply autonomous monitoring between conversations.

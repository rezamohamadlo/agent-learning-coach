# Reviewing Diffs and Verification Evidence

## Previous-note recap

- Agent loop: inspect the result before claiming completion.
- Permissions: capability does not establish authority.
- Task specification: acceptance criteria describe required outcomes; verification methods gather evidence.

## Priority review material

**Starred for future review at the learner's request — 1405-06-19 (Jalali).**

- [Final reusable code-review checklist](#final-reusable-code-review-checklist)
- [Worked example: username review and feedback](#username-review-practice-first-response)
- [Worked example: when to request a fix or evidence](#how-to-use-the-decision-rule)

Use before accepting an agent's code change. Build 2's writing outcome is complete; independent review-decision practice remains separate.

## Session objective

Review a small patch against its request, identify a defect or missing evidence, and explain what must happen before accepting it. Estimated effort: 15–25 minutes. Completion requires independent application and diagnosis in fresh scenarios; reading this note alone does not complete the roadmap item.

Based on [Task specification and verification](../../../references/curriculum/phase-1/task-specification-and-verification.md).

## Essential mental model

Compare three things: the request, the actual change, and the verification evidence. A convincing summary cannot replace either inspection of the change or relevant checks.

A diff shows removed lines with `-`, added lines with `+`, and surrounding unchanged code. Read enough surrounding code to understand the effect. Review changed tests too: passing tests can hide a regression if their expectations were weakened.

## Review sequence

1. Restate the requested behavior, preserved behavior, and scope constraints.
2. Inspect the changed files and lines. Check whether each change belongs to the task and whether the logic satisfies the criteria.
3. Identify affected cases: the reported failure, nearby boundaries, and existing valid behavior.
4. Inspect verification: what ran, what it asserted, its actual result, and whether it ran against the final patch in a relevant environment. A test command is a method; its output and assertions determine what evidence it supplies.
5. Give a supported verdict: accept, request correction, or request missing evidence. Distinguish an observed defect from uncertainty caused by an untested case.

## Guided example

Request: Allow reservation quantities from 1 through 8 inclusive. Reject everything else. Preserve the existing error message.

Assume `quantity` is already an integer. The original guard rejected zero and negatives but allowed quantities above 8. The proposed patch is:

```diff
-if quantity < 1:
+if quantity < 1 or quantity >= 8:
     raise ValueError("Invalid quantity")
```

Reported checks: quantities 0 and 9 are rejected; quantity 4 is accepted. All three pass. This is a hypothetical teaching example, not executed repository code.

The change rejects 8 even though the request allows it: a definite boundary defect visible in the diff. The passing checks missed that boundary. Correct the upper comparison to `> 8`, then check 0, 1, 8, and 9, with the required error message for invalid inputs. An ordinary valid case can also help confirm preserved behavior. Inspect the final diff and run relevant checks after the correction.

### Discussion: did the tests reveal the bug?

The requested behavior is to accept integers 1 through 8. However, the example's tests check only 0, 4, and 9; they all pass and do not reveal the rejection of 8. Reading `quantity >= 8` in the diff reveals that defect. A new test expecting 8 to be accepted would fail on this patch and expose the bug through execution as well.

This is an already-solved teaching example. No agent needs to implement it now. Later practice uses a fresh scenario to check whether the learner can compare requirements, changes, and evidence independently.

## Evidence limits

- Test counts alone say little about coverage of the acceptance criteria.
- A test of an isolated helper does not necessarily establish behavior of its caller or the full user flow.
- A skipped or blocked check leaves uncertainty; it is not a passing result.
- Verification from before a later edit may not support the final patch.
- An unrelated failure needs investigation before being classified as unrelated; do not widen the fix automatically.
- Choose additional checks based on affected behavior and risk, rather than running every possible check.

## Practice and pass evidence

After reading and discussion, review a different small patch and its reported checks. Identify whether it meets the request, support your judgment with a specific changed condition or evidence gap, and name a focused next action. Formal assessment follows separately after an opportunity for questions.

## Final reusable code-review checklist

Completed writing outcome: 1405-06-19 (Jalali; Asia/Tehran). Consolidated from the learner's original questions, test-result/coverage additions, and username-specific application, with coach refinements. This completes Build 2's writing criterion; independent review-decision mastery remains a separate active practice gap.

Use after an agent finishes a code change and before accepting it. Compare the original request, final diff (including changed tests), and actual verification results. Adapt examples and checks to the affected behavior.

1. **Requirements:** Does the actual change satisfy every acceptance criterion, including expected outputs and error messages?
2. **Scope and permissions:** Were edits and actions limited to what I authorized, with forbidden files, dependency changes, database changes, or other restricted actions respected?
3. **Code correctness:** After inspecting the final diff and relevant surrounding code, does the logic implement the requested behavior? Were relevant syntax or static checks successful?
4. **Preserved behavior:** What existing behavior could this change affect, including through shared code, and what evidence shows it still works?
5. **Test coverage:** Do existing or updated tests meaningfully check normal cases, exact boundaries, nearby invalid cases, and relevant regressions? Do their assertions match the requirements rather than merely the implementation?
6. **Actual results:** Which relevant checks ran against the final code, in what environment, and what were their actual results? Were any checks skipped, blocked, or run before later edits?
7. **Defects and evidence gaps:** Which findings show incorrect behavior, and which leave uncertainty? For a known defect, request a correction and verification; for missing evidence, request the specific check or inspection needed.
8. **Acceptance:** After inspecting the final changes and relevant results, is there sufficient evidence to accept the work, or what exact correction or evidence is still required?

### How to use the decision rule

Illustrative request: a booking form must reject dates in the past.

- Past dates were never checked: request a past-date check. The missing check alone does not prove a bug.
- A past date was checked and accepted: request a validation fix, a regression check expecting rejection, and relevant checks against the corrected final code. More test cases alone will not fix the observed behavior.
- Required behavior and relevant preserved behavior are supported by final-code inspection and checks: accept within the scope of that evidence.

Writing is complete because the learner supplied a substantive reusable draft and concrete application; the coach consolidated and refined it. No new independent assessment or Retained evidence is claimed. The next build is drafting project-level agent instructions. Revisit the decision-rule gap during bounded coding work and the Phase 1 review.

## Code-review checklist: learner draft and feedback

Historical draft status: this section preserves the earlier paused practice. The writing outcome is now complete; see Final reusable code-review checklist above. Independent review-decision practice remains pending.

The learner proposed six checks (wording normalized):

1. Were changes limited to the sections I authorized?
2. Were forbidden areas left unchanged?
3. Is the written code free of syntax errors?
4. Were tests added to validate the updated code later?
5. Are inputs and outputs validated as expected?
6. Were the validation requirements met?

The draft explicitly covers allowed scope, forbidden edits, syntax, future test coverage, and expected input/output behavior. The last question needs a clearer definition of validation and supporting evidence.

Feedback for revision:

- Unchanged files do not guarantee preserved behavior: changed shared logic can affect callers elsewhere. Include relevant existing behavior in the checks.
- Syntax checks establish only part of correctness; compare actual behavior with every acceptance criterion.
- Existing tests may already provide sufficient coverage. Add or update tests when needed, and inspect their assertions for normal, boundary, invalid-input, and regression cases relevant to the change.
- Tests being present does not establish that they ran or passed. Require actual results against the final code and identify skipped or blocked checks.
- Include a decision rule: request a correction for an observed defect, or specific missing evidence when correctness remains uncertain. Check that actions also stayed within granted permissions.

Next practice: revise the tests question to cover relevant coverage and actual final-code results; clarify the last question around acceptance criteria and the response to failed or missing evidence. Keep the final artifact concise, with up to eight questions. No independent verification-design mastery is claimed from this draft.

## Discussion: why write a review checklist?

The learner asked what this section is for, what they are learning, and where it will be useful. Pause checklist polishing to establish its purpose; this is a request for explanation, not a failed assessment.

The task-request template helps specify work before an agent starts. The review checklist helps decide whether to accept the result after the agent finishes. It is a reusable reminder for the human reviewer, and can also guide an agent review; an agent checking its own work does not establish correctness by itself.

The practical skill is comparing requested behavior, actual changes, and supporting evidence, then choosing a next action. For example, a request says a shop should provide free shipping for orders of $50 or more. The agent reports passing checks for $30 and $70. These results leave the exact $50 boundary unverified. If the code uses total > 50, there is an observed defect: request a correction and relevant checks. If the code appears correct but $50 was never checked, request that missing evidence before accepting the boundary behavior.

Use the checklist after an agent fixes a bug or adds a feature, before accepting or merging the change. It supports a focused review of affected behavior; it does not prove the entire project is bug-free or require exhaustive tests for every change. The writing outcome is a useful personal reminder, not memorizing particular wording.

The learner added two draft questions: whether all tests passed, and whether existing and newly added tests cover proper project operation. These address results and coverage. Suggested refinement: relevant tests must run against the final code, skipped or blocked checks must be visible, and coverage should match acceptance criteria and affected existing behavior.

Next coaching step: establish the purpose through this concrete example and allow discussion before asking for further checklist revision. Checklist completion and prior assessment evidence are unchanged.

## Username-review practice: first response

The learner requested a general checklist followed by a specific request to assess through their own review questions. The scenario requires usernames of 4–16 characters inclusive, English letters/digits/underscores only, a starting letter, the exact invalid message, preserved duplicate rejection and login behavior, edits limited to registration validation/tests, and no dependency installation or schema changes. The hypothetical agent reports only three passing cases: Alex_7, ab, and 1alex.

The learner independently questioned test sufficiency and identified overlength and non-English cases, the exact error message, preserved duplicate rejection (requesting a test if absent), preserved login behavior and passing tests, and dependency/schema preservation. These are relevant applications of coverage, preservation, and constraints. No actual code or test output was supplied, so this exercise cannot establish an implementation defect or a verified result.

Targeted feedback: add exact length boundaries (3, 4, 16, 17); representative forbidden spaces/punctuation and a leading underscore; inspection of changed files and actual validation logic; and actual relevant results against the final code, including skips or blocked checks. Unchanged dependency files do not by themselves prove no dependency was installed; action records address that constraint. Existing tests may be reused if their assertions cover the requirement.

Continue with a small follow-up: formulate a precise boundary question and state whether the available report proves a bug or leaves missing evidence, then name the next action. This is an ongoing assessment response, not completion of the checklist or a new mastery claim. Preserve prior demonstrated evidence.

### Username-review follow-up: boundaries and conclusion

The learner proposed lengths 2, 4, 8, 16, and 18, plus #reza as an invalid initial-character case, and requested completing the test samples. This correctly covers below-range, both valid endpoints, an interior case, and above-range inputs. Prefer adjacent invalid lengths 3 and 17 to catch off-by-one errors that lengths 2 and 18 could miss; the other username rules should remain valid when testing length in isolation. #reza is a valid forbidden-character test but mixes that rule with the starting-letter rule. _reza isolates the starting-letter restriction because underscore is allowed elsewhere.

The learner selected a useful next action (additional checks) but did not explicitly distinguish an observed bug from insufficient evidence. Clarification: three passing reported tests leave missing evidence; they do not establish that the code is wrong. Request the missing relevant checks against the final code and inspect their results before deciding whether a correction is needed. No completed checklist or new independent-mastery claim is recorded from this follow-up.

## Session close: 1405-06-19

Calendar: Jalali (Solar Hijri); Asia/Tehran. The learner ended practice and requested saving the updates. No further assessment is requested now.

In the final hypothetical scenario, _reza was accepted despite the requirement to start with a letter. The learner correctly withheld acceptance but requested more invalid-character tests rather than correction of the known defect. The coach explained that observed incorrect behavior calls for a fix followed by verification; untested behavior calls for evidence. Appropriate instruction: fix the starting-letter validation, ensure a regression test expects _reza to be rejected, and rerun relevant checks against the corrected final code. More tests alone do not correct the observed defect.

Outcome: Practiced. Strengths include identifying missing coverage, exact valid length limits, the required error message, preserved duplicate rejection/login behavior, and dependency/schema constraints. Adjacent invalid lengths 3 and 17 and isolation of the starting-character rule were supplied as feedback. Independent distinction between a known defect and missing evidence remains unresolved; no Retained claim is made and historical Demonstrated evidence is preserved.

Historical stopping point before the later checklist completion: session closed at the learner's request. Keep the checklist draft and scenario questions. On a future learning session, briefly revisit fix-versus-verify in a different practical context before finalizing the review-decision portion; do not restart the full questionnaire. See ../reports/1405-06-19-code-review-checklist-practice.md.

Completion record: [Build 2 writing outcome](../reports/1405-06-19-code-review-checklist-completed.md). The final checklist above supersedes historical next-practice instructions; preserve them as learning history.

## Discussion: preserving a value during an operation

In the [task-renaming exercise](../experiments/hypothetical-task-3.md), `completed` means whether the underlying task is finished, not whether renaming succeeded. Preserving it means True stays True and False stays False, for both accepted and rejected renames. A successful rename changes the title only; rejection raises `ValueError("Title is required")` and leaves the original task unchanged. Verify exact error text as well as rejection. This clarification is discussion evidence, not independent mastery.

## Summary

- Compare the request, actual diff, and verification evidence.
- Inspect boundaries, preserved behavior, and changed test expectations.
- Passing checks support only the behavior they meaningfully cover.
- Distinguish definite defects from missing evidence and state the next action precisely.

# Hypothetical task 3: preserving task completion during rename

## Previous-note recap

Compare requirements, changes, and evidence. Check exact error messages and preservation of existing state.

## Scenario

Rename a task by trimming the new title. Reject an empty trimmed title with `ValueError("Title is required")`. Preserve the task's existing `completed` value. The proposed implementation incorrectly returns `{"title": title, "completed": False}` for every accepted rename.

## Discussion and clarification

The learner correctly requested verification of the exact rejection message. They initially interpreted `completed` as a rename-success indicator. After explanations, they asked whether it should simply retain its initial value. Yes: `completed` describes whether the underlying task is finished, independently of renaming.

| Initial completed | Accepted rename | Rejected rename |
|---|---|---|
| True | True | True |
| False | False | False |

An accepted rename changes the title only. A rejected rename leaves the original title and completion state unchanged and raises the specified exception. For example, renaming an unfinished reading task does not finish the reading. There is no rename-success Boolean in this contract.

## Original simulation outcome

Guided exercise complete (Practiced). The learner adopted the coach-refined correction request below. This completes the writing/review exercise, not independent assessment or executed implementation. No code or tests ran.

## Final correction request

> Preserve `completed` from the original task when returning the renamed task. Test successful renames with both `True` and `False`. For rejected titles, verify `ValueError("Title is required")` and confirm the original task remains unchanged.

The learner independently requested the exact error-message check. The distinction between stored completion state and rename success required repeated explanation. A later proposal to omit `completed` from the output was corrected: this function returns a task object, so it must retain the field with its original value. The final request repeats coach-provided wording and is guided evidence only. Revisit state preservation in a fresh context during the Phase 1 review.

## Follow-up request review: 1405-06-24

Calendar: Jalali (Solar Hijri); Asia/Tehran.

The learner drafted a request for the separate list-based contract `rename_task(tasks, task_id, new_title)`, using `done` rather than the earlier scenario's `completed`. They explicitly included trimming, invalid-title and unknown-ID errors, preservation of IDs and completion flags, output order, returning the updated list, and leaving original records unchanged. They proposed whitespace and unknown-ID tests. This is request-writing practice; no implementation or tests ran.

Feedback: name the three function arguments precisely (one target ID); explicitly request a **new** list and preservation of other tasks' titles. Extend verification beyond input validation to cover successful renaming, both completion values, order, and unchanged input records. For `" name"`, `"name "`, and `" name "`, state the expected title `"name"`. Include both `""` and whitespace-only input. Ask the implementing agent to run tests and report the command and result. This new contract specifies exception types only, so the earlier exact error message is not required.

Next practice: describe a before/after test that catches an implementation which returns a new list but still modifies the original task dictionaries. Actual verified execution remains pending; roadmap completion is unchanged.

### Showing the original input versus testing preservation

The learner suggested "returning the original list in answer." If this means showing the original input in the agent's report, it helps visual inspection. If it means returning the original list from the function, it conflicts with the required new updated list. The intended meaning remains ambiguous; neither interpretation establishes a demonstrated misconception.

To verify preservation, save an independent snapshot before calling the function, then assert that the input still equals that snapshot afterward. Use `deepcopy(tasks)` for the snapshot: `before = tasks` shares the same list, and `tasks.copy()` still shares its dictionaries. Separately assert `result is not tasks` and check the expected updated output. Displaying the input after the call alone cannot prove it stayed unchanged. No code or tests ran during this discussion.

## Implementation follow-up: 1405-06-24

With the learner's agreement to continue, the coach created [rename_task.py](task-renaming/rename_task.py) and [test_rename_task.py](task-renaming/test_rename_task.py). The implementation trims and validates the title, checks the target ID, and builds a new list with copied dictionaries. Five test methods cover successful renaming for both completion values, order and other-title preservation, independent input snapshots, whitespace trimming, rejected titles, unknown IDs, and an empty list.

Attempted command: `py -m unittest discover -s learner/reza/experiments/task-renaming -v`.

Result: exit code 1, `No installed Python found!` The `python` command is also unavailable. No tests executed, so passing behavior is not claimed. Next step: run this command in a Python-enabled environment and have the learner review the actual results. Phase 1's verified-result exit criterion remains incomplete. These code artifacts were coach-authored, not independent learner implementation evidence.

## Hypothetical review follow-up: 1405-06-24

The learner explicitly chose hypothetical samples instead of real implementation or test execution. This supersedes the implementation follow-up's immediate next step; continue with simulated evidence, without claiming actual execution or closing the actual-verification exit criterion.

Sample: before the call, task 1 has title `Read chapter` and `done=False`; the returned separate list has title `New title`; the original input inspected after the call also has title `New title`.

The learner correctly identified preserved ID and completion status, the expected returned title, and missing evidence for errors, whitespace validation, and meaningful multi-record order preservation. They did not identify the shown input mutation. Clarification: "before" and "original input after calling" describe the same input at two different times. Its title changed, so input preservation demonstrably fails; this is a known defect, not merely a missing check. A new outer list can still share dictionaries with the input.

Review decision: request a correction for input mutation and additional hypothetical cases for uncovered requirements. Next guided check: state the title expected in the original input after a correct rename. No further implementation or test execution is requested.

## Actual verification resumed: 1405-06-25

Calendar: Jalali (Solar Hijri); Asia/Tehran.

The learner agreed to the proposed actual bounded task-renaming exercise. The existing implementation and tests were inspected without changes. The previously blocked command now ran successfully:

```text
py -m unittest discover -s learner/reza/experiments/task-renaming -v
Ran 5 tests in 0.001s
OK
```

Exit code: 0. This supersedes the earlier runtime blocker for the current environment. Coverage includes successful renames for both `done` values, trimming, invalid titles, unknown IDs, empty lists, order, other-task titles, a distinct returned list, and unchanged original input. See [session record](../reports/1405-06-25-weekly-targets-and-practical-verification.md).

### Practical review prompt (now completed; see outcome below)

Objective: review the actual result against the learner's bounded contract. Estimated remaining effort: 5–10 minutes; actual study time is unavailable.

Read the [existing implementation](task-renaming/rename_task.py) and [tests](task-renaming/test_rename_task.py), using the earlier explanation of independent snapshots if needed. For the successful call that renames task 1 from `Read chapter` to `New title`, explain:

1. What should the original input's task-1 title be after the call, and what should the returned task-1 title be?
2. Why is the unchanged-input assertion against `deepcopy` necessary in addition to `result is not tasks`?
3. Do you accept the result for the stated contract, request a correction, or request more evidence? Give a reason tied to the actual checks.

This is artifact-review practice, not another recall quiz. Ask for clarification before answering if useful. Completion requires learner reasoning; the coach's passing test run alone does not close the Phase 1 exit criterion.

### Learner review response

The learner correctly stated that the original input should remain unchanged. For this example, that means its task-1 title remains `Read chapter`; the returned task-1 title is `New title`. This is partial review evidence: the reason for checking input equality separately from list identity and the final acceptance decision remain unanswered. Continue with one question at a time; no completion or evidence-level change is recorded.

In the follow-up, the learner correctly rejected list identity as sufficient and proposed checking that task 1 has the new title in the returned result. This is a useful output-correctness check, but it does not establish input preservation. Clarification: a new list may contain the same dictionaries as the original list. Changing a shared dictionary can make the returned title correct while also changing the original input incorrectly. Verify both the expected returned output and `tasks == before`, where `before` is an independent snapshot made before the call. Next guided check: judge a case where the returned title and original title both become `New title`, although the original title was `Read chapter` before the call. Final acceptance reasoning remains pending.

### Clarification: two places to inspect after the call

The learner said the follow-up question was unclear. This is a clarification request, not a failed assessment attempt. Pause the review question and show the contract with a concrete before/after example.

There is an original task list before the function runs. This function must leave that list untouched and return a separate updated version. After a correct call, both are available: the original still contains `Read chapter`, and the returned version contains `New title`. The preceding table intentionally showed an incorrect implementation: both versions contained `New title` afterward. That violates input preservation even though the returned title is correct. The question was asking whether to accept that deliberately faulty outcome, not asking the learner to perform the rename.

For now, separate two checks: “Did the returned version get the requested new title?” and “Did the original keep its old title?” Both must pass. Revisit shared dictionaries only after this distinction is clear; no new quiz attempt or completion is recorded.

### Practical review outcome: 1405-06-25

The learner selected B for the meaning of `tasks == before`: the original input still matches the saved data. In the final review, they independently distinguished the two displayed assertions from the four-part coverage summary: the two assertions do not establish correct returned data, whereas the full reported coverage is acceptable for the contract. This is a useful challenge to ambiguous question scope, not a failed answer.

Precise distinction: `result is not tasks` checks object identity, not whether values differ or whether the rename is correct. `tasks == before` checks original-input preservation. The actual test also uses `self.assertEqual(result, expected)` to check the whole returned output, including the changed title and preserved fields/order.

Outcome: the bounded-task verified-result exit criterion is Demonstrated through the earlier learner-authored request, actual passing test execution, and final reasoned acceptance. The implementation/tests and earlier review explanations were coach-supported; this does not claim unaided coding, test authoring, or retained mastery of copying semantics. Schedule a fresh input/output-preservation review during the first Phase 2 skill evaluation. See [completion report](../reports/1405-06-25-phase-1-completed.md).

## Summary

Preserve means keep the original value: True stays True and False stays False. Operation success and stored task completion are different concepts.

Verify unchanged input against an independent before-call snapshot; returning a new list alone does not prove its original dictionaries were preserved.

Check three separate properties: a different returned list object, unchanged original input, and correct returned data. Each requires its own evidence.

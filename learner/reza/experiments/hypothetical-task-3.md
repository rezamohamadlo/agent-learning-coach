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

## Current position

Guided exercise complete (Practiced). The learner adopted the coach-refined correction request below. This completes the writing/review exercise, not independent assessment or executed implementation. No code or tests ran.

## Final correction request

> Preserve `completed` from the original task when returning the renamed task. Test successful renames with both `True` and `False`. For rejected titles, verify `ValueError("Title is required")` and confirm the original task remains unchanged.

The learner independently requested the exact error-message check. The distinction between stored completion state and rename success required repeated explanation. A later proposal to omit `completed` from the output was corrected: this function returns a task object, so it must retain the field with its original value. The final request repeats coach-provided wording and is guided evidence only. Revisit state preservation in a fresh context during the Phase 1 review.

## Summary

Preserve means keep the original value: True stays True and False stays False. Operation success and stored task completion are different concepts.

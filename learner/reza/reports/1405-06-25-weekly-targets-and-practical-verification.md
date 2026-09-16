# Learning Session: Weekly Targets and Practical Verification

- Date: 1405-06-25
- Calendar: Jalali (Solar Hijri), YYYY-MM-DD; Asia/Tehran
- Roadmap phase: Phase 1 — Agent foundations
- Objective: Establish measurable weekly targets and resume the bounded task-renaming exercise.
- Outcome: Practiced; actual execution obtained, learner review pending.

## Planning decision

The learner requested weekly targets based on the roadmap and agreed to continue the proposed practical exercise. A prospective baseline now defines dated, observable units for Weeks 3–12. The original end date, 1405-09-01, is retained as a planning target. Weekly study capacity is unknown; feasibility must be reviewed at the first checkpoint, 1405-06-29. Previous broad weekly themes are not retrospectively scored against these new targets.

## Work completed

Inspected the latest report and the newer 1405-06-24 exercise follow-ups. Those follow-ups record a learner-authored bounded request, coach-authored implementation/tests, an earlier unavailable Python runtime, and a subsequent preference for hypothetical review. Today's agreement to the proposed actual practical exercise resumes real verification.

Preserved the existing implementation, tests, and pre-existing exercise-note changes. Ran:

```text
py -m unittest discover -s learner/reza/experiments/task-renaming -v
```

Exit code: 0. Actual output: `Ran 5 tests in 0.001s`, `OK`. All five named test methods passed. The runtime output is test duration, not study-session duration.

## Verification coverage

- Successful rename with both stored completion values, expected whole-list output, order, and other-task titles.
- New outer list and unchanged input compared with a `deepcopy` snapshot.
- Leading/trailing whitespace trimmed.
- Empty/whitespace-only titles and unknown IDs rejected without input mutation.
- Empty list rejected for unknown ID.

The active list-based contract requires exception types, not exact messages. Tests cover that contract for records containing `id`, `title`, and `done`; no general claim about malformed records, duplicate IDs, or nested mutable fields is made.

## Understanding evidence

No new learner answer has been assessed this turn. Passing coach-authored tests does not establish independent learner review. The remaining step is to connect the actual checks to the contract, explain original-input preservation, and justify acceptance or a specific follow-up.

## Progress against plan

- Phase 1: Learn 7/7; revised Build 4/4; Exit 2/3, unchanged.
- Week 3 targets: 0/3 met; practical target in progress.
- Schedule: Replanned; first checkpoint pending on 1405-06-29.
- Evidence change: execution changed from blocked/unverified to five passing test methods. Learner acceptance remains pending.

## Current position and next checkpoint

Review the expected original title after a successful rename and the role of an independent before-call snapshot. Make a justified review decision from the actual evidence. If the Phase 1 exit criterion is met, proceed to Phase 2 discovery/triggering and the first skill contract with three evaluation cases.

## Files or artifacts

- `../ROADMAP.md`: measurable weekly targets, dates, current evidence, synchronized next actions.
- `../experiments/hypothetical-task-3.md`: current practical continuation.
- Existing `../experiments/task-renaming/rename_task.py` and `test_rename_task.py`: inspected and executed, not edited.
- README reviewed; existing descriptions remain accurate, so no textual update was needed.

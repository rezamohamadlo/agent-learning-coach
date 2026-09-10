# Learning Session: Code-review checklist practice

- Date: 1405-06-19
- Calendar: Jalali (Solar Hijri), YYYY-MM-DD; Asia/Tehran
- Roadmap phase: Phase 1 — Build
- Objective: Form concrete review questions from a bounded username-validation request.
- Outcome: Practiced; session ended at the learner's request.

## Work completed

Explained the checklist's purpose: evaluate an agent's result against the request, actual change, and verification evidence. Provided general review questions at the learner's request, then used a hypothetical username-validation scenario for learner-authored review questions. No project code was changed or tests executed.

## Understanding evidence

The learner identified missing overlength/non-English cases, exact error-message checks, duplicate rejection and login preservation, and dependency/schema constraints. They added exact valid length endpoints and an interior case, plus invalid starting-character examples. The coach supplied adjacent invalid boundaries, isolation of rules, and final-code evidence requirements.

## Attempt history and gaps

1. Initial scenario response: relevant review questions with coverage and preservation strengths; boundary and final-code evidence omissions received feedback.
2. Boundary follow-up: lengths 2, 4, 8, 16, 18 and #reza; valid endpoints identified, adjacent invalid cases and isolated starting-rule case taught. Requested more tests without explicitly distinguishing defect from missing evidence.
3. Decision scenario: _reza was reported accepted against a starting-letter requirement. The learner withheld acceptance but requested more tests rather than fixing the known defect. Targeted explanation followed; no successful independent reassessment occurred.

The purpose question was a learning clarification, not a failed assessment. Historical Demonstrated evidence remains intact. The present transfer gap is active and Retained is not claimed.

## Current position and next checkpoint

The learner said practice was enough and requested updates. Stop assessment now. The checklist remains In progress (Practiced), with the review-decision portion to revisit briefly in a different practical context when learning resumes. Preserve all prior drafts. Include this gap in the Phase 1 periodic review before phase completion.

## Progress against plan

Phase 1: Learn 7/7 previously demonstrated; Build 1/4 completed; Exit criteria 0/3. Counts unchanged. Date 1405-06-19 falls in Week 2, 1405-06-16 through 1405-06-22, within the planned Phase 1 window. Exact ahead/behind status remains unknown because the plan lacks measurable interim deadlines.

## Files or artifacts

- ../notes/reviewing-diffs-and-evidence.md
- ../ROADMAP.md
- ../reviews/strengths-and-gaps.md
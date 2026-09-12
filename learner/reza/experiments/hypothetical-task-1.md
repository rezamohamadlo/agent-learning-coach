# Hypothetical task 1: overdue library fees

## Session objective

Practice directing and reviewing a bounded code change in a hypothetical library application. Estimated effort: 15–20 minutes. The learner chose a hypothetical project because no local project is available.

## Scenario

The function `calculate_late_fee(days_late)` accepts an integer and returns a fee in whole currency units. It currently returns `days_late * 2`, so early returns produce negative fees.

Required behavior: zero fee when `days_late <= 0`; otherwise 2 units per day, capped at 20 units. Input validation for other types is outside this task. Borrowing records and notification behavior must remain unchanged. Relevant tests belong in `tests/test_late_fees.py`.

## Practice sequence

1. Learner writes a bounded request using the saved task-request template, including concrete verification cases.
2. Coach presents a simulated patch and explicitly simulated verification report.
3. Learner reviews scope, correctness, and evidence, then decides whether to accept or request follow-up.

## Completion evidence

A usable learner-authored request and a justified review decision. This conversational simulation supplies practice evidence; it does not establish execution of a coding task or automatically complete Build 4.

## Current position

Guided simulation complete (Practiced). The learner accepted the final simulated change, explaining zero/negative fees, the daily rate through 10 days, and the cap above 10 days. No code has been implemented or tests run. See `../reports/1405-06-21-hypothetical-late-fees.md`.

## Initial request and feedback

The learner identified negative fees for early returns, required zero for negative and zero inputs, protected borrowing records and notifications, named `tests/test_late_fees.py`, and requested checks using -4, 0, and 5 with reported outputs.

These cover the reported defect and an ordinary positive case. The request omitted the explicit positive-day rate and 20-unit cap, and did not provide expected outputs or a case that would expose a missing cap. Feedback asks the learner to add the positive-day rule and expected results for their cases plus cases at and above the cap. Reporting should identify actual checks and any failures or checks that could not run, rather than presupposing success.

This is task-writing practice with feedback, not a formal quiz or evidence of an executed coding task.

## Clarification: fee cap versus input limit

The learner asked whether numbers above 20 should be rejected. The input is days late; the cap applies to the output fee in currency units. Inputs above 20 days remain valid. For positive days, compute 2 units per day and limit the resulting fee to 20: 5 days gives 10 units, 10 days gives 20 units, 11 days gives 20 units, and 25 days also gives 20 units. This is output capping, not input validation. The clarification does not establish independent assessment evidence.

## Cap revision and simulated review

The learner correctly stated that the fee must not exceed 20 for more than 10 days and supplied 20 -> 20 and 25 -> 20 as test cases. These are valid above-cap cases. The coach adds 10 -> 20 and 11 -> 20 as boundary coverage; these additional cases are coach-supplied, not independent learner evidence.

Simulated patch: replace `return days_late * 2` with `return min(max(days_late, 0) * 2, 20)`. Simulated report: only the fee function changed; checks for -4 -> 0, 0 -> 0, and 5 -> 10 passed; cap tests were not added or run. All results are fictional exercise material.

Next prompt: decide whether to accept, request a code correction, or request more verification, and justify the decision from the patch and report. Review is practical discussion, not a scored formal quiz.

## First review response

The learner declined acceptance because inputs of 20 and above had not been tested. This correctly identifies missing requested verification. The learner has not yet explicitly selected a verification request versus a code correction. Coach feedback: the displayed expression meets the stated integer-input behavior by inspection; missing tests are not evidence of a code defect. Request the missing checks and their actual results before accepting. Next practice step: learner writes a short follow-up instruction.

## Verification follow-up

The learner asked for a test using a number above 10, checking that the output is capped at 20, and the full test response. This appropriately requests verification rather than an unsupported code change, with coaching. Coach clarification: assert equality to 20, since merely checking <= 20 would allow an incorrectly low fee.

The next fictional agent report retains the fee implementation and adds parameterized assertions for (-4, 0), (0, 0), (5, 10), (10, 20), (11, 20), (20, 20), and (25, 20). Simulated command: `python -m pytest tests/test_late_fees.py -q`; simulated result: 7 passed, exit code 0. Simulated scope: fee function and its test file only; borrowing records and notifications unchanged. These are invented exercise results, not actual execution evidence. Learner is asked whether this is sufficient to accept the bounded change and why.

## Final reusable example request

Coach-consolidated wording requested by the learner; no additional assessment evidence.

> Fix `calculate_late_fee(days_late)`, which currently returns negative fees for early returns. Assume `days_late` is an integer. Return 0 for zero or negative days; for positive days, charge 2 units per day, capped at 20 units. Days above 20 remain valid inputs.
>
> Limit changes to the fee function and relevant tests in `tests/test_late_fees.py`. Leave borrowing records and notifications unchanged. If a change outside this scope is necessary, explain the proposed change and obtain my approval before making it.
>
> Add or update tests asserting these exact input/output pairs: `-4 → 0`, `0 → 0`, `1 → 2`, `5 → 10`, `9 → 18`, `10 → 20`, `11 → 20`, `20 → 20`, and `25 → 20`.
>
> Run `python -m pytest tests/test_late_fees.py -q` against the final changes and inspect the final diff for scope and correctness. Report what changed, the command and full test output, and any failed, skipped, or unrun checks. Clearly distinguish actual results from expected results.

## Summary

A bounded request needs the full required behavior and tests that distinguish a complete fix from a partial one. Ordinary positive inputs alone cannot verify a maximum-fee rule. The 20-unit cap limits the fee, not the number of days accepted.

# Hypothetical task 2: shipping fee review

## Previous-note recap

Compare requirements, code, and verification results before accepting a change. The first simulation practiced requesting missing cap tests.

## Objective

Review a fresh proposed change and write an actionable follow-up. Estimated effort: 10–15 minutes. This is hypothetical practical review, not a scored quiz or executed coding task.

## Request

Update `shipping_fee(order_total)` so orders totaling 100 units or more receive free shipping; smaller orders cost 8 units to ship. Assume a non-negative integer input. Limit changes to the function and `tests/test_shipping.py`; leave discounts and payment handling unchanged.

## Proposed final code

```python
def shipping_fee(order_total):
    if order_total > 100:
        return 0
    return 8
```

## Simulated agent report

Only the fee function and its tests changed. Reported checks: 50 -> 8 and 120 -> 0 passed. The agent claims the work is complete. These are fictional results; no tests ran.

## Learner task

Write a short response stating whether to accept the change, what specific code or evidence supports the decision, and what the agent should do next. Include a concrete input and expected output.

## Current position

The learner independently identified that the proposed code returns 8 at an order total of 100, required free shipping for totals >= 100, specified 5 -> 8, 50 -> 8, 99 -> 8, 100 -> 0, and 120 -> 0, and requested correction of the function and tests followed by test execution and reporting. This demonstrates diagnosis of this specific visible defect and an appropriate follow-up without a scenario-specific hint. Final acceptance of the corrected simulated response is pending; no code or tests have actually run.

## Corrected simulated response

Replace `order_total > 100` with `order_total >= 100`. The five learner-requested cases are represented as exact assertions in `tests/test_shipping.py`. Fictional command: `python -m pytest tests/test_shipping.py -q`; fictional output: `5 passed`, exit code 0. Only the function and relevant tests change; discounts and payment handling remain unchanged. These results are simulated, not execution evidence.

The input represents the total value of one order, not the number of orders. Next: learner reviews the corrected response for acceptance.

## Exercise closure

Review practice is complete under the revised simulation requirement. The learner rejected simulated results as a substitute for actual tests, then explicitly canceled execution to continue learning. No implementation was accepted as actually verified. A later fictional change from fee 8 to 10 was correctly rejected as violating the requirement. The coach supplied the instruction to restore 8 and rerun checks against final code. Earlier pending-acceptance text describes the historical stage; see `../reports/1405-06-21-build-simulations-completed.md` for the final scope and status.

## Summary

A review decision should connect the requested behavior to the proposed code and reported checks, then identify the next action.

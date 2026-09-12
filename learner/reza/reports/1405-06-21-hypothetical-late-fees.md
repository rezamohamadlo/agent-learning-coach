# Learning Session: Hypothetical late-fee change

- Date: 1405-06-21
- Calendar: Jalali (Solar Hijri), YYYY-MM-DD; Asia/Tehran
- Roadmap phase: Phase 1 — Build 4 preparation
- Objective: Direct and review a bounded change using a hypothetical library application.
- Outcome: Practiced — guided simulation completed

## Understanding evidence

The learner authored a request identifying the negative-fee defect, zero-fee behavior, protected borrowing/notification behavior, test location, and representative inputs. After clarification that the cap applies to the fee rather than accepted days, the learner added the cap and expected outputs for 20 and 25 days.

The learner withheld acceptance when simulated verification omitted cap tests. After feedback distinguishing missing verification from a code defect, the learner requested an above-10 test and full results. The learner then accepted the expanded simulated evidence and correctly explained the three behavior regions: non-positive days, the daily rate through 10 days, and the capped fee beyond 10 days.

## Evidence limits and remaining practice

The coach supplied the implementation, boundary cases at 10 and 11 days, simulated results, and verification-versus-correction feedback. No actual implementation or tests ran. This is guided practice, not independent mastery, Retained evidence, or one of the three executed coding tasks. Representative tests support the reviewed patch; they do not exhaust every possible integer input.

## Current position and next checkpoint

Phase 1 remains Learn 7/7, Build 3/4, Exit criteria 0/3. Calendar position remains Week 2 (1405-06-16 through 1405-06-22); precise ahead/behind status is unknown. The user prefers hypothetical projects while no local project is available. Next: a fresh hypothetical review focused on independently distinguishing an observed defect from missing verification. Complete executed coding tasks when a suitable practice project is available, and conduct the Phase 1 retention review before phase completion.

## Files

- `../experiments/hypothetical-task-1.md`
- `../ROADMAP.md`
- `../reviews/strengths-and-gaps.md`

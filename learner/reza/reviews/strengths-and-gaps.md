# Strengths and Gaps

Calendar: Jalali (Solar Hijri), YYYY-MM-DD.

This private profile summarizes durable learning evidence for future periodic assessments. It distinguishes unresolved gaps from corrected concepts that need a delayed retention check.

## Demonstrated strengths

| Concept or behavior | Evidence | Level | Last checked | Source report |
|---|---|---|---|---|
| Agent loop and verification | Explained why action alone does not prove completion; diagnosed unsafe sequencing and unsupported completion claims | Demonstrated | 1405-06-10 | `../reports/1405-06-10-agent-loop.md` |
| Context relevance and instruction authority | Distinguished authoritative instructions from command-like untrusted data and selected focused context | Demonstrated | 1405-06-11 | `../reports/1405-06-11-context-and-instructions.md` |
| Assessment-quality reasoning | Detected assessment questions whose options contradicted the scenario instead of forcing an invalid answer | Demonstrated | 1405-06-12 | `../reports/1405-06-11-context-and-instructions.md`; `../reports/1405-06-12-prompts-and-repository-instructions.md` |
| Prompt and repository-instruction placement | Explained that vague scope causes unnecessary exploration and that a temporary no-edit constraint belongs in the current prompt | Demonstrated | 1405-06-12 | `../reports/1405-06-12-prompts-and-repository-instructions.md` |

| Tools and agent actions | Selected skill-as-guidance and non-booking quote tools; explained checking booking state after timeout to avoid duplicate execution | Demonstrated | 1405-06-14 | `../reports/1405-06-14-tools-and-actions.md` |

| Permissions and safe execution | Distinguished inspection authority from deletion capability, respected sandbox approval, and explained why a parent directory falls outside authorized cleanup scope | Demonstrated | 1405-06-15 | `../reports/1405-06-15-permissions-and-safety.md` |

| Task specification | Selected observable acceptance criteria and authorized scope in a fresh upload scenario after correction; selections without written reasoning | Demonstrated | 1405-06-16 | `../reports/1405-06-16-task-specification.md` |

| Diff and verification review | Selected coverage limits, corrected a delivery threshold, and required relevant verification after a later shared-code edit; 3/3 multiple-choice answers without written reasoning | Demonstrated | 1405-06-17 | `../reports/1405-06-17-reviewing-diffs-and-evidence.md` |
| Skill discovery and triggering | Correctly selected discovery metadata, a focused positive trigger, and a correction for an overly broad description (3/3); earlier discussion connected poor metadata to both trigger-error directions | Demonstrated | 1405-06-31 | `../reports/1405-06-31-skill-discovery-and-triggering.md` |
| Trigger-condition authoring | Independently chose applicant filtering and distinguished selection against requirements from aggregate reporting | Demonstrated | 1405-07-02 | ../reports/1405-07-02-trigger-condition-authoring.md |
| Stage-specific lifecycle evidence | Correctly kept creation, finalization, storage, and playability separate; after correction, treated a missing finalization event as unverified rather than proof of a specific defect; passed 3/3 fresh checks | Demonstrated | 1405-07-04 | `../reports/1405-07-04-recording-lifecycle-contract.md` |

Review update — 1405-06-22: All six choices were correct in fresh scenarios. Final-change verification is Retained at the conceptual level: selected final-code checks and explained that simplification may change logic. The explanation followed answer feedback. Agent-loop, permission, skill/tool, and state-preservation choices support recognition; do not infer full unaided explanation or actual execution. See `../reports/1405-06-22-phase-1-periodic-review.md`.

Component explanation update — 1405-06-23: The learner independently described the model, context, instructions, goal, tools, state, and verification, then correctly reassessed the distinction between authorization and verification in a fresh scenario. This supports Demonstrated evidence for the Phase 1 component-explanation exit criterion; practical execution remains unverified. See `../reports/1405-06-23-agent-components.md`.

Practical verification update — 1405-06-25: The learner's earlier bounded request led to five actual passing test methods. After guided input-preservation clarification, they independently identified that list identity and unchanged input do not establish correct returned output, then accepted the complete coverage summary. This supports Demonstrated evidence-aware acceptance and the bounded-task verified-result exit criterion. The code/tests were coach-authored; no independent test-authoring or Retained copying-semantics claim. Phase 1 is complete. See `../reports/1405-06-25-phase-1-completed.md`.

## Writing outcomes completed with guidance

- **Code-review checklist — 1405-06-19:** The learner supplied the original checklist, additions about actual test results and coverage, and concrete username-validation questions. The coach consolidated the final wording, including the decision rule. Build 2's writing criterion is complete; this does not establish independent mastery of the active gap below. Source: `../reports/1405-06-19-code-review-checklist-completed.md`.

## Active gaps

Task specification reassessment on 1405-06-16 passed after targeted teaching. Corrected concepts remain retention candidates; no delayed retention is claimed. See `../reports/1405-06-16-task-specification.md`.

Tools assessment on 1405-06-14 passed after replacing an answer-leaked quiz; deployment distinctions were discussed but not independently assessed.

| Concept | Evidence from question, answer, or artifact | Needed correction | Next check | Source report |
|---|---|---|---|---|
| Independent verification design | The learner supplied a bounded request; the coach refined earlier coverage and substantially guided the first skill's three evaluation cases. Evidence-aware interpretation was demonstrated, but independent case design remains unverified. | Design checks from a new contract without relying on a supplied coverage list or scenario sequence. | Independently add or revise a case during the first skill evaluation. | `../reports/1405-06-25-phase-1-completed.md`; `../reports/1405-07-04-recording-lifecycle-contract.md` |

## Retention candidates

Trigger authoring, 1405-07-02: Earlier vague exclusions and theme-versus-metadata ambiguity were corrected with coaching; independent applicant-filter writing passed. Recheck mixed requests and input scope during the first skill evaluation. No actual execution or delayed retention claimed. Source: ../reports/1405-07-02-trigger-condition-authoring.md.

Lifecycle evidence update, 1405-07-04: The learner initially inferred a broken finalization identifier from a missing event, then revised this to unverified finalization while preserving successful storage and playability. Fresh recognition and diagnosis checks passed. Recheck the missing-evidence-versus-known-defect distinction during actual skill execution. Source: `../reports/1405-07-04-recording-lifecycle-contract.md`.

Practical follow-up — 1405-06-25: Input/output preservation and evidence sufficiency were reinforced on the actual task. Earlier known-defect/missing-evidence review passed on 1405-06-22; today's final response correctly challenged incomplete output evidence and accepted full coverage. Treat these as fresh transfer/retention targets, not unresolved phase blockers. The clarification request concerned ambiguous question wording and was not a failed attempt. Recheck during the first Phase 2 skill evaluation.

State-preservation review — 1405-06-22: Correctly preserved subscribed=false in a fresh name-change question. Both values and rejected changes still need a practical check; no full retention claim. See `../reports/1405-06-22-phase-1-periodic-review.md`.

Historical state-preservation practice — 1405-06-21: The learner initially treated `completed` as rename success, then proposed removing it from the returned task. Clarified that both original Boolean values must be retained in the returned object; rejected renames leave the original object unchanged. The learner adopted the coach's correction request. Guided exercise complete; independent application remains unverified. Recheck in a fresh domain at the Phase 1 review. Source: `../reports/1405-06-21-build-simulations-completed.md`.

Guided practice update — 1405-06-21: In the hypothetical late-fee task, the learner identified missing cap checks, requested verification after feedback, and justified acceptance after expanded simulated results. The cap-versus-input-limit confusion was clarified and correctly applied within the same session. Independent defect-versus-missing-evidence transfer remains pending; no Retained evidence is claimed. Source: `../reports/1405-06-21-hypothetical-late-fees.md`.

| Concept | Earlier issue and correction | Fresh check needed | Target checkpoint | Source report |
|---|---|---|---|---|
| Diff review and evidence sufficiency | Earlier boundary correction and Phase 1 periodic review passed; actual task acceptance on 1405-06-25 distinguished incomplete assertions from full coverage | Diagnose a fresh known defect versus missing evidence and justify the review decision | First Phase 2 skill evaluation | `../reports/1405-06-22-phase-1-periodic-review.md`; `../reports/1405-06-25-phase-1-completed.md` |
| Input preservation versus output correctness | Guided clarification followed by correct unchanged-input recognition and an independent challenge that two assertions omit returned-output correctness | Explain and evaluate separate input/output checks in a new domain; recheck both Boolean values and rejection paths | First Phase 2 skill evaluation | `../reports/1405-06-25-phase-1-completed.md` |
| Acceptance criterion versus verification method; authorized scope | Initially selected test execution as a criterion and an unrelated subsystem redesign; after teaching, correctly selected observable upload behavior and a bounded fix | Explain both distinctions and apply them independently in a fresh task contract | Phase 1 periodic assessment | `../reports/1405-06-16-task-specification.md` |
| Diagnostic action versus final reporting | Initially treated preparation of the report as the diagnostic action; later selected the correct evidence-producing action | Diagnose a new failure by separating action, inspection, and final report | Phase 1 periodic assessment | `../reports/1405-06-10-agent-loop.md` |
| Information categories versus mandatory artifacts | Questions initially assumed every large project needs six separate locations; corrected to need-based placement and conventional discovery | Classify which artifacts a new project actually needs without creating every category | Phase 1 periodic assessment | `../reports/1405-06-12-prompts-and-repository-instructions.md` |
| Skill versus tool | Asked for clarification, then correctly selected a reusable workflow that coordinates existing tools | Explain and apply the distinction in a different domain | Phase 1 periodic assessment | `../reports/1405-06-12-prompts-and-repository-instructions.md` |
| Bounded acceptance criteria | Initially preferred a broad request using `make all tests pass`; later selected and justified focused scope and observable evidence | Improve a weak change-authorized prompt without over-broad verification | Phase 1 periodic assessment | `../reports/1405-06-12-prompts-and-repository-instructions.md` |

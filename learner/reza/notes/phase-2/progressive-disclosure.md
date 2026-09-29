# Progressive Disclosure and Context Efficiency

## Previous-note recap

Package organization separates core rules, conditional references, scripts, assets, and examples.

## Concept: progressive disclosure

**Definition:** Progressive disclosure means revealing information gradually, when it becomes relevant.

**Application to agent skills:** Load instructions and supporting material when the current task or decision requires them. Package organization determines where information lives; progressive disclosure determines when the agent reads it.

### Three stages of access

| Stage | Information available | Purpose |
| --- | --- | --- |
| Discovery | A compact skill description | Decide whether the skill applies to the task. |
| Skill use | Core instructions | Understand the required inputs, workflow, boundaries, and expected output. |
| A conditional decision | Relevant supporting references | Obtain the details needed for that part of the workflow. |

For example, the core can say: “When event ordering is ambiguous, read the timestamp rules before classifying the sequence.” This gives the agent both a loading condition and a reason to read the reference.

## Related concept: context efficiency

**Definition:** Context efficiency means using the available context for information that helps the agent perform the task correctly.

Progressive disclosure supports context efficiency by leaving unrelated detail unloaded. The aim is sufficient relevant context. A shorter prompt is not an improvement if it omits required evidence, decision rules, or safety boundaries.

## How to decide what to load

1. **Keep always-needed rules in the core.** A read-only audit must state there that modifying or deleting records is forbidden.
2. **Put conditional detail in references.** Give each reference an explicit loading condition in the core workflow.
3. **Read the reference before making the dependent decision.** A link alone is insufficient; the agent needs to know when its contents are required.
4. **Handle missing information explicitly.** Obtain the information or report the resulting limitation before drawing a conclusion that depends on it.

A reference index helps only if its links work and the workflow points to the relevant reference.

## Worked example

A parcel-audit skill has 20 pages describing regional delivery events.

| Situation | What the agent reads or does | Why |
| --- | --- | --- |
| Every audit | Read core instructions requiring a parcel ID, records, expected stages, read-only behavior, and a report of evidence gaps. | These requirements apply on every run. |
| Domestic parcel | Read the relevant domestic event definitions. | These definitions support classification of domestic events. |
| Cross-border parcel | Read the relevant delivery-event definitions and customs definitions. | Customs events require additional interpretation. |
| Region unknown | Obtain the region or report that classification is limited. | The agent cannot reliably select the applicable definitions. |

This is progressive disclosure because the task determines which details become necessary. It improves context efficiency when the agent reaches a supported conclusion without reading unrelated regional definitions.

## Missing inputs: which work must pause?

A missing input blocks conclusions and actions that depend on it, rather than every useful step. For a warranty claim with no region, the agent can inspect supplied records or request the region, but cannot determine eligibility under regional rules. If the region cannot be obtained, report the limitation instead of guessing. Independent checks may continue when the contract permits them.

## Practice and evidence

Use the [recording-lifecycle auditor contract draft](../../experiments/recording-lifecycle-auditor-contract.md):

1. Classify its contents as always-needed instructions, conditional reference material, executable support, or output templates.
2. Write one loading condition for each proposed reference.
3. Explain which decisions cannot be supported if each reference is missing.
4. For one scenario, describe what the agent should read and what can stay unloaded.

**Evaluation criteria:** Check that required rules remain visible, references are read before dependent decisions, and unrelated material stays unloaded. Compare correctness and unnecessary reads together.

**Evidence status:** This is a planned exercise, not completed evidence.

## Common mistakes

- Moving essential rules out solely to shorten the core.
- Linking a reference without saying when it is needed.
- Reading every reference on every run.
- Summarizing evidence so aggressively that its source or uncertainty disappears.

Validation on 1405-07-07: 3/3 correct; conceptual outcome Demonstrated. The missing-input refinement was coach-explained; practical transfer remains unverified. [Report](../../reports/1405-07-07-progressive-disclosure.md).

## Summary

Load enough information for the current decision. Keep essential rules visible, link conditional detail with clear loading conditions, and evaluate correctness alongside context use. Missing inputs block dependent decisions; request the information or report the limitation.

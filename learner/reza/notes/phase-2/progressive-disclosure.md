# Progressive Disclosure and Context Efficiency

## Previous-note recap

Package organization separates core rules, conditional references, scripts, assets, and examples.

## Essential mental model

Progressive disclosure means loading information when a decision needs it. A compact discovery description helps select the skill; the core then explains the workflow and when to open supporting files. The aim is sufficient relevant context, not the shortest possible prompt.

Keep unconditional safety rules in the core. A read-only audit must not depend on the agent opening an optional reference to learn that deletion is forbidden. Conditional details need explicit entry points: “When event ordering is ambiguous, read the timestamp rules before classifying the sequence.”

## Worked example

A parcel audit has 20 pages describing regional delivery events. The core requires a parcel ID, records, expected stages, and a report of evidence gaps. For domestic parcels, load only domestic event definitions. For cross-border parcels, also load customs definitions. If the region is unknown, obtain it or report that classification is limited; do not choose a convenient table.

A reference index saves context only if links work and the workflow names the relevant branch. A smaller core that hides essential decisions is worse than a slightly longer complete core.

## Practice and evidence

Take the [contract draft](../../experiments/recording-lifecycle-auditor-contract.md). Mark each rule as always needed, conditionally needed, executable support, or output template. Write one loading condition for each proposed reference. Explain which decisions become impossible if that reference is missing. This is a planned exercise, not completed evidence.

When evaluating, compare both correctness and unnecessary reads. A lower context count does not justify losing required evidence or safety boundaries.

## Common mistakes

- Moving essential rules out solely to shorten the core.
- Linking a reference without saying when it is needed.
- Reading every reference on every run.
- Summarizing evidence so aggressively that its source or uncertainty disappears.

## Summary

Load enough information for the current decision. Keep essential rules visible, link conditional detail with clear loading conditions, and evaluate correctness alongside context use.

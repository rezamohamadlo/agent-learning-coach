# Agent Learning Coach

Agent Learning Coach is a reusable AI-agent skill that turns a personal learning roadmap into supervised, evidence-based study. It helps a learner choose the next useful topic, understand notes, practice with realistic exercises, demonstrate competence, track progress against a timetable, and revisit weaknesses before they are forgotten.

The project is designed for people learning how AI agents work while building practical judgment about prompts, instructions, skills, tools, permissions, verification, evaluation, and agent workflows.

## Why this project exists

A checklist can show what someone intended to study, but it cannot prove what they understand. This coach treats a roadmap as both a plan and an evidence record:

```text
Roadmap position
      ↓
Focused learning note
      ↓
Discussion and practice
      ↓
Independent assessment
      ↓
Evidence, gaps, and progress update
      ↓
Periodic retention review
```

An item is not completed merely because it was explained or read. Completion normally requires independent explanation and application.

## What it provides

- Roadmap orientation and next-step planning
- Focused teaching and note discussion
- Guided practice followed by independent assessment
- Multiple-choice checks that progress from recall to application and transfer
- Corrective teaching and fresh reassessment when understanding is incomplete
- Evidence levels from `Not started` through `Retained`
- Progress snapshots after completed items
- Weekly timetable comparisons without invented precision
- A private strengths-and-gaps profile based on real questions, mistakes, corrections, and artifacts
- Periodic assessments, normally at each phase boundary
- Historical session reports that preserve learning evidence

The bundled reusable curriculum currently covers Phase 1 agent foundations. The roadmap extends beyond Phase 1 so later curriculum and practical work can be added as the learner advances.

## Evidence model

The coach uses these levels consistently:

| Level | Meaning |
|---|---|
| Not started | No meaningful attempt or evidence |
| Introduced | The concept was explained or demonstrated |
| Practiced | Guided work was completed with material help |
| Provisional | Study may continue, but a documented gap remains |
| Demonstrated | The learner independently applied the concept and explained important decisions |
| Retained | The learner demonstrated it again later or in a different context |

Roadmap checkboxes normally require `Demonstrated` evidence. A periodic review can raise a concept to `Retained` or expose a new retention gap without erasing the earlier evidence.

## Repository layout

```text
agent-learning-coach/
├── SKILL.md                         Main skill instructions and routing
├── agents/openai.yaml               User-facing skill metadata
├── assets/roadmap-template.md       Starting roadmap for a new learner
├── references/
│   ├── coaching-protocol.md         Session, assessment, and reporting rules
│   ├── progress-reporting.md        Per-step and timetable progress rules
│   ├── periodic-assessments.md      Retention-review workflow
│   └── curriculum/phase-1/          Reusable foundation notes
└── learner/                         Private, Git-ignored learner state
    ├── ROADMAP.md
    ├── notes/
    ├── experiments/
    ├── reports/
    └── reviews/strengths-and-gaps.md
```

Reusable curriculum and coaching behavior are tracked in Git. Personal answers, misconceptions, progress, and reports stay under the ignored `learner/` directory.

## Getting started

### 1. Get the repository

```bash
git clone https://github.com/rezamohamadlo/agent-learning-coach.git
cd agent-learning-coach
```

Keep this checkout as the editable learning workspace. Make its reusable skill available to your agent using the skill-installation method supported by your environment. If Codex provides `$skill-installer`, it can install a skill from the GitHub repository; otherwise, use your Codex environment's configured local skills directory.

Keep learner data in this source checkout or another explicitly chosen private workspace—not in a published skill bundle.

### 2. Initialize private learner state

On PowerShell:

```powershell
New-Item -ItemType Directory -Path learner -Force
Copy-Item assets/roadmap-template.md learner/ROADMAP.md
```

On macOS or Linux:

```bash
mkdir -p learner
cp assets/roadmap-template.md learner/ROADMAP.md
```

Edit the start date, target duration, goals, and weekly plan so schedule comparisons have meaningful inputs.

### 3. Start or resume coaching

Invoke the skill from the repository checkout:

```text
Use $agent-learning-coach to continue my roadmap.
```

The coach will inspect the roadmap and recent evidence, propose a tentative current position, and ask you to confirm it before beginning a full session.

Useful requests include:

```text
Use $agent-learning-coach to explain my current position and next milestone.

Use $agent-learning-coach to discuss the section about tool safety without starting an assessment.

Use $agent-learning-coach to assess whether I understand the current roadmap item.

Use $agent-learning-coach to review my progress against the weekly plan.
```

## A typical session

1. The coach reads the roadmap, relevant note, and latest report.
2. You confirm or correct the inferred learning position.
3. The coach states one objective, estimated effort, and observable completion evidence.
4. You read and discuss a concise learning note.
5. You complete practice and an assessment.
6. The coach explains the evidence, teaches any gap, and reassesses with a new scenario.
7. Only demonstrated outcomes are marked complete.
8. The roadmap, session report, strengths/gaps profile, and schedule snapshot are updated when warranted.

The coach does not monitor progress in the background. Supervision resumes when you invoke the skill again.

## Progress and periodic review

After a completed roadmap item, the learner should see a compact snapshot like this:

```text
Completed: <item and evidence level>
Phase progress: Learn <x/y>; Build <x/y>; Exit <x/y>
Schedule: <status and supporting evidence or uncertainty>
Evidence trend: <demonstrated strengths and remaining work>
Next checkpoint: <one required action>
```

Schedule labels are `Ahead`, `On track`, `Behind`, `Replanned`, or `Unknown`. The coach uses `Unknown` when dates or weekly targets are too vague for an honest comparison.

Periodic assessments normally happen before a phase is declared complete. They use fresh questions and scenarios based on:

- representative phase outcomes;
- unresolved gaps;
- earlier wrong answers and successful corrections;
- learner questions that revealed genuine confusion; and
- older prerequisites that need a retention check.

Asking a thoughtful question is not automatically a weakness. Questions that detect ambiguity or connect concepts may be evidence of strong reasoning.

## Getting the most from the coach

- Make weekly targets observable. “Study tools” is a theme; “explain read-only versus mutating tools and classify three examples” is measurable.
- Ask questions before assessment. Discussion is for learning and does not count as a failed attempt.
- Use `I don't know` rather than guessing. It signals that teaching is needed.
- Explain why you chose an answer. Correct reasoning is stronger evidence than a lucky selection.
- Let the coach preserve corrected gaps as retention candidates instead of hiding them.
- Use real project exercises only when they are safely bounded and authorized.
- Keep secrets and sensitive project details out of learner reports.

## Maintaining the skill

When working inside an active coaching conversation, prefix a request with `@#` to route it to skill maintenance rather than treating it as an assessment response:

```text
@# refine the periodic assessment report so it shows retention evidence
```

Maintenance should update the editable source, validate the result, and synchronize the installed copy when authorized. It must not commit or push unless the user explicitly requests that action.

## Scope and safety

The coach may inspect an authorized project for a bounded exercise, but it does not gain permission to refactor unrelated code, publish content, contact other people, install tools, or perform external mutations. Project changes require separate authorization and should be verified against explicit acceptance criteria.

## License

This project is available under the [MIT License](LICENSE).

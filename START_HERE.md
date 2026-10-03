# Start Here

Use this path to turn an AI idea into an operational decision in 30 minutes.

You do not need to choose a model, vendor, or architecture first. You need one real process, one accountable owner, and enough clarity to decide whether the workflow should move forward.

## What You Will Leave With

By the end of this review, you should have:

- a defined operational problem;
- a named process owner;
- an initial criticality level;
- explicit AI boundaries;
- a source-of-truth decision;
- minimum traceability requirements;
- a next decision: proceed, revise, or stop.

Use a fictional or sanitized scenario if you are evaluating the playbook publicly.

Open the [30-Minute Operational AI Assessment](templates/30-minute-assessment.md), copy it into your working notes, and use that single worksheet to keep every answer and the final gate decision in one place.

This path is designed for someone who already understands the process being evaluated. If basic process facts are unknown, choose `revise` rather than extending the session until an assumption looks complete.

## The 30-Minute Path

### Minutes 0-5: Name The Process

Write one sentence for each question:

1. Which process are you trying to improve?
2. Which decision or task should AI support?
3. Who owns the process today?
4. Which measurable problem should improve?

If the team cannot describe the process without mentioning AI, pause here and read [Process Before AI](docs/01-process-before-ai.md).

Record the answers in **Minutes 0-5: Process** in the assessment worksheet.

### Minutes 5-12: Complete The Use Case Canvas

Use the [AI Use Case Canvas](templates/ai-use-case-canvas.md) as a reference. In the assessment worksheet, complete at least:

- business context;
- decision or task;
- source of truth;
- owner and approver;
- one success metric;
- fallback plan.

Do not optimize for completeness. Capture the assumptions that would make the workflow unsafe or ineffective if they were wrong.

### Minutes 12-18: Classify Criticality

Use the [Criticality Matrix](docs/04-criticality-matrix.md).

Ask:

- Who is affected if the AI is wrong?
- Can the action be reversed?
- Does it affect money, safety, rights, contracts, or customers?
- Is AI assisting, recommending, approving, or executing?

Choose the highest plausible level when evidence is incomplete.

Record the level and its reason in **Minutes 12-18: Criticality** in the assessment worksheet.

### Minutes 18-24: Define Boundaries And Sources

Use the [Agent Charter](templates/agent-charter.md) as a reference when the workflow can call tools or influence actions. Separate every relevant action into:

- allowed;
- human approval required;
- denied.

If the workflow retrieves knowledge, review [RAG Source Governance](templates/rag-source-governance.md) to name the source owner, scope, freshness rule, and conflict behavior.

Record only the boundaries and source rules relevant to this use case in **Minutes 18-24: Boundaries And Sources** in the assessment worksheet.

### Minutes 24-28: Define Evidence

Use the [Decision Log Template](templates/decision-log-template.md) as a reference to decide what must be reconstructable later.

At minimum, retain:

- use case and criticality;
- input and source references;
- output and reason;
- model or system version;
- final decision;
- human review status when required.

Record the evidence requirements in **Minutes 24-28: Evidence** in the assessment worksheet.

### Minutes 28-30: Make The Gate Decision

Choose one outcome:

| Outcome | Use It When | Next Step |
|---|---|---|
| Proceed | Owner, source, boundaries, controls, and metric are clear | Plan a limited pilot |
| Revise | The use case is valuable, but one or more controls are unresolved | Assign owners and close the gaps |
| Stop | The process, authority, source, or acceptable risk cannot be defined | Do not automate yet |

Record the decision and its reason. A decision to stop is a valid operational result.

Complete **Minutes 28-30: Gate Decision** in the assessment worksheet, including the next concrete action and an owner for any unresolved gap.

## Minimum Review Before A Pilot

- [ ] Process owner is named.
- [ ] Source of truth is identified.
- [ ] Criticality is classified.
- [ ] Human review points are explicit.
- [ ] Allowed and denied actions are documented.
- [ ] Success metric is measurable.
- [ ] Required evidence can be logged.
- [ ] Fallback path exists.
- [ ] Gate decision and next action are recorded.

For build, pilot, and production checks, continue with the [Operational AI Rollout Checklist](templates/rollout-checklist.md).

## See The Method In Practice

The repository currently includes fictional examples for:

- [CRM next best action](examples/crm-next-best-action/README.md);
- [customer support monitoring](examples/customer-support-monitoring/README.md);
- [knowledge base RAG](examples/knowledge-base-rag/README.md).

Run the local [decision-log demo](src/demo_decision_log.py) to see a medium-criticality workflow require human review:

```bash
python src/demo_decision_log.py
```

The next release will connect one example end to end, from the completed canvas through the final decision log.

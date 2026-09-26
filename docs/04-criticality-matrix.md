# Criticality Matrix

Criticality should be an architecture decision.

Different AI use cases need different levels of control depending on what happens when the system is wrong.

## Risk Levels

| Level | Example | AI Role | Required Control |
|---|---|---|---|
| Low | Internal policy lookup | Assist | Source citation and user verification |
| Medium | Support ticket prioritization | Recommend | Human review before execution |
| High | Credit, safety, critical infrastructure | Influence or execute | Strong validation, logs, monitoring, formal approval |

## Questions To Classify Criticality

- What happens if the AI is wrong?
- Who is affected?
- Can the error be reversed?
- Is the decision regulated?
- Does it involve money, safety, legal, or customer impact?
- Does the AI recommend, approve, or execute?
- Is a human in the loop before the action?
- What evidence is required after the fact?

## Architecture Implications

Higher criticality may require:

- private or controlled runtime;
- stricter data boundaries;
- human validation;
- model evaluation;
- fallback flows;
- longer log retention;
- monitoring and alerts;
- approval workflows;
- rollback design.

## Practical Rule

Ask "what happens when this agent is wrong?" before choosing the model.


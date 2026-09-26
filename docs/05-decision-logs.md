# Decision Logs

In operational AI, logs are not only technical records.

They are evidence.

## Why Logs Matter

When AI influences a decision, the organization may need to reconstruct:

- what data was used;
- what rule was applied;
- what source was retrieved;
- what model generated the output;
- who requested it;
- who approved it;
- what action was taken;
- why the system stopped or escalated.

## Minimum Decision Log

```json
{
  "decision_id": "dec_001",
  "timestamp": "2026-09-25T12:00:00Z",
  "use_case": "support_ticket_priority",
  "actor": "agent.monitoring.v1",
  "user_context": "support_supervisor",
  "input_refs": ["ticket_123", "policy_sla_v4"],
  "model": "example-model",
  "prompt_version": "priority_classifier_v1",
  "retrieved_sources": ["sla_policy_v4"],
  "output": "high_priority",
  "confidence": "medium",
  "decision": "human_review_required",
  "reason": "Potential SLA breach detected, but customer impact requires supervisor validation."
}
```

## Retention

Retention should depend on criticality.

| Criticality | Suggested Retention |
|---|---|
| Low | 30 to 90 days |
| Medium | 180 days to 1 year |
| High | 2+ years or regulatory requirement |

## Practical Rule

If the decision cannot be reconstructed, the system is not ready for operational use.


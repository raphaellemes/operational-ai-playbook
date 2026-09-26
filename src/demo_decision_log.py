from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import json


@dataclass
class UseCase:
    name: str
    criticality: str
    ai_role: str
    reversible_error: bool
    human_validation: bool
    affects_customer: bool


@dataclass
class DecisionLog:
    decision_id: str
    timestamp: str
    use_case: str
    criticality: str
    actor: str
    input_refs: list[str]
    output: str
    decision: str
    reason: str


def classify_decision(use_case: UseCase) -> tuple[str, str]:
    if use_case.criticality == "high":
        return (
            "formal_approval_required",
            "High-impact AI workflow requires stronger approval, monitoring, and traceability.",
        )

    if use_case.human_validation:
        return (
            "human_review_required",
            "AI can recommend priority, but execution requires human validation.",
        )

    if use_case.affects_customer:
        return (
            "human_review_required",
            "Customer-impacting recommendation should be reviewed before execution.",
        )

    if use_case.ai_role in {"execute", "approve"} and not use_case.reversible_error:
        return (
            "human_review_required",
            "AI can recommend, but execution is not safely reversible.",
        )

    return (
        "allowed_with_logging",
        "Workflow can proceed if logs, source references, and ownership are maintained.",
    )


def build_log(use_case: UseCase) -> DecisionLog:
    decision, reason = classify_decision(use_case)
    return DecisionLog(
        decision_id="dec_001",
        timestamp=datetime.now(timezone.utc).isoformat(),
        use_case=use_case.name,
        criticality=use_case.criticality,
        actor="agent.operational-support.v1",
        input_refs=["ticket_123", "sla_policy_v4"],
        output="priority_recommendation: high",
        decision=decision,
        reason=reason,
    )


if __name__ == "__main__":
    use_case = UseCase(
        name="support_ticket_priority",
        criticality="medium",
        ai_role="recommend",
        reversible_error=True,
        human_validation=True,
        affects_customer=True,
    )

    log = build_log(use_case)

    print(f"Decision: {log.decision}")
    print(f"Criticality: {log.criticality}")
    print(f"Reason: {log.reason}")
    print()
    print(json.dumps(asdict(log), indent=2))

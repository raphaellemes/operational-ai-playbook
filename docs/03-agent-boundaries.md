# Agent Boundaries

An AI agent is not just a chat interface.

When an agent can call tools, access data, trigger workflows, or interact with systems, it becomes part of the operational architecture.

## Boundary Questions

Before deploying an agent, define:

- What is its goal?
- What can it read?
- What can it write?
- What can it execute?
- Which APIs can it call?
- Which credentials does it use?
- Which actions require human confirmation?
- When must it stop?
- How is its behavior audited?

## Allowed, Denied, Escalated

Every agent action should fit one of three groups:

| Category | Meaning | Example |
|---|---|---|
| Allowed | Agent can execute directly | Summarize a ticket |
| Escalated | Agent can recommend, human approves | Prioritize a high-impact case |
| Denied | Agent cannot execute | Change billing rules |

## Credentials And Access

If an agent can see a credential, it may treat that credential as an available tool.

Use:

- scoped credentials;
- least privilege;
- separate runtime identities;
- environment segregation;
- tool allowlists;
- network egress controls;
- secret scanning.

## Practical Rule

Autonomy without boundaries is not intelligence. It is ungoverned execution.


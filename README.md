# Operational AI Playbook

Practical playbook for designing operational AI with RAG, agents, knowledge governance, traceability, and process engineering.

This repository is a public, vendor-neutral reference for teams that want to move from AI experiments to AI-supported operations.

The main idea is simple:

> Good prompts help. Good operating systems make AI useful.

## Why This Exists

Many AI initiatives start with the model, the prompt, or the tool.

In real operations, that is rarely enough.

Before an AI agent can support decisions, retrieve knowledge, classify risks, or trigger workflows, the organization needs clarity about:

- which process the AI supports;
- which source is trusted;
- which decision is being influenced;
- who owns the rule;
- where human validation is required;
- how the answer can be reconstructed later;
- how value and risk are measured.

This playbook turns those questions into practical documents, templates, and examples.

## What Is Inside

```text
docs/
  01-process-before-ai.md
  02-rag-governance.md
  03-agent-boundaries.md
  04-criticality-matrix.md
  05-decision-logs.md

templates/
  ai-use-case-canvas.md
  agent-charter.md
  rag-source-governance.md
  decision-log-template.md
  rollout-checklist.md

examples/
  customer-support-monitoring/
  crm-next-best-action/
  knowledge-base-rag/

src/
  demo_decision_log.py
```

## Contributions Are Welcome

This project is intentionally open for collaboration.

You can contribute with:

- fictional operational AI use cases;
- RAG governance patterns;
- agent boundary examples;
- decision log improvements;
- risk and criticality checklists;
- diagrams;
- translations;
- small demos;
- critiques from real implementation experience.

Start with [CONTRIBUTING.md](CONTRIBUTING.md) and the open issues labeled `good first issue` or `help wanted`.

## Core Principles

### 1. Process Before Prompt

A prompt should not compensate for an unclear process.

If the workflow has no owner, source, rule, metric, or escalation path, the AI layer will only accelerate ambiguity.

### 2. RAG Is Governance, Not Only Retrieval

RAG is not just about finding the most similar chunk.

Operational RAG needs source ownership, scope, permission rules, freshness criteria, and traceability.

### 3. Agents Need Boundaries

An agent should operate inside a defined charter:

- goal;
- allowed actions;
- denied actions;
- input sources;
- tools;
- permissions;
- escalation rules;
- audit requirements.

### 4. Criticality Drives Architecture

Not every AI workflow needs the same level of control.

Low-risk workflows can be flexible. High-impact workflows require stronger validation, observability, rollback, and human accountability.

### 5. Logs Are Part Of The Product

If a decision cannot be reconstructed, it cannot be governed.

For operational AI, logs are not only technical telemetry. They are evidence.

## Example Use Cases

This repository uses fictional examples inspired by common operational scenarios:

- customer support monitoring;
- CRM next-best-action;
- knowledge base RAG;
- operational decision support.

No confidential company data is included.

## Quick Demo

Run a small local example that classifies an AI use case and produces an auditable decision log:

```bash
python src/demo_decision_log.py
```

Expected output:

```text
Decision: human_review_required
Criticality: medium
Reason: AI can recommend priority, but execution requires human validation.
```

## Who This Is For

- operations leaders;
- product operations teams;
- CRM and CX teams;
- AI transformation teams;
- solution architects;
- data and knowledge governance teams;
- builders implementing RAG and agentic workflows in business operations.

## Suggested Starting Point

1. Read [Process Before AI](docs/01-process-before-ai.md).
2. Use the [AI Use Case Canvas](templates/ai-use-case-canvas.md).
3. Classify the workflow with the [Criticality Matrix](docs/04-criticality-matrix.md).
4. Define agent boundaries with the [Agent Charter](templates/agent-charter.md).
5. Design traceability with the [Decision Log Template](templates/decision-log-template.md).

## Roadmap

See [ROADMAP.md](ROADMAP.md) for the next planned versions and collaboration opportunities.

## License

MIT License.

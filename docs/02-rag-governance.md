# RAG Governance

RAG is not memory.

RAG is a retrieval strategy that brings external information into the model context. In enterprise use, that external information needs governance.

## Common Failure Mode

Many RAG projects focus on:

- chunking;
- embeddings;
- vector search;
- prompt formatting;
- answer generation.

Those are important, but they do not answer operational questions:

- Can this document be used by this person?
- Is this source current?
- Who owns this content?
- What happens when two sources disagree?
- Should the answer cite the source?
- Should the system answer or declare insufficient evidence?

## Governed RAG Needs

### Source Ownership

Every source should have an owner responsible for quality, freshness, and retirement.

### Scope

Define where the source can be used:

- by business unit;
- by client;
- by process;
- by user role;
- by geography;
- by risk level.

### Freshness

Define how outdated content is handled.

Example:

```text
If a policy document is older than 180 days and has no active owner, the system may retrieve it but must mark it as stale.
```

### Answer Anchoring

The system should distinguish:

- answer supported by source;
- partial answer;
- source conflict;
- no sufficient evidence.

### Traceability

Every answer should retain:

- query;
- retrieved source identifiers;
- source versions;
- model version;
- prompt/template version;
- user/context;
- final answer;
- confidence or evidence status.

## Practical Rule

RAG should not create a second truth. It should expose, govern, and make usable the truth the organization already decided to trust.


# Example: Knowledge Base RAG

This fictional example shows how to govern a RAG workflow for internal knowledge.

## Process

Employees ask questions about internal procedures.

The AI system retrieves relevant documents and answers with source references.

## Main Risk

The answer may be correct for the wrong context.

Example:

- correct policy;
- wrong business unit;
- outdated version;
- user not authorized for that client or scope.

## Required Governance

- source owner;
- scope by user role;
- document version;
- freshness rule;
- source citation;
- insufficient-evidence response;
- retrieval log.

## Expected Behavior

If the source is missing or conflicting, the system should not improvise.

It should declare the gap and escalate to the source owner or process owner.


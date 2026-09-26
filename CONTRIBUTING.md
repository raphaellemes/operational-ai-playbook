# Contributing

Thanks for considering a contribution.

This repository is meant to be a practical, vendor-neutral reference for operational AI, RAG, agents, governance, traceability, and process engineering.

You do not need to contribute code only. Documentation, examples, templates, diagrams, and critiques are all useful.

## Good Contributions

Helpful contributions usually fit one of these categories:

- a fictional but realistic operational AI use case;
- a reusable template;
- an architecture pattern;
- a governance checklist;
- a decision log improvement;
- a Mermaid diagram;
- a small demo;
- a translation;
- a correction or clarification.

## Ground Rules

Please do not include:

- confidential company information;
- real customer data;
- personal data;
- production credentials;
- API keys, tokens, cookies, or session data;
- proprietary prompts, policies, or documents;
- content copied from private internal systems.

Use fictional examples or sanitized patterns.

## Security Rules For Contributions

This project is public by design, so contributions must be safe to review and run in isolation.

Do not add:

- GitHub Actions that deploy, call external services, or require secrets;
- scripts that read from home folders, Desktop folders, cloud folders, or private repositories;
- self-hosted runner configuration;
- submodules or symlinks to private projects;
- network calls unless they are clearly documented and optional;
- package installation steps that run post-install scripts without a clear reason;
- binary files that cannot be reviewed.

If you add code, it must run with synthetic data and without external credentials.

Maintainers should review code contributions before running them locally. When testing community code, use a disposable folder or environment with no `.env` file and no access to private projects.

## How To Contribute

1. Pick an open issue or create a new one.
2. Fork the repository.
3. Create a branch with a clear name.
4. Make a focused change.
5. Open a pull request.

## Pull Request Checklist

Before opening a pull request, check:

- [ ] The contribution uses fictional or public information only.
- [ ] The contribution does not read local folders or private repositories.
- [ ] The contribution does not require secrets or credentials.
- [ ] The contribution does not add a self-hosted runner or unsafe workflow.
- [ ] The change is aligned with operational AI, RAG, agents, governance, traceability, or process engineering.
- [ ] The writing is clear and practical.
- [ ] Examples can be reused by other teams.
- [ ] If code was added, it runs locally without external secrets.

## Writing Style

Prefer:

- clear language;
- practical examples;
- simple tables;
- explicit assumptions;
- operational trade-offs;
- traceability and accountability.

Avoid:

- hype;
- vendor lock-in;
- vague statements;
- unverifiable claims;
- exposing real internal processes.

## Discussion Before Big Changes

For large changes, open an issue or discussion first.

Examples:

- new technical demo;
- new framework structure;
- new methodology;
- major rewrite of the README;
- new domain-specific section.

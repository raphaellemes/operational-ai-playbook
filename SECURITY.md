# Security Policy

## Reporting Security Issues

If you find a security issue in this repository, please do not publish exploit details in a public issue.

Open a private security advisory on GitHub or contact the repository maintainer.

## Scope

This project is mostly documentation and examples.

Still, security matters because the subject includes:

- AI agents;
- credentials;
- tool access;
- data governance;
- decision logs;
- operational workflows.

## Repository Isolation Rules

This public repository must remain isolated from private workspaces and local machines.

The repository must not include:

- secrets, credentials, tokens, cookies, or session data;
- real customer, employee, company, financial, or operational data;
- scripts that read local user folders such as Desktop, Documents, cloud-sync folders, or private workspaces;
- symlinks or submodules pointing to private repositories;
- self-hosted runner configuration;
- workflows that require secrets or deploy to external systems;
- binary artifacts that cannot be reviewed.

## GitHub Actions Policy

GitHub Actions should remain disabled or limited to safe, read-only validation.

If Actions are enabled in the future:

- use GitHub-hosted runners only;
- use read-only permissions by default;
- do not use repository secrets;
- do not run workflows from untrusted pull requests with elevated permissions;
- do not deploy from this repository;
- do not connect to private infrastructure.

## Reviewing Community Contributions

Before running community code locally:

1. Review the diff first.
2. Check for file-system access, network calls, package install hooks, and shell commands.
3. Run in an isolated temporary folder or disposable environment.
4. Do not provide `.env` files or credentials.
5. Do not run code from a pull request against private company repositories.

## Do Not Submit Sensitive Data

Please do not include:

- credentials;
- API keys;
- customer data;
- personal data;
- internal company policies;
- proprietary prompts;
- real production logs.

Use synthetic or sanitized examples only.

## Maintainer Checklist For Pull Requests

- [ ] No secrets or sensitive data.
- [ ] No access to private local paths.
- [ ] No self-hosted runner or privileged workflow.
- [ ] No unexplained network calls.
- [ ] No unreviewable binary artifact.
- [ ] Code examples run with synthetic data only.

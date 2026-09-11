# New ChatGPT/Codex Account Setup

Reading this repository does not grant a new ChatGPT/Codex account GitHub write access. Repository access and Git authentication must be configured separately. Never paste a token, password, cookie, private key or service-account JSON into chat, source files or commits.

## 1. Open the same repository

Clone or open:

```text
https://github.com/OuYangThermal/OuYangThermal.github.io
```

Current Git transport is HTTPS. If cloning:

```bash
git clone https://github.com/OuYangThermal/OuYangThermal.github.io.git
cd OuYangThermal.github.io
```

If using an existing working directory, do not clone over it and do not discard its uncommitted files.

## 2. Read-only identity and repository checks

```bash
git status --short --branch
git remote -v
git branch -vv
git log -5 --oneline --decorate
git config --get user.name
git config --get user.email
```

The remote must point to `OuYangThermal/OuYangThermal.github.io`. Git author name/email do not prove GitHub authentication or write permission.

## 3. Confirm GitHub authentication

Preferred browser-based GitHub CLI flow, if `gh` is installed:

```bash
gh auth status
gh auth login
gh repo view OuYangThermal/OuYangThermal.github.io
```

Choose GitHub.com and HTTPS, then complete the browser/device authorization shown by the CLI. Do not store or document the resulting credential in this repository. On systems using Git Credential Manager, a normal authenticated Git operation may open a browser login instead.

## 4. Confirm access without writing

```bash
git fetch --prune origin
git ls-remote --heads origin
git status --short --branch
```

These commands test read access and update remote references without modifying published content. Review any ahead/behind state before working.

## 5. Check repository permissions safely

If GitHub CLI is available and authenticated, inspect repository metadata and Pages settings read-only. In the GitHub web interface, confirm that the signed-in identity has the intended repository role. Do not test permission by pushing an arbitrary commit to `main`.

Before the first real push:

- Confirm the user explicitly authorized that change and deployment.
- Pull/fetch and ensure the intended base is current.
- Review `git status`, `git diff`, `git diff --cached` and the exact branch.
- Run the build and tests in `docs/CODEX_OPERATIONS.md`.
- Push only the reviewed commit to the intended remote and branch.

## 6. If authentication fails

- Run `gh auth status` and reauthenticate with `gh auth login`, or use the standard browser sign-in prompted by Git Credential Manager.
- Confirm that the GitHub identity has access to the repository.
- Never put a personal access token in a remote URL, file, prompt, shell history example or documentation.
- If SSH is intentionally adopted later, configure the key outside this repository and update this document only with the transport method, never the private key.

## 7. Codex account boundary

A new Codex account may have different local tools, approvals, GitHub credentials, automations and connected services. Recheck each capability. The paused content automation is not permission to recreate or resume it. Search Console and Formspree access also remain separate account permissions.

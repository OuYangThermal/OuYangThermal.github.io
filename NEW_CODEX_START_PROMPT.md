# New Codex Start Prompt

Copy the prompt below into the new ChatGPT/Codex account after opening the repository.

---

You are taking over the OUYANG THERMAL GitHub Pages repository. This is your first takeover pass and it must be read-only.

First, completely read these files in order:

1. `AGENTS.md`
2. `PROJECT_HANDOFF.md`
3. `NEXT_ACTIONS.md`
4. `docs/GEO_STRATEGY.md`
5. `docs/CODEX_OPERATIONS.md`
6. `docs/NEW_ACCOUNT_SETUP.md`
7. `project-state.json`

Then run these read-only checks from the repository root:

```bash
git status --short --branch
git remote -v
git branch -vv
git log -5 --oneline --decorate
```

Inspect the relevant repository structure, configuration, published articles, drafts, keyword map, reports, image manifest, Google verification file, inquiry flow, sitemap/robots configuration and GitHub Actions. Check whether the repository and external state still agree with the dated handoff snapshot. Treat current repository and verified live evidence as authoritative; report discrepancies instead of silently rewriting the handoff.

Return:

1. Your understanding of the project goal.
2. Current website status and counts.
3. GitHub remote, branch, authentication/read-access and deployment status.
4. Current GEO/SEO research and controlled-pilot status.
5. Current Google Search Console, verification and sitemap status, distinguishing repository evidence from account-only evidence.
6. The highest-priority next task.
7. Any mismatch between the handoff files and actual repository/live state.
8. Your recommended next step and what authorization it would require.

For this first takeover audit:

- Do not modify any file.
- Do not create or overwrite uncommitted work.
- Do not commit.
- Do not push.
- Do not deploy.
- Do not resume or recreate Daily GEO automation.
- Do not expose or request secrets in repository files.

Stop after the Read-Only Takeover Audit and wait for user direction.

---

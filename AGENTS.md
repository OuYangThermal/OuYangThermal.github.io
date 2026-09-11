# Repository Instructions

## Mandatory takeover and safety workflow

1. Read `PROJECT_HANDOFF.md` before changing this repository. Then read `NEXT_ACTIONS.md`, `docs/GEO_STRATEGY.md`, `docs/CODEX_OPERATIONS.md`, `docs/NEW_ACCOUNT_SETUP.md`, and `project-state.json` as relevant.
2. Run `git status --short --branch` before editing. Preserve all user changes and untracked work; never overwrite, discard, clean, or reset work you did not create.
3. Do not delete a published page or change an existing public URL unless the user explicitly approves the migration and redirect plan.
4. Permanently preserve `googlebd2df6f2d347ec36.html` at the repository root.
5. Do not break or casually redesign `sitemap.xml`, `robots.txt`, canonical output, structured data, the private inquiry flow, or existing contact routes.
6. Do not change WhatsApp `+86 133 6790 9790`, email `5672306@gmail.com`, telephone links, or the Formspree endpoint unless the user explicitly requests it.
7. Never invent customer cases, customers, test data, material performance, certifications, authorizations, search volume, search-console results, rankings, citations, or supplier/manufacturer status.
8. Before creating content, search all articles, pages, `data/keyword-map.csv`, and mapped `Existing URL` values. Prefer `UPDATE` over duplicate `CREATE`; do not create keyword cannibalization.
9. New content remains a draft until it passes technical review and the user authorizes publication. Automated commit, push, and deploy are disabled during the current controlled pilot.
10. After edits, run the available source checks, image audit, Jekyll build in a compatible GitHub Pages environment, built-link checks, canonical and sitemap validation, 404 checks, and inquiry CTA checks proportional to the change.
11. Before committing, show or summarize `git diff`, test results, and the exact files to stage. Push only with explicit user authorization unless the current request explicitly includes deployment.
12. After an authorized deployment, verify the production homepage, changed URLs, sitemap, robots file, inquiry page, verification file, redirects, and HTTP status.
13. Never write passwords, cookies, tokens, private keys, API keys, OAuth secrets, or service-account credentials to this public repository.
14. Do not use destructive Git operations or force pushes. Follow the safe rollback procedure in `docs/CODEX_OPERATIONS.md`.

## Image Library Workflow

1. Before modifying a page or adding an article, read `data/image-library.json` and search by `products`, `applications`, and `topics`.
2. Prefer a suitable existing asset before cropping or creating a new image.
3. Check `used_on` and `reuse_policy`; do not mechanically repeat an image across pages.
4. Never describe a real photo as a customer case unless the manifest explicitly records that authorization.
5. Describe generated diagrams as **Engineering Diagram**, **Representative Engineering Diagram**, or **Generic Engineering Diagram**, as appropriate.
6. Never infer a customer, product model, material performance, equipment ownership, test result, certification, or production capacity from an image.
7. After adding, replacing, or deleting an image, update both `data/image-library.json` and `docs/IMAGE_LIBRARY.md`.
8. Do not move a published image unless every reference is updated and the effect of its old public URL is explicitly reviewed.
9. Do not store the same binary image under multiple filenames. Run `npm run audit:images` before committing.
10. Every rendered `<img>` must have accurate `width`, `height`, and `alt` attributes. Use `loading="lazy"` and `decoding="async"` except where an intentional above-the-fold performance rule is documented, such as the homepage hero.
11. Keep `visual-inbox/` as a temporary intake location only. Complete the provenance, duplicate-hash, naming, optimization, manifest, page, test, and deployment workflow before considering an image published.

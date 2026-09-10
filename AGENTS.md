# Repository Instructions

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

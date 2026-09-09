# Thermal Management Knowledge Base

A lightweight Jekyll site for GitHub Pages with 30 technical articles, topic hubs, glossary, policy pages, sitemap, feed, robots file, structured data, and responsive styling.

## Your next three steps

1. Replace placeholders in _config.yml, about/index.md, and contact/index.md with your real GitHub username, domain, author identity, qualifications, organization, and contact information.
2. Have a qualified thermal engineer review all articles and add genuine TDS sources, test conditions, and disclosures.
3. Create a GitHub repository, upload this project, and enable GitHub Pages.

## Create the GitHub repository

1. Sign in to GitHub and choose **+ → New repository**.
2. Name it exactly **OuYangThermal.github.io**.
3. Choose **Public** if you use GitHub Free.
4. Create it without another README when uploading this complete project.

## Upload the project

The easiest non-programmer workflow is GitHub Desktop: add this folder as a local repository, commit all files, and publish it. In the browser, use **Add file → Upload files**; nested folders are easier with GitHub Desktop.

## Enable GitHub Pages

1. Open repository **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Choose branch **main** and folder **/(root)**.
4. Save and wait for the Pages workflow.
5. For this user-site repository, the public URL is https://ouyangthermal.github.io/.
6. Update url and baseurl in _config.yml to match exactly.

## Custom domain

Enter the domain in **Settings → Pages** and follow the current DNS instructions shown by GitHub. For www, this normally includes a CNAME to USERNAME.github.io. For an apex domain, use current GitHub Docs values, not IPs copied from an old blog. After DNS verifies, enable HTTPS. Set baseurl to an empty string when the site is at the domain root.

## Add a new article

1. Copy a Markdown file inside _articles into the suitable category folder.
2. Use a lowercase hyphenated filename.
3. Edit title, description, category, category_slug, category_url, author, date, and updated.
4. Do not add another H1; the layout creates it from title.
5. Keep the Quick answer, takeaways, explanation, parameters, example, mistakes, FAQ, and references.
6. Commit. Jekyll automatically creates the clean URL and includes the article in its category and sitemap. The latest dated pages appear on the home page and in the Atom feed.

## Edit content and author

Edit index.html for the home page and assets/css/main.css for style. Change author.name in _config.yml, the biography in about/index.md, and each article byline. Add only real, verifiable qualifications.

## Search Console, Bing, and analytics

Add the deployed URL to Google Search Console. Use DNS verification or put the provided verification meta tag in _includes/head.html. Submit https://YOUR-DOMAIN/sitemap.xml. Use URL Inspection for key pages. A site:YOUR-DOMAIN search is only a rough check; Search Console is authoritative.

Bing Webmaster Tools can import a Search Console property or provide its own meta tag for _includes/head.html. Submit the same sitemap.

Put the official analytics snippet in _includes/head.html, ideally with consent appropriate to your markets. No account ID is hard-coded.

## Verify infrastructure

Open /robots.txt, /sitemap.xml, /feed.xml, /llms.txt, and /404.html after deployment. llms.txt is experimental and cannot guarantee AI crawling, indexing, or citation.

## Sustainable GEO workflow

Publish one distinct engineering answer per page. Answer directly; define terms; state assumptions; use tables only where useful; cite original standards and sources; separate illustrative, typical, and measured values; link related pages; record dates; and correct old claims.

Avoid keyword stuffing, near-duplicate pages, unsupported competitor claims, fake cases, and structured data that does not match visible content.

## Optional local preview

Install Ruby and Bundler, then run bundle install and bundle exec jekyll serve. Open http://localhost:4000/.

## Pre-publication checklist

- Confirm the GitHub username and replace contact/author placeholders.
- Review every article for technical accuracy and primary references.
- Check unique titles and descriptions and one visible H1.
- Run a broken-link checker on built output.
- Validate JSON-LD.
- Test mobile widths and keyboard navigation.
- Test 404, robots, sitemap, feed, and llms files.
- Run Lighthouse for performance, accessibility, best practices, and SEO.

## Limitations

These are engineering-first foundational drafts, not application approvals. They avoid invented properties, customer cases, certifications, and equivalence claims. Add real supplier TDS citations, measured values with complete conditions, real author identity, disclosures, and application validation before commercial reliance.

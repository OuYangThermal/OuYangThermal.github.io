# Wins — confirmed only, no vanity metrics

## 2026-10-08

- Compression calculator upgraded with citable methodology packaging: model assumptions, verifiable worked example (2.0 mm → 1.6 mm = 20% compression; 6 W/m·K, 40×40 mm² → ≈0.167 K/W bulk R), visible author/date provenance, JSON-LD dateModified 2026-10-08. Production HTTP 200, content verified live.
- Dow 5121C page discoverability strengthened: pillar page now links to it (inline in second-source paragraph + Related engineering guides); Dow page cross-links the compression calculator (this edit landed via concurrent run's 936af2b, verified live). Production HTTP 200.
- Local Jekyll build PASS; canonical/sitemap/robots/growth-exclusion validated; recovery push 582c344 verified non-empty (first push 14ea1b7 was empty due to shared-clone collision — see EXPERIMENT_LOG); local clone re-synced to origin/main.
- Outreach: Voltera follow-up #1 SENT 2026-10-08 (reply in original thread, 5672306@gmail.com); ALLPCB follow-up #1 SENT 2026-10-08 (reply in original thread). Reply/bounce pre-check: no replies, no bounces from voltera.io or allpcb.com. Follow-up #2 window 2026-10-09 – 2026-10-18 (final per max-2 rule). Notable: mailer-daemon failures for fiisustainability@fiifoxconn.com (known FII hard bounce) and editor@electronicscooling.com (2026-09-26) — both dead addresses, never retry; unrelated to this week's outreach.
- PCBWay first pitch: send blocked by Gmail service instability (2× +send + 1× drafts.send, 0 sends confirmed in Sent after each). Prepared text saved as a real Gmail draft for one-click manual send; retry autonomous send next run if path recovers.
- SP2000 brand-neutrality guard held: an initial "Bergquist Sil-Pad 2000" wording was caught and corrected to "SP2000 incumbent reference" before push, matching the SP2000 page's own disclaimer.
- GSC still blocked (session expired since 2026-09-29; owner re-sign-in still pending) — no new search data this week.

## 2026-09-27

- GSC access established (browser session, 5672306@gmail.com) — first independent read of real search data.
- Real baseline: 5 clicks / 24 impressions / avg position 8.8 (2026-09-09 → 09-24).
- "thermal interface material" ranking at position 1.5 (homepage) — confirmed with real data, not estimated.
- Growth memory infrastructure created: /growth/ with 8 tracking files, seeded with real GSC baseline.
- Pillar page upgraded for supplier intent (commit 6430296) — production verified.

## 2026-09-29

- Thermal Resistance Calculator upgraded with citable methodology packaging: explicit model assumptions (steady-state 1-D), verifiable worked example (6 W/m·K / 1.0 mm / 40×40 mm² → ≈0.104 K/W), visible author/date provenance, JSON-LD dateModified 2026-09-28. Production HTTP 200, content verified live.
- Pillar /china-thermal-interface-material-supplier/ strengthened per rank 11–50 rule: inline calculator link in the R = t/(kA) section + calculator added to Related engineering guides (no URL/title change). Production HTTP 200, link verified live.
- Local Jekyll build PASS (bundle install was required first); canonical/sitemap/robots/growth-exclusion all validated in built output.
- Stale 2026-09-27 "TIM manufacturer" meta risk note closed — removal verified (c40161e), current meta reads "supplier evaluation".
- Outreach pipeline: no replies/bounces on Batch 1 (Voltera/ALLPCB) — follow-up #1 texts prepared for the 2026-10-02 – 2026-10-04 window; PCBWay pitch prepared (send blocked by Gmail tool instability, 0 sends confirmed, retry next run).

## 2026-10-12

- TIM Selection Tool upgraded with citable methodology packaging: "Screening rules" paragraph, verifiable worked example (OBC / 1–3 mm / insulation Yes / rework No / tolerance High → Thermal Gel, 7 validation items — verified against the page's JS logic in Python, not hand-checked), visible author/date provenance, JSON-LD dateModified 2026-10-12. All three interactive tools (resistance, compression, selection) now carry the citable format.
- SP2000 page discoverability strengthened: contextual calculator links in "What engineers should compare" + TIM Selection Tool in Related engineering guides (no URL/title change; brand-neutrality guard held).
- Local Jekyll build PASS; canonical/sitemap/robots/growth-exclusion validated; new links verified present in built HTML.
- Outreach state fully reconciled with Sent-box evidence (both linked Gmail accounts): Batch 1 (Voltera/ALLPCB) 2026-09-27 sends re-verified; PCBWay first pitch corrected to **SENT 2026-10-08** (was mis-logged as draft-blocked); Voltera/ALLPCB follow-up #1s confirmed NOT sent — status reverted to PREPARED-ONLY per the user's 2026-10-09 decision (Voltera only, awaiting user's "send"; ALLPCB closed). Zero unverified "SENT" claims remain in the pipeline.
- Batch 3 prepared (all texts in OUTREACH_LOG.md): PCBWay follow-up #1 (window 2026-10-13 – 2026-10-18, final) + 4 technical-media follow-up #1s (Power Electronics News, EDN, Electronic Design, Lightwave) — the media four are SEND HOLD awaiting the user's go-ahead (user-owned relationships).
- Parker Chomerics competitor pass (BACKLINK_GAP.md): distributor-hosted selection guides (Mouser/Sealing Devices PDFs) confirm the 2026-10-08 pattern — no new target needed; pipeline already covers it.
- GSC still blocked (session expired since 2026-09-29; owner re-sign-in still pending) — no new search data this week. Standing: GSC milestone email (2026-10-10, recorded in daily memory) reported 5 clicks in the 28 days ending 2026-10-07 — email-observed only, not a full GSC read.

## 2026-10-19

- TIM TDS Comparison Tool upgraded with citable methodology packaging: "Model assumptions" paragraph, verifiable worked example (6 W/m·K at 1.0 mm BLT → ≈0.104 K/W vs 8 W/m·K at 1.5 mm BLT → ≈0.117 K/W — arithmetic checked in Python), visible author/date provenance, JSON-LD dateModified 2026-10-19. Four of five interactive tools now carry the format (resistance, compression, selection, TDS comparison); second-source generator remains.
- Homepage hero gained a conversion-only evidence line (internal ASTM D5470 benchmark numbers + thickness series + free tools) — rank-protection rule held: no URL/title change on the site's only ranking URL. Production HTTP 200, new content verified live.
- Local Jekyll build PASS; canonical/sitemap/robots/growth-exclusion validated; push 777c91a verified non-empty via git diff --stat; local clone re-synced; no shared-clone incident this run.
- Outreach: PCBWay follow-up #1 (final) send attempted ×2 — both blocked by Gmail connector service restarts, 0 sends confirmed, honestly kept as PREPARED; never claimed sent. Batch 4 prepared with verified contacts: TECHSiL (#9, technical@techsil.co.uk, TDS Comparison Tool) and RayPCB (#10, sales@raypcb.com, Thermal Resistance Calculator); both authorized GEO engineering outreach, send window 2026-10-20 – 2026-10-26. Reply/bounce pre-check: none from pcbway.com/voltera.io/allpcb.com.
- Momentive + Shin-Etsu competitor backlink pass (BACKLINK_GAP.md): distributor-hosted guides (TECHSiL/Momentive, Pantronics India/Shin-Etsu FAQ) and independent measured reviews (Igor's LAB) confirm the citation pattern for the fourth time — no new target needed from the pattern; the TDS tool's worked example occupies exactly the educational slot Pantronics uses.
- GSC still blocked (session expired since 2026-09-29; signed-out state directly observed) — no new search data this week.
- AI Overviews retest 2026-10-19: Ouyang Thermal not cited on either of 2 questions (unchanged); "How to select thermal pad?" still manufacturer how-to/data-table territory with ALLPCB in the citation path; AI-server query won by recent topical guides + IEEE whitepaper.

## 2026-10-26

- Second Source Qualification Generator upgraded with citable methodology packaging: deterministic selection rules, verifiable worked example (OBC / DC-DC, Thermal Gel, insulation Yes, Supplier Qualification, Automotive → 21-item checklist, verified against the page's JS logic in Python), visible author/date provenance, JSON-LD dateModified 2026-10-26. All five interactive tools now carry the format (resistance 9/29, compression 10/8, selection 10/12, TDS comparison 10/19, second-source generator 10/26).
- Thermal Gel Supplier China money page now links the Second Source Qualification Generator (contextual link + Related guides entry), matching the pad page's treatment — the last tool-link gap on that page. No URL/title change.
- Local Jekyll build PASS (Ruby/bundler installed on this VM first); front matter YAML valid; canonical/sitemap/robots/growth-exclusion validated; push 95f332f verified non-empty via git diff --stat; local clone re-synced; no shared-clone incident.
- Production HTTP 200 on homepage, generator, gel page, pillar, sitemap.xml, robots.txt, request-sample, and the Google verification file; new content verified live after deploy propagation.
- Outreach: sends FAILED on the Gmail connector (two +send attempts, service restarts, 0 sends confirmed, honestly kept as drafts, never claimed sent). Fallback drafts saved and verified: TECHSiL, RayPCB, and the PCBWay follow-up #1 reply — all in 5672306@gmail.com Drafts for one-click manual send. Reply/bounce pre-check: none from any pipeline domain in either account since 2026-10-19.
- Dow competitor backlink pass (fifth): manufacturer methodology papers + distributor-hosted guides pattern confirmed again; no new target (no verifiable editorial contact).
- GSC still blocked (session expired since 2026-09-29; signed-out state directly observed) — no new search data this week.
- AI Overviews retest 2026-10-26: Ouyang Thermal not cited on any of 3 questions (unchanged); "How to select thermal pad?" still manufacturer how-to/data-table territory with ALLPCB in the citation path; AI-server query names Dow DOWSIL examples.

# Demand Log — Ouyang Thermal (GEO 2.0)

Weekly public-source scan for genuine engineering demand signals for thermal interface materials. Public sources only, read-only, no logins, no fabricated questions/companies/needs. A company-level buying signal needs a named company + a named person + a stated TIM need to be flagged PROSPECT.

---

## 2026-11-11 (Wed) — Week scan

### New this week (verified dates)

**S1 — Competitor launch: Henkel Loctite Bergquist TGR 5000SF (silicone-free thermal grease)**
- Date: announced 2026-11-09 (Henkel press release; corroborated by ad-hoc-news.de same day).
- Source: https://www.henkel.com/press-and-media/press-releases-and-kits/2026-11-09-high-performance-thermal-grease-from-henkel-delivers-for-high-power-applications-2273388
- Need (in the announcement's words): "a high-performance thermal grease designed for high-power components" for "data center switches, routers, servers, IGBTs, motor drives and power modules"; 5.3 W/m-K, ultra-thin bond line <25 µm at 40 psi, thermal impedance 5.6 mm²-K/W, silicone-free.
- Application: data center / telecom / power modules, IGBT.
- What a good answer would need: a silicone-free grease second-source comparison — bond-line thickness vs. thermal impedance at low pressure, outgassing/silicone-migration risk, and verified TDS numbers before any equivalence claim.
- Our site: GAP. No silicone-free grease page; `/thermal-grease/` is an 18-line stub with no silicone-free, phase-change, or second-source content. Closest: `/_articles/comparison/thermal-pad-vs-thermal-grease-vs-thermal-gel.md` (generic comparison, no silicone-free angle).
- Second-source angle: yes — a new Henkel grease launch creates "TGR 5000SF alternative" search demand. Do not claim equivalence without a verified TDS.

**S2 — Competitor launch: Parker Chomerics THERM-A-GAP PAD 30RB (reusable gap pad)**
- Date: launched 2026-10-27; showcased at electronica 2026, Munich, 2026-11-10–13.
- Source: https://www.magazine-industry-usa.com/news/116613-parker-chomerics-launches-reusable-thermal-gap-filler-pad
- Need (in the announcement's words): a gap filler pad that "maintain[s] its physical and thermal performance across repeated compression cycles" for "applications requiring frequent maintenance or testing"; 3.0 W/m-K, thermal impedance 2.9 °C·cm²/W, −55 to 200 °C, 0.51–5.08 mm, RoHS.
- Application: serviced / frequently re-assembled electronic hardware.
- What a good answer would need: compression-set / rebound data over repeated cycles, thickness loss after N cycles, and a second-source comparison for reusable pads.
- Our site: GAP (partial). "Reworkable/reusable" is only mentioned in passing in the AI-server article; no reusable-gap-pad page.
- Second-source angle: yes — "reusable thermal gap pad alternative" for test/service hardware.

**S3 — Competitor launch: Parker Chomerics THERM-A-GAP PAD 120LOE (12 W/m-K, low oil migration)**
- Date: 2026-10-27 (Parker blog).
- Source: https://blog.parker.com/us/en/emg_cho/therm-a-gap-pad-120loe.html
- Need: highest-conductivity gap pad to date (12 W/m-K, Shore 00 60) where silicone-oil migration is a concern; ~90% compression-force reduction after 1 h.
- Application: high-density electronics where oil bleed is a defect risk.
- Our site: partial. `/dow-5121c-alternative-evaluation/` covers the 12 W/m-K class; no low-oil-migration angle.
- Second-source angle: watch item, not a new page yet.

### Genuine forum questions (evergreen — found in this scan, threads are older)

**S4 — EEVblog: "Heatsink: Silpad sucks, Paste sucks, what else?"**
- Date: last edit 2025-04-28 (not new this week; recurring demand theme).
- Source: https://www.eevblog.com/forum/projects/heatsink-silpad-sucks-paste-sucks-what-else/msg5896354/
- Question in the asker's words: "I've tried using a silicon pad, thermal paste, and direct attachment… the best thermal transfer was achieved with thermal paste, followed by direct attachment, and finally the silicon pad… I really dislike the mess that paste creates — and more importantly, the fact that it needs to be reapplied after a few years. So, my questions are: 1) Can I simply use direct attachment… 2) Is direct attachment better than dry thermal paste? 3) Are there any efficient alternatives (besides thermal paste) that can fill these air gaps without needing maintenance or replacement over time?" Measured: LM317 plastic-body temp 62 °C paste / 64–65 °C direct / 70–72 °C sil-pad (0.4 K/W).
- Application: linear regulator (LM317) on heatsink, hobbyist/prototype power electronics.
- What a good answer would need: measured comparison of paste vs. pad vs. phase-change vs. graphite pad, including long-term maintenance (dry-out, pump-out) and electrical-isolation trade-offs.
- Our site: PARTIAL. Pad-vs-grease-vs-gel comparison article exists, but no phase-change/graphite maintenance-free answer and no measured data of our own. GAP for the "what lasts without maintenance" angle.

**S5 — EEVblog: "Thermally Conductive, Electrically Isolated Heatsink Compound"**
- Date: not shown in search index (thread predates this scan; treat as evergreen).
- Source: https://www.eevblog.com/forum/projects/thermally-conductive-electrically-isolated-heatsink-compound/
- Question in the asker's words: "I am working on a project involving a lot of power dissipated from 10xTO247 packages into a heatsink… Cheapo sil-pad sheet. Junction reached 200C… 1mm thick Laird Tflex 640 sil-pad sheet. Junction reached 150C… Thermal compound (not electrically isolated) Junction reached 70C… I am looking for a solution which is as good as the thermal compound but electrically isolated (Very modest isolation voltage — up to about 200V)."
- Application: 10× TO-247 power devices, 100 W test, power electronics.
- What a good answer would need: electrically isolating TIMs that approach grease-level thermal resistance at ~200 V isolation — thin ceramic-filled pads, mica + grease, Kapton, phase-change — with measured °C/W at stated pressure.
- Our site: PARTIAL. `/_articles/power-electronics/thermal-interface-material-for-sic-power-modules.md` covers isolation for SiC modules; no dedicated "electrically isolated grease/pad for TO-247/IGBT" answer.

**S6 — EEVblog: "What is this Adhesive Thermal Pad?"**
- Date: original post date not shown on the fetched page (found in this week's crawl; treat as evergreen, not verified-new).
- Source: https://www.eevblog.com/forum/repair/what-is-this-adhesive-thermal-pad/?wap2
- Question in the asker's words: "I would like to clarify what kind of thermal pad this is. It looks like a flexible fiber-reinforced mat. The surface is not sticky… I do not quite understand what is this technology and how to attach the transistor back without much destruction." (TO-263AB/D2-PAK on a heatsink, new cutting-edge equipment.)
- Application: repair / rework of power transistors.
- What a good answer would need: identification of fiber-reinforced adhesive thermal interface sheets, and a safe rework procedure (replace, don't reuse; mica + compound as alternative).
- Our site: GAP. No repair/rework or pad-identification guide. Low priority (repair market, not B2B buying intent).

**S7 — EEVblog: "Methods of conducting heat from PCB to extruded aluminum enclosure?"**
- Date: old thread (evergreen).
- Source: https://www.eevblog.com/forum/projects/methods-of-conducting-heat-from-pcb-to-extruded-aluminum-enclosure/
- Question: 8 W board, ~6 mm gap to an aluminum enclosure, wants conduction instead of a fan/holes.
- Application: enclosed PCB, 6 mm gap.
- What a good answer would need: gap-filler thickness/compression rule (pick thicker than the gap, 15–30% compression), and when to couple only the hot parts.
- Our site: ANSWERED (partially) — gap-filler selection is covered in the pad-vs-grease-vs-gel comparison article; a dedicated "PCB-to-enclosure 6 mm gap" worked example would strengthen it.

### Older context (not new — noted for completeness)
- Dow DOWSIL TC-3120 thermal gel, ~12 W/m-K for 800G/1.6T optical modules — launched 2026-06-01. Source: https://iconnect007.com/article/150217/dow-launches-dowsil-tc3120-thermal-gel-for-optimum-heat-transfer-for-optical-modules-dense-electronics-and-highspeed-data-applications/150214/ein
- Qnity (Laird) Tflex CR910 liquid gap filler (9.2 W/m-K) + Tgrease 3000 (non-silicone, 200 °C) — launched 2026-07-28. Source: https://ir.qnityelectronics.com/_assets/_f1b4d075ea139139a6c744a900c2f58ccc5/qnityelectronics/news/2026-07-28_Qnity_Advances_Thermal_Management_Portfolio_as_AI__66.pdf
- Henkel Bergquist TGF 2030APS gap filler + Loctite TLB 9270APS adhesive for EV batteries — 2026-05-12.

### Clusters with no new genuine question found this week
- ESS/PCS and OBC/DC-DC/PDU searches returned vendor marketing pages only (Elaplus, JOME, Parker Lord whitepaper, Ziitek guides) — no new forum question with a stated need.
- AI Server / Optical Module: only vendor content (Sheen hot-pluggable guide) and a 2026-11-05 consumer laptop liquid-metal repair story (WCCFTech/Reddit, not B2B demand).
- Second Source / Replacement: no new asker question found; the demand signal this week is competitor launches (S1–S3) rather than questions.

### PROSPECTS
- None this week. No named company + named person + stated TIM need found in public sources.

### Draft replies
- None drafted. The EEVblog threads above are old and already answered by the community; posting now would add no value. No new unanswered question was found where a reply from us would fit.

### This week's best content/video ideas (max 3)
1. **Silicone-free thermal grease second-source page** — "TGR 5000SF alternative: silicone-free grease for IGBT / power modules" (from S1, this week's launch). Requires verified TDS data first; no equivalence claim without it. Also fixes the 18-line `/thermal-grease/` stub.
2. **"Sil-pad vs paste vs phase-change: what lasts without maintenance?"** — measured-answer article/video built around the S4 question pattern (paste dries out, pads underperform, phase-change/graphite as the maintenance-free middle). Needs our own measured numbers or clearly-labelled literature values, not invented data.
3. **"Reusable gap pads for serviced and test hardware"** — second-source angle on S2 (Therm-A-Gap 30RB class): compression-set/rebound after repeated cycles. Short video or comparison table once verified data exists.

# Outreach Queue & Pipeline

**Authorization (2026-09-27, user):** autonomous sending is APPROVED for low-risk,
normal, real B2B engineering content/link outreach. No per-email approval needed.
Prepare → 4-question check → send → record → follow up (max 2) → stop on refusal.

The 4-question check before every send:
1. Why this person? 2. Why this website? 3. Why this resource? 4. Why would their readers care?
If any has no answer → do not send.

**Sender:** 5672306@gmail.com (Owen Ouyang) — business address on ouyangthermal.github.io.
**Status 2026-09-27:** 5672306@gmail.com is NOT yet connected to the Gmail connector
(only suno223335@gmail.com is linked). Batch 1 emails are written and logged in
OUTREACH_LOG.md as PREPARED. Sending starts the moment the business address is connected.

## Pipeline

Discovery → Qualification → Find Contact → Personalize (4-question check) → Send →
Record → Follow-up #1 (5–7d) → Follow-up #2 (7–14d) → Reply / Backlink / Stop.

## Queue — Batch 1 (prepared 2026-09-27, full text in OUTREACH_LOG.md)

| # | Target | Type | Why them | Resource pitched | Contact (verified) | Status |
|---|---|---|---|---|---|---|
| 1 | Voltera blog | Resource suggestion | TIM Selection Guide cited by AI Overviews; engineering readers | TIM Selection Tool | hello@voltera.io (voltera.io/contact) | SENT 2026-09-27 |
| 2 | ALLPCB blog | Resource suggestion | Thermal pad/PCB thermal guides, large engineering audience | Thermal Resistance Calculator | sponsor@allpcb.com (Cooperation inbox) | SENT 2026-09-27 |
| 3 | ThomasNet | Supplier directory | Free supplier profile; lists TIM competitors | Company profile | Form submission | Entity confirmed 2026-09-27: Hongjing New Materials Technology (Shenzhen) Co., Ltd. — BLOCKED: site bot-walls our network, auto-retry planned, nothing submitted |
| 4 | GlobalSpec | Supplier directory | Assumed free listing — disproven 2026-09-27 | — | Paid program only | Parked: "List Your Company" is paid-only (no free tier); out of scope unless user approves paid route |

Parked/dropped 2026-09-27: NEDC (failed 4-question check — converter of competing
brands, weak reader fit), Krayden (distributor of competing brands), E-Mobility
Engineering (no verifiable editorial email). Details in OUTREACH_LOG.md.

## Queue — Batch 2 (prepared 2026-09-29; full text in OUTREACH_LOG.md)

| # | Target | Type | Why them | Resource pitched | Contact (verified) | Status |
|---|---|---|---|---|---|---|
| 3 | PCBWay blog | Resource suggestion | High-power PCB design guides with thermal management sections; large PCB-designer audience | Thermal Resistance Calculator | simon@pcbway.com (published "Co-operation" inbox from PCBWay's own contact list, via CNX Software sponsored post 2024-11-20) | PREPARED 2026-09-29 — send FAILED 3×: Gmail +send hit service restarts mid-command each time; zero sends confirmed in Sent after every attempt. Not retrying further on a flaky path (duplicate-send risk). Ready to send next run. |
| — | Voltera | Follow-up #1 | Batch 1 sent 2026-09-27; no reply, no bounce (verified 2026-09-29) | TIM Selection Tool | hello@voltera.io | PREPARED — send window 2026-10-02 – 2026-10-04 |
| — | ALLPCB | Follow-up #1 | Batch 1 sent 2026-09-27; no reply, no bounce (verified 2026-09-29) | Thermal Resistance Calculator | sponsor@allpcb.com | PREPARED — send window 2026-10-02 – 2026-10-04 |

Parked 2026-09-29: Sierra Circuits blog (protoexpress.com — strong thermal content incl. "12 PCB Thermal Management Techniques", but no verifiable editorial/cooperation email; amit@protoexpress.com from a 2020 guide PDF is stale — never guess contacts), EEWorld Online (contribution form strips URLs → no link value; no public editorial email; About page names editors but no addresses), ThomasNet (entity confirmed: Hongjing New Materials Technology (Shenzhen) Co., Ltd. — still bot-walled, retry planned), GlobalSpec (paid-only, out of scope).

### Technical abstracts (Batch 2)

- **PCBWay — Thermal Resistance Calculator:** estimates a TIM joint's bulk thermal resistance R = t/(k·A) from thermal conductivity, bond-line thickness, and contact area. Packaged with explicit model assumptions (steady-state, one-dimensional), a verifiable worked example (6 W/m·K, 1.0 mm, 40×40 mm² → ≈0.104 K/W), and stated limits. Companion link for high-power PCB thermal-management guides — readers can sanity-check a candidate pad's thermal path numerically before layout.
- **Voltera follow-up — TIM Selection Tool:** interactive selector mapping application constraints (power, gap, rework needs) to TIM families (pads, gels, greases, phase-change). Companion link for Voltera's TIM Selection Guide, cited by AI Overviews.
- **ALLPCB follow-up — Thermal Resistance Calculator:** as above; companion link for ALLPCB's PCB thermal-management articles.

### Author intro (all Batch 2 sends)

Owen Ouyang — Ouyang Thermal (ouyangthermal.github.io), Thermal Management Solutions. Engineering content author; outreach on behalf of Hongjing New Materials Technology (Shenzhen) Co., Ltd. for commercial follow-up. No invented titles, no manufacturer claims.

## Rules

- Precise > blast. Relevant > quantity. Engineering value > ads. Personalized > templates.
- Never send more than a small batch per day (protect sender reputation).
- Stop immediately on explicit refusal. Bounced address → mark dead, never retry.
- Full email text for every send lives in OUTREACH_LOG.md (audit trail).
- Bans: impersonation, fake reviews/testimonials/test data/cases/certs, fake engineer identity, unauthorized price/lead-time promises, paid links, PBN, comment/forum spam, fake accounts, captcha bypass.
- Still needs user approval: payment, contracts, legal statements, major commitments in user's personal identity, pricing/payment terms/exclusivity, captchas/2FA, unverifiable company info, unverified customer/cert/test data.

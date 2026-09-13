# Autonomous Backlink Outreach

This directory stores public, non-secret status for low-frequency technical outreach supporting OUYANG THERMAL citation assets.

## Safety gates

- Send only through an official Gmail/Google OAuth connection for `5672306@gmail.com`.
- Never request, store, log, or commit a Gmail password, OAuth token, client secret, cookie, mailbox export, or private contact database.
- Read the target page before scoring or writing. Automatic sending requires a score of at least 80/100.
- Contact only a relevant, publicly listed professional editorial or contribution channel.
- Week 1 permits at most three new messages per day. Week 2 and later permits at most five only if delivery health is normal.
- One initial message and at most one follow-up after 5–7 days. Stop immediately after rejection, unsubscribe, or stop requests.
- Positive replies receive a proposed response draft for Owen Ouyang to approve; no autonomous commercial negotiation.
- Pause sending on Gmail/OAuth warnings, unusual login alerts, sending limits, repeated invalid addresses, elevated bounces, or spam complaints.

## Workflow

1. Read the target article and its current editorial/contact page.
2. Match exactly one asset from `OUTREACH_ASSET_LIST.md`.
3. Score topical relevance (30), editorial quality (20), citation probability (20), authority/trust (15), audience fit (10), and contactability (5).
4. Record the evidence and status in `outreach-status.csv`; do not place non-public personal data in Git.
5. Draft an 80–140 word engineer-to-engineer note that names the exact article and a specific technical point.
6. Send only after official Gmail authorization is available and all gates pass.
7. Store Gmail message IDs and reply details only in secure local storage, not this public repository. The public CSV uses a non-sensitive status reference.
8. Verify any claimed backlink at its live URL before marking it acquired.

## Gmail authorization status

`BLOCKED — no official Gmail Connector or Google OAuth mail tool is available in the current Codex environment as of 2026-09-14.`

No message may be sent until that capability is connected. Browser passwords, unofficial SMTP relays, and repository-stored OAuth credentials are prohibited.

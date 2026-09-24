# docs/geo/

Daily commercial GEO tracking for ouyangthermal.github.io.

**Repo convention:** the keyword map lives at `data/keyword-map.csv` (see AGENTS.md rule 8).
Do not create a second copy here.

## Files

- `commercial-pages.csv` — money/commercial pages, their priority tier, last update,
  and remaining credibility/conversion gaps.
- `content-opportunities.csv` — candidate tasks scored per the daily rubric
  (Commercial Intent 30 / Application Fit 25 / Engineering Value 20 /
  Search Opportunity 15 / AI Citation Potential 10). Only tasks scoring ≥80 execute;
  below 80 the day does reinforcement work instead.

## Rules

- One search intent = one authoritative page. UPDATE wins over CREATE.
- Never invent customers, cases, test data, certs, specs, or supplier status.
- Competitor alternatives use compliant wording only ("candidate for evaluation",
  "benchmark against the incumbent", "application-specific qualification required").
  Never "drop-in replacement" / "exact equivalent" / "guaranteed".

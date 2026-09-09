#!/usr/bin/env python3
"""Dependency-free live SEO/GEO audit for OUYANG THERMAL."""
from __future__ import annotations
import argparse, concurrent.futures, datetime as dt, hashlib, json, os, re, time
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
from zoneinfo import ZoneInfo
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse, urldefrag
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

UA = "OUYANG-THERMAL-GEO-AUDIT/1.0 (+https://ouyangthermal.github.io/)"
ARTICLE_PREFIXES = ("/obc/", "/thermal-pad/", "/thermal-gel/", "/potting-compound/", "/thermal-insulator/", "/power-electronics/", "/energy-storage/", "/battery-pack/", "/pcs/", "/optical-module/", "/server/", "/testing/", "/comparison/")
HUB_PATHS = {"/obc/", "/thermal-pad/", "/thermal-gel/", "/potting-compound/", "/thermal-insulator/", "/power-electronics/", "/energy-storage/", "/battery-pack/", "/pcs/", "/optical-module/", "/server/", "/testing/", "/comparison/"}
PRIORITY_TERMS = ("obc", "dc-dc", "pcs", "energy-storage", "battery-pack", "bms", "optical", "server", "thermal-pad", "thermal-gel", "testing", "sp2000")
GEO_COMPONENTS = {
    "Direct Answer": ("quick answer", "direct answer"),
    "Key Takeaways": ("key takeaways",),
    "Technical Explanation": ("technical explanation",),
    "Selection Parameters": ("selection parameters",),
    "Application Example": ("application example",),
    "FAQ": ("faq",),
    "References / Standards": ("references and standards", "references / standards"),
    "Related Guides": ("related guides", "related guidance"),
}

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title=""; self.desc=""; self.h1=[]; self.canonical=""; self.links=[]; self.images=[]
        self.jsonld=[]; self.text=[]; self.headings=[]; self.times=[]; self.author_meta=""
        self._title=False; self._h1=False; self._heading=False; self._script=False; self._scriptbuf=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs); tag=tag.lower()
        if tag=="title": self._title=True
        if tag=="h1": self._h1=True
        if tag in ("h1","h2","h3"): self._heading=True
        if tag=="meta" and a.get("name","").lower()=="description": self.desc=a.get("content","").strip()
        if tag=="meta" and a.get("name","").lower()=="author": self.author_meta=a.get("content","").strip()
        if tag=="link" and "canonical" in a.get("rel","").lower(): self.canonical=a.get("href","").strip()
        if tag=="a" and a.get("href"): self.links.append(a["href"])
        if tag=="img": self.images.append(a.get("alt"))
        if tag=="time": self.times.append(a.get("datetime", ""))
        if tag=="script" and a.get("type","").lower()=="application/ld+json": self._script=True; self._scriptbuf=[]
    def handle_endtag(self, tag):
        tag=tag.lower()
        if tag=="title": self._title=False
        if tag=="h1": self._h1=False
        if tag in ("h1","h2","h3"): self._heading=False
        if tag=="script" and self._script:
            self.jsonld.append("".join(self._scriptbuf).strip()); self._script=False
    def handle_data(self, data):
        clean=" ".join(data.split())
        if not clean: return
        self.text.append(clean)
        if self._title: self.title += clean
        if self._h1: self.h1.append(clean)
        if self._heading: self.headings.append(clean)
        if self._script: self._scriptbuf.append(data)

def request(url, timeout=20):
    started=time.perf_counter(); req=Request(url,headers={"User-Agent":UA,"Accept":"text/html,application/xhtml+xml,application/xml,text/plain;q=0.9,*/*;q=0.8"})
    try:
        with urlopen(req,timeout=timeout) as res:
            body=res.read(); final=res.geturl(); status=res.status; ctype=res.headers.get("Content-Type","")
        return {"url":url,"status":status,"final_url":final,"redirected":final.rstrip("/")!=url.rstrip("/"),"elapsed_ms":round((time.perf_counter()-started)*1000),"size_bytes":len(body),"content_type":ctype,"body":body.decode("utf-8","replace"),"error":""}
    except HTTPError as e:
        return {"url":url,"status":e.code,"final_url":getattr(e,"url",url),"redirected":False,"elapsed_ms":round((time.perf_counter()-started)*1000),"size_bytes":0,"content_type":"","body":"","error":str(e)}
    except (URLError,TimeoutError,OSError) as e:
        return {"url":url,"status":0,"final_url":url,"redirected":False,"elapsed_ms":round((time.perf_counter()-started)*1000),"size_bytes":0,"content_type":"","body":"","error":str(e)}

def is_article(url):
    p=urlparse(url).path
    return p not in HUB_PATHS and any(p.startswith(x) for x in ARTICLE_PREFIXES)

def normalize(url, base):
    u=urldefrag(urljoin(base,url))[0]
    return u if urlparse(u).netloc==urlparse(base).netloc else ""

def issue(level, code, url, detail): return {"level":level,"code":code,"url":url,"detail":detail}

def audit(base, outdir):
    base=base.rstrip("/"); now=dt.datetime.now(ZoneInfo("Asia/Shanghai")); issues=[]
    sm=request(base+"/sitemap.xml")
    if sm["status"]!=200: issues.append(issue("critical","SITEMAP_UNAVAILABLE",base+"/sitemap.xml",f"HTTP {sm['status']}")); urls=[base+"/"]
    else:
        try:
            root=ET.fromstring(sm["body"]); urls=[x.text.strip() for x in root.findall(".//{*}loc") if x.text]
        except ET.ParseError as e:
            issues.append(issue("critical","SITEMAP_INVALID_XML",base+"/sitemap.xml",str(e))); urls=[base+"/"]
    urls=list(dict.fromkeys(urls)); outdir.mkdir(parents=True,exist_ok=True)
    (outdir/"sitemap-urls.json").write_text(json.dumps(urls,indent=2),encoding="utf-8")
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex: pages=list(ex.map(request,urls))
    parsed={}; titles=defaultdict(list); descs=defaultdict(list); all_internal=set()
    for p in pages:
        u=p["url"]
        if p["status"]!=200:
            level="high" if any(t in u.lower() for t in PRIORITY_TERMS) else "critical" if u.rstrip("/")==base else "warning"
            issues.append(issue(level,"HTTP_ERROR",u,f"HTTP {p['status']} {p['error']}")); continue
        if p["redirected"]: issues.append(issue("warning","REDIRECT",u,"Redirected to "+p["final_url"]))
        if "html" not in p["content_type"]: continue
        x=PageParser(); x.feed(p["body"]); parsed[u]=x
        if not x.title: issues.append(issue("high" if is_article(u) else "warning","MISSING_TITLE",u,"No title element"))
        else: titles[x.title.strip().lower()].append(u)
        if not x.desc: issues.append(issue("warning","MISSING_DESCRIPTION",u,"No meta description"))
        else: descs[x.desc.strip().lower()].append(u)
        if len(x.h1)==0: issues.append(issue("warning","MISSING_H1",u,"No H1"))
        elif len(x.h1)>1: issues.append(issue("warning","MULTIPLE_H1",u,f"{len(x.h1)} H1 elements"))
        if not x.canonical: issues.append(issue("high" if is_article(u) else "warning","MISSING_CANONICAL",u,"No canonical"))
        elif x.canonical.rstrip("/")!=u.rstrip("/"): issues.append(issue("high" if is_article(u) else "warning","WRONG_CANONICAL",u,"Canonical is "+x.canonical))
        if any(a is None or not a.strip() for a in x.images): issues.append(issue("warning","MISSING_IMAGE_ALT",u,"One or more images lack alt text"))
        internal={normalize(h,u) for h in x.links}; internal.discard(""); all_internal.update(internal)
        if len(internal)==0: issues.append(issue("warning","MISSING_INTERNAL_LINKS",u,"No internal links"))
        text=" ".join(x.text); words=len(re.findall(r"\b[\w'-]+\b",text))
        if words<80: issues.append(issue("warning","THIN_PAGE",u,f"Approximately {words} words"))
        if is_article(u):
            lower=" ".join(x.headings).lower()+" "+text.lower(); missing=[name for name,needles in GEO_COMPONENTS.items() if not any(n in lower for n in needles)]
            if missing: issues.append(issue("warning","MISSING_GEO_COMPONENTS",u,", ".join(missing)))
            if not (x.author_meta or re.search(r"\bby\s+(ouyang|editorial)",text,re.I)): issues.append(issue("high","MISSING_AUTHOR",u,"No visible or meta author"))
            if len(x.times)<1: issues.append(issue("warning","MISSING_PUBLISHED_DATE",u,"No machine-readable date"))
            if len(x.times)<2: issues.append(issue("warning","MISSING_UPDATED_DATE",u,"No second machine-readable date"))
            valid=[]
            for raw in x.jsonld:
                try: valid.append(json.loads(raw))
                except json.JSONDecodeError as e: issues.append(issue("high","INVALID_JSON_LD",u,str(e)))
            flat=json.dumps(valid)
            if "TechArticle" not in flat: issues.append(issue("high","MISSING_TECHARTICLE_SCHEMA",u,"TechArticle not found"))
            if "BreadcrumbList" not in flat: issues.append(issue("warning","BROKEN_BREADCRUMB",u,"BreadcrumbList not found"))
    for value,us in titles.items():
        if value and len(us)>1:
            for u in us: issues.append(issue("warning","DUPLICATE_TITLE",u,f"Shared by {len(us)} pages"))
    for value,us in descs.items():
        if value and len(us)>1:
            for u in us: issues.append(issue("warning","DUPLICATE_DESCRIPTION",u,f"Shared by {len(us)} pages"))
    known={u.rstrip("/") for u in urls}
    extras=[u for u in all_internal if u.rstrip("/") not in known and not re.search(r"/(feed\.xml|robots\.txt|sitemap\.xml|llms\.txt)$",u)]
    if extras:
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
            for p in ex.map(request,extras):
                if p["status"]>=400 or p["status"]==0: issues.append(issue("warning","BROKEN_INTERNAL_LINK",p["url"],f"HTTP {p['status']}"))
    robots=request(base+"/robots.txt"); robot_text=robots["body"] if robots["status"]==200 else ""
    if robots["status"]!=200: issues.append(issue("critical","ROBOTS_UNAVAILABLE",base+"/robots.txt",f"HTTP {robots['status']}"))
    def allowed(agent):
        groups=re.split(r"(?im)(?=^user-agent\s*:)",robot_text)
        applicable=[]
        for g in groups:
            m=re.search(r"(?im)^user-agent\s*:\s*([^\s#]+)",g)
            if m and m.group(1).lower() in (agent.lower(),"*"): applicable.append(g)
        return bool(applicable) and not any(re.search(r"(?im)^disallow\s*:\s*/\s*(?:#.*)?$",g) for g in applicable if re.search(r"(?im)^user-agent\s*:\s*"+re.escape(agent)+r"\s*$",g))
    bots={a:allowed(a) for a in ("OAI-SearchBot","GPTBot","Googlebot","Bingbot","*")}
    if not bots["OAI-SearchBot"]: issues.append(issue("critical","CRITICAL_GEO_ERROR",base+"/robots.txt","OAI-SearchBot is blocked or not covered by an allow rule"))
    for a in ("GPTBot","Googlebot","Bingbot","*"):
        if not bots[a]: issues.append(issue("high","CRAWLER_BLOCKED",base+"/robots.txt",a+" appears blocked"))
    article_urls=[u for u in urls if is_article(u)]; healthy=sum(1 for p in pages if p["status"]==200)
    article_issues=[i for i in issues if is_article(i["url"])]
    structure_misses=sum(len(i["detail"].split(", ")) for i in issues if i["code"]=="MISSING_GEO_COMPONENTS")
    json_bad=sum(1 for i in issues if i["code"] in ("INVALID_JSON_LD","MISSING_TECHARTICLE_SCHEMA"))
    internal_bad=sum(1 for i in issues if i["code"] in ("BROKEN_INTERNAL_LINK","MISSING_INTERNAL_LINKS"))
    entity_bad=0
    for u,x in parsed.items():
        t=" ".join(x.text)
        if "Thermal Management KB" in t: entity_bad+=1; issues.append(issue("warning","OLD_BRAND",u,"Found deprecated display brand"))
        if is_article(u) and "Ouyang Xiaohui" not in t: entity_bad+=1; issues.append(issue("warning","AUTHOR_ENTITY_MISMATCH",u,"Expected author Ouyang Xiaohui"))
    critical=sum(i["level"]=="critical" for i in issues); high=sum(i["level"]=="high" for i in issues); warnings=sum(i["level"]=="warning" for i in issues)
    avg_ms=round(sum(p["elapsed_ms"] for p in pages)/max(1,len(pages)))
    components_total=max(1,len(article_urls)*len(GEO_COMPONENTS))
    scores={
      "Technical Accessibility":max(0,20-min(20,critical*8+high*2)),
      "Crawlability":max(0,15-min(15,(0 if sm["status"]==200 else 8)+(0 if robots["status"]==200 else 5)+sum(not v for v in bots.values())*3)),
      "Article Structure":round(15*max(0,1-structure_misses/components_total),1),
      "Schema":round(10*max(0,1-json_bad/max(1,len(article_urls))),1),
      "Internal Linking":max(0,10-min(10,internal_bad)),
      "Content Completeness":max(0,10-min(10,sum(i["code"]=="THIN_PAGE" for i in issues))),
      "Entity Consistency":round(10*max(0,1-entity_bad/max(1,len(parsed))),1),
      "Freshness":5 if all(len(parsed[u].times)>=2 for u in article_urls if u in parsed) else 3,
      "Performance":5 if avg_ms<=2500 else 3 if avg_ms<=5000 else 1,
    }
    score=round(sum(scores.values()))
    search_status={"Google Search Console":"CONFIGURED" if os.getenv("GOOGLE_SEARCH_CONSOLE_CREDENTIALS") else "NOT CONFIGURED","Bing Webmaster Tools":"CONFIGURED" if os.getenv("BING_WEBMASTER_API_KEY") else "NOT CONFIGURED","IndexNow":"PENDING OPTIONAL STEP" if os.getenv("INDEXNOW_KEY") else "NOT CONFIGURED","ChatGPT Benchmark":"API TEST ENABLED" if os.getenv("OPENAI_API_KEY") and os.getenv("RUN_OPENAI_BENCHMARK","").lower()=="true" else "NOT TESTED"}
    previous=int(os.getenv("PREVIOUS_GEO_SCORE")) if os.getenv("PREVIOUS_GEO_SCORE","").isdigit() else None
    report={"brand":"OUYANG THERMAL","date":now.date().isoformat(),"generated_at":now.isoformat(),"base_url":base,"score":score,"comparison":{"yesterday":previous,"today":score,"change":score-previous if previous is not None else None},"score_breakdown":scores,"summary":{"pages_checked":len(urls),"pages_healthy":healthy,"articles_checked":len(article_urls),"critical":critical,"high_priority":high,"warnings":warnings,"average_response_ms":avg_ms},"robots":{"status":robots["status"],"agents":bots},"sitemap":{"status":sm["status"],"url_count":len(urls),"article_url_count":len(article_urls)},"search_engine_submission_status":search_status,"issues":issues}
    (outdir/"report.json").write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
    render(report,outdir)
    return report

def render(r,outdir):
    s=r["summary"]; status="🚨 ACTION REQUIRED" if s["critical"] or s["high_priority"] else "✅ GEO HEALTHY"
    grouped=defaultdict(list)
    for i in r["issues"]: grouped[i["level"]].append(i)
    details=[]
    for level in ("critical","high","warning"):
        details.append(f"## {level.title()} issues ({len(grouped[level])})")
        details.extend(f"- **{i['code']}** — {i['url']} — {i['detail']}" for i in grouped[level])
        if not grouped[level]: details.append("- None")
    md=f"""# OUYANG THERMAL — Daily GEO Report

**Date:** {r['date']}  
**Overall GEO Score:** {r['score']} / 100  
**Yesterday:** {r['comparison']['yesterday'] if r['comparison']['yesterday'] is not None else 'N/A'}  
**Today:** {r['comparison']['today']}  
**Change:** {('+' if r['comparison']['change'] is not None and r['comparison']['change'] >= 0 else '') + str(r['comparison']['change']) if r['comparison']['change'] is not None else 'N/A'}  
**Status:** {status}

| Metric | Result |
|---|---:|
| Pages checked | {s['pages_checked']} |
| Pages healthy | {s['pages_healthy']} |
| Articles checked | {s['articles_checked']} |
| Critical errors | {s['critical']} |
| High-priority errors | {s['high_priority']} |
| Warnings | {s['warnings']} |
| Average response time | {s['average_response_ms']} ms |
| Sitemap URLs | {r['sitemap']['url_count']} |

## Crawlability

- robots.txt: HTTP {r['robots']['status']}
- OAI-SearchBot: {'ALLOWED' if r['robots']['agents']['OAI-SearchBot'] else 'BLOCKED — CRITICAL GEO ERROR'}
- GPTBot: {'ALLOWED' if r['robots']['agents']['GPTBot'] else 'BLOCKED'}
- Googlebot: {'ALLOWED' if r['robots']['agents']['Googlebot'] else 'BLOCKED'}
- Bingbot: {'ALLOWED' if r['robots']['agents']['Bingbot'] else 'BLOCKED'}

## Score breakdown

"""+"\n".join(f"- {k}: {v}" for k,v in r["score_breakdown"].items())+"\n\n"+"\n".join(details)+"\n\n## Search engine submission status\n\n"+"\n".join(f"- {k}: **{v}**" for k,v in r["search_engine_submission_status"].items())+"\n\n## Recommended actions\n\n1. Resolve critical and high-priority technical errors first.\n2. Review Missing GEO Components without automatically rewriting technical claims.\n3. Review entity warnings against verified organization and author facts.\n4. Treat API benchmark results as API TEST data, never as ordinary ChatGPT rankings.\n"
    (outdir/f"{r['date']}-geo-report.md").write_text(md,encoding="utf-8")
    issue_body=md+f"\n\n[Download the full workflow artifact](https://github.com/OuYangThermal/OuYangThermal.github.io/actions)\n"
    (outdir/"issue-body.md").write_text(issue_body,encoding="utf-8")

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--base-url",default="https://ouyangthermal.github.io"); ap.add_argument("--output-dir",default="audit-output"); a=ap.parse_args()
    r=audit(a.base_url,Path(a.output_dir)); print(json.dumps(r["summary"],indent=2)); print("GEO Score:",r["score"])
if __name__=="__main__": main()

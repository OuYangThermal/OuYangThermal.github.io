#!/usr/bin/env python3
"""Detect duplicate paragraphs and potential source-content cannibalization."""
import argparse, json, re
from collections import defaultdict
from pathlib import Path

STOP={"the","a","an","and","or","to","of","in","for","with","is","are","be","by","at","on","from","that","this","it","as"}
def tokens(text): return {w for w in re.findall(r"[a-z0-9]+",text.lower()) if len(w)>2 and w not in STOP}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--articles",required=True); ap.add_argument("--opportunities",required=True); ap.add_argument("--output",required=True); a=ap.parse_args()
    docs=[]; paragraphs=defaultdict(list)
    for p in Path(a.articles).rglob("*.md"):
        raw=p.read_text(encoding="utf-8"); body=raw.split("---",2)[-1]; title=re.search(r'^title:\s*["\']?(.+?)["\']?$',raw,re.M)
        docs.append((str(p),tokens((title.group(1) if title else "")+" "+body)))
        for para in re.split(r"\n\s*\n",body):
            clean=" ".join(para.split())
            if len(clean)>=140 and not clean.startswith(("|","<","#","-")): paragraphs[clean].append(str(p))
    exact=[{"paragraph":k,"files":v} for k,v in paragraphs.items() if len(v)>1]
    pairs=[]
    for i,(pa,ta) in enumerate(docs):
        for pb,tb in docs[i+1:]:
            score=len(ta&tb)/max(1,len(ta|tb))
            if score>=0.78: pairs.append({"a":pa,"b":pb,"token_jaccard":round(score,3),"status":"POTENTIAL CANNIBALIZATION — REVIEW ONLY"})
    result={"article_count":len(docs),"exact_duplicate_paragraphs":exact,"potential_cannibalization":sorted(pairs,key=lambda x:x["token_jaccard"],reverse=True),"content_opportunities":json.loads(Path(a.opportunities).read_text(encoding="utf-8")),"automatic_deletion":False,"automatic_article_generation":False}
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding="utf-8")
    print("Content analysis:",len(docs),"articles,",len(exact),"duplicate paragraphs,",len(pairs),"potential pairs")
if __name__=="__main__": main()

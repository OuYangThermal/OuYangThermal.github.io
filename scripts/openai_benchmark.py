#!/usr/bin/env python3
"""Optional OpenAI Responses API benchmark. Results are always labeled API TEST."""
import argparse, json, os, re, urllib.request
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--benchmark",required=True); ap.add_argument("--output",required=True); a=ap.parse_args()
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True)
    key=os.getenv("OPENAI_API_KEY",""); enabled=os.getenv("RUN_OPENAI_BENCHMARK","").lower()=="true"
    if not key or not enabled:
        out.write_text(json.dumps({"status":"NOT TESTED","reason":"OPENAI_API_KEY missing or RUN_OPENAI_BENCHMARK is not true","label":"API TEST"},indent=2),encoding="utf-8"); print("OpenAI benchmark: NOT TESTED"); return
    model=os.getenv("OPENAI_MODEL") or "gpt-5.4-nano"
    rows=[]
    for line in Path(a.benchmark).read_text(encoding="utf-8").splitlines():
        if re.match(r"^\|\s*\d+\s*\|",line):
            cells=[c.strip() for c in line.strip("|").split("|")]; rows.append(cells)
    results=[]
    for cells in rows[:5]:
        prompt=cells[2]; target=cells[3]
        payload={"model":model,"tools":[{"type":"web_search"}],"input":"Answer this engineering question using web sources. Report sources accurately: "+prompt,"store":False,"include":["web_search_call.action.sources"]}
        req=urllib.request.Request("https://api.openai.com/v1/responses",data=json.dumps(payload).encode(),headers={"Authorization":"Bearer "+key,"Content-Type":"application/json"},method="POST")
        try:
            with urllib.request.urlopen(req,timeout=90) as res: data=json.load(res)
            text=" ".join(x.get("content",[{}])[0].get("text","") for x in data.get("output",[]) if x.get("type")=="message")
            results.append({"prompt":prompt,"target_url":target,"citation_status":"CITED" if target.lower() in json.dumps(data).lower() else "NOT CITED","brand_mention":"YES" if "ouyang thermal" in text.lower() else "NO","label":"API TEST","response_id":data.get("id")})
        except Exception as e: results.append({"prompt":prompt,"target_url":target,"status":"ERROR","error":str(e),"label":"API TEST"})
    out.write_text(json.dumps({"status":"API TEST","model":model,"sample_size":len(results),"results":results},indent=2),encoding="utf-8")
    print("OpenAI benchmark: API TEST",len(results))
if __name__=="__main__": main()


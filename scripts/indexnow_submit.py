#!/usr/bin/env python3
"""Optional IndexNow submission; records Submitted only for an accepted HTTP response."""
import argparse, json, os, urllib.request
from pathlib import Path
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--base-url",required=True); ap.add_argument("--sitemap",required=True); ap.add_argument("--output",required=True); a=ap.parse_args(); key=os.getenv("INDEXNOW_KEY",""); out=Path(a.output)
    if not key:
        out.write_text(json.dumps({"status":"NOT CONFIGURED"},indent=2),encoding="utf-8"); print("IndexNow: NOT CONFIGURED"); return
    urls=json.loads(Path(a.sitemap).read_text()); base=a.base_url.rstrip("/"); payload={"host":base.split("://",1)[1],"key":key,"keyLocation":base+"/"+key+".txt","urlList":urls[:10000]}
    req=urllib.request.Request("https://api.indexnow.org/indexnow",data=json.dumps(payload).encode(),headers={"Content-Type":"application/json"},method="POST")
    try:
        with urllib.request.urlopen(req,timeout=30) as res: code=res.status
        status="Submitted" if code in (200,202) else "FAILED"
        result={"status":status,"http_status":code,"url_count":len(payload["urlList"])}
    except Exception as e: result={"status":"FAILED","error":str(e)}
    out.write_text(json.dumps(result,indent=2),encoding="utf-8"); print("IndexNow:",result["status"])
if __name__=="__main__": main()


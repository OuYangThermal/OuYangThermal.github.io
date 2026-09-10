from pathlib import Path
import re, json, sys
root=Path(__file__).resolve().parents[1]
files=[p for p in list(root.rglob("*.md"))+list(root.rglob("*.html")) if "_layouts" not in p.parts and "_includes" not in p.parts and "docs" not in p.parts]
errors=[]
titles={}
permalinks={}
for p in files:
    s=p.read_text(encoding="utf-8")
    if s.startswith("---"):
        fm=s.split("---",2)[1]
        if "title:" not in fm: errors.append(str(p)+": missing title")
        if "description:" not in fm and p.name!="README.md": errors.append(str(p)+": missing description")
        m=re.search(r"^title:\s*[\"']?(.+?)[\"']?$",fm,re.M)
        if m:
            t=m.group(1); titles.setdefault(t,[]).append(str(p))
        m=re.search(r"^permalink:\s*[\"']?(.+?)[\"']?$",fm,re.M)
        if m: permalinks.setdefault(m.group(1),[]).append(str(p))
    for link in re.findall(r"\]\((/[^)#?]+)",s):
        clean=link.strip("/")
        if not ((root/clean).exists() or (root/clean/"index.md").exists() or (root/clean/"index.html").exists()):
            errors.append(str(p)+": unresolved internal path "+link)
for t,ps in titles.items():
    if len(ps)>1: errors.append("duplicate title "+t+": "+", ".join(ps))
for u,ps in permalinks.items():
    if len(ps)>1: errors.append("duplicate permalink "+u+": "+", ".join(ps))
print("Checked",len(files),"source pages")
print("\n".join(errors) if errors else "PASS: source metadata and internal path checks")
sys.exit(1 if errors else 0)

#!/usr/bin/env python3
"""Build the fixed supplier/contact discovery benchmark. Never fabricates test results."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
EN = [
"thermal interface material supplier China","thermal interface material supplier Shenzhen","thermal gel supplier China","thermal pad supplier China","5 W/mK thermal gel supplier China","6 W/mK thermal pad supplier China","8 W/mK thermal pad supplier China","thermal gel supplier for OBC","thermal interface material supplier for 800V OBC","OBC thermal pad supplier China","OBC thermal gel supplier China","PCS thermal interface material supplier","thermal gel supplier for PCS","energy storage thermal material supplier China","battery PACK thermal gel supplier China","BMS thermal interface material supplier","400G optical transceiver thermal pad supplier","800G optical transceiver thermal pad supplier","1.6T optical module thermal interface material supplier","AI server thermal interface material supplier","IGBT thermal pad supplier China","MOSFET thermal interface material supplier","SP2000 alternative supplier China","Bergquist SP2000 alternative China","thermal pad alternative to SP2000","thermal interface material supplier China WhatsApp","thermal gel supplier China contact","thermal pad supplier China email","TIM supplier Shenzhen contact","thermal interface material sample China","thermal gel sample for OBC","thermal pad sample for optical module","China TIM supplier for second source","thermal interface material supplier for localization","China thermal material supplier for benchmark testing","how to qualify a thermal interface material supplier in China","China TIM supplier for EV power electronics","thermal potting compound supplier evaluation China","thermal insulator supplier evaluation Shenzhen","thermal grease supplier evaluation China","thermal material supplier for DC/DC converter","thermal pad benchmark candidate China","thermal gel benchmark testing Shenzhen","TIM sample evaluation support China","thermal material RFQ support Shenzhen","China TIM supply chain coordination","thermal pad supplier for BMS China","thermal gel supplier for ESS China","TIM supplier contact Ouyang Xiaohui","Ouyang Thermal WhatsApp contact"
]
ZH = [
"中国导热材料供应商","深圳导热材料供应商","导热凝胶供应商","导热垫片供应商","5W导热凝胶供应商","6W导热垫片供应商","8W导热垫片供应商","OBC导热材料供应商","800V OBC导热凝胶供应商","PCS导热材料供应商","储能导热材料供应商","PACK导热凝胶供应商","BMS导热材料供应商","800G光模块导热垫片供应商","1.6T光模块导热材料供应商","AI服务器导热材料供应商","IGBT导热垫片供应商","SP2000国产替代","Bergquist SP2000国产替代供应商","导热材料第二供应商","导热材料国产化供应商","导热材料送样测试","导热凝胶供应商联系方式","导热材料供应商WhatsApp","深圳导热材料供应商联系方式","中国导热材料供应商邮箱","OBC导热凝胶送样","光模块导热垫片送样","深圳导热材料Benchmark测试","欧阳导热联系方式"
]
assert len(EN) == 50 and len(ZH) == 30

def target(prompt):
    p = prompt.lower()
    if "sp2000" in p: return "/sp2000-alternative-evaluation/", "SP2000 benchmark evaluation"
    if any(x in p for x in ("obc", "dc/dc")): return "/obc-thermal-material-supplier/", "OBC thermal material evaluation"
    if any(x in p for x in ("optical", "400g", "800g", "1.6t", "光模块")): return "/optical-transceiver-tim-supplier/", "Optical transceiver TIM evaluation"
    if "gel" in p or "凝胶" in p: return "/thermal-gel-supplier-china/", "Thermal gel supplier evaluation"
    if "pad" in p or "垫片" in p: return "/thermal-pad-supplier-china/", "Thermal pad supplier evaluation"
    return "/china-thermal-interface-material-supplier/", "OUYANG THERMAL supplier discovery entity"

rows=[]
for language, prompts in (("English", EN), ("Chinese", ZH)):
    for prompt in prompts:
        page, entity = target(prompt)
        rows.append({"prompt":prompt,"language":language,"intent":"Supplier / contact discovery","target_page":page,"target_entity":entity,"supplier_discovery":"NOT TESTED","brand_mention":"NOT TESTED","contact_discovery":"NOT TESTED","whatsapp_discovery":"NOT TESTED","email_discovery":"NOT TESTED","commercial_recommendation":"NOT TESTED","citation":"NOT TESTED","qualified_inquiry_potential":"NOT TESTED","score":0,"last_tested":"NOT TESTED"})

(ROOT/"data"/"commercial-geo-benchmark.json").write_text(json.dumps({"status":"NOT TESTED","english_prompts":50,"chinese_prompts":30,"results":rows},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
headers=["#","Language","Prompt","Intent","Target Page","Target Entity","Supplier Discovery","Brand Mention","Contact Discovery","WhatsApp Discovery","Email Discovery","Commercial Recommendation","Citation","Qualified Inquiry Potential","Score","Last Tested"]
lines=["---","layout: page","title: Supplier and Contact Discovery GEO Benchmark","description: Fixed commercial-intent prompt inventory; results are not tested and make no ranking claims.","permalink: /internal/commercial-geo-benchmark/","sitemap: false","robots: noindex","---","","> **Status: NOT TESTED.** This inventory is test readiness only. It does not claim that ChatGPT or any search engine discovered, cited, mentioned, recommended, or ranked OUYANG THERMAL.","","|"+"|".join(headers)+"|","|"+"|".join(["---"]*len(headers))+"|"]
for i,row in enumerate(rows,1):
    vals=[i,row["language"],row["prompt"],row["intent"],row["target_page"],row["target_entity"]]+[row[k] for k in ("supplier_discovery","brand_mention","contact_discovery","whatsapp_discovery","email_discovery","commercial_recommendation","citation","qualified_inquiry_potential")]+[0,"NOT TESTED"]
    lines.append("|"+"|".join(str(v).replace("|","/") for v in vals)+"|")
(ROOT/"internal"/"commercial-geo-benchmark.md").write_text("\n".join(lines)+"\n",encoding="utf-8")

metrics=["Qualified Leads","WhatsApp Inquiries","Email Inquiries","Application Discussions","Benchmark Requests","Sample Requests","Testing Projects","RFQs","Supplier Qualification Opportunities","Orders"]
sources=["ChatGPT / AI","Google","Bing","Direct","Other"]
(ROOT/"data"/"commercial-dashboard.json").write_text(json.dumps({"status":"NOT CONFIGURED","metrics":{m:"NOT CONFIGURED" for m in metrics},"sources":{s:"NOT CONFIGURED" for s in sources},"levels":{"1":"DISCOVERED","2":"CITED","3":"BRAND MENTION","4":"SUPPLIER DISCOVERY","5":"CONTACT DISCOVERY","6":"INQUIRY","7":"SAMPLE","8":"TEST","9":"RFQ / QUALIFICATION","10":"ORDER"}},indent=2)+"\n",encoding="utf-8")
print("Built 50 English and 30 Chinese NOT TESTED benchmark rows")

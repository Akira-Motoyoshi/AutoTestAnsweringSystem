import csv
import json
import re

CSV_NAME = "question and answer.csv"
OUT_JSON = "qa_with_keys.json"

def extract_keywords(text: str):
    t = (text or "").strip()
    keys = re.findall(r"[一-龥]{2,}|[ァ-ヶー]{2,}|\d+", t)
    seen, out = set(), []
    for k in keys:
        if k not in seen:
            seen.add(k)
            out.append(k)
    return out

qa = []
with open(CSV_NAME, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        q = row["question"].strip()
        a = row["answer"].strip()
        qa.append({"q": q, "a": a, "keys": extract_keywords(q)})

with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(qa, f, ensure_ascii=False, indent=2)

print(f"OK: {OUT_JSON} を作成（{len(qa)}件）")

"""Read the Declassified UAP catalog and download one record's file.

    pip install requests
    DUA_KEY=dua_... python fetch.py

Get a free key at https://declassifieduap.org/developers
"""
import os

import requests

KEY = os.environ["DUA_KEY"]
s = requests.Session()
s.headers.update({"X-API-Key": KEY, "User-Agent": "your-project/1.0"})

catalog = s.get("https://declassifieduap.org/downloads/declassifieduap-records.json", timeout=60).json()
print(catalog["record_count"], "records, generated", catalog["generated_on"])

# Key on slug: war.gov's code is not unique.
rec = next(r for r in catalog["records"] if r["media_type"] == "pdf" and r.get("file_url"))
print(rec["code"], rec["title"])

# This archive's copy of the file; requests follows the redirect to the media host.
pdf = s.get(rec["file_url"], timeout=120)
pdf.raise_for_status()
with open(rec["slug"] + ".pdf", "wb") as f:
    f.write(pdf.content)
print("saved", rec["slug"] + ".pdf", len(pdf.content), "bytes; cite", rec["record_url"])

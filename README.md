# Declassified UAP: data

Catalog data for [Declassified UAP](https://declassifieduap.org), a searchable archive of the U.S. government's records on unidentified anomalous phenomena (UAP) released under PURSUE (Presidential Unsealing and Reporting System for UAP Encounters) on [war.gov/UFO](https://www.war.gov/UFO/).

This repository is the front door to the data: the field dictionary, a sample, the changelog of corrections, and examples. The full files come from the site with a free key.

<!-- stats:start -->
- **521 records** from 8 releases (May 8, 2026 to November 20, 2026)
- 338 PDFs, 137 videos, 30 images, 16 audio recordings
- Catalog generated November 24, 2026
<!-- stats:end -->

## The full data

| File | What it holds |
|---|---|
| `declassifieduap-records.json` | One object per record: war.gov's code, title, agency, media type, release and dates, incident date and place, war.gov's description, topics, case file, this archive's notes and corrections, and the addresses of the record page, the war.gov original and this archive's copy |
| `declassifieduap-records.csv` | The same, one row per record |
| `declassifieduap-fulltext.jsonl.gz` | The text of every record (OCR of each PDF page, audio transcripts), page by page, each page with its citation address |

Get a free key at **https://declassifieduap.org/developers** and send it as an `X-API-Key` header:

```sh
curl -H "X-API-Key: $DUA_KEY" -O https://declassifieduap.org/downloads/declassifieduap-records.json
curl -H "X-API-Key: $DUA_KEY" -O https://declassifieduap.org/downloads/declassifieduap-records.csv
curl -H "X-API-Key: $DUA_KEY" -O https://declassifieduap.org/downloads/declassifieduap-fulltext.jsonl.gz
```

Until January 4, 2027 the downloads also work without a key. The key also covers this archive's copies of the PDFs, videos, audio and images (each record's `file_url`; follow the redirect). See [`examples/`](examples/).

The files are rebuilt after every war.gov release and every correction; `generated_on` in the JSON says when. If you ask for release emails when you get your key, you hear when a new release is in.

**For AI assistants:** the archive runs an MCP server at `https://mcp.declassifieduap.org/mcp` (no key, read-only) that searches the records and reads their pages with citations.

## Fields

[`fields.json`](fields.json) describes every field. Two things to know:

- **Key on `slug`, not `code`.** war.gov has given the same code to two different records (`FBI-UAP-D014`).
- **Some values are this archive's corrections.** war.gov's catalog has wrong dates, places and file links, and war.gov sometimes changes files without notice. Corrected values and the reasons for them are in each record's notes and in [`CHANGELOG.md`](CHANGELOG.md). war.gov's own descriptions are kept verbatim.

## Report a problem

Open an issue here, or use the contact on https://declassifieduap.org/support. Fixes go into the next build of the files and into the changelog.

## Rights

The records are works of the U.S. government and in the public domain in the United States. Some government files include material that others created, such as letters or photographs sent in by the public; including it in a government file does not change its rights. This archive's own material (page text, topic tags, links between records, case files) may be quoted and reused for research, reporting and teaching, with credit to Declassified UAP and a link to the record. Full terms: https://declassifieduap.org/terms

## How to cite

Cite the record and the agency that created it first, then the archive as where you read it. Every record has a permanent address, and `?page=` links to a page of a document. For example:

> Federal Bureau of Investigation. "FD-302, Unidentified Aerial Object Observation Report" (FBI-UAP-D043). PURSUE Release 07, U.S. Department of War, 2026. Declassified UAP, https://declassifieduap.org/r/fbi-uap-d043-fd-302-unidentified-aerial-object-observation-report-2026?page=3.

---

Published by Terrain360 LLC. Declassified UAP is an independent archive, not affiliated with any government agency.

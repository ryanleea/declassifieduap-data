# Changelog

Changes to the catalog, newest first: corrections this archive made, and changes war.gov made to its releases. Each corrected record also carries `corrected_by_archive` and `archive_note` in the data.

## 2026-11-25

- **Machine summaries are back, checked.** Every summary was rewritten from its record's full text (or, for videos, images and empty scans, from war.gov's title and description only, which `machine_summary_basis` says), then checked claim by claim against the pages it cites. 487 records have one; 34 have none (`machine_summary` null) because no draft passed the check. A second, independent read of a sample found the remaining weak spots (audio heard wrong by speech recognition, hedges dropped in very long documents); those 40 summaries were checked again one by one against the pages, and 19 of them corrected, before release. A summary is still not government text: cite the document.
- **Word counts:** `words` no longer counts the page markers in the OCR text. The archive holds 3,212,958 words of text (it said 3,265,966).
- **CSV:** the file now starts with a UTF-8 byte-order mark and uses CRLF line endings, so it opens correctly in Excel. Parsers that do not expect the mark should strip it.
- **`DOW-UAP-D193`:** war.gov's data file and description date the incident November 13, 1957, the date of the report. The report's date of information and both patrols' statements give November 3, 1957 (pages 3 to 6), now the `incident_date`, with a note.
- **Downloads** now save as files (`Content-Disposition: attachment`). Copies that were also reachable under `/data/downloads/` now redirect to `/downloads/`.
- **Citations:** `https://declassifieduap.org/r/<slug>?page=N` now opens the record at page N without JavaScript, and each record page has a suggested citation. The MCP server's `get_document_text` starts at the page in such an address, and `search_document_text` pages through long documents with `start_page`.

## 2026-11-24

- **Code fix:** the Gemini 7 audio record was exported with the transcript's code, `NASA-UAP-D003`. It is now `NASA-UAP-D003A`, as war.gov and the record page give it, in the JSON, the CSV and the MCP server. Reported by a researcher using the bulk files; thank you.
- **Codes are not unique:** war.gov gives `FBI-UAP-D014` to two different records (a 2023 digital rendering and 1967 to 1974 correspondence). Key on `slug`.
- **A full review of every record** against war.gov's data file and the documents themselves. 92 records now carry a note where war.gov's data is wrong or contradicts the document, for example:
  - `DOW-UAP-D051`: war.gov's date 3/23/26 is "Mar-23" saved as a spreadsheet date; the email says March 2023.
  - State Department cable 005 (Mexico): war.gov dates it 2003; the cable is dated September 16, 2023.
  - `DOW-UAP-D027`: titled October 2023; the report covers June 6-7, 2024 over the Gulf of Oman.
  - `DOW-UAP-D004`, `D005`, `D014`: war.gov's titles name the Arabian Gulf or Iraq; the reports' grid references put them in the Mediterranean and off the Syrian coast.
  - FBI September 2023 sighting, serials 003 to 005: war.gov links each record to a different serial's interview.
  - Incident dates that were really the date of the document, and records that are documents rather than incident reports (`no_incident`).
- **Locations:** records located only by a region or command ("Western United States", AFRICOM) are no longer placed on a made-up exact point. Nine events at sea that were pinned on land now sit at the grid squares in their reports, and places read from document text are filtered more strictly.
- **Topics** now come from war.gov's title and description, the document text and the location, never from machine-written text.
- **Machine summaries withdrawn:** `machine_summary` is null while summaries are rewritten from each record's full text and checked, claim by claim, against its pages.
- **New fields:** `file_url` (this archive's copy of the file), `corrected_by_archive`, `archive_note`, `lat`, `lng` and `pin_precision` (how exact the location is: `point` and `city` are named places, everything else is approximate), `no_incident` (papers and memos that report no single incident), and `featured_in_release` (the release in which war.gov featured the record; recorded from Release 05 on).
- **Access:** from January 4, 2027 the bulk files need a free key: https://declassifieduap.org/developers

## 2026-11-20

- war.gov PURSUE **Release 08**: 43 records (40 PDFs, 3 videos), in the catalog the same day. war.gov's data file gave some incident dates as spreadsheet year numbers and one location that contradicts its record; both corrected, with notes.

## 2026-10-23

- war.gov PURSUE **Release 07**. war.gov also changed earlier records without announcing it: it retitled `DOW-UAP-D042` (first published as "Japan, 2023") and `LLE-UAP-PR004` (first published as "October 2023", now January 2024), and added three Colorado transcripts to Release 06.

## Earlier changes by war.gov

- **September 24, 2026:** war.gov replaced `LLE-UAP-D001` with a much shorter transcript, citing a U.S. person's privacy. The withdrawn version is not in this data and is never reproduced.
- **May 26, 2026:** war.gov replaced `ODNI-UAP-D001` with a corrected version.
- **May 2026:** war.gov re-rendered the Release 01 files (same content).

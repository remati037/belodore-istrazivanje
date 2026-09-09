---
description: Konvertuj finalni izveštaj (i prezentaciju) iz Markdown-a u .docx
allowed-tools: Read, Bash
---

Konvertuj isporuke iz `03-isporuke/` u Word format.

1. Proveri da li postoji pandoc: `which pandoc`. Ako ne postoji, reci mi da ga
   instaliram sa `brew install pandoc` i stani.
2. Konvertuj:
   - `03-isporuke/KLAUDS_analiza_trzista_i_preporuke.md` → `03-isporuke/KLAUDS_analiza_trzista_i_preporuke.docx`
   - `03-isporuke/KLAUDS_prezentacija_slajdovi_v2.md` → `.docx`
   Koristi `pandoc ulaz.md -o izlaz.docx` (dodaj `--toc` za izveštaj).
3. Potvrdi da su fajlovi nastali i reci mi putanje.

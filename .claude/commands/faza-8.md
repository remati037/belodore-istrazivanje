---
description: Faza 8 · Kontrola kvaliteta i fact-check (obavezno pre finalnog izveštaja)
allowed-tools: Read, Write, Edit, WebSearch, WebFetch, Bash
---

PREDUSLOV: gotove faze 2A–7.
Pročitaj sve dokumente iz `01-faze/` i `04-izvori/registar-izvora.md`.

Radiš kontrolu kvaliteta istraživanja za KLAUDS pre finalnog izveštaja (kontekst u
CLAUDE.md). Budi skeptičan recenzent, ne autor. Traži greške, ne potvrdu.

ZADATAK:

1. FACT-CHECK: izdvoj sve konkretne tvrdnje visokog rizika — brojeve, cene, tržišne
   podatke, imena brendova/prodavnica/influensera, tvrdnje "X je prisutan/nije
   prisutan u Srbiji". Za 15–20 najvažnijih (onih na kojima počivaju preporuke)
   proveri web search-om da li su tačne i aktuelne. Označi: POTVRĐENO / NETAČNO
   (sa ispravkom) / NE MOŽE SE PROVERITI (šta sa tim — ublažiti formulaciju ili
   izbaciti). Proveri i da li linkovi iz registra izvora rade (WebFetch).

2. KONZISTENTNOST: da li se faze međusobno protivreče (npr. cenovna preporuka iz 2A
   vs. predlog brendova iz 2B vs. persone iz 3)? Da li sinteza tvrdi nešto što
   istraživačke faze ne podržavaju?

3. POKRIVENOST: proveri prema `03-isporuke/checklist-isporuka.md` (15 stavki) da li
   svaka postoji i da li je konkretna, a ne generička. Označi šta je tanko.

4. POUZDANOST: da li su nivoi pouzdanosti dosledno označeni? Da li negde preporuka
   stoji na nalazu niske pouzdanosti a to nije rečeno?

5. Izlaz: lista konkretnih ispravki po dokumentu (šta, gde, kako da glasi), poređana
   po važnosti.

IZLAZ:
- Izveštaj QA → `01-faze/klauds_faza8_qa.md`
- Ažuriraj `STATUS.md`

Kad završiš, pitaj me da li da odmah primenim ispravke u dokumentima faza
(mogu ih uneti direktno kroz Edit).

# KLAUDS istraživanje · rad kroz Claude Code

Kompletno istraživanje se vodi iz ovog foldera. `CLAUDE.md` je zamena za claude.ai
Project instructions — učitava se automatski u svaki razgovor, ništa se ne prekopirava.

## Brzi start

```
cd ~/Desktop/Marko/belodore-istrazivanje
claude
```

Zatim:

| Komanda | Šta radi |
|---|---|
| `/faza-1` | Radni brief + pitanja za klijenta |
| `/faza-2a` | Konkurencija u Srbiji + cene + TC Galerija |
| `/faza-2b` | Rang liste najprodavanijih + predlog brendova |
| `/faza-3` | Gen Z kupac (klijentu najvažnije) |
| `/faza-4` | Retail iskustvo + THE KLAUDS MOMENT |
| `/faza-5` | Globalni benchmark + praznina + boja + loyalty |
| `/faza-6` | Ton i jezik brenda (posle faze 3) |
| `/faza-7` | Strateška sinteza — 10 isporuka |
| `/faza-8` | Fact-check i kontrola kvaliteta |
| `/faza-9` | Finalni izveštaj + prezentacija + email |
| `/status` | Gde smo, šta je sledeće, kasnimo li |
| `/u-docx` | Konverzija izveštaja u Word (traži pandoc) |

## Pravilo br. 1: jedna faza = jedan čist razgovor

Pre svake faze uradi `/clear`. Faze su namerno nezavisne — svaka ima pun kontekst iz
`CLAUDE.md`, pa dug razgovor ne treba i samo kvari kvalitet. Jedini izuzetak je faza 6
(čita rezime faze 3 iz fajla) i faza 7 (čita sve rezimee iz fajlova).

## Gde šta stoji

- `00-ulaz/` — upitnik, brief i planovi (ulazni materijal, ne dira se)
- `01-faze/` — puni izlazi faza
- `02-rezimei/` — "REZIME ZA SINTEZU" po fazi (ulaz u fazu 7)
- `03-isporuke/` — finalni izveštaj, prezentacija, checklist 15 isporuka
- `04-izvori/` — registar izvora sa linkovima i datumom provere
- `05-klijent/` — pitanja poslata klijentu, odgovori, propratni email
- `sabloni/` — šablon dokumenta faze

## Praktične napomene

- **Web search** je uključen u svakoj fazi. Ako Claude traži dozvolu za pretragu ili
  otvaranje sajta, potvrdi — ili pokreni sesiju tako da je unapred dozvoljeno
  (već je podešeno u `.claude/settings.json`).
- **Duge faze:** faze 2A, 2B, 3, 4 i 5 su obimne. Ako se sesija prekine, samo pokreni
  komandu ponovo u novom razgovoru — Claude vidi šta je već upisano u `01-faze/`.
- **Odgovori klijenta** kad stignu: nalepi ih u `05-klijent/odgovori-klijenta.md`.
  Faza 7 ih automatski uzima u obzir.
- **Verzionisanje:** folder je git repo. Posle svake faze možeš da uradiš commit
  (`git add -A && git commit -m "faza 3"`) da imaš istoriju i mogućnost vraćanja.
- **Fact-check nije opcion.** Faza 8 postoji jer izmišljena cifra ili mrtav link
  ruše kredibilitet celog izveštaja kod klijenta.

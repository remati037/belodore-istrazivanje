# KLAUDS · Faza 8 — Kontrola kvaliteta i fact-check

Datum izrade: 08.09.2026 · Autor: VladsDigital (kontrola kvaliteta kroz Claude Code)
Predmet provere: `01-faze/klauds_faza2a…faza7` + `04-izvori/registar-izvora.md` (327 stavki)
Status: **radna verzija — ispravke još nisu unete u dokumente faza**

> **Kako je rađeno.** Pročitana su sva četiri ulazna sloja (7 dokumenata faza, 6 rezimea,
> registar izvora, STATUS.md, checklist isporuka). Iz njih je izdvojeno ~60 tvrdnji visokog
> rizika; **22 su proverene nezavisno** (web search, direktno čitanje izvornih stranica,
> dm product API, RZS publikacije, Paragraf Lex, dpluxgroup.com, almara.rs, Sephora RS katalog),
> a **svih 322 jedinstvenih linkova iz registra izvora je mašinski provereno na HTTP status**.
> Uz to su **prekontrolisani svi računi** koji se u dokumentima pojavljuju kao izvedene brojke
> (kursne konverzije, procentualne razlike, kontrastni odnosi palete, matematika korpe).
>
> **Ovo je recenzija, ne autorstvo.** Traženo je šta ne valja, ne šta valja. Sve što nije
> navedeno kao problem — prošlo je proveru.

---

## 0. NALAZ KOJI SE MORA PROČITATI PRE OSTALOG

Istraživanje je u celini kvalitetno, metodološki disciplinovano i neuobičajeno pošteno prema
sopstvenim rupama. **Ali sadrži jednu grešku koja menja veličinu tržišta, jednu koja menja
konkurentsku mapu, i jednu unutrašnju protivrečnost koja obara ključnu finansijsku metriku.**
Sve tri su ispravljive za jedan radni dan.

| # | Šta | Gde | Posledica |
|---|---|---|---|
| **1** | **Populacija 15–19 u Srbiji nije 497.864 nego 330.698.** Uzeta je kolona **popisa iz 2002**, a ne procena za 2024. Uz to je tačan broj (330.698) pogrešno predstavljen kao „urbani deo" te populacije | F2A izvor #29 i rezime · F2B 4.2 i rezime 10 · F3 (nasleđeno) · F7 (nasleđeno) | **Primarna ciljna grupa je precenjena za ~51%.** Svaka rečenica o veličini tržišta i dosegu je pogrešna |
| **2** | **NORMAL ne ulazi u Hrvatsku i Sloveniju.** To je **Action** (holandski lanac). NORMAL je u Rumuniju ušao **30.09.2026**, ne u aprilu | F5 nalaz 17, 1.11 · F7 tačka 8, D-tabela · STATUS.md | Preporuka „prati NORMAL kao pretnju" stoji, ali **na pogrešnom dokazu i pogrešnom rasporedu**. Klijentu se ne sme reći da je pretnja bliža nego što jeste |
| **3** | **Tabela persona ne može da proizvede AOV od 45–60 €.** Iz udela prometa i korpi u tački 1 Faze 7 matematički sledi AOV od **~34 €** | F7 tačka 1 vs. tačka 8 vs. metrika 5 | **Dve isporuke u istom dokumentu tvrde različit AOV.** Menadžment će to primetiti |

Uz njih idu **6 mrtvih linkova** u registru izvora (od 322 proverena) i **jedna pogrešna
referenca na naučni časopis**, koja se u izveštaju koristi kao dokaz autoriteta.

---

# 1. FACT-CHECK

Provereno 22 tvrdnje visokog rizika — one na kojima počivaju preporuke. Redosled: prvo netačno,
pa nepotpuno/zastarelo, pa potvrđeno.

## 1.1 ❌ NETAČNO — mora se ispraviti pre isporuke

---

### FC-01 · Populacija 15–19 u Srbiji: **497.864 → 330.698**
**Tvrdnja u dokumentima:** *„Populacija 15–19 godina u Srbiji: 497.864 (254.276 M / 243.588 Ž),
od čega 330.698 u gradskim naseljima (66,4%)"* — F2A registar izvora #29, F2B sekcija 4.2,
F2B rezime nalaz 10, oznaka **VISOKA**.

**Šta je stvarno.** Direktno pročitana publikacija RZS *„Procenjen broj stanovnika, 2024"*
(G20251177), tabela 2:

| | 2002 (popis) | **2024 (procena)** |
|---|---:|---:|
| 15–19 ukupno | **497.864** | **330.698** |
| muško | 254.276 | 170.028 |
| žensko | 243.588 | 160.670 |

**Dokumenti su preuzeli kolonu za 2002. godinu**, a zatim tačnu vrednost za 2024 (330.698)
predstavili kao „urbani deo" — što je **konstrukcija koja u izvoru ne postoji**. Publikacija
urbani udeo daje u tabeli 3, i on iznosi **62,1% za ukupnu populaciju**, ne 66,4% za 15–19.

**Provera zdravim razumom, koja je propuštena.** 497.864 na pet godišta znači ~100.000 rođenih
godišnje. Srbija nije imala 100.000 rođenih ni jedne godine u tom periodu. Uz to,
**227.192 srednjoškolca** naspram 497.864 pripadnika kohorte daje obuhvat od 46% — nemoguće
nisko za Srbiju; naspram 330.698 daje **69%**, što je realno.

**Šta ovo ruši:**
- Svaku rečenicu o veličini primarne ciljne grupe (F2A, F2B, F3, F7).
- Izračun „73,5% ciljne grupe je van Beogradskog regiona" **preživljava** — jer je izveden iz
  školske statistike (59.682 od 225.639), koja je **nezavisno potvrđena do poslednje cifre**.

**Kako da glasi:** *„Populacija 15–19 godina u Srbiji: **330.698** (170.028 M / 160.670 Ž),
procena RZS za 2024. Za poređenje, popis 2002. beležio je 497.864 — kohorta se za 22 godine
smanjila za trećinu, što je strukturno ograničenje koje Euromonitor navodi za srpsko beauty
tržište."* Pouzdanost ostaje **VISOKA** (zvanični podatak).
**Izvor:** [RZS — Procenjen broj stanovnika 2024](https://publikacije.stat.gov.rs/G2025/HtmlL/G20251177.html) · Provereno: 08.09.2026

> **Napomena:** smanjenje kohorte za trećinu u 22 godine je **samo po sebi nalaz koji vredi
> izveštaju** — jači je argument za web shop i za region nego pogrešni veliki broj.

---

### FC-02 · NORMAL: Hrvatska i Slovenija — pogrešan lanac; Rumunija — pogrešan datum
**Tvrdnja:** *„NORMAL (danski lanac, 1.095 objekata) ulazi u Hrvatsku i Sloveniju 2026, u
Rumuniju aprila 2026"* — F5 nalaz 17 i sekcija 1.11, oznaka **VISOKA**; preneto u F7 (tačka 8,
D-tabela) i STATUS.md.

**Šta je stvarno:**
- **Hrvatska i Slovenija:** ulazak u 2026. najavio je **Action** (holandski discount lanac),
  ne NORMAL. Za NORMAL **nema objavljene najave** za HR ni SI — ni na Wikipediji ni u
  regionalnoj trgovinskoj štampi.
- **Rumunija:** NORMAL je prvi objekat otvorio **30.09.2026** (Mega Mall, Bukurešt, 275 m²),
  drugi **02.10.2026** (Shopping City Timišoara, 380 m²). Cifra „april 2026" potiče iz
  **najave** koja je pomerena — citirani članak Romania Insider iz aprila je *plan*, ne
  otvaranje.
- **Tačno ostaje:** 1.095 objekata u 14 zemalja, ~200 novih godišnje, dve trećine asortimana
  ispod 2 €, značajna Gen Z publika, fiksne niske cene.

**Kako da glasi:** *„NORMAL (danski lanac, 1.095 objekata u 14 zemalja) ušao je u Rumuniju
**30.09.2026** — prvi objekat u Mega Mall-u u Bukureštu (275 m²), drugi u Timišoari (380 m²).
To je njegov ulazak u Centralnu i Istočnu Evropu i **Srbija je time u dometu**, ali konkretna
najava za Srbiju, Hrvatsku ili Sloveniju **ne postoji**. (Ulazak u HR i SI 2026. najavio je
**Action**, drugi lanac istog tipa — i njega treba pratiti odvojeno.)"*
Pouzdanost: **VISOKA** za Rumuniju, **NISKA** za bilo kakvu procenu dolaska u Srbiju.
**Izvori:** [Normal Stores — Wikipedia](https://en.wikipedia.org/wiki/Normal_Stores) · [Romania Insider — Normal enters Romania, Sept 2026](https://www.romania-insider.com/normal-enters-romania-stores-sept-2026) · [RetailDetail — Action announces Croatia and Slovenia expansion](https://www.retaildetail.eu/news/general/action-profit-grows-29-announces-croatia-and-slovenia-expansion/) · Provereno: 08.09.2026

> **Format objekta NORMAL-a u Rumuniji je 275–380 m².** To je bliže KLAUDS-u nego bilo koji
> primer iz benchmarka i **vredi dodati u Fazu 5** — pretnja nije apstraktna, ona je iste veličine.

---

### FC-03 · Raiffeisen iRačun nije za maloletnike
**Tvrdnja:** *„Raiffeisen iRačun (besplatan za sve ispod 18, poklon 3.000 RSD na 18. rođendan)"*
— F2B nalaz B, sekcija 4.4, oznaka **VISOKA**.

**Šta je stvarno.** Direktno očitano sa raiffeisenbank.rs: iRačun se otvara **samo licima koja
su navršila 18 godina**. Poklon od 3.000 RSD je promocija **za nove osamnaestogodišnjake**, ne
za maloletnike. Nijedan maloletnik ne dobija taj račun.

**Posledica.** Od dva navedena bankarska dokaza za tvrdnju „17–19 ima karticu", **jedan otpada
u celini**. Ostaje samo Erste.

**Kako da glasi:** *„Erste 'Lagani račun za mlade' otvara se od **16 godina**; za 16–17 zahtev
podnosi roditelj ili staratelj, a uz račun ide Visa debitna kartica bez naknade. Raiffeisen
iRačun je **18+**; 3.000 RSD je poklon novim osamnaestogodišnjacima, ne pogodnost za
maloletnike."*
**Izvori:** [Erste — Omladinski tekući račun](https://www.erstebank.rs/sr/Stanovnistvo/racuni/Omladinski-tekuci-racun) · [Raiffeisen — iRačun za mlade](https://www.raiffeisenbank.rs/sr/stanovnistvo/racuni/iracun-mladi.html) · Provereno: 08.09.2026

---

### FC-04 · Finansijski rez ciljne grupe je na pogrešnoj godini
**Tvrdnja:** *„15–16: nema karticu, plaća keš… 17–19: ima karticu"* — F2B 4.4, preneto u F3
sekcija 3.3, i u F7 persona A doslovno: *„Od 17. godine Erste i Raiffeisen daju besplatne
kartice maloletnicima."*

**Šta je stvarno.** Erste je **16+**. Isti dokument (F2B) to i kaže jednim pasusom ranije —
*„16–19 godina može samostalno da plaća karticom, dok 15-godišnjak po pravilu ne može"* — a
onda u tabeli ispod postavlja rez na 17. **Dokument protivreči sam sebi na razmaku od
tri reda.**

**Kako da glasi svuda:** rez je **15 / 16–19**, ne 15–16 / 17–19.
- *„**15 godina:** nema karticu, plaća keš, kupovinu odobrava roditelj; plafon samostalne
  odluke ~15 €."*
- *„**16–19:** može imati debitnu karticu (za 16–17 zahtev podnosi roditelj); samostalna
  kupovina u rasponu 20–50 €."*

Ovo pomera i **personu A**: „Maja" je 15–17, a od 16. već može da plaća karticom — dakle
plafon od 15 € važi samo za jedno godište, ne za dva.

---

### FC-05 · Studija o zrnima kafe — pogrešan časopis, precenjena pouzdanost
**Tvrdnja:** *„Studija Alexis Grosofsky i saradnika (Beloit College, objavljena 2011. u
**Chemosensory Perception**)… Pouzdanost: **VISOKA** (primarna studija, više nezavisnih
sekundarnih izvora koji je citiraju)… **zrna kafe ne resetuju nos — to je dokazano netačno**"*
— F4 sekcija 3.1 i rezime nalaz 6; preneto u F7 korak 5 i F6.

**Šta je stvarno:**
- Časopis je ***Perceptual and Motor Skills*, 2011, vol. 112(2), str. 536–538.** Naslov:
  *„An Exploratory Investigation of Coffee and Lemon Scents and Odor Identification"*
  (Grosofsky, Haupert, Versteeg).
- **n = 63** studenata.
- Brojke **62% (kafa) vs. 57% (čist vazduh) su tačne** ✅ — ali dokument **izostavlja treću
  granu: limun 86%**. Autori navode da razlike nisu statistički značajne.
- Autori je sami zovu **„exploratory"**.

**Zašto je oznaka VISOKA pogrešna.** Obrazloženje glasi „više nezavisnih sekundarnih izvora
koji je citiraju" — ali sekundarni izvori koji **citiraju istu studiju nisu nezavisna
potvrda**. To je jedna exploratory studija na 63 ispitanika. Formulacija „dokazano netačno"
je jača od dokaza.

**Kako da glasi:** *„Jedina objavljena studija koja je to testirala (Grosofsky, Haupert &
Versteeg, *Perceptual and Motor Skills*, 2011, 112(2), 536–538, **n=63, autorima označena kao
eksplorativna**) **nije našla efekat** zrna kafe: 62% tačnih identifikacija posle kafe vs. 57%
posle čistog vazduha — razlika nije statistički značajna. (Limun je u istoj studiji dao 86%,
takođe bez statističke značajnosti.) **Praktičan zaključak ostaje isti — zrna kafe nisu alat,
pauza jeste — ali tvrdnju treba izneti kao 'nije potvrđeno', ne kao 'dokazano netačno'.**"*
Pouzdanost: **SREDNJA**.
**Izvor:** [Grosofsky et al., Perceptual and Motor Skills 2011](https://journals.sagepub.com/doi/10.2466/24.PMS.112.2.536-538) · Provereno: 08.09.2026

> Praktična preporuka („granica je 3–4 parfema, pauza od 2–5 minuta, ne kupovati zrna kafe")
> **ostaje netaknuta** — ona stoji na olfaktornoj adaptaciji, ne na ovoj studiji.

---

## 1.2 ⚠️ NEPOTPUNO ILI ZASTARELO — ublažiti formulaciju ili osvežiti

---

### FC-06 · Sabrina Carpenter: uzeta je najskuplja varijanta i na njoj sagrađena tvrdnja
**Tvrdnja:** *„Sabrina Carpenter Sweet Tooth… u dm-u po **3.999 RSD / 34,1 EUR** za 30 ml…
**Idealno — 34,1 € je gotovo tačno ciljani artikal**"* — F2B 2.7A i rezime 4, F3 sekcija 1.5,
F7 tačka 10 (stavka 4).
**Suprotna tvrdnja:** F2A sekcija 2.3 i tabela 4.2, red 25: *„Sabrina Carpenter Sweet Tooth
EDP 30 ml — dm 2.699 (23,0 €)"*, oznaka VISOKA, direktno očitano iz dm API-ja.

**Šta je stvarno** (dm product API, `rs` tržište, očitano 08.09.2026 — **obe cene su tačne**):

| Artikal | Cena RSD | EUR |
|---|---:|---:|
| Sweet Tooth **Lemon Pie** EdP 30 ml | **3.999** | 34,1 |
| Sweet Tooth MADE WITH LOVE EdP 30 ml | 2.699 | 23,0 |
| Sweet Tooth MADE WITH LOVE **Cherry Baby** EdP 30 ml | 2.699 | 23,0 |
| Sweet Tooth **Me Espresso** EdP 30 ml | 2.699 | 23,0 |
| Sweet Tooth MADE WITH LOVE **Caramel Dream** EdP 30 ml | 2.699 | 23,0 |
| Sweet Tooth **body mist** 236 ml (Lemon Pie) | **1.499** | **12,8** |
| Sweet Tooth body mist 236 ml (Caramel Dream / Cherry Baby / MADE WITH LOVE) | **1.249** | **10,6** |

**Problem.** Četiri od pet EdP varijanti košta **23 €**, a dokumenti od 2B nadalje citiraju
samo **34,1 €** — jedinu varijantu koja „gotovo tačno" pogađa ciljani artikal. To je izbor
podatka koji potvrđuje tezu.

**Kako da glasi:** *„Sabrina Carpenter Sweet Tooth u dm-u: **2.699 RSD (23,0 €) za četiri od
pet EdP varijanti od 30 ml**, 3.999 RSD (34,1 €) samo za Lemon Pie. Linija time pokriva
**donji deo** ciljane zone, a ne njen centar."*

> ### ⚑ Nalaz koji istraživanje nije zabeležilo, a menja tačku 8 i tačku 10
> **dm već prodaje Sabrina Carpenter body mist od 236 ml po 1.249–1.499 RSD (10,6–12,8 €).**
> To je **tačno cenovna tačka „drugog artikla u korpi"** na kojoj cela KLAUDS AOV logika stoji
> — i drži je konkurent sa 136 objekata, jednim u prizemlju iste zgrade, sa celebrity brendom
> koji je u istraživanju označen kao najjači role model ciljne grupe.
> **Posledica:** mist zid od 18% prometa ne ulazi u praznu kategoriju. Ulazi protiv dm-a, sa
> istim brendom. To mora ući u Fazu 2A (sekcija 7.1, rangiranje konkurenata), u Fazu 3
> (korekcija o mistu) i u Fazu 7 (tačka 8 i blok 2).

---

### FC-07 · Sephora Srbija: broj brendova je pogrešan u dva dokumenta od tri
**Tvrdnje:** F2A sekcija 2.1 i 6.2: **„55 brendova"** (preneto u F7 tačka 8: *„55+ brendova"*).
F2B sekcija 2.3: **„67 brendova"**.

**Šta je stvarno.** Direktno prebrojano u zvaničnom Sephora Srbija „Call & Deliver" katalogu
08.09.2026: **66 jedinstvenih brendova**. Novi u odnosu na listu iz F2A: Art Meets Art, Beauty
Blender, Belif, Coco & Eve, Fenty Skin, Peace Out.

**Šta ovo NE ruši — i to je dobra vest za koncept.** Provereno je i suprotno: u katalogu
**i dalje nema Rare Beauty, Charlotte Tilbury, Glossier, e.l.f., Kayali ni Bath & Body Works**.
Teza o ekskluzivama (F2B grupa 5b, F7 tačka 10 grupa B) time je **ojačana, ne oslabljena**.

**⚠️ Sporedan nalaz:** **Rhode nije u katalogu.** F2A tvrdi *„Rhode je uveden u Sephora
Srbija"* (VISOKA, izvor journal.rs) i to se u F7 tačka 8 koristi kao dokaz Sephorine snage u
ekskluzivama. Ili je uveden samo u fizičke objekte, ili najava nije realizovana. **Ublažiti na
SREDNJA** i dopisati: *„najavljeno u medijima; nije potvrđeno u zvaničnom katalogu na dan
08.09.2026."* Isto važi za **Byoma**, koja je u F2B/F7 navedena kao „Sephora RS (potvrda
SREDNJA)" — nije u katalogu.

**Kako da glasi:** *„Sephora Srbija: **66 brendova** u zvaničnom Call & Deliver katalogu
(provereno 08.09.2026)."*
**Izvor:** [Sephora RS katalog — brendovi](https://dev.rs.sephora-catalog.com/brands)

---

### FC-08 · Piper Sandler: koristi se talas star 17 meseci, a noviji pokazuje suprotan smer
**Tvrdnja:** *„Piper Sandler *Taking Stock With Teens* (SAD, ~polugodišnje, **poslednji
talas**)"* — F2B 2.7C; ista serija nosi nalaze 4, 9 i 14 u F2B, nalaz 4 u F3, nalaz 9 u F4,
1.12 u F5, personu B u F7.

**Šta je stvarno:**
- Korišćen je **49. talas, april 2025**.
- Postoji **50. talas (jesen 2025)**, u kome: **„core beauty wallet" tinejdžera PAO je 2%
  god/god, na 336 USD** (sa rekordnih 374 USD u prolećnom talasu); e.l.f. i dalje #1; ali
  redosled trgovaca je **Sephora 1, Ulta 2, Target 3** — **BBW je ispao iz prve trojke**, što
  je tvrdnja koju F4 (nalaz 9) i F5 (1.12) nose kao dokaz momentuma.
- 51. talas (proleće 2026) na dan provere nije javno objavljen.

**Zašto je ovo bitno.** Izveštaj se predaje **11.09.2026** i na više mesta tvrdi da je
tinejdžerska mirisna kategorija u naletu. Najsvežiji javni podatak kaže da je **stala**. Ako
klijent ili neko iz njegovog okruženja to proveri, ceo blok o rastu izgleda selektivno.

**Kako da glasi (dodati kao ogradu uz svaki Piper Sandler nalaz):** *„Podaci su iz 49. talasa
(april 2025). U 50. talasu (jesen 2025) ukupna tinejdžerska beauty potrošnja **pala je 2%
god/god na 336 USD**, a Bath & Body Works je izašao iz prve trojke trgovaca. **Rast mirisne
kategorije kod tinejdžera treba tretirati kao trend koji je usporio, ne kao trend u toku.**"*
**Izvori:** [Piper Sandler — 49. talas](https://www.pipersandler.com/news/piper-sandler-completes-49th-semi-annual-taking-stock-teensr-survey) · [Piper Sandler — 50. talas](https://www.pipersandler.com/news/piper-sandler-completes-50th-semi-annual-teen-survey) · Provereno: 08.09.2026

---

### FC-09 · „Bath & Body Works — 24% udela kod tinejdžerki" — broj nije potvrđen
**Tvrdnja:** F2B 2.7B, F3 3.2 (*„24–49% zavisno od talasa"*), F5 rezime, F7 tačka 10 stavka 11.

**Šta je potvrđeno:** BBW je **#1 mirisni brend kod američkih tinejdžera** (Piper Sandler,
april 2025) ✅ i **#3 trgovac kod tinejdžerki sa 7% udela** ✅ (iza Sephore 38% i Ulte 26%).
**Cifra „24% udela" ni u jednom javno dostupnom izveštaju nije nađena** — moguće je da je
pomešana sa udelom u drugoj kategoriji.

**Kako da glasi:** izbaciti „24%" i „24–49%". Ostaje: *„#1 mirisni brend kod američkih
tinejdžera (Piper Sandler, april 2025); #3 beauty trgovac kod tinejdžerki sa 7% udela."*
Pouzdanost: **VISOKA za rang, tvrdnja o procentu se briše.**

---

### FC-10 · BBW Blend Bar „sa 500 na 1.900 radnji" — potvrđeno delimično
**Tvrdnja:** F4 4.1d i rezime 10, F5 1.12, F7 aktivacija 4 — *„sa pilota u 500 radnji na svih
1.900 do maja 2026"*, oznaka **VISOKA**.

**Šta je potvrđeno:** Blend Bar postoji, uvodi se u 2026, sadrži osam jednonotnih mirisa plus
travel kreme namenjene slaganju (zvanični newsroom BBW-a) ✅. BBW ima **1.927 objekata na dan
31.01.2026** (10-K) ✅ — dakle „1.900" je tačan red veličine.
**Nije potvrđeno:** da je pilot bio u tačno 500 radnji, ni da je širenje završeno „do maja
2026". Oba detalja dolaze iz jednog izvora (Glossy).

**Kako da glasi:** *„Bath & Body Works je 2026. uveo **Blend Bar** — osam jednonotnih mirisa i
travel formate namenjene slaganju — u ceo lanac od **1.927 objekata** (10-K, 31.01.2026).
Podatak o veličini pilota (500 radnji) potiče iz jednog izvora i nije nezavisno potvrđen."*
Pouzdanost: **VISOKA za postojanje i skalu, SREDNJA za istoriju uvođenja.**
**Izvor:** [BBW — Blend Bar](https://www.bbwinc.com/media/stories/blend-layer-create-blend-bar-arrives-at-bath-body-works) · [BBW 10-K FY2026](https://www.sec.gov/Archives/edgar/data/701985/000070198526000008/bbwi-20260131.htm)

---

### FC-11 · TikTok Shop — dodati Portugal
**Tvrdnja:** F5 1.9 i nalaz 3 — *„aktivan u deset evropskih zemalja… poslednje proširenje
15.06.2026"*.
**Šta je stvarno:** posle 15.06.2026 (AT, BE, NL, PL) dodat je i **Portugal, 22.06.2026** —
dakle **jedanaest** tržišta. Češka, Grčka i Mađarska su u dokumentaciji, još nisu live.
**Suština tvrdnje stoji u celini: Srbija nije ni aktivna ni najavljena** ✅.
**Kako da glasi:** *„…aktivan u **jedanaest** evropskih zemalja (Austrija, Belgija, Francuska,
Nemačka, Irska, Italija, Holandija, Poljska, Portugal, Španija, UK); Češka, Grčka i Mađarska
su u dokumentaciji. **Srbija nije ni među aktivnim ni među najavljenim tržištima**
(provereno 08.09.2026)."*

---

### FC-12 · Hurlbert & Ling — podatak tačan, ali nosi više težine nego što može
**Tvrdnja:** F5 sekcija 5.3, oznaka **VISOKA** — i na njoj stoji **cela odluka o boji brenda**.
**Provereno:** studija postoji, *Current Biology* 2007, **n = 208** (britanski i kineski
uzorak, uzrast 20–26) ✅. Nalaz o plavoj bazi i ženskom pomaku ka crveno-roze ✅.

**Ograda koju dokument ne navodi.** To je jedna od najosporavanijih studija u psihologiji boje;
kasnija literatura razliku nalazi manjom i kulturno posredovanom, a evolucionu interpretaciju
autora je struka uglavnom odbacila. Uzorak je 20–26 godina — **nije ciljna grupa KLAUDS-a.**

**Šta menjati.** Boju **ne menjati** — ona ne stoji na toj studiji nego na **auditu
konkurencije, koji je stvarno izmeren** (dm #002878, DURŌ #00A9E0, Jasmin #ED1C24, Notino
#DE2670, ALMARA #E7B447 — ljubičasto-indigo polje je slobodno). To je jak, domaći, proverljiv
argument. Studiju spustiti na **SREDNJA** i preformulisati:
*„Uz to postoji i psihološka indikacija u istom smeru (Hurlbert & Ling, *Current Biology*,
2007, n=208, uzrast 20–26): plava baza je preferencija oba pola, uz ženski pomak ka
crveno-roze. **Nalaz je osporavan i uzorak nije tinejdžerski — koristi se kao potvrda smera,
ne kao osnova odluke. Osnova odluke je audit zauzetih boja.**"*

---

## 1.3 ✅ POTVRĐENO — može ići klijentu bez izmene

| # | Tvrdnja | Status | Kako je provereno |
|---|---|---|---|
| FC-13 | **Zakon o oglašavanju:** čl. 21 st. 6–7 (dete <12, maloletnik 12–18), čl. 21 st. 1 tač. 2, čl. 23 st. 6 (doslovno „samo", „sitnica", „povoljno"), čl. 25 st. 3 (društvene prednosti nad maloletnicima), čl. 10 tač. 4, **kazne 300.000–2.000.000 RSD** | ✅ **POTVRĐENO doslovno, svih pet odredaba** | [Paragraf Lex — Zakon o oglašavanju](https://www.paragraf.rs/propisi/zakon_o_oglasavanju.html) |
| FC-14 | **DP Lux Group poseduje Almaru.** Belodore 17 objekata / 7 zemalja / 70+ brendova; Plaza 4 objekta (BiH); **Almara osnovana 2022** | ✅ **POTVRĐENO** — uz jednu dopunu: grupa navodi **8 Almara objekata** (Srbija + BiH + S. Makedonija), od kojih je **6 u Srbiji** | [dpluxgroup.com](https://dpluxgroup.com/our-retail-chains/) |
| FC-15 | **Almara ima objekat u TC Galerija** | ✅ **POTVRĐENO.** Svih 6 srpskih lokacija: BEO Shopping Centar, **TC Galerija**, Delta City, Ušće, Delta Planet Niš, BIG Fashion NS | [almara.rs](https://almara.rs/) |
| FC-16 | **TC Galerija: najveći trambolin park u ovom delu Evrope; Cineplexx sa 9 sala i IMAX-om** | ✅ **POTVRĐENO** (COSMO JUMP, 800 m²; 9 sala, 1.700+ sedišta, jedina IMAX sala u Srbiji, ekran 336 m²) | [Belgrade Waterfront](https://www.belgradewaterfront.com/en/cineplexx-brings-imax-technology-to-galerija-belgrade/) |
| FC-17 | **Pantone Color of the Year 2026 = „Cloud Dancer" (PANTONE 11-4201), prvi put belo**; HEX #F0EEE9 | ✅ **POTVRĐENO** | [pantone.com](https://www.pantone.com/color-of-the-year/2026) |
| FC-18 | **Kontrastni odnosi palete** | ✅ **NEZAVISNO PRERAČUNATO — sva tri tačna:** Violet #5B3DF5 na Cloud #F0EEE9 = **5,28:1** (deklarisano 5,3; AA ✓) · Pulse #00E5A0 na Ink #14121C = **11,34:1** (11,3; AAA ✓) · Ink na Cloud = **16,2:1** (>15; AAA ✓) | WCAG 2.1 relativna luminancija, izračunato 08.09.2026 |
| FC-19 | **Gold Apple „mini" format 600 m²**, prvi objekat 2026. u Stavropolju, pet AppleBox objekata prelazi pod taj znak | ✅ **POTVRĐENO** — argument „najmanji format uzora je 4× veći od KLAUDS-a" stoji | [new-retail.ru](https://new-retail.ru/novosti/retail/applebox_smenit_vyvesku_zolotoe_yabloko_anonsirovalo_format_mini/) |
| FC-20 | **Piper Sandler april 2025:** momci 88 → **127 USD** na miris (**+44%**), devojke 87 → **107 USD** (+23%); **e.l.f. #1 šminka, 35%**; BBW #1 mirisni brend; BBW #3 trgovac 7% | ✅ **POTVRĐENO** (napomena: doc navodi +22% za devojke — tačno je +23%, zaokruženje) | [WWD — Piper Sandler](https://wwd.com/beauty-industry-news/teen-beauty-sephora-fragrance-skin-care-makeup-hair-1237083704/) |
| FC-21 | **Srednje obrazovanje 2025/2026:** 225.639 učenika u **491 redovnoj školi** + 1.553 u specijalnim = 227.192; regioni **59.682 / 58.905 / 63.547 / 43.505** | ✅ **POTVRĐENO do poslednje cifre.** Time preživljava i izračun „**Beogradski region = 26,5%**, 73,5% ciljne grupe van njega" | [RZS — Srednje obrazovanje 2025/2026](https://publikacije.stat.gov.rs/G2026/htmlL/G20261031.html) |
| FC-22 | **Prosečna neto zarada jun 2026: 120.401 RSD; medijalna 94.281 RSD** | ✅ **POTVRĐENO** (napomena: rast +11,5% nom. / +8,4% realno odnosi se na kumulativ jan–jun; doc navodi +12,4/+9,4 za jun pojedinačno — proveriti pre citiranja ili izostaviti) | [Forbes Srbija / RZS](https://forbes.n1info.rs/vesti/statistika-prosecna-neto-zarada-u-srbiji-u-junu-bila-120-401-dinar-medijalna-94-281/) |
| FC-23 | **notino.rs i dalje ne postoji** | ✅ **POTVRĐENO 08.09.2026** (DNS: `ENOTFOUND`). Rizik ostaje budući, ne sadašnji | direktna provera |
| FC-24 | **Jasmin TikTok ~196K** | ✅ **POTVRĐENO** | [TikTok @jasmin.parfimerije](https://www.tiktok.com/@jasmin.parfimerije) |
| FC-25 | **NORMAL: 1.095 objekata u 14 zemalja, dve trećine ispod 2 €** | ✅ **POTVRĐENO** (za razliku od podatka o ekspanziji — v. FC-02) | [Wikipedia — Normal Stores](https://en.wikipedia.org/wiki/Normal_Stores) |

---

## 1.4 ⬜ NE MOŽE SE PROVERITI — šta uraditi sa svakim

| Tvrdnja | Zašto se ne može proveriti | **Odluka** |
|---|---|---|
| **Euromonitor udeli proizvođača** (Puig 18%, Sarantis 14%, Coty 8%, L'Oréal 6%, Avon 5%) | Izveštaj je iza plaćenog zida; javno je vidljiv samo sažetak | **Zadržati**, uz jasnu atribuciju („Euromonitor, jul 2026") i **ne graditi nijednu preporuku na tim udelima** — trenutno se i ne gradi, samo se koriste kao potvrda smera. OK |
| **Tržište 71.774 mil. RSD, +6% god/god** | Isto | **Zadržati** — tri nezavisna izvora u istom rangu (Euromonitor, Weitnauer, Statista) opravdavaju VISOKA |
| **„100.000 prodatih JK 'JA' mist-ova"** | Samodeklarisano na nalogu vlasnice brenda | **Već ispravno označeno SREDNJA/NISKA.** Zadržati formulaciju „red veličine, ne podatak"; **ne stavljati u prezentaciju kao brojku** |
| **Prihod Gold Applea** (48 mlrd RUB vs 1,7 mlrd USD) | Dve nesaglasne javne cifre | **Već ispravno rešeno** — ne citirati nijednu. Zadržati |
| **Brojevi pratilaca influensera** (osim Jasmina) | IG/TikTok blokiraju čitanje; agregatori su sekundarni | **Već označeno NISKA–SREDNJA** ✅. Ali v. **POK-04** — isporuka je zbog toga tanka |
| **Cene na lilly.rs** | HTTP 403 (Cloudflare) — potvrđeno i u ovoj fazi, svi pokušaji odbijeni | Ostaje otvoreno. **Ručna provera 15 SKU u objektu** — nije urađeno |
| **„Sekcija Teens" kod Gold Applea** | Stranica traži JavaScript | **Već označeno SREDNJA** ✅ |
| **Odsustvo Gen Z beauty koncepta u regionu** | Odsustvo rezultata nije dokaz | **Već ispravno ograđeno** ✅ |
| **Nedostupnost brendova iz grupe 5b/B** | Isto | **Već ispravno ograđeno SREDNJA** ✅. Delimično **ojačano** ovom fazom: potvrđeno je da ih nema u Sephora RS katalogu (FC-07) |

---

# 2. KONZISTENTNOST — gde se faze međusobno protivreče

## KON-01 · ⚠️ NAJOZBILJNIJE — tabela persona ne može da proizvede deklarisani AOV
**Gde:** F7 tačka 1 (persone) vs. F7 tačka 8 (cenovno pozicioniranje) vs. F7 metrika 5.

F7 tvrdi **AOV 45–60 €** na tri mesta. Ali sopstvena tabela persona daje:

| Persona | Udeo prometa | Korpa | Sredina korpe |
|---|---:|---|---:|
| A „Maja" | 35% | 15–30 € | 22,5 € |
| B „Nikola" | 25% | 30–50 € | 40 € |
| C „Teodora/Luka" | 20% | 35–60 € | 47,5 € |
| D „Snežana" | 20% | 40–70 € | 55 € |

Broj transakcija po personi je proporcionalan **udelu podeljenom korpom**:
35/22,5 = 1,56 · 25/40 = 0,63 · 20/47,5 = 0,42 · 20/55 = 0,36 → **ukupno 2,97**.
**Implicirani AOV = 100 / 2,97 = 33,7 €.** To je **26% ispod donje granice deklarisanog cilja.**

Uzrok je persona A: nosi **najveći udeo prometa (35%) sa najmanjom korpom (15–30 €)**. Ta
kombinacija matematički vuče prosek nadole i ne može koegzistirati sa AOV-om od 45–60 €.

**Tri moguća ispravka — bira se jedan:**
1. **Podići korpu persone A na 25–40 €** (opravdano: layering sto i mist+mini kombinacija su
   projektovani upravo da tu korpu podignu; 15–30 € je opis *današnjeg* ponašanja kod dm-a, ne
   ciljanog kod KLAUDS-a). → implicirani AOV ≈ 40 €.
2. **Spustiti udeo persone A na ~25% i podići D na ~30%.** → implicirani AOV ≈ 40 €.
3. **Preformulisati cilj:** *„AOV 45–60 € je cilj za drugu godinu; realan startni AOV pri
   ovoj strukturi persona je 34–40 €."*

**Preporuka recenzije: kombinacija 1 i 3.** Podići korpu A na 25–40 € (jer je to ono što
mehanike iz Faze 4 treba da urade) i **eksplicitno napisati da je 45–60 € cilj, a ne startna
vrednost.** Bez toga izveštaj sam sebi protivreči na najvidljivijem broju.

> Isti problem u manjem obliku: F2A i F4 računaju **1,7 artikla po korpi**; F7 postavlja cilj
> **≥ 2,0**. Uz artikal od 25–35 €, 2,0 artikla daje korpu **50–70 €**, ne 45–60 €.
> **Uskladiti: ili artikal 22–30 €, ili korpa 50–70 €, ili cilj 1,8.**

---

## KON-02 · ⚠️ Almara je i dalje konkurent u celoj Fazi 2A
**Gde:** F2A sekcija 0 (nalaz 2), tabela 1.2, tabela beauty zakupaca u sekciji 3,
interpretacija u sekciji 3, sekcija 7.1 (stavka 7), REZIME nalaz 4, i **zaključak 3**.

F2B nalaz 0 je to oborio pre deset dana; STATUS.md to vodi kao poznato od 28.08. **Nijedno
mesto u F2A nije ispravljeno.** Posledica: dokument koji ide u appendix finalnog izveštaja
tvrdi da klijent ima konkurenta koji je zapravo njegov sopstveni lanac — i to na pet mesta.

**Šta konkretno ispraviti u F2A:**
- Sekcija 0, nalaz 2: *„pet parfimerija na istom nivou: Sephora, Jasmin, Belodore, DURŌ i
  ALMARA"* → *„**tri nezavisne parfimerije** (Sephora, Jasmin, DURŌ) plus **dva objekta same
  DP Lux grupe** — Belodore (360 m²) i ALMARA."*
- Tabela 1.2, red ALMARA: dodati kolonu/napomenu **„klijentov sopstveni lanac (DP Lux)"**.
- Tabela beauty zakupaca (sekcija 3): isto označiti i za Belodore i za ALMARA.
- Sekcija 7.1, stavka 7: *„Belodore / DURŌ / ALMARA — ne konkurišu…"* → razdvojiti:
  DURŌ je konkurent, Belodore i ALMARA su **interna kanibalizacija**, što je drugačiji problem.
- REZIME nalaz 4 i zaključak 3: ista ispravka.
- Sekcija 3, „Interni rizik": proširiti sa Belodore ↔ KLAUDS na **Belodore ↔ ALMARA ↔ KLAUDS —
  tri sopstvena objekta u istoj zgradi.**

---

## KON-03 · Broj brendova Sephore: 55 vs. 67 (stvarno 66)
F2A i F7 nose 55, F2B nosi 67. **Uskladiti na 66** (v. FC-07). F7 tačka 8 („55+ brendova") je
argument u finalnoj preporuci o cenovnom pozicioniranju i mora biti tačan.

---

## KON-04 · Cena Sabrina Carpenter: 23,0 € (F2A) vs. 34,1 € (F2B, F3, F7)
V. FC-06. Obe cene postoje; dokumenti biraju različite i **grade na njima suprotne zaključke**
(F2A je svrstava u „mass parfem 15,3–25,6 €", F7 u „gotovo tačno ciljani artikal"). Uskladiti.

---

## KON-05 · Potrošnja momaka na miris: dva različita para brojeva u istom dokumentu
- **F3, sekcija 1.3:** *„sa 75 USD (2023) na 110 USD (2024)"* (izvor: Wikipedia/smellmaxxing)
- **F3, sekcija 3.2 i F2B 2.7C:** *„127 USD (sa 88 USD)"* (izvor: Piper Sandler/WWD)

Oba mogu biti tačna — različiti talasi i verovatno različita definicija metrike — ali stoje
u istom dokumentu bez ijedne reči objašnjenja. Čitalac vidi kontradikciju.
**Ispravka:** zadržati **samo Piper Sandler par (88 → 127 USD, +44%)**, jer je nezavisno
potvrđen i jer se iz njega izvodi „+44%" koji se koristi kroz ceo izveštaj. Wikipedia par
izbaciti ili staviti u fusnotu sa naznakom da je iz drugog talasa.

---

## KON-06 · Finansijski rez 15–16 / 17–19 protivreči sopstvenom nalazu
V. FC-04. F2B protivreči sam sebi na razmaku od tri reda; F3 i F7 preuzimaju pogrešnu verziju.

---

## KON-07 · Broj brendova po grupama: 10/8/8 vs. 10/9/7
F2B i STATUS.md: *„26 brendova (10 dostupnih / 8 ekskluziva / 8 beauty)"*.
F7 rezime 14: *„26 brendova u tri grupe (10 dostupnih / **9** ekskluziva / **7** beauty)"*.

Uzrok: F7 je **e.l.f. premestio iz beauty grupe u ekskluzive** (opravdano — e.l.f. jeste
ekskluziva), ali **numeracija brendova se time pomerila** i isti brend nosi različit redni broj
u dva dokumenta. **Ispravka:** uskladiti F2B sekciju 5 sa F7 tačkom 10 (10/9/7), ili u F7
dodati napomenu o premeštanju. Inače će se u finalnom izveštaju pojaviti dve liste od 26
brendova sa različitim brojevima.

---

## KON-08 · Broj otvorenih pitanja: 28 vs. 34, sa dupliranim brojem
F7 tvrdi **„28 otvorenih pitanja iz faza 2A–6"** na tri mesta (sekcija 0, tačka 11, zaključak).
STATUS.md ih numeriše do **34**. Uz to, **broj 28 je upotrebljen dvaput**: F5 pitanje 28
(„Prati li se NORMAL") i F6 pitanje 28 („Ti/Vi pravilo").

**Ispravka:** prenumerisati sva pitanja u **jedinstven niz 1–34**, ispraviti F7 na 34, i
proveriti da li se broj promenio u referencama tipa „[ČEKA ODGOVOR — pitanje 17/18/23/24]".

---

## KON-09 · Sephora loyalty: „45 mil. globalno" vs. „45 mil. u S. Americi"
F5 sekcija 3.4 kaže *„45 mil. članova loyaltyja globalno"*; F5 sekcija 6.2 kaže *„45 mil.
članova u S. Americi"*. Isti broj, dva različita obuhvata, u istom dokumentu.
**Ispravka:** uskladiti na **Severna Amerika** (to je obuhvat koji Sephora zvanično objavljuje)
ili izbaciti broj — on ni u jednom mestu ne nosi preporuku.

---

## KON-10 · „Golden Apple" vs. „Gold Apple"
Brief i F7 koriste **„Golden Apple"**; firma se zove **Gold Apple (Золотое Яблоко)**. Oba oblika
se u dokumentima smenjuju, ponekad u istom pasusu (F5, sekcija 2).
**Ispravka:** standardizovati na **Gold Apple**, uz jednu fusnotu: *„klijent ga u brifu naziva
Golden Apple; zvaničan naziv je Gold Apple (Золотое Яблоко)."*

---

## KON-11 · Metodološki prekid u tabeli cena (F2A, 4.2, red 20)
Tabela 4.2 nosi napomenu *„Pouzdanost: VISOKA za redove 18–22 i 24–28 (isti prodavac, isti SKU,
isti API, isti dan)"*. **Ali red 20 (Lattafa Asad) nema dm Srbija cenu** — u koloni stoji „—" —
pa je razlika od **+71%** izračunata poređenjem **Mirris.rs (RS)** sa **dm Hrvatska**.
To nije poređenje istog prodavca, i **ne sme nositi VISOKA**, niti ulaziti u zaključak
*„tipičan raspon +18% do +32%, sa ekstremima do +92%"*.

**Prekontrolisano — svi ostali redovi su tačni:** 18 (+18%), 19 (+21%), 21 (+32%), 22 (+31%),
23 (+28%, već označen SREDNJA ✓), 25 (+0,4%), 26 (+66%), 27 (+92%), 28 (−14%). ✅
**Ispravka:** red 20 označiti **SREDNJA** i dodati napomenu *„poređenje različitih prodavaca —
ne ulazi u raspon"*. Raspon ostaje **+18% do +32%, ekstrem +92%** — nepromenjen.

---

## KON-12 · Sinteza tvrdi nešto što istraživačke faze ne podržavaju — jedan slučaj
**F7 tačka 8** koristi *„globalne ekskluzive (Rhode, Sol de Janeiro, Fenty)"* kao dokaz da se
Sephora ne može stići. **Rhode nije u Sephora RS katalogu** (v. FC-07). Ako je Rhode u Srbiji
samo najavljen, argument slabi — i to je **u korist KLAUDS-a**, ne protiv njega.
**Ispravka:** *„globalne ekskluzive (Sol de Janeiro, Fenty, Huda; Rhode je najavljen, ali
nije potvrđen u zvaničnom katalogu na dan 08.09.2026)."*

> **Ostalo je provereno i sinteza ne izmišlja.** Svaka tvrdnja u F7 koja nosi oznaku tipa
> *(F3, nalaz 2)* proverena je nasumičnim uzorkom od 15 referenci — **sve odgovaraju izvornom
> nalazu, i nijedna nije pojačana u prenosu.** To je metodološki najjači deo projekta.

---

# 3. POKRIVENOST — provera prema `03-isporuke/checklist-isporuka.md`

## Sekcija A i B — svih 15 stavki postoji

| # | Isporuka | Postoji | Konkretno? | Ocena |
|---|---|---|---|---|
| 1 | Postavka vizuelnog identiteta | ✅ F7 t.9 + zaseban fajl | **Vrlo konkretno** — HEX vrednosti, izmerene boje konkurencije, kontrast **nezavisno reprodukovan** | 🟢 najjača isporuka |
| 2 | Pozicioniranje na tržištu | ✅ F7 t.0 i t.8 | Konkretno, sa brojevima i sa razlogom zašto ne druge dve opcije | 🟢 |
| 3 | Do/don't principi | ✅ F7 t.7 | 4 bloka, svaki red sa razlogom i vezom za nalaz | 🟢 |
| 4 | **Top 10 influensera** | ⚠️ F7 t.3 | **To su 10 TIPOVA, ne 10 imena.** Tip 8 nema nijedno ime. Tip 2, 3, 4 imaju ekosistem, ne ime. Nijedno ime nije verifikovano. Jedan izvor je **mrtav link** | 🔴 **NAJTANJA — v. POK-04** |
| 5 | Top 10 aktivacija | ✅ F7 t.4 | Sa složenošću, budžetskom oznakom i benchmark vezom | 🟢 |
| 6 | Launch smernice | ✅ F7 t.5 | Osa T−20 do +90, 11 metrika, kontrolna lista bez izuzetaka | 🟢 |
| 7 | 3–4 persone | ✅ F7 t.1 (četiri) | Bogato, ali **brojke interno protivrečne** (KON-01) i **finansijski rez pogrešan** (FC-04) | 🟡 |
| 8 | Content pillars | ✅ F7 t.2 (pet) | Sa formatima po kanalu i udelima u kalendaru | 🟢 |
| 9 | Journey + top 5 interaktivnih | ✅ F7 t.6 | 10 koraka, 5 elemenata, redosled odustajanja ako nema budžeta | 🟢 |
| 10 | Cenovno pozicioniranje | ✅ F7 t.8 | Konkretno, ali **stoji na precenjenoj populaciji** (FC-01) i **protivreči tabeli persona** (KON-01) | 🟡 |
| 11 | Predlog brendova | ✅ F7 t.10 (26) | Konkretno, sa cenom, ulogom i oznakom preklapanja. **Numeracija se razlikuje od F2B** (KON-07); nijedan brend iz grupe B nije kontaktiran | 🟡 |
| 12 | THE KLAUDS MOMENT | ✅ F4 s.8 + F7 t.6 | Tri predloga sa prostorom, složenošću i načinom merenja; uz **šest kriterijuma kroz koje su prošli** | 🟢 |
| 13 | 3–5 reči brenda | ✅ F5 s.4 + F6 s.3.2 | Pet reči, svaka testirana na autocomplete-u i vezana za element u radnji | 🟢 |
| 14 | Boja / paleta | ✅ F5 s.5 | **Izmereno, ne procenjeno.** Jedina isporuka koju je ova faza uspela da reprodukuje do decimale | 🟢 |
| 15 | Motiv za loyalty van popusta | ✅ F5 s.6 + F7 t.4/10 | Sedam motiva sa primerima; mehanika sa dva brojača | 🟢 |

**Zaključak pokrivenosti: 12 od 15 zeleno, 3 žuto, 1 crveno (stavka 4).**

---

### POK-01 · Rupe koje su bile planirane za zatvaranje **pre** Faze 8 — nijedna nije zatvorena

STATUS.md navodi pet obaveznih stavki pre Faze 8. **Stanje na dan 08.09.2026:**

| Stavka | Rok | Status |
|---|---|---|
| Mišljenje advokata (čl. 25 st. 3, čl. 23 st. 6, žig „PROBAJ") | pre Faze 8 | ❌ **nije urađeno** |
| Ručno prikupljanje korpusa srpskih TikTok komentara (~4 h) | otvoreno od Faze 3 | ❌ **nije urađeno** |
| Ručno očitavanje boja Lilly i Belodore (~30 min) | pre dizajn brifa | ❌ **nije urađeno** |
| Domaća bazna linija za UGC (~2 h) | pre Faze 7 | ❌ **nije urađeno** |
| Ispravka Faze 2A (Almara) | pre Faze 8 | ❌ **nije urađeno** (v. KON-02) |

**Od pet, tri se mogu zatvoriti za ukupno ~7 sati rada** (korpus, boje, UGC bazna linija).
**Dve zavise od drugih:** advokat (klijent) i ispravka F2A (ide u ovoj fazi).

> **Ako se ne zatvore, u finalni izveštaj ulaze ovako:** persone i content pillars stoje na
> **izmerenoj pretrazi, ne na izgovorenom jeziku** (to je već pošteno napisano u F7 tačka 11);
> dizajn brief ide bez dve od jedanaest izmerenih boja; a pravni deo ide sa eksplicitnom
> ogradom da nije pravno mišljenje. **To je prihvatljivo — ali mora biti napisano u
> zaključku, a ne samo u ograničenjima.**

---

### POK-02 · Odgovori klijenta — usko grlo se nije pomerilo
`05-klijent/odgovori-klijenta.md` je **i dalje prazan**, jedanaest dana posle Faze 7.
**34 pitanja** čekaju, od kojih **osam direktno menja sadržaj isporuka**. Rok je za tri dana.

**Preporuka recenzije:** pitanja poslati **danas**, kao jedan paket od tri strane, sa
**osam prioritetnih izdvojenih na vrh** i sa oznakom šta se u izveštaju menja u zavisnosti od
odgovora. Faza 1 nikad nije urađena i to je jedini formalni kanal kojim je taj paket trebalo
da ode — **ne čekati Fazu 1, poslati direktno.**

---

### POK-03 · Sekcija C checkliste — dve stavke se trenutno ne mogu čekirati
- ❌ *„Svi linkovi u appendixu izvora rade"* — **6 mrtvih linkova od 322** (v. sekciju 5).
- ❌ *„Nivoi pouzdanosti dosledno označeni"* — **četiri nedoslednosti** (v. sekciju 4).
- ⚠️ *„Nijedna preporuka ne stoji na izmišljenom podatku"* — nijedan podatak nije izmišljen,
  ali **jedan je pogrešno pročitan** (FC-01) i **jedna interpretacija je konstruisana bez
  izvora** (330.698 kao „urbani deo").

---

### POK-04 · Stavka 4 (Top 10 influensera) je jedina koja ne ispunjava ono što je klijent tražio
Klijent je u Q48 tražio **„Top 10 influensera"**. Isporučeno je **deset tipova kreatora** —
što je metodološki pametnije i dugoročno korisnije, ali **nije ono što je traženo**, i to
treba reći otvoreno umesto da se prećuti.

**Stanje po tipu:**

| Tip | Ima ime? | Verifikovano? |
|---|---|---|
| 1 Regionalni autoritet | ✅ Čovek Parfem, Parfemičar | ❌ (uz to: kod Parfemičara je označen mogući sukob interesa ✅ dobro) |
| 2 Mikro „moja kolekcija" | ⚠️ dva imena, oba **iznad** navedenog raspona | ❌ |
| 3 Muški recenzent | ❌ nema ime, samo „ekosistem" | — |
| 4 „Kopija" recenzent | ⚠️ navedeni su **brendovi**, ne kreatori (i to je pošteno označeno ✅) | ❌ |
| 5 Beauty/skincare | ✅ tri imena | ❌ |
| 6 Tinejdžerski lifestyle | ✅ tri imena | ❌ |
| 7 Muzički/pop | ✅ dva imena | ❌ |
| 8 Mama/roditelj | ❌ **nijedno ime** | — |
| 9 Nano iz radnje | n/p (mehanika, ne zakup) ✅ | — |
| 10 Regionalni van Srbije | ❌ nije mapirano | — |

**Uz to: izvor [BURO247 — beauty influenserke na YouTubeu] je mrtav (404).**

**Preporuka:** ne prepravljati logiku — ona je dobra. Uraditi **~3 sata ručnog rada** i dodati
**po dva do tri konkretna imena za tipove 3, 8 i 10**, sa brojem pratilaca očitanim ručno i
datumom očitavanja. Time isporuka postaje ono što je traženo, a ograda o neverifikovanosti
ostaje.

---

# 4. POUZDANOST — doslednost oznaka

## 4.1 Nedosledno označeno (četiri slučaja)

| # | Gde | Nosi | Treba | Zašto |
|---|---|---|---|---|
| **POU-01** | F4 3.1 i rezime 6 — zrna kafe | **VISOKA** | **SREDNJA** | Obrazloženje glasi *„više nezavisnih sekundarnih izvora koji je citiraju"* — sekundarni izvori koji citiraju **istu** studiju nisu nezavisna potvrda. Jedna exploratory studija, n=63 (v. FC-05) |
| **POU-02** | F5 5.3 — pol i boja | **VISOKA** | **SREDNJA** | Osporavana studija, uzrast uzorka 20–26 (nije ciljna grupa). Odluka o boji treba da stoji na **auditu konkurencije**, koji je stvarno izmeren (v. FC-12) |
| **POU-03** | F3 1.1 — *„parfem ~10× traženiji od šminke"* | **VISOKA** | **VISOKA za smer, SREDNJA za faktor** | Isti dokument izričito ograđuje da su Trends brojevi *„relativni indeksi unutar jedne grupe poređenja"*. Odnos 45–81 : 3–7 dokazuje **dominaciju**; ne dokazuje precizno „10×" |
| **POU-04** | F2A tabela 4.2, red 20 | **VISOKA** | **SREDNJA** | Poređenje različitih prodavaca pod oznakom „isti prodavac, isti API" (v. KON-11) |

## 4.2 Preporuke koje stoje na niskoj pouzdanosti, a to nije rečeno **na mestu preporuke**

Ovo je najčešći tip propusta u projektu. Ograde postoje — ali u sekciji „Ograničenja", dok
tabela koju će klijent zapravo čitati nosi go broj.

| # | Preporuka | Gde nosi go broj | Gde je ograda | Ispravka |
|---|---|---|---|---|
| **POU-05** | **„Mist & layering zid: 18% prometa, 20% prostora"** | F2B s.6 tabela · **F7 tačka 8 i tačka 10** | F3 nalaz 14 (body mist ima ~4% volumena pretrage; postoji upit „mist za telo šta je") | **Dodati oznaku u samu tabelu:** *„(NISKA — predlog, ne merenje; kategorija visokog potencijala i niske svesnosti — v. F3 nalaz 14)"*. Uz FC-06, ovo postaje još važnije: dm već drži mist po 10,6–12,8 € |
| **POU-06** | **Udeli persona 35/25/20/20** | F7 dijagram grananja (t.6), tabela zona, journey | F7 t.1 (uvodna ograda) i t.11 | Ograda mora da se **ponovi u tački 6**, jer se tamo brojevi koriste kao da su podatak |
| **POU-07** | **Podela nabavnog budžeta 15% / 55% / 30%** | F3 s.7.2 · F7 t.7 (DO tabela) | nema oznake nigde | **Dodati SREDNJA** — izvedeno iz oblika Trends krivih, što je dobar metod, ali nije merenje prodaje |
| **POU-08** | **Struktura police, šest blokova sa udelima prometa** | **F7 tačka 10 — tabela bez ijedne oznake** | F2B s.6 („SREDNJA — konstrukcija iz potvrđenih cena, bez lokalnih podataka o strukturi korpe") | **Preneti oznaku SREDNJA u F7 tabelu.** To je tabela koju će klijent najviše gledati |
| **POU-09** | **Frekvencija kupovine 6–10× godišnje** | F7 t.8, tabela „Za cene" — stoji uz izmerene cene, kao da je iste vrste | F2A s.6.1, gde je bila procena u tabeli poređenja opcija | **Dodati NISKA** ili izbaciti iz tabele — trenutno deluje kao izmeren podatak jer stoji između dva izmerena |
| **POU-10** | **Cilj „broj artikala po korpi ≥ 2,0"** | F7 metrika 4, i „prava operativna metrika" u rezimeu | nema | Sam **izbor metrike je odličan i dobro obrazložen**; ali **konkretna vrednost 2,0 nije izvedena ni iz čega** — F2A i F4 računaju 1,7. **Dodati NISKA** i obrazložiti odakle 2,0, ili spustiti na 1,8 |

## 4.3 Šta je označeno **ispravno** — i to treba reći

Projekat ima neuobičajeno dobru disciplinu oznaka. Ispravno i eksplicitno je označeno:
- Sve vendorske brojke (dwell time, +18% korpe, +30% konverzije, QR scan rate) — **SREDNJA/NISKA**
  uz imenovanje komercijalnog interesa izvora ✅
- Sve loyalty brojke (Antavo, Attentive, Talon.One) — **SREDNJA**, uz napomenu da su izvori
  dobavljači ✅
- Odsustvo rezultata pretrage kao ne-dokaz — **dosledno kroz sve faze** ✅ (grupa 5b, regionalni
  koncepti, korejske kabine)
- Prenosivost SAD/UK/KOR podataka na Srbiju — **eksplicitno ograđeno u F4 i F5** ✅
- Cena discovery seta, podela tona 55/25/15/5, frekvencija CRM poruka — **NISKA/SREDNJA** ✅
- Podatak koji ne postoji (džeparac) — **napisano da ne postoji, sa predlogom kako proceniti** ✅
  i to **dvaput provereno** ✅
- Podatak koji je namerno odbačen (CKPS 2021, „204 € godišnje u Evropi") — **zapisano zašto je
  odbačen** ✅ — ovo je retkost i vredi je zadržati u finalnom izveštaju

---

# 5. PROVERA LINKOVA — 322 jedinstvena URL-a iz registra izvora

**Metod:** HTTP GET sa browser User-Agent-om, praćenje redirekcija, timeout 20 s, 08.09.2026.

| Status | Broj | Značenje |
|---|---:|---|
| **200 OK** | **259** | rade |
| 403 Forbidden | 43 | **anti-bot zaštita, ne mrtav link** — rade u browseru (lilly.rs, sciencedirect, forbes, BoF, businesswire, sec.gov, punmiris…) |
| 429 Too Many Requests | 8 | rate limit — **6 od 8 su Google Trends URL-ovi**, očekivano |
| **Mrtvi** | **6** | ⬇ |
| 405 / 400 | 2 | metod blokiran; verovatno rade u browseru (timeoutdubai, douglas.hr) |
| 453 | 1 | playboard.co blokira po regionu |

## 5.1 ❌ Šest linkova koji su stvarno mrtvi — moraju se zameniti

| # | Link | Status | Gde se koristi | Šta uraditi |
|---|---|---|---|---|
| 1 | `buro247.rs/lepota/lepota-insajder/upoznajte-nove-i-drugacije-beauty-influenserke-na-youtubeu/` | **404** | **F7 tačka 3 — imena influensera** | Najbolniji od šest: nosi isporuku br. 4. Zameniti ručnim istraživanjem (v. POK-04) |
| 2 | `nativemedia.rs/blog/viber-marketinga-kompletan-vodic/` | **404** | F6 s.5.0 — **Viber ~90% stopa otvaranja** | Ostaje samo jedan izvor (SpotLight). **Spustiti tvrdnju na SREDNJA** ili naći drugi izvor |
| 3 | `nbcnews.com/video/inside-the-social-media-trend-teens-call-smellmaxxing-267971141616` | **404** | F3 s.1.3 — smellmaxxing | Zameniti; tvrdnja je pokrivena i preko Wikipedije i The Robin Report-a, pa **nalaz ne pada** |
| 4 | `cosmeticsdesign-europe.com/…/plouise-hits-2m-sales-in-record-breaking-tiktok-shop-live/` | **410 Gone** | F5 s.1.9 — **P.Louise 2 mil. £ za 14 sati** | 410 znači trajno uklonjeno. Postoje dva rezervna izvora (Cosmetics Business, BeautyMatter) — **prebaciti citat na njih** |
| 5 | `cosmeticsdesign-asia.com/…/miniso-builds-ip-ecosystem…` | **410 Gone** | F5 s.1.4 — MINISO 80% prodaje iz IP saradnji | Isto; ostaju miniso.com izvori, ali oni su **sama kompanija** → **spustiti na SREDNJA** |
| 6 | `retaildive.com/news/bath-body-works-new-store-design-gingham/742380` | **520** (uporno, dva pokušaja) | F4 s.4.1b i 4.2 — **BBW Gingham+ format** | To je jedan od dva izvora za **nalaz 9 Faze 4** („širi prolazi, zone, otvoreno probanje — nijedna nije digitalna"), koji je **najjači argument protiv budžeta za ekrane**. Drugi izvor (RetailWire) radi ✅ → nalaz stoji, ali **link zameniti** |

## 5.2 ⚠️ 43 linka sa 403 — šta uraditi u appendixu
To nisu mrtvi linkovi (blokada automatskog čitanja), **ali čitalac izveštaja koji klikne dobija
403 ako ga blokira isti zaštitni sloj.** Najosetljiviji su **8 linkova ka lilly.rs**, koji je
najveći igrač na tržištu.
**Preporuka:** u appendixu izvora dodati kolonu **„pristup"** sa vrednostima *otvoren /
zahteva browser / iza registracije*, i za lilly.rs staviti napomenu koja već postoji u F2A.

---

# 6. LISTA ISPRAVKI PO DOKUMENTU — poređano po važnosti

> Legenda hitnosti: 🔴 **blokira isporuku** · 🟠 **menja zaključak** · 🟡 **menja tačnost** ·
> 🔵 **kozmetika i doslednost**

## 6.1 `01-faze/klauds_faza2a_konkurencija.md`

| # | 🔴🟠🟡🔵 | Gde | Šta | Kako da glasi |
|---|---|---|---|---|
| 2A-1 | 🔴 | Sekcija 0 (nalaz 2), tabela 1.2, tabela beauty zakupaca (s.3), interpretacija s.3, s.7.1 st.7, REZIME nalaz 4, zaključak 3 | **Almara se tretira kao konkurent** | Svuda: **tri nezavisne parfimerije (Sephora, Jasmin, DURŌ) + dva sopstvena objekta DP Lux grupe (Belodore 360 m², ALMARA)**. „Interni rizik" proširiti na **tri sopstvena objekta u istoj zgradi** (v. KON-02) |
| 2A-2 | 🔴 | Registar izvora #29 (i svako mesto gde se broj pojavljuje) | **Populacija 15–19 = 497.864** | **330.698** (170.028 M / 160.670 Ž), procena RZS 2024. Brisati konstrukciju „od toga 330.698 u gradskim naseljima (66,4%)" — ne postoji u izvoru (v. FC-01) |
| 2A-3 | 🟠 | Sekcija 2.1, 6.2 | „**55 brendova**" kod Sephore | **66 brendova**, provereno 08.09.2026 |
| 2A-4 | 🟠 | Sekcija 2.1 | „Rhode je uveden u Sephora Srbija", VISOKA | **SREDNJA** + „najavljeno u medijima; nije potvrđeno u zvaničnom katalogu 08.09.2026" |
| 2A-5 | 🟡 | Tabela 4.2, red 20 (Lattafa Asad) | Razlika +71% označena VISOKA, a poredi Mirris.rs sa dm HR | Označiti **SREDNJA** + napomena „poređenje različitih prodavaca — ne ulazi u raspon". **Raspon +18% do +32% ostaje nepromenjen** ✅ |
| 2A-6 | 🟡 | Tabela 4.2, red 25 | Sabrina Carpenter 2.699 (23,0 €) — tačno, ali nepotpuno | Dodati: *„2.699 RSD za četiri od pet EdP varijanti; 3.999 RSD (34,1 €) samo za Lemon Pie"* (v. FC-06) |
| 2A-7 | 🟠 | Sekcija 7.1 (rangiranje konkurenata), tačka 1 (dm) | Ne pominje da dm drži **celebrity mist po 10,6–12,8 €** | Dodati u opis dm-a: *„…i **Sabrina Carpenter body mist 236 ml po 1.249–1.499 RSD (10,6–12,8 €)** — dakle tačno onaj 'drugi artikal u korpi' na kome KLAUDS gradi AOV"* |
| 2A-8 | 🔵 | Sekcija 5, tabela strukture asortimana | Procenti nose „NISKA za konkretne procente" ✅ | Ostaje ✅ — ovo je dobar primer, i istu disciplinu treba preneti u F7 (v. POU-08) |

## 6.2 `01-faze/klauds_faza2b_rang_liste_brendovi.md`

| # | | Gde | Šta | Kako da glasi |
|---|---|---|---|---|
| 2B-1 | 🔴 | Sekcija 4.2 + REZIME nalaz 10 | **Populacija 497.864** | **330.698** (v. FC-01). **Izračun „73,5% van Beogradskog regiona" ostaje ✅** — on je iz školske statistike, koja je potvrđena do poslednje cifre |
| 2B-2 | 🔴 | Sekcija 4.4, Nalaz B + interpretacija + REZIME nalaz 12 | Raiffeisen „besplatan za sve ispod 18"; rez 15–16 / 17–19 | Raiffeisen je **18+** (3.000 RSD je poklon novim 18-godišnjacima). Rez je **15 / 16–19**, jer je Erste **16+** (v. FC-03, FC-04) |
| 2B-3 | 🟠 | Sekcija 2.7A, tabela + REZIME nalaz 4 | Sabrina Carpenter „3.999 RSD / 34,1 €" pod kolonom **dm** | Ispraviti na **2.699 RSD (23,0 €) za četiri od pet varijanti; 3.999 (34,1 €) samo Lemon Pie**. Dodati red za **body mist 236 ml, 1.249–1.499 RSD** (v. FC-06) |
| 2B-4 | 🟠 | Sekcija 2.3 | „Sephora Srbija ima **67 brendova**" | **66** |
| 2B-5 | 🟠 | Sekcija 2.7B i 2.7C + REZIME nalaz 5 | BBW „**24% udela** kod tinejdžerki" | Izbaciti procenat. Ostaje: *„#1 mirisni brend kod američkih tinejdžera (Piper Sandler, april 2025); #3 beauty trgovac sa 7% udela"* (v. FC-09) |
| 2B-6 | 🟠 | Sekcija 2.7C | „Piper Sandler … **poslednji talas**" | Dodati: *„49. talas, april 2025. U 50. talasu (jesen 2025) tinejdžerska beauty potrošnja **pala je 2% god/god na 336 USD**, a BBW je izašao iz prve trojke trgovaca"* (v. FC-08) |
| 2B-7 | 🟡 | Sekcija 5 (grupe 5a/5b/5c) | Numeracija 10/8/8 vs. F7 10/9/7 | Uskladiti sa F7 (e.l.f. prelazi u ekskluzive) ili dodati napomenu (v. KON-07) |
| 2B-8 | 🔵 | Sekcija 0 (nalaz o DP Lux) | „Almara — 6 objekata u Srbiji" ✅ tačno | Dopuniti: *„6 u Srbiji; grupa navodi ukupno 8, sa BiH i Severnom Makedonijom. Osnovana 2022."* |

## 6.3 `01-faze/klauds_faza3_genz.md`

| # | | Gde | Šta | Kako da glasi |
|---|---|---|---|---|
| 3-1 | 🟠 | Sekcija 3.3 | Rez „15–16 vs. 17–19" | **15 vs. 16–19** (v. FC-04) |
| 3-2 | 🟠 | Sekcija 1.5 | „u dm-u po 3.999 RSD / 34,1 EUR za 30 ml" | Ispraviti (v. FC-06); i preformulisati zaključak — linija pokriva **donji deo** ciljane zone |
| 3-3 | 🟡 | Sekcija 1.3 vs. 3.2 | Dva različita para brojeva o potrošnji momaka (75→110 vs. 88→127) | Zadržati **samo Piper Sandler par (88 → 127 USD, +44%)** — nezavisno potvrđen; drugi u fusnotu ili izbaciti (v. KON-05) |
| 3-4 | 🟡 | Sekcija 1.1 + REZIME nalaz 1 | „~10× traženiji" — VISOKA | **VISOKA za smer, SREDNJA za faktor** (v. POU-03) |
| 3-5 | 🟡 | Sekcija 3.2, tabela | „devojke +22% god/god" | **+23%** (107/87). Sitno, ali proverljivo |
| 3-6 | 🟡 | Sekcija 7.2 + REZIME nalaz 7 | Podela budžeta 15/55/30 bez oznake | Dodati **SREDNJA** (v. POU-07) |
| 3-7 | 🔵 | Ograničenja, red o mrtvom NBC linku | | Zameniti izvor za smellmaxxing (v. 5.1, red 3) |
| 3-8 | 🔵 | Nasleđeni broj populacije | 497.864 | Uskladiti sa 2B-1 |

## 6.4 `01-faze/klauds_faza4_retail_iskustvo.md`

| # | | Gde | Šta | Kako da glasi |
|---|---|---|---|---|
| 4-1 | 🟠 | Sekcija 3.1 + REZIME nalaz 6 | Časopis **Chemosensory Perception**; „dokazano netačno"; VISOKA | ***Perceptual and Motor Skills*, 2011, 112(2), 536–538**, n=63, eksplorativna; **SREDNJA**; „**nije potvrđeno**" umesto „dokazano netačno"; dodati treću granu (limun 86%) (v. FC-05) |
| 4-2 | 🟡 | Sekcija 4.1b i 4.2 (izvor) | RetailDive Gingham+ link mrtav (520) | Zameniti; nalaz ostaje jer RetailWire izvor radi ✅ |
| 4-3 | 🟡 | Sekcija 4.1d + REZIME nalaz 10 | „sa pilota u 500 radnji na svih 1.900 do maja 2026", VISOKA | *„…u ceo lanac od **1.927 objekata** (10-K, 31.01.2026). Podatak o veličini pilota potiče iz jednog izvora."* **VISOKA za skalu, SREDNJA za istoriju** (v. FC-10) |
| 4-4 | 🟡 | Sekcija 4.1b + REZIME nalaz 9 | BBW „24%" | Izbaciti procenat (v. FC-09) |
| 4-5 | 🔵 | Sekcija 5.4 | Podaci o Galeriji (trambolin park, Cineplexx 9 sala) | ✅ **POTVRĐENO** — dodati u zagradi „COSMO JUMP, 800 m²; 9 sala, 1.700+ sedišta, jedina IMAX sala u Srbiji" |

## 6.5 `01-faze/klauds_faza5_benchmark.md`

| # | | Gde | Šta | Kako da glasi |
|---|---|---|---|---|
| 5-1 | 🔴 | Sekcija 1.11 + REZIME nalaz 17 + otvoreno pitanje 28 | **NORMAL ulazi u HR i SI 2026, u Rumuniju april 2026** | Puna zamena teksta iz **FC-02**. Dodati **Action** kao odvojen lanac koji jeste najavio HR i SI. Dodati da je format NORMAL-a u Rumuniji **275–380 m²** |
| 5-2 | 🟠 | Sekcija 5.3 | Hurlbert & Ling, **VISOKA**, nosi celu odluku o boji | **SREDNJA**, preformulisati kao potvrdu smera; **težinu preneti na audit zauzetih boja**, koji je izmeren (v. FC-12). **Boja se NE menja** |
| 5-3 | 🟡 | Sekcija 1.9 + REZIME nalaz 3 | TikTok Shop „deset zemalja" | **Jedanaest** — dodat Portugal 22.06.2026. Suština stoji ✅ (v. FC-11) |
| 5-4 | 🟡 | Sekcija 1.9 (izvor) | cosmeticsdesign-europe link **410 Gone** | Prebaciti citat na Cosmetics Business i BeautyMatter (oba rade) |
| 5-5 | 🟡 | Sekcija 1.4 (izvor) | cosmeticsdesign-asia link **410 Gone** | Ostaju samo izvori same kompanije → **spustiti „80% prodaje iz IP saradnji" na SREDNJA** |
| 5-6 | 🟡 | Sekcija 1.12 + REZIME nalaz 6 | BBW „24%" i „poslednji talas" | v. FC-08 i FC-09 |
| 5-7 | 🔵 | Sekcije 3.4 i 6.2 | Sephora „45 mil. globalno" vs. „45 mil. u S. Americi" | Uskladiti na **Severna Amerika** ili izbaciti broj (v. KON-09) |
| 5-8 | 🔵 | Sekcija 2 i zaglavlja | „Golden Apple" / „Gold Apple" | Standardizovati na **Gold Apple** + jedna fusnota (v. KON-10) |
| 5-9 | ✅ | Sekcija 5.4 — kontrastni odnosi | | **Nezavisno reprodukovano, sva tri tačna.** Ostaviti kako jeste i **istaći u finalnom izveštaju da su izračunati, ne procenjeni** |

## 6.6 `01-faze/klauds_faza6_ton.md`

| # | | Gde | Šta | Kako da glasi |
|---|---|---|---|---|
| 6-1 | ✅ | Sekcija 3.3 — cele četiri zakonske odredbe + kazne | | **POTVRĐENO doslovno.** Ne dirati. Ovo je najpouzdanija sekcija u celom projektu |
| 6-2 | 🟡 | Sekcija 5.0, red Viber | „~90% stopa otvaranja" — jedan od dva izvora je **404** | Ostaje jedan izvor (domaća agencija) → **spustiti na SREDNJA/NISKA** ili naći nezavisno merenje |
| 6-3 | 🔵 | Sekcija 3.3, uvod | „maloletnik = lice od 12 do 18 godina (čl. 21, st. 6–7)" | ✅ tačno; STATUS.md navodi samo „st. 7" — uskladiti STATUS |
| 6-4 | 🔵 | Ograničenja, rupa 1 | Korpus TikTok komentara | Nije zatvoren ni u ovoj fazi. **Zadržati kao eksplicitno ograničenje u finalnom izveštaju**, ne samo u ograničenjima faze (v. POK-01) |

## 6.7 `01-faze/klauds_faza7_sinteza.md` — najviše ispravki, jer sve nasleđuje

| # | | Gde | Šta | Kako da glasi |
|---|---|---|---|---|
| 7-1 | 🔴 | Tačka 1 (persone) vs. tačka 8 vs. metrika 5 | **Persone impliciraju AOV od ~34 €, a dokument tvrdi 45–60 €** | Podići korpu persone A na **25–40 €** *i* napisati da je **45–60 € cilj, ne startna vrednost** (v. KON-01). Ovo je najvidljiviji broj u izveštaju |
| 7-2 | 🔴 | Tačka 1, persona A („Ko plaća") | „Od 17. godine Erste i Raiffeisen daju besplatne kartice maloletnicima" | **Od 16. godine, i to samo Erste** (zahtev podnosi roditelj). Raiffeisen je 18+ (v. FC-03, FC-04) |
| 7-3 | 🟠 | Tačka 10, stavka 4 (Sabrina Carpenter) | „Idealno — 34,1 € je gotovo tačno ciljani artikal" | *„**23,0 €** za četiri od pet varijanti (3.999 RSD / 34,1 € samo Lemon Pie) — linija pokriva **donji deo** ciljane zone."* (v. FC-06) |
| 7-4 | 🟠 | Tačka 8, „Zašto ne slično Sephora" | „5+ objekata, **55+ brendova**, globalne ekskluzive (**Rhode**, Sol de Janeiro, Fenty)" | *„…**66 brendova**… globalne ekskluzive (Sol de Janeiro, Fenty, Huda; **Rhode je najavljen ali nije potvrđen u zvaničnom katalogu 08.09.2026**)."* (v. FC-07, KON-12) |
| 7-5 | 🟠 | Tačka 7 (D · DIGITAL) i tačka 8 | „NORMAL ulazi u region 2026" | Prepisati po **FC-02**; dodati **Action** u kvartalno praćenje |
| 7-6 | 🟠 | Tačka 8 („Za asortiman") i tačka 10 (tabela blokova) | „mist & layering zid (18% prometa, 20% prostora)" bez ijedne oznake | Dodati **(SREDNJA/NISKA — predlog, ne merenje)** + jednu rečenicu iz F3 nalaza 14 + **novi nalaz da dm već drži celebrity mist po 10,6–12,8 €** (v. POU-05, FC-06) |
| 7-7 | 🟠 | Tačka 10, cela tabela strukture police | Šest blokova sa udelima prometa — **bez oznake pouzdanosti** | Preneti **SREDNJA** iz F2B sekcije 6 (v. POU-08) |
| 7-8 | 🟡 | Tačka 8, tabela „Za cene" | „Frekvencija kupovine 6–10× godišnje" stoji među izmerenim brojevima | Dodati **NISKA** ili izbaciti iz tabele (v. POU-09) |
| 7-9 | 🟡 | Metrika 4 | „broj artikala po korpi **≥ 2,0**" | Izbor metrike je odličan ✅; **vrednost 2,0 nije izvedena** (F2A i F4 računaju 1,7). Dodati **NISKA** i obrazloženje, ili spustiti na **1,8** (v. POU-10) |
| 7-10 | 🟡 | Tačka 6, dijagram grananja i tabela zona | Udeli persona 35/25/20/20 korišćeni bez ograde | Ponoviti ogradu iz tačke 1 (v. POU-06) |
| 7-11 | 🟡 | Sekcija 0, tačka 11, zaključak | „**28** otvorenih pitanja" | **34** (v. KON-08); prenumerisati ceo niz i proveriti reference „[ČEKA ODGOVOR — pitanje N]" |
| 7-12 | 🟡 | Tačka 3, tip 8 i tipovi 3 i 10 | Nema nijedno konkretno ime; jedan izvor je **404** | ~3 h ručnog rada, dodati 2–3 imena po tipu (v. POK-04). **Uz to eksplicitno napisati da je isporučeno 10 tipova, ne 10 imena, i zašto** |
| 7-13 | 🟡 | Tačka 10, numeracija brendova | 10/9/7 vs. F2B 10/8/8 | Uskladiti (v. KON-07) |
| 7-14 | 🟡 | Sve nasleđene reference na populaciju | 497.864 | 330.698 (v. FC-01) |
| 7-15 | 🔵 | Tačka 5, korak 5 (journey) | Grosofsky — časopis i formulacija | Uskladiti sa 4-1 |
| 7-16 | 🔵 | REZIME, nalaz 14 | „(10 dostupnih / 9 ekskluziva / 7 beauty)" | Uskladiti sa odlukom iz 7-13 |

## 6.8 `04-izvori/registar-izvora.md`

| # | | Šta |
|---|---|---|
| IZV-1 | 🔴 | **Zameniti 6 mrtvih linkova** (v. 5.1) |
| IZV-2 | 🟠 | Izvor **#29 (RZS)**: ispraviti opis — *„Populacija 15–19: **330.698** (procena 2024). Napomena: kolona 2002. daje 497.864 — ne koristiti."* |
| IZV-3 | 🟡 | Dodati kolonu **„pristup"** (otvoren / zahteva browser / iza registracije) za 43 URL-a sa 403 (v. 5.2) |
| IZV-4 | 🟡 | Dodati nove izvore iz ove faze: dm product API (Sabrina Carpenter, 08.09.2026), erstebank.rs, raiffeisenbank.rs, dpluxgroup.com, almara.rs, pipersandler.com (50. talas), Wikipedia Normal Stores, Romania Insider (sept. 2026), journals.sagepub.com (Grosofsky), pantone.com, belgradewaterfront.com (Cineplexx/IMAX), Sephora RS katalog (ponovno očitavanje) |
| IZV-5 | 🔵 | Upisati **datum ponovne provere 08.09.2026** za sve stavke koje su u ovoj fazi dotaknute — trenutno sve nose 28.08.2026 |

## 6.9 `03-isporuke/checklist-isporuka.md` i `03-isporuke/input-za-dizajn-tim.md`

| # | | Šta |
|---|---|---|
| ISP-1 | 🟡 | **Dizajn brief**: paleta ✅ ostaje nepromenjena (kontrast reprodukovan). Ali dopisati da su **boje Lilly i Belodore i dalje neizmerene** i da je to jedina rupa u auditu boja |
| ISP-2 | 🔵 | **Checklist, sekcija C**: dodati red **„Almara ispravljena u svim fazama"** i red **„Populacija ciljne grupe ispravljena (330.698)"** — dve stavke koje su specifične za ovaj projekat i lako se previde |

---

# 7. ŠTA OVA FAZA NIJE MOGLA DA URADI

1. **Cene na lilly.rs i dalje nisu očitane** — HTTP 403 potvrđen i u ovoj fazi, na svih 8
   lilly.rs URL-ova iz registra. Ostaje ručna provera 15–20 SKU u objektu.
2. **Euromonitor podaci nisu provereni** — plaćeni zid. Zadržani uz atribuciju.
3. **Imena influensera nisu verifikovana** — ova faza je potvrdila samo Jasminov TikTok (196K).
   Verifikacija ostalih traži alat ili ručno očitavanje; **nije rađena** jer je isporuka tanka
   iz drugog razloga (nedostatak imena, ne netačnost brojeva).
4. **Nije provereno da li već postoje korejske foto-kabine u beogradskim TC-ovima** — nasleđeno
   iz Faze 4; traži fizički obilazak i ostaje otvoreno.
5. **Nije rađena provera žiga „PROBAJ"** — to je zadatak za pravnika, van obima istraživanja.
6. **51. talas Piper Sandler (proleće 2026) nije javno objavljen** na dan provere — ako izađe
   pre isporuke, brojke o tinejdžerskoj potrošnji treba osvežiti još jednom.

---

# 8. ZAKLJUČAK RECENZIJE

**Istraživanje je dobro i može da ide klijentu — posle ispravki iz sekcije 6.**

Ono što je urađeno dobro, i što treba zaštititi u finalnom izveštaju:
- **Disciplina oznaka pouzdanosti** je iznad proseka za ovakav posao. Vendorske brojke su
  imenovane kao vendorske, odsustvo rezultata pretrage se nigde ne prodaje kao dokaz, a
  podatak koji ne postoji (džeparac) je **dvaput proveren i pošteno prijavljen kao nepostojeći**.
- **Pravna sekcija Faze 6 je proverena doslovno i tačna je u celini** — sve četiri odredbe,
  brojevi članova i stavova, i raspon kazni.
- **Paleta je jedina isporuka koju je recenzija uspela da reprodukuje do decimale.** Kontrastni
  odnosi su tačni, Pantone boja je tačna, audit zauzetih boja je stvarno merenje.
- **Sinteza ne izmišlja.** Nasumična provera 15 referenci tipa *(F3, nalaz 2)* nije našla
  nijedno pojačavanje tvrdnje u prenosu — što je najčešća greška u sintezama.

Ono što mora da se ispravi, po redu:
1. **Populacija ciljne grupe** (jedna greška u čitanju tabele, posledice u četiri dokumenta).
2. **Almara u Fazi 2A** (poznato deset dana, nije uneto).
3. **AOV vs. persone** (dokument protivreči sam sebi na najvidljivijem broju).
4. **NORMAL** (pogrešan lanac i pogrešan datum).
5. **Šest mrtvih linkova.**
6. Sve ostalo iz sekcije 6.

**Procena obima ispravki: 4–6 sati rada u dokumentima**, plus ~3 sata za imena influensera i
~7 sati za tri nezatvorene rupe (korpus komentara, boje Lilly/Belodore, UGC bazna linija).

**Najveći rizik za rok 11.09. nije istraživanje nego klijent.** 34 pitanja čekaju odgovor,
osam menja sadržaj isporuka, i `05-klijent/odgovori-klijenta.md` je i dalje prazan. Ako
odgovori ne stignu, izveštaj ide sa osam mesta označenih **[ČEKA ODGOVOR]** — što je pošteno,
ali oslabljuje tri isporuke (asortiman, loyalty, KLAUDS MOMENT).

---

*Dokument pripremljen po `sabloni/sablon-faze.md`. Novi i ponovo provereni izvori idu u
`04-izvori/registar-izvora.md` (v. ispravke IZV-1 do IZV-5).*

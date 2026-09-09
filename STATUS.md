# KLAUDS · status projekta

Poslednje ažuriranje: 08.09.2026 (završene Faze 2A–9; ispravke iz Faze 8 unete u FINALNI IZVEŠTAJ, ali NE i u pojedinačne fazne dokumente)
Rok isporuke klijentu: **11.09.2026** · cilj: isporuka 09–10.09.

## Faze

| Faza | Šta je | Status | Izlazni fajl |
|---|---|---|---|
| 1 | Validacija brifa + pitanja klijentu | ⬜ nije počelo | `01-faze/klauds_faza1_brief.md` |
| 2A | Konkurencija + cenovno pozicioniranje | ✅ završeno | `01-faze/klauds_faza2a_konkurencija.md` |
| 2B | Rang liste + predlog brendova | ✅ završeno | `01-faze/klauds_faza2b_rang_liste_brendovi.md` |
| 3 | Gen Z kupac | ✅ završeno | `01-faze/klauds_faza3_genz.md` |
| 4 | Retail iskustvo + KLAUDS MOMENT | ✅ završeno | `01-faze/klauds_faza4_retail_iskustvo.md` |
| 5 | Globalni benchmark + praznina | ✅ završeno | `01-faze/klauds_faza5_benchmark.md` |
| 6 | Ton i jezik brenda (posle faze 3) | ✅ završeno | `01-faze/klauds_faza6_ton.md` |
| 7 | Strateška sinteza (posle 2A–6) | ✅ završeno | `01-faze/klauds_faza7_sinteza.md` |
| 8 | Kontrola kvaliteta / fact-check | ✅ završeno | `01-faze/klauds_faza8_qa.md` |
| 9 | Finalni izveštaj + prezentacija + email | ✅ završeno | `03-isporuke/KLAUDS_analiza_trzista_i_preporuke.md` (v2) |

Legenda: ⬜ nije počelo · 🟡 u toku · ✅ završeno

## Zavisnosti

```
1 → (2A, 2B, 3, 4, 5 mogu bilo kojim redom) → 6 (traži 3) → 7 (traži sve) → 8 → 9
```

## Klijent

| Stavka | Status |
|---|---|
| Pitanja poslata klijentu | ⬜ nije poslato (nastaje u fazi 1) |
| Odgovori stigli | ⬜ ne |
| Odluka o plaćenom izveštaju o tržišnim udelima | ⬜ čeka se |
| Interni Belodore podaci (prodaja, CRM) | ⬜ traženo/nije stiglo |

## Urađeno u Fazi 2A (28.08.2026)

- Pun dokument: `01-faze/klauds_faza2a_konkurencija.md`
- Rezime za sintezu: `02-rezimei/rezime-2a.md`
- Registar izvora dopunjen: 42 izvora (`04-izvori/registar-izvora.md`)
- Cene 20+ referentnih artikala očitane direktno sa sajtova (Jasmin, Belodore, dm RS,
  dm HR, Sephora RS katalog, Mirris.rs, Apothecary.rs), kurs 1 EUR = 117,34 RSD
- Kompletan direktorijum zakupaca TC Galerija (281 zakupac, 22 beauty)

## Urađeno u Fazi 2B (28.08.2026)

- Pun dokument: `01-faze/klauds_faza2b_rang_liste_brendovi.md`
- Rezime za sintezu: `02-rezimei/rezime-2b.md`
- Registar izvora dopunjen: **88 izvora ukupno** (stavke 43–88 su iz Faze 2B)
- Konsolidovana rang lista parfemskih brendova u Srbiji iz 5 nezavisnih izvora
- Posebna rang lista viralnog kod 15–19, sa cenama i kanalom nabavke
- **Predlog od 26 brendova** u tri grupe (10 dostupnih / 8 ekskluziva / 8 beauty)
- Predlog strukture police na dan otvaranja sa udelima prometa i prostora

### ⚠️ NALAZ KOJI MENJA OKVIR — ispraviti u Fazi 8

**ALMARA parfimerije su klijentov sopstveni lanac, ne konkurencija.** DP Lux Group
poseduje tri lanca: Belodore (17 objekata, 7 zemalja), Plaza (BiH, 4) i **Almara
(6 objekata u Srbiji, uključujući TC Galerija, specijalizovan za orijentalne parfeme:
Afnan, Ajmal, Al Haramain, Armaf, Flavia, Khadlaj, Lattafa, Paris Corner, Swiss Arabian,
Zimaya)**. Uz to, DP Lux distribuira 90+ brendova na 15 tržišta.

Posledice:
1. **Faza 2A mora da se ispravi** — Almara je u tabeli konkurencije u Galeriji. Realan broj
   nezavisnih parfimerija u prizemlju je **tri** (Sephora, Jasmin, DURŌ), ne pet.
2. **Ograničenje „minimalno preklapanje sa Belodore" je preusko.** Belodore je čist niche
   (71 brend) i sa realnim KLAUDS asortimanom se skoro ne dodiruje. Pravi rizik je Almara.
3. **Nabavka nije glavni problem** — klijent sam uvozi najprodavaniji deo asortimana.

## Rupe iz Faze 2B koje treba zatvoriti (pre Faze 8)

- ~~**Google Trends** — vraćao HTTP 429 tokom cele faze.~~ ✅ **ZATVORENO U FAZI 3** —
  API je uspešno povučen 28.08.2026; krive 2019–2026 za 20+ pojmova, izvori 89–96 u registru.
- **Džeparac srednjoškolaca u Srbiji** — javnog istraživanja NEMA. **Provereno drugi put u
  Fazi 3 — i dalje ne postoji.** Najbliži surogat je hrvatsko istraživanje HUB + Štedopis
  (n=1.011, 13–19 god., 2020) — daje strukturu potrošnje, ne iznose. Zamena: interni CRM
  klijenta ili anketa na 300–500 srednjoškolaca (procena 800–1.500 EUR).
- **Puna lista 90+ DP Lux brendova** — podstranice `dpluxgroup.com/brands/*` vraćaju 403.
  Tražiti od klijenta.
- **Potvrda nedostupnosti brendova iz grupe 5b** (BBW, Kayali, Phlur, Ariana Grande, Billie
  Eilish, Glossier, Charlotte Tilbury, e.l.f.) — zaključena iz odsustva rezultata pretrage,
  što nije dokaz. Proveriti direktno kod vlasnika brendova.
- **Tvrdnja „100.000 prodatih JK JA mist-a"** — samodeklarisana na X profilu vlasnice brenda.
  NE citirati klijentu kao činjenicu; tretirati kao red veličine.

## Urađeno u Fazi 3 (28.08.2026)

- Pun dokument: `01-faze/klauds_faza3_genz.md` (797 redova)
- Rezime za sintezu: `02-rezimei/rezime-3.md` — **ovo je direktan ulaz u Fazu 6**
- Registar izvora dopunjen: **125 izvora ukupno** (stavke 89–125 su iz Faze 3)
- **Google Trends za geo=RS uspešno povučen** — 8 grupa poređenja, 2019–2026, 20+ pojmova
- Google Suggest: 35 novih upita, fokus na jezik i motivaciju (ne na brendove kao u 2B)
- Četiri arhetipa KLAUDS kupca sa procenom udela prometa i korpe — osnova za persone u Fazi 7

### Ključni novi nalazi

1. **Parfem je u Srbiji ~10× traženiji od „šminka" i ~7× od „krema za lice"** — odnos 80/20
   iz brifa je nezavisno potvrđen podacima o pretrazi.
2. **Srpski kupac miris opisuje referencama, ne notama** — od 20 autocomplete predloga za
   „parfem koji miriše na…", samo 3 su prave note; ostalo je čisto, sapun, puder, kokos,
   more, leto, krema za sunčanje. Diktira oznake na polici i filtere u web shopu.
3. **Izmeren životni ciklus viralnog proizvoda na srpskim podacima** — tri oblika (vatromet /
   plato / konstanta), sa predlogom podele nabavnog budžeta 15% / 55% / 30%.
4. **Dior Sauvage pao ~65% sa vrha, domaći Manoard iz nule na nivo Club de Nuit-a.**
5. **Dekant/discovery je najveća neuslužena prilika** — tražnja dokazana, uslužuje je samo
   sivo tržište (KupujemProdajem).
6. **Samo 2% u Srbiji potpuno veruje influenserima** (Social Serbia 2025) → KPI influencer
   kampanje mora biti dolazak i testiranje, ne prodaja preko koda.

### ⚠️ Korekcija ka Fazi 2B — ispraviti u Fazi 8

**Body mist u Srbiji ima ~4% volumena pretrage upita „parfem", a autocomplete i dalje daje
predlog „mist za telo šta je".** Faza 2B predlaže mist zid sa 18% prometa i 20% prostora.
Predlog se zadržava, ali se **mora tretirati kao kategorija koju KLAUDS mora da EDUKUJE** —
zid bez objašnjenja i bez probanja zauzeće 20% prostora za promet koji tu još nije.

## Rupe iz Faze 3 koje treba zatvoriti (pre Faze 6 i Faze 8)

- **PRIORITET — ručno prikupljanje srpskog korpusa jezika.** TikTok discover vraća prazan
  sadržaj, reddit.com blokira crawler, punmiris.com vraća HTTP 403 (Cloudflare). Potrebno
  ručno: **100–150 komentara sa 10–15 srpskih TikTok objava o parfemima + 3–5 tema sa
  PunMirisa (~4 sata).** Ovo je direktan ulaz u Fazu 6 — **uraditi PRE nje.**
- **Procene frekvencije i iznosa kupovine kod 15–19** (sekcija 6.4 punog dokumenta) su
  označene kao NISKA pouzdanost. **Ne smeju ući u finalni izveštaj kao projekcija.**
- **Apsolutni volumeni pretrage za geo=RS** — Trends daje samo relativne indekse. Zatvara se
  preko Google Ads Keyword Planner-a (traži nalog sa aktivnom kampanjom).
- **Regionalna raspodela pretraga unutar Srbije** — Trends vratio samo „Vojvodina: 100",
  uzorak pretanak. Javno se ne može zatvoriti; zameniti podacima o poreklu porudžbina posle
  lansiranja.
- **Broj pratilaca i engagement rate regionalnih kreatora** (nasleđeno iz 2B) — i dalje
  nije verifikovano. Potrebno pre pregovora o saradnji (Čovek Parfem + 10–15 mikro-kreatora).
- **Upiti `dekant`, `Yara`, `9PM` su višeznačni u srpskom** — smer nalaza pouzdan, veličina
  nije. Ne citirati kao precizne brojeve.

## Urađeno u Fazi 4 (28.08.2026)

- Pun dokument: `01-faze/klauds_faza4_retail_iskustvo.md` (1.204 reda)
- Rezime za sintezu: `02-rezimei/rezime-4.md`
- Registar izvora dopunjen: **195 izvora ukupno** (stavke 126–195 su iz Faze 4)
- Predlog zoniranja 150 m² sa kvadraturama po zonama — **brief za projektanta enterijera**
- **Tri predloga za THE KLAUDS MOMENT**, svaki sa prostorom, složenošću i načinom merenja

### Ključni novi nalazi

1. **Prvih 3–4,5 m iza ulaza fiziološki ne prodaje** (decompression zone, Underhill) — to je
   ~9% prodajnog prostora i **tačno mesto za KLAUDS MOMENT**, jer element koji tu stoji ne
   oduzima prodajni prostor nego ga stvara.
2. **Zrna kafe ne resetuju nos — dokazano netačno** (Grosofsky et al. 2011, *Chemosensory
   Perception*: 62% vs. 57%). Praktična granica je **3–4 parfema po seansi**, što problem
   pomera sa police na **pretkvalifikaciju**.
3. **Bath & Body Works — brend br. 1 po mirisu među američkim tinejdžerima — novi format
   radnje gradi na tri stvari: širi prolazi, zone, otvoreno probanje. Nijedna nije
   digitalna.** Najjači argument da budžet ne ide na ekrane.
4. **Layering je najjača poznata mehanika za korpu od 50 €** — BBW proširio „Blend Bar" sa
   pilota u 500 radnji na svih 1.900 do maja 2026; pretrage +63,9% god/god.
5. **Red na kasi**: dokumentovan slučaj UK beauty trgovca — **+18% vrednosti korpe i +27%
   artikala po transakciji bez ijednog popusta**, samo pozicioniranjem robe.
6. **Galerija već ima najveći trambolin park u ovom delu Evrope i Cineplexx sa 9 sala** —
   tinejdžeri u zgradi već postoje kao tok. KLAUDS ne mora da stvori razlog za dolazak u
   zgradu, samo za skretanje sa hodnika. **Lokal treba da bude na putu između zabavnog
   sadržaja i fashion klastera.**
7. **Pravilo „dva koraka i dva minuta"** za osoblje — obrnuto od klasične parfimerijske
   prodaje; traži drugačiju obuku i drugačiji sistem nagrađivanja (ne po prodaji po prodavcu).
8. **„Instagram zid" / neon natpis je potrošen format** i najskuplja moguća greška — kopira
   se za nedelju dana i ne daje kupcu ništa da ponese.

### ⚠️ Stavka sa ROKOM — jedina u celom projektu do sada

**Mirisno zoniranje (lokalni odsis nad test stanicama) mora ući u projekat mašinskih
instalacija za lokal.** Ako projekat ode u izvođenje bez toga, ispravka posle otvaranja je
skupa i prljava. Ovo je pitanje 19 za klijenta i treba ga postaviti pre svih ostalih.

## Rupe iz Faze 4 koje treba zatvoriti (pre Faze 7 i Faze 8)

- **Nijedan srpski retail-behavior podatak ne postoji.** Sve brojke su iz SAD, UK, EU i
  Koreje. **Ništa iz Faze 4 se ne sme citirati klijentu kao „u Srbiji je tako".**
- **Ključne brojke o efektu su vendorske** (dwell time → prodaja, +18% korpe, +30%
  konverzije kroz AI kviz, QR scan rate). Smer verovatno tačan, **veličine ne prenositi u
  izveštaj kao projekcije.**
- **PRIORITET — domaća bazna linija za UGC.** Ručna pretraga oznaka lokacije na Instagramu
  i TikToku za Sephoru, Lilly i dm u Galeriji (broj i tip objava po lokaciji). **~2 sata,
  uraditi pre Faze 7.**
- **Provera da li korejske self-photo kabine već postoje u beogradskim TC-ovima.** Srpska
  pretraga nalazi samo rentiranje za proslave; odsustvo rezultata nije dokaz. Fizički
  obilazak Galerije i Ušća.
- **Trošak elemenata KLAUDS MOMENT-a nije procenjen** (van obima). Prikupiti tri ponude —
  foto-kabina sa štampačem i softverom, rang-lista zid, termalni štampač etiketa —
  **paralelno sa Fazom 7**, da bi sinteza mogla da ih rangira po odnosu efekat/trošak.
- **Regulatorni status dekanta i layering-a** (deklarisanje, punjenje, odgovornost za
  proizvod) — van obima, ali blokira predlog „Nazovi svoj miris".
- **BBW / Piper Sandler podatak (brend br. 1 po mirisu među tinejdžerima)** preuzet iz
  indeksa pretrage jer bbwinc.com vraća HTTP 403. Proveriti pre citiranja.
- **Footfall Galerije po zonama i satima** (nasleđeno iz 2A) — Faza 4 precizira zahtev:
  potreban je **tok između zabavnog sadržaja i fashion klastera**, ne opšti footfall zgrade.

## Urađeno u Fazi 5 (28.08.2026)

- Pun dokument: `01-faze/klauds_faza5_benchmark.md` (1.106 redova)
- Rezime za sintezu: `02-rezimei/rezime-5.md` — **ulaz u Fazu 7, a sekcija o rečima i u Fazu 6**
- Registar izvora dopunjen: **294 izvora ukupno** (stavke 196–294 su iz Faze 5)
- **12 globalnih primera** obrađenih po formatu WHAT THEY DO → WHY IT WORKS → WHAT KLAUDS CAN
  LEARN → WHAT KLAUDS SHOULD NOT COPY, uključujući jedan namerno biran **anti-primer**
- **Golden Apple obrađen zasebno i dublje** (sekcija 2) — tabela prenosivosti na 150 m²
- **Boje konkurencije IZMERENE, ne procenjene** — direktno čitanje sajtova i `theme-color`
  oznaka; predložena paleta sa HEX vrednostima i izračunatim kontrastnim odnosima
- **Pet reči brenda** i lista reči koje se ne smeju vezati — direktan ulaz u Fazu 6

### Ključni novi nalazi

1. **Golden Apple je uzor za metod, ne za format.** Njihov **najmanji planirani objekat je
   600 m²** („mini", 2026), Dubai objekat 1.500 m² sa ~17.000 artikala. Prenosivo je pet
   stvari; širina ponude nije nijedna od njih.
2. **⚠️ TikTok Shop ne postoji u Srbiji** — aktivan u 10 evropskih zemalja, Srbija nije ni
   najavljena. Sve social commerce mehanike moraju ići kao **live iz radnje + drop na
   sopstvenom web shopu.** Ako se u planu pojavi „TikTok Shop", to je greška u planu.
3. **Kineski talas „Gen Z beauty" prodavnica je propao — 700+ zatvorenih objekata.** Uzrok
   nije bio koncept nego **nedostatak razlike u nabavci i popust kao odgovor na slab promet.**
   KLAUDS-ova jedina prava odbrana je sopstveni uvoz DP Lux-a i 15–25 ekskluzivnih artikala.
4. **NOSE Paris model** (5 uzoraka po fiksnoj ceni, cena se odbija od sledeće kupovine, a
   dijagnostika polazi od toga **šta si već nosio**, ne od nota) rešava odjednom probanje,
   cenovnu barijeru, CRM upis i drugi dolazak.
5. **Bath & Body Works u malom formatu ne smanjuje radnju nego briše asortiman** — na 600+
   kampus lokacija drži samo ono što grupa već kupuje, u više formata. Najkonkretnija
   smernica za 150 m².
6. **Slobodno polje u bojama je ljubičasto-indigo.** Izmereno je zauzeto: dm #002878, DURŌ
   #00A9E0, Jasmin #ED1C24, Sephora crno-belo, Notino #DE2670, **ALMARA #E7B447 (klijentov
   sopstveni lanac)**. Preporuka: **KLAUDS VIOLET #5B3DF5 · CLOUD #F0EEE9 · INK #14121C ·
   VAPOR #CFC6FF · PULSE #00E5A0**, uz obrazloženje iz recenziranog istraživanja o polu i boji.
7. **Ušteda je razlog za učlanjenje kod 71% potrošača, ali samo kod 51% Gen Z-a.** Rešenje:
   **dva odvojena brojača** — potrošnja daje proizvod, aktivnost (recenzija, glasanje, dolazak)
   daje nivo i status. Bez toga tinejdžer bez novca trajno ostaje na dnu programa.
8. **⚠️ Pravno: u Srbiji maloletnik sa 15 godina daje pristanak SAM; ispod 15 traži se
   proveriv roditeljski pristanak.** Donja granica loyalty programa mora biti 15.
9. **Loyalty sa Belodore-om: deli se sistem, ne deli se program.** Zajedničko CRM i valuta
   (MUSE i Douglas to dokazuju); odvojeno naziv, kartica, mehanika i komunikacija (A&F i
   Hollister su namerno razdvojeni). **Most ide samo u smeru Belodore → KLAUDS, za poklon.**
10. **⚠️ NORMAL (danski lanac, 1.095 objekata) ulazi u Hrvatsku i Sloveniju 2026, u Rumuniju
    aprila 2026.** Ne prodaje parfem, ali uzima artikal od 8–15 € na kome KLAUDS gradi korpu.

### Preporuka koja se ne sme prevideti

**Boja, pet reči i mehanika loyaltyja su tri odluke čiji je trošak danas nula, a posle štampe
ambalaže i CRM setupa nije.** Sve tri su u Fazi 5 zaključene merenjem, ne ukusom.

## Rupe iz Faze 5 koje treba zatvoriti (pre Faze 7 i Faze 8)

- **PRIORITET — boje Lilly i Belodore nisu izmerene.** lilly.rs vraća HTTP 403 (Cloudflare)
  na sva četiri pokušaja; belodore.com ne izlaže CSS. Potrebno **ručno očitavanje sa logotipa
  ili kese (fotografija + pipeta), ~30 minuta.** Isto važi za Victoria's Secret, Lush, The Body
  Shop, MAC i Kiko u Galeriji.
- **Prihod Gold Applea ima dve nesaglasne javne cifre** (48 mlrd RUB vs 1,7 mlrd USD).
  **Ne citirati nijednu klijentu** dok se ne nađe revidiran izveštaj.
- **Sekcija „Teens" kod Gold Applea nije mašinski potvrđena** (stranica traži JavaScript).
  Postojanje SREDNJA, sadržaj nepoznat.
- **Nijedan Gen Z beauty koncept u regionu (HR, SI, RO, HU) nije nađen** kao uzor ili pretnja.
  Odsustvo rezultata nije dokaz — pretraga je rađena na engleskom i srpskom. Zatvara se
  obilaskom Zagreba/Ljubljane ili pitanjem regionalnim distributerima DP Lux-a.
- **Cena discovery seta (1.000–1.500 RSD) je izvedena, ne merena** — NISKA. Traži proveru
  nabavne cene uzoraka i marže.
- **Kontrastni odnosi palete su izračunati, ali nisu testirani na štampi ni pod rasvetom
  lokala.** Zasićena ljubičasta se pod toplim izvorima (2700 K) pomera ka smeđoj — proveriti
  **pre projekta rasvete** (vezuje se za stavku sa rokom iz Faze 4).
- **Brojke o loyaltyju dolaze od dobavljača loyalty platformi** (Antavo, Attentive, Talon.One,
  Rivo, Open Loyalty). Smer je konzistentan, **veličine ne prenositi u izveštaj kao projekcije.**
- **Pravna analiza loyaltyja za maloletnike nije urađena** (van obima). Sekcija 6.4 daje samo
  zakonski okvir — traži proveru sa pravnikom pre CRM setupa.

## Urađeno u Fazi 6 (28.08.2026)

**Izlaz:** `01-faze/klauds_faza6_ton.md` (73 KB) · rezime: `02-rezimei/rezime-6.md`
**Izvori dodati u registar:** #295–327 (33 nova; ukupno 327)

**Metod:**
- **69 novih upita kroz Google Suggest** (`client=firefox&hl=sr&gl=rs`), fokusiranih
  isključivo na jezik, formate i sleng — ne na brendove (2B) ni na motivaciju (3).
- **Doslovni opisi objava (captions)** tri najveća domaća trgovca — Jasmin, dm, Lilly.
- **Izvorni tekst Zakona o oglašavanju RS** povučen sa sajta Narodne skupštine, izvučen iz
  PDF-a i pročitan; unakrsno provereno na Paragraf Lex.
- Recenzirana i industrijska istraživanja o brend slengu (Tippie/*JMR*, Princeton n=195,
  dcdx n=92, YouGov, Kantar) + DataReportal *Digital 2026: Serbia*.
- **TikTok komentari, Reddit i PunMiris ponovo mašinski nedostupni** — vidi Rupe.

### Ključni novi nalazi

1. **Pravilo KLAUDS jezika (glavni nalaz faze):** engleski se koristi **samo za IME STVARI**
   (body mist, layering, dekant, EDP), **nikad za IME OSEĆANJA ILI FORMATA** (vibe, haul,
   GRWM, slay, smellmaxxing, signature). Merljivo: `layering`→`layering parfema`, ali
   `haul`→`haul znacenje`/`haul prevod`, `grwm`→`gremlin`, `vajb`→`viber`. **„Previše se
   trudi" time dobija operativan test — *test prevoda*.**
2. **Tri nezavisna istraživanja mere da brend sleng ODMAŽE.** Tippie/*Journal of Marketing
   Research* („The Slang Paradox"): Arizona Tea sa slengom → **manje** lajkova; ChapStick →
   **manja** namera kupovine. Princeton (n=195, svi Gen Z): tradicionalne reklame
   **autentičnije**. dcdx (n=92): **85%** smatra „bestie" od brenda cringe.
   **⚑ Izuzetak: slengu se prašta kod INFLUENSERA, ne kod korporativnih naloga.**
3. **Otud podela posla: KREATOR NOSI JEZIK, KLAUDS NOSI TVRDNJU** (rang listu, poređenje,
   cenu, broj). Spaja se sa nalazom iz Faze 3 da u Srbiji samo 2% potpuno veruje
   influenserima → KPI ostaje **dolazak i testiranje**.
4. **Odgovor na „note vs. situacije" je treći: REFERENCA.** `parfem za izlazak/maturu/
   skolu/fakultet` = **NULA predloga**; `parfem koji mirise na …` = 10; `parfem za leto/
   zimu` = 16. **Situacija u zapadnom smislu u Srbiji nema tražnju.** Model:
   **REFERENCA → POSLEDICA → SEZONA → NOTE (sitno, poslednje).**
5. **„Koji parfem koristi [domaća zvezda]" je najjači neiskorišćen format u kategoriji** —
   devet imena u autocomplete-u (Ceca, Prijović, Karleuša, Bekvalac, **Breskvica**, Brena,
   Đoković, Rihanna). **Imena su domaća, ne globalna. Nijedan trgovac to ne uslužuje.**
6. **Domaći trgovci imaju promo ton, ne brend ton.** Jasmin (196K) piše akcijski letak
   („*ne propušta se… požuri!*") i **nema stabilnu personu — „ti" i „Vi" u istom nalogu.**
   dm je jedini dosledan na „ti". **Svi autoritet uvoze** (Parfemičar, Jeremy Fragrance).
   **Prazno mesto nije „mladalački ton" nego BILO KAKAV sopstveni stav.**
7. **Test pet reči iz Faze 5 menja im redosled: PROBAJ je izmereno prva** — prvi predlog za
   `probaj` u srpskom je **`probaj parfem`**. NOVO potvrđeno kroz `novo u dm/lidlu/ikei` →
   **„NOVO U KLAUDS"**. MOJE kroz `moja kolekcija parfema`.
8. **„Dupe" je u srpskom vulgaran homograf** (`dupeguru`, `dupence`, `dupelizac`) — kupčeva
   reč je **„kopija"** (`kopija parfema` daje 9 predloga sa imenima originala). Faza 5 je
   „dupe" zabranila stilski; sada postoji merljiv, jači razlog.
9. **U Srbiji Instagram ima veći doseg od TikToka (3,40 vs 2,98 mil.), ali TikTokova cifra
   NE obuhvata uzrast 13–17** — tj. najveći deo primarne ciljne grupe. Podela: TikTok =
   otkrivanje (oglasno nemerljivo za maloletnike), Instagram = doseg i zajednica.
10. **Predložena podela tona: 55% ISKRENO · 25% PLAYFUL · 15% EDUKATIVNO · 5% EKSPERTSKO ·
    0% PREMIUM U JEZIKU.** Humor namerno nije u centru — **Kantar meri da je kod Gen Z-a
    MUZIKA, a ne humor, najjači faktor prijemčivosti** (humor je najjači kod Gen X i boomera).

### ⚠️⚠️ NALAZ SA NAJVEĆIM POSLEDICAMA U CELOJ FAZI — pravna ograničenja tona

> **Ovo nije pravno mišljenje** (pravno savetovanje je van obima). Odredbe su citirane iz
> izvornog teksta zakona. **Pre prve kampanje obavezno mišljenje advokata.**

Zakon o oglašavanju RS definiše **maloletnika kao lice od 12 do 18 godina** (čl. 21 st. 7) —
**cela primarna ciljna grupa KLAUDS-a.** Četiri odredbe direktno diktiraju ton:

**SUDAR 1 — čl. 25, st. 3** zabranjuje da poruka namenjena maloletnicima „*sugeriše da će
korišćenjem robe steći fizičke, intelektualne ili druge **društvene prednosti nad ostalim
maloletnicima***". **To direktno pogađa najjači nalaz Faze 3 („kupuje se kompliment").**
Rešenje ne oslabljuje poruku nego je pojačava:
**KLAUDS ne OBEĆAVA reakciju, nego je MERI i objavljuje.**
„Budi ta koju primete" ❌ → „*Najčešći komentar na ovaj: 'stalno me pitaju šta nosim'*" ✅.
*(Obećanje konkurent kopira za dan; merenje ne može — nema podatke.)*

**SUDAR 2 — čl. 23, st. 6** zabranjuje vrednosni sud uz cenu, **doslovno reči „samo",
„sitnica", „povoljno"**. Ovo **potvrđuje** preporuku Faze 3 o otvorenoj ceni, uz jednu
izmenu: **cena ostaje, pridev odlazi.** „Samo 990!" ❌ → „990 din · 30 ml" ✅.

**Čl. 21, st. 1, tač. 2** — poruka ne sme **neposredno pozivati maloletnike na kupovinu ni
da to zahtevaju od roditelja.** Važi i za **Viber i newsletter** → CRM se piše u
**informativnom, ne prodajnom modu**: „Kupi sad!" ❌ → „Ovo je ponovo na polici." ✅;
„Traži od mame" ❌ → „Wishlist ti je spreman za deljenje." ✅.

**Čl. 10, tač. 4** — maloletnik se ne sme dovoditi u vezu sa seksualnošću →
**„sexy/provokativno" je za KLAUDS ISKLJUČENO.** Granica: privlačnost kao **posledica koju
drugi primete** — da; privlačnost kao **seksualna ponuda** — ne.

Kazne: **300.000–2.000.000 RSD.**

**Posledica za CRM:** baza se **od prvog dana segmentira na 15–17 / 18+ / odrasli** — iz
pravnih, ne marketinških razloga. ZZPL (Faza 5) rešava **da li** sme da se šalje (granica 15
godina); čl. 21 rešava **šta sme da piše.** To su **dva odvojena ograničenja**, ne jedno.

### Rupe iz Faze 6 koje treba zatvoriti (pre Faze 8)

1. **⚑ Doslovni korpus srpskih TikTok komentara I DALJE NIJE PRIKUPLJEN.** Platforme ponovo
   blokirale (prazan render / HTTP 403 / blokiran Reddit JSON). Faza 6 je to zaobišla
   merenjem pretrage i doslovnim captionima trgovaca — što je **jače za jezik kupovine, ali
   ne pokriva jezik razgovora.** **Ručno, ~4 sata: 100–150 komentara sa 10–15 srpskih TikTok
   objava + 3–5 tema sa PunMirisa.** Ovo je jedini nezatvoren ulaz u ovu fazu.
2. **Autocomplete meri kucanje, ne govor.** Odsustvo predloga dokazuje da se ne pretražuje,
   ne da se ne govori. Isto se zatvara rupom 1.
3. **Nema dokumentovanih regionalnih promašaja tona** — sekcija o promašajima stoji
   isključivo na globalnim primerima. Zatvara se razgovorom sa 2–3 domaće agencije.
4. **Starosna struktura po platformi za Srbiju nije javna** (TikTok ne prikazuje 13–17).
   Jedini domaći podatak (CKPS, n=700) je iz **2021.** (TikTok 6,6%) — **proveren i odbačen,
   ne koristiti.**
5. **⚠️ Status žiga „PROBAJ" nije proveren.** U autocomplete-u postoji trag `probaj
   parfem.rs` (domen na dan provere ne odgovara). **Provera u Zavodu za intelektualnu
   svojinu pre nego što reč uđe u slogan ili domen.**
6. **Podela tona 55/25/15/5 je izvedena, ne merena** → A/B test naslova na IG oglasima u
   prva tri meseca.
7. **Frekvencija CRM poruka (2 mesečno za 15–17) je radna pretpostavka** bez domaćeg
   benchmark-a → kalibrisati na stopi odjave posle 3 meseca.
8. **⚠️ Pravni deo traži advokata** — naročito dva sudara gore. Ovo je jedina stavka faze
   koja može zaustaviti kampanju ako se ne uradi.

## Urađeno u Fazi 7 (28.08.2026)

- Pun dokument: `01-faze/klauds_faza7_sinteza.md` (~1.440 linija, 10 isporuka + rezime)
- Samostalan brief: **`03-isporuke/input-za-dizajn-tim.md`** — upotrebljiv bez ostatka izveštaja
- Sve tvrdnje vezane za nalaz iz konkretne faze oznakom tipa *(F3, nalaz 2)* — nijedna nova
  tvrdnja o tržištu nije uvedena
- **Jedina nova pretraga u ovoj fazi:** konkretna imena influensera sa srpske/regionalne scene
  (tačka 3) — Modash, StarNgage, nova.rs, BURO247, YouTube kanali Parfemičar i Čovek Parfem

### Šta je isporučeno — svih 10 stavki iz prompta

| # | Isporuka | Gde je |
|---|---|---|
| 1 | 4 customer persone (A „Maja", B „Nikola", C „Teodora/Luka", D „Snežana") | sekcija 1 |
| 2 | 5 content pillars sa TikTok i Instagram formatima | sekcija 2 |
| 3 | Top 10 tipova influensera + konkretna imena za verifikaciju | sekcija 3 |
| 4 | Top 10 aktivacija sa složenošću i benchmark vezom | sekcija 4 |
| 5 | Launch smernice: faza 0 / pre-launch / otvaranje / 90 dana + 11 metrika | sekcija 5 |
| 6 | Customer journey (10 koraka) + top 5 interaktivnih elemenata | sekcija 6 |
| 7 | Do/don't principi u četiri bloka (komunikacija / asortiman / radnja / digital) | sekcija 7 |
| 8 | Finalna preporuka cenovnog pozicioniranja | sekcija 8 |
| 9 | Input za dizajn tim | sekcija 9 + **zaseban fajl** |
| 10 | 26 brendova u tri grupe + struktura police | sekcija 10 |

### Ključne odluke koje je sinteza donela

1. **Cenovni spor „pristupačno" vs. „slično Sephora" razrešen trećom pozicijom:**
   *cene koje tinejdžer može sam da plati, u prodavnici koja izgleda i radi kao da košta duplo.*
   Artikal **25–35 €**, korpa **45–60 €**, ulazna tačka **6–12 €**.
2. **⚠️ Klijentov cilj od 30 € po artiklu meri pogrešnu stvar.** Prava operativna metrika je
   **broj artikala po korpi (≥ 2,0)**, jer svaki viralni miris koji ciljna grupa kupuje je 30–55 €.
3. **Najvažnija aktivacija nije ni jedna od zabavnih — nego 15–25 artikala ekskluzive.**
   Kineski „Gen Z beauty" talas je imao sve ostalo i zatvorio 700 objekata.
4. **Preporuka za Almaru: opcija B** — iste kuće, drugi formati (mini, seti, mist, discovery)
   pod pop/Gen Z narativom. Almara zadržava klasične boce i orijentalni narativ.
5. **Pet interaktivnih elemenata, nijedan nije ekran.**

### ⚠️ Usko grlo projekta se pomerilo sa istraživanja na klijenta

**`05-klijent/odgovori-klijenta.md` je prazan.** 28 otvorenih pitanja iz faza 2A–6 nije
razrešeno, a **osam direktno menja sadržaj Faze 7**: odnos prema Almari · broj ekskluziva (23) ·
foto-kabina (17) · istinitost rang liste (18) · boja brenda (22) · discovery set (24) ·
loyalty sa dva brojača (25) · budžet za testere (27). Sve je u dokumentu označeno **[ČEKA ODGOVOR]**.

### Rupe iz Faze 7 (za Fazu 8)

1. **Imena influensera nisu verifikovana** — brojevi pratilaca su iz sekundarnih agregatora;
   engagement, starosna struktura publike, brand safety i cene nisu provereni ni za jedno ime.
   **Pouzdanost imena: NISKA do SREDNJA.** Tipovi i logika: VISOKA.
2. **Budžet klijenta nije poznat** — rangiranje aktivacija po odnosu efekat/trošak je kvalitativno.
   Tri ponude (foto-kabina, rang-lista zid, štampač etiketa) **nisu prikupljene.**
3. **Udeli persona u prometu (35/25/20/20) su radna procena, NISKA pouzdanost** — ne smeju ući
   u finansijsku projekciju.
4. Nezatvorene rupe iz ranijih faza koje Faza 7 nije mogla da zameni: korpus TikTok komentara
   (~4 h), domaća bazna linija za UGC (~2 h), boje Lilly i Belodore (~30 min).

## Otvorena pitanja koja je Faza 6 otvorila (za `05-klijent/`)

28. **Prihvata li se pravilo „Ti" uvek, „Vi" nikad** — na svim kanalima, uključujući natpise
    u radnji i web shop? (Ulazi u fizičke natpise; posle otvaranja se teško menja.)
29. **Ko pravno proverava copy pre kampanja?** Sudari sa čl. 25 st. 3 i čl. 23 st. 6 traže
    mišljenje **pre**, ne posle.
30. **Prihvata li se da KLAUDS ne obećava komplimente nego ih MERI?** To znači da radnja i
    web shop moraju te podatke **prikupljati od prvog dana** (jedno polje u recenziji).
31. **Ko piše — jedan glas ili agencija po kanalu?** Preporuka: **jedan copywriter za sve
    kanale u prvoj godini.** Doslednost glasa nosi više od pojedinačne objave.
32. **Ugovorni kreatori isključivo 18+?** Pravno čistije (čl. 21 + saglasnost roditelja);
    gubi se nešto autentičnosti kod 15–17. Mlađi od 18 samo kao organski UGC koji se ne plaća.
33. **Prihvata li se da najviše 1 od 5 objava bude o ceni/akciji?** Direktan otklon od
    domaće prakse — očekivati otpor iz prodaje.
34. **Je li „PROBAJ" slobodan kao žig?** Zadatak za pravnika pre ulaska u naziv.

## Otvorena pitanja koja je Faza 5 otvorila (za `05-klijent/`)

22. **Prihvata li klijent ljubičasto-indigo (#5B3DF5) kao boju brenda, umesto izvedenice
    Golden Apple kiselo-zelene (#DCFF00)?** Odluka o samostalnosti brenda; donosi se **pre
    projekta enterijera i pre naručivanja ambalaže.**
23. **Koliko artikala može da bude stvarna ekskluziva za Srbiju** (roba koju DP Lux uvozi, a
    ne drži ni Almara ni Belodore ni drugi trgovci)? Cilj **15–25 na dan otvaranja** — to je
    jedina odbrana koncepta koju konkurencija u Galeriji ne može da kopira.
24. **Ide li discovery set (5 uzoraka, cena se odbija od sledeće kupovine) u obim otvaranja?**
    Lakša varijanta pitanja 14 — uzorci od brenda, bez punjenja, pa verovatno bez regulatornog
    problema koji dekant ima.
25. **Prihvata li se loyalty sa DVA brojača** — potrošnja (daje proizvod) i aktivnost (daje
    nivo i status)? Odluka pre izbora CRM platforme.
26. **Donja granica loyalty programa: 15 godina.** Potvrđuje li klijent, i ko pravno proverava
    uslove programa pre lansiranja?
27. **Postoji li budžet za mesečnu zamenu testera kao stalnu stavku?** Bez toga „sve otvoreno"
    ne stoji, a zaključavanje testera ruši reč PROBAJ i sa njom celu poziciju.
28. **Prati li se NORMAL kao pretnja?** Ulazi u Hrvatsku i Sloveniju 2026, u Rumuniju april 2026.

## Otvorena pitanja koja je Faza 3 otvorila (za `05-klijent/`)

12. **Prihvata li klijent da KLAUDS otvoreno vodi „sličan na…" narativ?** Dokazana tražnja
    (`parfem sličan … ali jeftiniji`) i domaći brend koji je na tome izgradio poziciju
    (Manoard). Ovo je strateška odluka o brend integritetu, ne operativna.
13. **Sme li se planirati zasebna zona i komunikacija za momke od prvog dana?** Segment
    raste +44% god/god vs. +22% kod devojaka i troši više po glavi. Preporuka je pomeriti
    cilj sa 20% ka 30% u prvih 12 meseci.
14. **Ulazi li dekant/discovery format u obim otvaranja?** Ima regulatorne i operativne
    implikacije (deklarisanje, punjenje) koje su van obima ovog istraživanja, ali je to
    najveća neuslužena prilika koju je istraživanje našlo.
15. **Ulazi li wishlist + fizička QR poklon-kartica u obim otvaranja?** Rešava treću poklon
    situaciju („tinejdžer traži da mu se kupi") koju danas ne uslužuje nijedan trgovac u
    Srbiji, i problem 15–16 segmenta bez platne kartice.
16. **Kada se zaključava finalna lista brendova?** Kriva Sabrine Carpenter (12 meseci uspona,
    na trećini vrha posle 24) pokazuje da roba nabavljena u vrhu trenda postaje mrtav lager.
    Preporuka: zaključati najranije u martu 2026, uz 15% budžeta rezervisano za novo.

## Otvorena pitanja koja je Faza 2A otvorila (za `05-klijent/`)

1. **Kanibalizacija Belodore ↔ KLAUDS u istom tržnom centru** — oba bi bila na prizemlju
   TC Galerija. Da li klijent to prihvata i kako pozicionira dva svoja brenda na 30 m
   razdaljine?
2. **Zajednički loyalty sa Belodore-om** — Lilly ima 900.000 članova kao benchmark.
   Odluka utiče na ceo CRM setup.
3. **Footfall TC Galerija po zonama i satima** — javno ne postoji; treba tražiti od
   zakupodavca u pregovorima o lokalu.
4. **Izbor lokala u Galeriji** — preporuka je van beauty koridora (bliže Zara/Bershka/
   Pull & Bear klasteru). Da li je to još moguće u pregovorima?
5. Potvrda cenovnog cilja: preporuka je artikal **25–35 EUR** / korpa **45–60 EUR**.


## Otvorena pitanja koja je Faza 2B otvorila (za `05-klijent/`)

6. **ODNOS KLAUDS ↔ ALMARA (prioritet 1).** Almara ima objekat u TC Galerija i drži tačno
   najprodavaniji orijentalni blok (Lattafa, Armaf, Afnan). Sme li KLAUDS da ih drži i u
   kojim formatima? Preporuka istraživanja: **iste kuće, drugi SKU i formati** (mini, seti,
   mist, discovery) pod pop/Gen Z narativom, dok Almara zadržava klasične boce.
7. **Puna lista 90+ brendova koje DP Lux distribuira**, sa uslovima nabavke. Najbrži put do
   finalne liste brendova; nije javno dostupno.
8. **Interni podaci Belodore/Almara o kupcima mlađim od 25** — struktura korpe, prosečna
   vrednost, učestalost, top SKU. Zamenjuje nepostojeći podatak o džeparcu.
9. **Može li se dobiti zvanična distribucija za e.l.f. i Bath & Body Works?** Dve najjače
   potvrđene praznine u ponudi za 15–19 u Srbiji.
10. **Prihvata li klijent TRI sopstvena objekta u istoj zgradi** (Belodore 360 m², Almara,
    KLAUDS 150 m²)?
11. **Budžet za brzu anketu na 300–500 srednjoškolaca (800–1.500 EUR)?** Bez toga nema
    domaćeg podatka o kupovnoj moći tinejdžera.

## Otvorena pitanja koja je Faza 4 otvorila (za `05-klijent/`)

17. **Da li je u budžetu opreme predviđena foto-kabina sa štampačem i softverom?** Jedini
    KLAUDS MOMENT predlog sa značajnim kapitalnim troškom; traži odluku **pre** projekta
    enterijera, jer zauzima ulaznu zonu.
18. **Prihvata li klijent da rang lista „TOP 10 ove nedelje" bude istinita, i kada ne
    odgovara nabavci?** Isto po prirodi kao pitanje 12 (brend integritet).
19. **Ide li mirisno zoniranje — lokalni odsis nad test stanicama — u projekat mašinskih
    instalacija? PITANJE SA ROKOM.**
20. **Deli li se loyalty sa Belodore-om i po kojoj mehanici?** Faza 4 menja odgovor na
    pitanje 2 iz Faze 2A: mehanika koja radi za KLAUDS publiku (zadaci, nivoi, nagrada u
    proizvodu) je **suprotna** od one koja radi za Belodore publiku (status, tihe
    pogodnosti). Preporuka: **isti CRM, dva različita programa.**
21. **Prihvata li se pravilo „dva koraka i dva minuta" kao standard usluge?** Obrnuto od
    klasične parfimerijske prodaje; traži drugačiju obuku i drugačiji sistem nagrađivanja
    osoblja (ne po prodaji po prodavcu).

## Rupe u podacima koje treba zatvoriti ručno (pre Faze 8)

- **Lilly cene** — lilly.rs blokira automatsko čitanje. Potrebna ručna provera 15 SKU.
- **Sephora Srbija cene** — jedini javni izvor je `dev.` katalog; potreban fizički obilazak
  objekta u Galeriji sa listom SKU.
- **Brojevi pratilaca na IG/TikTok** — preuzeti iz pretrage, treba ručno proveriti i
  dodati engagement rate (koristi se u Fazi 3 i 6).

## Urađeno u Fazi 8 (08.09.2026)

- Pun dokument: `01-faze/klauds_faza8_qa.md`
- **22 tvrdnje visokog rizika provereno nezavisno**; **svih 322 jedinstvenih linkova iz
  registra izvora mašinski provereno** na HTTP status; prekontrolisani svi izvedeni računi
  (kursne konverzije, procentualne razlike, kontrastni odnosi palete, matematika korpe)

### ⚠️⚠️ TRI GREŠKE KOJE MENJAJU ZAKLJUČKE

1. **Populacija 15–19 u Srbiji nije 497.864 nego 330.698.** Uzeta je kolona **popisa iz 2002**
   umesto procene RZS za 2024; uz to je tačan broj (330.698) pogrešno predstavljen kao „urbani
   deo" te populacije — konstrukcija koja u izvoru ne postoji. **Primarna ciljna grupa je
   precenjena za ~51%.** Pogađa F2A (izvor #29, rezime), F2B (4.2, rezime 10), F3 i F7.
   *Izračun „73,5% ciljne grupe je van Beogradskog regiona" PREŽIVLJAVA* — on je iz školske
   statistike, koja je potvrđena do poslednje cifre.
2. **NORMAL ne ulazi u Hrvatsku i Sloveniju — to je Action** (holandski lanac). NORMAL je u
   Rumuniju ušao **30.09.2026** (Mega Mall Bukurešt, 275 m²), ne u aprilu. Pogađa F5 (nalaz 17,
   1.11), F7 i ovaj fajl.
3. **Tabela persona ne može da proizvede AOV od 45–60 €.** Iz udela prometa i korpi u F7 tačka 1
   matematički sledi **AOV ≈ 34 €** — 26% ispod donje granice cilja koji isti dokument tvrdi na
   tri mesta.

### Ostale netačne tvrdnje

4. **Raiffeisen iRačun je 18+**, ne „besplatan za sve ispod 18". Erste je **16+**. Time je
   finansijski rez ciljne grupe **15 / 16–19**, ne 15–16 / 17–19 — a F2B protivreči sam sebi
   na razmaku od tri reda. F7 persona A („od 17. godine") je netačna.
5. **Studija o zrnima kafe** objavljena je u ***Perceptual and Motor Skills* (2011, 112(2),
   536–538)**, ne u *Chemosensory Perception*; n=63, autori je zovu eksplorativnom; treća grana
   (limun, 86%) je izostavljena. Oznaka **VISOKA → SREDNJA**, „dokazano netačno" → „nije potvrđeno".
6. **Sephora Srbija ima 66 brendova** (F2A i F7 kažu 55, F2B kaže 67). **Rhode nije u zvaničnom
   katalogu** iako F2A tvrdi da je uveden.
7. **Sabrina Carpenter: obe cene postoje.** 2.699 RSD (23,0 €) za četiri od pet EdP varijanti;
   3.999 RSD (34,1 €) samo za Lemon Pie. Dokumenti od 2B nadalje citiraju samo skuplju i na njoj
   grade tvrdnju „gotovo tačno ciljani artikal".
8. **BBW „24% udela kod tinejdžerki" nije potvrđeno** ni u jednom javnom izvoru — briše se.
   Potvrđeno je samo „#1 mirisni brend" i „#3 trgovac sa 7%".
9. **Piper Sandler podaci su iz 49. talasa (april 2025).** U 50. talasu (jesen 2025) tinejdžerska
   beauty potrošnja **pala je 2% god/god na 336 USD**, a BBW je izašao iz prve trojke trgovaca.

### ⚑ NOVI NALAZ KOJI ISTRAŽIVANJE NIJE ZABELEŽILO

**dm već prodaje Sabrina Carpenter body mist 236 ml po 1.249–1.499 RSD (10,6–12,8 €)** — tačno
cenovnu tačku „drugog artikla u korpi" na kojoj cela KLAUDS AOV logika stoji, sa celebrity
brendom koji je označen kao najjači role model ciljne grupe, u objektu u prizemlju iste zgrade.
**Mist zid od 18% prometa ne ulazi u praznu kategoriju.** Ulazi u F2A (7.1), F3 i F7 (t. 8 i 10).

### Šta je POTVRĐENO i ne dira se

- **Zakon o oglašavanju — sve četiri odredbe doslovno tačne** (čl. 21 st. 6–7, čl. 21 st. 1
  tač. 2, čl. 23 st. 6, čl. 25 st. 3, čl. 10 tač. 4) + kazne 300.000–2.000.000 RSD.
  **Najpouzdanija sekcija u celom projektu.**
- **Paleta: kontrastni odnosi nezavisno preračunati i sva tri tačna** (5,28 / 11,34 / 16,2).
  Pantone „Cloud Dancer" #F0EEE9 ✓. **Boja se NE menja.**
- **DP Lux poseduje Almaru** (6 objekata u Srbiji, uključujući TC Galerija; grupno 8) ✓
- **Srednje obrazovanje 2025/2026 — svaka cifra tačna** (225.639 / 491 škola / regionalna podela)
- **Galerija: trambolin park + Cineplexx 9 sala i IMAX** ✓ · **Gold Apple „mini" 600 m²** ✓
- **Prosečna neto zarada jun 2026: 120.401 / medijalna 94.281** ✓ · **notino.rs i dalje ne postoji** ✓
- **Piper Sandler april 2025: momci 88→127 USD (+44%), e.l.f. 35%, BBW #1 miris** ✓
- **Sinteza ne izmišlja** — nasumična provera 15 referenci tipa *(F3, nalaz 2)* nije našla
  nijedno pojačavanje tvrdnje u prenosu.

### Provera linkova: 322 URL-a

259 OK · 43× HTTP 403 (anti-bot, rade u browseru) · 8× 429 (uglavnom Google Trends) ·
**6 stvarno mrtvih** — buro247.rs (nosi isporuku „Top 10 influensera"), nativemedia.rs (Viber
90%), nbcnews.com (smellmaxxing), cosmeticsdesign-europe (P.Louise, 410 Gone),
cosmeticsdesign-asia (MINISO, 410 Gone), retaildive BBW Gingham+ (520).

### Konzistentnost — 12 nađenih protivrečnosti

AOV vs. persone · Almara u F2A nije ispravljena · Sephora 55 vs. 67 · Sabrina Carpenter 23 € vs.
34,1 € · dva različita para brojeva o potrošnji momaka · finansijski rez 15–16/17–19 ·
grupe brendova 10/8/8 vs. 10/9/7 · **34 otvorena pitanja, ne 28, uz duplirani broj 28** ·
Sephora loyalty „globalno" vs. „S. Amerika" · 1,7 vs. ≥2,0 artikla po korpi ·
Golden Apple / Gold Apple · metodološki prekid u tabeli cena F2A (red 20).

### Pouzdanost — 4 nedosledne oznake + 6 preporuka bez ograde na mestu preporuke

Nedosledno: zrna kafe (VISOKA→SREDNJA) · Hurlbert & Ling / boja (VISOKA→SREDNJA, **boja se ne
menja**, težina se prenosi na audit konkurencije koji JESTE merenje) · „parfem 10× traženiji"
(VISOKA za smer, SREDNJA za faktor) · F2A tabela 4.2 red 20.
Bez ograde na mestu preporuke: **mist zid 18%/20%** · udeli persona u tački 6 · podela nabavnog
budžeta 15/55/30 · **cela tabela strukture police u F7 tačka 10** · frekvencija 6–10× godišnje ·
cilj „≥ 2,0 artikla po korpi".

### Pokrivenost checkliste: 12 od 15 zeleno, 3 žuto, 1 crveno

🔴 **Stavka 4 „Top 10 influensera"** je isporučena kao **10 tipova, ne 10 imena**; tip 8 nema
nijedno ime, tipovi 3 i 10 nemaju; nijedno ime nije verifikovano; jedan izvor je mrtav.
🟡 Persone (brojke protivrečne) · cenovno pozicioniranje (stoji na precenjenoj populaciji) ·
predlog brendova (numeracija se razlikuje između F2B i F7).

### Rupe koje su bile obavezne PRE Faze 8 — nijedna nije zatvorena

Mišljenje advokata ❌ · korpus srpskih TikTok komentara (~4 h) ❌ · boje Lilly i Belodore
(~30 min) ❌ · domaća bazna linija za UGC (~2 h) ❌ · ispravka F2A/Almara ❌ (ide sada).
**Tri od pet se zatvaraju za ~7 sati rada.**

## Urađeno u Fazi 9 (08.09.2026)

**Izlazi:**
- `03-isporuke/KLAUDS_finalni_izvestaj.pdf` — **68 strana A4**, brendiran, sa koricama,
  sadržajem sa brojevima strana, brojevima strana u futeru i PDF bookmarkovima
- `03-isporuke/KLAUDS_prezentacija.html` — prezentacija za prolaz i slanje klijentu, 13 slajdova
- `03-isporuke/KLAUDS_finalni_izvestaj.md` — **2.419 redova**, 9 poglavlja + 3 priloga
- `03-isporuke/KLAUDS_prezentacija_slajdovi.md` — **12 slajdova** + 7 rezervnih, sa govornim
  napomenama i predlogom vizuala po slajdu
- `05-klijent/propratni-email.md` — pun tekst + kraća varijanta samo za vlasnika
- `03-isporuke/checklist-isporuka.md` — **prođena i čekirana**

> Napomena (09.09.2026): svi v1 izlazi ove faze — `KLAUDS_finalni_izvestaj.md/.pdf`,
> `KLAUDS_prezentacija.html`, `KLAUDS_prezentacija_slajdovi.md` — **obrisani su** pošto ih je
> zamenila verzija 2.0. Zapis ispod je istorijski.

### ⚠️ Ključna odluka ove faze

**Faza 9 je startovala iako ispravke iz Faze 8 nisu bile unete u dokumente faza.**
Umesto čekanja, **finalni izveštaj je napisan direktno na ispravljenim podacima** — Faza 8 je
tretirana kao autoritativna nad ranijim fazama. U izveštaju stoji izričita napomena da
**u slučaju razlike važi finalni izveštaj**, a **Prilog B popisuje svih 18 ispravki** radi
sledljivosti.

**Posledica:** `01-faze/*` i dalje nose stare brojeve. **Ako se ti dokumenti šalju klijentu ili
koriste kao osnova za dalji rad, prvo uneti ispravke iz `01-faze/klauds_faza8_qa.md`, sekcija 6**
(procena 4–6 h). Finalni izveštaj je samodovoljan i ne zavisi od toga.

### Šta je konkretno ispravljeno u finalnom izveštaju

| Ispravka | Bilo → Jeste |
|---|---|
| Populacija 15–19 | 497.864 → **330.698** (RZS 2024; 497.864 je popis 2002) |
| Almara | konkurent → **klijentov sopstveni lanac**; u Galeriji **tri nezavisne parfimerije + dva DP Lux objekta** |
| AOV | „45–60 €" na tri mesta → **~40 € start, 45–60 € cilj druge godine**; artikala po korpi **1,8 → 2,0** |
| NORMAL | „HR i SI 2026, RO april" → **Action za HR/SI**; NORMAL u RO **30.09.2026**, format 275–380 m² |
| Erste / Raiffeisen | rez 15–16 / 17–19 → **15 / 16–19** (Erste 16+, Raiffeisen 18+) |
| Sephora RS | 55 / 67 brendova → **66**; Rhode **nije u katalogu** (SREDNJA) |
| Sabrina Carpenter | „34,1 €" → **23,0 € za 4 od 5 varijanti**; + **dm mist 10,6–12,8 €** |
| BBW | „24% udela" → **briše se**; ostaje #1 mirisni brend, #3 trgovac 7% |
| Piper Sandler | „poslednji talas" → **49. talas (april 2025)**, uz ogradu o 50. talasu (−2%, BBW ispao iz top 3) |
| Zrna kafe | *Chemosensory Perception*, „dokazano netačno", VISOKA → ***Perceptual and Motor Skills* 112(2)**, „nije potvrđeno", **SREDNJA** |
| TikTok Shop | 10 zemalja → **11** (dodat Portugal); Srbija i dalje nije ni najavljena |
| Otvorena pitanja | 28 / 34 → **35** (broj 28 je bio dupliran); niz prenumerisan |
| Grupe brendova | 10/8/8 → **10/9/7** (e.l.f. u ekskluzive), ukupno 26 |
| Gold Apple | „Golden Apple" → **Gold Apple** uz fusnotu |
| Oznake pouzdanosti | mist zid, struktura police, udeli persona, 15/55/30, frekvencija 6–10×, cilj 2,0 — **svi dobili ogradu NA MESTU preporuke** |

### Stanje checkliste posle Faze 9

**15 od 15 stavki isporučeno.** Sekcija C: **9 zeleno, 3 žuto, 1 nezatvoreno.**

| Ostaje otvoreno | Šta treba |
|---|---|
| 🟡 **Isporuka 4 — influenseri** | Isporučeno kao **10 tipova**, ne 10 verifikovanih imena. Ograničenje je **eksplicitno napisano** u izveštaju i u emailu. **~3 h ručnog rada** zatvara |
| 🟡 **Ispravke u faznim dokumentima** | Nisu unete u `01-faze/` (4–6 h) |
| 🟡 **6 mrtvih linkova** | Popisani u **Prilogu C** sa zamenama; nijedan nalaz ne pada |
| ✅ **Konverzija u PDF** | **urađeno** — 68 strana, prelomi provereni |

## Sledeći korak

1. ~~Konvertovati izveštaj u PDF~~ — **urađeno 08.09.2026.** `KLAUDS_finalni_izvestaj.pdf`,
   68 strana, bez praznih strana i bez osamljenih redova tabela.
2. **Poslati klijentu** — tekst je gotov u `05-klijent/propratni-email.md`. Uz izveštaj ide i
   `03-isporuke/input-za-dizajn-tim.md` kao zaseban prilog.
3. **Zakazati prezentaciju** — 12 slajdova, ~60 min (35–40 izlaganje + 20 na osam odluka).
   **Tražiti da prisustvuju i nabavka i projektant enterijera** — pola pitanja je iz njihovog
   domena.
4. **Paralelno, ako ima vremena do sastanka** (~7 h ukupno): korpus srpskih TikTok komentara
   (4 h), boje Lilly i Belodore (30 min), bazna linija za UGC (2 h). Sve tri su popisane u
   poglavlju 9.2 izveštaja kao otvorene — bolje ih zatvoriti nego objasniti.

## ⚠️ Šta i dalje blokira klijenta, ne nas

**35 otvorenih pitanja**, od kojih **osam menja sadržaj isporuka**: Almara (6) · ekskluzive (23) ·
mirisno zoniranje ⏱ (19) · boja (22) · foto-kabina (17) · istinitost rang liste (18) · loyalty
sa dva brojača (25) · budžet za testere (27).

**Uz njih, jedna stavka koja može zaustaviti kampanju: ⚖️ mišljenje advokata** — čl. 25 st. 3,
čl. 23 st. 6 Zakona o oglašavanju, i status žiga „PROBAJ".

**Preostaje i `/faza-1`** (validacija brifa) — nije blokirajuća; njena jedina neispunjena
funkcija (slanje paketa pitanja klijentu) sada je pokrivena poglavljem 9.3 izveštaja i
propratnim emailom.

## Verzija 2.0 (09.09.2026) · prerada po feedbacku pre slanja

**Novi klijentski dokument:** `03-isporuke/KLAUDS_analiza_trzista_i_preporuke.md` + `.pdf`
(60 strana) + `03-isporuke/slike/` (6 grafika). Stari `KLAUDS_finalni_izvestaj.md/.pdf` i
stara prezentacija obrisani 09.09.2026 — v1 se ne šalje. Nova prezentacija: `KLAUDS_prezentacija_slajdovi_v2.md`.
Propratni email prepisan. Registar izvora dopunjen na 403 stavke (336 do 403 su iz Faze 8 i
iz ove prerade).

**Sve što treba znati pre slanja je u `INTERNO_pre-slanja-v2.md`** (tabela izmena, šta nije
moglo, podaci za proveru, osam odluka, otvorena pitanja, šta još poslati).

Ključno: uklonjen interni QA materijal i tehničke rupe iz klijentske verzije; 73,5% i
76,8%/100% preformulisani iz primarnih RZS izvora; pouzeće se NE ukida zakonom; Lilly dobio
sopstvenu sekciju (lista brendova, cene, događaji); 10 konkretnih influensera sa brojevima sa
profila; NORMAL datumi ispravljeni (30.09. i 02.10.2026 su najava); plan lansiranja u dva
scenarija; osam odluka na jednoj strani.

**Otvoreno posle v2:** uzorak TikTok komentara (4 h), boje sa logotipa (30 min), UGC bazna
linija (2 h), cene u objektima (2 h), obilazak (2 h), verifikacija kreatora (3 h + alat),
HTML prezentacija (2 h), fazni dokumenti u `01-faze/` i dalje nose stare greške.

# KLAUDS · FINALNI AKCIONI PLAN ISTRAŽIVANJA TRŽIŠTA (v2)

Pripremio: VladsDigital · Za interno praćenje · Rok isporuke klijentu: 11.09.2026 (cilj: isporuka 09–10.09)

---

## 0. KAKO SE KORISTI OVAJ PLAN

**Preporučena postavka (štedi vreme i kontekst):**

1. Na claude.ai napravi **Project** pod imenom „KLAUDS istraživanje".
2. U **Project instructions** nalepi ceo **KONTEKST BLOK** (sekcija 1 ispod). Time svaki novi razgovor u projektu automatski ima pun kontekst i pravila rada — ne moraš ništa da prekopiravaš.
3. Svaka faza = **novi razgovor u projektu**, sa uključenim web search-om. Nalepi samo prompt te faze.
4. Rezultat svake faze sačuvaj kao poseban fajl, po konvenciji:
   `klauds_faza2a_konkurencija.md`, `klauds_faza3_genz.md` itd.
5. Svaki prompt faza 2A–6 na kraju traži sekciju **„REZIME ZA SINTEZU"** (max 1 strana). Te rezimee ćeš nalepiti u fazu 7 — puni dokumenti mogu da se prilože kao fajlovi ako zatreba dubina.

Ako ne koristiš Projects: otvori novi razgovor po fazi i nalepi KONTEKST BLOK + prompt faze u istoj poruci.

**Redosled i zavisnosti:**

```
FAZA 1 (brief + pitanja klijentu)
   ├── FAZA 2A (konkurencija + cene)      ┐
   ├── FAZA 2B (rang liste + brendovi)    │  mogu PARALELNO,
   ├── FAZA 3  (Gen Z kupac)              │  nezavisne jedna od druge
   ├── FAZA 4  (retail iskustvo)          │
   └── FAZA 5  (globalni benchmark)       ┘
            FAZA 6 (ton komunikacije) ← radi se POSLE faze 3 (koristi njen rezime)
                     FAZA 7 (sinteza) ← posle SVIH prethodnih
                          FAZA 8 (kontrola kvaliteta / fact-check)
                               FAZA 9 (finalni izveštaj + prezentacija)
```

**Vremenski plan (danas je 27.08, rok 11.09, klijent traži ubrzanje):**

| Datum | Aktivnost |
|---|---|
| 27–28.08 | Faza 1 + slanje otvorenih pitanja klijentu (ne čekati odgovore da bi se krenulo dalje) |
| 28.08–02.09 | Faze 2A, 2B, 3, 4, 5 — paralelno (realno 1 radni blok po fazi) |
| 02–03.09 | Faza 6 (posle faze 3) |
| 03–05.09 | Faza 7 · strateška sinteza (uključi odgovore klijenta ako su stigli) |
| 05–08.09 | Faza 8 · kontrola kvaliteta + ispravke |
| 08–09.09 | Faza 9 · finalni izveštaj + verzija za prezentaciju |
| 09–10.09 | Interna revizija, formatiranje (Word/PDF), isporuka |

---

## 1. KONTEKST BLOK (nalepi u Project instructions, ili na početak svakog razgovora)

```
Ti si istraživač tržišta koji radi za agenciju VladsDigital. Klijent je DP Lux Group
(vlasnik lanca niche parfimerija Belodore). Radimo istraživanje tržišta za KLAUDS,
njihov novi retail koncept. Sve što napišeš ulazi u izveštaj koji čita menadžment i
vlasnik kompanije (interno, ne investitori) — ton je direktan i radni, ne "pitch".

KONCEPT KLAUDS:
- Multibrend prodavnica: 80% parfemi, 20% beauty proizvodi; vremenom i sopstveni
  private label. Parfemi su nosilac koncepta.
- Sopstveni flagship objekti + web shop (sopstveni sajt, ne marketplace; ne franšiza).
- Nastupa kao samostalan brend, odvojen od Belodore komunikacije, ali verovatno deli
  isti loyalty program (ovo je i strateško pitanje — Belodore publika je starija/premium).
- Razlog pokretanja: postojeće parfimerije u Srbiji su konceptom okrenute starijoj
  populaciji; KLAUDS cilja mlade — "Klauds su teenageri". Interaktivan koncept koji
  poštuje njihov svet, način biranja i način komunikacije (preporuke iz digitalnog sveta).

CILJNA GRUPA:
- Primarno: devojke 15–19 (50%) i momci 15–19 (20%).
- Sekundarno: 30% odraslih koji kupuju za sebe ili za tinejdžere.
- Pokloni su bitan segment; očekivani obrazac: većinski planirana kupovina + impulsna
  za dodatni asortiman (podiže AOV).
- Fokus je na Gen Z PONAŠANJU, ne samo demografiji.

LOKACIJA I FORMAT:
- Prvi objekat: TC Galerija, Beograd, 150 m². Otvaranje: oktobar 2026.
- Kanali: web shop, performance marketing, Instagram, TikTok, newsletter, Viber.

CENE I ASORTIMAN:
- Prosečna cena artikla ~30 EUR; ciljna vrednost korpe (AOV) ~50 EUR.
- Cenovno pozicioniranje: klijent je dao dva neusklađena odgovora — "pristupačno" i
  "slično Sephora" (srednje-premium). Istraživanje treba da da preporuku za razrešenje.
- Minimalno preklapanje sa Belodore asortimanom. Lista brendova još ne postoji;
  klijent OČEKUJE da mu istraživanje predloži idealne brendove.

UZOR: Golden Apple (beauty retail iz regiona). Po viđenju klijenta, direktna
konkurencija po konceptu (mladi, interaktivno, Gen Z) u Srbiji trenutno ne postoji.

KLIJENT EKSPLICITNO TRAŽI da se ne oslanjamo samo na to šta ljudi KAŽU, već na stvarno
ponašanje: search behavior, TikTok i Reddit razgovori, viral product lifecycle, jezik
u recenzijama, engagement, konkurentski traffic, ponašanje u fizičkom retailu.

METODOLOGIJA RANG LISTA (javnih podataka o prodaji po artiklu u Srbiji nema):
rang liste najprodavanijih proizvoda/brendova grade se iz pet nezavisnih izvora —
objavljene bestseller liste na sajtovima trgovaca, volumen pretraga, zastupljenost i
cene na policama, prisustvo na društvenim mrežama, zvanični finansijski izveštaji.

VAN OBIMA: pravno/poresko/carinsko savetovanje, uvozne procedure, transport i
skladištenje, precizne finansijske projekcije, terensko istraživanje (ankete, intervjui).

PRAVILA RADA (važe za svaki zadatak):
1. Koristi web search za sve tvrdnje o tržištu. Uz svaki ključni nalaz navedi izvor
   (naziv + link).
2. Uz svaki nalaz označi pouzdanost: VISOKA (više nezavisnih izvora), SREDNJA (jedan
   solidan izvor ili posredan zaključak), NISKA (pretpostavka/ekstrapolacija).
3. Jasno razdvajaj: podatak / interpretacija / preporuka.
4. Ne izmišljaj brojeve, imena, statistike ni izvore. Ako podatka nema, napiši da ga
   nema i predloži kako se može proceniti.
5. Piši na srpskom; engleske stručne termine ostavi u originalu gde je prirodno.
6. Kada tražiš lokalne podatke, pretražuj i na srpskom i na engleskom.
```

---

## 2. CHECKLIST ISPORUKA (mapa: šta klijent dobija → gde nastaje)

Isporuke koje je klijent eksplicitno tražio (Q48):

| # | Isporuka | Nastaje u | Finalizuje se u |
|---|---|---|---|
| 1 | Postavka vizuelnog identiteta (input za dizajn tim) | 5, 6 | 7 (sekcija 9) |
| 2 | Pozicioniranje na tržištu | 2A, 5 | 7 |
| 3 | Do/don't principi brenda | sve faze | 7 |
| 4 | Top 10 influensera | 7 (uz aktivnu pretragu) | 7 |
| 5 | Top 10 aktivacija za lansiranje | 4, 5 | 7 |
| 6 | Launch smernice | 7 | 7 |
| 7 | 3–4 customer persone | 3 | 7 |
| 8 | Content pillars | 3, 6 | 7 |
| 9 | Customer journey + top 5 interaktivnih elemenata | 4 | 7 |

Dodatne isporuke koje proizlaze iz upitnika (Q15, Q49 sekcija 4):

| # | Isporuka | Nastaje u | Finalizuje se u |
|---|---|---|---|
| 10 | Preporuka cenovnog pozicioniranja („pristupačno" vs „kao Sephora") | 2A | 7 |
| 11 | Predlog idealnih brendova za asortiman (klijent ovo očekuje — Q15) | 2B | 7 |
| 12 | THE KLAUDS MOMENT | 4 | 7 |
| 13 | 3–5 reči koje ciljna grupa spontano vezuje za KLAUDS | 5 | 7 |
| 14 | Boja/paleta za detalje brenda (unisex, uklapa se u koncept) | 5 | 7 |
| 15 | Motiv za učlanjenje u loyalty program (van popusta) | 5 | 7 |

> Pre isporuke klijentu proći kroz obe tabele i overiti da svaka stavka postoji u finalnom izveštaju.

---

## 3. FAZA 1 · Validacija brifa i pitanja za klijenta

Cilj: radni brief, potvrda da ništa iz upitnika nije promaklo, i lista pitanja koja se ODMAH šalje klijentu (odgovori se uključuju u fazu 7 ako stignu na vreme; istraživanje ne čeka).

```
Krećemo sa istraživanjem za KLAUDS (kontekst je u uputstvima projekta).

ZADATAK ZA OVU FAZU (bez dubinskog istraživanja — pripremamo teren):

1. Napravi radni brief na pola strane koji sažima kontekst — referentni dokument za
   sve naredne faze. Proveri da li u kontekstu ima unutrašnjih kontradikcija ili rupa
   koje bi mogle da ugroze istraživanje, i navedi ih.

2. Sastavi listu otvorenih pitanja za klijenta, spremnu za slanje (formulisanu učtivo
   i konkretno). Obavezno uključi:
   - okvirni budžet lansiranja (red veličine),
   - gradovi/redosled širenja posle Beograda i broj objekata u godinama 1–3,
   - politika akcija, popusta i loyalty programa (u upitniku "TBD"),
   - da li je loyalty zaista deljen sa Belodore (i kako to vide s obzirom na potpuno
     različitu publiku),
   - okvirni broj brendova u prvoj godini i da li već postoje dogovori sa dobavljačima,
   - potvrda da žele da im MI predložimo idealne brendove (Q15),
   - interni Belodore podaci (prodaja po kategorijama, CRM, statistika sajta) — da li
     mogu da se dobiju,
   - da li ih zanima plaćeni izveštaj o tržišnim udelima za Srbiju (pomenut u upitniku),
   - ključni interni rokovi: do kada mora postavka vizuelnog identiteta, do kada se
     naručuje asortiman,
   - u kojoj meri računaju na muške kupce 15–19 (Q25 ostalo prazno).

3. Predloži početnu listu direktnih i indirektnih konkurenata u Srbiji za mapiranje u
   fazi 2A: parfimerije (uklj. Belodore radi konteksta), kozmetički lanci i drogerije,
   premium prodajna mesta, online prodavci (uklj. regionalne koji isporučuju u Srbiju),
   i sivu/neformalnu konkurenciju ako je relevantna (Instagram/TikTok preprodavci,
   dekanti). Za TC Galerija posebno označi ko od njih već ima lokal u samom centru.

4. Predloži listu ključnih pojmova za praćenje search/TikTok ponašanja u fazi 3
   (srpski + engleski), kao polaznu tačku.
```

**Posle faze 1:** pitanja iz tačke 2 poslati klijentu istog dana.

---

## 4. FAZA 2A · Konkurencija i cenovno pozicioniranje

```
Radimo mapiranje konkurencije i analizu cena (kontekst u uputstvima projekta).

ZADATAK:

1. Mapiraj relevantne igrače u Srbiji: parfimerije (Sephora, Lilly, dm, Jasmin,
   Aleksandar Cosmetics, Beauty Fox, Belodore i druge koje nađeš), drogerije, premium
   prodajna mesta i online prodavce (uklj. Notino i druge regionalne koji isporučuju
   u Srbiju). Za svakog: koje brendove drži (posebno parfemi koje bi Gen Z prepoznao),
   širina asortimana, cenovno pozicioniranje, kanali (fizički/online/oba), kako
   komunicira (ton, kanali, da li i kako cilja mlađu publiku, TikTok/Instagram
   prisustvo i engagement).

2. Posebno obradi TC GALERIJA: koji beauty/parfem igrači već imaju lokal u Galeriji,
   gde su pozicionirani, šta to znači za KLAUDS na 150 m² u istom centru (i kao
   konkurencija i kao dokaz tražnje).

3. Analiza cena: uporedi cene 15–20 referentnih parfema (mix: mass/designer viralni
   među Gen Z + pristupačni niche) između srpskih prodavaca i referentnih tržišta
   (region + EU, npr. Notino u više zemalja). Utvrdi: koji cenovni rasponi postoje,
   na šta su kupci navikli, koliko su popusti i promocije standard (realna cena na
   polici vs. deklarisana), razlike fizičko vs. online.

4. Postavi cenovnu analizu u odnos sa ciljem klijenta: prosečan artikal ~30 EUR,
   korpa ~50 EUR. Šta na tržištu realno postoji u tom rasponu, i šta taj raspon
   znači za strukturu asortimana (koje kategorije/formati proizvoda upadaju u ~30 EUR:
   body mist, manji ml formati, pristupačni designer, lifestyle brendovi...).

5. Daj EKSPLICITNU PREPORUKU za razrešenje kontradikcije "pristupačno" vs "slično
   Sephora": gde tačno KLAUDS treba da stoji, čime se to brani, i šta bi bio rizik
   pogrešnog izbora u oba smera.

6. Zaključi: ko je najozbiljniji konkurent i zašto; koje praznine u ponudi konkurencije
   KLAUDS može da iskoristi.

Format: strukturiran dokument sa podnaslovima, izvorima i nivoom pouzdanosti.
Na kraju dodaj sekciju "REZIME ZA SINTEZU" (max 1 strana, 10–15 najvažnijih nalaza).
```

---

## 5. FAZA 2B · Rang liste, tržišni kontekst i predlog brendova

```
Radimo rang liste najprodavanijih proizvoda, širi tržišni kontekst i predlog brendova
za KLAUDS asortiman (kontekst u uputstvima projekta).

ZADATAK:

1. Napravi rang listu najprodavanijih/najtraženijih parfemskih brendova i proizvoda u
   Srbiji, po metodologiji iz brifa (pet nezavisnih izvora), sa nivoom pouzdanosti za
   svaki nalaz. Posebno izdvoj šta je traženo KOD MLADIH (viralni parfemi, TikTok
   favoriti dostupni u Srbiji) — to je za KLAUDS važnije od opšte liste.

2. Isto uradi, kraće, za beauty kategoriju (20% asortimana): koje beauty kategorije i
   brendovi su najtraženiji kod 15–19 u Srbiji/regionu.

3. Širi kontekst tržišta: veličina i rast tržišta parfema/kozmetike u Srbiji,
   demografija ciljne grupe (koliko ima 15–19-godišnjaka, gde žive), kupovna moć —
   POSEBNO kupovna moć tinejdžera: džeparac, ko plaća (roditelji?), načini plaćanja
   (kartice/keš/pouzeće — bitno za web shop), penetracija online kupovine kod mladih,
   razvijenost premium segmenta.

4. PREDLOG BRENDOVA (klijent je eksplicitno tražio da mu istraživanje ovo predloži):
   sastavi listu od 15–25 brendova idealnih za KLAUDS, podeljeno na:
   a) brendovi već prisutni u Srbiji koje Gen Z traži (lako dostupni za nabavku),
   b) brendovi koje Gen Z traži a NISU prisutni u Srbiji (prilika za ekskluzivu),
   c) beauty dopuna (20% asortimana).
   Za svaki: zašto odgovara ciljnoj grupi, okvirni cenovni rang, uklapanje u ~30 EUR
   prosečan artikal, i da li se preklapa sa Belodore (izbegavati preklapanje).

5. Zaključi: šta struktura tražnje govori o tome kako KLAUDS asortiman treba da
   izgleda na dan otvaranja.

Format: strukturiran dokument sa izvorima i nivoom pouzdanosti.
Na kraju dodaj sekciju "REZIME ZA SINTEZU" (max 1 strana).
```

---

## 6. FAZA 3 · Gen Z kupac: ponašanje i motivacija

Klijentu najvažnija faza (Q24, Q49/1).

```
Radimo dubinski deo o KLAUDS kupcu (kontekst u uputstvima projekta). Ovo je za
klijenta najvažniji deo istraživanja. Ne zanima nas samo demografija nego ponašanje.

ZADATAK — istraži i odgovori:

1. Šta najviše triguje mladu osobu (15–19) da kupi parfem? Ključne reči, trendovi,
   role modeli. Gde god je moguće, koristi podatke za Srbiju/region/Balkan; globalne
   Gen Z nalaze jasno označi kao globalne i proceni koliko su prenosivi.

2. Gde se mladi ZAPRAVO informišu o parfemima — šire od marketinških kanala: uticaj
   vršnjaka i okoline, idoli/influenseri koji nisu iz parfemske industrije (muzika,
   sport, gaming, lifestyle), PerfumeTok/#perfumetok, Reddit (r/fragrance i sl.),
   YouTube recenzenti, regionalni kreatori.

3. Dominantan motiv: signature scent, status, trend, ili value for money? Da li se
   razlikuje devojke vs. momci, i mlađi (15–16) vs. stariji (18–19)?

4. Koliko Gen Z poznaje mirisne note, a koliko kupuje po osećaju, estetici i
   viralnosti (TikTok viral parfemi)? Šta to znači za način na koji se parfemi
   predstavljaju u radnji i online?

5. Spremnost na eksperimentisanje sa nepoznatim brendovima: šta je čini prihvatljivom
   (preporuka influensera, ambalaža, cena, društveni dokaz, mogućnost testiranja)?

6. Kupovna moć i mehanika kupovine kod 15–19: džeparac, uloga roditelja u plaćanju,
   frekvencija kupovine parfema, prosečan iznos koji su spremni da daju. Uloga
   POKLONA (i kad tinejdžer prima poklon od odraslog, i kad kupuje drugarima).

7. Analiza stvarnog ponašanja (ne izjava): search behavior i volumen pretraga za
   relevantne pojmove i brendove (srpski + engleski), TikTok i Reddit razgovori,
   jezik u recenzijama i komentarima (koje reči koriste za miris), viral product
   lifecycle — kako parfem postane viralan, koliko talas traje, šta ostaje posle.

8. Sinteza: profil "KLAUDS kupca" — 3 do 4 kratka arhetipa/segmenta unutar ciljne
   grupe (uključi i sekundarnu grupu: odrasli koji kupuju za sebe ili za poklon
   tinejdžeru). Ovo je osnova za customer persone u sintezi.

Format: nalazi po pitanjima sa izvorima, sinteza na kraju.
Na kraju dodaj sekciju "REZIME ZA SINTEZU" (max 1 strana).
```

---

## 7. FAZA 4 · Retail iskustvo, prostor i „KLAUDS MOMENT"

```
Radimo deo o fizičkom i digitalnom iskustvu u prodavnici (kontekst u uputstvima
projekta). Prodavnica: 150 m², TC Galerija, Beograd. Klijent želi prostor koji nije
samo komercijalan nego interaktivan i "shareable" — da kupci prirodno postaju content
creatori bez direktnog traženja. Klijent je otvoren i za zabavne nekomercijalne
elemente (pominjao je npr. stoni hokej).

ZADATAK — istraži i odgovori:

1. Šta privlači kupca sa hodnika tržnog centra, i šta treba da vidi u prvih 5–10
   sekundi od ulaska?

2. Koji deo radnje treba prvi da poseti? Kako Gen Z voli da istražuje parfeme —
   samostalno vs. uz prodavca, i kako osoblje treba da se ponaša da ne otera
   tinejdžera (pristup "dostupan ali nenametljiv")?

3. Kako organizovati asortiman da bude intuitivan ovoj grupi: po brendu, notama,
   raspoloženju/mood-u, trendu, ceni — ili kombinacija? Kako učiniti discovery
   jednostavnim i kako SPREČITI SENSORY OVERLOAD (150 m² parfema je puno mirisa —
   šta rade najbolji: coffee bar momenti, zone, blotter sistemi, digitalna
   pretkvalifikacija)?

4. Koja digitalna iskustva ZAISTA dodaju vrednost ovoj grupi (AI preporuka mirisa,
   ekrani, QR, digital testing, gamifikacija) — sa konkretnim primerima gde je već
   primenjeno u svetu i šta je poznato o efektu? Jasno odvoj dokazano-korisno od
   gimmick-a.

5. Šta povećava dwell time, konverziju i veličinu korpe kod ove grupe (primeri iz
   retaila; uključi mehanike za impulsnu dokupovinu koja diže korpu ka 50 EUR —
   mini formati, kasa zona, bundlovi, gift-ready pakovanja)?

6. Pokloni: kako radnja treba da podrži gifting (odrasli kupuje tinejdžeru; tinejdžer
   kupuje drugarici) — gift smernice, pakovanje, gift kartice?

7. Shareability analiza: koji retail elementi najčešće generišu organski UGC — šta
   ljudi fotografišu i snimaju, šta ih tera da taguju prijatelje, šta generiše FOMO.
   Primeri iz beauty, perfume, fashion, sneakers, hospitality, entertainment i
   experiential retail industrija (ne samo parfimerije). Za svaki primer: mehanizam
   zašto radi, ne samo opis.

8. Na osnovu svega predloži THE KLAUDS MOMENT: 1–3 konkretna iskustvena elementa koja
   bi kupac hteo da slika/snimi/podeli i koja postaju prepoznatljiva za brend.
   Za svaki: opis, zašto će raditi baš za ovu ciljnu grupu, okvirna složenost
   izvođenja (nisko/srednje/visoko), i kako se meri da li radi.

Format: nalazi po pitanjima sa primerima i izvorima, jasan predlog KLAUDS momenta na
kraju. Na kraju dodaj sekciju "REZIME ZA SINTEZU" (max 1 strana).
```

---

## 8. FAZA 5 · Globalni benchmark i tržišna praznina

```
Radimo globalni benchmark i definisanje praznine koju KLAUDS preuzima (kontekst u
uputstvima projekta).

ZADATAK:

1. Istraži najbolje i najinovativnije koncepte iz: perfume retail, beauty retail,
   experiential retail, Gen Z retail, social commerce, creator economy, entertainment
   retail. Posebno primeri iz Evrope, SAD, Bliskog istoka, Kine, Koreje i Japana.

2. Obradi 8–12 najrelevantnijih primera, svaki u formatu:
   WHAT THEY DO (konkretno) → WHY IT WORKS (mehanizam) → WHAT KLAUDS CAN LEARN →
   WHAT KLAUDS SHOULD NOT COPY (i zašto: neprimenljivo na srpsko tržište, preskupo,
   ne odgovara pozicioniranju, zahteva scale koji KLAUDS nema).

3. Obavezno uključi GOLDEN APPLE (klijentov navedeni uzor) — objasni konkretno šta
   kod njega funkcioniše i šta je od toga prenosivo na 150 m² u Beogradu.

4. Definiši prazninu: koju konkretnu poziciju KLAUDS može da preuzme na srpskom
   tržištu? Šta bi bio razlog da neko kaže "Idemo u Klauds" umesto "idem da kupim
   parfem"? Šta danas nedostaje mladima između klasičnih parfimerija, niche
   parfimerija, drogerija i online/TikTok discovery-ja?

5. Predloži 3–5 reči koje treba da se spontano vezuju za KLAUDS u svesti ciljne
   grupe, sa obrazloženjem.

6. Predloži boju ili paletu za detalje brenda: atraktivna i prihvatljiva i za mušku
   i za žensku publiku, uklapa se u koncept, i RAZLIKUJE se od boja postojećih igrača
   na srpskom tržištu (proveri čime se koriste Sephora, Lilly, dm, Notino, Belodore
   i sl. da ne dođe do preklapanja). Obrazloži izbor.

7. Predloži motive za učlanjenje mlade osobe u loyalty program VAN klasičnog popusta
   (pristup, status, early access, iskustva, gamifikacija...) — sa primerima programa
   koji to već uspešno rade. Osvrni se i na to da li deljenje loyalty programa sa
   Belodore pomaže ili odmaže, s obzirom na potpuno različitu publiku.

Format: benchmark po primeru (tabela ili strukturisana lista), sinteza praznine na
kraju. Na kraju dodaj sekciju "REZIME ZA SINTEZU" (max 1 strana).
```

---

## 9. FAZA 6 · Ton komunikacije i jezik brenda

**Radi se posle faze 3.** Na početak razgovora, ispod prompta, nalepi „REZIME ZA SINTEZU" iz faze 3.

```
Radimo ton i jezik komunikacije za KLAUDS (kontekst u uputstvima projekta). Ispod
prompta je nalepljen rezime nalaza o ciljnoj grupi iz prethodne faze — koristi ga.

KLJUČNO OGRANIČENJE: klijent ne želi tradicionalni beauty/perfume jezik. Cilj je da
brend zvuči autentično mladoj publici, a NE kao da se "previše trudi da bude mlad".

ZADATAK — istraži i odgovori:

1. Kako Gen Z u Srbiji i regionu prirodno govori o parfemima i beauty proizvodima:
   koji izrazi, sleng, mešanje srpskog i engleskog, formati (GRWM, perfume
   collection, "koji parfem nosiš danas"...) su prirodni, a šta deluje forsirano?
   Traži stvarne primere sa TikToka/Instagrama/YouTube-a na srpskom/regionalnom.

2. Koji ton u ovoj kategoriji deluje zastarelo, a koji deluje kao da brend forsira
   mladalački ton? Navedi primere brendova koji su pogodili i koji su promašili
   (globalno i regionalno ako nađeš).

3. Gde KLAUDS treba da stoji na spektru: humoristično / sexy / provokativno /
   edukativno / ekspertsko / playful / premium — ili kombinacija? Obrazloži na
   osnovu nalaza o ciljnoj grupi. Obrati pažnju: publika su maloletnici — "sexy/
   provokativno" ima jasne granice; definiši ih.

4. Note vs. situacije: da li KLAUDS govori o mirisnim notama (klasično) ili o
   situacijama, emocijama i reakcijama koje parfem izaziva (bliže Gen Z)?
   Argumentuj podacima; predloži i hibridni model ako ima smisla (npr. situacija
   napred, note kao sekundarna informacija).

5. Razlike po kanalima: TikTok, Instagram, web shop, CRM (email/Viber/newsletter) i
   sama radnja (natpisi, police, osoblje). Za svaki kanal: uloga, ton, format.
   Ne zaboravi da CRM za maloletnu publiku ima ograničenja (pristanak, ton).

6. Predloži 5–10 konkretnih primera fraza, hook-ova ili formata objava koji bi
   zvučali autentično za KLAUDS (na srpskom, sa engleskim gde je prirodno).

7. Završi vodičem tona: tabela "OVAKO DA / OVAKO NE" sa parovima primera (ista
   poruka napisana pogrešno i ispravno) — ovo ide direktno u input za dizajn tim i
   buduće copywritere.

Format: nalazi po pitanjima, primeri, vodič tona na kraju.
Na kraju dodaj sekciju "REZIME ZA SINTEZU" (max 1 strana).
```

---

## 10. FAZA 7 · Strateška sinteza

**Novi razgovor.** Nalepi prompt + svih šest „REZIME ZA SINTEZU" blokova (2A, 2B, 3, 4, 5, 6). Ako su stigli odgovori klijenta na pitanja iz faze 1, nalepi i njih. Pune dokumente faza priloži kao fajlove ako platforma dozvoljava.

```
Ovo je sintezna faza istraživanja za KLAUDS (kontekst u uputstvima projekta). Ispod
prompta su nalepljeni rezimei svih istraživačkih faza: konkurencija i cene (2A), rang
liste i brendovi (2B), Gen Z kupac (3), retail iskustvo (4), globalni benchmark (5),
ton komunikacije (6). Koristi ISKLJUČIVO te nalaze + opšte znanje; ništa novo ne
izmišljaj. Ako za neku stavku nema dovoljno osnova u nalazima, reci to eksplicitno.

Za stavku 3 (influenseri) koristi web search da proveriš i dopuniš konkretna imena.

ZADATAK — napravi svaku od sledećih isporuka, jasno odvojene:

1. CUSTOMER PERSONE (3–4): ime/arhetip, uzrast, ključne motivacije, ponašanje pri
   kupovini (uklj. ko plaća), omiljeni kanali i kreatori, šta ih privlači a šta odbija
   kod brenda, tipična korpa u KLAUDS-u. Bar jedna persona iz sekundarne grupe
   (odrasli — za sebe ili poklon). Zasnovano na fazi 3.

2. CONTENT PILLARS (4–6): tematski stubovi za društvene mreže; za svaki: opis, zašto
   radi za ovu publiku (veza sa nalazima), primer formata objave za TikTok i za
   Instagram.

3. TOP 10 INFLUENSERA: kombinovano —
   a) 10 tipova/kategorija kreatora koje KLAUDS treba da targetira (niša, raspon
      pratilaca, tip sadržaja, zašto odgovara ciljnoj grupi);
   b) za svaki tip, konkretna imena sa srpske/regionalne scene kao primeri, sa
      napomenom da lista imena mora da se verifikuje pre outreach-a (aktuelnost,
      brand safety, cene).

4. TOP 10 AKTIVACIJA za lansiranje i redovan rad: konkretni predlozi (događaji,
   kampanje, saradnje, in-store aktivacije). Za svaku: opis, cilj (awareness/traffic/
   UGC/prodaja), okvirna složenost (nisko/srednje/visoko), veza sa benchmark nalazom
   iz faze 5. Označi koje su realne i sa skromnim budžetom (budžet klijenta nepoznat).

5. LAUNCH SMERNICE: akcioni vodič za otvaranje u oktobru 2026 — faze (pre-launch
   teasing, opening, prvih 90 dana), ključni koraci i redosled, šta MORA biti spremno
   pre otvaranja, ključne metrike uspeha za prvih 90 dana.

6. CUSTOMER JOURNEY kroz prodavnicu sa TOP 5 INTERAKTIVNIH ELEMENATA: hronološki od
   hodnika tržnog centra do izlaska i post-kupovine (deljenje na mrežama, loyalty
   enrollment, retencija). Za svaki interaktivni element: šta je, gde stoji u
   prostoru, koju fazu journey-ja pojačava. Uključi KLAUDS MOMENT iz faze 4.

7. DO / DON'T PRINCIPI BRENDA: komunikacija, proizvod/asortiman, iskustvo u radnji,
   digital. Kratko, oštro, sa obrazloženjem u jednoj rečenici po stavci.

8. FINALNA PREPORUKA CENOVNOG POZICIONIRANJA: razreši "pristupačno" vs "slično
   Sephora" na osnovu faze 2A; jedna jasna rečenica pozicioniranja + šta to znači za
   asortiman, cene i komunikaciju.

9. INPUT ZA DIZAJN TIM (postavka vizuelnog identiteta): objedini na jednom mestu —
   preporučena boja/paleta (faza 5), 3–5 reči brenda (faza 5), ton i jezik (faza 6,
   uklj. "ovako da/ovako ne"), vizuelne reference iz benchmarka koje pogađaju pravac,
   i vizuelni do/don't (šta izbegavati da ne liči na postojeće igrače ili na
   "korporativni pokušaj mladosti"). Ovo mora da bude upotrebljivo kao samostalan
   brief za dizajnera.

10. PREDLOG BRENDOVA ZA ASORTIMAN: finalizuj listu iz faze 2B — top 15–25 brendova
    (prisutni u Srbiji / prilika za ekskluzivu / beauty dopuna), sa kratkim
    obrazloženjem i vezom sa cenovnim pozicioniranjem iz tačke 8.

Format: jasno odvojene sekcije, konkretno i akciono. Izbegavaj generičke marketinške
fraze bez pokrića u nalazima — svaka preporuka mora da može da se poveže sa nalazom
iz neke faze.
```

---

## 11. FAZA 8 · Kontrola kvaliteta (obavezna pre finalnog izveštaja)

Izveštaj ide klijentu — svaka izmišljena cifra ili mrtav link ruši kredibilitet celog dokumenta. **Novi razgovor**, priloži dokumente faza 2A–7 (ili njihove ključne delove).

```
Radiš kontrolu kvaliteta istraživanja za KLAUDS pre finalnog izveštaja (kontekst u
uputstvima projekta). Priloženi su dokumenti istraživačkih faza i sinteze. Budi
skeptičan recenzent, ne autor.

ZADATAK:

1. FACT-CHECK: izdvoj sve konkretne tvrdnje visokog rizika — brojeve, cene, tržišne
   podatke, imena brendova/prodavnica/influensera, tvrdnje "X je prisutan/nije
   prisutan u Srbiji". Za 15–20 najvažnijih (onih na kojima počivaju preporuke)
   proveri web search-om da li su tačne i aktuelne. Označi: POTVRĐENO / NETAČNO
   (sa ispravkom) / NE MOŽE SE PROVERITI (šta sa tim — ublažiti formulaciju ili
   izbaciti).

2. KONZISTENTNOST: da li se faze međusobno protivreče (npr. cenovna preporuka iz 2A
   vs. predlog brendova iz 2B vs. persone iz 3)? Da li sinteza tvrdi nešto što
   istraživačke faze ne podržavaju?

3. POKRIVENOST: proveri prema checklisti isporuka (15 stavki — 9 eksplicitnih od
   klijenta + 6 dodatnih iz upitnika) da li svaka postoji i da li je konkretna, a ne
   generička. Označi šta je tanko.

4. POUZDANOST: da li su nivoi pouzdanosti dosledno označeni? Da li negde preporuka
   stoji na nalazu niske pouzdanosti a to nije rečeno?

5. Izlaz: lista konkretnih ispravki po dokumentu (šta, gde, kako da glasi), poređana
   po važnosti.
```

**Posle faze 8:** uneti ispravke u dokumente faza pre nego što se pređe na fazu 9 (može u istom razgovoru: „primeni ispravke i ispiši korigovane sekcije").

---

## 12. FAZA 9 · Finalni izveštaj i verzija za prezentaciju

**Novi razgovor**, priloži korigovane dokumente svih faza.

```
Kompajluj sve priložene nalaze u finalni izveštaj istraživanja tržišta za KLAUDS
(kontekst u uputstvima projekta). Čitaoci: menadžment i vlasnik kompanije, interno.
Ton: direktan i radni, ne "pitch". Ne uvodi nove tvrdnje — samo organizuj, sažmi i
izoštri postojeće.

ZADATAK:

1. EXECUTIVE SUMMARY na jednoj strani: najvažniji nalazi + ključne preporuke
   (pozicioniranje, kupac, praznina, KLAUDS moment, cena). Ovo je prvo i možda
   jedino što će vlasnik pročitati u celini — mora da stoji samostalno.

2. Struktura izveštaja:
   1. Executive summary
   2. Metodologija i nivoi pouzdanosti (kratko — kako su građene rang liste)
   3. Tržišni kontekst i konkurencija (uklj. TC Galerija, cene, cenovna preporuka)
   4. Ko je KLAUDS kupac (nalazi + persone)
   5. Retail iskustvo i THE KLAUDS MOMENT (uklj. customer journey + 5 interaktivnih
      elemenata)
   6. Globalni benchmark i praznina na tržištu
   7. Ton i jezik brenda + input za dizajn tim
   8. Strateške preporuke (content pillars, influenseri, aktivacije, launch
      smernice, do/don't, predlog brendova)
   9. Zaključak, otvorena pitanja i sledeći koraci

3. Zadrži izvore i nivoe pouzdanosti uz ključne nalaze; na kraju dodaj spisak svih
   izvora (appendix).

4. Sekcija "Otvorena pitanja i preporučeni sledeći koraci": šta ostaje neodgovoreno
   (pitanja koja klijent nije odgovorio, terenska provera, interni podaci,
   verifikacija influensera pre outreach-a, opcioni plaćeni izveštaj o tržišnim
   udelima) i šta preporučujemo kao nastavak.

5. Odvojeno napravi VERZIJU ZA PREZENTACIJU: 10–12 slajdova (naslov + 3–5 bulleta po
   slajdu, bez sitnog teksta), sa predlogom šta ide na koji slajd — osnova za
   prezentaciju menadžmentu.

6. Na kraju predloži i kratak propratni email klijentu uz isporuku (šta dobijaju,
   šta je ostalo otvoreno, predlog termina za prezentaciju).

Format: kompletan tekstualni izveštaj (spreman za prebacivanje u Word/PDF) + odvojen
sažetak za prezentaciju + propratni email.
```

**Posle faze 9:** prebaciti u finalni format (Word/PDF; na claude.ai može direktno da se traži .docx fajl), interna revizija (pročitati očima klijenta), isporuka do 10.09.

---

## 13. PITANJA ZA KLIJENTA — poslati odmah posle faze 1

Kratka verzija (faza 1 će dati doteranu formulaciju):

1. Okvirni budžet lansiranja (red veličine)?
2. Gradovi i redosled širenja posle Beograda; broj objekata u godinama 1–3?
3. Politika akcija, popusta i loyalty programa (bilo „TBD")?
4. Da li je loyalty zaista deljen sa Belodore, s obzirom na različitu publiku?
5. Okvirni broj brendova u prvoj godini; postoje li već dogovori?
6. Potvrda: želite da vam mi predložimo idealne brendove (Q15)?
7. Interni Belodore podaci (prodaja, CRM, sajt) — može li se dobiti bilo šta?
8. Da li vas zanima plaćeni izveštaj o tržišnim udelima za Srbiju?
9. Interni rokovi: do kada postavka vizuelnog identiteta; do kada naručivanje
   asortimana; do kada zaključenje lokacije?
10. Muški kupci 15–19 — koliko računate na njih (Q25 prazno)?

> Istraživanje NE čeka odgovore. Ako stignu do faze 7, uključuju se u sintezu; ako ne,
> u finalnom izveštaju idu pod „otvorena pitanja".

---

## 14. ŠTA JE IZMENJENO U ODNOSU NA v1 (interna napomena)

1. **Dodat predlog brendova** (faza 2B + sinteza t. 10) — klijent ga je eksplicitno tražio u Q15, v1 ga nije imao.
2. **Dodata QA faza (8)** — fact-check pre slanja klijentu; izveštaj sa izmišljenim cenama/imenima je najveći rizik ovog pristupa.
3. **Faza 2 podeljena na 2A i 2B** — bila je preopterećena (konkurencija + cene + rang liste + makro u jednom promptu).
4. **Rešena kolizija paralelnog rada**: v1 je govorio da faze 2–6 mogu paralelno, a promptovi faza 5 i 6 su se pozivali na nalaze prethodnih. Sada: sve faze su samostalne uz KONTEKST BLOK; jedino faza 6 formalno zavisi od faze 3 (dobija njen rezime); ukrštanje nalaza radi se u sintezi.
5. **Uveden KONTEKST BLOK + Claude Project** umesto oslanjanja na „isti razgovor" (dugi razgovori gube kvalitet, a prekid je značio ručno prepričavanje).
6. **Svaka faza završava „REZIME ZA SINTEZU"** — standardizovan prenos nalaza u fazu 7.
7. **Dodati propusti iz upitnika**: sensory overload i pojednostavljenje discovery-ja (Q49/2), pokloni kao segment (Q26), zabavni nekomercijalni elementi (Q33), kupovna moć i način plaćanja tinejdžera (bitno za web shop), mini analiza TC Galerije.
8. **„Input za dizajn tim" objedinjen** u sintezi (t. 9) — v1 je boju, reči i ton ostavljao rasute po fazama, a klijentu je to isporuka br. 1.
9. **Influenseri pojačani**: pored tipologije, aktivna pretraga konkretnih regionalnih imena uz ogradu da se verifikuju pre outreach-a.
10. **Dodat vremenski plan sa datumima** (rok 11.09 + želja za ubrzanjem) i checklist svih 15 isporuka za proveru pre slanja.
11. **Faza 9 proširena**: appendix izvora, propratni email klijentu, eksplicitna zabrana uvođenja novih tvrdnji u kompajliranju.
12. U fazu 6 dodata ograda: publika su maloletnici — granice za „sexy/provokativno" ton i CRM ograničenja.

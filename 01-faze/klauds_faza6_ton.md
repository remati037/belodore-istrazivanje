# KLAUDS · Faza 6 — Ton komunikacije i jezik brenda

Datum izrade: 28.08.2026 · Autor: VladsDigital (istraživanje kroz Claude Code)
Status: radna verzija

> **Napomena o pouzdanosti:** uz svaki ključni nalaz stoji oznaka **VISOKA** (više
> nezavisnih izvora), **SREDNJA** (jedan solidan izvor ili posredan zaključak) ili
> **NISKA** (pretpostavka/ekstrapolacija). Podatak, interpretacija i preporuka su
> vizuelno odvojeni.

> **Ulaz u ovu fazu:** `02-rezimei/rezime-3.md` (Gen Z kupac) — pročitan i korišćen kao
> osnova; dopunski `rezime-4.md` (radnja, osoblje, zoniranje) i `rezime-5.md` (pet reči
> brenda: **PROBAJ · MOJE · KOMPLIMENT · ISKRENO · NOVO**, lista zabranjenih veza).
> Ova faza te reči **testira na izmerenom jeziku** i dve od njih menja status.

---

## 0. Šta je u ovoj fazi urađeno i kojom metodom

| Metod | Obim | Status |
|---|---|---|
| **Google Suggest / autocomplete** (`client=firefox&hl=sr&gl=rs`) | **69 upita**, fokusiranih isključivo na jezik, formate i sleng (ne na brendove kao u 2B, ne na motivaciju kao u 3) | ✅ |
| Prikupljanje doslovnih opisa objava (captions) domaćih trgovaca | Jasmin parfimerije, dm Srbija, Lilly Drogerie — objave nađene preko indeksa pretraživača | ✅ 7 doslovnih |
| Recenzirana i industrijska istraživanja o brend slengu | Tippie/*Journal of Marketing Research*, Princeton (n=195), dcdx (n=92), YouGov Profiles, Kantar | ✅ |
| Domaći rečnici slenga generacije Z | Mondo (20 pojmova), Nova.rs (18 pojmova) | ✅ |
| Pravni okvir oglašavanja prema maloletnicima | Zakon o oglašavanju RS — izvorni tekst sa parlament.gov.rs, izvučen i pročitan | ✅ |
| Podaci o dosegu kanala u Srbiji | DataReportal *Digital 2026: Serbia* (podaci okt. 2025) | ✅ |
| **TikTok komentari, Reddit, PunMiris — mašinski** | ponovo blokirani (prazan render / HTTP 403) | ❌ — vidi Ograničenja |

**Metodološka napomena o autocomplete-u.** Google Suggest rangira predloge po stvarnoj
učestalosti upita. On meri **šta ljudi kucaju**, ne šta gledaju i ne kako govore uživo.
Zato je odsustvo predloga za neki izraz dokaz da se **ne pretražuje**, a ne automatski
dokaz da se **ne koristi**. Gde je ta razlika bitna, eksplicitno je označena u tekstu.

---

## 1. Kako Gen Z u Srbiji stvarno govori o parfemima i beauty proizvodima

### 1.1 Glavni nalaz faze: pravilo koje razdvaja engleski koji prolazi od engleskog koji ne prolazi

**Nalaz.** Mešanje srpskog i engleskog kod ove kategorije **nije nasumično**. Izmereno
na 69 upita, engleske reči se dele u dve jasne grupe:

**(A) Engleski koji je već ušao u srpski i pretražuje se bez prevoda — to su NAZIVI STVARI:**

| Izraz | Dokaz iz autocomplete-a (`gl=rs`) |
|---|---|
| **body mist** | `body mist lilly` · `body mist dm` · `body mist victoria secret` · `body mist za muskarce` · `body mist manoard` · `body mist jk` · `body mist sa sljokicama` — bogat, komercijalan, domaći set |
| **layering** | prvi predlog za `layering` je **`layering parfema`** — ispred svih engleskih značenja |
| **dekant** | `dekant rs` · `dekant parfemi` · `dekanti parfema` · `parfemicar dekant` |
| **viralni** | `viralni parfemi` · `viralni parfem` · `viralni zara parfem` |
| **kopija** | `kopija parfema libre` · `... coco chanel mademoiselle` · `... bois imperial` · `... replica` · `... my way` · `... zara` · `... jimmy choo` |

**(B) Engleski koji NIJE ušao — to su NAZIVI FORMATA I OSEĆANJA. Ljudi ih ne kucaju, ili
kucaju da bi ih PREVELI:**

| Izraz | Šta autocomplete stvarno vraća |
|---|---|
| **GRWM** | `gremlin` · `gremlini` · `gremio` · `gemini` — jedini srodan predlog je `grwm dress to impress` (Roblox igra). **Nula veze sa beauty sadržajem.** |
| **haul** | `haul meaning` · `haul znacenje` · `haul prevod` — ljudi traže **prevod te reči** |
| **vajb / vibe** | `vajb znacenje`, a ostalo su **imena lokala** (`vajb kragujevac`, `vajb street food`, `vajbtike`). `vibe` autocorrect-uje u **`viber`** |
| **smellmaxxing** | isključivo upiti na engleskom: `meaning` · `reddit` · `trend` · `definition` · `explained` |
| **signature** | `signature parfem oriflame` · `... farmasi` — reč je u srpskom **zauzeta katalog/MLM prodajom** |
| **„parfem sa TikToka"** | **nula predloga** (potvrda nalaza iz Faze 3) |
| **„šta nosim" / „koji parfem nosiš"** | **nula predloga** u parfemskom kontekstu; `sta nosim` vodi na trudnoću |
| **dupe** | `dupeguru` · `dupence` · `dupelizac` — **u srpskom je vulgaran homograf** |

Pouzdanost: **VISOKA** · Izvor: [Google Suggest API (`hl=sr&gl=rs`), 69 upita, avgust 2026](https://suggestqueries.google.com/complete/search?client=firefox&hl=sr&gl=rs&q=grwm) · Provereno: 28.08.2026

> ### ⚑ PRAVILO KLAUDS JEZIKA — najoperativniji nalaz ove faze
>
> **Engleski se u KLAUDS copy-ju koristi samo kada imenuje STVAR koja nema srpski naziv
> (body mist, layering, dekant, EDP). Engleski se NIKADA ne koristi da imenuje OSEĆANJE,
> FORMAT ili REAKCIJU (vibe, haul, GRWM, slay, smellmaxxing, signature, dupe).**
>
> Razlog nije stilski nego merljiv: prvu grupu srpski kupac pretražuje, drugu prevodi.
> Brend koji koristi drugu grupu ne zvuči mlado — zvuči kao da ga treba prevesti.

**Interpretacija.** Ovo pravilo rešava klijentovo ograničenje („da ne zvuči kao da se
previše trudi") bez ijedne subjektivne procene. „Trudi se previše" u ovoj kategoriji
ima merljiv oblik: to je **upotreba engleskog za osećanje umesto za stvar.**

**Preporuka.** Ovo pravilo ide u brand book kao jedan red i primenjuje ga svaki
copywriter bez rasprave. Praktična provera pred objavu: *da li Srbin tu reč guglа da bi
je razumeo?* Ako da — reč ne ide u naslov.

---

### 1.2 Sedam konstrukcija koje srpski kupac stvarno koristi (i koje KLAUDS može da uzme doslovno)

**Nalaz.** Iz 69 upita izdvaja se sedam produktivnih rečeničnih obrazaca. Sve su
domaće, sve imaju volumen, nijedna nije marketinška.

| # | Konstrukcija | Dokaz | Šta je to za KLAUDS |
|---|---|---|---|
| 1 | **„miriše na ____"** | `parfem koji mirise na cisto / more / kokos / vanilu / kremu za suncanje / puder / bebi puder / tamjan / lipu / jasmin` | Oznaka na polici i filter u web shopu (već preporučeno u Fazi 3 i 4) |
| 2 | **„koji parfem koristi ____"** | `ceca` · `aleksandra prijovic` · `jelena karleusa` · `lepa brena` · `natasa bekvalac` · **`breskvica`** · `novak djokovic` · `rihanna` · `putin` | **Najjači neiskorišćen format sadržaja.** Domaća imena, ne globalna |
| 3 | **„koji dugo traje / koji traje ceo dan"** | `parfem koji traje` · `parfem koji traje cijeli dan` · `zenski parfem koji dugo traje` · `parfem koji najduze traje` | Obavezan podatak na etiketi, uz jačinu |
| 4 | **„____ ali jeftiniji" / „a dobar" / „kao skupi"** | `burberry goddess ali jeftiniji` (Faza 3) · `jeftin a dobar parfem` · `jeftini parfemi koji mirisu kao skupi` | Polica „sličan na…" i cenovni jezik |
| 5 | **„kopija parfema ____"** | 9 predloga sa konkretnim imenima originala | **Reč je `kopija`, ne `dupe`.** Kupac je već izgovara bez stida |
| 6 | **„parfem koji ostavlja trag"** | jedini predlog za `parfem koji ostavlja` | Gotova domaća fraza za posledicu — bez ijedne engleske reči |
| 7 | **„novo u ____"** | `novo u dm` · `novo u lidlu` · `novo u ikei` · `novo u pepcu` | Ustaljen srpski retail obrazac → **„NOVO U KLAUDS"** je već poznata forma |

Pouzdanost: **VISOKA** · Izvor: [Google Suggest API (`hl=sr&gl=rs`)](https://suggestqueries.google.com/complete/search?client=firefox&hl=sr&gl=rs&q=parfem+koji+koristi) · Provereno: 28.08.2026

**Interpretacija — dva iznenađenja.**

**Prvo: „koji parfem koristi [domaća zvezda]" je jedini format u kategoriji sa dokazanom
domaćom tražnjom, a nijedan trgovac ga sistematski ne uslužuje.** Imena u predlozima nisu
globalna — to su Ceca, Prijovićka, Karleuša, Bekvalac, **Breskvica** (pevačica koju sluša
tačno ciljna grupa), Brena, Đoković. Faza 3 je pokazala da tinejdžer ne pretražuje sebe
kao tinejdžera; ovde se vidi **kroz koga se pretražuje** — kroz ljude koje gleda.

**Drugo: reč koju kupac koristi za istu stvar je `kopija`, ne `dupe`.** Faza 5 je „dupe"
već stavila na listu reči koje se ne smeju vezati za brend; ova faza daje merljiv razlog
koji je jači od stilskog — **u srpskom je to vulgaran homograf.** Rizik nije da zvuči
neozbiljno, nego da postane predmet šale koju brend ne kontroliše.

**Preporuka.** Sedam konstrukcija iz tabele su **zatvorena lista dozvoljenih obrazaca za
naslove** u prvoj godini. Copywriter ne izmišlja osmi bez podatka koji ga opravdava.

---

### 1.3 Sleng koji stvarno kruži — i zašto ga brend ipak ne koristi

**Nalaz.** Domaći rečnici slenga generacije Z (dva nezavisna, objavljena u srpskim
medijima) daju sledeći korpus, transkribovan na srpski:

> **krindž** (nelagoda zbog tuđeg ponašanja) · **delulu** (nerealne nade) · **riz / rizler**
> (harizma, muvanje) · **slej** (fenomenalno) · **sigma** (samouveren muškarac) · **fleks /
> fleksovati se** (hvalisanje) · **mid** (osrednje) · **W** (pobeda) · **L** (poraz) · **POV** ·
> **sus** (sumnjivo) · **pik mi** (traži pažnju) · **gejtkipovati** (kriti informaciju) ·
> **sinovati** (pročitati bez odgovora) · **kraš** (simpatija) · **hajp** · **skibidi** ·
> **en-pi-si** · **digitalac** · **gaser** (pozer) · **citer** (varalica) · **spaljen** ·
> **japa** · **oldara / kidara / nubara** · **prenkovati** · **rešiti nekog**

Pouzdanost: **VISOKA** za postojanje korpusa (dva nezavisna domaća izvora), **NISKA** za
trajnost pojedinačnih reči · Izvori: [Mondo — Rečnik generacije Z](https://mondo.rs/Magazin/Stil/a2195954/sta-znace-reci-generacije-z.html); [Nova.rs — Rečnik izraza koje koriste današnji tinejdžeri](https://nova.rs/magazin/prica-se/recnik-izraza-koje-koriste-danasnji-tinejdzeri/) · Provereno: 28.08.2026

**Interpretacija — i ovo je najvažnija „ne radi" preporuka faze.** Postojanje ovog
korpusa **nije dozvola da ga brend koristi.** Tri nezavisna istraživanja to mere direktno
(detaljno u sekciji 2.3), a jedan detalj je presudan: **oba rečnika su objavljena u
medijima namenjenim RODITELJIMA** — kao prevodi. Reč koja je stigla do članka „šta vaše
dete pokušava da vam kaže" je reč koja je iz ciljne grupe već izašla.

**Preporuka.** KLAUDS ne piše ovim rečima. **Ali ih razume i prepoznaje u komentarima** —
razlika između brenda koji govori sleng i brenda koji ga razume je merljiva u odgovorima
na komentare, ne u objavama. Community manager sme da odgovori „W" na tuđe „W". Brend ne
sme prvi da napiše „W".

---

### 1.4 Formati: šta postoji na srpskom, a šta je uvezeno

**Nalaz.** Formati iz prompta („GRWM", „perfume collection", „koji parfem nosiš danas")
imaju **različit status na domaćem terenu**:

| Format | Status u srpskom | Dokaz |
|---|---|---|
| **„moja kolekcija parfema"** | ✅ **postoji kao domaća fraza** | `moja kolekcija parfema` · `kolekcija mini parfema` — direktni predlozi |
| **„rutina"** | ✅ postoji, u mešanom obliku | `moja rutina` · `moja skincare rutina` · `moja jutarnja rutina` |
| **preporuka** | ✅ jak, čisto srpski | `parfem preporuka` · `muski parfem preporuka` · `zenski parfem preporuka` |
| **recenzija** | ✅ jak, vezan za konkretna imena | `jk parfem recenzija` · `zorannah parfem recenzija` · `lattafa` · `9pm` · `delina` |
| **GRWM** | ❌ **nula prisustva** | vraća `gremlin`, `gremio` |
| **haul** | ❌ traži se prevod | `haul znacenje` · `haul prevod` |
| **„koji parfem nosiš danas"** | ⚠️ **nula u pretrazi, ali živ u govoru** | nema predloga; ali cela Faza 3 pokazuje da je to **pitanje koje ti drugi postave** |

Pouzdanost: **VISOKA** za pretragu · Izvor: [Google Suggest API](https://suggestqueries.google.com/complete/search?client=firefox&hl=sr&gl=rs&q=kolekcija+parfema) · Provereno: 28.08.2026

**Interpretacija.** Format se ne uvozi pod engleskim imenom — **uvozi se pod domaćim.**
Isti video koji na engleskom nosi naziv „GRWM" na srpskom se zove **„spremam se sa vama"**
ili se uopšte ne imenuje. Isti video koji je „perfume collection" zove se **„moja kolekcija
parfema"** — i ta fraza ima merljivu tražnju.

**„Koji parfem nosiš danas" je poseban slučaj i najvredniji.** Ne pretražuje se — jer to
niko ne gugla. **To je rečenica koju ti neko kaže.** Faza 3 je izmerila da je dominantan
trigger kupovine kompliment, a doslovni regionalni citat je „*Zaustave me na ulici i pitaju
koji parfem nosim*". To znači da je „koji parfem nosiš" **ishod, ne format** — i u copy-ju
mora da stoji u toj ulozi, kao ono što se tebi desi, a ne kao naslov rubrike.

**Preporuka — imena formata na srpskom, spremna za upotrebu:**

| Umesto | KLAUDS koristi |
|---|---|
| GRWM | **„Spremam se"** ili bez imena (video se ne mora imenovati) |
| Perfume collection / shelfie | **„Moja kolekcija"** · **„Šta mi stoji na polici"** |
| Haul | **„Šta sam uzela"** (ili bez imena) |
| Fragrance review | **„Iskreno o ____"** — vezuje se za reč ISKRENO iz Faze 5 |
| Fragrance of the day | **„Danas nosim"** |
| Dupe / clone | **„Kopija"** ili **„Sličan na ____"** |
| Smellmaxxing | ne prevoditi — **ne koristiti uopšte** |

---

## 2. Koji ton deluje zastarelo, a koji deluje forsirano

### 2.1 Zastarelo: „mirisna piramida" register — i on je u Srbiji još uvek standard

**Nalaz.** Domaći specijalizovani trgovci parfemima pišu opise u registru koji je
prepoznatljiv i doslovno merljiv. Autentični primeri sa srpskih prodajnih sajtova:

> „*Srce mirisa je zavodljivo, ali profinjeno, čineći parfem izuzetno privlačnim i
> elegantnim.*"
> „*Miris na koži ostaje topao, elegantan i zavodljiv.*"
> „*Kompozicija postaje punija, senzualnija i sofisticiranija, ističući ženstveni karakter
> parfema.*"
> „*Savršeno balansira između klasične elegancije i moderne zavodljivosti.*"
> „*Glava parfema (gornje note) je ono što osećate odmah nakon nanošenja… Srce parfema
> (srednje note) počinje da se razvija nakon oko 15 minuta…*"

Pouzdanost: **VISOKA** (doslovni tekst sa aktivnih prodajnih sajtova) · Izvori: [Originalni Parfemi — mirisne grupe i piramida](https://originalniparfemi.rs/mirisne-grupe/); [Originalni Parfemi — D&G The One for Men „Zavodljiv miris"](https://originalniparfemi.rs/proizvod/parfemi/muski-parfemi/dolce-gabbana-the-one-for-men-eau-de-toilette/); [Max Parfemi](https://maxparfemi.rs/product/paco-rabanne-1-million-prive-100ml/) · Provereno: 28.08.2026

**Interpretacija.** Ovaj registar ima četiri obeležja i sva četiri su za KLAUDS zabranjena:
1. **Vokabular odraslog zavođenja** — „zavodljiv", „senzualan", „ženstveni karakter".
2. **Anatomska metafora** — „glava", „srce", „baza" — traži pismenost koju kupac nema.
3. **Bezličnost** — nema ni „ti" ni „ja"; miris nešto radi sam od sebe.
4. **Nulta posledica** — nigde ne piše šta se **tebi** desi kad ga nosiš.

Faza 3 je izmerila da srpski kupac miris opisuje **referencama** (17 od 20 predloga nisu
note). Ovaj registar je time **jezik koji kupac ne koristi**, a koji zauzima celu policu.

---

### 2.2 Šta domaći trgovci danas stvarno pišu — izmereno na doslovnim objavama

**Nalaz.** Doslovni opisi objava (captions) sa naloga tri najveća domaća igrača:

**Jasmin parfimerije** (TikTok ~196K pratilaca, IG ~181K — najveći domaći nalog u kategoriji):
> „*Vreme je da obnoviš neseser sa šminkom! 😍 Šta ti je baš sad pri kraju? 🤔 Piši nam u
> komentarima! \*Akcija šminke traje do 21. juna u svim Jasmin parfimerijama i online
> prodavnici na jasmin.rs #JasminParfimerije #Šminka #Sniženje*"
>
> „*Ovo se ne propušta! ⏳ BLACKFRIDAY euforija je uveliko u jeku, a tebi ne preostaje ništa
> sem da požuriš! 🖤❤️*"
>
> „*Da Nova 2025a bude još srećnija, iskoristi HAPPY DAY popust (20%–50%) u svim Jasmin
> parfimerijama i online! 😍❄️*"
>
> „**Koliko parfema ste Vi znali?** *😄*" · „*Ovo je više savet momcima! A bliži se i Black
> Friday 🥰*"
>
> Slogan: „*Kad kažeš parfem, pomisliš Jasmin.*"

**dm Srbija** (TikTok ~168K):
> „*Koji je tvoj omiljeni parfem iz dm-a?*" — 12,3K lajkova, 23 komentara

**Lilly Drogerie** (IG ~355K):
> „*Atmosfera danas? 10/10! 🤩✨ Gužva nikad veća, a Jeremy Fragrance je još jednom pokazao
> zašto je svetska zvezda i izmamio osmehe svima. 💙🙌 #Manoard #LillyDrogerie*"

Pouzdanost: **VISOKA** (doslovni tekst objava) · Izvori: [TikTok @jasmin.parfimerije](https://www.tiktok.com/@jasmin.parfimerije); [objava — Black Friday](https://www.tiktok.com/@jasmin.parfimerije/video/7443064656526200119); [objava — šminka](https://www.tiktok.com/@jasmin.parfimerije/video/7649298601062960391); [TikTok @dm_srbija — „Koji je tvoj omiljeni parfem iz dm-a?"](https://www.tiktok.com/@dm_srbija/video/7307645010344791301); [TikTok @lilly_drogerie — Jeremy Fragrance](https://www.tiktok.com/@lilly_drogerie/video/7657281927568690452) · Provereno: 28.08.2026

**Interpretacija — tri konkretne slabosti koje KLAUDS može da napadne:**

**(a) Ton je promo, ne brend.** Kod Jasmina je gotovo svaka objava vezana za **popust,
rok ili hitnost** („ne propušta se", „požuri", „traje do", „euforija"). To je ton
**akcijskog letka prenetog na TikTok**. Nema ni jednog stava o mirisu.

**(b) Persona nije stabilna — „ti" i „Vi" se smenjuju u istom nalogu.** „*tebi ne preostaje
ništa*" i „*Koliko parfema ste **Vi** znali?*" su isti nalog. Za tinejdžera je „Vi" sa
velikim slovom signal da poruka **nije za njega**. dm je u tome dosledan („*Koji je **tvoj**
omiljeni parfem*") i to je njegova jedina, ali stvarna prednost u tonu.

**(c) Ekspertiza je iznajmljena, ne sopstvena.** Domaći trgovci autoritet uvoze —
Jasmin tagira **@Parfemičara** i domaće kreatore, Lilly dovodi **Jeremyja Fragrancea**.
Nijedan **nema sopstveni glas koji nešto tvrdi.**

**Preporuka.** Tri pravila koja iz ovoga slede direktno, i koja se mogu proveriti na
svakoj objavi pre nego što izađe:
1. **Najviše jedna od pet objava sme da bude o ceni ili akciji.** Ostale četiri imaju stav.
2. **„Ti" uvek, „Vi" nikad** — bez izuzetka, na svim kanalima, uključujući web shop i
   natpise u radnji. Jedini izuzetak je pisana korespondencija sa odraslim kupcem
   (reklamacija, poklon-porudžbina) — vidi 5.4.
3. **KLAUDS mora imati sopstveni glas koji nešto tvrdi** (npr. rang lista iz Faze 4), pa
   tek onda gosta. Trgovac koji ima samo goste nema ton.

---

### 2.3 Forsirano: tri nezavisna istraživanja mere da brend sleng ODMAŽE

Ovo je najbolje potkrepljen nalaz cele faze i direktno pokriva klijentovo ograničenje.

**Nalaz 1 — recenzirano, sa eksperimentima.** Studija sa Tippie College of Business
(Univerzitet Ajova), autori **Bryce Pyrah i Alice Wang**, naslov **„The Slang Paradox:
Connecting or Disconnecting with Consumers"**, prihvaćena za *Journal of Marketing Research*.
Metod: serija eksperimenata i onlajn anketa sa objavama brendova na društvenim mrežama,
sa slengom i bez njega (testirane reči: *rizz, slap, bae, bougie, pop off, ghost, lit,
understands the assignment*).

Izmereni rezultati:
- **Arizona Tea** je sa slengom dobila **manje lajkova i deljenja** nego bez njega;
- posle objava sa slengom ispitanici su bili **manje skloni da kupe ChapStick**;
- **skoro svi ispitanici su reagovali negativnije** na verziju sa slengom;
- **izuzetak: Monster** — kod već „edgy" brenda sleng **nije napravio razliku** (ni + ni −);
- **⚑ ključni izuzetak: sleng od INFLUENSERA prolazi.** „*Potrošači su bili popustljiviji
  prema slengu kada dolazi od influensera nego sa korporativnih naloga.*"

Doslovno, autor: „*More often than not, the use of slang backfires on the brand and they
lose credibility, unless they have a specific brand personality that fits the use of the
slang.*" Objašnjenje koje autori nude: **ljudi taj jezik doživljavaju kao svoj i zameraju
kompanijama što na njemu zarađuju.**

Pouzdanost: **VISOKA** · Izvori: [Tippie College of Business — „Bruh, using slang to vibe with consumers doesn't slap"](https://tippie.uiowa.edu/news/2025/04/bruh-using-slang-vibe-consumers-doesnt-slap); [Newswise — saopštenje](https://www.newswise.com/articles/bruh-using-slang-to-vibe-with-consumers-doesn-t-slap-for-brands) · Provereno: 28.08.2026

**Nalaz 2 — eksperiment na samoj Gen Z publici.** Princeton (Adele E. Goldberg, Grace H.
Yoo, 2025): *„It's Giving Slang: The Impact of Explicit Gen Z Authorship Acknowledgement
on Gen Z Perceptions of Brand Authenticity and Humor in TikTok Ads"*, **n = 195, svi
pripadnici Gen Z-a**. Svaki ispitanik gledao je jednu TikTok reklamu sa slengom i jednu
tradicionalnu bez slenga.

Izmereno: **tradicionalne reklame ocenjene su kao značajno AUTENTIČNIJE i kao da se
manje trude u humoru**, dok su TikTok reklame sa slengom ocenjene kao **zabavnije**. Nije
bilo razlike u pozitivnom stavu prema brendu ni u nameri angažovanja. Zaključak autora:
„*overt signaling of cultural alignment may backfire*".

Pouzdanost: **VISOKA** za nalaz, **SREDNJA** za prenosivost (SAD, mali uzorak) · Izvor: [Princeton — teze i disertacije](https://theses-dissertations.princeton.edu/entities/publication/cc6b5f2d-0918-43ad-ac34-de229d531169) · Provereno: 28.08.2026

**Nalaz 3 — jedna reč, jedan broj.** Posle zajedničke kampanje **Oreo i Coca-Cole
(avgust 2024)** u kojoj se dva brenda proglašavaju „besties", anketa platforme **dcdx**
na **92 pripadnika Gen Z-a** dala je: **85% opisuje brend koji koristi reč „bestie" kao
cringe.** Kampanja je inače ostvarila 75 miliona impresija.

Pouzdanost: **SREDNJA** (n=92, nije reprezentativan uzorak; sam izvor to naglašava) ·
Izvor: [Bakery&Snacks — Why internet slang can damage food and drink brands](https://www.bakeryandsnacks.com/Article/2026/08/21/why-internet-slang-can-damage-food-and-drink-brands/) · Provereno: 28.08.2026

**Interpretacija.** Tri nezavisne metode (eksperiment na brendovima, eksperiment na Gen Z
publici, anketa o jednoj reči) daju isti smer. **Za KLAUDS je presudan izuzetak sa
influenserima**, jer se spaja sa nalazom 11 iz Faze 3 (u Srbiji samo 2% potpuno veruje
influenserima):

> **Sleng je dozvoljen samo u ustima kreatora, nikad u ustima brenda. Ali kreatoru se
> u Srbiji ne veruje kao dokazu — veruje mu se kao podsticaju da se dođe i proba.** Zato
> je podela posla: **kreator nosi jezik, KLAUDS nosi tvrdnju.**

---

### 2.4 Ko je pogodio — i zašto to nije zbog tona

**Nalaz.** Najcitiraniji primeri brendova koji su „pogodili" mladu publiku:

| Brend | Rezultat | Šta je stvarno bio mehanizam |
|---|---|---|
| **Duolingo** | 16+ mil. pratilaca na TikToku; DAU sa 4,9 mil. (2021) na 80+ mil.; engagement 19–21% ≈ 10× prosek kategorije | **Specifičan lik, ne ton.** Sova je pretnja, ali vezana isključivo za učenje jezika — „*threatening but not mean, obsessed with language learning specifically, not generically weird*" |
| **e.l.f. Cosmetics** | prvi TikTok hashtag challenge preko 1 mlrd pregleda; #eyeslipsface 7,7 mlrd; ~90% potpomognute prepoznatljivosti (2024) | **Sopstvena imovina** (pesma, ime brenda kao refren), ne pozajmljen sleng |
| **Liquid Death** | — | **Doslednost kroz godine**, apsurd kao stalni identitet, ne kao kampanja |
| **Field Roast** | — | Sleng vezan **direktno za proizvod**, a ne za publiku |

Pouzdanost: **SREDNJA** (izvori su marketinški case study-ji i medijski prikazi, ne recenzirana istraživanja; brojke su samoprijavljene ili sekundarne) · Izvori: [NoGood — Duolingo Social Media Strategy](https://nogood.io/blog/duolingo-social-media-strategy/); [Fullintel — Duolingo case study](https://fullintel.com/blog/how-duolingos-duo-became-the-internets-favorite-marketing-genius/); [Campaign US — „Eyes, Lips, Face": How e.l.f. built its brand on TikTok](https://www.campaignlive.com/article/%E2%80%9Ceyes-lips-face%E2%80%9D-elf-cosmetics-built-its-brand-tiktok/1699297); [Shorty Awards — e.l.f. Cosmetics' Innovation on TikTok](https://shortyawards.com/13th/elf-cosmetics-innovation-on-tiktok) · Provereno: 28.08.2026

**Interpretacija — i ovo je najvažnija ograda cele faze.** Sva četiri primera su
**vlasnički**, ne pozajmljeni. Nijedan nije uspeo tako što je preuzeo tuđi jezik. Doslovno
zapažanje iz analize Duolinga: *„Desetine brendova su probale 'unhinged' glas na TikToku i
većina je sramotna. Razlika nije u tonu — nego u izvedbi i infrastrukturi oko njega."*

**Preporuka.** Klijentu treba jasno reći: **ton se ne kopira.** Ako KLAUDS želi glas koji
se pamti, mora imati **jednu sopstvenu stvar** koja postoji samo kod njega — a Faza 4 je tu
stvar već predložila: **istinita rang lista** koju konkurent ne može da kopira jer nema te
podatke. To, a ne sleng, je „glas".

---

### 2.5 Šta su promašaji naučili — tri obrasca

| Kampanja | Šta se desilo | Pravilo za KLAUDS |
|---|---|---|
| **Oreo × Coca-Cola „besties" (2024)** | 85% Gen Z-a označilo reč kao cringe | Reč koja je stigla do dva korporativna brenda **istekla je** |
| **Gatorade, sleng (2025)** | Dvosmislenost i igra rečima podelile publiku | **Igra rečima na jeziku koji nije tvoj = nekontrolisan rizik.** U srpskom je najkonkretniji primer **„dupe"** |
| **American Eagle „Great Genes" (2025)** | Dosetka u kontekstu tela i izgleda izazvala nelagodu | **Telo mlade osobe nije materijal za dosetku.** Za KLAUDS (publika 15–19) ovo je i zakonsko ograničenje — sekcija 3.3 |

Pouzdanost: **SREDNJA** (medijski i strukovni pregledi) · Izvori: [Boderia — 10 Failed Marketing Campaigns of 2025](https://www.boderia.io/insights/10-failed-marketing-campaigns-of-2025-revealed); [Creativepool — Top 5 Biggest Campaign Flops of 2025](https://creativepool.com/magazine/features/the-top-5-biggest-campaign-flops-of-2025.34051) · Provereno: 28.08.2026

**Napomena o regionalnim primerima.** **Nije pronađen nijedan dokumentovan slučaj domaćeg
ili regionalnog brenda koji je javno „pao" na forsiranom mladalačkom tonu.** To ne znači da
ih nema — znači da domaća struka takve slučajeve ne dokumentuje. Zapisano u Ograničenja.

---

## 3. Gde KLAUDS stoji na spektru tona

### 3.1 Predlog: 55 / 25 / 15 / 5, sa jednim isključenim poljem

**Preporuka (interpretacija, ne merenje).** KLAUDS nije jedno mesto na spektru nego
**odnos četiri sastojka**, u svakoj poruci:

| Sastojak | Udeo | Zašto baš toliko — vezano za nalaz |
|---|---|---|
| **ISKRENO / DIREKTNO** (osnovni registar) | **55%** | Faza 3: kupac sam spaja cenu i kvalitet („a dobri", „ali jeftiniji", „kao skupi"). YouGov: 62% Gen Z-a iskrenost smatra „vrlo važnom", poverenje 61%, doslednost između reči i dela 56%. Vodeći domaći kanal (**Parfemičar**) se pozicionira upravo rečju „*iskrene recenzije*" — reč je slobodna, ali je **već dokazana kao valuta u ovoj kategoriji** |
| **PLAYFUL** (način izvedbe) | **25%** | Kantar: za Gen Z **muzika**, a ne humor, najjače podiže prijemčivost za reklamu — dok je humor najjači kod Gen X i boomera. Playful se zato radi **tempom, muzikom i montažom**, a ne dosetkom u tekstu |
| **EDUKATIVNO** (na ulaznom nivou) | **15%** | Faza 3: `mist za telo šta je` je stvaran upit. Ova faza dodaje: `haul znacenje`, `layering meaning`, `vajb znacenje`, `aura parfema znacenje` — **ljudi ne razumeju ni reči kojima im se prodaje** |
| **EKSPERTSKO** (na zahtev, nikad prvo) | **5%** | Mirisna piramida ostaje — sitnim slogom, ispod. Faza 4: note ostaju na etiketi, nikad kao naziv zone |
| **PREMIUM** | **0% u jeziku** | Premium se u KLAUDS-u vidi u materijalu, ambalaži, boji i osvetljenju — **nikad u rečniku.** Faza 4: sukob „radnja za tinejdžere" vs. „odrasli koji plaća" rešava se **metrima, vazduhom i zvukom, ne tonom** |
| **SEXY / PROVOKATIVNO** | **ISKLJUČENO** | Zakonska zabrana + kategorijalni rizik — sekcija 3.3 |

**Interpretacija.** Ovaj odnos svesno **ne stavlja humor u centar.** To je namerno i
suprotno očekivanju: podatak koji se najčešće citira („Gen Z voli smešne reklame") kod
Kantara se za Gen Z **ne potvrđuje kao najjači faktor** — muzika ga pobeđuje. Uz to,
humor je najbrži put u „previše se trudi", tj. tačno u ono što je klijent zabranio.

Pouzdanost: **SREDNJA** za predloženi odnos (izvedeno), **VISOKA** za pojedinačne nalaze
na kojima počiva · Izvori: [YouGov Profiles — What America's Gen Z really wants from brands](https://yougov.com/en-us/articles/53409-gen-z-wants-from-brands-values-ethics-authenticity) (SAD, odrasli 18+, prikupljano nov. 2024 – nov. 2025); [Kantar — How to get humour right in advertising](https://www.kantar.com/uki/inspiration/advertising-media/how-to-get-humour-right-in-advertising); [eMarketer — Humor and music are the way to get Gen Z's attention](https://www.emarketer.com/content/humor-music-way-gen-z-s-attention) · Provereno: 28.08.2026

---

### 3.2 Reč koja treba da nosi ton: PROBAJ — i ona je izmereno već prva

**Nalaz.** Faza 5 je predložila pet reči za KLAUDS: **PROBAJ · MOJE · KOMPLIMENT ·
ISKRENO · NOVO.** Ova faza ih je testirala na autocomplete-u i rezultat menja njihov redosled:

| Reč | Šta autocomplete pokazuje | Status posle testa |
|---|---|---|
| **PROBAJ** | prvi predlog za `probaj` je **`probaj parfem`**, ispred svih drugih značenja; postoji i `probaj besplatno` | ✅ **potvrđena i unapređena u prvu reč** — najjača kolokacija sa „parfem" u srpskom |
| **NOVO** | `novo u dm` · `novo u lidlu` · `novo u ikei` — ustaljen retail obrazac | ✅ potvrđena; koristi se **isključivo u formi „NOVO U KLAUDS"** |
| **KOMPLIMENT** | `komplimenti za devojku` · `... za muskarca` · `... za izgled` — reč je živa | ⚠️ **potvrđena kao reč, ali sa pravnim ograničenjem u upotrebi** — sekcija 3.3 |
| **ISKRENO** | `iskreno na engleskom`, ostalo tekstovi pesama — **neutralno u pretrazi**, ali je pozicija vodećeg domaćeg kanala | ✅ zadržati; nosi ga **ponašanje** (istinita rang lista, otvorena cena), ne slogan |
| **MOJE** | u parfemskom kontekstu potvrđeno kroz **`moja kolekcija parfema`** | ✅ potvrđena, u obliku **„moja kolekcija"** |

Pouzdanost: **VISOKA** za autocomplete, **SREDNJA** za zaključak o redosledu · Izvor: [Google Suggest API](https://suggestqueries.google.com/complete/search?client=firefox&hl=sr&gl=rs&q=probaj) · Provereno: 28.08.2026

> ⚠️ **Provera pre upotrebe:** u predlozima se pojavljuje i **`probaj parfem.rs`**, što
> ukazuje da je neko u Srbiji već koristio taj naziv (domen na dan provere ne odgovara —
> `ENOTFOUND`). **Pre nego što se PROBAJ stavi u slogan ili domen, obavezna je provera
> žiga u Zavodu za intelektualnu svojinu.** Ovo je zadatak za klijentovog pravnika, ne za
> istraživanje.

---

### 3.3 ⚠️ Granice: publika su maloletnici i to je ZAKONSKO, ne samo etičko pitanje

> **Ovo nije pravno mišljenje.** Pravno savetovanje je van obima ovog istraživanja
> (CLAUDE.md, sekcija „VAN OBIMA"). Ovde se navode odredbe zakona koje **direktno diktiraju
> ton** i koje su izvučene iz izvornog teksta. **Pre lansiranja bilo koje kampanje
> potrebno je mišljenje advokata.**

**Nalaz.** Zakon o oglašavanju RS („Sl. glasnik RS" br. 6/2016, 52/2019) definiše:
**dete = lice mlađe od 12 godina; maloletnik = lice od 12 do 18 godina** (čl. 21, st. 6–7).
**Cela primarna ciljna grupa KLAUDS-a (15–19) je najvećim delom u kategoriji „maloletnik".**

Četiri odredbe koje direktno pogađaju ton KLAUDS-a, doslovno:

**(1) Čl. 10, tač. 4 — zabranjeno je** „*prikazivanje maloletnika u vezi sa seksualnošću,
kao i muškaraca i žena kao dečaka ili devojčica sa seksualnim odlikama odraslih*".
Uz čl. 10, tač. 3: zabranjeno je i „*seksualno uznemiravanje, prikazano kao prihvatljivo,
poželjno ili uobičajeno društveno ponašanje*".

**(2) Čl. 21, st. 1, tač. 2 — oglasna poruka ne sme da** „*neposredno poziva decu ili
maloletnike na kupovinu roba ili usluga ili da ih poziva da to zahtevaju od svojih
roditelja*"; tač. 4: ne sme da ih „*neposredno podstiče na kupovinu… zloupotrebom njihovog
neiskustva i lakovernosti*"; tač. 5: ne sme da „*zloupotrebljava posebno poverenje koje
deca i maloletnici imaju u roditelje, nastavnike ili druga lica*".

**(3) Čl. 23, st. 6 — oglasna poruka namenjena maloletnicima** „*ne sme, uz podatak o ceni,
sadržati još i vrednosni sud o ceni, a naročito reči 'samo', 'sitnica', 'povoljno' i sl.*"

**(4) ⚑ Čl. 25, st. 3 — oglasna poruka namenjena maloletnicima** „*ne sme da sugeriše da
će korišćenjem robe ili usluge steći fizičke, intelektualne ili druge društvene prednosti
nad ostalim maloletnicima, odnosno da će nekorišćenje robe ili usluge imati suprotno
dejstvo*".

Kazne za nepridržavanje: **300.000 do 2.000.000 RSD.**

Pouzdanost: **VISOKA** (izvorni tekst zakona, mašinski izvučen iz PDF-a Narodne skupštine i unakrsno proveren) · Izvori: [Narodna skupština RS — Zakon o oglašavanju, izvorni tekst (PDF)](http://www.parlament.gov.rs/upload/archive/files/lat/pdf/zakoni/2016/2926-15%20lat.pdf); [Paragraf Lex — Zakon o oglašavanju (prečišćen tekst)](https://www.paragraf.rs/propisi/zakon_o_oglasavanju.html); [RTV — Zakon o oglašavanju štiti decu i maloletnike](https://rtv.rs/sr_lat/zivot/porodica/zakon-o-oglasavanju-stiti-decu-i-maloletnike_914953.html) · Provereno: 28.08.2026

#### 3.3.1 Dva sudara sa nalazima iz prethodnih faza — i kako se rešavaju

Ovo su, po oceni ovog istraživanja, **dve najozbiljnije stavke cele faze**, jer pogađaju
tačno one preporuke koje su iz Faze 3 izašle kao najjače.

> ### ⚠️ SUDAR 1 — „kompliment" kao obećanje vs. čl. 25, st. 3
>
> **Faza 3 (nalaz 2, VISOKA):** tinejdžer ne kupuje miris, kupuje **reakciju okoline**;
> svaki opis proizvoda treba da ima socijalnu posledicu.
> **Zakon:** poruka namenjena maloletnicima ne sme da sugeriše da će kupac steći
> **društvene prednosti nad ostalim maloletnicima.**
>
> Copy tipa „**Budi ta koju primete**", „**Svi će te pitati šta nosiš**", „**Onaj koga
> pamte**" je **obećanje društvene prednosti nad vršnjacima** — tj. tačno ono što odredba
> pominje.
>
> **Rešenje — pomeranje lica i vremena, bez gubitka snage poruke:**
>
> | Oblik | Ko govori | Vreme | Status |
> |---|---|---|---|
> | „Budi ta koju primete." | **brend** | budućnost | ❌ obećanje prednosti |
> | „Sa ovim ćeš dobiti komplimente." | **brend** | budućnost | ❌ obećanje prednosti |
> | „*Najčešći komentar na ovaj: 'stalno me pitaju šta nosim'.*" | **kupac** (citat) | prošlost | ✅ **preneta činjenica** |
> | „*Ovaj je 3. na listi po tome koliko puta su nam ljudi rekli da ih neko zaustavio.*" | **podatak** | prošlost | ✅ **merenje** |
>
> **Princip: KLAUDS ne obećava reakciju — KLAUDS je meri i objavljuje.** To je istovremeno
> pravno mnogo bezbednije, i **jače** — jer se poklapa sa rečju ISKRENO i sa mehanikom
> istinite rang liste iz Faze 4. Konkurent obećanje može da kopira za jedan dan; merenje
> ne može, jer nema podatke.

> ### ⚠️ SUDAR 2 — otvorenost o ceni vs. čl. 23, st. 6
>
> **Faza 3 (interpretacija):** „*Cena se pominje otvoreno i bez stida… Brend koji o ceni
> ćuti zvuči kao da nešto krije.*"
> **Zakon:** uz cenu se maloletnicima ne sme dodati vrednosni sud — **naročito reči
> „samo", „sitnica", „povoljno" i slično.**
>
> Ovo NIJE sudar nego **potvrda, sa jednom izmenom u izvedbi.** Otvorenost o ceni ostaje;
> **pridev uz cenu odlazi.**
>
> | ❌ | ✅ |
> |---|---|
> | „Samo 1.190 din!" | „1.190 din." |
> | „Povoljno — 990 din" | „990 din · 30 ml · traje 6–8 h" |
> | „Nikad jeftinije!" | „Bilo 1.490 → sad 1.190 din" |
>
> **Gola cena je istovremeno i zakonski bezbedna i tonski tačnija** — pridev uz cenu je
> upravo ono što Jasminov ton (2.2) čini akcijskim letkom. **Ovde se pravna obaveza i
> brend strategija poklapaju u potpunosti.**

#### 3.3.2 „Sexy / provokativno" — gde je granica, konkretno

**Preporuka.** Za KLAUDS **isključeno**, i to iz tri nezavisna razloga:

1. **Zakonski** (čl. 10, tač. 4) — maloletnik se ne sme dovoditi u vezu sa seksualnošću.
2. **Kategorijalno** — u srpskom parfemskom sadržaju taj registar **postoji i zauzet je**:
   autocomplete daje `parfem koji privlaci muskarce` i `koji parfemi imaju feromone`, a
   domaći YouTube sadržaj ide do naslova poput „*PARFEMI ZA MUVANJE I ZAVOĐENJE*". To je
   **teritorija kreatora i teritorija odraslih**, i KLAUDS na njoj nema šta da traži.
3. **Poslovno** — Faza 3 (arhetip D) pokazuje da **20% prometa čini odrasli koji plaća**,
   od čega deo kupuje poklon tinejdžeru. Roditelj koji vidi taj registar ne kupuje.

**Gde je onda granica, praktično:** KLAUDS sme da govori o **privlačnosti kao posledici
koju drugi primete** („*pitaju te šta nosiš*"), a ne o **privlačnosti kao seksualnoj
ponudi** („*da te požele*", „*feromoni*", „*za muvanje*", „*ne mogu da ti odole*").
Prvo je socijalno, drugo je seksualno. **Test u jednoj rečenici: da li bi ovu rečenicu
napisao roditelju šesnaestogodišnjakinje uz njeno ime? Ako ne — ne ide.**

---

## 4. Note ili situacije — i zašto je odgovor „ni jedno ni drugo, nego referenca"

### 4.1 Nalaz koji koriguje uobičajenu pretpostavku

**Nalaz.** Pitanje je postavljeno kao izbor između **nota** (klasično) i **situacija**
(bliže Gen Z-u). Merenje na srpskom autocomplete-u pokazuje da **„situacija" u zapadnom
smislu u Srbiji NEMA tražnju** — dok referenca i sezona imaju.

| Tip okvira | Upit | Rezultat |
|---|---|---|
| **REFERENCA** | `parfem koji mirise na …` | **10 predloga**, bogato i stabilno |
| **SEZONA** | `parfem za leto` / `parfem za zimu` | **10 + 6 predloga**, uključujući `parfem za leto 2026`, `manoard parfem za leto`, `arapski parfem za leto` |
| **REŽIM** | `parfem za svaki dan` · `parfem za teretanu` | **4 + 2 predloga** |
| **POSLEDICA** | `parfem koji traje` / `parfem koji ostavlja trag` | **6 + 1 predlog** |
| **SITUACIJA** | `parfem za izlazak` | **NULA predloga** |
| **SITUACIJA** | `parfem za maturu` | **NULA predloga** |
| **SITUACIJA** | `parfem za skolu` | **NULA predloga** |
| **SITUACIJA** | `parfem za fakultet` | **NULA predloga** |
| **NOTA** | `parfem od vanile` · `parfem od kokosa` · `parfem od lipe` · `parfem od ruze` | predlozi postoje, ali su **imenovane sirovine, ne mirisne porodice** |

Kontrolna provera: okvir „prilika" u srpskom **postoji za odeću** (`sta da obucem za
svadbu / za rodjendan / za slavu / za skolu`), **ali ne za parfem.** Dakle nije u pitanju
odsustvo okvira u jeziku — nego to da se **parfem u Srbiji ne bira po prilici.**

Pouzdanost: **VISOKA** · Izvor: [Google Suggest API (`hl=sr&gl=rs`), 16 upita o okvirima](https://suggestqueries.google.com/complete/search?client=firefox&hl=sr&gl=rs&q=parfem+za+leto) · Provereno: 28.08.2026

**Interpretacija.** Preporuka „situacije umesto nota" je **tačna u smeru, ali pogrešna u
sadržaju za srpsko tržište.** Gen Z zaista ne kupuje po notama — ali ne kupuje ni po
prilikama („date night", „office", „party"), što je zapadni obrazac. Kupuje po
**referenci** („na šta ovo liči") i po **sezoni** („kad se ovo nosi").

Postoji i tanak, ali stvaran trag da nota **nije mrtva** — upit `zorannah parfem note`
postoji. Znači: **notu traži onaj ko je već kupio ili se odlučio** i sad hoće detalj.
To je tačno mesto gde nota pripada — **posle odluke, ne pre nje.**

---

### 4.2 Preporučeni model: četiri sloja, uvek istim redom

**Preporuka.** Jedan hijerarhijski model koji važi **istovremeno** za policu, etiketu,
web shop filter i copy — tako da kupac na sva četiri mesta sreće isti redosled:

| Sloj | Šta piše | Gde je vidljiv | Veličina sloga |
|---|---|---|---|
| **1 · REFERENCA** | „miriše na **čisto**" · „na **more**" · „na **kokos i leto**" · „na **vanilu i slatko**" · „na **sapun**" · „na **puder**" · „na **kremu za sunčanje**" | oznaka zone, glavni filter, prvi red opisa | **najveći** |
| **2 · POSLEDICA** | „traje **6–8 h**" · „**oseti se**" / „**samo za tebe**" (jačina) · citat kupca | odmah ispod reference | veliki |
| **3 · SEZONA / REŽIM** | „**za leto**" · „**za zimu**" · „**za svaki dan**" · „**za teretanu**" | drugi filter, ikonica na etiketi | srednji |
| **4 · NOTE** | mirisna piramida, klasično | **poslednji red, sitno**; u web shopu iza „vidi još" | **najmanji** |

**Ovo je hibridni model iz prompta, ali sa ispravljenim drugim slojem:** umesto
„situacije" stoji **posledica + sezona**, jer su te dve merljive u domaćoj pretrazi, a
situacija nije.

**Šta ovo znači operativno:**
- Zone u radnji nose **imena po referenci** (potvrda Faze 4: „mirisne porodice ostaju na
  etiketi, nikad kao naziv zone");
- **Sezona je jedini legitiman razlog za rotaciju zida** — i istovremeno odgovor na uslov
  „nešto se menja svake nedelje" iz Faze 5, bez izmišljanja povoda;
- **Note ostaju** i to je važno za arhetip C (istraživač, 18–19) i za odrasle. Ne brišu se
  — **spuštaju se za jedan nivo.**

---

## 5. Razlike po kanalima

### 5.0 Polazni podatak: koliki je koji kanal u Srbiji

**Nalaz.** DataReportal *Digital 2026: Serbia* (podaci oktobar 2025):

| Kanal | Doseg u Srbiji | Napomena |
|---|---|---|
| YouTube | 4,83 mil. (72,3% populacije) | najveći |
| **Instagram** | **3,40 mil. (50,9%)** | **veći od TikToka u apsolutnom broju** |
| Facebook | 3,25 mil. (48,7%) | van ciljne grupe |
| **TikTok** | **2,98 mil. — ali samo 18+** | **13–17 se uopšte ne prikazuje** u oglasnim alatima |
| Snapchat | 1,76 mil. (26,4%) | najmlađa struktura, neistražen kanal |
| Viber | ~3,5 mil. korisnika u Srbiji | stopa otvaranja poruka do ~90% |
| Internet ukupno | 6,13 mil. (91,8%) | — |

Pouzdanost: **VISOKA** za DataReportal (izvor: oglasni alati Meta, Google, TikTok, Snap), **SREDNJA** za Viber (izvori su domaće agencije, ne nezavisno merenje) · Izvori: [DataReportal — Digital 2026: Serbia](https://datareportal.com/reports/digital-2026-serbia); [SpotLight — Viber marketing](https://spotlight.rs/viber-marketing/); [Native Media — Viber marketing: kompletan vodič](https://nativemedia.rs/blog/viber-marketinga-kompletan-vodic/) · Provereno: 28.08.2026

**Interpretacija — ispravka česte pretpostavke.** „TikTok je kanal za mlade, Instagram za
starije" **ne stoji za Srbiju** kad se gleda doseg: Instagram ima veći apsolutni doseg.
Ali **TikTokov broj isključuje uzrast 13–17 — dakle najveći deo primarne ciljne grupe
uopšte nije u toj cifri.** Iz toga sledi jasna podela: **TikTok je kanal otkrivanja koji
se ne može precizno meriti oglasno za maloletnike; Instagram je kanal dosega i zajednice
koji se meri.** Nijedan ne zamenjuje drugi.

> **Rupa:** starosna struktura po platformi za Srbiju nije javno dostupna. Jedini domaći
> podatak koji je pronađen (CKPS, n=700) je iz **2021.** i navodi TikTok na 6,6% — što je
> danas očigledno zastarelo i **ne sme se koristiti.** Zapisano u Ograničenja.

---

### 5.1 Pregled svih kanala

| Kanal | ULOGA | TON | FORMAT | Ko govori | Čega tu NEMA |
|---|---|---|---|---|---|
| **TikTok** | **otkrivanje** — ulaz u levak | najopušteniji; tempo i muzika nose energiju, ne tekst | rang liste, poređenja, „**koji parfem koristi ____**", kopija vs. original, kratka „šta je" objašnjenja | **kreator češće od brenda** (Tippie: slengu se prašta kod influensera, ne kod korporativnih naloga) | cene kao glavna poruka; slogan; poziv na kupovinu |
| **Instagram** | **doseg + zajednica + arhiva** | isti glas, uredniji; ovde se brend „drži" | karusel-liste, sezonske rotacije, **repost kupaca**, „NOVO U KLAUDS" | brend, sopstvenim glasom | „estetika radi estetike"; stok fotografije |
| **Web shop** | **odluka i pretraga** | najfunkcionalniji; **jezik = jezik pretrage** | filteri po **referenci** i **sezoni**; „sličan na ____"; note sitno, iza „vidi još" | brend, kratkim rečenicama | mirisna piramida u prvom redu; „zavodljiv/senzualan"; opis bez cene |
| **CRM · Viber** | **podsetnik, retko** | kratko, bez emocije, **nikad hitnost** | „stiglo je ono što si čuvala" · „subota, 12h, radionica" | brend, službeno-prijateljski | ⚠️ **poziv na kupovinu** (čl. 21) i **pridev uz cenu** (čl. 23) |
| **CRM · email** | **dubina, za odrasle i 18+** | najsmireniji od svih | poklon vodiči (decembar), novi brendovi, wishlist podsetnik | brend | tinejdžerski registar — ovde su odrasli |
| **Radnja · natpisi** | **navigacija i dozvola** | **kupčeve reči, doslovno** | oznake zona po referenci; „šta je ____" u jednoj rečenici; cena gola | prostor | „Vi"; struka; „Mogu li da Vam pomognem?" |
| **Radnja · osoblje** | **potvrda, ne savet** | „ti"; kratko; **dva režima** | „dva koraka i dva minuta" (Faza 4); prilazak tek na signal | čovek | prodajni pritisak; mirisna piramida na uvod |

---

### 5.2 TikTok — pravilo podele posla

**Preporuka.** Iz Tippie nalaza (sleng prolazi kod influensera, pada kod brendova) i
Faze 3 (u Srbiji samo 2% potpuno veruje influenserima) sledi **podela koja rešava oba
ograničenja odjednom:**

> **Kreator nosi JEZIK. KLAUDS nosi TVRDNJU.**
>
> - Kreator sme da priča kako priča — svojim slengom, svojim tempom. To je njegov posao i
>   to mu publika prašta.
> - KLAUDS na svom nalogu **ne imitira taj jezik.** On donosi ono što kreator nema:
>   **rang listu, poređenje, cenu, broj.**
> - **KPI influencer saradnje nije prodaja preko koda nego dolazak i testiranje** (Faza 3,
>   nalaz 11) — pa i brief kreatoru glasi „*dođi i probaj*", a ne „*preporuči*".

**Napomena o mikro-kreatorima.** Faza 3 preporučuje 10–15 mikro-kreatora uzrasta 17–24.
Ovde se dodaje **pravno upozorenje**: saradnja sa kreatorom **mlađim od 18** povlači i
pitanje saglasnosti roditelja i pitanje čl. 21 (poruka ne sme neposredno pozivati
maloletnike na kupovinu). **Praktična preporuka: ugovorni kreatori 18+; mlađi od 18 samo
kao organski UGC koji brend deli, a ne plaća.** Proveriti sa pravnikom.

---

### 5.3 Web shop — jezik filtera je već izmeren

**Preporuka.** Filteri se pišu **doslovno rečima iz pretrage**, ne kategorijama iz
industrije:

| ❌ Industrijska kategorija | ✅ KLAUDS filter (izmerena fraza) |
|---|---|
| Sveži / citrusni | **miriše na čisto** · **na more** |
| Gurmandski | **na vanilu i slatko** · **na kokos** |
| Pudrasti | **na puder** · **na bebi puder** |
| Orijentalni | **na tamjan** |
| Solarni | **na kremu za sunčanje** · **na leto** |
| Sapunasti | **na sapun** |
| Postojanost | **koliko traje** (u satima, brojem) |
| Sillage / projekcija | **koliko se oseti** (troslojno: samo za tebe / za sto / za sobu) |
| Cena | **cena** — gola, bez prideva |
| Dupes | **sličan na ____** |
| Discovery set | **probaj pre nego što kupiš** (5 ml) |

**Napomena.** Ova tabela je gotov brief za dizajnera web shopa i može se preuzeti u
celini. Sve leve kolone su industrijske; sve desne su izmerene u srpskom autocomplete-u
(Faza 3 + Faza 6).

---

### 5.4 ⚠️ CRM — najosetljiviji kanal, i on ima dva odvojena ograničenja

**Nalaz — ograničenje 1 (pristanak).** Faza 5 je utvrdila: po ZZPL, **maloletnik sa
navršenih 15 godina može sam dati pristanak** za obradu podataka u korišćenju usluga
informacionog društva; **ispod 15 traži se roditeljski pristanak koji rukovalac mora da
proveri.** Otud preporuka: **donja granica loyalty programa je 15 godina**, uz wishlist
bez naloga i poklon karticu za mlađe.

**Nalaz — ograničenje 2 (sadržaj poruke), novo u ovoj fazi.** Pristanak rešava **da li**
sme da se pošalje. **Ne rešava ŠTA sme da piše.** Čl. 21 Zakona o oglašavanju važi za
svaku oglasnu poruku namenjenu maloletniku — uključujući **Viber poruku i newsletter.**
Dakle: **CRM poruka maloletniku ne sme da bude neposredan poziv na kupovinu, niti da ga
poziva da to zahteva od roditelja.**

Pouzdanost: **VISOKA** za odredbe · Izvori: [Zakon o oglašavanju, čl. 21](http://www.parlament.gov.rs/upload/archive/files/lat/pdf/zakoni/2016/2926-15%20lat.pdf); [Paragraf Lex — Zakon o zaštiti podataka o ličnosti](https://www.paragraf.rs/propisi/zakon_o_zastiti_podataka_o_licnosti.html) · Provereno: 28.08.2026

**Preporuka — CRM se piše u INFORMATIVNOM, ne u prodajnom modu.** Razlika je merljiva u
glagolu:

| ❌ prodajni mod (rizičan) | ✅ informativni mod |
|---|---|
| „Kupi sad, akcija ističe!" | „Ovo je ponovo na polici." |
| „Traži od mame za rođendan 🎁" | „Wishlist ti je spreman za deljenje." |
| „Samo danas −30%!" | „Cena do 15.09: 1.190 din." |
| „Ne propusti!" | „Subota, 12h. Ima mesta za 12 ljudi." |

**Segmentacija CRM baze je obavezna od prvog dana, i nije marketinška nego pravna:**

| Segment | Kanal | Ton | Šta sme |
|---|---|---|---|
| **15–17** (sopstveni pristanak) | Viber, retko; app notifikacija | informativni mod, „ti" | dostupnost, događaj, wishlist, loyalty stanje |
| **18+** | Viber + email | informativni mod, „ti" | + kampanje, + poziv na kupovinu |
| **Odrasli platilac (arhetip D)** | email | smiren, „ti" ali odrasliji | poklon vodiči, decembar, poklon kartica |
| **Ispod 15** | **nema CRM-a** | — | samo wishlist bez naloga + poklon kartica |

**Frekvencija.** Viber ima do ~90% stope otvaranja u Srbiji, što je istovremeno njegova
vrednost i njegov rizik: kanal koji se **uvek** otvori je kanal koji se **brzo blokira**.
Predlog: **maksimum 2 Viber poruke mesečno za segment 15–17**, i to samo kada postoji
stvaran povod (stiglo/događaj/wishlist). Email do 4 mesečno za 18+ i odrasle. *(NISKA
pouzdanost — ovo je radna preporuka bez domaćeg benchmark-a; kalibrisati na sopstvenim
podacima o odjavi posle prva tri meseca.)*

---

### 5.5 Radnja — natpis je copy, i to najčitaniji copy koji brend ima

**Preporuka.** Faza 4 je definisala ponašanje osoblja („dva koraka i dva minuta", nikad
„Mogu li da Vam pomognem?"). Ovde se dodaje **jezik natpisa**, po tipu:

| Tip natpisa | ❌ | ✅ |
|---|---|---|
| **Oznaka zone** | „Orijentalni mirisi" | „**MIRIŠE NA VANILU I SLATKO**" |
| **Dozvola** | „Molimo ne otvarati testere" | „**Sve na ovoj polici sme da se proba.**" |
| **Objašnjenje** | „Body mist — mirisna maglica za telo" | „**Body mist = lakši i jeftiniji od parfema. Traje kraće, prska se više.**" |
| **Cena** | „Akcija! samo 990" | „**990 din · 30 ml · traje 4–6 h**" |
| **Rang lista** | „Preporučujemo" | „**TOP 10 kod momaka ovog meseca. Merili smo, nismo birali.**" |
| **Granica** | „Ograničenje 3 komada" | „**Nos izdrži 3–4 mirisa. Posle toga ništa ne miriše. Vidimo se za 5 minuta.**" |

**Interpretacija.** Poslednji red je najvažniji i vezuje se za nalaz iz Faze 4 (zrna kafe
ne resetuju nos; jedino pauza od 2–5 minuta pomaže; praktična granica je 3–4 parfema).
**Radnja koja to kaže naglas zvuči iskreno i istovremeno rešava operativni problem** —
to je jedan natpis koji radi dva posla.

---

## 6. Konkretni primeri: 10 fraza, hook-ova i formata

> Svaki primer je vezan za izmeren jezik ili za nalaz iz prethodne faze. Nijedan ne koristi
> engleski za osećanje. Nijedan ne obećava društvenu prednost. Svi su testirani na oba
> pravna sudara iz sekcije 3.3.

**1 · „Miriše na čisto."**
*Format:* oznaka zone, naslov objave, filter.
*Zašto:* prvi predlog za `parfemi koji` u srpskom. Tri reči, nijedna stručna.

**2 · „Koji parfem koristi ____?"**
*Format:* serijal na TikToku i Instagramu; domaća imena (Breskvica, Prijovićka, Đoković,
Karleuša), pa **KLAUDS-ova ponuda najbližeg mirisa i njegova cena.**
*Zašto:* izmerena tražnja sa **devet različitih imena** u autocomplete-u; **nijedan trgovac
u Srbiji ovaj format ne uslužuje sistematski.**
*Ograda:* ne tvrditi da neka osoba koristi konkretan parfem bez javnog izvora; format je
„*ovo se najviše traži — evo šta mi imamo blizu toga*", ne „*Ceca nosi ovo*".

**3 · „Sličan na ____. Nije isti. Evo u čemu se razlikuje."**
*Format:* etiketa na polici + kratak video.
*Zašto:* `burberry goddess ali jeftiniji`, `kopija parfema …` (9 predloga). **Treća
rečenica je ono što niko drugi ne kaže** — i ona je razlog zašto ovo zvuči iskreno umesto
kao izgovor.

**4 · „Probaj pre nego što kupiš. 5 ml, ____ din."**
*Format:* naziv dekant/discovery ponude.
*Zašto:* `probaj parfem` je prvi predlog za `probaj`; `dekant` ima trajan volumen od 2023;
78% Gen Z-a počinje mini formatom (Faza 3). **Reč PROBAJ je izmereno najjača.**

**5 · „Traje 6–8 h. Oseti se za sto, ne za sobu."**
*Format:* obavezan drugi red na svakoj etiketi i svakoj stranici proizvoda.
*Zašto:* `parfem koji traje` / `koji dugo traju` — kriterijum ugrađen u sam upit.
Troslojna skala jačine („samo za tebe / za sto / za sobu") pretvara `sillage` u srpski.

**6 · „NOVO U KLAUDS: ____"**
*Format:* nedeljna rubrika, isti dan, isti format, uvek.
*Zašto:* `novo u dm` / `novo u lidlu` / `novo u ikei` — gotov domaći retail obrazac. Uz to
ispunjava uslov iz Faze 5 („*nešto se menja svake nedelje*") **bez izmišljanja povoda.**

**7 · „Moja kolekcija: 6 mirisa, ukupno ____ din."**
*Format:* UGC serijal sa kupcima; kupac pokazuje svoju policu.
*Zašto:* `moja kolekcija parfema` je izmerena fraza; Gen Z gradi kolekciju od 5–12 mirisa
(Faza 3). Ukupna cifra otvara temu cene **bez prideva** — dakle bezbedno po čl. 23.

**8 · „TOP 10 kod momaka ovog meseca. Merili smo, nismo birali."**
*Format:* mesečna rang lista, u radnji i onlajn.
*Zašto:* Faza 3 — momci traže rang listu umesto kustosiranja; Faza 4 — istinita lista je
najjeftinija stvar koju konkurent ne može da kopira. Druga rečenica je cela pozicija
brenda u četiri reči.
*Pravno:* ovo je **merenje**, ne obećanje prednosti — prolazi test čl. 25.

**9 · „Nos izdrži 3–4 mirisa. Posle toga ništa ne miriše. Vidimo se za 5 minuta."**
*Format:* natpis kod test stanice; može i kao kratak video.
*Zašto:* Faza 4 — dokazano da zrna kafe ne rade, jedina stvarna mera je pauza. **Brend koji
kaže „stani" umesto „probaj još" gradi tačno onu reputaciju koju reč ISKRENO traži.**

**10 · „Šta je body mist? Lakši i jeftiniji od parfema. Traje kraće, prska se više. To je sve."**
*Format:* natpis + jedan video, ponavljati sezonski.
*Zašto:* `mist za telo šta je` je stvaran upit (Faza 3); `body mist` je izmereno prihvaćen
naziv, a `mist` sam po sebi ne znači ništa u srpskom. **„To je sve" je tonski potpis** —
signal da nema nastavka prodajnog govora.

> **Bonus format za decembar (arhetip D1):** „**Ako ti neko kupuje poklon, ovo mu pošalji.**"
> — wishlist kao QR kartica koju tinejdžer prosleđuje. Faza 3: treća poklon situacija
> („tinejdžer traži da mu se kupi") **danas nije uslužena ni kod jednog trgovca u Srbiji**.
> *Pravna ograda:* poruka **ne sme** glasiti „*traži od mame*" (čl. 21, st. 1, tač. 2).
> Formulacija mora ostati u informativnom modu: „*Wishlist ti je spreman za deljenje.*"

---

## 7. VODIČ TONA — „OVAKO DA / OVAKO NE"

> **Ovo je isporuka koja ide direktno dizajn timu i copywriterima.** Svaki par je ista
> poruka napisana pogrešno i ispravno. Levu kolonu **ne ispravljati po osećaju** — svaki
> red ima razlog naveden u trećoj koloni.

### 7.1 Opis proizvoda i police

| ❌ OVAKO NE | ✅ OVAKO DA | Zašto |
|---|---|---|
| „Zavodljiva orijentalna kompozicija čije srce krije vanilu i amber." | „Miriše na vanilu i nešto toplo. Traje 6–8 h." | Registar zavođenja + piramida; kupac pretražuje referencu (17/20 predloga) |
| „Senzualan miris koji ističe tvoju ženstvenost." | „Slatko, ali ne teško. Za zimu." | „Senzualno/ženstveno" je jezik odraslog zavođenja; publika su maloletnici (čl. 10) |
| „Gurmand za prave poznavaoce." | „Miriše na karamelu. Ako voliš slatko — ovaj." | „Gurmand" i „poznavalac" traže pismenost koju kupac nema |
| „Ekskluzivan niche miris." | „Nema ga nigde drugde u Srbiji. Zato košta više." | „Ekskluzivan" je tvrdnja; druga verzija je **provera koju kupac može da uradi** |
| „Idealan za posebne prilike." | „Za leto." / „Za svaki dan." | `parfem za izlazak` = 0 predloga; `parfem za leto` = 10 predloga |
| „Dupe za Baccarat Rouge." | „Sličan na Baccarat Rouge. Nije isti — evo u čemu." | **„Dupe" je vulgaran homograf u srpskom**; „kopija/sličan" je kupčeva reč |

### 7.2 Cena i ponuda

| ❌ OVAKO NE | ✅ OVAKO DA | Zašto |
|---|---|---|
| „Samo 990 din!" | „990 din · 30 ml" | **Čl. 23, st. 6** — zabranjen vrednosni sud uz cenu |
| „Neverovatno povoljno!" | „Bilo 1.490 → sad 1.190 din." | Isto + brojem se dokazuje ono što se pridevom samo tvrdi |
| „Ne propusti! Akcija ističe!" | „Cena do 15.09." | Hitnost je Jasminov registar; datum kaže isto bez pritiska |
| „Luksuz koji možeš da priuštiš." | „Cena je ovde jer je boca manja, ne zato što je miris lošiji." | „Luksuz koji možeš da priuštiš" je fraza koja kupca podseća da nema para |
| „Kvalitet po najboljoj ceni." | „Ovaj je najjeftiniji u ovoj polici. Traje najkraće. Zato je najjeftiniji." | ISKRENO je ponašanje, ne pridev |

### 7.3 Obraćanje i persona

| ❌ OVAKO NE | ✅ OVAKO DA | Zašto |
|---|---|---|
| „Koliko parfema **ste Vi** znali?" | „Koliko **si** ih pogodio?" | Doslovan primer sa domaćeg naloga (2.2); „Vi" tinejdžeru signalizira da poruka nije za njega |
| „Poštovani kupci, obaveštavamo Vas…" | „Stiglo je." | Isto |
| „Mogu li da Vam pomognem?" | *(ćutanje 2 minuta, pa:)* „Reci ako hoćeš nešto da probaš." | Faza 4 — motiv dolaska je potvrda, ne savet |
| „Naš stručni tim preporučuje…" | „Ovo je 3. na listi ovog meseca." | Autoritet iz podatka, ne iz titule |

### 7.4 Mladalački ton — gde je granica „previše se trudi"

| ❌ OVAKO NE | ✅ OVAKO DA | Zašto |
|---|---|---|
| „Ovaj miris je totalni **slay** ✨💅" | „Ovaj se najbrže prodaje. Treći put ga naručujemo." | **Tippie/JMR:** sleng sa korporativnog naloga obara kredibilitet |
| „**GRWM**: spremi se sa nama!" | „Spremam se. 3 minuta." | `grwm` u srpskoj pretrazi vraća `gremlin` |
| „**Haul** iz KLAUDS-a 🛍️" | „Šta sam uzela za 2.500 din." | `haul` se u Srbiji **prevodi**, ne koristi |
| „Uhvati **vajb** leta ☀️" | „Miriše na kremu za sunčanje." | `vajb` u srpskoj pretrazi vodi na **Viber i imena lokala** |
| „Bestie, ovaj ti je must have!" | „Ako ti se svideo ____, probaj ovaj." | dcdx: 85% Gen Z-a „bestie" od brenda smatra cringe |
| „**Smellmaxxing** season je počeo 🔥" | „Momci, top 10 ovog meseca." | `smellmaxxing` se u Srbiji traži **na engleskom, radi definicije** |
| „POV: ušla si u KLAUDS 💗" | *(bez teksta — samo snimak i muzika)* | Kantar: kod Gen Z-a **muzika** nadmašuje humor; Princeton: eksplicitno signaliziranje pripadnosti **smanjuje** doživljaj autentičnosti |

### 7.5 Obećanja i posledice (pravna zona)

| ❌ OVAKO NE | ✅ OVAKO DA | Zašto |
|---|---|---|
| „Budi ta koju primete." | „Najčešći komentar na ovaj: *'stalno me pitaju šta nosim'*." | **Čl. 25, st. 3** — zabranjeno sugerisati društvenu prednost nad vršnjacima |
| „Svi će te pitati šta nosiš." | „Ovaj je 3. po tome koliko puta su nam ljudi to rekli." | Isto — obećanje → merenje |
| „Bez ovog nisi spremna za maturu." | „Za maturu obično uzimaju ova tri." | **Čl. 25, st. 3** — zabranjena i sugestija suprotnog dejstva ako se ne kupi |
| „Traži od mame za rođendan 🎁" | „Wishlist ti je spreman za deljenje." | **Čl. 21, st. 1, tač. 2** — zabranjen poziv da se traži od roditelja |
| „Kupi sad!" *(poruka ka 15–17)* | „Ovo je ponovo na polici." | Isto — zabranjen neposredan poziv maloletniku na kupovinu |
| „Parfem koji te niko neće odbiti." | „Miriše na sveže oprano." | **Čl. 10, tač. 4** — maloletnik se ne dovodi u vezu sa seksualnošću |
| „Za muvanje i zavođenje." | *(ne postoji ispravna verzija — tema ne ide)* | Isto; postojeći domaći sadržaj tog tipa je teritorija kreatora, ne brenda |

### 7.6 Tri pravila koja hvataju ostalo

1. **Test prevoda.** Ako Srbin tu reč gugla da bi je razumeo — ne ide u naslov.
   *(Pada: GRWM, haul, vajb, smellmaxxing, signature, slay.)*
2. **Test lica i vremena.** Da li brend obećava budućnost, ili prenosi prošlost?
   Obećanje → prepiši kao citat kupca ili kao merenje.
3. **Test roditelja.** Da li bi ovu rečenicu napisao roditelju šesnaestogodišnjakinje uz
   njeno ime? Ako ne — ne ide.

---

## 8. Ograničenja i rupe u podacima

| Rupa | Zašto postoji | Šta to znači za pouzdanost | Kako se zatvara |
|---|---|---|---|
| **1. TikTok komentari, Reddit i PunMiris ponovo nisu mašinski dostupni** (prazan render / HTTP 403 / blokiran JSON) | Platforme blokiraju automatsko čitanje — **isto kao u Fazi 3** | **Doslovni korpus srpskih komentara i dalje NIJE prikupljen.** Ova faza ga je zaobišla merenjem pretrage i doslovnim captionima trgovaca — što je jače za *jezik kupovine*, ali ne pokriva *jezik razgovora* | **Ručno, ~4 sata:** 100–150 komentara sa 10–15 srpskih TikTok objava + 3–5 tema sa PunMirisa. **Ovo je i dalje otvoreno i sada je jedini nezatvoren ulaz u ovu fazu** |
| **2. Autocomplete meri kucanje, ne govor** | Priroda metode | Odsustvo predloga (npr. `koji parfem nosiš`) dokazuje da se **ne pretražuje**, ne da se **ne govori** | Isto kao rupa 1 — korpus komentara |
| **3. Nema dokumentovanih regionalnih promašaja tona** | Domaća struka ne objavljuje analize neuspelih kampanja | Sekcija 2.5 stoji **isključivo na globalnim primerima**; prenosivost je pretpostavka | Razgovor sa 2–3 domaće agencije, ili prihvatiti kao ograničenje |
| **4. Starosna struktura po platformi za Srbiju nije javna** | TikTok oglasni alati ne prikazuju 13–17 | **Ne može se reći koliki deo ciljne grupe je na kom kanalu.** Sekcija 5.0 daje ukupan doseg, ne strukturu | Sopstveni podaci posle lansiranja; ili anketa (ista ona iz Faze 3, 800–1.500 €) |
| **5. Jedini domaći podatak o mrežama (CKPS, n=700) je iz 2021.** i navodi TikTok na 6,6% | Zastarelo | **Ne koristiti ga.** Naveden samo da bi se znalo da je proveren i odbačen | Isto kao rupa 4 |
| **6. Rečnici slenga su medijski, ne lingvistički** | Nema akademskog korpusa srpskog omladinskog slenga | Korpus u 1.3 je **VISOKA za postojanje, NISKA za trajnost** | Nije potrebno zatvarati — preporuka je ionako da se sleng ne koristi |
| **7. Pravni deo nije pravno mišljenje** | Van obima istraživanja | Odredbe su citirane iz izvornog teksta i tačne, ali **primena na konkretan copy je stvar advokata** | **Obavezno: mišljenje advokata pre prve kampanje.** Naročito na sudare iz 3.3.1 |
| **8. Podela 55/25/15/5 je izvedena, ne merena** | Nema testa na domaćoj publici | **SREDNJA** | A/B test naslova na Instagram oglasima u prva tri meseca — jeftino |
| **9. Naziv „PROBAJ" možda nije slobodan** | `probaj parfem.rs` se pojavljuje u autocomplete-u; domen na dan provere ne odgovara | Rizik za slogan/domen, ne za reč u copy-ju | **Provera žiga u Zavodu za intelektualnu svojinu** pre upotrebe u nazivu |
| **10. Frekvencija CRM poruka (2/mes) je radna pretpostavka** | Nema domaćeg benchmark-a za Viber ka maloletnicima | **NISKA** | Kalibrisati na sopstvenoj stopi odjave posle 3 meseca |

---

## 9. Otvorena pitanja za klijenta (dopuna `05-klijent/`)

1. **Prihvata li se pravilo „Ti" uvek, „Vi" nikad** — uključujući i komunikaciju sa
   odraslim kupcem u radnji i u web shopu? (Ovo je jedina odluka iz faze koja se posle
   otvaranja teško menja, jer ulazi u natpise i u sistem.)
2. **Ko pravno proverava copy pre kampanja?** Sudari iz 3.3.1 (čl. 25 st. 3 i čl. 23 st. 6)
   traže mišljenje pre, ne posle.
3. **Prihvata li se da KLAUDS ne obećava komplimente nego ih meri?** To znači da radnja i
   web shop moraju **prikupljati** te podatke od prvog dana (jedno polje u recenziji).
4. **Ko piše? Jedan glas ili agencija po kanalu?** Duolingo/e.l.f. nalaz kaže da doslednost
   glasa nosi više od pojedinačne objave. Preporuka: **jedan copywriter za sve kanale u
   prvoj godini**, ne po kanalu.
5. **Da li se ide na ugovorne kreatore isključivo 18+?** (Pravno čistije; gubi se nešto
   autentičnosti kod 15–17.)
6. **Prihvata li se da najviše 1 od 5 objava bude o ceni/akciji?** Ovo je direktan otklon
   od domaće prakse i verovatno će naići na otpor iz prodaje.
7. **Je li „PROBAJ" slobodan kao žig?** Zadatak za pravnika pre nego što uđe u naziv.

---

## REZIME ZA SINTEZU

> Ovaj rezime je ulaz za Fazu 7. Piše se tako da bude razumljiv nekome ko NIJE čitao pun
> dokument. Kopija: `02-rezimei/rezime-6.md`.

1. **Postoji merljivo pravilo koje razdvaja engleski koji prolazi od engleskog koji ne
   prolazi: engleski se koristi za IME STVARI (body mist, layering, dekant), nikada za
   IME OSEĆANJA ILI FORMATA (vibe, haul, GRWM, slay, smellmaxxing).** Dokaz: `layering`
   u srpskom autocomplete-u odmah daje `layering parfema`, dok `haul` daje `haul znacenje`
   i `haul prevod`, a `grwm` daje `gremlin`. **„Previše se trudi" ima merljiv oblik — to je
   engleski upotrebljen za osećanje.** — *(VISOKA)*
2. **Tri nezavisna istraživanja mere da brend sleng ODMAŽE, uz jedan izuzetak koji
   određuje celu strategiju.** Tippie/*Journal of Marketing Research* („The Slang Paradox"):
   Arizona Tea je sa slengom dobila **manje** lajkova, ChapStick **manju** nameru kupovine;
   Princeton (n=195, svi Gen Z): tradicionalne reklame ocenjene kao **autentičnije**;
   dcdx (n=92): **85%** smatra da je „bestie" od brenda cringe. **Izuzetak: slengu se prašta
   kod influensera, ne kod korporativnih naloga.** — *(VISOKA za prva dva, SREDNJA za treći)*
3. **Otud podela posla: KREATOR NOSI JEZIK, KLAUDS NOSI TVRDNJU.** Kreator priča kako
   priča; KLAUDS na svom nalogu donosi ono što kreator nema — rang listu, poređenje, cenu,
   broj. Spojeno sa nalazom iz Faze 3 (u Srbiji samo 2% potpuno veruje influenserima), KPI
   saradnje ostaje **dolazak i testiranje**, ne prodaja preko koda. — *(VISOKA)*
4. **⚠️ Zakon o oglašavanju, čl. 25, st. 3 zabranjuje da poruka namenjena maloletnicima
   sugeriše društvene prednosti nad vršnjacima — što direktno pogađa najjači nalaz Faze 3
   („kupuje se kompliment").** Rešenje ne oslabljuje poruku nego je pojačava: **KLAUDS ne
   obećava reakciju, nego je meri i objavljuje.** „Budi ta koju primete" ❌ → „*Najčešći
   komentar na ovaj: 'stalno me pitaju šta nosim'*" ✅. Obećanje konkurent kopira za dan;
   merenje ne može. — *(VISOKA za odredbu, SREDNJA za predloženo rešenje — traži advokata)*
5. **⚠️ Čl. 23, st. 6 zabranjuje vrednosni sud uz cenu prema maloletnicima — doslovno reči
   „samo", „sitnica", „povoljno".** Ovo se poklapa sa preporukom iz Faze 3 o otvorenoj
   ceni: **cena ostaje vidljiva, pridev odlazi.** „Samo 990!" ❌ → „990 din · 30 ml" ✅.
   Pravna obaveza i brend strategija se ovde potpuno poklapaju. — *(VISOKA)*
6. **„Sexy/provokativno" je za KLAUDS isključeno iz tri nezavisna razloga:** zakonskog
   (čl. 10, tač. 4 — maloletnik se ne dovodi u vezu sa seksualnošću), kategorijalnog (taj
   registar u srpskom parfemskom sadržaju već postoji i pripada kreatorima — `parfem koji
   privlaci muskarce`, `feromoni`, „za muvanje i zavođenje") i poslovnog (20% prometa je
   odrasli platilac). **Granica: privlačnost kao posledica koju drugi primete — da;
   privlačnost kao seksualna ponuda — ne.** — *(VISOKA)*
7. **Odgovor na „note vs. situacije" je treći: REFERENCA.** Izmereno: `parfem za izlazak`,
   `parfem za maturu`, `parfem za skolu`, `parfem za fakultet` daju **NULA predloga**, dok
   `parfem koji mirise na …` daje 10 i `parfem za leto/zimu` daje 16. **Situacija u
   zapadnom smislu u Srbiji nema tražnju.** Preporučeni redosled na polici, etiketi, filteru
   i u copy-ju: **REFERENCA → POSLEDICA (koliko traje, koliko se oseti) → SEZONA → NOTE
   (sitno, poslednje).** — *(VISOKA)*
8. **Sedam domaćih konstrukcija sa dokazanim volumenom čine zatvorenu listu dozvoljenih
   naslova:** „miriše na ___", „**koji parfem koristi ___**", „koji dugo traje", „___ ali
   jeftiniji / a dobar / kao skupi", „**kopija** parfema ___", „parfem koji ostavlja trag",
   „**novo u** ___". — *(VISOKA)*
9. **„Koji parfem koristi [domaća zvezda]" je najjači neiskorišćen format u kategoriji.**
   Autocomplete daje devet imena — Ceca, Aleksandra Prijović, Jelena Karleuša, Nataša
   Bekvalac, **Breskvica**, Lepa Brena, Đoković, Rihanna. **Imena su domaća, ne globalna, i
   nijedan trgovac u Srbiji taj format ne uslužuje sistematski.** — *(VISOKA)*
10. **Reč koju kupac koristi je „kopija", a „dupe" je u srpskom vulgaran homograf**
    (autocomplete: `dupeguru`, `dupence`, `dupelizac`). Faza 5 je „dupe" već zabranila iz
    stilskih razloga; sada postoji jači, merljiv razlog. — *(VISOKA)*
11. **Test pet reči iz Faze 5 menja im redosled: PROBAJ je izmereno prva.** Prvi predlog za
    `probaj` u srpskom je **`probaj parfem`**, ispred svih drugih značenja te reči. NOVO je
    potvrđeno kroz obrazac `novo u dm / lidlu / ikei` → **„NOVO U KLAUDS"**. MOJE kroz
    `moja kolekcija parfema`. **⚠️ Pre upotrebe PROBAJ u sloganu ili domenu obavezna je
    provera žiga** — u autocomplete-u postoji trag `probaj parfem.rs`. — *(VISOKA)*
12. **Domaći trgovci imaju promo ton, ne brend ton — i to je merljiva praznina.** Doslovne
    objave Jasmina (najveći nalog, 196K) gotovo redom vezuju se za popust i hitnost
    („*Ovo se ne propušta! ⏳ … tebi ne preostaje ništa sem da požuriš!*"), a **persona im
    nije stabilna — „ti" i „Vi" se smenjuju u istom nalogu.** dm je jedini dosledan („*Koji
    je tvoj omiljeni parfem iz dm-a?*"). **Nijedan nema sopstveni glas koji nešto tvrdi —
    autoritet uvoze (Parfemičar, Jeremy Fragrance).** — *(VISOKA)*
13. **Predložena podela tona: 55% ISKRENO/DIREKTNO · 25% PLAYFUL · 15% EDUKATIVNO · 5%
    EKSPERTSKO · 0% PREMIUM U JEZIKU.** Humor namerno nije u centru: Kantar meri da je kod
    Gen Z-a **muzika**, a ne humor, najjači faktor prijemčivosti — humor je najjači kod Gen
    X i boomera. Playful se zato izvodi **tempom i muzikom, ne dosetkom u tekstu.**
    Premium se vidi u materijalu i boji, nikad u rečniku (Faza 4: sukob tinejdžer/odrasli
    rešava se metrima, ne tonom). — *(SREDNJA za odnos, VISOKA za pojedinačne nalaze)*
14. **U Srbiji Instagram ima veći doseg od TikToka (3,40 mil. vs 2,98 mil.), ali TikTokov
    broj ne obuhvata uzrast 13–17 — dakle najveći deo primarne ciljne grupe.** Podela:
    **TikTok = otkrivanje (nemerljivo oglasno za maloletnike), Instagram = doseg, zajednica
    i arhiva (merljivo).** Nijedan ne zamenjuje drugi. — *(VISOKA za brojke, SREDNJA za podelu)*
15. **CRM ima DVA odvojena ograničenja, ne jedno.** ZZPL (Faza 5) rešava **da li** sme da
    se šalje — granica je 15 godina. Čl. 21 Zakona o oglašavanju rešava **šta sme da piše**
    — poruka maloletniku ne sme biti neposredan poziv na kupovinu ni poziv da to traži od
    roditelja. **Zato se CRM piše u informativnom, ne prodajnom modu:** „Kupi sad!" ❌ →
    „Ovo je ponovo na polici." ✅; „Traži od mame" ❌ → „Wishlist ti je spreman za deljenje."
    ✅. Baza se segmentira na 15–17 / 18+ / odrasli **od prvog dana, iz pravnih razloga.** — *(VISOKA)*

---

## Tri stvari koje ovo menja za KLAUDS

- **Ton se ne bira estetski nego se izvodi iz dve merljive stvari: jezika pretrage i
  zakona.** Klijentovo ograničenje („da ne zvuči kao da se previše trudi") ima od sada
  operativan test — *test prevoda*: ako Srbin reč gugla da bi je razumeo, ne ide u naslov.
  A klijentov najjači nalaz („kupuje se kompliment") ima pravnu granicu koja ga **ne ruši
  nego preusmerava sa obećanja na merenje.** Oba testa staju u jedan red brand booka i ne
  traže ukus da bi se primenili.

- **Najveća tonska prilika u Srbiji nije da se govori mlađe, nego da se uopšte progovori.**
  Izmereno na doslovnim objavama: najveći domaći nalog u kategoriji (196K) piše akcijski
  letak, sa nestabilnim obraćanjem („ti" i „Vi" u istom nalogu), i autoritet iznajmljuje
  od kreatora. **Prazno mesto nije „mladalački ton" — prazno mesto je BILO KAKAV
  sopstveni stav.** KLAUDS ga dobija najjeftinijom mogućom imovinom: istinitom rang listom
  i rečenicom „*merili smo, nismo birali*".

- **Format sadržaja koji ovo istraživanje nalazi (i koji niko u Srbiji ne radi) vredi
  koliko i cela strategija tona.** „Koji parfem koristi ___" ima devet domaćih imena u
  autocomplete-u, spaja se sa policom „sličan na…" i sa dekantom iz Faze 3, i ne traži
  nijednu englesku reč, nijedno obećanje i nijedan dinar produkcije preko snimka telefonom.
  **To je jedini format u ovom dokumentu koji istovremeno rešava jezik, sadržaj i razlog
  za dolazak.**

---

*Kraj Faze 6. Sledeći korak: Faza 7 (strateška sinteza) — ulazi `02-rezimei/rezime-2a.md`
do `rezime-6.md`. Pre Faze 8 zatvoriti rupu 1 (ručno prikupljanje korpusa komentara) i
rupu 7 (mišljenje advokata na sudare iz 3.3.1).*

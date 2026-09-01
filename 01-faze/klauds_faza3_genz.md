# KLAUDS · Faza 3 — Gen Z kupac: ponašanje i motivacija

Datum izrade: 28.08.2026 · Autor: VladsDigital (istraživanje kroz Claude Code)
Status: radna verzija

> Napomena o pouzdanosti: uz svaki ključni nalaz stoji oznaka **VISOKA** (više
> nezavisnih izvora), **SREDNJA** (jedan solidan izvor ili posredan zaključak) ili
> **NISKA** (pretpostavka/ekstrapolacija). Interpretacije i preporuke su vizuelno
> odvojene od podataka.

---

## 0. Šta je u ovoj fazi novo i kako je rađeno

Ova faza se **nadovezuje na Fazu 2B**, ne ponavlja je. Iz 2B se preuzimaju kao već
utvrđeni ulazi: rang liste brendova, cene viralnih artikala, demografija 15–19
(497.864 osobe, 227.192 srednjoškolca, 73,5% van Beogradskog regiona), podaci o
onlajn kupovini Gen Z-a u Srbiji i odsustvo javnog podatka o džeparcu.

Tri nove metode korišćene ovde:

| Metoda | Šta daje | Status |
|---|---|---|
| **Google Trends, geo=RS** | Prvi put u projektu **uspešno povučen** (u Fazi 2B je vraćao HTTP 429). Krive interesovanja 2019–2026 za 20+ pojmova i brendova. | ✅ **rupa iz Faze 2B zatvorena** |
| **Google Suggest / autocomplete** (`hl=sr&gl=rs`) | 35 novih upita, fokusiranih na jezik i motivaciju (ne na brendove kao u 2B) | ✅ |
| **Analiza jezika u regionalnim recenzijama i komentarima** | Doslovni izrazi korisnika (materijal za Fazu 6) | ⚠️ delimično — vidi Ograničenja |

> **Kako se čitaju brojevi iz Google Trends-a.** To su **relativni indeksi unutar jedne
> grupe poređenja** (najviša tačka u grupi = 100), a ne apsolutni broj pretraga.
> Brojevi iz različitih grafikona nisu međusobno uporedivi. Sve krive su povučene
> 28.08.2026 za geo=RS.

---

## 1. Šta triguje mladu osobu (15–19) da kupi parfem

### 1.1 Nalaz koji menja okvir: parfem je u Srbiji najtraženija beauty kategorija, ubedljivo

**Nalaz.** U Srbiji, u poslednjih pet godina, upit **`parfem` ima približno 10× veći
relativni volumen pretraga od `šminka` i ~7× veći od `krema za lice`**. U istoj grupi
poređenja `parfem` se kreće 45–81, `šminka` 3–7, `krema za lice` 5–11 — bez ijednog
preseka u pet godina.

Pouzdanost: **VISOKA** · Izvor: [Google Trends, geo=RS, 2021–2026](https://trends.google.com/trends/explore?geo=RS&q=parfem,%C5%A1minka,krema%20za%20lice) · Provereno: 28.08.2026

**Interpretacija.** Brif klijenta postavlja 80% parfemi / 20% beauty kao poslovnu odluku.
Podaci o pretragama tu odluku **nezavisno potvrđuju** — u Srbiji je miris, a ne šminka,
kategorija oko koje se organizuje traženje. Ovo je jak argument u prezentaciji jer ne
dolazi od klijenta niti od agencije.

**Preporuka.** Odnos 80/20 ne treba preispitivati. Ali ga treba **komunicirati** —
KLAUDS je „mirisna radnja koja ima i beauty", ne „beauty radnja". To utiče na naziv
kategorija u web shopu, na raspored u prostoru i na to šta je u izlogu.

### 1.2 Trigeri: kompliment, ne miris

**Nalaz.** Dominantan opisani okidač kupovine kod tinejdžera nije opis mirisa nego
**socijalna potvrda koju miris donosi**. WWD to formuliše kao „Fragrances Are the New
Sneakers" — parfem je postao teen status simbol, a najtraženiji su mirisi sa reputacijom
„compliment-getter". U regionalnom medijskom prostoru isti obrazac: naslovi koji su
generisali najviše interesovanja doslovno glase **„Stalno mi govore da mirišem dobro"** i
**„Zaustave me na ulici"**.

Pouzdanost: **VISOKA** (globalno) / **SREDNJA** (region) · Izvori: [WWD — Fragrances Are the New Sneakers](https://wwd.com/beauty-industry-news/fragrance/fragrance-teens-boys-girls-viral-tiktok-perfume-1237900380/); [Index.hr — „Stalno mi govore da mirišem dobro"](https://www.index.hr/amp/shopping/clanak/stalno-mi-govore-da-mirisem-dobro-jedan-parfem-izazvao-veliki-interes-na-tiktoku/2651400.aspx); [Index.hr — „Zaustave me na ulici"](https://www.index.hr/shopping/clanak/djevojke-tvrde-da-im-jedan-zarin-parfem-donosi-bezbroj-komplimenata/2621507.aspx) · Provereno: 28.08.2026

**Interpretacija.** Ovo je najvažnija distinkcija cele faze. Klasična parfimerija prodaje
**miris** („note bergamota i vanile"). Tinejdžer kupuje **reakciju okoline** („ljudi me
zaustavljaju"). To su dva različita proizvoda iz iste boce.

**Preporuka.** Svaki opis proizvoda — na polici, na sajtu, u komunikaciji — mora da ima
**socijalnu posledicu**, ne samo mirisnu piramidu. Konkretno: umesto „orijentalno-gurmanski,
note cimeta i datula" → „ovo je onaj zbog kog te pitaju šta nosiš". Mirisna piramida ostaje,
ali kao drugi red informacije, za onoga ko hoće dublje.

### 1.3 „Smellmaxxing" — najjači aktivni trend u ciljnoj grupi

**Nalaz.** Termin **smellmaxxing** (izveden iz „looksmaxxing") označava praksu tinejdžera,
pretežno momaka, da grade rotirajuću kolekciju mirisa i tretiraju dobar miris kao
takmičarsku disciplinu. Merljive posledice: godišnja potrošnja tinejdžera momaka na miris
porasla je sa **75 USD (2023) na 110 USD (2024)**; **73% Gen Z-a nosi parfem najmanje tri
puta nedeljno**; TikTok je uticao na **66%** kupovina parfema kod Gen Z-a, Instagram na 64%;
u julu 2025. **38% ukupne potrošnje na mirise** u SAD poticalo je iz domaćinstava sa
Gen Z članom. Neke škole u SAD su uvele zabranu nanošenja parfema u učionici; polomljene
bočice u rancu postale su čest incident.

Pouzdanost: **VISOKA** (SAD) · Izvori: [Wikipedia — Smellmaxxing (sa primarnim referencama)](https://en.wikipedia.org/wiki/Smellmaxxing); [The Robin Report — Gen Z Is „Smellmaxxing"](https://therobinreport.com/gen-z-is-smellmaxxing-do-you-speak-the-language/); [NBC News — Inside the trend teens call smellmaxxing](https://www.nbcnews.com/video/inside-the-social-media-trend-teens-call-smellmaxxing-267971141616) · Provereno: 28.08.2026

**Prenosivost na Srbiju: SREDNJA-VISOKA.** Direktnog srpskog merenja nema. Ali posredni
domaći signal postoji i jak je — vidi 1.4 i sekciju 7.2 (kriva `Manoard`, `Club de Nuit`,
`Jean Paul Gaultier`).

### 1.4 Domaći signal koji potvrđuje trend: uspon Manoard-a i pad Sauvage-a

**Nalaz.** Dve krive iz Google Trends-a za Srbiju, u istom periodu, idu u suprotnim smerovima:

| Pojam | 2021 | Dec 2023 | Sredina 2025 | 2026 (avg) | Tumačenje |
|---|---|---|---|---|---|
| **Manoard** (domaći dupe brend) | 0 | 0 | **86–89 (vrh)** | 47–88 | Nov ulazak, održan na vrhu |
| **Dior Sauvage** | 20–44 | **65 (vrh)** | 20–26 | 14–25 | Pad ~65% sa vrha |
| **Jean Paul Gaultier** | 0 | 38 | 31–46 | 18–49 | Ulazak i stabilizacija |
| **Armaf Club de Nuit** | 14–27 | 44 | 45–64 | 28–42 | Stabilno visoko, 5 godina |

Pouzdanost: **VISOKA** · Izvor: [Google Trends, geo=RS, 2021–2026](https://trends.google.com/trends/explore?geo=RS&q=Zara%20parfem,Manoard,Club%20de%20Nuit,body%20mist) · Provereno: 28.08.2026

**Interpretacija.** Dior Sauvage je bio podrazumevani „muški parfem za mlade" u Srbiji i
**više nije**. Zamenili su ga: (a) orijentalni blok koji je jeftiniji i ima jaču projekciju,
(b) **domaći dupe brend Manoard** koji je za dve godine iz nule došao do nivoa pretrage
uporedivog sa Club de Nuit-om. To je najjači dokaz da srpski tinejdžer **ne kupuje ime nego
efekat po ceni koju može da plati**. Manoard se otvoreno pozicionira kao „kopije originala"
i to mu ne šteti — to mu je prednost.

**Preporuka.** KLAUDS ne sme da bude prodavnica u kojoj su „prave" i „lažne" police
razdvojene vrednosnim sudom. Ako se dupe blok tretira kao sramota, gubi se najbrže rastući
deo tražnje. Vidi predlog „Sličan na..." mehanike u sekciji 4.3.

### 1.5 Role modeli: pop, ne parfimerija

**Nalaz.** Kod ciljne grupe najjači imenovani role model u kategoriji je **Sabrina Carpenter**.
Njena linija (Scent Beauty) ostvarila je **100 mil. USD globalne maloprodaje u 2025, +60%
god/god**, prisutna je na **54 tržišta**, i bila je jedini celebrity miris u top 10 beauty
prodaje na Black Friday vikendu 2025. (Klarna). Cenovno: 30 ml ~30 USD, 75 ml 55 USD,
**mini 20 USD**. U Srbiji se prodaje u dm-u po **3.999 RSD / 34,1 EUR za 30 ml** (Faza 2B).
Iz sporta i muzike trend je noviji i slabiji: Coty–adidas radi „vibe-based" mirise, a
olimpijski sportisti se uvode u kampanje.

Pouzdanost: **VISOKA** (prodaja i cene) / **SREDNJA** (sport i gaming kao kanal) · Izvori: [Glossy — Inside Sabrina Carpenter's plan for global fragrance domination](https://www.glossy.co/beauty/inside-sabrina-carpenters-plan-for-global-fragrance-domination/); [Fashionista — Why Gen-Z influencers and celebrities are getting into fragrance](https://fashionista.com/2022/07/gen-z-influencers-celebrities-fragrance-perfume) · Provereno: 28.08.2026

**Ali — i to je ključno — u Srbiji ta kriva već pada.** Vidi 7.3.

---

## 2. Gde se mladi ZAPRAVO informišu

### 2.1 Poredak kanala

**Nalaz.** Konsolidovano iz više izvora, po jačini uticaja na odluku:

| # | Kanal | Podatak | Pouzdanost |
|---|---|---|---|
| 1 | **TikTok** | 66% Gen Z navodi TikTok kao primarni kanal otkrivanja parfema; 45% kupovina inspirisanih društvenim mrežama počinje na TikToku; 61% Gen Z-a dobija beauty preporuke sa TikToka — 3,4× više nego sa Instagrama | VISOKA (globalno) |
| 2 | **Vršnjaci uživo** | Word-of-mouth je drugi po jačini (39,7%) posle društvenih mreža; **74,1%** ispitanika za preporučene proizvode sazna kroz **kontakt uživo** | SREDNJA |
| 3 | **Instagram** | 64% uticaja na kupovinu parfema; u Srbiji i dalje glavna scena za svakodnevni sadržaj | VISOKA / SREDNJA |
| 4 | **YouTube recenzenti** | U regionu dominira jedan kanal — vidi 2.2 | SREDNJA |
| 5 | **Fizička radnja kao izvor informacije** | **81% Gen Z-a preferira kupovinu u fizičkoj radnji** u odnosu na onlajn — više od svih ostalih generacija; 92% navodi „da vidim, dodirnem i probam" kao razlog dolaska | VISOKA |

Izvori: [Beauty Independent — Gen Z favorites (Faza 2B, izvor 71)](https://www.beautyindependent.com/prioritizing-performance-gen-z-consumers-cerave-e-l-f-rare-beauty-products-as-favorites-new-report-finds/); [Wikipedia — Smellmaxxing](https://en.wikipedia.org/wiki/Smellmaxxing); [Retail Dive — How retailers are connecting with younger shoppers](https://www.retaildive.com/news/retailers-connecting-gen-z-gen-alpha-shoppers-foot-locker-coach-sephora/745172/); [The Role of Peer Influence on Purchase Decisions (JHECR)](https://jhecr.com/jhecr/article/download/25/15) · Provereno: 28.08.2026

**Interpretacija.** Redosled je: **TikTok otkriva → vršnjak potvrđuje → radnja odlučuje.**
Nijedan od tri koraka ne može da se preskoči. TikTok bez radnje daje želju bez konverzije;
radnja bez TikToka nema ulazni tok; a vršnjačka potvrda je korak koji nijedan brend ne
kontroliše direktno — može samo da ga olakša (vidi 4.3, „kupovina u paru").

### 2.2 Regionalni kreatori — mapa

**Nalaz.**

| Kreator / zajednica | Šta je | Pozicija |
|---|---|---|
| **Čovek Parfem** (Viktor Mihajlović) — [YouTube](https://www.youtube.com/channel/UCi1aWW4DvR8ds_T7LC_L7HQ), [TikTok](https://www.tiktok.com/@covekparfem), [X](https://x.com/covekparfem), [blog Eau de Viktor](https://eaudeviktor.com/omeni/) | Vodeći parfemski kanal na Balkanu i prvi te vrste u istočnoj Evropi; nedeljni live „konsultacije" utorkom u 22h na zasebnom kanalu | **Najuticajnija parfemska ličnost regiona.** Radi i sadržaj tipa „najbolji ženski parfemi iz Lilly i dm drogerija" — dakle direktno u cenovnoj zoni KLAUDS-a |
| **PunMiris.com** | Regionalni parfemski portal i forum; **50.000 članova, 137.000 parfema, 118.000 recenzija**; ima i sekciju za prodaju/razmenu i **dekante** | Najveći korpus recenzija na srpskom. **Zajednica odraslih entuzijasta**, ne tinejdžera — ali je izvor jezika i autoriteta koji se preliva |
| **Nicole parfemi**, **Santini**, **Parfemanija** (sekcija „Klonovi") | Domaći/regionalni dupe brendovi sa aktivnim TikTok recenzijskim ekosistemom | Dokaz da dupe segment ima **sopstvene kreatore**, ne samo kupce |

Pouzdanost: **SREDNJA** (brojevi članova PunMirisa iz opisa portala; broj pratilaca kreatora nije nezavisno verifikovan) · Izvori: [PunMiris.com](https://www.punmiris.com/); [Playboard — Čovek Parfem analitika](https://playboard.co/en/channel/UCi1aWW4DvR8ds_T7LC_L7HQ); [Favikon — Top fragrance influencers YouTube 2026](https://www.favikon.com/blog/top-fragrance-influencers-youtube) · Provereno: 28.08.2026

**Preporuka.** Za lansiranje: **Čovek Parfem je jedini regionalni kreator sa dovoljnim
autoritetom da sam po sebi legitimiše nov lanac.** Ali njegova publika je starija od ciljne
grupe. Predlog: koristiti ga za **kredibilitet prema roditeljima i prema tržištu** (segment
„odrasli koji kupuju za tinejdžera"), a paralelno graditi **10–15 mikro-kreatora 17–24 godine**
za samu ciljnu grupu. Nemoj oba posla dati istoj osobi.

### 2.3 Ograničenje: poverenje u influensere u Srbiji je nisko

**Nalaz.** Prema istraživanju **Social Serbia 2025** (Pioniri + Smart Plus Research, uzorak
1.000 ispitanika 12–65, jun 2025, deveta godina zaredom): **samo 2% onlajn populacije
potpuno veruje preporukama influensera**; najveće poverenje je u grupi 18–34. TikTok je
zabeležio **+37% rasta u odnosu na prethodnu godinu**. Digitalne navike su „sve brže,
površnije i fragmentisanije".

Pouzdanost: **VISOKA** (uzorak i metodologija objavljeni; puni izveštaj iza registracije) · Izvori: [Netokracija — Social Serbia 2025](https://www.netokracija.rs/social-serbia-2025-224282); [Pioniri — Social Serbia 2025](https://pioniri.com/sr/socialserbia2025/) · Provereno: 28.08.2026

**Interpretacija.** Ovo je korektiv za ceo influencer plan. U Srbiji **plaćena preporuka ne
prolazi kao dokaz**. Prolazi kao *podsticaj da se ode i proba*. Razlika je operativna: KPI za
influencer kampanju ne sme biti „prodaja preko koda", nego **dolazak u radnju i broj
testiranja**.

**Preporuka.** Težište budžeta pomeriti sa plaćenih objava na **user-generated sadržaj iz
same radnje** — prostor koji ljudi sami snimaju (Faza 4) i mehaniku koja daje razlog da se
snimi. Plaćeni kreatori nose prvih 6–8 nedelja; posle toga nose kupci ili niko.

---

## 3. Dominantan motiv: nije signature scent

### 3.1 Osnovni nalaz

**Nalaz.** Gen Z **ne traži signature scent** — gradi „fragrance wardrobe" / „scent
wardrobe": rotirajuću kolekciju koja se bira prema raspoloženju, prilici i „vibe-u" dana.
Merljivo: prosečno **5–12 mirisa** u posedu naspram 2–3 kod starijih generacija; udeo
ponovnih kupaca istog brenda pao je **sa 35% (2019) na 29%**; **88% Gen Z-a stavlja miris
ispred imena brenda**. Circana beleži da su prateći „layering" proizvodi (body sprej) u SAD
2024. porasli **+94%**, a mirisi za kosu +32%; u Evropi body mist +18% po vrednosti i +17%
po komadima u 2025. Prestižni segment hair & body mist dostigao je **474 mil. USD (+94%
god/god)**, uz **prosečnu cenu ~25 USD**; **mini formati čine 38% svih prodatih komada
prestižnog mirisa**.

Pouzdanost: **VISOKA** · Izvori: [Glossy — Inside the Gen Z–Gen Alpha hair perfume and body mist explosion (Circana, YipitData)](https://www.glossy.co/pop/inside-the-gen-z-gen-alpha-hair-perfume-and-body-mist-explosion/); [Cosmetics Business — Top 5 fragrance trends of 2026](https://cosmeticsbusiness.com/cosmetics-business-reveals-the-top-5-fragrance-trends-1); [Mintel — Social media fuels fragrance sampling](https://www.mintel.com/press-centre/fragrance-trends-2025-gen-z-gen-alpha-social-media-sampling/) · Provereno: 28.08.2026

**Interpretacija za KLAUDS.** Ovo direktno pogađa metriku iz brifa. Ako kupac ne traži
**jednu** bocu nego **kolekciju**, onda:
- cilj „prosečan artikal 30 EUR" je u sukobu sa stvarnim ponašanjem (viralne boce su 30–55 €,
  a sve ostalo u kolekciji je 5–25 €);
- cilj „korpa 50 EUR" je **realan i lako dostižan**, ali kroz **broj artikala**, ne kroz cenu;
- ponovna poseta je važnija od prve kupovine, jer se garderoba **dopunjuje**, ne kupuje odjednom.

Ovo potvrđuje zaključak Faze 2B (nalaz 15) iz nezavisnog ugla.

### 3.2 Razlika devojke vs. momci

**Nalaz.**

| | **Momci 15–19** | **Devojke 15–19** |
|---|---|---|
| Dominantan motiv | **Status i socijalna potvrda.** Miris kao takmičarska disciplina (smellmaxxing); traže „compliment-getter" reputaciju | **Estetika i identitet.** Miris kao deo „vibe-a" / estetike (vanilla girl, clean girl); rotacija po raspoloženju |
| Rast potrošnje | **+44% god/god** | +22% god/god |
| Apsolutna godišnja potrošnja | **127 USD** | 107 USD |
| Broj artikala | Manji broj, veće boce, jača projekcija | Veći broj, manji formati, mist + layering |
| Top brendovi (SAD) | Jean Paul Gaultier #1; zatim Ralph Lauren, Calvin Klein, Dior | Bath & Body Works #1 (24–49% udela zavisno od talasa) |
| Penetracija kategorije | 44% kod 12–14, **~57% kod 15–17** | Viša, ali sporije raste |

Pouzdanost: **VISOKA** (SAD, Piper Sandler) / **SREDNJA** (prenosivost) · Izvori: [WWD — Teens Want Sephora, Jean Paul Gaultier and CeraVe](https://wwd.com/beauty-industry-news/teen-beauty-sephora-fragrance-skin-care-makeup-hair-1237083704/); [WWD — Fragrances Are the New Sneakers](https://wwd.com/beauty-industry-news/fragrance/fragrance-teens-boys-girls-viral-tiktok-perfume-1237900380/) · Provereno: 28.08.2026

**Domaća potvrda smera.** Google Trends za Srbiju pokazuje da je **Jean Paul Gaultier** iz
nule (2021) porastao na 18–49 u 2026, dok **Dior Sauvage** pada sa 65 na ~20 — identičan
obrazac zamene lidera kao u američkim teen podacima. To je jedini nezavisan domaći dokaz
prenosivosti nalaza o momcima.

**Interpretacija.** Brif klijenta daje momcima **20%** ciljne grupe. Faza 2B je to već
označila kao potcenjeno; Faza 3 to potvrđuje iz drugog ugla: **momci su segment koji brže
raste, više troši po glavi, i ima jasniji, jednostavniji trigger.** Ne traže kustosiranje —
traže rangiranje.

**Preporuka.** Zadržati 50/20 podelu kao **planirani udeo prometa na startu**, ali predvideti
zasebnu zonu i zasebnu komunikaciju za momke od prvog dana, sa ciljem da se udeo pomeri ka
**30%** u prvih 12 meseci. Konkretna razlika: devojkama treba **izbor po estetici**, momcima
**rang lista i poređenje**.

### 3.3 Razlika 15–16 vs. 18–19

**Nalaz.** Faza 2B je već utvrdila finansijski rez: 15–16 (bez kartice, keš, roditelj
odobrava, plafon ~15 €) vs. 17–19 (Erste i Raiffeisen daju besplatne račune maloletnicima,
samostalna kupovina, 20–50 €). Faza 3 dodaje **bihevioralni rez**:

| | **15–16** | **18–19** |
|---|---|---|
| Izvor odluke | TikTok + drugarica; kupuje ono što je videla | TikTok → **provera** (PunMiris, Fragrantica, YouTube recenzija) → kupovina |
| Odnos prema dupe-u | Kupuje dupe jer je to ono što može | Kupuje dupe **svesno i argumentovano** („isti DNK, 1/5 cene") |
| Format | Mist, mini, poklon-set; retko puna boca | Puna boca 50–100 ml, ili dekant radi testiranja |
| Rizik | Ne kupuje neproverено; treba mu socijalni dokaz | Spreman na blind buy ako je cena ispod praga |
| Prisustvo roditelja | Često fizički u radnji | Retko |

Pouzdanost: **SREDNJA** (rez je izveden iz kombinacije finansijskih podataka Faze 2B i
obrazaca pretrage, nije direktno mereno na srpskom uzorku)

**Preporuka.** Ovo je argument za **dva cenovna ulaza u istoj radnji**: zona do 15 € koja je
dostupna bez pitanja roditelja, i zona 30–55 € koja podrazumeva odluku. Ako radnja ima samo
jednu, gubi polovinu primarne ciljne grupe.

---

## 4. Poznavanje nota vs. kupovina po osećaju — najoperativniji nalaz faze

### 4.1 Dokaz iz srpskih pretraga: mladi ne traže note, traže poređenja

**Nalaz.** Google Suggest za `hl=sr&gl=rs` pokazuje da se **jezik pretrage mirisa u Srbiji
gotovo u potpunosti sastoji od poređenja sa poznatim stvarima, a ne od mirisnih nota.**

Kompletan set predloga za `parfemi koji` i `parfem koji`:

> parfemi koji mirišu na **čisto** · na **more** · na čisto **dm** · na **kokos** · na
> **sveže** · na **sapun** · na **puder** · na **vanilu** · na **jasmin** · na **leto**
>
> parfem koji miriše na **čisto** · na **more** · na **kokos** · **koji privlači muškarce** ·
> na **tamjan** · na **lipu** · na **vanilu** · na **kremu za sunčanje** · na **puder** ·
> na **bebi puder**

Od 20 predloga, **samo tri su stvarne parfemske note** (vanila, jasmin, tamjan). Ostalih 17
su **referentni objekti iz svakodnevnog života**: čisto, more, sapun, puder, bebi puder,
krema za sunčanje, kokos, leto, lipa.

Pouzdanost: **VISOKA** (autocomplete rangira po stvarnoj učestalosti upita) · Izvor: [Google Suggest API (`hl=sr&gl=rs`)](https://suggestqueries.google.com/complete/search?client=firefox&hl=sr&gl=rs&q=parfemi+koji) · Provereno: 28.08.2026

**Drugi dokaz — traženje ekvivalenata.** Predlozi za `parfem sličan`:

> parfem sličan **light blue** · **kirke** · **creed aventus** · **chanel mademoiselle** ·
> **dior sauvage** · **burberry goddess ali jeftiniji**

Poslednji predlog sadrži i cenovni uslov u samom upitu. To je **kupac koji zna referencu i
traži put do nje po nižoj ceni** — ne kupac koji istražuje mirisnu piramidu.

**Treći dokaz — praznina u pismenosti.** U predlozima za `mist za telo` nalazi se
**„mist za telo **šta je**"**. Kategorija koja u Evropi raste +18% god/god u Srbiji još
uvek generiše upit „šta je to".

**Interpretacija.** Klijentova pretpostavka o „interaktivnom konceptu koji poštuje njihov
način biranja" ovde dobija konkretan sadržaj. Način biranja je: **poređenje, referenca,
posledica** — a ne edukacija o notama. Radnja koja mladog kupca dočeka mirisnom piramidom
govori jezikom koji on ne koristi.

**Preporuka — tri konkretne mehanike:**

1. **Navigacija po referenci, ne po noti.** Fizičke oznake na polici i filteri u web shopu
   glase: *„čisto"*, *„sapun i sveže oprano"*, *„kokos i leto"*, *„vanila i slatko"*,
   *„puder"*, *„krema za sunčanje"*, *„more"*. To su **doslovno reči kojima srpski kupac
   pretražuje**. Mirisna piramida stoji ispod, sitnijim slogom.
2. **„Sličan na…" polica.** Legitimna, otvorena, bez izvinjavanja. Postoji dokazana tražnja
   (`parfem sličan …ali jeftiniji`) i domaći brend koji je na njoj izgradio poziciju
   (Manoard). Ovo je istovremeno **najjači razlog da tinejdžer uđe baš u KLAUDS** — jer ni
   Sephora ni Jasmin taj razgovor neće da vode.
3. **„Šta je" objašnjenja u samom prostoru.** Za mist, layering, dekant, EDP vs EDT — jedna
   rečenica, ne pasus. Pretraga „mist za telo šta je" je dokaz da je edukacija potreba, ali
   samo na ulaznom nivou.

### 4.2 Gurmandski mirisi kao ulazna kapija

**Nalaz.** Globalna lansiranja gurmandskih mirisa porasla su **+7 procentnih poena između
2022. i 2024.** Razlog koji industrija navodi: jestive note (karamela, vanila, čokolada) su
jedine koje **ne zahtevaju prethodnu mirisnu pismenost** — svako ih prepoznaje i može da ih
oceni. Gen Z je najveća grupa kupaca **bez treniranog nosa**, pa je gurmand najprirodniji
ulaz. Domaća potvrda: `parfem koji miriše na vanilu` je među top predlozima, a Sabrina
Carpenter linija (dessert-inspired: Sweet Tooth, Caramel Dream, Cherry Baby, Me Espresso,
Lemon Pie) prodaje se u dm-u Srbija.

Pouzdanost: **VISOKA** · Izvori: [Mintel — Fragrance trends: Gen Z, Gen Alpha and sampling](https://www.mintel.com/press-centre/fragrance-trends-2025-gen-z-gen-alpha-social-media-sampling/); [Cosmetics Business — Top 5 fragrance trends 2026](https://cosmeticsbusiness.com/cosmetics-business-reveals-the-top-5-fragrance-trends-1) · Provereno: 28.08.2026

**Preporuka.** Prvi metar police od ulaza = **gurmand + „čisto"**. To su dve zone u kojima
kupac bez iskustva može sam da donese odluku za manje od minuta, bez pomoći prodavca.

### 4.3 Estetike su kategorije proizvoda

**Nalaz.** Cosmetics Business za 2026. navodi da su estetske odrednice postale nosilac
naracije: pored „vanilla girl" i „clean girl", rastu **„gourmand girly"** (med, pistaći),
**„fruit girl"** (maline) i **„granny chic"** (ljubičica, lavanda). Paralelno, „mini perfume"
je prema Spate Global Beauty Insights **trend broj jedan u celoj lepoti**, sa projekcijom
rasta **+78,4% za 2026**.

Pouzdanost: **SREDNJA** (Spate projekcija je jednokratna, nije nezavisno potvrđena) · Izvor: [Cosmetics Business](https://cosmeticsbusiness.com/cosmetics-business-reveals-the-top-5-fragrance-trends-1) · Provereno: 28.08.2026

**Preporuka.** Merchandising po estetikama je **skuplji za održavanje** (estetike se menjaju
na 6–9 meseci) ali je jedini raspored koji Gen Z čita bez uputstva. Rešenje: **fiksna
arhitektura police + izmenljive oznake.** Vidi Fazu 4 za prostornu razradu.

---

## 5. Spremnost na eksperimentisanje sa nepoznatim brendom

### 5.1 Šta je čini prihvatljivom — po jačini

**Nalaz.** Redosled faktora, konsolidovano:

| # | Faktor | Podatak | Pouzdanost |
|---|---|---|---|
| 1 | **Mogućnost probe pre kupovine** | **78% Gen Z-a počinje sa travel/mini formatom**, ne punom bocom; sampling smanjuje „purchase regret" i podiže stopu ponovne kupovine; Mintel: potrošači racionalizuju cenu sample seta i onda kad je jednaka punoj boci, jer im daje pravo na više mirisa | **VISOKA** |
| 2 | **Miris sam po sebi, nezavisno od imena** | **88% Gen Z-a stavlja miris ispred brenda** | VISOKA |
| 3 | **Društveni dokaz** (komentari, „compliment" reputacija) | 66% otkriva preko TikToka; reakcija u komentarima je presudna | VISOKA |
| 4 | **Cena ispod praga blind-buy-a** | **57% kupovina parfema kod Gen Z-a je ispod 50 USD**; dekant 2/5/8 ml „za par evra" umesto boce od 120 € | VISOKA |
| 5 | **Ambalaža** | Dizajnirana za „shelfie" — proizvod mora dobro da izgleda na polici u sobi i na telefonu | SREDNJA |
| 6 | **Preporuka influensera** | Uticajna za **otkrivanje**, ali slaba kao dokaz — u Srbiji samo 2% potpuno veruje | SREDNJA |

Izvori: [Mintel](https://www.mintel.com/press-centre/fragrance-trends-2025-gen-z-gen-alpha-social-media-sampling/); [Glossy](https://www.glossy.co/pop/inside-the-gen-z-gen-alpha-hair-perfume-and-body-mist-explosion/); [Netokracija — Social Serbia 2025](https://www.netokracija.rs/social-serbia-2025-224282) · Provereno: 28.08.2026

**Interpretacija.** Ovo je najbolja vest za KLAUDS u celoj fazi. **Nepoznat brend nije
prepreka za ovu ciljnu grupu — nepoznat brend koji se ne može probati jeste.** Klijent u
Fazi 2B ima problem „nema listu brendova"; Faza 3 pokazuje da lista brendova nije ono što
odlučuje. Odlučuje **format u kom se brend nudi**.

### 5.2 Domaći dokaz: dekant tražnja postoji i uslužuju je sivi kanali

**Nalaz.** U Srbiji:
- `dekant` ima **merljiv i trajan volumen pretrage** od avgusta 2023. naovamo, sa vrhovima
  46–80 u grupi poređenja — dok `tester parfema` i `mini parfem` ostaju na ~0 (dakle,
  **„dekant" je reč koju domaći kupac stvarno koristi**, ostale dve nisu);
- autocomplete daje `dekant rs`, `dekant parfemi`, `dekanti parfema`;
- Faza 2B je već utvrdila da je „parfemi na točenje" 7. predlog za `parfemi`, sa
  modifikatorima za pet gradova;
- `testeri parfema` u autocomplete-u vodi na **`kupujemprodajem`, `5ml`, `10ml`, `20 ml`,
  `brojevi`, `iskustva`** — dakle na **peer-to-peer sivo tržište**, ne na trgovca.

Pouzdanost: **VISOKA** za postojanje tražnje, **SREDNJA** za veličinu · Izvori: [Google Trends geo=RS](https://trends.google.com/trends/explore?geo=RS&q=tester%20parfema,dekant,mini%20parfem,parfem%20set); [Google Suggest](https://suggestqueries.google.com/complete/search?client=firefox&hl=sr&gl=rs&q=dekant) · Provereno: 28.08.2026

> **Metodološka ograda:** upit `dekant` u srpskom jeziku deli koren sa „dekanter za vino" i
> „dekantiranje vina", što je vidljivo i u samom autocomplete-u. Deo krive je kontaminiran.
> Smer nalaza (postoji, raste, ima svoj vokabular) ostaje, tačna veličina ne.

**Preporuka.** **Discovery format je najveća pojedinačna prilika koju je ova faza otkrila za
KLAUDS.** Tražnja je dokazana, cenovno je idealna za 15–16 segment, rešava problem
„nepoznat brend", obara prosečnu cenu artikla ka cilju od 30 € i istovremeno podiže broj
artikala u korpi. I — najvažnije — **nijedan legalan trgovac u Srbiji je danas ne uslužuje
sistematski.** Ako KLAUDS uzme kategoriju „dekant/discovery" i uradi je uredno, brendirano i
legalno, uzima nišu koja trenutno postoji samo na KupujemProdajem-u.

---

## 6. Kupovna moć i mehanika kupovine kod 15–19

### 6.1 Domaći podatak ne postoji — i dalje

**Nalaz.** Ponovnom pretragom (srpski i engleski, 28.08.2026) **potvrđeno je da javno
istraživanje o iznosu džeparca srednjoškolaca u Srbiji ne postoji.** Postoje samo
savetodavni medijski tekstovi bez uzorka i metodologije.

Pouzdanost: **podatak ne postoji** · Kontrolni izvor: [Telegraf — Kada dati deci džeparac](https://www.telegraf.rs/vesti/srbija/2969976-kada-dati-deci-dzeparac-koliko-novca-izdvojiti-i-koliko-cesto-im-puniti-budzet-resavamo-veliku-dilemu-roditelja) · Provereno: 28.08.2026

### 6.2 Najbliži validan surogat: hrvatsko istraživanje na 1.011 tinejdžera

**Nalaz.** Hrvatska udruga banaka i Štedopis (Institut za financijsko obrazovanje),
**uzorak 1.011 učenika uzrasta 13–19**, objavljeno 2020:

| Podatak | Vrednost |
|---|---|
| Prima džeparac | ~50% od roditelja; 30% deo sam zarađuje uz pomoć roditelja |
| Štedi | 71% (gimnazijalci 75%, prvi razred 77%, uzrast 15 g. **78%**) |
| Slaže se da „novac postoji da se troši" | 65% |
| Ima otvoren bankovni račun | **51%** |
| Koristi mobilno bankarstvo (od onih sa računom) | 33% |
| **Najveći rashodi** | izlasci **62%** · hrana u školi/pekari **62% / 50%** · odeća i obuća **40%** · **kozmetika 32%** |

Pouzdanost: **SREDNJA** za Srbiju (druga zemlja, 2020. godina — pre inflacije i pre
smellmaxxing talasa; smer i struktura potrošnje prenosivi, iznosi nisu) · Izvor: [Točka na I — Istraživanje o financijskoj pismenosti tinejdžera (HUB + Štedopis)](https://tockanai.hr/biznis/financije/istrazivanje-o-financijskoj-pismenosti-tinejdzera-36420/) · Provereno: 28.08.2026

**Interpretacija.** **Kozmetika je četvrta stavka u budžetu tinejdžera, iza izlazaka, hrane i
odeće — sa 32%.** To znači da skoro svaki treći tinejdžer već ima kozmetiku kao redovnu
stavku. Ali stavke ispred nje su socijalne (izlasci, hrana s drugarima) — što potvrđuje da
je **odlazak u tržni centar sa društvom deo istog budžeta iz kog se plaća parfem**. Radnja
koja je usput na toj ruti dobija impulsnu kupovinu; radnja koja traži namensko putovanje ne.

### 6.3 Poklon: dvosmerni kanal, i najveći sezonski vrh

**Nalaz — sezona.** Google Trends, `parfem`, Srbija, poslednjih 12 meseci: vrh je nedelja
**14–20.12.2025 (indeks 90)**, minimum početkom aprila 2026 (52). Odnos **~1,7×**. Isti
obrazac ponavlja se svake godine u petogodišnjoj krivoj.

Pouzdanost: **VISOKA** · Izvor: [Google Trends, geo=RS, 12 meseci](https://trends.google.com/trends/explore?date=today%2012-m&geo=RS&q=parfem) · Provereno: 28.08.2026

**Nalaz — poklon kao format.** Globalno, poklon-setovi rastu **+26% god/god** i spadaju u
najbrže rastuće vrednosne kategorije kod Gen Z-a. Domaći autocomplete (Faza 2B): „parfem
poklon setovi" i „parfem poklon paket" su vodeći predlozi za `parfem poklon`. Uz to,
`parfem set` u srpskom autocomplete-u daje **`parfem set dm`, `set parfem i dezodorans`,
`set parfem i krema`, `set parfem lilly`** — dakle traži se **kombinovani set**, ne samo boca.

Pouzdanost: **VISOKA** · Izvori: Faza 2B; [Google Suggest](https://suggestqueries.google.com/complete/search?client=firefox&hl=sr&gl=rs&q=parfem+set) · Provereno: 28.08.2026

**Interpretacija — tri različite poklon situacije, tri različita kupca:**

| Situacija | Ko plaća | Iznos | Šta mu treba u radnji |
|---|---|---|---|
| **Odrasli kupuje tinejdžeru** (rođendan, Nova godina, slava) | roditelj, tetka, kum | 30–60 € | **Vođenje.** Ne zna šta je „u fazonu". Treba mu polica „siguran pogodak, 15–19 godina" i osoblje koje ne prodaje najskuplje |
| **Tinejdžer kupuje tinejdžeru** (rođendan drugarice, kraj školske godine) | tinejdžer, keš | 10–20 € | **Da izgleda skuplje nego što je.** Mini, mist, set od 2–3 sitna artikla, pakovanje |
| **Tinejdžer traži da mu se kupi** (spisak želja) | roditelj, ali izbor je tinejdžerov | 30–55 € | **Wishlist mehanika** — da tinejdžer sačuva izbor i pošalje ga |

**Preporuka.** Treća situacija je danas potpuno neuslužena u srpskoj parfimeriji, a
tehnički je najjeftinija za implementaciju: **wishlist na sajtu + fizička kartica sa QR
kodom u radnji** koju tinejdžer napuni i pošalje. Ona rešava i problem 15–16 segmenta bez
kartice, i problem odraslog kupca bez znanja. Preporuka je da uđe u obim otvaranja, ne u
drugu fazu.

### 6.4 Frekvencija i iznos — sinteza za KLAUDS

**Nalaz (izvedeno).** Kombinovanjem: 73% Gen Z nosi miris 3+ puta nedeljno · kolekcija
5–12 komada · 57% kupovina ispod 50 USD · mini formati 38% prestižnih komada · domaći
cenovnik iz Faze 2B (viralne boce 30–55 €, mist 6–25 €, mini 4–15 €) · finansijski rez
15–16 (~15 €) vs. 17–19 (20–50 €).

Radna procena za srpskog kupca 15–19:

| Segment | Frekvencija kupovine mirisa | Tipičan iznos po poseti | Godišnje |
|---|---|---|---|
| 15–16 | 4–6× godišnje (mist, mini, sitno) | **8–18 €** | ~60–90 € |
| 17–19 | 3–4× godišnje, veće stavke | **25–50 €** | ~100–160 € |
| Poklon primljen | 1–2× godišnje | 30–60 € (plaća odrasli) | — |

Pouzdanost: **NISKA** — ovo je **ekstrapolacija**, ne merenje. Nijedan element nije domaći
podatak o stvarnoj kupovini srpskog tinejdžera.

**Preporuka.** Ove brojeve **ne stavljati u finalni izveštaj kao projekciju**, nego kao
hipotezu koju treba testirati. Dva jeftina načina da se zameni stvarnim podatkom, po
prioritetu:
1. **Interni CRM Belodore/Almara, presek kupaca mlađih od 25** — košta nula, traži se od
   klijenta (otvoreno pitanje 8 iz Faze 2B, i dalje bez odgovora).
2. **Anketa na 300–500 srednjoškolaca** — 800–1.500 € (otvoreno pitanje 11 iz Faze 2B).

---

## 7. Analiza stvarnog ponašanja

### 7.1 Search behavior — šta se stvarno kuca

**Nalaz — jezik cene.** Predlozi za `jeftini parfemi`, po redosledu učestalosti:

> jeftini parfemi · **dm** · **koji dugo traju** · **a dobri** · **koji mirišu na čisto** ·
> **lilly** · **koji mirišu kao skupi** · **srbija** · **reddit** · ana rs

Tri od deset predloga su **kriterijumi kvaliteta ugrađeni u upit o ceni**: „koji dugo traju",
„a dobri", „koji mirišu kao skupi". Deveti predlog je **`reddit`** — kupac eksplicitno traži
zajednicu, ne trgovca.

**Nalaz — čega NEMA.** Sledeći upiti **ne generišu nijedan predlog** u srpskom
autocomplete-u (dakle imaju volumen ispod praga):
`parfem sa tiktoka` · `parfem koji svi hvale` · `najbolji parfem za srednju skolu` ·
`dupe parfem` · `parfem poklon za devojku` · `parfem poklon za decka` · `parfem za skolu`
· `parfem 15 godina`

Predlozi za `parfem za tinejdzere` postoje ali su tanki (3 predloga), a `parfem za tinejdzere`
u Google Trends-u za Srbiju stoji na **0 kroz celih pet godina**.

Pouzdanost: **VISOKA** · Izvori: [Google Suggest API](https://suggestqueries.google.com/complete/search?client=firefox&hl=sr&gl=rs&q=jeftini+parfemi); [Google Trends geo=RS](https://trends.google.com/trends/explore?geo=RS&q=parfem,body%20mist,parfem%20za%20tinejdzere) · Provereno: 28.08.2026

**Interpretacija — i ovo je ozbiljno upozorenje za SEO i za naming.**
**Tinejdžer sebe ne pretražuje kao tinejdžera.** Ne kuca „parfem za tinejdžere", „parfem za
školu", ni „parfem sa TikToka". Kuca **ime brenda**, **poređenje** („sličan …"), ili
**referencu na miris** („miriše na čisto"). Zaključak: sadržajna strategija web shopa ne sme
da se gradi oko demografskih fraza. Gradi se oko **brendova, poređenja i referenci**.

**Nalaz — body mist u Srbiji je manji nego što deluje.** U direktnom poređenju sa `parfem`,
upit `body mist` u Srbiji stoji na **2–6 indeksnih poena** kroz ceo period — dakle reda
veličine **~4% volumena** upita `parfem`.

Pouzdanost: **VISOKA** · Izvor: [Google Trends geo=RS](https://trends.google.com/trends/explore?geo=RS&q=parfem,body%20mist,parfem%20za%20tinejdzere) · Provereno: 28.08.2026

> ⚠️ **Korekcija ka Fazi 2B i Fazi 7.** Faza 2B predlaže „mist & layering zid" sa **18%
> prometa i 20% prostora**. Evropski rast kategorije (+18% god/god, Circana) je stvaran, ali
> **u Srbiji je pretraga za tim proizvodom i dalje niska, a u autocomplete-u se pojavljuje
> upit „mist za telo šta je"**. Realan zaključak: mist je kategorija sa **visokim potencijalom
> i niskom trenutnom svesnošću**. Ne treba je smanjiti — treba je **tretirati kao kategoriju
> koju KLAUDS mora da EDUKUJE, a ne da samo izloži.** Ako se postavi kao zid bez objašnjenja
> i bez probanja, zauzeće 20% prostora za promet koji nije tu.

### 7.2 Viral product lifecycle — izmereno na srpskim podacima

**Nalaz.** Google Trends, Srbija, omogućava da se izmeri stvarni životni ciklus tri različita
tipa viralnog proizvoda:

**Tip A — „Vatromet": Sabrina Carpenter (celebrity gurmand)**

| Period | Indeks |
|---|---|
| do nov. 2023 | 0 |
| dec. 2023 | 11 (prvi signal) |
| **jul 2024** | **59 (vrh)** |
| jan. 2025 | 57 |
| avg. 2025 | 28 |
| **avg. 2026** | **14–20** |

Ceo luk: **~12 meseci uspona, ~24 meseca do pada na trećinu vrha.** Proizvod i dalje postoji
u dm-u, ali interesovanje je u repu.

**Tip B — „Plato": Lattafa / Khamrah (orijentalni)**

| Period | Lattafa | Khamrah |
|---|---|---|
| do sep. 2022 | 0 | 0 |
| jan. 2023 | 17 | 0 |
| **sep. 2024** | 48 | **45 (prvi vrh)** |
| **dec. 2025** | **75 (vrh)** | 44 |
| avg. 2026 | 47 | 23 |

Lattafa je **tri godine u usponu** i još nije pala ispod nivoa iz 2024. Khamrah pokazuje
oscilaciju 20–45 bez kolapsa. Ovo **nije viralni talas — ovo je ulazak brenda u kanon.**

**Tip C — „Konstanta": Armaf / Club de Nuit**
Armaf se od 2021. do 2026. drži u rasponu **31–80**, bez ijednog perioda ispod 30. Club de
Nuit isto: 14–77 kroz pet godina. Ovo je brend koji **nikad nije bio viralan i nikad nije pao**.

Pouzdanost: **VISOKA** za oblik krive, **SREDNJA** za tumačenje (Trends meri interesovanje,
ne prodaju) · Izvori: [Google Trends: Lattafa/Armaf/Sol de Janeiro/VS](https://trends.google.com/trends/explore?geo=RS&q=Lattafa,Armaf,Sol%20de%20Janeiro,Victoria%27s%20Secret); [Google Trends: Khamrah/9PM/Yara](https://trends.google.com/trends/explore?geo=RS&q=Khamrah,9PM,Yara); [Google Trends: Dior Sauvage/JPG/Sabrina Carpenter](https://trends.google.com/trends/explore?geo=RS&q=Dior%20Sauvage,Jean%20Paul%20Gaultier,Sabrina%20Carpenter) · Provereno: 28.08.2026

> **Ograde:** `9PM` i `Yara` su višeznačni upiti u srpskom (Yara je i lično ime i naziv
> kompanije za đubriva; 9PM je i vreme) — njihove krive su najmanje pouzdane u setu.
> `Victoria's Secret` se u Srbiji kreće na nivou šuma (0–22), što je verovatno posledica
> toga da se traži kao radnja i kao donji veš, a ne kao miris.

**Globalna potvrda „plato" obrasca.** Lattafa je preko TikTok Shop-a od avg. 2024. do jul
2025. ostvarila **preko 63 mil. USD, +174%** u odnosu na 23,1 mil. USD godinu ranije; u
februaru 2025. bila je **br. 1 mirisni brend po prodaji na TikTok Shop-u** sa preko 4 mil. USD
u periodu.

Pouzdanost: **VISOKA** · Izvor: [WWD — Rising fragrance brands netting millions on TikTok Shop](https://wwd.com/beauty-industry-news/fragrance/lattafa-phlur-sol-de-janeiro-dupe-tiktok-shop-fragrances-1237049601/) · Provereno: 28.08.2026

**Interpretacija — šta ostaje posle talasa.** Tri obrasca traže tri različite nabavne odluke:

| Tip | Primer | Trajanje | Šta raditi |
|---|---|---|---|
| **Vatromet** | Sabrina Carpenter, viralni mist | 12 meseci uspon / 24 do repa | Kupovati **malo i brzo**, u malim formatima. Nikad dubok lager. Vrednost je u tome što donosi ljude u radnju, ne u marži |
| **Plato** | Lattafa, Khamrah, Yara | 3+ godine, i dalje raste | **Ovo je jezgro asortimana.** Dubok lager, stalna polica |
| **Konstanta** | Armaf, Club de Nuit, 9PM | 5+ godina bez pada | **Nikad ne sme da nedostaje.** To je razlog zbog kog se kupac vraća |

**Preporuka.** U planu otvaranja odvojiti budžet nabavke na **~15% vatromet / ~55% plato /
~30% konstanta**. Greška koju treba izbeći: otvoriti radnju punu vatrometa jer je „to sad
trend". Kriva Sabrine Carpenter pokazuje da bi roba nabavljena u vrhu (jul 2024) danas bila
mrtav lager.

> **Napomena za Fazu 8:** ovo je i **operativni test za sam KLAUDS.** Otvaranje je oktobar
> 2026 (klijent javlja da kasni). Sve što je danas na vrhu krive biće u repu do otvaranja.
> Lista brendova mora da se zaključa **najranije u martu 2026**, i to sa 15% rezervisanog
> budžeta za ono što tada bude novo.

### 7.3 Jezik korisnika — doslovni materijal za Fazu 6

**Nalaz.** Prikupljeni doslovni izrazi, po tipu:

**(a) Kako opisuju miris — srpski/regionalni upiti (Google Suggest, `gl=rs`):**
> „miriše na **čisto**" · „miriše na **sapun**" · „miriše na **bebi puder**" · „miriše na
> **kremu za sunčanje**" · „miriše na **more**" · „miriše na **kokos**" · „miriše na **leto**"
> · „**koji dugo traju**" · „**a dobri**" · „**koji mirišu kao skupi**" · „**ali jeftiniji**"
> · „**mist za telo šta je**" · „**parfem koji privlači muškarce**"

**(b) Kako opisuju efekat — regionalni mediji i TikTok (doslovni citati):**
> „**Stalno mi govore da mirišem dobro**"
> „**Zaustave me na ulici** i pitaju koji parfem nosim"
> „**Svaki put kad ga nosim dobijem kompliment**"
> „**Hvala ti, naručujem ga!**"
> „**Upravo sam ga kupila!**"
> „**Još jedna stvar koju ću dodati na svoj popis kad postanem bogata.**"

**(c) Kako opisuju izbor — Gen Z, engleski, iz industrije:**
> „I kind of pick what goes with my outfit and what would match **the vibe**."
> (kupac o načinu biranja mirisa, Glossy/Circana)
> „It's about **play**. Consumers come to touch, to feel the products."
> (predstavnik Sephore o mladim kupcima u radnji, Retail Dive)

Pouzdanost: **VISOKA** za (a) — to su stvarni upiti; **SREDNJA** za (b) — citati su preneti
kroz medij, nisu izvučeni direktno iz TikToka; **VISOKA** za (c) · Izvori: [Google Suggest](https://suggestqueries.google.com/complete/search?client=firefox&hl=sr&gl=rs&q=jeftini+parfemi); [Index.hr](https://www.index.hr/amp/shopping/clanak/stalno-mi-govore-da-mirisem-dobro-jedan-parfem-izazvao-veliki-interes-na-tiktoku/2651400.aspx); [Index.hr — Zara](https://www.index.hr/shopping/clanak/djevojke-tvrde-da-im-jedan-zarin-parfem-donosi-bezbroj-komplimenata/2621507.aspx); [ELLE.hr — Parfemi i komplimenti](https://elle.hr/ljepota/parfemi-i-komplimenti-su-pokazatelj-da-ste-pronasli-pravi-miris/); [Glossy](https://www.glossy.co/pop/inside-the-gen-z-gen-alpha-hair-perfume-and-body-mist-explosion/); [Retail Dive](https://www.retaildive.com/news/retailers-connecting-gen-z-gen-alpha-shoppers-foot-locker-coach-sephora/745172/) · Provereno: 28.08.2026

**Interpretacija za Fazu 6.** Tri stvari o tonu KLAUDS-a proizlaze direktno iz ovog jezika:
1. **Nema stručnih termina u prvom redu.** Kupac ne kaže „gurmand", kaže „miriše na vanilu".
2. **Rečenice su posledične, ne opisne.** „Zaustave me na ulici" je struktura: *ja nosim →
   svet reaguje*. Kopirajting KLAUDS-a treba da ima isti oblik.
3. **Cena se pominje otvoreno i bez stida.** „a dobri", „ali jeftiniji", „kao skupi" — kupac
   sam spaja cenu i kvalitet u istoj rečenici. Brend koji o ceni ćuti zvuči kao da nešto krije.

---

## 8. Sinteza: četiri arhetipa KLAUDS kupca

> Ovi arhetipi su **osnova za customer persone u Fazi 7**. Svaki je izveden iz nalaza gore;
> uz svaki stoji koji nalaz ga nosi. Procenti prometa su **radna procena (NISKA pouzdanost)**,
> ne merenje.

### A. „MAJA" — kolekcionarka vibe-ova · devojka 15–17
**~35% prometa · korpa 15–30 € · dolazi 5–6× godišnje**

- **Motiv:** estetika i identitet. Miris je deo „vibe-a" dana, ne potpis. Ima 4–8 stvari,
  rotira ih. *(nalaz 3.1, 3.2)*
- **Kako bira:** TikTok je otkriva, drugarica potvrđuje, radnja odlučuje. Ne zna note; zna
  „miriše na čisto / kokos / vanilu". *(4.1, 2.1)*
- **Novac:** keš ili roditeljska kartica, plafon ~15 € po odluci koju donosi sama. *(6.2, 3.3)*
- **Šta joj KLAUDS mora dati:** mist i mini u zoni 6–18 €, police označene rečima koje
  koristi, mogućnost da proba sve bez pitanja, i razlog da uslika. Dolazi sa društvom.
- **Šta je gubi:** prodavac koji joj priđe sa mirisnom piramidom. Zaključana testera.

### B. „NIKOLA" — smellmaxxer · momak 15–19
**~25% prometa · korpa 30–50 € · dolazi 3–4× godišnje, ciljano**

- **Motiv:** status i socijalna potvrda. Miris je takmičarska disciplina; traži projekciju i
  „compliment-getter" reputaciju. *(1.3, 3.2)*
- **Kako bira:** dolazi sa **imenom** koje je već video — Armaf, Afnan 9PM, Club de Nuit, JPG.
  Ne istražuje u radnji, verifikuje. Segment koji raste **+44% god/god** i troši više po glavi
  od devojaka. *(3.2, 7.2)*
- **Novac:** 17–19 ima karticu; 15–16 dolazi sa keš iznosom koji je ceo namenjen jednoj boci.
- **Šta mu KLAUDS mora dati:** **rang listu, ne kustosiranje.** Poređenje „ovaj vs. onaj",
  jasno istaknutu jačinu i trajnost, i sekciju „sličan na…". Kupovina traje 4 minuta.
- **Šta ga gubi:** radnja koja izgleda kao da nije za njega. Vizuelni jezik koji je isključivo
  ženski je najveći rizik ovog segmenta.

### C. „TEODORA / LUKA" — istraživač · 18–19, oba pola
**~20% prometa · korpa 35–60 € · dolazi 3–4× godišnje, i kupuje onlajn**

- **Motiv:** **value for money, argumentovano.** Zna referencu, traži put do nje jeftinije.
  Kuca „parfem sličan burberry goddess ali jeftiniji". *(4.1, 7.1)*
- **Kako bira:** TikTok → **provera** (PunMiris, YouTube, Reddit) → kupovina. Ima sopstvenu
  karticu i kupuje i onlajn. 73,5% ove grupe u Srbiji živi van Beogradskog regiona i
  **dostupna je isključivo preko web shopa**. *(3.3, Faza 2B nalaz 10)*
- **Šta mu KLAUDS mora dati:** **dekant i discovery set** — dokazana tražnja koju danas
  uslužuje samo sivo tržište. Iskrene, uporedive informacije. Web shop koji radi na telefonu.
- **Šta ga gubi:** osećaj da ga radnja tretira kao dete. Ovo je segment koji najbrže prepozna
  marketinšku prazninu.

### D. „SNEŽANA" — odrasla, plaća · 30–50
**~20% prometa · korpa 40–70 € · dolazi 2–3× godišnje, koncentrisano u decembru**

Ovaj segment ima **dva režima** i oba su u brifu:

- **D1 — kupuje poklon tinejdžeru.** Ne zna šta je „u fazonu", i to je **jedini put kad je
  spremna da posluša prodavca**. Decembarski vrh je 1,7× iznad proseka. *(6.3)*
- **D2 — kupuje sebi.** Ušla je zbog poklona, ostaje zbog sebe. Ovo je segment koji
  najprirodnije prelazi ka Belodore/Almara asortimanu i **najveći je rizik kanibalizacije**
  (otvoreno pitanje 1 i 6 iz Faze 2A/2B).
- **Šta joj KLAUDS mora dati:** policu „siguran pogodak, 15–19", gotova poklon pakovanja u
  tri cenovna stepena (20 / 35 / 55 €), i **poklon karticu / wishlist** kao izlaz kada ne
  ume da odluči.
- **Šta je gubi:** radnja koja komunicira toliko „tinejdžerski" da se ona u njoj oseća kao
  uljez. Ovo je direktan sukob sa pozicioniranjem i mora se rešiti u Fazi 4 (zoniranje) i
  Fazi 6 (ton) — **ne kompromisom u komunikaciji, nego odvojenom zonom u prostoru.**

---

## Ograničenja i rupe u podacima

| Rupa | Zašto je nastala | Kako se zatvara |
|---|---|---|
| **Nema domaćeg podatka o džeparcu i stvarnoj potrošnji 15–19** | Javno istraživanje ne postoji (potvrđeno drugi put) | (1) Interni CRM Belodore/Almara — presek kupaca <25; (2) anketa 300–500 srednjoškolaca, 800–1.500 €. **Bez ovoga svaka projekcija korpe je pretpostavka.** |
| **TikTok, Reddit i PunMiris nisu bili mašinski dostupni** | tiktok.com/discover vraća prazan sadržaj; reddit.com blokira crawler; punmiris.com vraća HTTP 403 (Cloudflare) | **Ručno prikupljanje: 100–150 komentara sa 10–15 srpskih TikTok objava o parfemima + 3–5 tema sa PunMirisa.** ~4 sata rada. Ovo je **direktan ulaz u Fazu 6** i preporuka je da se uradi pre nje |
| **Nema srpskih podataka o teen search volumenu u apsolutnim brojevima** | Google Trends daje relativne indekse | Google Ads Keyword Planner (traži nalog sa aktivnom kampanjom) — daje raspone volumena za geo=RS |
| **Regionalna raspodela pretraga unutar Srbije** | Trends je vratio samo „Vojvodina: 100" — uzorak je pretanak za podregione | Ne može se zatvoriti javno. Zameniti podacima o poreklu porudžbina iz web shopa posle lansiranja |
| **Piper Sandler podaci su američki** | Ekvivalentno istraživanje za Srbiju/region ne postoji | Smer je potvrđen domaćom krivom (JPG ↑ / Sauvage ↓), ali **iznosi u USD se ne smeju prenositi na Srbiju** |
| **Hrvatsko istraživanje o džeparcu je iz 2020.** | Novije nema | Koristi se za **strukturu potrošnje**, ne za iznose |
| **Broj pratilaca i engagement rate regionalnih kreatora** | Nije nezavisno verifikovan (nasleđena rupa iz Faze 2B) | Alat (Analisa / HypeAuditor) ili direktan kontakt. Potrebno pre pregovora o saradnji |
| **`dekant`, `Yara`, `9PM` su višeznačni upiti** | Priroda srpskog jezika | Smer nalaza je pouzdan, veličina nije. Ne citirati kao precizne brojeve |

---

## REZIME ZA SINTEZU

> Ovaj rezime je **ulaz za Fazu 6** (ton i jezik brenda) i za Fazu 7. Piše se tako da bude
> razumljiv nekome ko nije čitao pun dokument.

1. **Parfem je u Srbiji ubedljivo najtraženija beauty kategorija — ~10× više pretraga od
   „šminka" i ~7× od „krema za lice", bez ijednog preseka u pet godina.** Odnos 80/20 iz
   brifa je nezavisno potvrđen. KLAUDS je mirisna radnja koja ima beauty, ne obrnuto. — *(VISOKA)*
2. **Tinejdžer ne kupuje miris — kupuje reakciju okoline.** Dominantan trigger je kompliment,
   ne mirisna piramida. Regionalni jezik: „Stalno mi govore da mirišem dobro", „Zaustave me
   na ulici". Svaki opis proizvoda mora imati socijalnu posledicu, ne samo note. — *(VISOKA)*
3. **Srpski kupac miris opisuje referencama, ne notama.** Od 20 najčešćih autocomplete
   predloga za „parfem koji miriše na…", samo tri su prave note (vanila, jasmin, tamjan);
   ostalih 17 su **čisto, more, sapun, puder, bebi puder, kokos, leto, krema za sunčanje**.
   Police i filteri moraju da koriste te reči. — *(VISOKA)*
4. **„Smellmaxxing" je najjači aktivni trend u ciljnoj grupi.** Godišnja potrošnja tinejdžera
   momaka na miris: 75 USD (2023) → 110 USD (2024); 73% Gen Z-a nosi miris 3+ puta nedeljno;
   TikTok utiče na 66% kupovina. Momci rastu **+44% god/god** vs. +22% kod devojaka. — *(VISOKA, SAD)*
5. **Domaći dokaz da je trend stigao: Dior Sauvage je pao ~65% sa vrha (2023→2026), a domaći
   dupe brend Manoard je iz nule došao na nivo Club de Nuit-a.** Srpski tinejdžer kupuje
   efekat po ceni koju može, ne ime. — *(VISOKA)*
6. **Gen Z ne traži signature scent — gradi kolekciju od 5–12 mirisa.** Udeo ponovnih kupaca
   istog brenda pao je sa 35% (2019) na 29%; 88% stavlja miris ispred brenda. **Cilj „korpa
   50 €" je realan, ali kroz broj artikala, ne kroz cenu artikla.** — *(VISOKA)*
7. **Životni ciklus viralnog proizvoda, izmeren na srpskim podacima, ima tri oblika:**
   *vatromet* (Sabrina Carpenter: 12 meseci uspona, na trećini vrha posle 24), *plato*
   (Lattafa: tri godine rasta, još raste), *konstanta* (Armaf: pet godina bez pada ispod 30).
   Predlog podele nabavnog budžeta: **15% vatromet / 55% plato / 30% konstanta.** — *(VISOKA za oblik, SREDNJA za tumačenje)*
8. **Nepoznat brend nije prepreka — nepoznat brend koji se ne može probati jeste.** 78% Gen
   Z-a počinje sa mini/travel formatom; 57% kupovina je ispod 50 USD; 88% bira miris pre
   imena. **Pitanje „koje brendove" je manje važno od pitanja „u kom formatu".** — *(VISOKA)*
9. **Dekant/discovery je najveća pojedinačna prilika koju je ova faza otkrila.** „Dekant" ima
   trajan volumen pretrage u Srbiji od 2023, ima sopstveni vokabular, a „testeri parfema"
   vodi na KupujemProdajem — **nijedan legalan trgovac tu tražnju ne uslužuje sistematski.** — *(VISOKA za tražnju, SREDNJA za veličinu)*
10. **Redosled kanala je: TikTok otkriva → vršnjak potvrđuje → radnja odlučuje.** 81% Gen Z-a
    preferira fizičku radnju (više od svih generacija); 92% dolazi da vidi, dodirne i proba.
    Nijedan korak se ne preskače. — *(VISOKA)*
11. **Ali u Srbiji samo 2% potpuno veruje influenserima** (Social Serbia 2025, n=1.000).
    Plaćena preporuka ne prolazi kao dokaz — prolazi kao podsticaj da se ode i proba. **KPI
    influencer kampanje mora biti dolazak i testiranje, ne prodaja preko koda.** — *(VISOKA)*
12. **Regionalni autoritet je jedan: „Čovek Parfem" (Viktor Mihajlović)** — vodeći parfemski
    kanal na Balkanu, radi i sadržaj o dm/Lilly cenovnoj zoni. Njegova publika je starija od
    ciljne grupe → koristiti ga za kredibilitet prema odraslima, a 10–15 mikro-kreatora
    17–24 za samu ciljnu grupu. — *(SREDNJA)*
13. **Tinejdžer sebe ne pretražuje kao tinejdžera.** Upiti „parfem za tinejdžere", „parfem za
    školu", „parfem sa TikToka", „dupe parfem" imaju **nulti volumen** u Srbiji. Kuca ime
    brenda, poređenje („parfem sličan … ali jeftiniji") ili referencu na miris. **SEO i naming
    se ne grade oko demografskih fraza.** — *(VISOKA)*
14. **Korekcija ka Fazi 2B: body mist u Srbiji ima ~4% volumena pretrage upita „parfem", a
    autocomplete i dalje daje „mist za telo šta je".** Kategorija je visok potencijal / niska
    svesnost. Predloženih 20% prostora treba zadržati, ali uz **obaveznu edukaciju i probanje** —
    zid bez objašnjenja neće prodavati. — *(VISOKA)*
15. **Poklon je dvosmeran i sezonski oštar.** Decembarski vrh pretrage je **1,7×** iznad
    aprilskog minimuma; poklon-setovi rastu +26% god/god. Tri različite poklon situacije traže
    tri različita rešenja, a **treća — „tinejdžer traži da mu se kupi" — danas nije uslužena
    ni kod jednog trgovca u Srbiji.** Rešenje je wishlist + fizička QR kartica, jeftino i u
    obimu otvaranja. — *(VISOKA)*
16. **Kozmetika je četvrta stavka u budžetu regionalnog tinejdžera (32%)**, iza izlazaka
    (62%), hrane (62%) i odeće (40%). Stavke ispred nje su socijalne → **odlazak u tržni
    centar sa društvom je isti budžet iz kog se plaća parfem.** Radnja usput dobija impuls;
    radnja koja traži namensko putovanje ne. — *(SREDNJA — hrvatski uzorak n=1.011, 2020)*

**Tri stvari koje ovo menja za KLAUDS:**

- **Radnja se ne organizuje po brendovima nego po referencama i posledicama.** Podatak o
  jeziku pretrage („miriše na čisto", „sličan … ali jeftiniji", „ali dobri") je najkonkretniji
  nalaz faze i direktno diktira oznake na polici, filtere u web shopu i copy. Ovo je i ulaz
  u Fazu 6 — ton KLAUDS-a je **posledičan, bez stručnih termina, i otvoren oko cene**.
- **Momci su potcenjeni drugi put — ali problem nije udeo, nego jezik.** Segment raste
  dvostruko brže i troši više po glavi, a traži rang listu umesto kustosiranja. Ako vizuelni
  jezik radnje bude isključivo ženski, 20% iz brifa neće biti dostignuto, a kamoli povećano.
  Treba zasebna zona od prvog dana.
- **Format je važniji od liste brendova.** Klijent čeka da mu istraživanje predloži brendove;
  ova faza pokazuje da ista boca prodata kao dekant od 5 € i kao boca od 55 € pogađa dva
  različita kupca — i da je prvi danas potpuno neuslužen u Srbiji. To istovremeno rešava i
  problem preklapanja sa Almarom (iste kuće, drugi format) i cilj prosečne cene artikla.


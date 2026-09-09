# PDF pipeline za KLAUDS izveštaj

Skripte kojima se iz Markdown-a pravi klijentski PDF. Ranije su živele samo u
privremenom folderu sesije, pa su se gubile; sada stoje ovde.

## Kako se pokreće

1. Grafikoni (Pillow):
   `python3 sabloni/pdfgen/charts.py 85.6`
   Argument je broj Lilly TikTok pratilaca u hiljadama. Upisuje u `03-isporuke/slike/`.

2. PDF (traži playwright + pypdf u virtuelnom okruženju):
   `<venv>/bin/python sabloni/pdfgen/render.py`
   Radi u dva prolaza: prvi nalazi na kojoj je strani koje poglavlje, drugi upisuje
   te brojeve u sadržaj. Rezultat: `03-isporuke/KLAUDS_analiza_trzista_i_preporuke.pdf`.

## Na šta paziti

- `md2html.py`, promenljiva `pb`: lista podnaslova pred kojima se lomi strana.
  Nikad ne stavljati prvi podnaslov poglavlja, jer tada naslov poglavlja ostane
  sam na strani (to se desilo poglavlju 10 u verziji 2.0).
- Kurziv (`*tekst*`) sme da prelomi red, ali ne i prazan red.
- Red teksta ne sme da počne brojem i tačkom (npr. „1.529 RSD"), jer to Markdown
  čita kao numerisanu listu. Prelomiti red ranije.
- Posle generisanja grafikona proveriti da nijedan tekst ne dodiruje desnu ivicu.

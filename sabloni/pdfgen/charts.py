#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Jednostavni grafici za KLAUDS izvestaj (Pillow, bez matplotlib-a)."""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = "/Users/marko/Desktop/Marko/belodore-istrazivanje/03-isporuke/slike"
os.makedirs(OUT, exist_ok=True)

VIOLET = "#5B3DF5"; CLOUD = "#F0EEE9"; INK = "#14121C"; VAPOR = "#CFC6FF"; PULSE = "#00E5A0"
MUTED = "#615C71"; LINE = "#C9C5BE"; WHITE = "#FFFFFF"; PULSE_DARK = "#00835B"

FONT_DIR = "/System/Library/Fonts/Supplemental/"
def font(size, bold=False):
    for name in (["Arial Bold.ttf", "Arial.ttf"] if bold else ["Arial.ttf"]):
        p = os.path.join(FONT_DIR, name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def canvas(w, h, bg=WHITE):
    im = Image.new("RGB", (w, h), bg)
    return im, ImageDraw.Draw(im)

def text_w(d, t, f):
    b = d.textbbox((0, 0), t, font=f)
    return b[2] - b[0]

def save(im, name):
    im.save(os.path.join(OUT, name), optimize=True)
    print("ok", name)

# ------------------------------------------------------------------ 1. paleta
def paleta():
    sw = [("KLAUDS VIOLET", "#5B3DF5", "logo, kesa, traka, znak, dugmad"),
          ("CLOUD", "#F0EEE9", "zidovi, police, ambalaža, sajt"),
          ("INK", "#14121C", "tekst, ram police, muška zona"),
          ("VAPOR", "#CFC6FF", "oznake zona, poklon zona"),
          ("PULSE", "#00E5A0", "TOP 10, cene, NOVO, odbrojavanje")]
    W, H = 1800, 520
    im, d = canvas(W, H)
    d.text((40, 30), "Paleta KLAUDS", font=font(40, True), fill=INK)
    d.text((40, 82), "Pet boja, tri pravila: Violet je znak, ne enterijer · muška zona je Ink i Pulse · Pulse samo za ono što je novo",
           font=font(22), fill=MUTED)
    n = len(sw); gap = 30; x0 = 40; bw = (W - 2 * x0 - gap * (n - 1)) // n
    for i, (name, hexv, use) in enumerate(sw):
        x = x0 + i * (bw + gap); y = 140
        d.rounded_rectangle([x, y, x + bw, y + 210], radius=18, fill=hexv, outline=LINE if hexv.upper() in ("#F0EEE9",) else None, width=2)
        d.text((x, y + 230), name, font=font(28, True), fill=INK)
        d.text((x, y + 268), hexv, font=font(24), fill=MUTED)
        d.text((x, y + 302), use, font=font(20), fill=INK)
    # kontrast primeri
    y = 480
    d.text((40, y), "Kontrast: Violet na Cloud 5,28:1 (AA) · Pulse na Ink 11,34:1 (AAA) · Ink na Cloud 16,2:1 (AAA)",
           font=font(20), fill=MUTED)
    save(im, "paleta.png")

# ---------------------------------------------------- 2. mapa pozicioniranja
def mapa():
    W, H = 1600, 1100
    im, d = canvas(W, H)
    d.text((40, 30), "Mapa pozicioniranja: cena naspram iskustva u prodavnici", font=font(36, True), fill=INK)
    d.text((40, 78), "Kvalitativna procena na osnovu izmerenih cena i analize koncepata; položaj je relativan, ne merenje.",
           font=font(20), fill=MUTED)
    L, T, R, B = 140, 150, W - 60, H - 130
    d.rectangle([L, T, R, B], fill="#FAF9F6", outline=LINE, width=2)
    # ose
    d.line([L, B, R, B], fill=INK, width=3); d.line([L, T, L, B], fill=INK, width=3)
    d.text((L, B + 20), "niža cena", font=font(22, True), fill=INK)
    t = "viša cena"; d.text((R - text_w(d, t, font(22, True)), B + 20), t, font=font(22, True), fill=INK)
    t = "CENA (prosečan artikal)"; d.text(((L + R) // 2 - text_w(d, t, font(22)) // 2, B + 55), t, font=font(22), fill=MUTED)
    # y label (rotated)
    lab = Image.new("RGBA", (700, 40), (255, 255, 255, 0)); ld = ImageDraw.Draw(lab)
    ld.text((0, 0), "ISKUSTVO: polica  →  probanje, odabran asortiman, doživljaj", font=font(22), fill=MUTED)
    lab = lab.rotate(90, expand=True); im.paste(lab, (40, (T + B) // 2 - 350), lab)
    # mreza
    for k in range(1, 4):
        x = L + (R - L) * k // 4; y = T + (B - T) * k // 4
        d.line([x, T, x, B], fill="#E6E3DD", width=1); d.line([L, y, R, y], fill="#E6E3DD", width=1)
    def P(px, py):  # 0..1
        return (L + (R - L) * px, B - (B - T) * py)
    pts = [("Onlajn diskonteri", 0.10, 0.06, MUTED), ("dm", 0.18, 0.22, MUTED), ("Zara", 0.14, 0.30, MUTED),
           ("Lilly", 0.30, 0.28, MUTED), ("Victoria's Secret", 0.42, 0.50, MUTED),
           ("ALMARA (DP Lux)", 0.50, 0.46, "#B8892B"), ("Jasmin", 0.72, 0.42, MUTED),
           ("Sephora", 0.78, 0.76, MUTED), ("Belodore (DP Lux)", 0.86, 0.90, "#B8892B"),
           ("KLAUDS (predlog)", 0.32, 0.86, VIOLET)]
    for name, px, py, col in pts:
        x, y = P(px, py); r = 16 if col == VIOLET else 11
        d.ellipse([x - r, y - r, x + r, y + r], fill=col)
        f = font(26, True) if col == VIOLET else font(22, col != MUTED)
        tx = x + r + 8
        if tx + text_w(d, name, f) > R:      # natpis levo od tacke da ostane unutar okvira
            tx = x - r - 8 - text_w(d, name, f)
        d.text((tx, y - 14), name, font=f, fill=col if col != MUTED else INK)
    # zona praznine
    x1, y1 = P(0.12, 0.62); x2, y2 = P(0.52, 0.98)
    d.rounded_rectangle([x1, y2, x2, y1], radius=24, outline=VIOLET, width=3)
    d.text((x1 + 16, y2 + 14), "Nepokriveno među analiziranim kanalima:", font=font(20, True), fill=VIOLET)
    d.text((x1 + 16, y2 + 42), "cena koju tinejdžer plaća sam + probanje + odabran i često osvežavan asortiman", font=font(18), fill=VIOLET)
    save(im, "mapa_pozicioniranja.png")

# ------------------------------------------------------- 3. cenovna lestvica
def lestvica():
    rows = [("Dizajnerski parfem 100 ml", 95, 140), ("Dizajnerski 30 ml", 65, 100),
            ("Viralni orijentalni 60–100 ml (Lattafa, Armaf, Afnan)", 29, 46),
            ("Victoria's Secret body mist 250 ml", 25, 30), ("Celebrity EDP 30 ml (Sabrina Carpenter)", 23, 34),
            ("Mass parfem 30 ml", 15.3, 25.6), ("Zara parfem", 7.6, 18),
            ("Sabrina Carpenter body mist 236 ml (dm)", 10.6, 12.8), ("Manoard (domaći)", 4.8, 21),
            ("Sephora Collection šminka", 5.7, 20.7)]
    W = 1880; rh = 58; H = 200 + rh * len(rows) + 90
    im, d = canvas(W, H)
    d.text((40, 30), "Cenovna lestvica u Srbiji (EUR, izmereno 28.08. do 09.09.2026)", font=font(36, True), fill=INK)
    d.text((40, 78), "Zelena traka: preporučena zona jezgra KLAUDS-a 25 do 35 €. Ljubičasta: ulazna tačka 6 do 12 €.", font=font(20), fill=MUTED)
    L = 640; R = W - 230; T = 150; B = T + rh * len(rows)
    vmax = 150.0
    def X(v): return L + (R - L) * v / vmax
    d.rectangle([X(25), T - 10, X(35), B + 10], fill="#DDF7EC")
    d.rectangle([X(6), T - 10, X(12), B + 10], fill="#E9E5FF")
    for v in range(0, 151, 25):
        d.line([X(v), T - 10, X(v), B + 10], fill="#E6E3DD", width=1)
        d.text((X(v) - 12, B + 16), str(v), font=font(18), fill=MUTED)
    d.text((R - 40, B + 40), "EUR", font=font(18), fill=MUTED)
    for i, (name, lo, hi) in enumerate(rows):
        y = T + i * rh + rh // 2
        d.text((40, y - 12), name, font=font(21), fill=INK)
        d.rounded_rectangle([X(lo), y - 12, X(hi), y + 12], radius=8, fill=VIOLET if hi <= 60 else "#918BA3")
        lab = f"{lo:g}–{hi:g} €".replace(".", ",")
        d.text((X(hi) + 10, y - 12), lab, font=font(20, True), fill=INK)
    save(im, "cenovna_lestvica.png")

# ------------------------------------------------------ 4. scenariji korpe
def korpa():
    W, H = 1500, 720
    im, d = canvas(W, H)
    d.text((40, 30), "Vrednost korpe: procena, cilj i cilj iz brifa (EUR)", font=font(36, True), fill=INK)
    d.text((40, 78), "Sve vrednosti su poslovne hipoteze izvedene iz izmerenih cena artikala, ne merenje. Stvarna korpa se meri od prvog dana rada.",
           font=font(20), fill=MUTED)
    bars = [("Procenjena\npočetna korpa", 35, 35, "#918BA3"), ("Cilj prve godine\n(posle mehanika)", 40, 40, VIOLET),
            ("Cilj druge\ngodine", 45, 60, VIOLET), ("Cilj iz brifa", 50, 50, PULSE_DARK)]
    L, T, R, B = 120, 150, W - 60, H - 130; vmax = 70
    def Y(v): return B - (B - T) * v / vmax
    for v in range(0, 71, 10):
        d.line([L, Y(v), R, Y(v)], fill="#E6E3DD", width=1); d.text((60, Y(v) - 12), str(v), font=font(18), fill=MUTED)
    n = len(bars); bw = 180; gap = (R - L - n * bw) // (n + 1)
    for i, (name, lo, hi, col) in enumerate(bars):
        x = L + gap + i * (bw + gap)
        d.rectangle([x, Y(hi), x + bw, Y(0)], fill=col if lo == hi else "#E9E5FF")
        if lo != hi:
            d.rectangle([x, Y(hi), x + bw, Y(lo)], fill=col)
            d.rectangle([x, Y(lo), x + bw, Y(0)], fill="#E9E5FF")
        lab = f"{lo} €" if lo == hi else f"{lo}–{hi} €"
        d.text((x + bw // 2 - text_w(d, lab, font(26, True)) // 2, Y(hi) - 40), lab, font=font(26, True), fill=INK)
        for j, line in enumerate(name.split("\n")):
            d.text((x + bw // 2 - text_w(d, line, font(20)) // 2, B + 16 + j * 26), line, font=font(20), fill=INK)
    save(im, "korpa_scenariji.png")

# ------------------------------------------------------ 5. ciljna grupa
def grupa():
    W, H = 1500, 620
    im, d = canvas(W, H)
    d.text((40, 30), "Ciljna grupa 15 do 19 godina u Srbiji", font=font(36, True), fill=INK)
    d.text((40, 78), "Levo: procenjen broj stanovnika 15–19 (RZS, 2024). Desno: gde srednjoškolci pohađaju školu (RZS, 2025/2026).", font=font(20), fill=MUTED)
    # levo: broj
    d.rounded_rectangle([40, 140, 700, 560], radius=20, fill="#FAF9F6", outline=LINE, width=2)
    d.text((70, 170), "330.698", font=font(84, True), fill=VIOLET)
    d.text((70, 275), "osoba uzrasta 15 do 19 godina (2024)", font=font(24), fill=INK)
    d.text((70, 330), "170.028 momaka · 160.670 devojaka", font=font(22), fill=MUTED)
    d.text((70, 380), "Popis 2002: 497.864", font=font(22), fill=MUTED)
    d.text((70, 412), "Kohorta se za 22 godine smanjila za trećinu.", font=font(22), fill=MUTED)
    d.text((70, 470), "225.639 učenika u redovnim srednjim školama", font=font(22, True), fill=INK)
    d.text((70, 502), "(školska 2025/2026)", font=font(20), fill=MUTED)
    # desno: donut, legenda ispod njega (ranije desno, pa je izlazila van platna)
    cx, cy, r = 1010, 300, 130
    d.pieslice([cx - r, cy - r, cx + r, cy + r], start=-90, end=-90 + 360 * 0.265, fill=VIOLET)
    d.pieslice([cx - r, cy - r, cx + r, cy + r], start=-90 + 360 * 0.265, end=270, fill=VAPOR)
    d.ellipse([cx - 74, cy - 74, cx + 74, cy + 74], fill=WHITE)
    t = "26,5%"; d.text((cx - text_w(d, t, font(36, True)) // 2, cy - 28), t, font=font(36, True), fill=VIOLET)
    t = "Beograd"; d.text((cx - text_w(d, t, font(19)) // 2, cy + 16), t, font=font(19), fill=MUTED)
    lx = 760
    for i, (col, lab) in enumerate(((VIOLET, "Beogradski region: 59.682 (26,5%)"), (VAPOR, "Ostali regioni: 73,5%"))):
        y = 452 + i * 38
        d.rectangle([lx, y, lx + 26, y + 26], fill=col)
        d.text((lx + 40, y + 1), lab, font=font(21), fill=INK)
    d.text((lx, 538), "Udeli se odnose na upisane srednjoškolce, ne na mesto stanovanja cele populacije 15–19.",
           font=font(18), fill=MUTED)
    save(im, "ciljna_grupa.png")

# ------------------------------------------------------ 6. pratioci trgovaca
def pratioci(lilly_tt=None):
    data_tt = [("Jasmin", 196), ("dm Srbija", 168), ("Sephora Srbija", 19.4)]
    if lilly_tt: data_tt.insert(1, ("Lilly", lilly_tt))
    data_ig = [("dm Srbija", 356), ("Lilly", 355), ("Jasmin", 181)]
    W, H = 1500, 640
    im, d = canvas(W, H)
    d.text((40, 30), "Domaći trgovci na društvenim mrežama (broj pratilaca u hiljadama)", font=font(34, True), fill=INK)
    d.text((40, 76), "Očitano sa naloga 28.08.2026. Sa mladima se već razgovara; praznina je u polici i ceni, ne u komunikaciji.", font=font(20), fill=MUTED)
    def panel(x0, title, data, col):
        d.text((x0, 130), title, font=font(26, True), fill=INK)
        vmax = 400.0; L = x0 + 170; R = x0 + 640
        for i, (n, v) in enumerate(data):
            y = 190 + i * 70
            d.text((x0, y + 8), n, font=font(22), fill=INK)
            w = (R - L) * v / vmax
            d.rounded_rectangle([L, y, L + w, y + 40], radius=8, fill=col)
            d.text((L + w + 12, y + 8), f"{v:g}K".replace(".", ","), font=font(22, True), fill=INK)
    panel(40, "TikTok", data_tt, INK)
    panel(780, "Instagram", data_ig, VIOLET)
    save(im, "pratioci_trgovaca.png")

if __name__ == "__main__":
    import sys
    paleta(); mapa(); lestvica(); korpa(); grupa()
    lt = float(sys.argv[1]) if len(sys.argv) > 1 else None
    pratioci(lt)

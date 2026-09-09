#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KLAUDS finalni izvestaj: Markdown -> print-ready HTML (A4)."""
import re, html, sys, json, os

SRC = "/Users/marko/Desktop/Marko/belodore-istrazivanje/03-isporuke/KLAUDS_analiza_trzista_i_preporuke.md"
IMG_DIR = "/Users/marko/Desktop/Marko/belodore-istrazivanje/03-isporuke"

# ---------------------------------------------------------------- inline

ICONS = {
    "⏱ ROK": '<span class="chip chip-rok">ROK</span>',
    "⚠️": '<span class="ic ic-warn" aria-hidden="true"></span>',
    "⚠": '<span class="ic ic-warn" aria-hidden="true"></span>',
    "⏱": '<span class="chip chip-rok">ROK</span>',
    "⚑": '<span class="chip chip-novo">NOVO</span>',
    "⚖️": '<span class="chip chip-pravno">PRAVNO</span>',
    "⚖": '<span class="chip chip-pravno">PRAVNO</span>',
    "✅": '<span class="tick">✓</span>',
    "✓": '<span class="tick">✓</span>',
    "❌": '<span class="cross">✕</span>',
    "⛔": '<span class="cross">✕</span>',
    "🔴": '<span class="dot d-red"></span>',
    "🟠": '<span class="dot d-amber"></span>',
    "🟡": '<span class="dot d-amber"></span>',
    "🟢": '<span class="dot d-green"></span>',
    "🔵": '<span class="dot d-blue"></span>',
    "⬜": '<span class="box"></span>',
    "⬇": "↓",
    "→": "→",
}

def icons(t):
    for k, v in ICONS.items():
        t = t.replace(k, v)
    return t

def inline(t):
    """Inline markdown -> HTML. Input is raw markdown text (not escaped)."""
    ph = []

    def stash(h):
        ph.append(h)
        return "\x00%d\x00" % (len(ph) - 1)

    # code spans first
    t = re.sub(r"`([^`]+)`", lambda m: stash("<code>" + html.escape(m.group(1)) + "</code>"), t)
    # links
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",
               lambda m: stash('<a href="%s">%s</a>' % (html.escape(m.group(2), True), html.escape(m.group(1)))), t)
    # bold then italic
    t = html.escape(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t, flags=re.S)
    # kurziv sme da prelomi red, ali ne i da pređe prazan red (kraj pasusa)
    t = re.sub(r"(?<![\*\w])\*((?:[^*\n]|\n(?!\n))+?)\*(?!\*)", r"<em>\1</em>", t)
    # serbian typographic quotes are already in source; keep
    t = icons(t)
    for i, h in enumerate(ph):
        t = t.replace("\x00%d\x00" % i, h)
    return t

# ---------------------------------------------------------------- helpers

def slug(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[^0-9A-Za-zČĆŠŽĐčćšžđ]+", "-", s).strip("-").lower()
    return s or "x"

def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]

def is_sep(line):
    return bool(re.match(r"^\s*\|?[\s:\-|]+\|[\s:\-|]*$", line)) and "-" in line

def aligns(sep):
    out = []
    for c in split_row(sep):
        c = c.strip()
        if c.startswith(":") and c.endswith(":"):
            out.append("center")
        elif c.endswith(":"):
            out.append("right")
        else:
            out.append("left")
    return out

# ---------------------------------------------------------------- block parser

def parse(lines, depth=0):
    """lines: list of str (blockquote markers already stripped). returns html"""
    out = []
    i = 0
    n = len(lines)
    while i < n:
        ln = lines[i]
        s = ln.strip()

        # blank
        if not s:
            i += 1
            continue

        # fenced code
        if s.startswith("```"):
            j = i + 1
            buf = []
            while j < n and not lines[j].strip().startswith("```"):
                buf.append(lines[j])
                j += 1
            out.append('<pre class="diagram">%s</pre>' % html.escape("\n".join(buf)))
            i = j + 1
            continue

        # horizontal rule
        if re.match(r"^\s*(---|\*\*\*|___)\s*$", ln):
            out.append('<hr class="rule">')
            i += 1
            continue

        # heading
        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            lvl = len(m.group(1))
            txt = m.group(2).strip()
            hid = slug(txt)
            # prelom strane pred odredjenim podnaslovima; NIKAD pred prvim
            # podnaslovom poglavlja, jer tada H1 ostaje sam na strani
            pb = any(k in txt for k in ("5.8 Četiri persone", "7.2 Grupa A", "5.5 Šta pokazuje TikTok"))
            out.append('<h%d id="%s"%s>%s</h%d>' % (lvl, hid, ' class="pb"' if pb else "", inline(txt), lvl))
            i += 1
            continue

        # blockquote
        if s.startswith(">"):
            buf = []
            while i < n and (lines[i].strip().startswith(">") or
                             (lines[i].strip() == "" and i + 1 < n and lines[i + 1].strip().startswith(">"))):
                cur = lines[i]
                cur = re.sub(r"^\s*>\s?", "", cur)
                buf.append(cur)
                i += 1
            inner_raw = "\n".join(buf)
            cls = "callout"
            if "⚠" in inner_raw:
                cls += " callout-warn"
            if "⏱" in inner_raw or "ROK" in inner_raw[:120]:
                cls += " callout-rok"
            if "⚑" in inner_raw:
                cls += " callout-novo"
            if "ČEKA ODGOVOR" in inner_raw or "ČEKA MIŠLJENJE" in inner_raw or "ZADATAK ZA PRAVNIKA" in inner_raw:
                cls += " callout-ceka"
            out.append('<div class="%s">%s</div>' % (cls, parse(buf, depth + 1)))
            continue

        # table
        if s.startswith("|") and i + 1 < n and is_sep(lines[i + 1]):
            head = split_row(lines[i])
            al = aligns(lines[i + 1])
            j = i + 2
            rows = []
            while j < n and lines[j].strip().startswith("|"):
                rows.append(split_row(lines[j]))
                j += 1
            is_src = len(head) == 4 and "Naziv izvora" in head[1]
            wide = (not is_src) and (len(head) >= 6 or any(len(" ".join(r)) > 260 for r in rows))
            th = []
            for k, c in enumerate(head):
                a = al[k] if k < len(al) else "left"
                th.append('<th class="a-%s">%s</th>' % (a, inline(c)))
            trs = []
            for r in rows:
                tds = []
                for k, c in enumerate(r):
                    a = al[k] if k < len(al) else "left"
                    tds.append('<td class="a-%s">%s</td>' % (a, inline(c)))
                trs.append("<tr>%s</tr>" % "".join(tds))
            keep = (len(rows) <= 9 and sum(len(" ".join(r)) for r in rows) < 2300)
            cls = " tw-wide" if wide else ""
            if keep and not is_src:
                cls += " tw-keep"
            cg = ""
            if is_src:
                cls = " tw-src"
                cg = ('<colgroup><col style="width:7%"><col style="width:41%">'
                      '<col style="width:45%"><col style="width:7%"></colgroup>')
            out.append(
                '<div class="tw%s"><table>%s<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
                % (cls, cg, "".join(th), "".join(trs))
            )
            i = j
            continue

        # lists (unordered / ordered / checkbox)
        m = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", ln)
        if m:
            base_indent = len(m.group(1))
            ordered = bool(re.match(r"^\d+\.$", m.group(2)))
            items = []
            cur = None
            while i < n:
                mm = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", lines[i])
                if mm and len(mm.group(1)) <= base_indent:
                    if cur is not None:
                        items.append(cur)
                    cur = [mm.group(3)]
                    i += 1
                    continue
                if lines[i].strip() == "":
                    # blank line: continue only if next is a deeper continuation of this list
                    if i + 1 < n and re.match(r"^\s{%d,}\S" % (base_indent + 1), lines[i + 1]):
                        cur.append("")
                        i += 1
                        continue
                    break
                if cur is not None and lines[i].startswith(" " * (base_indent + 1)):
                    cur.append(lines[i].strip())
                    i += 1
                    continue
                break
            if cur is not None:
                items.append(cur)

            lis = []
            for it in items:
                body = "\n".join(it)
                cb = re.match(r"^\[([ xX])\]\s*(.*)$", body, flags=re.S)
                if cb:
                    mark = '<span class="box%s"></span>' % (" box-on" if cb.group(1).strip() else "")
                    lis.append('<li class="chk">%s<span>%s</span></li>' % (mark, inline(cb.group(2).strip())))
                else:
                    lis.append("<li>%s</li>" % inline(body.strip()))
            tag = "ol" if ordered else "ul"
            has_cb = any('class="chk"' in x for x in lis)
            out.append('<%s class="%s">%s</%s>' % (tag, "chklist" if has_cb else "md", "".join(lis), tag))
            continue

        # image
        mi = re.match(r"^!\[([^\]]*)\]\(([^)\s]+)\)\s*$", s)
        if mi:
            src = mi.group(2)
            if not src.startswith("/"):
                src = os.path.join(IMG_DIR, src)
            out.append('<figure class="fig"><img src="file://%s" alt="%s"></figure>' % (html.escape(src, True), html.escape(mi.group(1))))
            i += 1
            continue

        # paragraph
        buf = [ln.strip()]
        i += 1
        while i < n:
            nxt = lines[i]
            t = nxt.strip()
            if (not t or t.startswith("#") or t.startswith(">") or t.startswith("|")
                    or t.startswith("```") or re.match(r"^\s*(---|\*\*\*|___)\s*$", nxt)
                    or re.match(r"^(\s*)([-*+]|\d+\.)\s+", nxt)):
                break
            buf.append(t)
            i += 1
        out.append("<p>%s</p>" % inline(" ".join(buf)))
    return "\n".join(out)

# ---------------------------------------------------------------- document

def build(toc_pages=None):
    raw = open(SRC, encoding="utf-8").read()
    lines = raw.split("\n")

    # ---- cut off the source front matter (title block + status note + SADRZAJ)
    idx_exec = next(i for i, l in enumerate(lines) if l.strip().startswith("# 1. KONTEKST"))
    front = lines[:idx_exec]
    body_lines = lines[idx_exec:]

    # status note from front matter (the blockquote)
    q = [l for l in front if l.strip().startswith(">")]
    status_html = parse([re.sub(r"^\s*>\s?", "", l) for l in q])

    # contents table from front matter
    toc_rows = []
    infront = False
    for l in front:
        st = l.strip()
        if st.startswith("| # | Poglavlje"):
            infront = True
            continue
        if infront:
            if is_sep(l):
                continue
            if st.startswith("|"):
                c = split_row(l)
                if len(c) >= 3:
                    toc_rows.append((c[0], c[1], c[2]))
                continue
            if st == "":
                continue
            break

    deliver_note = ""
    for k, l in enumerate(front):
        if l.strip().startswith("**Gde su isporuke"):
            blk = []
            j = k
            while j < len(front) and front[j].strip():
                blk.append(front[j].strip())
                j += 1
            deliver_note = "<p>%s</p>" % inline(" ".join(blk))
            break

    body_html = parse(body_lines)

    # wrap each chapter in its own section so a forced page break can never
    # leave a phantom blank page after a full preceding page
    parts = re.split(r'(?=<h1 )', body_html)
    parts = [x for x in parts if x.strip()]
    # the markdown puts a "---" before every chapter; that trailing rule would
    # spill onto a page of its own when the previous page is exactly full
    parts = [re.sub(r'(?:\s*<hr class="rule">\s*)+$', "", x) for x in parts]
    body_html = "\n".join('<section class="chapter">%s</section>' % x for x in parts)

    # anchors for toc: map row label -> heading id
    def hid_for(label):
        lab = re.sub(r"<[^>]+>|\*\*", "", label).strip()
        for l in body_lines:
            st = l.strip()
            if st.startswith("# "):
                t = st[2:].strip()
                if lab in ("A", "B", "C"):
                    if t.startswith("PRILOG " + lab):
                        return slug(t)
                elif t.startswith(lab + ". "):
                    return slug(t)
        return ""

    toc_html = []
    for num, title, desc in toc_rows:
        n_clean = re.sub(r"\*\*|`", "", num).strip()
        t_clean = re.sub(r"\*\*", "", title).strip()
        pg = ""
        if toc_pages:
            key = hid_for(n_clean)
            if key in toc_pages:
                pg = str(toc_pages[key])
        big = n_clean in ("2", "13")
        toc_html.append(
            '<div class="toc-row%s"><span class="toc-n">%s</span>'
            '<span class="toc-t">%s</span><span class="toc-d">%s</span>'
            '<span class="toc-p">%s</span></div>'
            % (" toc-key" if big else "", html.escape(n_clean), inline(t_clean), inline(desc), pg)
        )
    toc_html = "\n".join(toc_html)

    css = open(os.path.join(os.path.dirname(__file__), "report.css"), encoding="utf-8").read()

    doc = """<!DOCTYPE html>
<html lang="sr"><head>
<meta charset="utf-8">
<title>KLAUDS · Analiza tržišta i strateške preporuke</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..800&family=Source+Serif+4:opsz,wght@8..60,400..600&display=block">
<style>%s</style>
</head><body>

<section class="cover">
  <div class="cover-top">
    <span class="cv-brand">VladsDigital</span>
    <span class="cv-for">za DP Lux Group</span>
  </div>
  <div class="cover-mid">
    <p class="cv-mark">KLAUDS</p>
    <h1 class="cv-title">Analiza tržišta i strateške preporuke</h1>
    <p class="cv-sub">Ko je kupac, gde je praznina, po kojoj ceni i koje odluke slede. Verzija za donošenje ključnih odluka.</p>
  </div>
  <div class="cover-bot">
    <div class="cv-meta">
      <div><span class="k">Datum</span><span class="v">9. septembar 2026.</span></div>
      <div><span class="k">Verzija</span><span class="v">2.1</span></div>
      <div><span class="k">Izvora</span><span class="v">426</span></div>
      <div><span class="k">Za koga</span><span class="v">Menadžment i vlasnik, interno</span></div>
    </div>
  </div>
  <div class="cv-band"></div>
</section>

<section class="frontmatter">
  <h2 class="fm-h">Sadržaj</h2>
  <div class="toc">%s</div>
  %s
  <div class="fm-status">
    <p class="fm-lab">O ovom dokumentu</p>
    %s
  </div>
  <div class="fm-legend">
    <p class="fm-lab">Oznake pouzdanosti</p>
    <div class="lg">
      <div><b>VISOKA</b><span>Više nezavisnih izvora, zvaničan podatak, ili sopstveno merenje koje se može ponoviti.</span></div>
      <div><b>SREDNJA</b><span>Jedan solidan izvor, posredan zaključak, ili podatak od izvora sa komercijalnim interesom.</span></div>
      <div><b>NISKA</b><span>Pretpostavka, procena ili radna konstrukcija. Ne koristi se za finansijsku projekciju.</span></div>
    </div>
  </div>
</section>

<main class="doc">
%s
</main>

</body></html>""" % (css, toc_html, deliver_note, status_html, body_html)
    return doc


if __name__ == "__main__":
    pages = None
    if len(sys.argv) > 2 and os.path.exists(sys.argv[2]):
        pages = json.load(open(sys.argv[2], encoding="utf-8"))
    open(sys.argv[1], "w", encoding="utf-8").write(build(pages))
    print("written", sys.argv[1])

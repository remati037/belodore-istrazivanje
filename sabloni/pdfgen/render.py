#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render KLAUDS report HTML -> branded A4 PDF (cover + numbered body, merged)."""
import os, re, json, sys, unicodedata
from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = "/Users/marko/Desktop/Marko/belodore-istrazivanje/03-isporuke"
FINAL = os.path.join(OUT_DIR, "KLAUDS_analiza_trzista_i_preporuke.pdf")

FOOTER = """
<div style="width:100%;box-sizing:border-box;padding:0 17mm;-webkit-print-color-adjust:exact;">
  <div style="border-top:0.5px solid #E3E0DB;padding-top:2.2mm;display:flex;
              justify-content:space-between;align-items:baseline;
              font-family:Helvetica,Arial,sans-serif;font-size:7pt;color:#8C8699;">
    <span style="letter-spacing:0.11em;text-transform:uppercase;">KLAUDS &nbsp;&middot;&nbsp; Analiza tr&#382;i&#353;ta i strate&#353;ke preporuke &nbsp;&middot;&nbsp; VladsDigital za DP Lux Group</span>
    <span style="font-weight:700;color:#5B3DF5;font-size:8pt;"><span class="pageNumber"></span></span>
  </div>
</div>"""

EMPTY = "<div></div>"


def norm(s):
    s = unicodedata.normalize("NFC", s)
    return re.sub(r"\s+", "", s)


def render(page, html_path, pdf_path, cover=False):
    page.goto("file://" + html_path, wait_until="load")
    page.wait_for_timeout(400)
    page.evaluate("document.fonts.ready")
    page.wait_for_timeout(1200)
    kwargs = dict(path=pdf_path, format="A4", print_background=True,
                  prefer_css_page_size=False)
    if cover:
        kwargs["margin"] = {"top": "0", "bottom": "0", "left": "0", "right": "0"}
        kwargs["display_header_footer"] = False
    else:
        kwargs["margin"] = {"top": "19mm", "bottom": "17mm", "left": "17mm", "right": "17mm"}
        kwargs["display_header_footer"] = True
        kwargs["header_template"] = EMPTY
        kwargs["footer_template"] = FOOTER
        try:
            page.pdf(outline=True, tagged=True, **kwargs)
            return
        except TypeError:
            pass
    page.pdf(**kwargs)


def split_html(full_html):
    """cover.html (only .cover section) + body.html (frontmatter + doc)."""
    head_end = full_html.index("</head>") + len("</head>")
    head = full_html[:head_end]
    body_inner = full_html[full_html.index("<body>") + 6: full_html.rindex("</body>")]
    m = re.search(r'(<section class="cover">.*?</section>)', body_inner, flags=re.S)
    cover = m.group(1)
    rest = body_inner.replace(cover, "", 1)
    cov = head + "<body>" + cover + "</body></html>"
    bod = head + "<body>" + rest + "</body></html>"
    return cov, bod


def heading_pages(pdf_path, headings):
    reader = PdfReader(pdf_path)
    pages = [norm(p.extract_text() or "") for p in reader.pages]
    found = {}
    for hid, text in headings.items():
        key = norm(text)
        for i, pt in enumerate(pages):
            if key and key in pt:
                found[hid] = i + 1
                break
    return found, len(reader.pages)


def main():
    sys.path.insert(0, HERE)
    import md2html

    # ---- pass 1
    full = md2html.build(None)
    cov_html, bod_html = split_html(full)
    p_cov = os.path.join(HERE, "cover.html")
    p_bod = os.path.join(HERE, "body.html")
    open(p_cov, "w", encoding="utf-8").write(cov_html)
    open(p_bod, "w", encoding="utf-8").write(bod_html)

    # collect chapter headings from source
    src = open(md2html.SRC, encoding="utf-8").read().split("\n")
    headings = {}
    for l in src:
        st = l.strip()
        if st.startswith("# "):
            t = st[2:].strip()
            headings[md2html.slug(t)] = re.sub(r"\*\*|`", "", t)

    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page()
        tmp = os.path.join(HERE, "_pass1.pdf")
        render(pg, p_bod, tmp, cover=False)
        pages, npages = heading_pages(tmp, headings)
        print("pass1 body pages:", npages, "| headings located:", len(pages), "/", len(headings))
        missing = [h for h in headings if h not in pages]
        if missing:
            print("  NOT LOCATED:", missing)

        json.dump(pages, open(os.path.join(HERE, "pages.json"), "w"))

        # ---- pass 2 with page numbers in TOC
        full2 = md2html.build(pages)
        cov2, bod2 = split_html(full2)
        open(p_cov, "w", encoding="utf-8").write(cov2)
        open(p_bod, "w", encoding="utf-8").write(bod2)

        pdf_cov = os.path.join(HERE, "_cover.pdf")
        pdf_bod = os.path.join(HERE, "_body.pdf")
        render(pg, p_cov, pdf_cov, cover=True)
        render(pg, p_bod, pdf_bod, cover=False)
        br.close()

    w = PdfWriter()
    w.append(PdfReader(pdf_cov))
    w.append(PdfReader(pdf_bod))
    w.add_metadata({
        "/Title": "KLAUDS · Analiza tržišta i strateške preporuke",
        "/Author": "VladsDigital",
        "/Subject": "Analiza tržišta i strateške preporuke za KLAUDS, retail koncept DP Lux Group",
        "/Keywords": "KLAUDS, DP Lux Group, Belodore, istraživanje tržišta, Gen Z, parfemi",
        "/Creator": "VladsDigital",
    })
    with open(FINAL, "wb") as f:
        w.write(f)

    total = len(PdfReader(FINAL).pages)
    print("FINAL:", FINAL, "|", total, "pages |",
          round(os.path.getsize(FINAL) / 1024 / 1024, 2), "MB")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Build script for SDRBench website.
Converts .md + YAML data into static HTML files.

Usage:
    python build.py          # Build the site
    python build.py serve    # Build and start local server on port 8000
"""

import os
import re
import sys
import yaml
import markdown

SITE_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_TITLE = "SDRBench"

PAGES = [
    {"src": "index.md", "out": "index.html", "url": "/"},
    {"src": "datasets.md", "out": "datasets.html", "url": "/datasets.html"},
    {"src": "tools.md", "out": "tools.html", "url": "/tools.html"},
    {"src": "publications.md", "out": "publications.html", "url": "/publications.html"},
    {"src": "about.md", "out": "about.html", "url": "/about.html"},
]


def read_file(path):
    with open(os.path.join(SITE_DIR, path), encoding="utf-8") as f:
        return f.read()


def write_file(path, content):
    full = os.path.join(SITE_DIR, path)
    os.makedirs(os.path.dirname(full) if os.path.dirname(full) else ".", exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  wrote {path}")


def parse_front_matter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if m:
        fm = yaml.safe_load(m.group(1))
        body = text[m.end():]
        return fm or {}, body
    return {}, text


def md_to_html(md_text):
    return markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "attr_list", "md_in_html"],
    )


def load_datasets():
    return yaml.safe_load(read_file("_data/datasets.yml"))


def build_nav(current_url):
    links = [
        ("/", "index.html", "Home"),
        ("/datasets.html", "datasets.html", "Datasets"),
        ("/tools.html", "tools.html", "Tools"),
        ("/publications.html", "publications.html", "Publications"),
        ("/about.html", "about.html", "About"),
    ]
    items = []
    for url, href, label in links:
        active = ' class="active"' if current_url == url else ""
        items.append(f'<li><a href="{href}"{active}>{label}</a></li>')
    return "\n      ".join(items)


def build_layout(title, content, current_url):
    if title:
        page_title = f"{title} - {SITE_TITLE}"
    else:
        page_title = SITE_TITLE

    nav_html = build_nav(current_url)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{page_title}</title>
  <meta name="description" content="Scientific Data Reduction Benchmarks">
  <style>
    :root {{
      --primary: #0070c0;
      --primary-dark: #005a9e;
      --primary-light: #e8f4fd;
      --accent: #00a4ef;
      --bg: #ffffff;
      --bg-alt: #f5f7fa;
      --text: #2c3e50;
      --text-light: #5a6d7e;
      --border: #dce1e8;
      --code-bg: #f0f3f7;
      --shadow: 0 2px 8px rgba(0,0,0,0.08);
      --radius: 6px;
    }}

    * {{ margin: 0; padding: 0; box-sizing: border-box; }}

    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      color: var(--text);
      line-height: 1.7;
      background: var(--bg);
    }}

    nav {{
      background: var(--primary-dark);
      padding: 0 2rem;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 2px 12px rgba(0,0,0,0.15);
    }}
    nav .nav-inner {{
      max-width: 1200px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    nav .site-title {{
      color: #fff;
      font-size: 1.25rem;
      font-weight: 700;
      text-decoration: none;
      padding: 0.9rem 0;
      letter-spacing: 0.5px;
    }}
    nav ul {{
      list-style: none;
      display: flex;
      gap: 0;
    }}
    nav ul li a {{
      color: rgba(255,255,255,0.85);
      text-decoration: none;
      padding: 1rem 1.25rem;
      display: block;
      font-size: 0.95rem;
      font-weight: 500;
      transition: background 0.2s, color 0.2s;
    }}
    nav ul li a:hover,
    nav ul li a.active {{
      background: rgba(255,255,255,0.12);
      color: #fff;
    }}

    .hero {{
      background: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary) 50%, var(--accent) 100%);
      color: #fff;
      padding: 3.5rem 2rem 3rem;
      text-align: center;
    }}
    .hero h1 {{
      font-size: 2.4rem;
      font-weight: 700;
      margin-bottom: 0.75rem;
      letter-spacing: -0.5px;
      color: #fff;
    }}
    .hero p {{
      font-size: 1.15rem;
      opacity: 0.92;
      max-width: 700px;
      margin: 0 auto;
    }}

    .content {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 2.5rem 2rem;
    }}

    h1 {{ font-size: 2rem; color: var(--primary-dark); margin-bottom: 1rem; }}
    h2 {{
      font-size: 1.5rem;
      color: var(--primary-dark);
      margin: 2.5rem 0 1rem;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
    }}
    h3 {{ font-size: 1.15rem; color: var(--primary); margin: 1.5rem 0 0.75rem; }}
    h4 {{ font-size: 1rem; color: var(--text); margin: 1rem 0 0.5rem; }}

    p {{ margin-bottom: 1rem; }}

    a {{ color: var(--primary); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}

    ul, ol {{ margin: 0.5rem 0 1rem 1.75rem; }}
    li {{ margin-bottom: 0.35rem; }}

    .card {{
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 2rem;
      overflow: hidden;
      scroll-margin-top: 4.5rem;
    }}
    .card-header {{
      background: var(--primary);
      color: #fff;
      padding: 1rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 0.5rem;
    }}
    .card-header h3 {{
      color: #fff;
      margin: 0;
      font-size: 1.2rem;
    }}
    .card-header .badge {{
      background: rgba(255,255,255,0.2);
      padding: 0.25rem 0.75rem;
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 500;
    }}
    .card-body {{
      padding: 1.5rem;
    }}

    .dataset-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
      margin-bottom: 1rem;
    }}
    @media (max-width: 768px) {{
      .dataset-grid {{ grid-template-columns: 1fr; }}
    }}

    .detail-group {{ margin-bottom: 1rem; }}
    .detail-group h4 {{
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--text-light);
      margin: 0 0 0.4rem;
      font-weight: 600;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 0.75rem 0;
      font-size: 0.9rem;
    }}
    th, td {{
      padding: 0.5rem 0.75rem;
      text-align: left;
      border: 1px solid var(--border);
    }}
    th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 600;
      font-size: 0.85rem;
    }}
    td {{ background: var(--bg); }}
    tr:nth-child(even) td {{ background: var(--bg-alt); }}

    .entropy-table {{ width: auto; min-width: 200px; }}
    .entropy-table th, .entropy-table td {{ text-align: center; padding: 0.35rem 0.6rem; }}

    code {{
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
      background: var(--code-bg);
      padding: 0.15rem 0.4rem;
      border-radius: 3px;
      font-size: 0.85em;
    }}
    pre {{
      background: var(--code-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1rem;
      overflow-x: auto;
      margin: 0.5rem 0 1rem;
      font-size: 0.82rem;
      line-height: 1.6;
    }}
    pre code {{ background: none; padding: 0; font-size: inherit; }}

    .download-links {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-top: 0.5rem;
    }}
    .download-links a {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary-dark);
      padding: 0.35rem 0.8rem;
      border-radius: 4px;
      font-size: 0.85rem;
      font-weight: 500;
      transition: background 0.2s;
    }}
    .download-links a:hover {{
      background: var(--primary);
      color: #fff;
      text-decoration: none;
    }}

    .source-info {{
      font-size: 0.88rem;
      color: var(--text-light);
      font-style: italic;
      margin-top: 0.25rem;
    }}

    .alert {{
      background: #fff3cd;
      border: 1px solid #ffc107;
      border-left: 4px solid #ffc107;
      border-radius: var(--radius);
      padding: 1.25rem 1.5rem;
      margin: 1.5rem 0;
    }}
    .alert h3 {{ color: #856404; margin: 0 0 0.75rem; font-size: 1.05rem; }}
    .alert ul {{ margin-bottom: 0; }}

    .info-box {{
      background: var(--primary-light);
      border: 1px solid #b3d7f2;
      border-left: 4px solid var(--primary);
      border-radius: var(--radius);
      padding: 1.25rem 1.5rem;
      margin: 1.5rem 0;
    }}

    .sponsors {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 3rem;
      flex-wrap: wrap;
      padding: 2rem 0;
    }}
    .sponsors img {{
      max-height: 80px;
      width: auto;
      opacity: 0.85;
      transition: opacity 0.2s;
    }}
    .sponsors img:hover {{ opacity: 1; }}

    footer {{
      background: var(--bg-alt);
      border-top: 1px solid var(--border);
      padding: 2rem;
      text-align: center;
      color: var(--text-light);
      font-size: 0.9rem;
    }}

    details {{ margin: 0.5rem 0; }}
    details summary {{
      cursor: pointer;
      font-weight: 600;
      font-size: 0.9rem;
      color: var(--primary);
      padding: 0.25rem 0;
    }}
    details summary:hover {{ color: var(--primary-dark); }}

    .contributors {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 0.5rem;
      list-style: none;
      margin-left: 0;
    }}
    .contributors li {{
      padding: 0.5rem 0.75rem;
      border-left: 3px solid var(--primary-light);
    }}

    .page-header {{
      background: var(--bg-alt);
      border-bottom: 1px solid var(--border);
      padding: 2rem;
    }}
    .page-header .content {{ padding: 0; }}
    .page-header h1 {{ margin-bottom: 0.5rem; }}
    .page-header p {{ color: var(--text-light); margin-bottom: 0; font-size: 1.05rem; }}

    .jump-to {{
      position: relative;
      display: inline-block;
      margin-top: 1rem;
    }}
    .jump-to-btn {{
      background: var(--primary);
      color: #fff;
      border: none;
      padding: 0.55rem 1.25rem;
      border-radius: var(--radius);
      font-size: 0.95rem;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.2s;
    }}
    .jump-to-btn:hover {{ background: var(--primary-dark); }}
    .jump-to-btn::after {{ content: " \\25BC"; font-size: 0.75em; }}
    .jump-to-list {{
      display: none;
      position: absolute;
      left: 0;
      top: 100%;
      margin-top: 4px;
      background: #fff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      box-shadow: 0 4px 16px rgba(0,0,0,0.12);
      min-width: 260px;
      z-index: 50;
      max-height: 70vh;
      overflow-y: auto;
    }}
    .jump-to.open .jump-to-list {{ display: block; }}
    .jump-to-list a {{
      display: block;
      padding: 0.5rem 1rem;
      color: var(--text);
      text-decoration: none;
      font-size: 0.9rem;
      border-bottom: 1px solid var(--bg-alt);
    }}
    .jump-to-list a:hover {{
      background: var(--primary-light);
      color: var(--primary-dark);
    }}
    .jump-to-list a:last-child {{ border-bottom: none; }}

    .hamburger {{
      display: none;
      background: none;
      border: none;
      color: #fff;
      font-size: 1.5rem;
      cursor: pointer;
      padding: 0.5rem;
    }}
    @media (max-width: 600px) {{
      .hamburger {{ display: block; }}
      nav ul {{
        display: none;
        flex-direction: column;
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        background: var(--primary-dark);
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
      }}
      nav ul.open {{ display: flex; }}
      nav ul li a {{ padding: 0.75rem 2rem; }}
    }}
  </style>
</head>
<body>

<nav>
  <div class="nav-inner">
    <a href="index.html" class="site-title">SDRBench</a>
    <button class="hamburger" onclick="document.getElementById('nav-menu').classList.toggle('open')">&#9776;</button>
    <ul id="nav-menu">
      {nav_html}
    </ul>
  </div>
</nav>

{content}

<footer>
  <p>SDRBench &mdash; Scientific Data Reduction Benchmarks</p>
  <p>Established as part of the <a href="https://www.exascaleproject.org/">ECP</a> <a href="https://www.exascaleproject.org/project/codar-co-design-center-online-data-analysis-reduction-exascale/">CODAR</a> project.</p>
</footer>

</body>
</html>"""


def nl2br(text):
    return text.strip().replace("\n", "<br>\n")


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def build_entropy_html(entropy_list):
    if not entropy_list:
        return ""
    parts = []
    for ent in entropy_list:
        label = ent.get("label", "")
        if label:
            parts.append(f"<p><strong>{label}</strong></p>")
        parts.append('<table class="entropy-table">')
        parts.append("<tr><th></th><th>8-bit Entropy</th><th>32-bit Entropy</th></tr>")
        for row in ent.get("rows", []):
            parts.append(
                f'<tr><td><strong>{row["stat"]}</strong></td>'
                f'<td>{row["e8"]}</td><td>{row["e32"]}</td></tr>'
            )
        parts.append("</table>")
    return "\n".join(parts)


def build_commands_html(ds):
    cmds = ds.get("commands", {})
    if cmds.get("sz_compress") == "NA":
        note = ds.get("commands_note", "")
        if note:
            return f'<div class="info-box"><p>{note}</p></div>'
        return ""

    lines = []
    lines.append(f'<b>SZ (Compress):</b>   {cmds.get("sz_compress", "")}')
    lines.append(f'<b>SZ (Decompress):</b> {cmds.get("sz_decompress", "")}')
    lines.append(f'<b>ZFP:</b>              {cmds.get("zfp", "")}')
    lp = cmds.get("libpressio", "")
    if lp:
        lines.append(f'<b>LibPressio:</b>       {lp}')
        note = cmds.get("libpressio_note", "")
        if note:
            lines.append(f"                      {note}")
    zc = cmds.get("zchecker", "")
    if zc:
        lines.append(f'<b>Z-checker:</b>        {zc}')

    code_block = "\n".join(lines)
    return f"""<details>
      <summary>Command Examples</summary>
<pre><code>{code_block}</code></pre>
    </details>"""


def build_links_html(links):
    parts = []
    for link in links:
        parts.append(f'<a href="{link["url"]}">{link["label"]}</a>')
    return "\n".join(parts)


def build_dataset_card(ds):
    name = ds["name"]
    dtype = ds.get("type", "")
    source = ds.get("source", "")
    source_url = ds.get("source_url", "")
    source_note = ds.get("source_note", "")
    fmt = nl2br(ds.get("format", ""))
    size = nl2br(ds.get("size", ""))
    entropy_html = build_entropy_html(ds.get("entropy", []))
    commands_html = build_commands_html(ds)
    links_html = build_links_html(ds.get("links", []))

    source_line = f"<strong>Source:</strong> {source}"
    if source_url:
        source_line += f' (<a href="{source_url}">{source_url}</a>)'
    source_note_html = f'<p class="source-info">{source_note}</p>' if source_note else ""

    entropy_section = ""
    if entropy_html:
        entropy_section = f"""
        <div class="detail-group">
          <h4>Entropy</h4>
          {entropy_html}
        </div>"""

    return f"""
<div class="card" id="{slugify(name)}">
  <div class="card-header">
    <h3>{name}</h3>
    <span class="badge">{dtype}</span>
  </div>
  <div class="card-body">
    <p class="source-info">{source_line}</p>
    {source_note_html}

    <div class="dataset-grid">
      <div>
        <div class="detail-group">
          <h4>Format</h4>
          <p>{fmt}</p>
        </div>
        <div class="detail-group">
          <h4>Size</h4>
          <p>{size}</p>
        </div>
      </div>
      <div>{entropy_section}
      </div>
    </div>

    <div class="detail-group">
      <h4>Download Links</h4>
      <div class="download-links">
        {links_html}
      </div>
    </div>

    {commands_html}
  </div>
</div>"""


def build_jump_dropdown(datasets):
    links = []
    for ds in datasets:
        name = ds["name"]
        anchor = slugify(name)
        links.append(f'<a href="#{anchor}">{name}</a>')
    items = "\n    ".join(links)
    return f"""<div class="jump-to" id="jump-to">
  <button class="jump-to-btn" onclick="document.getElementById('jump-to').classList.toggle('open')">Jump to Dataset</button>
  <div class="jump-to-list" onclick="document.getElementById('jump-to').classList.remove('open')">
    {items}
  </div>
</div>
<script>document.addEventListener('click',function(e){{if(!document.getElementById('jump-to').contains(e.target))document.getElementById('jump-to').classList.remove('open')}})</script>"""


def build_datasets_page(datasets):
    cards = "\n".join(build_dataset_card(ds) for ds in datasets)
    dropdown = build_jump_dropdown(datasets)
    return f"""
<div class="page-header">
  <div class="content">
    <h1>Datasets</h1>
    <p>Reference scientific datasets for benchmarking data reduction techniques. Click on command examples to expand.</p>
    {dropdown}
  </div>
</div>

<div class="content">

<p><em>
<strong>FORMAT:</strong> Describes the data organization, including the number of fields in each data file and the data dimensions.<br>
<strong>SIZE:</strong> Indicates the file size in bytes. Since most datasets are distributed as compressed .tar.gz archives, SIZE typically refers to the size of the corresponding .tar.gz file.
</em></p>

{cards}

</div>"""


def process_md_page(src_file):
    text = read_file(src_file)
    fm, body = parse_front_matter(text)
    html = md_to_html(body)
    return fm, html


def main():
    print("Building SDRBench site...")
    datasets = load_datasets()

    for page in PAGES:
        src = page["src"]
        out = page["out"]
        url = page["url"]

        if src == "datasets.md":
            fm = {"title": "Datasets"}
            content = build_datasets_page(datasets)
        else:
            fm, content = process_md_page(src)

        title = fm.get("title", "")
        html = build_layout(title, content, url)
        write_file(out, html)

    write_file(".nojekyll", "")
    print("Done! Run 'python -m http.server 8000' to preview.")


if __name__ == "__main__":
    main()

    if len(sys.argv) > 1 and sys.argv[1] == "serve":
        import http.server
        import socketserver

        PORT = 8000
        os.chdir(SITE_DIR)
        handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", PORT), handler) as httpd:
            print(f"\nServing at http://localhost:{PORT}")
            print("Press Ctrl+C to stop.")
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\nStopped.")

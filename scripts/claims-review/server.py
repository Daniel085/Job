#!/usr/bin/env python3
"""Claims review: approve or edit the claims in an application package, in context, before rendering PDFs.

Usage: python3 -I scripts/claims-review/server.py [port] [packages-dir]
  port defaults to 8765 (binds 127.0.0.1 only); packages-dir defaults to applications/.
  To try it on the bundled example: python3 -I scripts/claims-review/server.py 8765 examples/applications

Each package that wants review has applications/<pkg>/claims.json:
{
  "role": "Northwind",                     # PDF names: <pdf_prefix>-Resume-<role>.pdf, <pdf_prefix>-Cover-Letter-<role>.pdf
  "pdf_prefix": "Jordan-Avery",            # the candidate's name as it appears in PDF file names (optional)
  "claims": [
    {"id": "c1", "label": "short name", "why": "where it comes from",
     "status": "pending",                  # pending | approved | edited | rejected
     "locations": [{"file": "resume-x.html", "text": "exact text as it appears in the file"}],
     "history": []}
  ]
}
A claim with no locations is a note (for example, wording kept out of the materials until confirmed).

Edits rewrite the text in the source file (HTML-escaped for .html files), so what is approved is what renders.
The checklist's block between <!-- claims:start --> and <!-- claims:end --> is regenerated after every change.
Render is refused while any claim is pending, or rejected while its text is still in the documents.
"""
import datetime
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, unquote, urlparse

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
APPS = os.path.join(ROOT, "applications")
HERE = os.path.dirname(os.path.abspath(__file__))
CHROME_APP = "Google Chrome"
# On macOS, Chrome launched as a bare binary can fail at startup (path_service 1001), so it is launched through
# LaunchServices with its own profile. Elsewhere, the binary is run directly.
CHROME_PROFILE = (os.path.expanduser("~/Library/Application Support/Google/ChromeHeadlessRender")
                  if sys.platform == "darwin" else os.path.join(tempfile.gettempdir(), "claims-review-chrome"))

LETTER_CSS = ("@page{size:letter;margin:0.7in 0.85in}body{font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;"
              "font-size:11px;line-height:1.45;color:#2d3748;max-width:7in;margin:0 auto}h1{font-size:14px;color:#1a365d;"
              "margin:0 0 6px}p{margin:0 0 9px;text-wrap:pretty}hr{border:0;border-top:1px solid #e2e8f0;margin:8px 0}"
              "a{color:#3182ce;text-decoration:none}")
MARK_CSS = ("mark.claim{background:#fef3c7;color:inherit;border-bottom:2px solid #d97706;padding:0 1px;cursor:pointer}"
            "mark.claim.approved,mark.claim.edited{background:#dcfce7;border-color:#16a34a}"
            "mark.claim.rejected{background:#fee2e2;border-color:#dc2626}"
            "mark.claim.active{outline:3px solid #2563eb;outline-offset:1px}"
            "@media print{mark.claim{background:none;border:0;outline:0}}")


# ---------- package helpers ----------

def pkg_dir(pkg):
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", pkg or ""):
        raise ValueError("bad package name")
    d = os.path.join(APPS, pkg)
    if not os.path.isdir(d):
        raise ValueError("no such package")
    return d


def safe_file(pkg, name):
    if not re.fullmatch(r"[A-Za-z0-9._-]+", name or ""):
        raise ValueError("bad file name")
    p = os.path.join(pkg_dir(pkg), name)
    if not os.path.isfile(p):
        raise ValueError("no such file: " + name)
    return p


def load(pkg):
    with open(os.path.join(pkg_dir(pkg), "claims.json"), encoding="utf-8") as f:
        return json.load(f)


def save(pkg, data):
    p = os.path.join(pkg_dir(pkg), "claims.json")
    tmp = p + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    os.replace(tmp, p)
    sync_checklist(pkg, data)


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def write(p, s):
    with open(p, "w", encoding="utf-8") as f:
        f.write(s)


def esc_for(fname, text):
    """Text as it is stored in a source file: HTML files keep & < > escaped, Markdown keeps it raw."""
    if fname.endswith(".html"):
        return html.escape(text, quote=False)
    return text


def unesc_for(fname, text):
    return html.unescape(text) if fname.endswith(".html") else text


def location_found(pkg, loc):
    try:
        return esc_for(loc["file"], loc["text"]) in read(safe_file(pkg, loc["file"]))
    except ValueError:
        return False


def summary(data):
    counts = {"pending": 0, "approved": 0, "edited": 0, "rejected": 0}
    for c in data["claims"]:
        counts[c.get("status", "pending")] = counts.get(c.get("status", "pending"), 0) + 1
    return counts


def files_of(pkg):
    names = sorted(os.listdir(pkg_dir(pkg)))
    resume = [n for n in names if n.startswith("resume-") and n.endswith(".html")]
    letter = [n for n in names if n.startswith("cover-letter-") and n.endswith(".md")]
    return resume[:1] + letter[:1]


# ---------- checklist sync ----------

STATUS_WORD = {"pending": "PENDING", "approved": "Approved", "edited": "Edited", "rejected": "Rejected"}


def sync_checklist(pkg, data):
    p = os.path.join(pkg_dir(pkg), "application-checklist.md")
    if not os.path.isfile(p):
        return
    s = read(p)
    start, end = "<!-- claims:start -->", "<!-- claims:end -->"
    if start not in s or end not in s:
        return
    lines = [start, "", "*Maintained by the claims review tool (`scripts/claims-review/`); edit claims there, not here.*", ""]
    for i, c in enumerate(data["claims"], 1):
        st = STATUS_WORD.get(c.get("status", "pending"), c.get("status"))
        when = ""
        if c.get("history"):
            when = " (" + c["history"][-1]["at"][:10] + ")"
        texts = "; ".join('"' + l["text"] + '" (' + l["file"] + ")" for l in c.get("locations", [])) or "not used in the materials"
        lines.append("%d. **%s%s:** %s. %s" % (i, st, when, c.get("label", ""), texts))
        if c.get("why"):
            lines.append("   Source: " + c["why"])
    lines += ["", end]
    a, b = s.index(start), s.index(end) + len(end)
    write(p, s[:a] + "\n".join(lines) + s[b:])


# ---------- previews ----------

def md_letter_html(md, marks=None):
    """Same structure build-letter.sh produces: hard line breaks, '# ' heading, '---' rule, links."""
    marks = marks or []
    first = re.search(r"^# (.+)$", md, re.M)
    title = html.escape(first.group(1).strip() if first else "Cover Letter")
    # insert sentinels around claim text before escaping, then turn them into <mark> tags
    for m in marks:
        if m["text"] and m["text"] in md:
            md = md.replace(m["text"], "\u0001%s\u0003%s\u0002" % (m["attrs"], m["text"]), 1)

    def inline(s):
        s = html.escape(s, quote=False)
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
        s = re.sub(r"\u0001([^\u0003]*)\u0003", lambda m: "<mark " + m.group(1) + ">", s)
        return s.replace("\u0002", "</mark>")

    blocks, cur = [], []
    for ln in md.split("\n"):
        if ln.strip() == "":
            if cur:
                blocks.append(cur)
                cur = []
        else:
            cur.append(ln)
    if cur:
        blocks.append(cur)
    body = []
    for b in blocks:
        if len(b) == 1 and b[0].startswith("# "):
            body.append("<h1>" + inline(b[0][2:]) + "</h1>")
        elif len(b) == 1 and b[0].strip() == "---":
            body.append("<hr>")
        else:
            body.append("<p>" + "<br>\n".join(inline(x) for x in b) + "</p>")
    return ('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>' + title + '</title>'
            "<style>" + LETTER_CSS + "</style></head><body>\n" + "\n".join(body) + "\n</body></html>")


FIT_SCRIPT = """<script>
(function(){function fit(){var w=8.5*96+24,v=window.innerWidth;if(v>0)document.documentElement.style.zoom=Math.min(1,v/w);}
fit();window.addEventListener('load',fit);window.addEventListener('resize',fit);})();
</script>"""

PREVIEW_SCRIPT = """<script>
(function(){
  function act(id){document.querySelectorAll('mark.claim').forEach(function(m){m.classList.toggle('active',m.dataset.claim===id)});
    var t=document.querySelector('mark.claim[data-claim="'+id+'"]'); if(t) t.scrollIntoView({block:'center'});}
  document.addEventListener('click',function(e){var m=e.target.closest('mark.claim'); if(m) parent.postMessage({claim:m.dataset.claim},'*');});
  window.addEventListener('message',function(e){if(e.data&&e.data.activate) act(e.data.activate);});
  var q=new URLSearchParams(location.search).get('hl'); if(q) act(q);
})();
</script>"""


def preview(pkg, fname):
    data = load(pkg)
    p = safe_file(pkg, fname)
    marks = []
    for c in data["claims"]:
        for loc in c.get("locations", []):
            if loc["file"] == fname:
                attrs = 'class="claim %s" data-claim="%s" title="%s"' % (
                    html.escape(c.get("status", "pending")), html.escape(c["id"]), html.escape(c.get("label", "")))
                marks.append({"text": loc["text"], "attrs": attrs})
    src = read(p)
    if fname.endswith(".md"):
        out = md_letter_html(src, marks)
    else:
        out = src
        for m in marks:
            t = esc_for(fname, m["text"])
            if t and t in out:
                out = out.replace(t, "<mark " + m["attrs"] + ">" + t + "</mark>", 1)
    # Lay the preview out at the printed page's width, then zoom it to fit the pane, so every line wraps
    # exactly where it will in the PDF. Resume: 8.5in page with 0.6in side margins (its own body padding).
    # Letter: 8.5in page with 0.85in side margins, matching LETTER_CSS's @page rule.
    # The resume template's print rule that zeroes body padding is overridden by the later body rule, so printed
    # resumes keep the body padding inside the @page margins. Mirror that: body width = 8.5in minus the @page side
    # margins, body padding unchanged. The letter has no body padding, so give it the @page margins as padding.
    if fname.endswith(".md"):
        page_css = "width:8.5in;padding:0.7in 0.85in"
    else:
        m = re.search(r"@page\s*\{[^}]*margin:\s*([\d.]+)in(?:\s+([\d.]+)in)?", src)
        side = float(m.group(2) or m.group(1)) if m else 0.0
        page_css = "width:%.3fin" % (8.5 - 2 * side)
    page = ("@media screen{html{background:#d1d5db}body{%s;max-width:none;box-sizing:border-box;"
            "margin:12px auto;background:#fff;box-shadow:0 1px 6px rgba(0,0,0,.2)}}") % page_css
    inject = "<style>" + MARK_CSS + page + "</style>" + FIT_SCRIPT
    out = out.replace("</head>", inject + "</head>", 1)
    out = out.replace("</body>", PREVIEW_SCRIPT + "</body>", 1)
    return out


# ---------- actions ----------

def now():
    return datetime.datetime.now().isoformat(timespec="seconds")


def find_claim(data, cid):
    for c in data["claims"]:
        if c["id"] == cid:
            return c
    raise ValueError("no such claim")


def act(pkg, cid, body):
    data = load(pkg)
    c = find_claim(data, cid)
    action = body.get("action")
    entry = {"at": now(), "action": action}
    if action in ("approve", "reject", "reset"):
        c["status"] = {"approve": "approved", "reject": "rejected", "reset": "pending"}[action]
        if body.get("note"):
            entry["note"] = body["note"]
    elif action == "edit":
        i = int(body.get("loc", 0))
        loc = c["locations"][i]
        new = body.get("text", "")
        fpath = safe_file(pkg, loc["file"])
        s = read(fpath)
        old_s = esc_for(loc["file"], loc["text"])
        if old_s not in s:
            raise ValueError("the claim text is no longer in %s; fix it by hand or update claims.json" % loc["file"])
        if s.count(old_s) > 1:
            raise ValueError("the claim text appears more than once in %s; make it longer in claims.json" % loc["file"])
        write(fpath, s.replace(old_s, esc_for(loc["file"], new), 1))
        entry.update({"file": loc["file"], "from": loc["text"], "to": new})
        loc["text"] = new
        c["status"] = "edited"
    else:
        raise ValueError("unknown action")
    c.setdefault("history", []).append(entry)
    save(pkg, data)
    return data


def approve_all(pkg):
    data = load(pkg)
    for c in data["claims"]:
        if c.get("status", "pending") == "pending":
            c["status"] = "approved"
            c.setdefault("history", []).append({"at": now(), "action": "approve", "note": "approve all remaining"})
    save(pkg, data)
    return data


def count_pages(path):
    with open(path, "rb") as f:
        return len(re.findall(rb"/Type\s*/Page(?!s)", f.read()))


def find_chrome():
    """A Chrome or Chromium binary from $CHROME or PATH (used off macOS, or on macOS when CHROME is set)."""
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    for name in ("chromium", "chromium-browser", "google-chrome", "google-chrome-stable", "chrome"):
        path = shutil.which(name)
        if path:
            return path
    return None


def chrome_print(src_html, out_pdf):
    """Print an HTML file to PDF with headless Chrome. Inputs and outputs sit in a temp dir, because macOS
    privacy settings can keep Chrome out of ~/Documents."""
    os.makedirs(CHROME_PROFILE, exist_ok=True)
    flags = ["--headless", "--disable-gpu", "--no-first-run", "--no-default-browser-check",
             "--user-data-dir=" + CHROME_PROFILE, "--no-pdf-header-footer", "--print-to-pdf=" + out_pdf,
             "file://" + src_html]
    if sys.platform == "darwin" and not os.environ.get("CHROME"):
        cmd = ["open", "-W", "-n", "-a", CHROME_APP, "--args"] + flags
    else:
        binary = find_chrome()
        if not binary:
            raise RuntimeError("no Chrome or Chromium found; install one or set CHROME=/path/to/chrome")
        cmd = [binary, "--no-sandbox"] + flags
    subprocess.run(cmd, timeout=120, check=False)
    if not os.path.isfile(out_pdf):
        raise RuntimeError("Chrome did not write %s (is Google Chrome installed?)" % os.path.basename(out_pdf))


def render(pkg):
    data = load(pkg)
    # a rejected claim blocks only if its text is still in the documents; a rejected note (no locations) just stays out
    open_claims = [c["label"] for c in data["claims"]
                   if c.get("status", "pending") == "pending" or (c.get("status") == "rejected" and c.get("locations"))]
    if open_claims:
        raise ValueError("resolve these claims first: " + "; ".join(open_claims))
    missing = [l["text"][:60] for c in data["claims"] for l in c.get("locations", []) if not location_found(pkg, l)]
    if missing:
        raise ValueError("claim text not found in the files (edited by hand?): " + "; ".join(missing))
    role = data.get("role") or pkg
    prefix = (data.get("pdf_prefix") + "-") if data.get("pdf_prefix") else ""
    d = pkg_dir(pkg)
    tmp = tempfile.mkdtemp(prefix="claims-render-")
    results = []
    try:
        for fname in files_of(pkg):
            src = os.path.join(d, fname)
            if fname.endswith(".html"):
                staged = os.path.join(tmp, fname)
                shutil.copy(src, staged)
                out_name = "%sResume-%s.pdf" % (prefix, role)
                want = 2
            else:
                staged = os.path.join(tmp, "letter.html")
                write(staged, md_letter_html(read(src)))
                out_name = "%sCover-Letter-%s.pdf" % (prefix, role)
                want = 1
            out_tmp = os.path.join(tmp, out_name)
            chrome_print(staged, out_tmp)
            pages = count_pages(out_tmp)
            shutil.copy(out_tmp, os.path.join(d, out_name))
            results.append({"file": out_name, "pages": pages, "expected": want, "ok": pages == want})
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    data.setdefault("renders", []).append({"at": now(), "results": results})
    save(pkg, data)
    return results


# ---------- HTTP ----------

class H(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        sys.stderr.write("%s %s\n" % (self.command, self.path))

    def send(self, code, body, ctype="application/json"):
        b = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(code)
        self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def j(self, obj, code=200):
        self.send(code, json.dumps(obj, ensure_ascii=False))

    def do_GET(self):
        u = urlparse(self.path)
        parts = [unquote(x) for x in u.path.strip("/").split("/") if x]
        try:
            if not parts:
                return self.send(200, read(os.path.join(HERE, "index.html")), "text/html")
            if parts == ["api", "packages"]:
                out = []
                for n in sorted(os.listdir(APPS)):
                    if os.path.isfile(os.path.join(APPS, n, "claims.json")):
                        data = load(n)
                        out.append({"pkg": n, "role": data.get("role"), "counts": summary(data)})
                return self.j(out)
            if len(parts) == 3 and parts[:2] == ["api", "pkg"]:
                pkg = parts[2]
                data = load(pkg)
                for c in data["claims"]:
                    for l in c.get("locations", []):
                        l["found"] = location_found(pkg, l)
                data["files"] = files_of(pkg)
                data["counts"] = summary(data)
                return self.j(data)
            if len(parts) == 3 and parts[0] == "preview":
                return self.send(200, preview(parts[1], parts[2]), "text/html")
            return self.j({"error": "not found"}, 404)
        except (ValueError, OSError, KeyError) as e:
            return self.j({"error": str(e)}, 400)

    def do_POST(self):
        if self.headers.get("Origin") not in (None, "http://127.0.0.1:%d" % PORT, "http://localhost:%d" % PORT):
            return self.j({"error": "cross-origin request refused"}, 403)
        n = int(self.headers.get("Content-Length") or 0)
        try:
            body = json.loads(self.rfile.read(n) or b"{}")
        except ValueError:
            return self.j({"error": "bad JSON"}, 400)
        parts = [unquote(x) for x in urlparse(self.path).path.strip("/").split("/") if x]
        try:
            if len(parts) == 5 and parts[:2] == ["api", "pkg"] and parts[3] == "claim":
                act(parts[2], parts[4], body)
                return self.j({"ok": True})
            if len(parts) == 4 and parts[:2] == ["api", "pkg"] and parts[3] == "approve-all":
                approve_all(parts[2])
                return self.j({"ok": True})
            if len(parts) == 4 and parts[:2] == ["api", "pkg"] and parts[3] == "render":
                return self.j({"ok": True, "results": render(parts[2])})
            return self.j({"error": "not found"}, 404)
        except (ValueError, RuntimeError, OSError, KeyError, IndexError, subprocess.TimeoutExpired) as e:
            return self.j({"error": str(e)}, 400)


PORT = 8765

if __name__ == "__main__":
    # Arguments are read only when run as the server, so scripts/render.py can import this module.
    if len(sys.argv) > 1:
        PORT = int(sys.argv[1])
    if len(sys.argv) > 2:
        APPS = os.path.abspath(os.path.join(ROOT, sys.argv[2]))
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), H)
    print("claims review on http://127.0.0.1:%d" % PORT, flush=True)
    srv.serve_forever()

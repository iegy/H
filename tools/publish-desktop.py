#!/usr/bin/env python3
"""Puts a new Hisn for Windows installer on the site: download/Hisn-Setup.msi, version-desktop.json and the
Windows download button on the pages (hidden until the first installer is published).

The installer is bigger than GitHub's 100 MB file limit, so it is NOT stored in the repository: the workflow uploads it as a
GitHub Release asset (tag desktop-v<versionName>) and this script only records its URL, size and SHA-256.

Usage: publish-desktop.py <msi> <versionCode> <versionName> [notesAr] [notesEn]
Run from the root of this repository. Used by the HisnDesktop build workflow; can also be run by hand.
"""
import hashlib, json, math, os, re, sys

msi, code, name = sys.argv[1], int(sys.argv[2]), sys.argv[3]
notes_ar = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4].strip() else None
notes_en = sys.argv[5] if len(sys.argv) > 5 and sys.argv[5].strip() else None

data = open(msi, "rb").read()
url = f"https://github.com/iegy/H/releases/download/desktop-v{name}/Hisn-Setup-{name}.msi"
sha = hashlib.sha256(data).hexdigest()
size = len(data)
mb = max(1, math.ceil(size / 1_048_576))

v = json.load(open("version-desktop.json", encoding="utf-8")) if os.path.exists("version-desktop.json") else {}
if v.get("versionCode", 0) >= code:
    sys.exit(f"versionCode {code} is not newer than the published {v.get('versionCode')}")
v.update(
    versionCode=code, versionName=name,
    installerUrl=url,
    size=size, sha256=sha,
)
if notes_ar: v["notesAr"] = notes_ar
if notes_en: v["notesEn"] = notes_en
with open("version-desktop.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(v, ensure_ascii=False, indent=2) + "\n")

for page in ("index.html", "en/index.html"):
    s = open(page, encoding="utf-8").read()
    # Reveal the Windows button and fill in its size / version / checksum.
    s = re.sub(r'(<div class="cta-win" data-hisn="win") style="display:none"', r"\1", s)
    s = re.sub(r'href="[^"]*Hisn-Setup[^"]*\.msi"', f'href="{url}"', s)
    s = re.sub(r'(data-hisn="win-size">)[^<]*(<)', rf"\g<1>{mb}\g<2>", s)
    s = re.sub(r'(data-hisn="win-version">)[^<]*(<)', rf"\g<1>{name}\g<2>", s)
    s = re.sub(r'(data-hisn="win-sha">)[^<]*(<)', rf"\g<1>{sha}\g<2>", s)
    open(page, "w", encoding="utf-8").write(s)

print(f"Published Windows {name} ({code}), {size} bytes, sha256 {sha}")

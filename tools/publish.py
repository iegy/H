#!/usr/bin/env python3
"""Puts a new Hisn APK on the site: download/Hisn.apk, version.json and the version/size/SHA-256 shown on the pages.

Usage: publish.py <apk> <versionCode> <versionName> [notesAr] [notesEn]
Run from the root of this repository. Used by the Hisn build workflow; can also be run by hand.
"""
import hashlib, json, math, os, re, shutil, sys

apk, code, name = sys.argv[1], int(sys.argv[2]), sys.argv[3]
notes_ar = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4].strip() else None
notes_en = sys.argv[5] if len(sys.argv) > 5 and sys.argv[5].strip() else None

shutil.copyfile(apk, "download/Hisn.apk")
data = open("download/Hisn.apk", "rb").read()
sha = hashlib.sha256(data).hexdigest()
size = len(data)
mb = max(1, math.ceil(size / 1_048_576))

v = json.load(open("version.json", encoding="utf-8")) if os.path.exists("version.json") else {}
if v.get("versionCode", 0) >= code:
    sys.exit(f"versionCode {code} is not newer than the published {v.get('versionCode')}")
v.update(
    versionCode=code, versionName=name,
    apkUrl="https://raw.githubusercontent.com/iegy/H/main/download/Hisn.apk",
    size=size, sha256=sha,
)
if notes_ar: v["notesAr"] = notes_ar
if notes_en: v["notesEn"] = notes_en
with open("version.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(v, ensure_ascii=False, indent=2) + "\n")

short = ".".join(name.split(".")[:3])
for page in ("index.html", "en/index.html"):
    s = open(page, encoding="utf-8").read()
    s = re.sub(r'(data-hisn="version">)[^<]*(<)', rf"\g<1>{short} ({code})\g<2>", s)
    s = re.sub(r'(data-hisn="sha">)[^<]*(<)', rf"\g<1>{sha}\g<2>", s)
    s = re.sub(r'(data-hisn="size">)[^<]*(<)', rf"\g<1>{mb}\g<2>", s)
    open(page, "w", encoding="utf-8").write(s)

print(f"Published {name} ({code}), {size} bytes, sha256 {sha}")

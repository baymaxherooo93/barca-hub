#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
prepare-deploy.py — menyiapkan folder `deploy/` + zip untuk GitHub Pages (tanpa token).

Isi deploy/:
  index.html   ← salinan barca-hub.html (portal single-file)
  .nojekyll    ← mematikan pemrosesan Jekyll agar file lolos apa adanya
  README.md    ← cara deploy & cara update konten

Pakai:
  python3 update-snapshot.py     # (opsional) segarkan data seed dulu
  python3 prepare-deploy.py      # lalu upload isi deploy/ ke repo GitHub via web UI
"""
import os, shutil, zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "barca-hub.html")
DEP = os.path.join(ROOT, "deploy")
ZIP = os.path.join(ROOT, "barca-hub-gh-pages.zip")

README = """# Barça Hub di GitHub Pages

Portal ini **satu file** (`index.html`). Tidak butuh build, server, atau token apa pun.

## Deploy pertama kali (tanpa token, lewat web GitHub)
1. Buka https://github.com/new → buat repository **public**, mis. `barca-hub` → *Create repository*.
2. Di halaman repo kosong, klik **uploading an existing file** → seret `index.html` (+ `.nojekyll`) dari folder `deploy/` → *Commit changes*.
3. Buka **Settings → Pages** (sidebar kiri).
   - *Source*: **Deploy from a branch**
   - *Branch*: `main` → folder `/ (root)` → *Save*.
4. Tunggu ±30–60 detik. Situs live di: `https://<USERNAME>.github.io/<NAMA-REPO>/`
   (link pastinya muncul di banner Settings → Pages).

> Karena disajikan lewat HTTPS, seluruh sumber data live (ESPN, TheSportsDB) diakses
> langsung tanpa proxy; situs resmi fcbarcelona.com tetap lewat CORS proxy publik.

## Update konten później / berkala
1. Di mesin lokal: `python3 update-snapshot.py` (menyegarkan seed resmi di dalam file),
   lalu `python3 prepare-deploy.py` (menyalin ke `deploy/` + zip).
2. Di repo GitHub: buka `index.html` → ikon tempat sampah / atau *Add file → Upload files*
   → seret `index.html` baru → *Commit changes*. Pages akan rebuild otomatis.

Alternatif tanpa mesin lokal: tombol **Setelan → Ekspor .html** di dalam portal
mengunduh salinan portal berisi data terakhir — file itu bisa langsung di-upload menggantikan `index.html`.
"""

def main():
    os.makedirs(DEP, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(DEP, "index.html"))
    with open(os.path.join(DEP, ".nojekyll"), "w") as f:
        f.write("")
    with open(os.path.join(DEP, "README.md"), "w", encoding="utf-8") as f:
        f.write(README)
    if os.path.exists(ZIP):
        os.remove(ZIP)
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for name in ("index.html", ".nojekyll", "README.md"):
            z.write(os.path.join(DEP, name), name)
    kb = os.path.getsize(os.path.join(DEP, "index.html")) / 1024
    print(f"✔ deploy/index.html  : {kb:.0f} KB")
    print(f"✔ deploy/.nojekyll   : ada")
    print(f"✔ deploy/README.md   : ada")
    print(f"✔ {os.path.basename(ZIP)} : {os.path.getsize(ZIP)/1024:.0f} KB")
    print("\nLangkah tanpa token: github.com/new → upload index.html → Settings → Pages → branch main / (root).")

if __name__ == "__main__":
    main()

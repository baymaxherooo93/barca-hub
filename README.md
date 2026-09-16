# Barça Hub di GitHub Pages

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

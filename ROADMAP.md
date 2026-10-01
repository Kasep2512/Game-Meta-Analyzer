# 🗺️ Roadmap 40 Hari: Game Meta Analyzer & Tournament Tracker

**Fokus Teknologi:** FastAPI, Streamlit, Pandas, SQLAlchemy, Pydantic, SQLite/MySQL, GitHub Actions, Docker, Plotly, Lottie Animations.

## 🏁 Fase 1: Perencanaan & Fondasi (Hari 1 - 5)
Fokus pada arsitektur sistem, desain database, dan inisiasi repositori.
*   **Hari 1:** Inisiasi repositori Git, pembuatan `README.md`, `.gitignore`, dan pembentukan struktur direktori (backend, frontend, data). *(Selesai)*
*   **Hari 2:** Merancang ERD/EERD untuk entitas utama: `Heroes`, `Patch_Notes`, `Matches/Tournaments`, dan `Hero_Stats` (Pick rate, Win rate, Ban rate).
*   **Hari 3:** *Setup environment* virtual Python, instalasi dependensi (FastAPI, Uvicorn, Streamlit, Pandas, SQLAlchemy).
*   **Hari 4:** Membuat *mockup* antarmuka UI/UX untuk dashboard menggunakan Canva/Figma, menentukan tema warna.
*   **Hari 5:** Konfigurasi awal koneksi database (SQLite untuk development) dan pembuatan model dasar menggunakan SQLAlchemy.

## ⚙️ Fase 2: Manajemen Data & Backend Dasar (Hari 6 - 15)
Fokus pada pengumpulan data, manipulasi data, dan pembuatan API.
*   **Hari 6-7:** Mengumpulkan dataset awal (CSV/JSON berisi data patch terbaru, penyesuaian hero, dan sistem poin turnamen).
*   **Hari 8-9:** Menggunakan **Pandas** untuk melakukan *data cleaning* dan *preprocessing* dari dataset mentah.
*   **Hari 10-11:** Membuat script *seeder* untuk memasukkan data yang sudah bersih ke dalam database.
*   **Hari 12-13:** Membangun endpoint API (GET) menggunakan **FastAPI** untuk menarik data hero, status meta, dan riwayat patch.
*   **Hari 14:** Membangun endpoint (POST/PUT) untuk memperbarui data turnamen (jadwal, hasil match, klasemen).
*   **Hari 15:** Implementasi **Pydantic** untuk validasi skema request dan response API.

## 🧠 Fase 3: Logika Analitik & Pengujian (Hari 16 - 22)
Fokus pada kalkulasi tren meta dan memastikan keandalan backend.
*   **Hari 16-17:** Membuat fungsi analitik khusus dengan Pandas di backend untuk menghitung tren *win rate* dan *pick rate* berdasarkan pembaruan patch tertentu.
*   **Hari 18-19:** Membangun endpoint agregasi data (misal: `/api/v1/meta-tier-list` untuk *tier list* otomatis berdasarkan performa).
*   **Hari 20-21:** Menulis *unit test* untuk API dan fungsi kalkulasi data menggunakan **pytest**.
*   **Hari 22:** Melakukan *debugging* dan optimasi query database agar API merespons lebih cepat.

## 🎨 Fase 4: Pengembangan Frontend Interaktif & Animasi (Hari 23 - 32)
Fokus pada visualisasi data, Custom CSS, dan UX yang dinamis menggunakan Streamlit.
*   **Hari 23:** Mengonfigurasi tema dasar di `.streamlit/config.toml` (warna primary, background, dan font agar sesuai dengan tema game).
*   **Hari 24:** Menginjeksi **Custom CSS** (`st.markdown`) untuk efek *drop shadow*, *border-radius*, dan animasi transisi *hover* pada kartu/metrik agar tidak kaku.
*   **Hari 25:** Mengimplementasikan **Lottie Animations** (`streamlit-lottie`). Memasang animasi JSON untuk *loading screen* dan *empty states* (misal: saat data hero tidak ditemukan).
*   **Hari 26:** Mengintegrasikan frontend dengan API backend (`requests`), memastikan animasi *loading* berjalan mulus saat fetching data.
*   **Hari 27-28:** Membuat visualisasi interaktif menggunakan **Plotly Express**. Menambahkan *line chart* untuk *Win Rate* dengan efek animasi transisi data (`animation_frame`) dan *hover tooltip*.
*   **Hari 29-30:** Merancang *Card UI* untuk daftar hero dan klasemen turnamen menggunakan kolom Streamlit, ditambahkan CSS *scale transform* saat di-hover.
*   **Hari 31-32:** Menambahkan filter interaktif (dropdown/slider) dengan manajemen *state* (`st.session_state`) agar halaman tidak melakukan *full-refresh* yang mengganggu saat mengganti parameter.

## 🚀 Fase 5: CI/CD, Kontainerisasi & Finalisasi (Hari 33 - 40)
Fokus pada otomatisasi deployment dan dokumentasi portofolio.
*   **Hari 33-34:** Menulis `Dockerfile` untuk backend FastAPI dan frontend Streamlit, serta mengonfigurasi `docker-compose.yml`.
*   **Hari 35-36:** Merancang workflow **GitHub Actions** untuk menjalankan *automated testing* setiap ada push ke branch utama.
*   **Hari 37-38:** Melakukan *code refactoring*, merapikan struktur direktori, dan memastikan kode memiliki komentar (docstrings) yang jelas.
*   **Hari 39:** Menyempurnakan `README.md` (menambahkan penjelasan arsitektur, panduan instalasi lokal, diagram ERD, dan screenshot UI dashboard).
*   **Hari 40:** *Final review*, memastikan semua commit sudah rapi di GitHub, dan merilis versi v1.0.0.
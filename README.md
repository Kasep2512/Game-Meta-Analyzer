# 🎮 Game Meta Analyzer (Honor of Kings)

![CI/CD Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-009688?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)

**Game Meta Analyzer** adalah sebuah aplikasi web *Full-Stack* yang dirancang untuk menganalisis statistik performa *hero* (seperti *Win Rate*, *Pick Rate*, dan *Ban Rate*) pada game **Honor of Kings**. Proyek ini bertujuan untuk memberikan wawasan berbasis data kepada pemain dan analis *esports* mengenai tren *meta* di berbagai *patch* pembaruan.

Aplikasi ini mengimplementasikan arsitektur *microservices* sederhana dengan memisahkan *Backend* (API) dan *Frontend* (Visualisasi), serta dikemas menggunakan kontainerisasi modern.

---

## ✨ Fitur Utama

- **📈 Dasbor Analitik Meta:** Pantau statistik *hero* teratas secara seketika dengan filter dinamis berdasarkan peran (*Role*).
- **📊 Visualisasi Data Interaktif:** Eksplorasi korelasi antara *Win Rate* dan *Pick Rate* melalui grafik *scatter plot* interaktif.
- **🗡️ Direktori Hero:** Katalog lengkap yang menampilkan profil dasar seluruh *hero* menggunakan desain *Card UI*.
- **🏆 Pelacak Turnamen:** Pantau klasemen liga simulasi dan tren *drafting* (prioritas *Pick* dan *Ban*) di level kompetitif.
- **⚡ RESTful API Cepat:** Didukung oleh FastAPI dan basis data SQLite yang ringan untuk respons data di bawah hitungan milidetik.
- **🐳 Siap Deploy (Dockerized):** Konfigurasi *multi-container* yang memudahkan proses instalasi di lingkungan mana pun.
- **🔄 CI/CD Terintegrasi:** Memastikan kualitas kode melalui *automated build testing* dengan GitHub Actions.

---

## 🛠️ Teknologi yang Digunakan

**Backend & Database:**
- **Python 3.11**
- **FastAPI:** *Framework* web modern berkinerja tinggi untuk membangun API.
- **Pydantic:** Validasi data dan manajemen skema.
- **SQLAlchemy & SQLite:** ORM dan sistem manajemen basis data relasional.

**Frontend & Data Visualization:**
- **Streamlit:** *Framework* antarmuka web interaktif berbasis Python (*Dark Mode UI*).
- **Pandas:** Manipulasi dan analisis data struktur.
- **Plotly Express:** Pustaka grafik visual interaktif.

**DevOps & Deployment:**
- **Docker & Docker Compose:** Kontainerisasi dan orkestrasi layanan.
- **GitHub Actions:** Otomatisasi *pipeline Continuous Integration* (CI).

---

## ⚙️ Prasyarat (Prerequisites)

Sebelum menjalankan aplikasi ini, pastikan sistem Anda telah memasang:
- [Python 3.11+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) *(Opsional, sangat disarankan)*

---

## 🚀 Panduan Instalasi & Menjalankan Aplikasi

Anda dapat menjalankan aplikasi ini menggunakan **Docker** (Direkomendasikan) atau menjalankannya secara manual di mesin **Lokal**.

### Opsi 1: Menjalankan dengan Docker (Rekomendasi)

Ini adalah cara termudah. Anda tidak perlu mengonfigurasi *virtual environment* atau menginstal pustaka Python secara manual.

1. **Clone repositori ini:**
   ```bash
   git clone https://github.com/username-anda/Game-Meta-Analyzer.git
   cd Game-Meta-Analyzer
   ```

2. **Jalankan Docker Compose:**
   Pastikan Docker Desktop sudah menyala, lalu jalankan:
   ```bash
   docker compose up --build
   ```

3. **Akses Aplikasi:**
   - Frontend (Streamlit Dashboard): [http://localhost:8501](http://localhost:8501)
   - Backend API Docs (Swagger UI): [http://localhost:8000/docs](http://localhost:8000/docs)

### Opsi 2: Menjalankan secara Lokal (Development)

Jika Anda ingin memodifikasi kode atau tidak memiliki Docker, gunakan langkah berikut:

1. **Clone repositori dan siapkan Virtual Environment:**
   ```bash
   git clone https://github.com/username-anda/Game-Meta-Analyzer.git
   cd Game-Meta-Analyzer
   python -m venv venv
   ```

2. **Aktivasi Virtual Environment:**
   - **Windows:** `venv\Scripts\activate`
   - **macOS/Linux:** `source venv/bin/activate`

3. **Jalankan Backend (Terminal 1):**
   ```bash
   cd backend
   pip install -r requirements.txt
   cd app
   uvicorn main:app --reload
   ```

4. **Jalankan Frontend (Terminal 2):**
   Buka terminal baru, pastikan `venv` aktif, lalu jalankan:
   ```bash
   cd frontend
   pip install -r requirements.txt
   streamlit run app.py
   ```

---

## 📁 Struktur Direktori Proyek

```text
Game-Meta-Analyzer/
├── .github/workflows/       # Konfigurasi CI/CD Pipeline (GitHub Actions)
├── backend/                 # Logika API & Manajemen Database
│   ├── app/                 # Source code FastAPI (main.py, models.py, dsb.)
│   ├── game_meta.db         # Basis data SQLite
│   ├── Dockerfile           # Konfigurasi container Backend
│   └── requirements.txt     # Dependensi Backend
├── frontend/                # Antarmuka Visual
│   ├── .streamlit/          # Konfigurasi tema Dark Mode
│   ├── app.py               # Source code Streamlit
│   ├── Dockerfile           # Konfigurasi container Frontend
│   └── requirements.txt     # Dependensi Frontend
├── docker-compose.yml       # Orkestrasi multi-container
└── README.md                # Dokumentasi Proyek
```

---

## 📄 Lisensi

Silakan gunakan dan modifikasi untuk keperluan portofolio atau pembelajaran Anda.
import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# konfigurasi halaman
st.set_page_config(
    page_title="Game Meta Analyzer",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# url API FastAPI
API_URL = "http://127.0.0.1:8000/api"


def main():
    # --- SIDEBAR NAVIGATION ---
    st.sidebar.title("🎮 Meta Analyzer")
    st.sidebar.caption("Honor of Kings")

    # menu navigasi
    st.sidebar.markdown("### Menu")
    menu = st.sidebar.radio(
        "Pilih Halaman",
        ["Dasbor (Meta)", "Daftar Hero", "Turnamen"],
        label_visibility="collapsed",
    )

    st.sidebar.markdown("---")

    # indikator status API
    try:
        req = requests.get("http://127.0.0.1:8000/")
        if req.status_code == 200:
            st.sidebar.success("🟢 API Aktif (v1.0.0)")
    except:
        st.sidebar.error("🔴 API Terputus")
        st.sidebar.caption("Pastikan server Uvicorn berjalan.")

    # --- KONTEN UTAMA ---
    if menu == "Dasbor (Meta)":
        render_dashboard()
    elif menu == "Daftar Hero":
        render_hero_list()
    elif menu == "Turnamen":
        render_tournament()


def render_tournament():
    st.title("🏆 Pelacak Turnamen")
    st.write("Klasemen, jadwal, dan hasil pertandingan Liga Musim 1.")

    st.markdown("---")
    st.subheader("📊 Klasemen Sementara")

    # data klasemen (mock data)
    data_klasemen = {
        "Tim": ["Tim Alpha", "Tim Bravo", "Tim Cobra", "Tim Delta", "Tim Echo"],
        "Main": [7, 7, 7, 7, 7],
        "Menang": [6, 5, 5, 4, 3],
        "Kalah": [1, 2, 2, 3, 4],
        "Poin": [18, 15, 15, 12, 9],
    }
    df_klasemen = pd.DataFrame(data_klasemen)

    df_klasemen.index = df_klasemen.index + 1

    st.dataframe(df_klasemen, use_container_width=True)

    st.markdown("---")

    st.subheader("🔥 Statistik Draft Turnamen")
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("📈 **Paling sering dipilih**")
            st.progress(0.82, text="Lu Bu (82%)")
            st.progress(0.75, text="Marco Polo (75%)")
            st.progress(0.68, text="Diaochan (68%)")

    with col2:
        with st.container(border=True):
            st.markdown("🚫 **Paling sering diban**")
            st.progress(0.71, text="Lu Bu (71%)")
            st.progress(0.57, text="Li Bai (57%)")
            st.progress(0.55, text="Diaochan (55%)")


def render_hero_list():
    st.title("🗡️ Daftar Hero")
    st.write(
        "Jelajahi daftar lengkap hero, saring berdasarkan peran, dan lihat statistik dasar mereka."
    )

    try:
        # Kita panggil endpoint API yang mengambil semua data hero (tanpa statistik win rate dsb)
        response = requests.get(f"{API_URL}/heroes")

        if response.status_code == 200:
            heroes = response.json()

            if not heroes:
                st.info("Belum ada data hero di database.")
                return

            # Filter Role di halaman Hero (Opsional, tapi bagus untuk UX)
            daftar_role = ["Semua"] + list(set([h["role"] for h in heroes]))
            pilihan_role = st.selectbox("Saring Peran", daftar_role)

            if pilihan_role != "Semua":
                heroes = [h for h in heroes if h["role"] == pilihan_role]

            st.markdown("---")

            # Membuat grid 3 kolom untuk Card UI
            cols = st.columns(3)

            # Looping untuk membuat kartu sebanyak jumlah hero yang ada
            for index, hero in enumerate(heroes):
                # Membagi urutan hero ke kolom 1, 2, dan 3 secara bergantian
                with cols[index % 3]:
                    # Fitur 'border=True' di Streamlit 1.30+ otomatis membuat kotak ala kartu
                    with st.container(border=True):
                        st.subheader(f"🛡️ {hero['name']}")
                        st.caption(f"Role: {hero['role']}")

                        # Tombol interaktif (saat ini hanya visual)
                        st.button(
                            "Lihat Detail",
                            key=f"btn_hero_{hero['id']}",
                            use_container_width=True,
                        )

    except Exception as e:
        st.error(f"Gagal terhubung ke API: {e}")


def render_dashboard():
    st.title("📈 Dasbor Meta Analyzer")
    st.write(
        "Pantau win rate, pick rate, dan ban rate setiap hero dari patch ke patch."
    )

    st.subheader("🔥 Hero Teratas - Patch 7")

    try:
        response = requests.get(f"{API_URL}/meta/2")
        if response.status_code == 200:
            data = response.json()

            if len(data) > 0:
                top_hero: dict = data[0]
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric(
                        label=f"Win Rate Tertinggi: {top_hero['hero_name']}",
                        value=f"{top_hero['win_rate']}%",
                        delta="Naik dari patch lalu",
                    )
                with col2:
                    st.metric(label="Pick Rate", value=f"{top_hero['pick_rate']}%")
                with col3:
                    st.metric(label="Ban Rate", value=f"{top_hero['ban_rate']}%")

            st.markdown("---")

            # Ubah JSON menjadi Pandas DataFrame
            df = pd.DataFrame(data)

            # --- FITUR BARU: Filter Interaktif di Sidebar ---
            st.sidebar.markdown("### 🎛️ Filter Data")
            # Mengambil daftar role unik dari database (Fighter, Mage, dll)
            daftar_role = ["Semua Peran"] + list(df["hero_role"].unique())
            pilihan_role = st.sidebar.selectbox("Saring berdasarkan Peran", daftar_role)

            # Terapkan filter pada DataFrame jika user tidak memilih "Semua Peran"
            if pilihan_role != "Semua Peran":
                df = df[df["hero_role"] == pilihan_role]
            # ------------------------------------------------

            chart_col, table_col = st.columns([1.2, 1])

            with chart_col:
                st.subheader("📊 Analisis Performa")
                # Jika data kosong setelah difilter, tampilkan peringatan
                if df.empty:
                    st.warning(
                        f"Tidak ada hero dengan role {pilihan_role} di patch ini."
                    )
                else:
                    fig = px.scatter(
                        df,
                        x="pick_rate",
                        y="win_rate",
                        color="hero_role",
                        hover_name="hero_name",
                        size="ban_rate",
                        title="Win Rate vs Pick Rate",
                        labels={
                            "pick_rate": "Pick Rate (%)",
                            "win_rate": "Win Rate (%)",
                        },
                    )
                    fig.update_layout(
                        plot_bgcolor="rgba(0,0,0,0)",
                        paper_bgcolor="rgba(0,0,0,0)",
                        font=dict(color="#FAFAFA"),
                    )
                    st.plotly_chart(fig, use_container_width=True)

            with table_col:
                st.subheader("📋 Tier List Meta")
                if not df.empty:
                    st.dataframe(
                        df[["hero_name", "hero_role", "win_rate"]],
                        use_container_width=True,
                        hide_index=True,
                    )

    except Exception as e:
        st.error(f"Gagal mengambil data dari API: {e}")


if __name__ == "__main__":
    main()

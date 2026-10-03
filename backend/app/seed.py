from database import engine, SessionLocal, Base
from models import Hero, PatchNote, HeroStat, Tournament, Match
import datetime

# tabel di database
Base.metadata.create_all(bind=engine)


def seed_data():
    db = SessionLocal()

    # Cek data sudah ada agar tidak duplikat
    if db.query(Hero).first():
        print("Data sudah ada, membatalkan seeding.")
        db.close()
        return

    # Data Hero
    heroes = [
        Hero(name="Lu Bu", role="Fighter"),
        Hero(name="Diaochan", role="Mage"),
        Hero(name="Marco Polo", role="Marksman"),
        Hero(name="Arthur", role="Fighter"),
        Hero(name="Yao", role="Support"),
    ]
    db.add_all(heroes)
    db.commit()

    # Data Patch
    patches = [
        PatchNote(
            version_number="Patch 6",
            release_date=datetime.date(2026, 9, 1),
            description="Marco Polo Buff, Arthur Nerf",
        ),
        PatchNote(
            version_number="Patch 7",
            release_date=datetime.date(2026, 10, 1),
            description="Lu Bu Buff, Li Bai Nerf",
        ),
    ]
    db.add_all(patches)
    db.commit()

    # Data Statistik Hero (Contoh untuk Patch 7)
    patch_7 = db.query(PatchNote).filter(PatchNote.version_number == "Patch 7").first()
    lu_bu = db.query(Hero).filter(Hero.name == "Lu Bu").first()
    diaochan = db.query(Hero).filter(Hero.name == "Diaochan").first()

    stats = [
        HeroStat(
            hero_id=lu_bu.id,
            patch_id=patch_7.id,
            win_rate=53.9,
            pick_rate=14.8,
            ban_rate=33.1,
        ),
        HeroStat(
            hero_id=diaochan.id,
            patch_id=patch_7.id,
            win_rate=53.2,
            pick_rate=12.1,
            ban_rate=19.7,
        ),
    ]
    db.add_all(stats)

    # Data Turnamen
    tournament = Tournament(
        name="Liga Contoh Musim 1",
        start_date=datetime.date(2026, 10, 1),
        end_date=datetime.date(2026, 10, 31),
    )
    db.add(tournament)
    db.commit()

    print("Seeding data berhasil!")
    db.close()


if __name__ == "__main__":
    seed_data()

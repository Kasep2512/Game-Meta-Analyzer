from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine
import models, schemas

# aplikasi FastAPI
app = FastAPI(title="Game Meta Analyzer API", version="1.0.0")


# Dependency untuk close/open koneksi database setiap kali diakses
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Selamat datang di API Game Meta Analyzer. Akses /docs untuk dokumentasi."
    }


# endpoint 1: mengambil semua data hero
@app.get("/api/heroes", response_model=List[schemas.HeroResponse], tags=["Heroes"])
def get_heroes(db: Session = Depends(get_db)):
    heroes = db.query(models.Hero).all()
    return heroes


# endpoint 2: mengambil semua data patch
@app.get(
    "/api/patches", response_model=List[schemas.PatchNoteResponse], tags=["Patches"]
)
def get_patches(db: Session = Depends(get_db)):
    patches = db.query(models.PatchNote).all()
    return patches


# endpoint 3: mengambil tier list / statistik meta berdasrkan ID Patch
@app.get(
    "/api/meta/{patch_id}",
    response_model=List[schemas.HeroMetaResponse],
    tags=["Analytics"],
)
def get_meta_by_patch(patch_id: int, db: Session = Depends(get_db)):
    # menggabungkan tabel hero dan herostat, filter bberdasarkan patch_id
    results = (
        db.query(
            models.Hero.name.label("hero_name"),
            models.Hero.role.label("hero_role"),
            models.HeroStat.win_rate,
            models.HeroStat.pick_rate,
            models.HeroStat.ban_rate,
        )
        .join(models.HeroStat, models.Hero.id == models.HeroStat.hero_id)
        .filter(models.HeroStat.patch_id == patch_id)
        .all()
    )

    return results

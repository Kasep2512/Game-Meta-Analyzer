from sqlalchemy import Column, Integer, String, Float, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Hero(Base):
    __tablename__ = "heroes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    role = Column(String)

    # Relasi ke hero_stats
    stats = relationship("HeroStat", back_populates="hero")


class PatchNote(Base):
    __tablename__ = "patch_notes"

    id = Column(Integer, primary_key=True, index=True)
    version_number = Column(String, unique=True, index=True)
    release_date = Column(Date)
    description = Column(Text)

    # Relasi ke hero_stats
    stats = relationship("HeroStat", back_populates="patch")


class HeroStat(Base):
    __tablename__ = "hero_stats"

    id = Column(Integer, primary_key=True, index=True)
    hero_id = Column(Integer, ForeignKey("heroes.id"))
    patch_id = Column(Integer, ForeignKey("patch_notes.id"))
    win_rate = Column(Float)
    pick_rate = Column(Float)
    ban_rate = Column(Float)

    # relasi balik
    hero = relationship("Hero", back_populates="stats")
    patch = relationship("PatchNote", back_populates="stats")


class Tournament(Base):
    __tablename__ = "tournaments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    start_date = Column(Date)
    end_date = Column(Date)

    # Relasi ke matches
    matches = relationship("Match", back_populates="tournament")


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    tournament_id = Column(Integer, ForeignKey("tournaments.id"))
    team_blue = Column(String)
    team_red = Column(String)
    winner = Column(String)
    match_date = Column(Date)

    # Relasi balik
    tournament = relationship("Tournament", back_populates="matches")

from pydantic import BaseModel
from typing import List, Optional


# skema untuk data hero
class HeroBase(BaseModel):
    name: str
    role: str


class HeroResponse(HeroBase):
    id: int

    class Config:
        from_attributes = True


# skema data Patch
class PatchNoteResponse(BaseModel):
    id: int
    version_number: str
    description: str

    class Config:
        from_attributes = True


# skema untuk merespons gabungan data hero dan statistik (tier list)
class HeroMetaResponse(BaseModel):
    hero_name: str
    hero_role: str
    win_rate: float
    pick_rate: float
    ban_rate: float

    class Config:
        from_attributes = True

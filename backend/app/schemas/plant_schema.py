"""
Plant schemas.

Schemas define how data is received and returned by the API. What kind of data is allowed to enter or leave the system.
Defines what data looks like when entering or leaving the API.
Pydantic also checks and validates the data automatically.
validates input
structures output
controls request/response format
prevents bad data
documents API automatically
"""

from pydantic import BaseModel
from typing import Optional


# ===============================
# BASE SCHEMA
# ===============================

class PlantBase(BaseModel):
    name: str
    species: str
    location: str
    growth_stage: Optional[str] = None


# ===============================
# CREATE SCHEMA
# ===============================

class PlantCreate(PlantBase):
    """
    Used when creating a plant.
    """
    pass


# ===============================
# UPDATE SCHEMA
# ===============================

class PlantUpdate(BaseModel):
    """
    Used when updating plant.
    All fields optional for partial update.
    """
    name: Optional[str] = None
    species: Optional[str] = None
    location: Optional[str] = None
    growth_stage: Optional[str] = None


# ===============================
# RESPONSE SCHEMA
# ===============================

class PlantResponse(PlantBase):
    id: int

    class Config:
        orm_mode = True  # for SQLAlchemy compatibility
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


from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime
from app.schemas.location_schema import LocationResponse


# ===============================
# CREATE
# ===============================
class PlantCreate(BaseModel):
    name: str
    species: Optional[str] = None

    location_id: Optional[int] = None
    group_id: Optional[int] = None

    environment_type: Optional[str] = "outdoor"
    planting_date: Optional[date] = None

    source: Optional[str] = "manual"


# ===============================
# UPDATE
# ===============================
class PlantUpdate(BaseModel):
    name: Optional[str] = None
    species: Optional[str] = None

    location_id: Optional[int] = None
    group_id: Optional[int] = None

    environment_type: Optional[str] = None
    planting_date: Optional[date] = None

    is_synced: Optional[bool] = None


# ===============================
# RESPONSE
# ===============================
class PlantResponse(BaseModel):
    id: int
    name: str
    species: Optional[str]

    user_id: int
    location_id: Optional[int]
    group_id: Optional[int]

    environment_type: str
    planting_date: Optional[date]

    is_synced: bool
    source: str

    created_at: datetime

    # ✅ NEW: include location info
    location: Optional[LocationResponse] = None

    model_config = ConfigDict(from_attributes=True)

'''
    class Config:
        from_attributes = True  # for SQLAlchemy ORM
'''

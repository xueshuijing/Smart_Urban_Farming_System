from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import JSONB
from app.database.db import Base


class PlantSpeciesCache(Base):
    __tablename__ = "plant_species_cache"

    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(String(100), unique=True)
    species_name = Column(String(100))

    data = Column(JSONB)
    last_updated = Column(TIMESTAMP, server_default=func.now())

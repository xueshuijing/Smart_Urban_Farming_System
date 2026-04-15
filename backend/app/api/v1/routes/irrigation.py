from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.services.irrigation_service import (
    get_plants_needing_water,
    water_plant,
    water_all_due_plants
)

router = APIRouter(prefix="/irrigation", tags=["Irrigation"])


# ===============================
# GET PLANTS NEEDING WATER
# ===============================
@router.get("/check")
def check_irrigation(user_id: int, db: Session = Depends(get_db)):
    """
    Returns all plants that need watering
    """
    return get_plants_needing_water(db, user_id)


# ===============================
# WATER SINGLE PLANT
# ===============================
@router.post("/water/{plant_id}")
def water_single_plant(plant_id: int, user_id: int, db: Session = Depends(get_db)):
    """
    Manually water a plant
    """
    return water_plant(db, plant_id, user_id)


# ===============================
# WATER ALL DUE PLANTS
# ===============================
@router.post("/water-all")
def water_all(user_id: int, db: Session = Depends(get_db)):
    """
    Water all plants that need watering
    """
    return water_all_due_plants(db, user_id)

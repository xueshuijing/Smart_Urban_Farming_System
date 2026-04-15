from datetime import date, timedelta
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.plant import Plant


# ===============================
# CHECK IF PLANT NEEDS WATER
# ===============================
def needs_watering(plant: Plant) -> bool:
    """
    Pure function → easy to unit test
    """

    if not plant.last_watered:
        return True  # never watered → needs water

    next_watering_date = plant.last_watered + timedelta(days=plant.watering_interval_days)

    return date.today() >= next_watering_date


# ===============================
# GET ALL PLANTS THAT NEED WATER
# ===============================
def get_plants_needing_water(db: Session, user_id: int):
    plants = db.query(Plant).filter(Plant.user_id == user_id).all()

    return [plant for plant in plants if needs_watering(plant)]


# ===============================
# TRIGGER IRRIGATION
# ===============================
def water_plant(db: Session, plant_id: int, user_id: int):
    plant = db.query(Plant).filter(
        Plant.id == plant_id,
        Plant.user_id == user_id
    ).first()

    if not plant:
        raise HTTPException(status_code=404, detail="Plant not found")

    # update last watered date
    plant.last_watered = date.today()

    db.commit()
    db.refresh(plant)

    return plant


# ===============================
# BULK WATERING (OPTIONAL)
# ===============================
def water_all_due_plants(db: Session, user_id: int):
    plants = get_plants_needing_water(db, user_id)

    for plant in plants:
        plant.last_watered = date.today()

    db.commit()

    return plants

"""
Plant service layer contains business logic related to plants.
Routes --> call services--> talk to database.
"""

from sqlalchemy.orm import Session
from app.models.plant import Plant
from app.schemas.plant_schema import PlantCreate, PlantUpdate


# ===============================
# CREATE PLANT
# ===============================

def create_plant(db: Session, plant: PlantCreate, user_id: int):
    """
    Create a new plant linked to a specific user.
    """

    new_plant = Plant(
        name=plant.name,
        species=plant.species,
        location=plant.location,
        growth_stage=plant.growth_stage,
        owner_id=user_id  # ✅ link to user
    )

    db.add(new_plant)
    db.commit()
    db.refresh(new_plant)

    return new_plant


# ===============================
# GET ALL PLANTS (USER-SCOPED)
# ===============================

def get_all_plants(db: Session, user_id: int):
    """
    Get all plants belonging to the current user.
    """

    return db.query(Plant).filter(
        Plant.owner_id == user_id
    ).all()


# ===============================
# GET PLANT BY ID (USER-SCOPED)
# ===============================

def get_plant_by_id(db: Session, plant_id: int, user_id: int):
    """
    Get a single plant only if it belongs to the user.
    """

    return db.query(Plant).filter(
        Plant.id == plant_id,
        Plant.owner_id == user_id
    ).first()


# ===============================
# UPDATE PLANT (USER-SCOPED)
# ===============================

def update_plant(
    db: Session,
    plant_id: int,
    plant_update: PlantUpdate,
    user_id: int
):
    """
    Update a plant only if it belongs to the user.
    """

    plant = db.query(Plant).filter(
        Plant.id == plant_id,
        Plant.owner_id == user_id
    ).first()

    if not plant:
        return None

    if plant_update.name is not None:
        plant.name = plant_update.name

    if plant_update.species is not None:
        plant.species = plant_update.species

    if plant_update.location is not None:
        plant.location = plant_update.location

    if plant_update.growth_stage is not None:
        plant.growth_stage = plant_update.growth_stage  # ✅ added

    db.commit()
    db.refresh(plant)

    return plant


# ===============================
# DELETE PLANT (USER-SCOPED)
# ===============================

def delete_plant(db: Session, plant_id: int, user_id: int):
    """
    Delete a plant only if it belongs to the user.
    """

    plant = db.query(Plant).filter(
        Plant.id == plant_id,
        Plant.owner_id == user_id
    ).first()

    if not plant:
        return False

    db.delete(plant)
    db.commit()

    return True
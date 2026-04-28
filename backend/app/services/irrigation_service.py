"""
Service layer for FastAPI (Irrigation).

Key Point:
Handles business logic for irrigation processes.

Responsibilities:
- Determine irrigation needs
- Execute watering logic (manual or automated)
- Update plant or soil conditions
- Trigger related actions (e.g., notifications)

Architecture Role:
- Core logic layer for irrigation system
- Integrates plant data and environmental conditions

Layer Interaction:
- Communicates with: Models (plant, soil_condition), Database
- Called by: Routes, Workers (scheduler)

Data Flow:
Irrigation request or scheduled trigger received
        ↓
Plant and soil data retrieved
        ↓
Irrigation logic evaluated
        ↓
Database updated with results
        ↓
Optional notifications triggered
        ↓
Result returned to caller
"""

#app.services.irrigation_service.py


from datetime import date, timedelta
from sqlalchemy.orm import Session
from app.models.soil_condition import SoilCondition
from app.services import notification_service
from app.models.notification import Notification
from app.models.plant import Plant

# ===============================
# CONFIG (sample thresholds)
# ===============================
MOISTURE_THRESHOLD = 30  # below = dry

def _get_thirsty_plants(db: Session, user_id: int):
    plants = db.query(Plant).filter(Plant.user_id == user_id).all()
    return [plant for plant in plants if needs_watering(db, plant)]

# ===============================
# GET LATEST SOIL DATA
# ===============================
def get_latest_soil_condition(db: Session, plant_id: int):
    return db.query(SoilCondition).filter(
        SoilCondition.plant_id == plant_id
    ).order_by(SoilCondition.recorded_at.desc()).first()


# ===============================
# CHECK IF PLANT NEEDS WATER
# ===============================
def needs_watering(db: Session, plant: Plant) -> bool:
    # Determines if a plant needs watering based on sensor or schedule

    soil = get_latest_soil_condition(db, plant.id)
    # SENSOR MODE
    if plant.use_sensor and soil and soil.moisture is not None:
        return float(soil.moisture) < MOISTURE_THRESHOLD

    # SCHEDULE MODE (fallback)
    if not plant.watering_interval_days:
        return False

    if not plant.last_watered:
        return True

    next_watering_date = plant.last_watered + timedelta(days=plant.watering_interval_days)

    return date.today() >= next_watering_date


# ===============================
# GET PLANTS NEEDING WATER
# ===============================
def get_plants_needing_water(db: Session, user_id: int):
    thirsty_plants = _get_thirsty_plants(db, user_id)

    result = []

    for plant in thirsty_plants:
        existing_notification = db.query(Notification).filter(
            Notification.plant_id == plant.id,
            Notification.user_id == user_id,
            Notification.type == "irrigation"
        ).first()

        if not existing_notification:
            notification_service.create_notification(
                db=db,
                user_id=user_id,
                plant=plant,
                message=f"Plant '{plant.name}' needs watering"
            )

        result.append({
            "plant_id": plant.id,
            "name": plant.name,
            "last_watered": plant.last_watered,
            "watering_interval_days": plant.watering_interval_days,
            "use_sensor": plant.use_sensor,
            "needs_water": True
        })

    return result

# ===============================
# WATER PLANT
# ===============================
def water_plant(db: Session, plant_id: int, user_id: int):
    plant = db.query(Plant).filter(
        Plant.id == plant_id,
        Plant.user_id == user_id
    ).first()

    if not plant:
        return None

    # update watering date
    plant.last_watered = date.today()

    # Find the "unwatered" notification and delete it
    db.query(Notification).filter(
        Notification.plant_id == plant.id,
        Notification.user_id == user_id,
        Notification.type == "irrigation"
    ).delete(synchronize_session=False)

    db.commit()
    db.refresh(plant)
    return plant

# ===============================
# BULK WATERING
# ===============================
def water_all_due_plants(db: Session, user_id: int):
    plants = _get_thirsty_plants(db, user_id)

    for plant in plants:
        plant.last_watered = date.today()

        # Delete the active notification for each plant
        db.query(Notification).filter(
            Notification.plant_id == plant.id,
            Notification.user_id == user_id,
            Notification.type == "irrigation"
        ).delete(synchronize_session=False)

    db.commit()
    return plants


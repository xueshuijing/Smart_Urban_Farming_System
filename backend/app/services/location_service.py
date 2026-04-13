from sqlalchemy.orm import Session
from app.models.location import Location
from app.schemas.location_schema import LocationCreate, LocationUpdate


# ===============================
# CREATE
# ===============================
def create_location(db: Session, location: LocationCreate, user_id: int):
    new_location = Location(
        name=location.name,
        description=location.description,
        environment_type=location.environment_type,
        user_id=user_id
    )

    db.add(new_location)
    db.commit()
    db.refresh(new_location)

    return new_location


# ===============================
# GET ALL
# ===============================
def get_locations(db: Session, user_id: int):
    return db.query(Location).filter(Location.user_id == user_id).all()


# ===============================
# GET ONE
# ===============================
def get_location(db: Session, location_id: int, user_id: int):
    return db.query(Location).filter(
        Location.id == location_id,
        Location.user_id == user_id
    ).first()


# ===============================
# UPDATE
# ===============================
def update_location(db: Session, location_id: int, location_update: LocationUpdate, user_id: int):
    location = db.query(Location).filter(
        Location.id == location_id,
        Location.user_id == user_id
    ).first()

    if not location:
        return None

    for field, value in location_update.dict(exclude_unset=True).items():
        setattr(location, field, value)

    db.commit()
    db.refresh(location)

    return location


# ===============================
# DELETE
# ===============================
def delete_location(db: Session, location_id: int, user_id: int):
    location = db.query(Location).filter(
        Location.id == location_id,
        Location.user_id == user_id
    ).first()

    if not location:
        return None

    db.delete(location)
    db.commit()

    return True

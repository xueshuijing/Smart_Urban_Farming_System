#tests/fixtures/plant_fixtures.py


import pytest
from app.models.plant import Plant
from app.models.plant_species_cache import PlantSpeciesCache


# -------------------------
# DB LEVEL PLANT
# -------------------------
@pytest.fixture
def plant(db, species):
    plant = Plant(
        name="Test Plant",
        species_id=species.id,
        user_id=1,
        watering_interval_days=3,
        last_watered=None,
        use_sensor=False
    )
    db.add(plant)
    db.commit()
    db.refresh(plant)
    return plant


@pytest.fixture
def sensor_plant(db, species):
    plant = Plant(
        name="Sensor Plant",
        species_id=species.id,
        user_id=1,
        watering_interval_days=3,
        last_watered=None,
        use_sensor=True
    )
    db.add(plant)
    db.commit()
    db.refresh(plant)
    return plant


# -------------------------
# API LEVEL PLANT
# -------------------------
@pytest.fixture
def plant_api(client, user_token,species):
    response = client.post(
        "/plants/",
        json={
            "name": "API Plant",
            "plant_species.id": species.id,
            "environment_type": "indoor"
        },
        headers={"Authorization": f"Bearer {user_token}"}
    )

    return response.json()

@pytest.fixture
def species(db):
    sp = PlantSpeciesCache(scientific_name="Test")
    db.add(sp)
    db.commit()
    db.refresh(sp)
    return sp
import pytest
from datetime import date, timedelta
from app.models.plant import Plant
from app.services.irrigation_service import needs_watering


# ===============================
# TEST: never watered
# ===============================
def test_needs_watering_never_watered():
    plant = Plant(
        last_watered=None,
        watering_interval_days=3
    )

    assert needs_watering(plant) is True


# ===============================
# TEST: recently watered
# ===============================
def test_needs_watering_recent():
    plant = Plant(
        last_watered=date.today(),
        watering_interval_days=3
    )

    assert needs_watering(plant) is False


# ===============================
# TEST: exactly due
# ===============================
def test_needs_watering_due_today():
    plant = Plant(
        last_watered=date.today() - timedelta(days=3),
        watering_interval_days=3
    )

    assert needs_watering(plant) is True


# ===============================
# TEST: overdue
# ===============================
def test_needs_watering_overdue():
    plant = Plant(
        last_watered=date.today() - timedelta(days=5),
        watering_interval_days=3
    )

    assert needs_watering(plant) is True

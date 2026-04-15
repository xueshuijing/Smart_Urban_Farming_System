# tests/conftest.py

import pytest
import uuid
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient

from main import app
from app.database.db import Base, get_db


# -----------------------------
# TEST DATABASE (IN-MEMORY)
# -----------------------------
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool  # IMPORTANT for in-memory DB
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# -----------------------------
# OVERRIDE DEPENDENCY
# -----------------------------
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# -----------------------------
# CLIENT FIXTURE
# -----------------------------
@pytest.fixture(scope="function")
def client():
    app.dependency_overrides[get_db] = override_get_db

    Base.metadata.create_all(bind=engine)

    with TestClient(app) as c:
        yield c

    Base.metadata.drop_all(bind=engine)
    app.dependency_overrides.clear()


# -----------------------------
# USER FACTORY FIXTURE
# -----------------------------
@pytest.fixture
def create_user(client):
    def _create_user(email=None, password="test12345"):
        if not email:
            email = f"test_{uuid.uuid4()}@example.com"

        # Register
        client.post("/auth/register", json={
            "email": email,
            "password": password
        })

        # Login
        response = client.post("/auth/login", data={
            "username": email,
            "password": password
        })

        assert response.status_code == 200, f"Login failed: {response.text}"

        return response.json()["access_token"]

    return _create_user


# -----------------------------
# DEFAULT TOKEN FIXTURE
# -----------------------------
@pytest.fixture
def token(create_user):
    return create_user()

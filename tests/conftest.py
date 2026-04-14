import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
import uuid
import pytest
from main import app
from app.database.db import Base, get_db

# Use SQLite for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Override DB dependency
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="function")
def client():
    # Create fresh DB
    Base.metadata.create_all(bind=engine)

    with TestClient(app) as c:
        yield c

    # Drop DB after tests
    Base.metadata.drop_all(bind=engine)




@pytest.fixture
def token(client):
    """
    Create a unique user and return JWT token.
    Shared across all test files.
    """
    unique_email = f"test_{uuid.uuid4()}@example.com"
    password = "test12345"

    # Register
    client.post(
        "/auth/register",
        json={
            "email": unique_email,
            "password": password
        }
    )

    # Login (OAuth2 requires form data)
    response = client.post(
        "/auth/login",
        data={
            "username": unique_email,
            "password": password
        }
    )

    assert response.status_code == 200, f"Login failed: {response.text}"

    return response.json()["access_token"]
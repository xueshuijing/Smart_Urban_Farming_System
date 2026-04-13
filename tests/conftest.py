import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture(scope="module")
def client():
    """
    Create a reusable test client for all tests
    """
    with TestClient(app) as c:
        yield c

import pytest
from fastapi.testclient import TestClient
from main import app

#using fixture to set client to be used for all the tests
@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

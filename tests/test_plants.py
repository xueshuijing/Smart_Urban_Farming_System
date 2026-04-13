import uuid


def get_auth_token(client):
    unique_email = f"test_{uuid.uuid4()}@example.com"

    # Register user
    client.post(
        "/auth/register",
        json={
            "email": unique_email,
            "password": "test123"
        }
    )

    # Login user
    response = client.post(
        "/auth/login",
        json={
            "email": unique_email,
            "password": "test123"
        }
    )

    # Debug safety (optional but smart)
    assert response.status_code == 200, response.json()

    return response.json()["access_token"]


def test_create_plant(client):
    token = get_auth_token(client)

    response = client.post(
        "/plants",
        json={
            "name": "Tomato",
            "species": "Solanum lycopersicum",
            "location": "Greenhouse"
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200


def test_get_plants(client):
    token = get_auth_token(client)

    response = client.get(
        "/plants",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200

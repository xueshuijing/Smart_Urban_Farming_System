# tests/utils/test_helpers.py

def create_test_plant(client, token):
    """
    Helper to create a plant with authentication.
    Keeps test code clean and reusable.
    """
    return client.post(
        "/plants/",
        json={
            "name": "Test Plant",
            "species": "Test Species",
            "environment_type": "indoor",
            "is_synced": True,
            "source": "test"
        },
        headers={"Authorization": f"Bearer {token}"}
    )

def create_test_location(client, token):
    """
    Helper to create a location.
    """
    return client.post(
        "/locations/",
        json={
            "name": "Test Location",
            "description": "Test Desc",
            "environment_type": "indoor"
        },
        headers={"Authorization": f"Bearer {token}"}
    )

def create_test_location(client, token):
    """
    Create a location and return its response JSON.
    """
    response = client.post(
        "/locations/",
        json={
            "name": "Test Location",
            "description": "Test Desc",
            "environment_type": "indoor"
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code in [200, 201]
    return response.json()

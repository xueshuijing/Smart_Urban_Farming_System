def create_test_plant(client):
    return client.post(
        "/plants",
        json={
            "name": "Test Plant",
            "species": "Test Species",
            "location": "Test Lab"
        }
    )

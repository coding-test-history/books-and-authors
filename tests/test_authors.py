import pytest
from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)


@pytest.fixture
def test_author_data():
    return {"name": "Test Author", "bio": "Test bio", "birth_date": "1980-01-01"}

### Test Authors ###
def test_create_author(test_author_data):
    response = client.post("/authors/store", json=test_author_data)
    assert response.status_code == 201
    assert response.json()["data"]["name"] == test_author_data["name"]

def test_get_author_by_id(test_author_data):
    create_response = client.post("/authors/store", json=test_author_data)
    author_id = create_response.json()["data"]["id"]

    get_response = client.get(f"/authors/{author_id}")
    assert get_response.status_code == 200
    assert get_response.json()["data"]["name"] == test_author_data["name"]


def test_update_author(test_author_data):
    create_response = client.post("/authors/store", json=test_author_data)
    author_id = create_response.json()["data"]["id"]

    updated_data = {"name": "Updated Author", "bio": "Updated bio", "birth_date": "1990-01-01"}
    update_response = client.put(f"/authors/update/{author_id}", json=updated_data)
    assert update_response.status_code == 200
    assert update_response.json()["data"]["name"] == "Updated Author"


def test_delete_author(test_author_data):
    create_response = client.post("/authors/store", json=test_author_data)
    author_id = create_response.json()["data"]["id"]

    delete_response = client.delete(f"/authors/delete/{author_id}")
    assert delete_response.status_code == 204

    # Verify deletion
    get_response = client.get(f"/authors/{author_id}")
    assert get_response.status_code == 404


### Edge Case Tests ###
def test_get_nonexistent_author():
    response = client.get("/authors/9999")
    assert response.status_code == 404


def test_get_nonexistent_books_for_author():
    response = client.get("/authors/9999/books")
    assert response.status_code == 404

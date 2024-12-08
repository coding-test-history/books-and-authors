import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


@pytest.fixture
def test_author_data():
    return {"name": "Test Author", "bio": "Test bio", "birth_date": "1980-01-01"}


@pytest.fixture
def test_book_data():
    return {
        "title": "Test Book",
        "description": "Test description",
        "publish_date": "2024-01-01",
    }


### Test Books ###
def test_create_book(test_book_data, test_author_data):
    author_response = client.post("/authors/store", json=test_author_data)
    author_id = author_response.json()["data"]["id"]
    test_book_data["author_id"] = author_id
    response = client.post("/books/store", json=test_book_data)
    assert response.status_code == 201
    assert response.json()["data"]["title"] == test_book_data["title"]


def test_get_books_by_author():
    author_response = client.post(
        "/authors/store/",
        json={"name": "Author with Books", "bio": "Bio", "birth_date": "1975-01-01"},
    )
    author_id = author_response.json()["data"]["id"]

    client.post(
        "/books/store/",
        json={
            "title": "Book 1",
            "description": "Description 1",
            "publish_date": "2024-01-01",
            "author_id": author_id,
        },
    )
    client.post(
        "/books/store/",
        json={
            "title": "Book 2",
            "description": "Description 2",
            "publish_date": "2024-02-01",
            "author_id": author_id,
        },
    )

    response = client.get(f"/authors/{author_id}/books")
    assert response.status_code == 200
    assert len(response.json()["data"]) == 2


def test_update_book(test_book_data, test_author_data):
    author_response = client.post("/authors/store/", json=test_author_data)
    author_id = author_response.json()["data"]["id"]
    test_book_data["author_id"] = author_id

    book_response = client.post("/books/store/", json=test_book_data)
    book_id = book_response.json()["data"]["id"]

    updated_data = {
        "title": "Updated Book",
        "description": "Updated description",
        "publish_date": "2024-06-01",
        "author_id": author_id,
    }
    response = client.put(f"/books/update/{book_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["data"]["title"] == updated_data["title"]


def test_delete_book(test_book_data, test_author_data):
    author_response = client.post("/authors/store/", json=test_author_data)
    author_id = author_response.json()["data"]["id"]
    test_book_data["author_id"] = author_id

    book_response = client.post("/books/store/", json=test_book_data)
    book_id = book_response.json()["data"]["id"]

    response = client.delete(f"/books/delete/{book_id}")
    assert response.status_code == 204


### Edge Case Tests ###
def test_create_book_with_nonexistent_author(test_book_data):
    test_book_data["author_id"] = 9999
    response = client.post("/books/store/", json=test_book_data)
    assert response.status_code == 400

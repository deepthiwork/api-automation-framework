from utils.api_client import ApiClient
import pytest

@pytest.mark.parametrize("usere_id", [1, 2, 3, 4, 5])

def test_multiple_users(base_url, usere_id):
    api_client = ApiClient(base_url)
    response = api_client.get(f"/users/{usere_id}")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == usere_id
    assert data["name"].strip() != ""
    assert data["username"].strip() != ""
    assert data["email"].strip() != ""

@pytest.mark.parametrize("user_id", [999, 1000, 1001])
def  test_multiple_invalid_users(base_url, user_id):
    api_client = ApiClient(base_url)
    response = api_client.get(f"/users/{user_id}")
    assert response.status_code == 404

def test_api_client_header(base_url):
    api_client = ApiClient(base_url)
    assert api_client.session.headers["Accept"] == "application/json"

def test_get_user(base_url):
    api_client = ApiClient(base_url)

    response = api_client.get("/users/1")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert data["name"] != ""

def test_create_user(base_url):
    api_client = ApiClient(base_url)
    data = {
        "name": "Test User",
        "username": "testuser",
        "email": "testuser@example.com"
    }
    response = api_client.post("/users", data=data)
    assert response.status_code == 201

    response_data = response.json()
    assert response_data["name"] == "Test User"
    assert response_data["username"] == "testuser"
    assert response_data["email"] == "testuser@example.com"

def test_delete_user(base_url):
    api_client = ApiClient(base_url)
    response = api_client.delete("/users/1")
    assert response.status_code == 200

def test_update_user(base_url):
    api_client = ApiClient(base_url)
    data = {
        "name": "Updated User",
        "username": "updateduser",
        "email": "updated@example.com"
    }
    response = api_client.put("/users/1", data)
    assert response.status_code == 200

    response_data = response.json()
    assert response_data["name"] == "Updated User"
    assert response_data["username"] == "updateduser"
    assert response_data["email"] == "updated@example.com"

def test_user_not_found(base_url):
    api_client = ApiClient(base_url)
    response = api_client.get("/users/ 9999")
    assert response.status_code == 404

def test_invalid_endpoint(base_url):
    api_client = ApiClient(base_url)
    response = api_client.get("/invalid-endpoint")
    assert response.status_code == 404

def test_user_response_is_json(base_url):
    api_client = ApiClient(base_url)
    response = api_client.get("/users/1")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    data = response.json()
    assert isinstance(data, dict)   
    assert data["id"] == 1

def test_user_fields_are_not_empty(base_url):
    api_client = ApiClient(base_url)
    response = api_client.get("/users/1")
    assert response.status_code == 200

    data = response.json()
    assert data["name"].strip() != ""
    assert data["username"].strip() != ""
    assert data["email"].strip() != ""
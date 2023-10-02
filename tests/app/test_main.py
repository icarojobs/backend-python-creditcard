import sys

sys.path.append('../../')

from fastapi.testclient import TestClient
from fastapi import status
from app.main import app
from app.helpers.custom_helpers import random_string

client = TestClient(app=app)


def test_index_route():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"ping": "pong!"}


def test_register_new_user():
    random_user = random_string()

    response = client.post(
        url="/v1/users",
        json={
          "username": random_user,
          "password": "password"
        }
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {
      "status": True,
      "message": "User registered successfully!"
    }


def test_if_user_exists():
    pass


def test_if_user_login_works():
    pass
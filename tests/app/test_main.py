import sys

sys.path.append('../../')

from fastapi.testclient import TestClient
from fastapi import status
from app.main import app

client = TestClient(app=app)


def test_index_route():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"ping": "pong!"}

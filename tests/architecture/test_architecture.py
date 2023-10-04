from decouple import config
from fastapi.testclient import TestClient
from fastapi import status
from app.main import app

client = TestClient(app=app)


def test_database_connection():
    database_name = config('POSTGRES_DB')
    assert config('DB_URL') == f"postgresql+psycopg2://database/{database_name}?user=admin&password=password"


def test_if_ping_endpoint_is_working():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"ping": "pong!"}
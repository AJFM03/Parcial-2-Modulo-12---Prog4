import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_vacunas(client):
    response = client.get("/vacunas")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_vacuna_por_anio_existente(client):
    response = client.get("/vacunas/2005")
    assert response.status_code == 200
    data = response.get_json()
    assert data["anio"] == 2005

def test_get_vacuna_por_anio_inexistente(client):
    response = client.get("/vacunas/1999")
    assert response.status_code == 404

def test_get_vacuna_provincia(client):
    response = client.get("/vacunas/provincia/Panamá")
    assert response.status_code == 200
    data = response.get_json()
    assert data["provincia"] == "Panamá"

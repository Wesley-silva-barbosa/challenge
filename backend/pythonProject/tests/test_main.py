from fastapi.testclient import TestClient

from .mock_main import app

client = TestClient(app)

def test_find_insights():
    response = client.get("/insights/", headers={"X-Token": "unitTest"})
    assert response.status_code == 200

def test_find_insights_bad_token():
    response = client.get("/insights/", headers={"X-Token": "mockUnitTest"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}

def test_create_insight():
    response = client.post(
        "/insights/",
        headers={"X-Token": "unitTest"},
        json={"id": 0, "descricao": "Rodada iniciada", "categoria": "Brasileirão"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 0,
        "descricao": "Rodada iniciada",
        "categoria": "Brasileirão",
    }

def test_create_insight_bad_token():
    response = client.post(
        "/insights/",
        headers={"X-Token": "mockUnitTest"},
        json={"id": 0, "descricao":"Rodada 7 é cancelada por mau tempo", "categoria": "notícias"},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}

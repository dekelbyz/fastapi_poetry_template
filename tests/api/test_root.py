from tests.mock import client


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Server is running..."

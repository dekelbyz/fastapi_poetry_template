from fastapi.testclient import TestClient

from fastapi_poetry_template.server import app

client = TestClient(app)


def test_example_route():
    """Testing the example route of the example entity."""
    response = client.get("/example")
    assert response.status_code == 200
    assert response.json() == "Hello World!"

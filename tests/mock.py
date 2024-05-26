from fastapi.testclient import TestClient

from fastapi_poetry_template.server import app

# test client (rest API)
client = TestClient(app)

from fastapi.testclient import TestClient
from fastapi_poetry_template.server import app
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker

# test client (rest API)
client = TestClient(app)

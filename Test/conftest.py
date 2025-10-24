# Test/conftest.py
import pytest
from server import app

@pytest.fixture
def client():
    """Fixture pour créer un client Flask réutilisable"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

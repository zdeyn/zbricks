import pytest
from zbricks import zFlask
from flask import Flask
from hello import create_app # type: ignore[import]

@pytest.fixture
def app() -> zFlask:
    app = create_app()
    return app

def test_app_is_Flask(app):
    assert isinstance(app, Flask)

def test_app_responds(app: zFlask):
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'
import pytest
from zbricks import zFlask
from project import create_app

@pytest.fixture
def app() -> zFlask:
    app = create_app()
    return app

def test_app_is_Flask(app):
    assert isinstance(app, zFlask)

def test_app_responds(app: zFlask):
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert 'Hello, World!' in response.data.decode('utf-8')
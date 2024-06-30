import pytest
from zbricks import zFlask, create_flask

@pytest.fixture
def flask() -> zFlask:
    flask = create_flask(__name__)
    return flask

def test_create_flask():
    flask = create_flask(__name__)
    assert isinstance(flask, zFlask)
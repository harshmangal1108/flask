## for testing -- filename is specific that pytest will look for
import pytest
from urlshort import create_app

## 
@pytest.fixture
def app():
    app=create_app()

## so testing fw can test if it was a browser and testing out project for us
@pytest.fixture
def client(app):
    return app.test_client()
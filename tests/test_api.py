from unittest.mock import Mock

from starlette.testclient import TestClient

from app.config.dependency import get_sprocket_dao
from app.dao.sprocket_dao import SprocketDao
from app.main import app

client = TestClient(app)


def get_mock_sprocket_dao():
    mock_sprocket_dao = Mock(SprocketDao)
    mock_sprocket_dao.list = Mock(return_value=[])
    return mock_sprocket_dao


app.dependency_overrides[get_sprocket_dao] = get_mock_sprocket_dao


def test_list_sprockets_empty():
    response = client.get("/sprockets")
    assert response.status_code == 200
    assert response.json() == []

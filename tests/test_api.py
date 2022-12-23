"""
This module serves as an example of test cases and is not meant to provide complete code coverage for this project.
"""
from unittest.mock import Mock

from starlette.testclient import TestClient

from app.config.dependency import get_sprocket_dao
from app.dao.sprocket_dao import SprocketDao
from app.main import app
from app.orm.sprocket import Sprocket

client = TestClient(app)


def get_mock_sprocket_dao():
    mock_sprocket_dao = Mock(SprocketDao)
    mock_sprocket_dao.list = Mock(return_value=[Sprocket(id="test", pitch_diameter=5)])
    return mock_sprocket_dao


def get_empty_sprocket_dao():
    mock_sprocket_dao = Mock(SprocketDao)
    mock_sprocket_dao.list = Mock(return_value=[])
    return mock_sprocket_dao


def test_list_sprockets_empty():
    app.dependency_overrides[get_sprocket_dao] = get_empty_sprocket_dao
    response = client.get("/sprockets")
    assert response.status_code == 200
    assert response.json() == []


def test_list_sprockets_one():
    app.dependency_overrides[get_sprocket_dao] = get_mock_sprocket_dao
    response = client.get("/sprockets")
    assert response.status_code == 200
    assert response.json() == [{'id': 'test', 'pitch_diameter': 5}]

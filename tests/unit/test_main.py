from unittest.mock import patch, MagicMock, _patch, AsyncMock

import pytest

import json

import src.main
from src.main import ping, app, get_users
from src.STATUS_CODES import OK


def test_ping_exists() -> None:
    assert ping


def test_ping_returns_right_value() -> None:
    actual = ping()
    assert actual == "pong"


def test_get_users_returns_right_code() -> None:
    with patch("src.main.get_users_controller") as get_users_controller:
        get_users_controller.get.return_value = []
        actual = get_users().status
    assert actual == OK


def test_get_users_returns_right_value() -> None:
    with patch("src.main.get_users_controller") as get_users_controller:
        get_users_controller.get.return_value = [
            {
                "id": 0,
                "first_name": "test",
                "last_name": "test",
                "age": 20,
                "group": "user"
            }
        ]
        actual = get_users().data
    assert actual == json.dumps([
            {
                "id": 0,
                "first_name": "test",
                "last_name": "test",
                "age": 20,
                "group": "user"
            }
        ]).encode()

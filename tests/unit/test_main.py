from unittest.mock import patch

import pytest

import json

import src.main
from src.main import ping, get_users, get_user
from src.STATUS_CODES import OK, BAD_REQUEST


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


def test_get_users_returns_right_200_code() -> None:
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
        actual = get_user(0).status
    assert actual == OK


def test_get_users_returns_right_400_code() -> None:
    with patch("src.main.get_users_controller") as get_users_controller:
        get_users_controller.get.side_effect = ValueError
        actual = get_user(1).status
    assert actual == BAD_REQUEST


def test_get_users_passes_id() -> None:
    with patch("src.main.get_users_controller") as get_users_controller:
        get_users_controller.get.return_value = []
        get_user(1)
    get_users_controller.get.assert_called_with(id=1)


def test_get_user_returns_right_value() -> None:
    with patch("src.main.get_users_controller") as get_users_controller:
        get_users_controller.get.return_value = {
            "id": 0,
            "first_name": "test",
            "last_name": "test",
            "age": 20,
            "group": "user"
        }
        actual = get_user(0).data
    assert actual == json.dumps({
        "id": 0,
        "first_name": "test",
        "last_name": "test",
        "age": 20,
        "group": "user"
    }).encode()

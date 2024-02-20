from unittest.mock import patch

import pytest

import json

import src.main
from src.main import ping, get_users, get_user, post_user, app, patch_user, delete_user
from src.STATUS_CODES import OK, BAD_REQUEST, CREATED, NO_CONTENT


@pytest.fixture()
def user() -> dict[str, int | str]:
    return {
        "first_name": "test",
        "last_name": "test",
        "birth_year": 2000,
        "group": "user"
    }


@pytest.fixture()
def users() -> list[dict[str, int | str]]:
    return [{
        "id": 0,
        "first_name": "test",
        "last_name": "test",
        "age": 20,
        "group": "user"
    }]


@pytest.fixture()
def aged_user() -> dict[str, int | str]:
    return {
        "id": 0,
        "first_name": "test",
        "last_name": "test",
        "age": 20,
        "group": "user"
    }


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


def test_get_users_returns_right_value(users: list[dict[str, int | str]]) -> None:
    with patch("src.main.get_users_controller") as get_users_controller:
        get_users_controller.get.return_value = users
        actual = get_users().data
    assert actual == json.dumps(users).encode()


def test_get_user_returns_right_200_code(users: list[dict[str, int | str]]) -> None:
    with patch("src.main.get_users_controller") as get_users_controller:
        get_users_controller.get.return_value = users
        actual = get_user(0).status
    assert actual == OK


def test_get_user_returns_right_400_code() -> None:
    with patch("src.main.get_users_controller") as get_users_controller:
        get_users_controller.get.side_effect = ValueError
        actual = get_user(1).status
    assert actual == BAD_REQUEST


def test_get_user_passes_id() -> None:
    with patch("src.main.get_users_controller") as get_users_controller:
        get_users_controller.get.return_value = []
        get_user(1)
    get_users_controller.get.assert_called_with(id=1)


def test_get_user_returns_right_value(aged_user: dict[str, int | str]) -> None:
    with patch("src.main.get_users_controller") as get_users_controller:
        get_users_controller.get.return_value = aged_user
        actual = get_user(0).data
    assert actual == json.dumps(aged_user).encode()


def test_post_user_passes_right_user(user: dict[str, int | str]) -> None:
    with (
        patch("src.main.create_users_controller") as create_users_controller,
        app.test_request_context(json=user)
    ):
        post_user()
    create_users_controller.create.assert_called_with(user)


def test_post_user_returns_right_200_code(user: dict[str, int | str]) -> None:
    with app.test_request_context(json=user):
        actual = post_user().status
    assert actual == CREATED


def test_post_user_returns_right_400_code() -> None:
    with (
        patch("src.main.create_users_controller") as create_users_controller,
        app.test_request_context(json={
            "first_name": "test",
            "last_name": "test",
            "birth_year": 2000
        })
    ):
        create_users_controller.create.side_effect = ValueError("Missing one of the arguments.")
        actual = post_user().status
    assert actual == BAD_REQUEST


def test_post_user_returns_right_error_code() -> None:
    with (
        patch("src.main.create_users_controller") as create_users_controller,
        app.test_request_context(json={
            "first_name": "test",
            "last_name": "test",
            "birth_year": 2000
        })
    ):
        create_users_controller.create.side_effect = ValueError("Missing one of the arguments.")
        actual = post_user().data
    assert actual == "Missing one of the arguments.".encode()


def test_patch_user_passes_right_values(user: dict[str, int | str]) -> None:
    with (
        patch("src.main.update_users_controller") as update_users_controller,
        app.test_request_context(json=user)
    ):
        patch_user(0)
    update_users_controller.update.assert_called_with(0, user)


def test_patch_user_returns_right_204_code(user: dict[str, int | str]) -> None:
    with (
        patch("src.main.update_users_controller"),
        app.test_request_context(json=user)
    ):
        actual = patch_user(0).status
    assert actual == NO_CONTENT


def test_patch_user_returns_right_400_code(user: dict[str, int | str]) -> None:
    with (
        patch("src.main.update_users_controller") as update_users_controller,
        app.test_request_context(json=user)
    ):
        update_users_controller.update.side_effect = ValueError
        actual = patch_user(0).status
    assert actual == BAD_REQUEST


def test_patch_user_returns_right_error_code(user: dict[str, int | str]) -> None:
    with (
        patch("src.main.update_users_controller") as update_users_controller,
        app.test_request_context(json=user)
    ):
        update_users_controller.update.side_effect = ValueError("Invalid id.")
        actual = patch_user(0).data
    assert actual == "Invalid id.".encode()


def test_delete_user_passes_right_id() -> None:
    with patch("src.main.delete_users_controller") as delete_users_controller:
        delete_user(0)
    delete_users_controller.delete.assert_called_with(0)


def test_delete_user_returns_right_204_code() -> None:
    with patch("src.main.delete_users_controller"):
        actual = delete_user(0).status
    assert actual == NO_CONTENT


def test_delete_user_returns_right_400_code() -> None:
    with patch("src.main.delete_users_controller") as delete_users_controller:
        delete_users_controller.delete.side_effect = ValueError
        actual = delete_user(0).status
    assert actual == BAD_REQUEST


def test_delete_user_returns_right_error_code() -> None:
    with patch("src.main.delete_users_controller") as delete_users_controller:
        delete_users_controller.delete.side_effect = ValueError("Invalid id.")
        actual = delete_user(0).data
    assert actual == "Invalid id.".encode()

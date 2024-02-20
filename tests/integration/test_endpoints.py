from src.main import app
from src.STATUS_CODES import OK, BAD_REQUEST, CREATED, NO_CONTENT

from flask.testing import FlaskClient

import pytest


@pytest.fixture()
def client() -> FlaskClient:
    return app.test_client()


def test_get_users_endpoint_returns_right_200_code(client: FlaskClient) -> None:
    actual = client.get("/users").status
    assert actual == OK


def test_get_user_endpoint_returns_right_200_code(client: FlaskClient) -> None:
    client.post("/users", json={
        "first_name": "test",
        "last_name": "test",
        "birth_year": 2000,
        "group": "user"
    })
    actual = client.get("/users/0").status
    assert actual == OK


def test_get_user_endpoint_returns_right_400_code(client: FlaskClient) -> None:
    actual = client.get("/users/2").status
    assert actual == BAD_REQUEST


def test_post_user_endpoint_returns_right_200_code(client: FlaskClient) -> None:
    actual = client.post("/users", json={
        "first_name": "test",
        "last_name": "test",
        "birth_year": 2000,
        "group": "user"
    }).status
    assert actual == CREATED


def test_post_user_endpoint_returns_right_400_code(client: FlaskClient) -> None:
    actual = client.post("/users", json={
        "last_name": "test",
        "birth_year": 2000,
        "group": "user"
    }).status
    assert actual == BAD_REQUEST


def test_patch_user_endpoint_returns_right_200_code(client: FlaskClient) -> None:
    actual = client.patch("/users/0", json={
        "last_name": "test2",
    }).status
    assert actual == NO_CONTENT


def test_patch_user_endpoint_returns_right_400_code(client: FlaskClient) -> None:
    actual = client.patch("/users/0", json={
        "test": "test2",
    }).status
    assert actual == BAD_REQUEST


def test_delete_user_endpoint_returns_right_200_code(client: FlaskClient) -> None:
    actual = client.delete("/users/0").status
    assert actual == NO_CONTENT


def test_delete_user_endpoint_returns_right_400_code(client: FlaskClient) -> None:
    actual = client.delete("/users/2").status
    assert actual == BAD_REQUEST

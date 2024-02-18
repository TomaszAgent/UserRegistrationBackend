import pytest

from unittest.mock import Mock

from src.controllers import CreateUserController

from src.repositories import UsersRepository


@pytest.fixture()
def users_repository() -> Mock:
    return Mock(UsersRepository)


@pytest.fixture()
def create_user_controller(users_repository: Mock) -> CreateUserController:
    return CreateUserController(repository=users_repository)


def test_create_user_controller_exists():
    assert create_user_controller


def test_create_user_controller_passes_user(
        create_user_controller: CreateUserController,
        users_repository: Mock
) -> None:
    create_user_controller.create("test", "test", 2000, "user")
    users_repository.add_user.assert_called_with("test", "test", 2000, "user")

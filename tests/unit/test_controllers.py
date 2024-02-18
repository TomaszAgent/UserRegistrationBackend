import pytest

from unittest.mock import Mock

from src.controllers import CreateUserController, GetUsersController

from src.repositories import UsersRepository


@pytest.fixture()
def users_repository() -> Mock:
    return Mock(UsersRepository)


@pytest.fixture()
def create_user_controller(users_repository: Mock) -> CreateUserController:
    return CreateUserController(repository=users_repository)


@pytest.fixture()
def get_users_controller(users_repository: Mock) -> GetUsersController:
    return GetUsersController(repository=users_repository)


def test_create_user_controller_exists() -> None:
    assert create_user_controller


def test_create_user_controller_passes_user(
        create_user_controller: CreateUserController,
        users_repository: Mock
) -> None:
    create_user_controller.create("test", "test", 2000, "user")
    users_repository.add_user.assert_called_with("test", "test", 2000, "user")


def test_create_user_raises_first_name_type_error(create_user_controller: CreateUserController) -> None:
    with pytest.raises(TypeError) as actual:
        create_user_controller.create(0, "test", 2000, "user")
    assert str(actual.value) == "One of arguments was of invalid type."


def test_create_user_raises_last_name_type_error(create_user_controller: CreateUserController) -> None:
    with pytest.raises(TypeError) as actual:
        create_user_controller.create("test", 0, 2000, "user")
    assert str(actual.value) == "One of arguments was of invalid type."


def test_create_user_raises_birth_year_type_error(create_user_controller: CreateUserController) -> None:
    with pytest.raises(TypeError) as actual:
        create_user_controller.create("test", "test", "test", "user")
    assert str(actual.value) == "One of arguments was of invalid type."


def test_create_user_raises_group_type_error(create_user_controller: CreateUserController) -> None:
    with pytest.raises(TypeError) as actual:
        create_user_controller.create("test", "test", 2000, 0)
    assert str(actual.value) == "One of arguments was of invalid type."


def test_create_user_raises_birth_year_value_error(create_user_controller: CreateUserController) -> None:
    with pytest.raises(ValueError) as actual:
        create_user_controller.create("test", "test", 3000, "user")
    assert str(actual.value) == "The user can't be from the future."


def test_create_user_raises_group_value_error(create_user_controller: CreateUserController) -> None:
    with pytest.raises(ValueError) as actual:
        create_user_controller.create("test", "test", 2000, "person")
    assert str(actual.value) == "Invalid group."


def test_get_users_raises_value_error(get_users_controller: GetUsersController, users_repository: Mock) -> None:
    users_repository.get_users.return_value = []
    with pytest.raises(ValueError) as actual:
        get_users_controller.get(0)
    assert str(actual.value) == "Invalid id."


def test_get_users_returns_users(get_users_controller: GetUsersController, users_repository: Mock) -> None:
    users_repository.get_users.return_value = [
        {
            'id': 0,
            'first_name': 'test',
            'last_name': 'test',
            'birth_year': 2000,
            'group': 'user'
        }
    ]
    actual = get_users_controller.get()
    assert actual == [
        {
            'id': 0,
            'first_name': 'test',
            'last_name': 'test',
            'birth_year': 2000,
            'group': 'user'
        }
    ]


def test_get_users_returns_user_by_id(get_users_controller: GetUsersController, users_repository: Mock) -> None:
    users_repository.get_users.return_value = [
        {
            'id': 0,
            'first_name': 'test',
            'last_name': 'test',
            'birth_year': 2000,
            'group': 'user'
        }
    ]
    actual = get_users_controller.get(0)
    assert actual == {
            'id': 0,
            'first_name': 'test',
            'last_name': 'test',
            'birth_year': 2000,
            'group': 'user'
        }

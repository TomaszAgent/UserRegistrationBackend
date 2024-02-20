import pytest

from unittest.mock import Mock

from src.controllers import CreateUserController, GetUsersController, UpdateUserController, DeleteUserController

from src.repositories import UsersRepository

from src.data_transfer_objects import UserDTO


@pytest.fixture()
def users_repository() -> Mock:
    return Mock(UsersRepository)


@pytest.fixture()
def user_dto() -> Mock:
    return Mock(UserDTO)


@pytest.fixture()
def create_user_controller(users_repository: Mock, user_dto: UserDTO) -> CreateUserController:
    return CreateUserController(repository=users_repository, dto=user_dto)


@pytest.fixture()
def get_users_controller(users_repository: Mock) -> GetUsersController:
    return GetUsersController(repository=users_repository)


@pytest.fixture()
def update_user_controller(users_repository: Mock, user_dto: UserDTO) -> UpdateUserController:
    return UpdateUserController(repository=users_repository, dto=user_dto)


@pytest.fixture()
def delete_user_controller(users_repository: Mock) -> DeleteUserController:
    return DeleteUserController(repository=users_repository)


def test_create_user_controller_exists() -> None:
    assert create_user_controller


def test_create_user_controller_passes_user_data(
        create_user_controller: CreateUserController,
        users_repository: Mock,
        user_dto: Mock
) -> None:
    user_dto.get_data.return_value = ("test", "test", 2000, "user")
    create_user_controller.create({
        "first_name": "test",
        "last_name": "test",
        "birth_year": 2000,
        "group": "user"
    })
    users_repository.add_user.assert_called_with("test", "test", 2000, "user")


def test_create_user_passes_user_dict(
        create_user_controller: CreateUserController,
        user_dto: Mock
) -> None:
    user_dto.get_data.return_value = ("test", "test", 2000, "user")
    create_user_controller.create({
        "first_name": "test",
        "last_name": "test",
        "birth_year": 2000,
        "group": "user"
    })
    user_dto.add_data.assert_called_with({
        "first_name": "test",
        "last_name": "test",
        "birth_year": 2000,
        "group": "user"
    })


def test_create_user_raises_value_error(
        create_user_controller: CreateUserController,
        user_dto: Mock
) -> None:
    user_dto.get_data.return_value = ("test", "test", None, "user")
    with pytest.raises(ValueError) as actual:
        create_user_controller.create({
            "first_name": "test",
            "last_name": "test",
            "group": "user"
        })
    assert str(actual.value) == "Missing one of the arguments."


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
            'age': 24,
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
        'age': 24,
        'group': 'user'
    }


def test_update_user_controller_passes_user_data(
        update_user_controller: UpdateUserController,
        users_repository: Mock,
        user_dto: Mock
) -> None:
    user_dto.get_data.return_value = ("test", "test", 2000, "user")
    users_repository.get_users.return_value = [
        {
            'id': 0,
            'first_name': 'test',
            'last_name': 'test',
            'birth_year': 2000,
            'group': 'user'
        }
    ]
    update_user_controller.update(0, {
        "first_name": "test",
        "last_name": "test",
        "birth_year": 2000,
        "group": "user"
    })
    users_repository.update_user.assert_called_with(0, "test", "test", 2000, "user")


def test_update_user_controller_passes_user_dict(
        update_user_controller: UpdateUserController,
        users_repository: Mock,
        user_dto: Mock
) -> None:
    user_dto.get_data.return_value = ("test", "test", 2000, "user")
    users_repository.get_users.return_value = [
        {
            'id': 0,
            'first_name': 'test',
            'last_name': 'test',
            'birth_year': 2000,
            'group': 'user'
        }
    ]
    update_user_controller.update(0, {
        "first_name": "test",
        "last_name": "test",
        "birth_year": 2000,
        "group": "user"
    })
    user_dto.add_data.assert_called_with({
        "first_name": "test",
        "last_name": "test",
        "birth_year": 2000,
        "group": "user"
    })


def test_update_user_raises_type_error_on_id(
        update_user_controller: UpdateUserController,
        users_repository: Mock,
        user_dto: Mock
) -> None:
    user_dto.get_data.return_value = ("test", "test", 2000, "user")
    with pytest.raises(TypeError) as actual:
        update_user_controller.update("0", {
            "first_name": "test",
            "last_name": "test",
            "birth_year": 2000,
            "group": "user"
        })
    assert str(actual.value) == "One of arguments was of invalid type."


def test_update_user_raises_value_error_on_id(
        update_user_controller: UpdateUserController,
        users_repository: Mock,
        user_dto: Mock
) -> None:
    user_dto.get_data.return_value = ("test", "test", 2000, "user")
    users_repository.get_users.return_value = [
        {
            'id': 0,
            'first_name': 'test',
            'last_name': 'test',
            'birth_year': 2000,
            'group': 'user'
        }
    ]
    with pytest.raises(ValueError) as actual:
        update_user_controller.update(1, {
            "first_name": "test",
            "last_name": "test",
            "birth_year": 2000,
            "group": "user"
        })
    assert str(actual.value) == "Invalid id."


def test_delete_user_raises_value_error(
        delete_user_controller: DeleteUserController,
        users_repository: UsersRepository
) -> None:
    users_repository.get_users.return_value = []
    with pytest.raises(ValueError) as actual:
        delete_user_controller.delete(0)
    assert str(actual.value) == "Invalid id."


def test_delete_user_passes_id(
        delete_user_controller: DeleteUserController,
        users_repository: UsersRepository
) -> None:
    users_repository.get_users.return_value = [{
        "id": 0,
        "first_name": "test",
        "last_name": "test",
        "birth_year": 2000,
        "group": "user"
    }]
    delete_user_controller.delete(0)
    users_repository.delete_user.assert_called_with(0)

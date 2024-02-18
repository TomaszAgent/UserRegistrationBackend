import pytest

from src.repositories import UsersRepository


@pytest.fixture()
def users_repository() -> UsersRepository:
    return UsersRepository()


def test_users_repository_exists() -> None:
    assert UsersRepository


def test_users_repository_returns_users(users_repository: UsersRepository) -> None:
    actual = users_repository.get_users()
    assert actual == users_repository._users


def test_users_repository_adds_users(users_repository: UsersRepository) -> None:
    users_repository.add_user('test', 'test', 2000, 'user')
    assert users_repository.get_users() == [
        {
            'id': 0,
            'first_name': 'test',
            'last_name': 'test',
            'birth_year': 2000,
            'group': 'user'
        }
    ]

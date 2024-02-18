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


def test_users_returns_user_by_id(users_repository: UsersRepository) -> None:
    users_repository.add_user('test', 'test', 2000, 'user')
    actual = users_repository.get_user(0)
    assert actual == {
            'id': 0,
            'first_name': 'test',
            'last_name': 'test',
            'birth_year': 2000,
            'group': 'user'
        }


def test_users_returns_none_for_bad_id(users_repository: UsersRepository) -> None:
    actual = users_repository.get_user(0)
    assert actual is None


def test_users_updates_users(users_repository: UsersRepository) -> None:
    users_repository.add_user('test', 'test', 2000, 'user')
    users_repository.update_user(0, first_name='test2')
    actual = users_repository.get_user(0)
    assert actual == {
            'id': 0,
            'first_name': 'test2',
            'last_name': 'test',
            'birth_year': 2000,
            'group': 'user'
        }


def test_update_users_raises_value_error(users_repository: UsersRepository) -> None:
    with pytest.raises(ValueError) as actual:
        users_repository.update_user(0, first_name='test2')
    assert "Id not in users." in str(actual.value)


def test_delete_user_deletes_user(users_repository: UsersRepository) -> None:
    users_repository.add_user('test', 'test', 2000, 'user')
    users_repository.delete_user(0)
    actual = users_repository.get_users()
    assert actual == []


def test_delete_user_raises_value_error(users_repository: UsersRepository) -> None:
    with pytest.raises(ValueError) as actual:
        users_repository.delete_user(0)
    assert "Id not in users." in str(actual.value)

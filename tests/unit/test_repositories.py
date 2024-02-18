from src.repositories import UsersRepository


def test_user_repository_exists() -> None:
    assert UsersRepository
    
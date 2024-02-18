import datetime

from src.repositories import UsersRepository


class CreateUserController:
    def __init__(self, repository: UsersRepository) -> None:
        self._repository = repository

    def create(self, first_name: str, last_name: str, birth_year: int, group: str):
        if type(first_name) != str or type(last_name) != str or type(birth_year) != int or type(group) != str:
            raise TypeError("One of arguments was of invalid type.")
        if birth_year > datetime.date.today().year:
            raise ValueError("The user can't be from the future.")
        if group not in ["user", "premium", "admin"]:
            raise ValueError("Invalid group.")

        self._repository.add_user(first_name, last_name, birth_year, group)

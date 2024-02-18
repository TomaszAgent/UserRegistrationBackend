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


class GetUsersController:
    def __init__(self, repository: UsersRepository) -> None:
        self._repository = repository

    def get(self, id: int | None = None):
        users = self._repository.get_users()

        if id is None:
            return users

        for user in users:
            if user["id"] == id:
                return user

        raise ValueError("Invalid id.")


class UpdateUserController:
    def __init__(self, repository: UsersRepository) -> None:
        self._repository = repository

    def update(self, id: int, user: dict[str, str | int | None]) -> None:
        for key in list(user.keys()):
            if key not in ["first_name", "last_name", "birth_year", "group"]:
                raise ValueError("Invalid user data.")
        for key in [key for key in ["first_name", "last_name", "birth_year", "group"] if key not in list(user.keys())]:
            user[key] = None
        first_name = user["first_name"]
        last_name = user["last_name"]
        birth_year = user["birth_year"]
        group = user["group"]
        id_type_check = type(id) == int
        names_type_check = type(first_name) == str and type(last_name) == str
        year_type_check = type(birth_year) == int
        group_type_check = type(group) == str
        if not id_type_check or not names_type_check or not year_type_check or not group_type_check:
            raise TypeError("One of arguments was of invalid type.")
        if birth_year > datetime.date.today().year:
            raise ValueError("The user can't be from the future.")
        if group not in ["user", "premium", "admin"]:
            raise ValueError("Invalid group.")

        users = self._repository.get_users()
        user_exists = False
        for user in users:
            if user["id"] == id:
                user_exists = True

        if not user_exists:
            raise ValueError("Invalid id.")

        self._repository.update_user(id, first_name, last_name, birth_year, group)


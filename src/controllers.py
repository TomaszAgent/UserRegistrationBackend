import datetime

from src.repositories import UsersRepository, users_repository

from src.data_transfer_objects import UserDTO, user_dto


class CreateUserController:
    def __init__(self, repository: UsersRepository, dto: UserDTO) -> None:
        self._repository = repository
        self._dto = dto

    def create(self, user: dict[str, str | int]):
        self._dto.add_data(user)
        data = self._dto.get_data()

        if None in data:
            raise ValueError("Missing one of the arguments.")

        first_name = data[0]
        last_name = data[1]
        birth_year = data[2]
        group = data[3]

        self._repository.add_user(first_name, last_name, birth_year, group)


class GetUsersController:
    def __init__(self, repository: UsersRepository) -> None:
        self._repository = repository

    def get(self, id: int | None = None):
        users = self._repository.get_users().copy()
        for user in users:
            current_year = datetime.date.today().year
            user["age"] = current_year - user["birth_year"]
            user.pop("birth_year")
        if id is None:
            return users

        for user in users:
            if user["id"] == id:
                return user

        raise ValueError("Invalid id.")


class UpdateUserController:
    def __init__(self, repository: UsersRepository, dto: UserDTO) -> None:
        self._repository = repository
        self._dto = dto

    def update(self, id: int, user: dict[str, str | int | None]) -> None:
        self._dto.add_data(user)
        data = self._dto.get_data()
        first_name = data[0]
        last_name = data[1]
        birth_year = data[2]
        group = data[3]

        if type(id) != int:
            raise TypeError("One of arguments was of invalid type.")

        users = self._repository.get_users()
        user_exists = False
        for user in users:
            if user["id"] == id:
                user_exists = True
                break

        if not user_exists:
            raise ValueError("Invalid id.")

        self._repository.update_user(id, first_name, last_name, birth_year, group)


class DeleteUserController:
    def __init__(self, repository: UsersRepository):
        self._repository = repository

    def delete(self, id: int):
        users = self._repository.get_users()
        found = False
        for user in users:
            if user["id"] == id:
                found = True
                break
        if not found:
            raise ValueError("Invalid id.")

        self._repository.delete_user(id)


create_users_controller = CreateUserController(users_repository, user_dto)
get_users_controller = GetUsersController(users_repository)
update_users_controller = UpdateUserController(users_repository, user_dto)
delete_users_controller = DeleteUserController(users_repository)

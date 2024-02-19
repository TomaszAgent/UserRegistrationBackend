class UsersRepository:
    def __init__(self) -> None:
        self._users: list[dict[str, str | int]] = []
        self._last_available_id = 0

    def add_user(self, first_name: str, last_name: str, birth_year: int, group: str) -> None:
        self._users.append(
            {
                'id': self._last_available_id,
                'first_name': first_name,
                'last_name': last_name,
                'birth_year': birth_year,
                'group': group
            }
        )
        self._last_available_id += 1

    def get_users(self) -> list[dict[str, str | int]]:
        return self._users

    def update_user(self, id: int, first_name, last_name, birth_year, group) -> None:
        user = None
        for potential_user in self._users:
            if potential_user["id"] == id:
                user = potential_user
                break

        if first_name is not None:
            user["first_name"] = first_name
        if last_name is not None:
            user["last_name"] = last_name
        if birth_year is not None:
            user["birth_year"] = birth_year
        if group is not None:
            user["group"] = group

    def delete_user(self, id: int) -> None:
        for user_index, user in enumerate(self._users):
            if user["id"] == id:
                self._users.pop(user_index)
                return


users_repository = UsersRepository()

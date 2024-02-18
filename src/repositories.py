class UsersRepository:
    def __init__(self):
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

    def get_user(self, id: int):
        for user in self._users:
            if user["id"] == id:
                return user
        return None

    def update_user(self, id: int, first_name=None, last_name=None, birth_year=None, group=None) -> None:
        user = None
        for potential_user in self._users:
            if potential_user["id"] == id:
                user = potential_user
                break

        if user is None:
            raise ValueError("Id not in users.")

        if first_name is not None:
            user["first_name"] = first_name
        if last_name is not None:
            user["last_name"] = last_name
        if birth_year is not None:
            user["birth_year"] = birth_year
        if group is not None:
            user["group"] = group
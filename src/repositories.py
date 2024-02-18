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

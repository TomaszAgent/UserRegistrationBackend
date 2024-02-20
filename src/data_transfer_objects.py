import datetime


class UserDTO:
    def __init__(self):
        self._first_name = None
        self._last_name = None
        self._birth_year = None
        self._group = None

    def add_data(self, user: dict[str, str | int | None]):
        for key in list(user.keys()):
            if key not in ["first_name", "last_name", "birth_year", "group"]:
                raise ValueError("Invalid user data.")
        for key in [key for key in ["first_name", "last_name", "birth_year", "group"] if key not in list(user.keys())]:
            user[key] = None
        first_name = user["first_name"]
        last_name = user["last_name"]
        birth_year = user["birth_year"]
        group = user["group"]
        first_name_type_check = type(first_name) == str or first_name is None
        last_name_type_check = type(last_name) == str or last_name is None
        names_type_check = first_name_type_check and last_name_type_check
        year_type_check = type(birth_year) == int or birth_year is None
        group_type_check = type(group) == str or group is None
        if not names_type_check or not year_type_check or not group_type_check:
            raise TypeError("One of arguments was of invalid type.")
        if birth_year is not None and birth_year > datetime.date.today().year:
            raise ValueError("The user can't be from the future.")
        if group is not None and group not in ["user", "premium", "admin"]:
            raise ValueError("Invalid group.")

        self._first_name = first_name
        self._last_name = last_name
        self._birth_year = birth_year
        self._group = group

    def get_data(self) -> tuple[str, str, int, str]:
        data = (self._first_name, self._last_name, self._birth_year, self._group)
        self._first_name = None
        self._last_name = None
        self._birth_year = None
        self._group = None
        return data


user_dto = UserDTO()

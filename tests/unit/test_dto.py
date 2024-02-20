import pytest

from src.data_transfer_objects import UserDTO


@pytest.fixture()
def user_dto() -> UserDTO:
    return UserDTO()


def test_user_dto_raises_value_error_on_invalid_user(user_dto: UserDTO) -> None:
    with pytest.raises(ValueError) as actual:
        user_dto.add_data({
            "first_name": "test",
            "last_name": "test",
            "birth_year": 2000,
            "group": "user",
            "test": "test"
        })
    assert str(actual.value) == "Invalid user data."


def test_user_dto_raises_type_error_on_first_name(user_dto: UserDTO) -> None:
    with pytest.raises(TypeError) as actual:
        user_dto.add_data({
            "first_name": 0,
            "last_name": "test",
            "birth_year": 2000,
            "group": "user",
        })
    assert str(actual.value) == "One of arguments was of invalid type."


def test_user_dto_raises_type_error_on_last_name(user_dto: UserDTO) -> None:
    with pytest.raises(TypeError) as actual:
        user_dto.add_data({
            "first_name": "test",
            "last_name": 0,
            "birth_year": 2000,
            "group": "user",
        })
    assert str(actual.value) == "One of arguments was of invalid type."


def test_user_dto_raises_type_error_on_birth_year(user_dto: UserDTO) -> None:
    with pytest.raises(TypeError) as actual:
        user_dto.add_data({
            "first_name": "test",
            "last_name": "test",
            "birth_year": "2000",
            "group": "user",
        })
    assert str(actual.value) == "One of arguments was of invalid type."


def test_user_dto_raises_type_error_on_group(user_dto: UserDTO) -> None:
    with pytest.raises(TypeError) as actual:
        user_dto.add_data({
            "first_name": "test",
            "last_name": "test",
            "birth_year": 2000,
            "group": 0,
        })
    assert str(actual.value) == "One of arguments was of invalid type."


def test_user_dto_raises_value_error_on_year(user_dto: UserDTO) -> None:
    with pytest.raises(ValueError) as actual:
        user_dto.add_data({
            "first_name": "test",
            "last_name": "test",
            "birth_year": 3000,
            "group": "user",
        })
    assert str(actual.value) == "The user can't be from the future."


def test_user_dto_raises_value_error_on_group(user_dto: UserDTO) -> None:
    with pytest.raises(ValueError) as actual:
        user_dto.add_data({
            "first_name": "test",
            "last_name": "test",
            "birth_year": 2000,
            "group": "person",
        })
    assert str(actual.value) == "Invalid group."


def test_user_dto_saves_correct_first_name(user_dto: UserDTO) -> None:
    user_dto.add_data({
        "first_name": "test",
        "last_name": "test",
        "birth_year": 2000,
        "group": "user",
    })
    actual = user_dto._first_name
    assert actual == "test"


def test_user_dto_saves_correct_last_name(user_dto: UserDTO) -> None:
    user_dto.add_data({
        "first_name": "test",
        "last_name": "test",
        "birth_year": 2000,
        "group": "user",
    })
    actual = user_dto._last_name
    assert actual == "test"


def test_user_dto_saves_correct_birth_year(user_dto: UserDTO) -> None:
    user_dto.add_data({
        "first_name": "test",
        "last_name": "test",
        "birth_year": 2000,
        "group": "user",
    })
    actual = user_dto._birth_year
    assert actual == 2000


def test_user_dto_saves_correct_group(user_dto: UserDTO) -> None:
    user_dto.add_data({
        "first_name": "test",
        "last_name": "test",
        "birth_year": 2000,
        "group": "user",
    })
    actual = user_dto._group
    assert actual == "user"


def test_user_dto_returns_correct_data(user_dto: UserDTO) -> None:
    user_dto.add_data({
        "first_name": "test",
        "last_name": "test",
        "birth_year": 2000,
        "group": "user",
    })
    actual = user_dto.get_data()
    assert actual == ("test", "test", 2000, "user")

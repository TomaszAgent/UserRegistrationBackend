from src.main import ping


def test_ping_exists() -> None:
    assert ping


def test_ping_returns_right_value() -> None:
    actual = ping()
    assert actual == "pong"

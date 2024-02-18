from src.main import ping

def test_ping() -> None:
    actual = ping()
    assert actual == "pong"

from flask import Flask

from src.controllers import CreateUserController, GetUsersController, UpdateUserController, DeleteUserController

app = Flask(__name__)


@app.get('/ping')
def ping() -> str:
    return 'pong'


if __name__ == "__main__":
    app.run("localhost", 8080)

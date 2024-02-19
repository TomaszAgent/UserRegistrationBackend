from flask import Flask, Response
import json

from src.controllers import create_users_controller, get_users_controller, update_users_controller, delete_users_controller
from src.STATUS_CODES import OK, BAD_REQUEST

app = Flask(__name__)


@app.get('/ping')
def ping() -> str:
    return 'pong'


@app.get('/users')
def get_users() -> Response:
    users = get_users_controller.get()
    return Response(response=json.dumps(users), status=OK, mimetype='application/json')


@app.get('/users/<id>')
def get_user(id: int) -> Response:
    try:
        user = get_users_controller.get(id=int(id))
        return Response(response=json.dumps(user), status=OK, mimetype='application/json')
    except ValueError:
        return Response(status=BAD_REQUEST)


if __name__ == "__main__":
    app.run("localhost", 8080)

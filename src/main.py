from flask import Flask

app = Flask(__name__)


@app.get('/ping')
def ping() -> str:
    return 'pong'


if __name__ == "__main__":
    app.run("localhost", 8080)

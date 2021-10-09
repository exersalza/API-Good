from threading import Thread

from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return ''


def run():
    app.run(host='0.0.0.0', port=8080)


def start_server():
    server = Thread(target=run)
    server.start()

import json

from flask import Flask, request
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.server import WSGIServer
from gevent.pywsgi import WSGIServer
from geventwebsocket.websocket import WebSocket

app = Flask(__name__)

clientList = []


@app.route("/")
def func():
    client_socket = request.environ.get("wsgi.websocket")
    if not client_socket:
        return "error"
    clientList.append(client_socket)
    while 1:
        for i in clientList:
            try:
                i.send(json.dumps("11111"))
            except Exception as e:
                continue


if __name__ == "__main__":
    http_server = WSGIServer(("127.0.0.1", 8888), application=app, handler_class=WebSocketHandler)
    http_server.serve_forever()

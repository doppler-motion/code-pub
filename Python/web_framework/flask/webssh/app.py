import time

from flask import Flask, request, render_template
from geventwebsocket.websocket import WebSocket, WebSocketError
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from channels.generic.websocket import WebsocketConsumer
import paramiko
import threading
from loguru import logger

import json

app = Flask(__name__)


@app.route('/api/v1/webssh')
def ws():
    try:
        this_socket = request.environ.get("wsgi.websocket")
        if not this_socket:
            return "请以WEBSOCKET方式连接"

        sshclient = paramiko.SSHClient()
        sshclient.load_system_host_keys()
        sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshclient.connect(HOSTS, PORT, USERNAME, PASSWORD)

        chan = sshclient.invoke_shell(term='xterm')
        chan.exit_status_ready()
        chan.settimeout(0)
        t1 = MyThread(chan, this_socket, sshclient)
        t1.setDaemon(True)
        t1.start()
        logger.info(dir(this_socket))

        while True:
            try:
                logger.info(this_socket.closed)
                if this_socket.closed:
                    break

                user_msg = this_socket.receive()
                chan.send(user_msg)

            except WebSocketError as e:

                logger.exception("receive or send failed")
        logger.info("close")
    except Exception as e:
        logger.error(f"======================== : [{str(e)}]")

    return ""


# 配置服务器信息
HOSTS = ""  # IP
PORT = 22  # 端口
USERNAME = ""  # 用户名
PASSWORD = ""  # 密码


class MyThread(threading.Thread):
    def __init__(self, chan, ws, sshclient):
        threading.Thread.__init__(self)
        self.chan = chan
        self.ws = ws
        self.sshclient = sshclient

    def run(self):
        while not self.chan.exit_status_ready():
            time.sleep(0.1)
            try:
                data = self.chan.recv(32 * 1024)
                self.ws.send(data.decode("utf-8", errors="ignore"))
            except Exception as ex:
                # print(str(ex))
                pass
        logger.info("close")
        self.sshclient.close()
        return False


if __name__ == '__main__':
    http_serve = WSGIServer(("0.0.0.0", 9000), app, handler_class=WebSocketHandler)
    http_serve.serve_forever()

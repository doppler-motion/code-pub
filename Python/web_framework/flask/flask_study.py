import time
import json
import os, sys

from flask import Flask, jsonify, request, abort
from flask_apscheduler import APScheduler
from flask_sqlalchemy import SQLAlchemy
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.jobstores.redis import RedisJobStore

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common.common_log import Log

logger = Log(__name__).get_logger()

# MYSQL
USERNAME = "root"
PASSWORD = "123456qa!"
IP = "127.0.0.1"
PORT = 3306
DB = "flaskdb"

# redis
REDIS_CONFIG = {
    "host": "127.0.0.1",
    "port": 6379,
    "db": 2,
    # "username": "",
    "password": "123456qa!",
    "jobs_key": "scheduler_task",
    "run_times_key": "task_req"

}

app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://{username}:{password}@{ip}:{port}/{db}?charset=utf8".format(
#     username=USERNAME,
#     password=PASSWORD,
#     ip=IP,
#     port=PORT,
#     db=DB)
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)


class Config(object):
    # 存储定时任务
    SCHEDULER_JOBSTORES = {
        "mysql": SQLAlchemyJobStore(url="mysql+pymysql://{username}:{password}@{ip}:{port}/{db}?charset=utf8".format(
            username=USERNAME,
            password=PASSWORD,
            ip=IP,
            port=PORT,
            db=DB)),
        "redis": RedisJobStore(**REDIS_CONFIG),
        "default": RedisJobStore(**REDIS_CONFIG)
    }

    # 设置定时任务的执行器(默认是最大执行数量为10的线程池)
    SCHEDULER_EXECUTORS = {
        "default": {
            "type": "threadpool",
            "max_workers": 10
        }
    }
    # 设置时区
    SCHEDULER_TIMEZONE = "Asia/Shanghai"
    # 开启api功能
    SCHEDULER_API_ENABLED = True
    # api前缀
    SCHEDULER_API_PREFIX = "/scheduler"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class User(db.Model):
    idx = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, default=18)

    def __init__(self, idx, name, age):
        self.idx = idx
        self.name = name
        self.age = age

    def __repr__(self):
        return "<User %s>" % self.name

    def __str__(self):
        return "<User %s>" % self.name


def work(num):
    start_time = int(time.time())
    time.sleep(num)
    end_time = int(time.time())
    logger.info(f"task end, cost time {end_time - start_time} second!")


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/add_post", methods=["POST"])
def add_post():
    logger.info(request.headers)
    logger.info(type(request.json))
    logger.info(request.json)
    result = request.json
    return str(result)


@app.route("/add_user", methods=["POST"])
def add_user():
    logger.info(request.headers)
    logger.info(type(request.json))
    logger.info(request.json)
    result = request.json

    u1 = User(124, "李四", 99)
    db.session.add(u1)
    db.session.commit()

    return str(result)


# @app.route("/post/<int:post_id>")
# def hello_world(post_id):
#     return "Post %d!" % post_id


if __name__ == "__main__":
    # db.init_app(app)
    # db.create_all()

    app.config.from_object(Config)

    sched = APScheduler()
    sched.init_app(app)
    sched.start()

    host, port = "127.0.0.1", 5005
    logger.info(f"listening to {host}:{port}")
    app.run(host=host, port=port, debug=False)

from flask import Blueprint

# 定义蓝图
tag = Blueprint("tag", __name__)


@tag.route("/")
def index():
    return 'ok'


@tag.route("/add/")
def add():
    return "tag add"

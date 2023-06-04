import os, sys
import json

from loguru import logger
from flask import jsonify
from flask import Blueprint

sys.path.append(os.path.dirname(__file__))
from app.models import db, User

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/", methods=["POST", "GET"])
def index():
    js = {
        "message": 1,
        "error": 0,
        "data": [{"pos": 1}, {"pos": 2}]
    }
    return jsonify(js)


@admin_bp.route("/<string:name>/<int:pwd>")
def login(name, pwd):
    user = User(name, pwd)
    db.session.add(user)
    db.session.commit()
    return "创建用户 %s, 密码 %d" % (name, pwd)


@admin_bp.route("/login/<string:name>")
def loginByName(name):
    user = User.query.filter(User.name == name).first()
    if user is None or user.name.strip == "":
        return "用户不存在"
    else:
        return "%s 用户登陆" % user.name


@admin_bp.route("/checkout")
def checkAll():
    user = User.query.all()
    logger.info(user)
    return json.dumps({"data": [{"name": u.name, "pwd": u.thtust} for u in user]}, indent=4)


@admin_bp.route('/update/<string:name>/<string:pwd>')
def update(name, pwd):
    user = User.query.filter(User.name == name).first()
    if user is not None:
        user.thrust = pwd
        db.session.commit()
        return '修改 用户 %s ,密码为：%s' % (name, pwd)
    else:
        return '用户不存在'


@admin_bp.route('/delete/<string:name>/<string:pwd>')
def delete(name, pwd):
    user = User.query.filter(User.name == name, User.thrust == pwd).first()
    if user is not None:
        db.session.delete(user)
        db.session.commit()
        return '删除 用户 %s ,密码为：%s' % (name, pwd)
    else:
        return '用户不存在，或密码不正确'




from flask import Blueprint

tag = Blueprint("tag", __name__)


@tag.route("/")
def index():
    return 'ok'


@tag.route("/add/")
def add():
    return "tag add"

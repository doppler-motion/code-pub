from flask import Blueprint

movie = Blueprint("movie", __name__)


@movie.route("/")
def index():
    return 'ok'


@movie.route("/add/")
def add():
    return "movie add"

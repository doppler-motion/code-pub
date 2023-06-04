from flask import Flask

from admin.admin import admin_bp
from app.models import db

app = Flask(__name__)
app.config.from_object("config")
app.register_blueprint(admin_bp)

# 应用上下文
with app.app_context():
    db.init_app(app)
    db.create_all()


@app.route("/")
def hello_world():
    return "Hello Flask!"


if __name__ == "__main__":
    app.debug = app.config["DEBUG"]
    host, port = "127.0.0.1", 5008
    app.run(host=host, port=port)

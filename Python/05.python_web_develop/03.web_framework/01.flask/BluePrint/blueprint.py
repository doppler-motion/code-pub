from flask import Flask
from app.tag.view import tag as tag_bp
from app.movie.view import movie as movie_bp

if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(tag_bp, url_prefix="/tag/")  # 注册蓝图
    app.register_blueprint(movie_bp, url_prefix="/movie/")
    host, port = "127.0.0.1", 5007
    app.run(host=host, port=port, debug=False)
   
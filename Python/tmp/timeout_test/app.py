import time

from flask import Flask, jsonify, request, abort

app = Flask(__name__)


@app.route("/add_post", methods=["POST"])
def add_post():
    print(request.headers)
    print(type(request.json))
    print(request.json)

    time.sleep(30)
    result = request.json
    return str(result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)


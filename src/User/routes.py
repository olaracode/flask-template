from flask import Blueprint


user = Blueprint("user", __name__)


@user.route("/crear", methods=["POST", "GET"])
def hello_world():
    return {"hello": "world"}

@user.route("/borrar", methods=["POST", "GET"])
def goodbye_world():
    return {"hello": "world"}
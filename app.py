from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)


@app.route("/reset", methods=["POST"])
def reset_password():

    username = request.json.get("username")
    email = request.json.get("email")

    return jsonify({"reset_link": f"www.resetpassword/{username}/{email}"})


@app.route("/unlock", methods=["POST"])
def unlock_account():

    username = request.json.get("username")
    email = request.json.get("email")
    status_code = HTTPStatus.OK.value
    response = {
        "message": "Unlock Success",
        "status_code": status_code,
        "data": {"User": username, "email": email},
    }

    return response


@app.route("/register", methods=["POST"])
def register():

    full_name = request.json.get("full_name")
    username = request.json.get("username")
    email = request.json.get("email")
    password = request.json.get("password")
    status_code = HTTPStatus.OK.value
    response = {
        "message": "Registration Successful",
        "status_code": status_code,
        "data": {"User": username, "email": email},
    }

    return response


@app.route("/login", methods=["POST"])
def login():

    email = request.json.get("email")
    password = request.json.get("password")
    status_code = HTTPStatus.OK.value
    response = {
        "message": "login Successful",
        "status_code": status_code,
        "data": {"email": email},
    }

    return response


if __name__ == "__main__":
    app.run(debug=True, port=5003)

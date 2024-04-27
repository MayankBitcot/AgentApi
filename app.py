from flask import Flask,jsonify,request
from http import HTTPStatus

app = Flask(__name__)


@app.route('/reset', methods=["POST"])
def reset_password():
    username = request.json.get("username")
    email = request.json.get("email")
    return jsonify({"reset_link": f"www.resetpassword/{username}/{email}"})


@app.route('/unlock', methods=["POST"])
def unlock_account():  
    username = request.json.get("username")
    email = request.json.get("email")
    status_code = HTTPStatus.OK.value
    response = {'message': 'Success', "status_code":status_code,'data': {'User': username, "email": email}}

    return response



if __name__ == '__main__':
    app.run(debug=True)
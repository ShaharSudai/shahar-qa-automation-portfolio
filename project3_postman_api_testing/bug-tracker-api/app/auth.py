from flask import Blueprint, jsonify, request
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

auth_bp = Blueprint("auth", __name__)


users = {
    "admin": {"password": "1234", "role": "admin"},
    "tester": {"password": "1234", "role": "user"}
}


@auth_bp.post("/login")
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username not in users or users[username]["password"] != password:
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity={"user": username, "role": users[username]["role"]})
    return jsonify(access_token=access_token), 200

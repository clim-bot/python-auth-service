from flask import jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from ..utils.jwt_utils import encode_auth_token

# Dummy user database
users_db = {}

def register_user(data):
    username = data.get('username')
    password = data.get('password')
    if username in users_db:
        return jsonify({"message": "User already exists"}), 400
    hashed_password = generate_password_hash(password)
    users_db[username] = hashed_password
    return jsonify({"message": "User registered successfully"}), 201

def login_user(data):
    username = data.get('username')
    password = data.get('password')
    user_password = users_db.get(username)
    if user_password and check_password_hash(user_password, password):
        token = encode_auth_token(username)
        return jsonify({"token": token}), 200
    return jsonify({"message": "Invalid username or password"}), 401

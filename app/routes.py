from flask import Blueprint, jsonify, request
from .services.auth_service import login_user, register_user

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    return register_user(data)

@auth_blueprint.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    return login_user(data)

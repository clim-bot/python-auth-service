import jwt
from datetime import datetime, timedelta
from flask import current_app

def encode_auth_token(username):
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
            'sub': username
        }
        return jwt.encode(
            payload,
            current_app.config.get('JWT_SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return None

def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, current_app.config.get('JWT_SECRET_KEY'), algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Token expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

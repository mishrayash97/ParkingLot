from flask import Flask, jsonify, request
import jwt
from data_access import JWT_SECRET

# Decorator for JWT authentication.
def authenticate_token(func):
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'message': 'Authorization header is missing.'}), 401
        token = auth_header.split(' ')[1]
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms='HS256')
            print("payload decoded:")
            print(payload)
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired.'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token.'}), 401
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

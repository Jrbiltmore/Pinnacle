
import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'your-secret-key'

def authenticate_user(username, password):
    # Replace with real user authentication logic
    if username == 'admin' and password == 'password':
        return generate_token(username)
    return None

def generate_token(username):
    payload = {
        'username': username,
        'exp': datetime.utcnow() + timedelta(days=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['username']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def authenticate_request(token):
    username = decode_token(token)
    if username:
        return True
    return False

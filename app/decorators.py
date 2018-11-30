from functools import wraps
import json
from app.models import User
from app.errors import unauth, bad_json
from flask import request

def require_key(view):
    @wraps(view)
    def decorated_function(*args, **kwargs):
        try:
            data = json.loads(request.data.decode('utf-8'))
        except json.JSONDecodeError:
            return bad_json()
        if 'key' not in data:
            return unauth('No `key` provided in request')
        user = User.query.filter_by(key=data['key']).first()
        if not user:
            return unauth('Bad `key` provided')
        return view(*args, **kwargs, user=user)
    return decorated_function


# app/decorator.py
from flask import session, redirect, url_for
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("main.login"))
        return f(*args, **kwargs)
    return decorated_function




from flask import make_response, session, redirect, url_for

def nocache(view):
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, private, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response
    return no_cache



# def logout_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if "user_id" in session:
#             return redirect(url_for("main.dashboard"))
#         return f(*args, **kwargs)
#     return decorated_function

# def admin_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if session.get("role") != "admin":
#             return redirect(url_for("main.dashboard"))
#         return f(*args, **kwargs)
#     return decorated_function

# def guest_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if session.get("role") == "guest":
#             return redirect(url_for("main.dashboard"))
#         return f(*args, **kwargs)
#     return decorated_function

# def api_key_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if "api_key" not in session:

#             return redirect(url_for("main.pricing"))
#         return f(*args, **kwargs)
#     return decorated_function       
from functools import wraps

from flask import session, flash, redirect, url_for, request
from src.app import  app


def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'email' not in session.keys() or session['email'] is None:
            flash(u'You need to be signed in for this page.')
            return redirect(url_for('users.login_user', next=request.path))
        return f(*args, **kwargs)

    return decorated_function

def requiers_admin_permissions(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'email' not in session.keys() or session['email'] is None:
            flash(u'You need to be signed in for this page.')
            return redirect(url_for('users.login_user', next=request.path))
        if session['email'] not in app.config['ADMINS']:
            return redirect(url_for('users.login_user', message="You need to be an admin to access that"))
        return f(*args, **kwargs)

    return decorated_function


# def requires_login(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         print("Hi")
#         return f(*args, **kwargs)  # func(...) args: func(5,6) kwargs: func(x=5,y=6)
#
#     return decorated_function
#
#
# @requires_login
# def my_function(x, y):
#     return x + y
#
#
# print(my_function(5,6))

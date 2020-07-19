"""
This module creates a wrapped function decorator that is
called to ascertain if the user is currently logged in.
"""

from functools import wraps
from flask import redirect, session

class Login:
    def logged_in(f):
        """
            Checks for the log in status of the user.
        """
        @wraps(f)
        def decorated(*args, **kwargs):
            if "username" not in session:
                return redirect(url_for("index"))
            return f(*args, **kwargs)
        return decorated

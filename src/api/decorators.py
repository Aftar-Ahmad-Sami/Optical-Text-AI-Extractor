from functools import wraps
from flask import request, abort
from config.settings import API_KEY

def require_api_key(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        """
        Decorator function to require API key for accessing a view function.

        Args:
            view_function (function): The view function to be decorated.

        Returns:
            The decorated view function.

        Raises:
            HTTPException: If the API key is missing or incorrect.
        """
        print(API_KEY)
        if request.headers.get('x-api-key') != API_KEY:
            abort(401, description=API_KEY)
        return view_function(*args, **kwargs)
    return decorated_function
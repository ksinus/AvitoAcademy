from typing import Callable
from functools import wraps
from random import randint


def log(pattern: str) -> Callable:
    """Decorator for adding integer number to a text pattern"""

    def inner(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            print(pattern.replace("{}", f"{randint(1, 100)}"))
            return func(*args, **kwargs)

        return wrap

    return inner

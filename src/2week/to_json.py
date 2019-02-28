import functools
from json import dumps


def to_json(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return dumps(func(*args, **kwargs))
    return wrapper

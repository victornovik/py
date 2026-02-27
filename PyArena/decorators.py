from functools import wraps


def upper(func):
    def wrapper():
        return func().upper()

    return wrapper


def reverse(func):
    def wrapper():
        return func()[::-1]

    return wrapper


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'Called {func.__name__}() with {args}, {kwargs} and returned {res!r}')
        return res
    return wrapper


@trace
@upper
@reverse
def get_string():
    return "Hi world"


print(get_string())


@trace
def reverse_str(s: str) -> str:
    return s[::-1]


print(reverse_str("How are you?"))

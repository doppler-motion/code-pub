from functools import wraps


# def welcome(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         print("welcome")
#         result = fn(*args, **kwargs)
#         return result
#
#     return wrapper

def welcome(name):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"welcome {name}")
            result = fn(*args, **kwargs)
            return result

        return wrapper
    return decorator


@welcome("Tom")
def my_fun(msg: str):
    print(f"hello {msg}")


my_fun(msg="Jack")
print(my_fun)

from time import time
from functools import wraps

def runtime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        begin:float = time()
        func(*args, **kwargs)
        end:float = time()
        print(f'{func.__name__} run time is {end - begin}s')
    return wrapper
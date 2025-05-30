from time import time
from functools import wraps

def runtime(func): # type: ignore
    @wraps(func) # type: ignore
    def wrapper(*args, **kwargs): # type: ignore
        begin:float = time()
        func(*args, **kwargs)
        end:float = time()
        print(f'{func.__name__} run time is {end - begin}s') # type: ignore
    return wrapper # type: ignore
from time import perf_counter
from functools import wraps


def runTime(function):
    @wraps(function)
    def innerfunction(*args, **kwargs):
        """after process, it will print total execution time for function """
        now = perf_counter() 
        result = function(*args, **kwargs)
        end = perf_counter()
        diff = (end - now) * 1000
        print(f"Total time taken {diff:.4f} ms")
        return result
    return innerfunction
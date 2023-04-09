import functools


def d2(func):
    def wrapper(f):
        print("first")
        return func(f)
    return wrapper

def d(_func = None, *, msg = "aea"):
    def out(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(msg)
            
            print("2")
            return func(*args, **kwargs)
        return wrapper
    if not _func:
        return out
    return out(_func)
@d2
@d
def f(we):
    print(we)
    return "aea mongol"



print(f("we"))
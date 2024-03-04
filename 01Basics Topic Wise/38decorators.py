def repeat(times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(times=3)
def say_hello(name):
    print(f"Hello {name}!")

say_hello("World")
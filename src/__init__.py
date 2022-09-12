def basemethod(funcobj):
    def wrapper(*args, **kwargs):
        yield ; ...
        return funcobj(*args, **kwargs)
    return wrapper
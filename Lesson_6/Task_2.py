import functools
from functools import singledispatch

def trace(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return inner

@trace
def funtion(x):
    print('Вызвана функция "funtion"')
    return x

funtion(42)
print("".center(20, "-"))


@singledispatch
def func(arg, verbose=False):
    if verbose:
        print('some verbose here')
    print('arg is: ', arg)
    return ('arg is: '+ str(type(arg)))

@func.register(int)
def _(arg, verbose=False):
    if verbose:
        print('got int')
    print('arg is: ', arg)
    return ('arg is: '+ str(type(arg)))

@func.register(list)
def _(arg, verbose=False):
    if verbose:
        print('got list')
    print('arg is: ', arg)
    return ('arg is: '+ str(type(arg)))

print(func("rety"))
print(func(5))
print(func([5, 7]))



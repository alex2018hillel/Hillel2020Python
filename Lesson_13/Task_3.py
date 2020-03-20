import time
from contextlib import ContextDecorator

a = 5
b = 0

class my_context_decorator(ContextDecorator):

    def __init__(self, *suppressed):
        self.supressed = suppressed
        print('init')

    def __enter__(self):
        print('enter')
        self.t = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        t = time.time()
        print('Execution time: {}'.format(t - self.t))
        print('exit','\n')
        return (exc_type is not None and issubclass(exc_type, self.supressed))

my_list = [1, 2, 3, 4, 5]

@my_context_decorator()
def func(a, b):
    print('1')
    c = 0
    for i in range(100_000_000):
        try:
            c = a / b
        except ZeroDivisionError:
            c = 0

func(5, 0)

with my_context_decorator():
    c = 0
    for i in range(100_000_000):
        try:
            c = a / b
        except ZeroDivisionError:
            c = 0


@my_context_decorator(Exception)
def func2(a, b):
    print('2')
    c = 0
    for i in range(100_000_000):
        if b == 0:
            c = 0
        else:
            c = a / b
    return c

func2(5, 0)

with my_context_decorator(Exception):
    #c = 0
    for i in range(100_000_000):
        if b == 0:
            c = 0
        else:
            c = a / b





















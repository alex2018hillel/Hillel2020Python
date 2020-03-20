import time
from contextlib import ContextDecorator

class my_context_decorator(ContextDecorator):

    def __init__(self, *suppressed):
        self.supressed = suppressed
        print('init')

    def __enter__(self):
        print('enter')
        self.t = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        time.sleep(1)
        t = time.time()
        print('Execution time: {}'.format(t - self.t))
        print('exit','\n')
        return (exc_type is not None and issubclass(exc_type, self.supressed))

my_list = [1, 2, 3, 4, 5]

@my_context_decorator()
def func():
    print('1')
    try:
        my_list[6]
    except IndexError:
        print("That index is not in the list!")

func()

with my_context_decorator():
    try:
        my_list[6]
    except IndexError:
        pass

@my_context_decorator(Exception)
def func2():
    print('2')
    if my_list[6] is None:
        return
    else:
        return my_list[6]

func2()

with my_context_decorator(Exception):
    if my_list[6] is None:
        pass






















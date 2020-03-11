import time
import random
from contextlib import ContextDecorator

class my_context_decorator(ContextDecorator):

    def __init__(self):
        print('init')
        self.t = time.time()

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, *exc):
        t = time.time()
        print('Execution time: {}'.format(t - self.t))
        print('exit')
        return False

l = []
def l_list():
    for i in range(1000):
        l.append(random.randint(1,99))
    return l

@my_context_decorator()
def func(x, y, z):
    for i in range(1,x):
        s = sum(l_list()[random.randint(1,y):random.randint(y,z)])
        print(s)

func(500, 50, 100)

with my_context_decorator():
    for i in range(1,1000):
        s = sum(l_list()[random.randint(1,50):random.randint(50,100)])
        print(s)
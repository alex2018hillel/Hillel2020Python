import time
import random

class my_context_decorator:

    def __init__(self):
        print('init')


    def __enter__(self):
        print('enter')
        self.t = time.time()
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

with my_context_decorator():
    for i in range(1,1000):
        s = sum(l_list()[random.randint(1,50):random.randint(50,100)])
        print(s)
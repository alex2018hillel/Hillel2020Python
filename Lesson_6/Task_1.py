import time
import random

def timer(f):
    def tmp(*args):
        t = time.time()
        res = f(*args)
        print('Execution time: {}'.format(time.time() - t))
        return res
    return tmp

@timer
def func(x, y, z):
    for i in range(1,x):
        s = sum(l_list()[random.randint(1,y):random.randint(y,z)])
        print(s)

l = []
def l_list():
    for i in range(1000):
        l.append(random.randint(1,99))
    print(l)
    return l

func(1000, 50, 100)

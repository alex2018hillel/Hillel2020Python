import time
import random

def memoize(f):
    cache = {}

    def decorate(*args):
        print(args)
        if args not in cache:
            print('args not in cache')
            cache[args] = f(*args)
        return cache[args]
    return decorate

def timer(f):
    def tmp(*args):
        t = time.time()
        res = f(*args)
        print('Execution time: {}'.format(time.time() - t))
        return res
    return tmp

@timer
@memoize
def long_story(x, y):
    l = []
    # for i in range(y):
    #     l.append(x)
    for i in range(x):
        l.append(random.randint(1,99))
    for i in range(1,y):
        s = sum(l[random.randint(1,50):random.randint(50,100)])
        print(s)

long_story(1_000_000, 100)
long_story(1_000_000, 100)

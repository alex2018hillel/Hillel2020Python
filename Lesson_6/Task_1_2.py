import time
import random

def tracer(func):
    calls = 0
    def wrapper(*args):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args)
    return wrapper

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

@tracer
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
    return s

print(long_story(1_000_000, 100))
print(long_story(1_000_000, 101))
print(long_story(1_000_000, 101))

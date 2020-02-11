import itertools
import random
import time

def summa2():
    t = time.time()
    length = 1200000
    for i in range(1,1000):
        list_1000000 = itertools.islice(list(range(length)), random.randint(1,20), random.randint(21,40))
        list_random_slice = list(list_1000000)
        print(list_random_slice)
        print(sum(list_random_slice))
    return (time.time()-t)

print(summa2(), "ceк. - время обработки")

"""Больше 1000 'побоялся' ставить"""








l = []

def l_list():
    for i in range(1000000):
        l.append(random.randint(1,99))
    print(l)
    return l

def summa():

    for i in range(1,100):
        s = sum(l_list()[random.randint(1,50):random.randint(51,100)])
        print(s)
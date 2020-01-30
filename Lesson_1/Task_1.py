import numpy as np
from collections import OrderedDict

def max_element(l):
    max = sorted(l, reverse=True)[0]
    return (max,[i for i,maximum in enumerate(l) if maximum==max])

def min_element(l):
    min = sorted(l)[0:1][0]
    return (min,[i for i,minimum in enumerate(l) if minimum==min])

def three_element(l):
    frequency = dict(zip(*np.unique(l, return_counts=True)))
    three_el = sorted(frequency, key=frequency.get, reverse=True)[0:3]
    return three_el

def unique_list_unsorted(l):
    return list(set(l))

def unique_list_sorted(l):
    return list(OrderedDict.fromkeys(l))

l = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]

print("---------------1.1--------------------")
print("maximum ", max_element(l)[0]," - index ",max_element(l)[1])
print("minimum ", min_element(l)[0]," - index ",min_element(l)[1])
print("---------------1.2--------------------")
print(three_element(l))
print("---------------1.31-------------------")
print(unique_list_unsorted(l))
print("---------------1.32-------------------")
print(unique_list_sorted(l))

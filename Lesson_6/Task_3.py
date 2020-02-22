from functools import lru_cache
"""
Вычисление числа Фибоначчи
"""
@lru_cache(maxsize=4)
def fib(n):
    if n <= 2:
        return n
    return fib(n - 1) + fib(n - 2)

print([fib(i) for i in range(100)])
print(fib.cache_info())

"""
Вычисление факториала
"""
@lru_cache(maxsize=None)
def fact(n):
    res = 1
    for i in range(1, n):
        res *= i
    return res

print(fact(100))
print(fact.cache_info())


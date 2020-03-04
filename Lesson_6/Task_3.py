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

# def get_pep(num):
#     'Retrieve text of a Python Enhancement Proposal'
#     # Same code as an in official example
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
print(fib(50))

def analyze_peps():
    cached_fib = lru_cache(maxsize=32)(fib)
    all, type = analyze(cached_fib(0))
    words1 = get_words_in_peps(cached_fib, all)
    words2 = get_words_in_informational(cached_fib,
                                        type["Informational"])
    # do_something(words1, words2)

# def get_pep(num):
#     'Retrieve text of a Python Enhancement Proposal'
#     resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
#     try:
#         with urllib.request.urlopen(resource) as s:
#             return s.read()
#         except urllib.error.HTTPError:
#         return 'Not Found'
#

analyze_peps
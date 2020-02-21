

# if base.count(200) < try_count:
#     return 'Error'
# else:
#     return 'OK'
# def decoration(calls):
#
#     print('decorated func arg: %s' % calls)
#     return func(calls + 1)
#
# return decoration
#nonlocal calls
# while calls <= try_count:
#     print(calls)
#     #calls += 1
#     return func(*args)
###calls += 1
# def count(*arg):
#     nonlocal calls
#     while calls <= try_count:
#         try:
#             return func(*arg)
#         except:
#             calls += 1
# #func(*args)
#     # print(calls)
#     # if calls <= try_count:
#     #     print("calls <= try_count")
#     # #return func(*args)
#     #     return func(*args)
#     # else:
#     #     print("calls > try_count")
#     #     return None
#     return func(*arg)
# return count

#request = func(*args)

def skip(n):
    attempts = 0
    def decorator(func):
        def wrapper(*args, **kwargs):
            nonlocal attempts
            attempts += 1
            if attempts <= n:
                print("Function now works")
                return func(*args, **kwargs)
            else:
                print("Function has been waiting")
                return None
        return wrapper
    return decorator

@skip(3)
def inc(a):
    return a + 1

print(inc(1))
print(inc(1))
print(inc(1))
print(inc(1))
print(inc(1))
print(inc(1))
print(inc(1))
print(inc(1))
print(inc(1))
print(inc(1))

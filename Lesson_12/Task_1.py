def my_contextdecorator(func):
    def inner(*args):
        try:
            func(*args)
        except:
            pass
    return inner

@my_contextdecorator
def function(a):
    print("Start")
    return a/0

function(5)
print("function - подавлена")

class My_context_decorator(object):
    def __init__(self):
        pass
    def __enter__(self):
        pass
    def __exit__(self, type, value, traceback):
        print("Исключение было обработано")
        return True

with My_context_decorator():
    print(1 / 0)
print("ContextDecorator - подавлен")

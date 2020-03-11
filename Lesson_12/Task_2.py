from contextlib import (ContextDecorator)

class my_context_decorator(ContextDecorator):
    def __init__(self, *suppressed):
        self.supressed = suppressed

    def __enter__(self):
        pass

    def __exit__(
            self, exc_type, exc_val, exc_tb):
        return (exc_type is not None and issubclass(exc_type, self.supressed))

@my_context_decorator(FileNotFoundError, ZeroDivisionError)
def function(a):
    return a/0

function(5)
print("function - подавлена")

with my_context_decorator(FileNotFoundError, ZeroDivisionError):
    print(1 / 0)
print("ContextDecorator - подавлен")

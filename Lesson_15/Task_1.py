import math

class my_staticmethod(object):
    def __init__(self, method):
        print("__init__")
        self.method = method
    def __get__(self, instance, owner):
        print("__get__")
        return self.method

class my_classMethod(object):
    def __init__(self, method):
        print("__init__")
        self.method = method
    def __get__(self, instance, owner):
        if owner is None:
            owner = type(instance)
        def new_func(*args):
            print("__get__")
            return self.method(owner, *args)
        return new_func

class SomeClass:
    @my_staticmethod
    def do_pi():
        print(math.pi)
        print("do_pi!")

    @my_classMethod
    def do_2pi(self,a):
        print(a*math.pi)
        print("do_2pi!")

SomeClass.do_pi()
print('='*20)
SomeClass.do_2pi(2)


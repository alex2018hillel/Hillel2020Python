class Singleton(object):
    def my_Singleton(to_decorate):
        def wrapper(cls, ):
            if not hasattr(cls, 'instance'):
                cls.instance = super(Singleton, cls).__new__(cls)
            return cls.instance
            to_decorate(cls)
        return wrapper

    @my_Singleton
    def __new__(cls):
        print("")

s = Singleton()
print("Object created", s)
s1 = Singleton()
print("Object created", s1)
s2 = Singleton()
print("Object created", s2)



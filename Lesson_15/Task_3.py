import re

class EmailDescriptor:
    def __get__(self, instance, owner):
        print('get: ', instance, owner)
        return owner

    def __set__(self, instance, value):
        print('set: ', instance, value)
        reg = "^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$"
        if re.match(reg, value):
            print("email is valid")
            return value
        else:
            print("email is invalid")
            raise Exception('email is invalid')

class MyClass:
    reg = EmailDescriptor()
    email = EmailDescriptor()

my_class = MyClass()

my_class.email = "validemail@gmail.com"
print(MyClass.email)

my_class.email = "novalidemail"
print(MyClass.email)

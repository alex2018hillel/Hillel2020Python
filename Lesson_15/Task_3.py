import re

class EmailDescriptor:
    def __get__(self, instance, owner):
        print('get: ', instance, owner)
        reg = "^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$"
        if re.match(reg, self.value):
            print("email is valid")
            return self.value
        else:
            print("email is invalid")
            raise Exception('email is invalid')

    def __set__(self, instance, value):
        print('set: ', instance, value)
        self.value = value

class MyClass:
    reg = EmailDescriptor()
    email = EmailDescriptor()

my_class = MyClass()

my_class.email = "validemail@gmail.com"
print(MyClass.email)

my_class.email = "novalidemail"
print(MyClass.email)

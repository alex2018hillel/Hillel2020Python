import re

def func(self, *args):
    print('func: ', self.__dict__)
    if re.match(self.reg, self.__dict__['email']):
        print("email is valid")
    else:
        print("email is invalid")
    return args

MyClass = type(
    'EmailValidate',
    (object,),
    {"reg" : "^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$", "validate": func, '__dict__': {"email" : "tropp-alex&2019@ukr.net"}}
)

email_validate = MyClass()
print("regex =  " , MyClass.reg)
print(email_validate.validate())

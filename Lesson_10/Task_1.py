import os

class Person(object):
    def __init__(self, age, name, salary=0):
        self.person_age = age
        self.person_name = name
        self.salary = salary

    def __str__(self):
        return  f'{self.__class__.__name__}{os.path.dirname(__file__)}({self.__dict__})'

class Manager (Person):
    def __init__(self):
        Person.__init__(self,1,Manager,-1)
        self.new_attr = 0
        super ()

p = Manager()
print(str(p), p.__dict__, sep='\n')
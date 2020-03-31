from random import random

class simple_revert:
    def __init__(self, l):
        self.counter = 1
        self.l = l

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > len(self.l):
            raise StopIteration
        else:
            self.counter += 1
            return self.l[(-self.counter+1)]

l = []
for i in range(10):
    l.append(round(100*random()))
    print(l[i])

sf = simple_revert(l)
print("Revert collection")
while True:
    try:
        item = next(sf)
        print(item)
    except StopIteration:
        break

#-----------------------------------------------------
def reverse_enum(t):
    for index in reversed(range(len(t))):
        yield index, t[index]

t = ('one', 'two', 'three')
for index, item in reverse_enum(t):
    print (index, item)
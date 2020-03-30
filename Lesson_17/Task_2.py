from random import random

class simple_range1:
    def __init__(self, num):
        self.current = 1
        self.number = num - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.number:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

l = []
for i in range(10):
    l.append(round(100*random()))
    print(l[i])

sf = simple_range1(l)
print("Revert list")
while True:
    try:
        item = next(sf)
        print(item)
    except StopIteration:
        break
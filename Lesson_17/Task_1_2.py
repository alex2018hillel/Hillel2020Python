class simple_range:
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

def simple_range_func(num):
    l = []
    srf = simple_range(num)
    while True:
        try:
            l.append(next(srf))
        except StopIteration:
            break
    return l

#---------------------------------------------------------
def simple_range1(last):
    for i in simple_range_func(last):
        yield i

sr = simple_range1(11)
print("simple_range for 1 arguments:")
for v in sr:
    print(v)

#---------------------------------------------------------

def simple_range2(first, last):
    print("simple_range for 2 arguments:")
    full_range = simple_range_func(last)
    for i in full_range:
        if i < first:
            pass
        else: yield i

sr = simple_range2(3, 11)
for v in sr:
    print(v)

#---------------------------------------------------------
def simple_range3(first, last, step):
    full_range = simple_range_func(last)
    i = 0
    while i<last:
        if i >= first:
            yield full_range[i-1]
            i += step
        else:
            i += 1

sr = simple_range3(2, 11, 3)
print("simple_range for 3 arguments:")
for v in sr:
    print(v)










def simple_range_3(last, first=1, step=1):
    while first<last:
        yield first
        first += step

sr1 = simple_range_3(11)
print("simple_range for 1 arguments:")
for v in sr1:
    print(v)

sr2 = simple_range_3(11, 2)
print("simple_range for 2 arguments:")
for v in sr2:
    print(v)

sr3 = simple_range_3(11, 2, 3)
print("simple_range for 3 arguments:")
for v in sr3:
    print(v)


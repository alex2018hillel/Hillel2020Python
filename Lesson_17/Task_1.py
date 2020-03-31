class simple_range_3:
    def __init__(self, num, start=0, step=1):

        self.current = start
        self.step = step
        self.number = num - 1

    def __iter__(self):
        return self  # return iterator

    def __next__(self):
        if self.current > self.number:
            raise StopIteration
        else:
            self.current += self.step
            return self.current - self.step

sf1 = simple_range_3(11)
print("simple_range for 1 argument:")
print("finish = {}".format(sf1.number))
while True:
    try:
        item = next(sf1)
        print(item)
    except StopIteration:
        break

sf2 = simple_range_3(11, 2)
print("simple_range for 2 argument:")
print("start = {}, finish = {}".format(sf2.current, sf2.number))
while True:
    try:
        item = next(sf2)
        print(item)
    except StopIteration:
        break

sf3 = simple_range_3(11, 2, 3)
print("simple_range for 3 arguments:")
print("start = {}, finish = {}, step = {}".format(sf3.current, sf3.number, sf3.step))
while True:
    try:
        item = next(sf3)
        print(item)
    except StopIteration:
        break

#--------------------------------------------------------------------
print("Python function range")
for i in range(2, 11, 3):
    print(i)











































# class simple_range1:
#     def __init__(self, num):
#         self.current = 1
#         self.number = num - 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current > self.number:
#             raise StopIteration
#         else:
#             self.current += 1
#             return self.current - 1
#
# sf = simple_range1(11)
# print("simple_range for 1 argument:")
# print("finish = {}".format(sf.number))
# while True:
#     try:
#         item = next(sf)
#         print(item)
#     except StopIteration:
#         break
#
# class simple_range2:
#     def __init__(self, start, num):
#         self.current = start
#         self.number = num - 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current > self.number:
#             raise StopIteration
#         else:
#             self.current += 1
#             return self.current - 1
#
# sf = simple_range2(3, 11)
# print("simple_range for 2 arguments:")
# print("start = {}, finish = {}".format(sf.current, sf.number))
# while True:
#     try:
#         item = next(sf)
#         print(item)
#     except StopIteration:
#         break
#
# class simple_range3:
#     def __init__(self, start, num, step):
#         self.current = start
#         self.step = step
#         self.number = num - 1
#
#     def __iter__(self):
#         return self  # return iterator
#
#     def __next__(self):
#         if self.current > self.number:
#             raise StopIteration
#         else:
#             self.current += self.step
#             return self.current - self.step
#
# sf = simple_range3(2, 11, 3)
# print("simple_range for 3 arguments:")
# print("start = {}, finish = {}, step = {}".format(sf.current, sf.number, sf.step))
# while True:
#     try:
#         item = next(sf)
#         print(item)
#     except StopIteration:
#         break
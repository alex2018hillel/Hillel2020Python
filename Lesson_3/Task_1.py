from collections import deque
#Sift size
n = 4
#List
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# left shift
for _ in range(n):
    d = deque(l)
    d.rotate(-n)
print(d)

# right shift
for _ in range(n):
    d = deque(l)
    d.rotate(n)
print(d)


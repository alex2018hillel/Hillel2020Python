l_1 = [-3, -2, -1, 0, 1, 2, 3, 4, 5]
l_2 = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 7]
l_3 = [-3]

def median(l):
    l_sort = sorted(l)
    length = len(l_sort)
    center = len(l_sort) / 2

    if length == 1:
        return l_sort[0]
    elif length % 2 == 0:
        return(l_sort[int(center) - 1] + l_sort[ int(center)]) / 2.0
    else:
        return l_sort[int(center)]

print(median(l_1))
print(median(l_2))
print(median(l_3))
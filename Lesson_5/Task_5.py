l = [[], [1, 2], [2, 3, [1, 2]], [1, 2, 3]]

l2 = []
for s in l:
    for column in s:
        if type(column) != type(l2):
            l2.append(column)
        else:
            for high in column:
                l2.append(high)
print(l2)
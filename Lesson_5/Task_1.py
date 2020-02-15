l = [2, 2, 4, 4, 4, 6, 6, 7, 9, 9, 9, 9, 5, 5, 1, 9, 9]

def max_list(l):
    k = 1
    j = 1
    n = 0
    for i in range(len(l)-1):
        if l[i+1] == l[i]:
            j += 1
        elif l[i+1] != l[i]:
            j = 1
        if j > n:
            n = j
            k = i

    print( l[k], n)
max_list(l)











# def max_list1(l):
#     result = {i: l.count(i) for i in l}
#     print(result)
#     num = (sorted(result.values(), reverse=True)[0])
#     print(result.values())
#     index_key = (sorted(result.keys(), reverse=True)[0])
#
#     print( index_key, num)
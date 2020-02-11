l = [2, 2, 4, 4, 4, 6, 6, 7, 9, 9, 9, 9, 5, 5, 1]

def max_list(l):
    result = {i: l.count(i) for i in l}
    print(result)
    num = (sorted(result.values(), reverse=True)[0])
    index_key = (sorted(result.keys(), reverse=True)[0])

    print( index_key, num)

max_list(l)
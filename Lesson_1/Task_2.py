a = {'a': 1, 'b': 4, 't': 67}
b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}

def common_keys(a,b):
    """Поиск одинаковых элементов в 2x словарях."""
    all_keys = set(list(a.keys()) + list(b.keys()))
    a_keys = list(a.keys())
    b_keys = list(b.keys())
    res = []
    for i in b_keys:
        if (i in a_keys):
            res.append(i)
    return res

def difference_keys(a,b):
    """Поиск ключей, которые есть только во 2м словаре, но нет в 1м."""
    a_keys = list(a.keys())
    b_keys = list(b.keys())
    res = []
    for i in b_keys:
        if not (i in a_keys):
            res.append(i)
    return res

def union_dikts(a, b):
    """объединение словарей в один, так чтоб числа при одинаковых ключах суммировались"""
    dict_itog = {}
    for i in a.keys():
        if i in b.keys():
            dict_itog[i] = a[i] + b[i]
            b.pop(i)
        else:
            dict_itog[i] = a[i]
    return (dict(b.items() | dict_itog.items()))

print("---------------2.1--------------------")
print(common_keys(a,b))
print("-------------------------------------")
print(difference_keys(a,b))
print("-------------------------------------")
print(union_dikts(a,b))

import re

l = [2, 2, 4, 4, 4, 6, 6, 7, 9, 9, 9, 9, 5, 5, 1, 7, 7]

def decode(l):
    l_str = []
    for i in l:
        l_str.append(str(i))
    myString = ''.join(l_str)

    l_res = []
    for item in re.findall(r"((.)\2*)", myString):
        print(item[0])
        res = (len(item[0]), int((item[0])[0]))
        l_res.append(res)
    return l_res

print(decode(l))

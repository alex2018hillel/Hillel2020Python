s = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
w = 4

for i in range(0, len(s), w):
    end = i + w
    res = s[i:end]
    print(res)

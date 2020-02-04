from heapq import heappush, heappop

def heapsort(l):
    result = []
    for i in l:
        heappush(result, i)
    return [heappop(result) for i in range(len(result))]

l = [88, 1, 56, 45, 3, 8, 99, 5]
print(heapsort(l))

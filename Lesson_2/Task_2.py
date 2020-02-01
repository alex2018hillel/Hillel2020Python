def binary_search(array, item):
    if len(array) == 0:
        return False
    else:
        mid_point = len(array)//2
    if array[mid_point]==item:
        return True
    else:
        if item<array[mid_point]:
            return binary_search(array[:mid_point],item)
        else:
            return binary_search(array[mid_point+1:],item)

array = [0, 4, 6, 8, 15, 16, 19, 48, 72, 103]
value = int(input("Input value:"))
print(binary_search(array, value))

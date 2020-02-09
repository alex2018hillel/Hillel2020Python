l = [1, 'one', 'two', 3.0, 4j, 5j, 3, 2, 12., 17, [1,2], {1:1}]
"""вывести только объекты самого частого типа"""
type_list = []
for x in l:
    type_list.append((type(x)))

result = {i: type_list.count(i) for i in type_list}
print(result)

num = (sorted(result.values(), reverse=True )[0])
max_type = ({k for k, v in result.items() if v == num})
print("max frequency == ", list(max_type)[0])

list_max_type = []
for el in l:
    if type(el) == list(max_type)[0]:
        list_max_type.append((el))
print(list_max_type)

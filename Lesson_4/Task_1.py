def swap(target_list, item_index1, item_index2):
    target_list[item_index1], target_list[item_index2] = target_list[item_index2], target_list[item_index1]
    return target_list

target_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(target_list)
item_index1 = 2
item_index2 = 4
print(swap(target_list, item_index1, item_index2))
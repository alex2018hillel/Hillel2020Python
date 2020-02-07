def swap(target_list):
    summ_i = 0
    for i in target_list:
        a, b, *c = list(bin(i))#%==2
        sum_bin = 0
        for item in c:
            sum_bin = sum_bin + int(item)
        #print (sum_bin)
        if sum_bin%2 == 0:
            summ_i += i
        print("число" , i , "cумма bin" , sum_bin , "cумма чисел" , summ_i)
    return summ_i * target_list[-2]

target_list = [8, 2, 3, 4, 5, 6, 7, 2, 9]

print(swap(target_list))

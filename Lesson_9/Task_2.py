all_list = []
with open("222.txt", 'r', encoding='utf-8') as file:
    for line in file:
        line = line.rstrip('\n')
        a, b, c = line.split(' ')
        all_list.append([a, b[0], b, c])
    print(all_list)

number_list = []
letter_list = ['K', 'C']
for l in letter_list:
    file_name = l + ".txt"
    myfile = open(file_name, 'w')
    for i in all_list:
        kapital = i[1]
        if kapital == l:
            string = '{} {} {}'.format(i[0], i[2], i[3])
            myfile.write(string +'\n')

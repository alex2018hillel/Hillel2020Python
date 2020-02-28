with open("text1.txt", 'r', encoding='utf-8') as file:
    word_list = []
    for line in file:
        line = line.rstrip('\n')
        word_list = line.split(' ')
        print(word_list)
        delete_list = []
        for word in word_list:
            if (len(word) > 2 and len(word)<6):
                delete_list.append(word)
            count = len(delete_list)
        if count % 2 == 1:
            del delete_list[-1]
            print(delete_list)
        new_list = [i for i in word_list if not i in delete_list or delete_list.remove(i)]

        print(new_list)

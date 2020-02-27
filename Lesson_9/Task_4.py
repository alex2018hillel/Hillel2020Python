with open("text.txt", 'r', encoding='utf-8') as file:
    word_list = []
    for line in file:
        line = line.rstrip('\n')
        word_list = line.split(' ')
        delete_list = []
        for word in word_list:
            if (len(word) > 2 and len(word)<6):
                delete_list.append(word)
            count = len(delete_list)
        if count % 2 == 1:
            del delete_list[-1]
        new_list = []
        for word in word_list:
            if word in delete_list:
                pass
            else:
                new_list.append(word)
        string = ' '.join(new_list)
        print(string)

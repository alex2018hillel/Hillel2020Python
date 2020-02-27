def print_full_name(first_name, last_name):
    print('Hello {} {} You just delved into python.'.format(first_name, last_name))

first_name = None
if __name__ =="__main__":
    while first_name !='0':

        first_name = input("Exit - 0 \nInput first name:")
        last_name = input("Input last name:")
        if len(list(first_name))<=10 and len(list(last_name))<=10:
            print_full_name(first_name, last_name)
            break
        else:
            print("Input Format is wrong. Please input again:")

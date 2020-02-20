
def phones_fixer(func):
    def wrapper(nlist):
        #
        for item in list(nlist):
            #print("2",item)
            nnlist = []

            numb = []

            c = item[-5:]
            b = item[-10:-5]
            a = item[-15:-10]
            numb.append(a)
            numb.append(b)
            numb.append(c)
            nlist_one = " ".join(numb)
            print(nlist_one)
            #nlist = []
            nnlist.append(nlist_one)
            print(nnlist)



        return func(nnlist)
    return wrapper

# phones_fixer(numbers)
@phones_fixer
def sort_numbers(numbers_list):
    return '\n'.join(sorted(numbers_list))

def read_numbers():
    n = int(input())
    #n = "+919875641230"
    numbers = []
    for i in range(n):
        number  = input()
        numbers.append(number)
    return numbers

if __name__=='__main__':
    numbers = read_numbers()
    print("555", sort_numbers(numbers))


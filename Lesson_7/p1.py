def phones_fixer(func):
    def wrapper(nlist):
        phone_numbers = []
        for item in list(nlist):
            numb = []
            c = item[-5:]
            b = item[-10:-5]
            a = item[-15:-10]
            if a != "+91":
                a = "+91"
            numb.append(a)
            numb.append(b)
            numb.append(c)
            phone_num = " ".join(numb)
            phone_numbers.append(phone_num)
        return func(phone_numbers)
    return wrapper

@phones_fixer
def sort_numbers(nnlist):
    return '\n'.join(sorted(nnlist))

def read_numbers():
    n = int(input())
    numbers = []
    for i in range(n):
        number  = input()
        numbers.append(number)
    return numbers

if __name__=='__main__':
    numbers = read_numbers()
    print(sort_numbers(numbers))


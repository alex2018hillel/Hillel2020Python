import string

def print_the_alphabet_rangoli(n):
    len_arrow = n*2-1
    s = lowercase[:n][::-1]
    for number in range(len_arrow):
        i = min(number, len_arrow-number-1)
        center_string = '-'.join(list(s[:i]+s[i]+s[:i][::-1]))
        print('-'*(len_arrow-2*i-1)+center_string+'-'*(len_arrow-2*i-1))

n = 1
lowercase = string.ascii_lowercase
if __name__ =="__main__":
    while n !=0:
        n = int(input("Input N:"))
        if n<27 and n>0:
            print_the_alphabet_rangoli(n)
            break
        else:
            print("Input Format is wrong. Please input again:")
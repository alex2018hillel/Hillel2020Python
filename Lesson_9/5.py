import time

import string

def print_the_alphabet_rangoli(n):
    len_arrow = n*2-1
    s = lowercase[:n][::-1]
    for number in range(len_arrow):
        i = min(number, len_arrow-number-1)
        center_string = '-'.join(list(s[:i]+s[i]+s[:i][::-1]))
        print('-'*(len_arrow-2*i-1)+center_string+'-'*(len_arrow-2*i-1))

n = 12
lowercase = string.ascii_lowercase
if __name__ =="__main__":
    while n !=0:
        n = int(input("Input N:"))
        if n<27 and n>0:
            print_the_alphabet_rangoli(n)
            time.sleep(0.25)
            lowercase_list = list(lowercase)
            lowercase_list.append(lowercase_list[0])
            lowercase_list.remove(lowercase_list[0])
            lowercase = ''.join(lowercase_list)

        else:
            print("Input Format is wrong. Please input again:")

#p1 = figure(title="Legend Example")


# p1.circle(x,   y, legend="sin(x)")
# p1.circle(x, 2*y, legend="2*sin(x)", color="orange")
# p1.circle(x, 3*y, legend="3*sin(x)", color="green")
#
# p1.legend.title = 'Example Title'
#     while n !=0:
#         #n = int(input("Input N:"))
#         if n<27 and n>0:
#             print_the_alphabet_rangoli(n)
#             time.sleep(0.25)
#             lowercase_list = list(lowercase)
#             lowercase_list.append(lowercase_list[0])
#             lowercase_list.remove(lowercase_list[0])
#             lowercase = ''.join(lowercase_list)
#
#         else:
#             print("Input Format is wrong. Please input again:")
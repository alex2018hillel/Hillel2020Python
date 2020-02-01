import random
import re

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def password(chars):
    password =''
    for i in range(length):
        password += random.choice(chars)
    if len(list(password)) == len(re.findall(r'\d', password)):
        print("password contein only numbers")
    else:
        print("password contein numbers and letters")
    return password

length = 1
while length!=0:
    length = input('Password length:')
    length = int(length)
    print(password(chars))


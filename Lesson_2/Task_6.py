import re

str = "English = 78 Science = 83 Math = 68 History = 65"

def sum_num(str):
    """Return sum all numbers in string"""
    regex_num = re.compile('\d+')
    numbers_string = regex_num.findall(str)
    numbers = [int(elem) for elem in numbers_string]
    return sum(numbers)

print(sum_num(str))
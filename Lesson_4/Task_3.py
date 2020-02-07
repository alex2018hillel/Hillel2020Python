import re

def assert_4_simbol():
    if (len(list(string))) > 4:
        return print("длина больше 4 символов")
    else:
        return print("пароль не валидный")

def assert_char(string):
    chars = list(string)
    Number = 0
    for char in chars:
        if  symbol.__contains__(char):
            Number += 1
        else:
            return print("Ошибка:", char, "не является валидным символом")
    return print("Все", Number, "символов валидны")

def assert_letters_and_numbers(string):
    regex_num = re.compile('\d+')
    regex_let = re.compile('[a-z]')
    numbers_string = regex_num.findall(string)
    letters_string = regex_let.findall(string)
    print(numbers_string)
    print(letters_string)
    if (len(numbers_string)%2 == 0) & (len(letters_string)%2 != 0):
        print("Проверка пройдена")
    else:
        print("Проверьте правильность пароля")

string = "abg2dfg8j"
string2 = "abg2dTg8j"
string3 = "ag2dfg8j"
symbol = 'abcdefghijklnopqrstuvwxyz1234567890'

print("1) Проверка", string, "на символы")
assert_4_simbol()
print("2.1) Проверка", string, "на символы")
assert_char(string)
print("2.2) Проверка", string2, "на символы")
assert_char(string2)
print("3.1) Проверка", string, "на буквы и цифры")
assert_letters_and_numbers(string)
print("3.2) Проверка", string3, "на буквы и цифры")
assert_letters_and_numbers(string3)
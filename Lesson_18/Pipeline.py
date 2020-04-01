from string import ascii_letters as letters


def filter_upper(letters):
    for letter in letters:
        print("filter_upper")
        if letter.isupper():
            yield letter

def filter_selected(letters, selected):
    selected = set(map(str.lower, selected))
    for letter in letters:
        print("filter_selected")
        if letter.lower() in selected:
            yield letter


def main():
    stuff = filter_selected(filter_upper(letters), ['a', 'b', 'c'])
    print(list(stuff))

main()
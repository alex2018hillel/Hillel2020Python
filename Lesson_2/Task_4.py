def turn_words(s):
    """Turn words in string"""
    turn = s.split()
    words = []
    for i in turn:
        word = ''.join(reversed(i))
        words.append(word)
    new_frase = " ".join(map(str, words))
    return new_frase

s = input("Input string: ")
print(turn_words(s))
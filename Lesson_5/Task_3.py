text = "Help ELephant learn LOops. While's and fOrs. RLD!"
symbol = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

word_list = []
for l in list(text):
    if l in list(symbol):
        word_list.append(l)
word = ''.join(word_list)
print(word)
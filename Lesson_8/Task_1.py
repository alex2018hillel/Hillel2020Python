import string
import itertools
import pyzipper as pyzipper

with pyzipper.AESZipFile('lesson6.zip') as file:
    for item in itertools.permutations(string.ascii_lowercase, 3):
        word = (''.join(item))
        try:
            print(word)
            file.pwd = word.encode('ascii')
            file.extractall()
            print("Password is finding")
        except:
            pass

if __name__ == "__main__":
    pass
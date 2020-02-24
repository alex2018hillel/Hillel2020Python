import string
from itertools import combinations_with_replacement
import pyzipper as pyzipper
import zipfile
# l = []
# for i in range(97, 123):
#     l.append(chr(i))
#########################################################################
# with zipfile.ZipFile('123.zip', 'r') as archive:
#     for item in combinations_with_replacement(string.ascii_lowercase, 3):
#         word = (''.join(item))
#         password = word.encode('ascii')
#         password_b = word.encode('utf-8')
#         print(password_b)
#         try:
#             ###z = zipfile.ZipFile('lesson6.zip')
#             z = zipfile.ZipFile('123.zip')
#             ###z.extractall(pwd=bytes(word,'utf-8'))
#             z.pwd = word
#             z.extractall(pwd=str(line))
#             # z.extractall(pwd=word.encode('ascii'))
#             print("1111111111111")
#         except :
#             pass
###############################################################
#with pyzipper.AESZipFile('lesson6.zip') as file:

with pyzipper.AESZipFile('123.zip') as file:
    for item in combinations_with_replacement(string.ascii_lowercase, 3):
        word = (''.join(item))
        try:
            print(word)
            file.pwd = word.encode('ascii')
            file.extractall('Extracted')
            print("Password is finding")
        except:
            pass

        #-----------------------------------------
# with pyzipper.AESZipFile('123.zip') as file:
#     for item in combinations_with_replacement(string.ascii_lowercase, 3):
#         word = (''.join(item))
#         try:
#             print(word)
#             file.pwd = word.encode('ascii')
#             file.extractall('Extracted')
#             print("Password is finding")
#         except:
#             pass
        #--------------------------------------------

if __name__ == "__main__":
    pass
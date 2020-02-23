import string
import zipfile
from itertools import combinations_with_replacement
#from zipfile import  ZipFile
import zipfile
from os import mkdir

import args as args

l = []
for i in range(97, 123):
    l.append(chr(i))#, end=' '

def generator(l):
    for item in combinations_with_replacement(l, 3):
        word = (''.join(item))

directory = "Archive"
# try: mkdir(directory):
# except FileExistsError:
#     pass

# with open(input)
with zipfile.ZipFile('lesson6.zip', 'r') as archive:
    #for password in generator(l):
   ### print(archive.read(2).decode())
    for item in combinations_with_replacement(string.ascii_lowercase, 3):
        word = (''.join(item))
        word_encode = word.encode('utf8')#.encode('ascii')
        #print(word_encode)
        word1 = 'ibm'
        word_encode1 = word1.encode('utf-8')#.encode('ascii')

        print(word_encode1)
        word_decode1 = word_encode1.decode('utf8')
        print(word_decode1)

        # try:
        #     word_encode1 = word1.encode('windows-1251')#.encode('ascii')
        # except Exception as e:
        #     print(e)
        #print(word_encode1)
        #if word_encode ==
        # with open(archive, 'rb') as file:
        #     currentType = file.read(2).decode()
z = zipfile.ZipFile('lesson6.zip')
word1 = 'ibm'
z.extractall(pwd=bytes('ibm','utf-8'))
###z.setpassword(word1.encode('utf-8'))
#z.setpassword(word_encode1)
###z.extractall()
        #try:
        #     z = zipfile.ZipFile('lesson6.zip')
        #     z.setpassword("ibm")
        #     z.extract("sample.txt")
        #     # zipfile.ZipFile.setpassword('ibm')
        #     # zipfile.ZipFile.extract("sample/sample.txt")
        #     ###zipfile.ZipFile.extractall(pwd=word_encode1)
        #     print("!!!")
        ###archive.extractall(pwd=word_encode)pwd=bytes('the_zip_password','utf-8')
        #     print( "\n[True]: " + word)
        # except:
        #     pass

###############################################################
# def cutMagicNumbers(archive):
#     with open(archive, 'rb') as file:
#         currentType = file.read(2).decode()
#     return launcher(currentType)

def launcher(extension):
    return {'PK': prepareBruteZip}.get(extension, 'Not Found')

def prepareBruteZip(archive, dictionary):
    zArchive = zipfile.ZipFile #&#40;archive&#41;
    with open(dictionary, 'r') as wordlist:
        for word in wordlist.readlines():
            password = word.strip('\n').encode('ascii')  # unicode → byte
            brute(zArchive, password)

def brute(archive, password):
    try:
        archive.extractall(pwd=password)
        print('[+] Password is {}'.format(password))
    except:
        pass

import argparse
parser = argparse.ArgumentParser( '--file ' + '--dict ')
parser.add_argument('-f', '--file', dest='archive', required=True, type=str, help='Archive file')
parser.add_argument('-d', '--dict', dest='dictionary', required=True, type=str, help="Dictionary file")
#args = parser.parse_args()

#cutMagicNumbers(args.archive)(args.archive, args.dictionary)


if __name__ == "__main__":
    pass
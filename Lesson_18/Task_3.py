import os

def find_files(dir):

    for i in dir_list(dir):
        if os.path.isdir(i):
            find_files(i)
        else: print(i)

def dir_list(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        yield path

find_files("C:\Recovery")



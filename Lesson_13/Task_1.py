class my_exeption(Exception):
    def __init__(self, text):
        self.txt = text

    def __enter__(self):
        pass

    def write_to_file(self,c):
        with open("output.txt", "w") as f:
            line = (str(c)+' - ZeroDivisionError!')
            f.write(line)
            e = (self.args)[0]
        return e

def func(b,c):
    try:
        if c == 0:
            raise my_exeption("ZeroDivisionError!")
    except my_exeption as mr:
        return mr.write_to_file(c)
    else:
        print(c)
    return b/c

c=0
print(func(5,c))
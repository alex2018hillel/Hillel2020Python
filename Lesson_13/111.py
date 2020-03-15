
class my_exeption(Exception):
    def __init__(self, text):
        self.txt = text
        print("!!!!!!!!!!!!")

    def __enter__(self):
        pass

    def write_to_file(self,c):
        with open("output.txt", "w") as f:
            f.write(str(c))


def func(b,c):
    try:
        if c == 0:
            raise my_exeption("ZeroDivisionError!")
    except my_exeption as mr:
        mr.write_to_file(c)
        return

    else:
        print(c)
    return b/c

c=0
print(func(5,c))




    # except my_exeption as mr:
    # print(mr)
    #
    # exept Exception as e:
    #     e.wr
    #
    # with foo('start') as f:
    #     print(f)
    #

import math

class Figure:
    def P(self):
        raise Exception('wrong data')
    def S(self):
        raise Exception('wrong data')

class Triangle(Figure):
    def __init__(self, args):
        self.a = args
        print('Triangle ',self.a)
        if len(args) != 3:
            super().P()
            super().S()
        else:
            self.P()
            self.S()

    def P(self):
        theSum = 0
        for i in self.a:
            theSum = theSum + i
        print('P = ' + str(theSum))
    def S(self):
        a,b,c = self.a

        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print('S = ' + str(s))

class Rectangle(Figure):
    def __init__(self, args):
        self.a = args
        print('Rectangle',self.a)
        if len(args) != 2:
            super().P()
            super().S()
        else:
            self.P()
            self.S()

    def P(self):
        a,b = self.a
        perimetr = (a + b)*2
        print('P = ' + str(perimetr))

    def S(self):
        a,b = self.a
        s = a*b
        print('S = ' + str(s))

class Circle(Figure):
    def __init__(self, args):
        self.a = args
        print('Circle',self.a)
        if len(args) != 1:
            super().P()
            super().S()
        else:
            self.P()
            self.S()

    def P(self):
        r = self.a[0]
        perimetr = 2 * math.pi * r
        print('P = ' + str(perimetr))

    def S(self):
        r = self.a[0]
        s = math.pi * r ** 2
        print('S = ' + str(s))

t = Triangle([3,4,5])
p = Rectangle([3,4])
c = Circle([3])

class Figure:
    def P(self):
        raise Exception('wrong data')
    def S(self):
        raise Exception('wrong data')

class Triangle(Figure):
    def __init__(self, args):
        self.a = args
        print(self.a)
        if len(args) != 3:
            super().P()
        else:
            self.P()

    def P(self):
        theSum = 0
        for i in self.a:
            theSum = theSum + i
        print('P = ' + str(theSum))
    def S(self):
        ploshad = 6


    #return sum()

t = Triangle([3,4,5])




import math
import pytest

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
        return theSum

    def S(self):
        a,b,c = self.a

        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print('S = ' + str(s))
        return s

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
        return perimetr

    def S(self):
        a,b = self.a
        s = a*b
        print('S = ' + str(s))
        return s

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
        return perimetr

    def S(self):
        r = self.a[0]
        s = math.pi * r ** 2
        print('S = ' + str(s))
        return s

t = Triangle([3,4,5])
p = Rectangle([3,4])
c = Circle([3])


class TestTriangle:
    tr = Triangle([3,4,5])

    def test_len_args(self):
        print(self.tr.a)
        assert len(self.tr.a) == 3, 'Invalid list size'

    def test_perimeter_function(self):
        res = self.tr.P()
        assert res == 12, 'Invalid function'

    def test_perimeter_type(self):
        with pytest.raises(TypeError):
            res = self.tr.P([1, '2', 3])
            assert pytest.raises == TypeError

    def test_perimeter_type_list(self):
        with pytest.raises(TypeError):
            tr = Triangle([[3],[4],[5]])
            res = self.tr.P()
            print("data1" + str(res))
            assert pytest.raises == TypeError

    def test_area_function(self):
        res = self.tr.S()
        assert res == 6, 'Invalid function'

    def test_area_type(self):
        with pytest.raises(TypeError):
            res = self.tr.S([1, '2', 3])
            assert pytest.raises == TypeError

    def test_area_type_list(self):
        with pytest.raises(TypeError):
            tr = Triangle([[3],[4],[5]])
            res = self.tr.S()
            print("data1" + str(res))
            assert pytest.raises == TypeError

class TestRectangle:
    rec = Rectangle([3,4])

    def test_len_args(self):
        print(self.rec.a)
        assert len(self.rec.a) == 2, 'Invalid list size'

    def test_perimeter_function(self):
        res = self.rec.P()
        assert res == 14, 'Invalid function'

    def test_area_function(self):
        res = self.rec.S()
        assert res == 12, 'Invalid function'

    def test_perimeter_type(self):
        with pytest.raises(TypeError):
            res = self.rec.P([3, '4'])
            assert pytest.raises == TypeError

    def test_perimeter_type_list(self):
        with pytest.raises(TypeError):
            rec = Rectangle([[3],[4]])
            res = self.rec.P()
            assert pytest.raises == TypeError

    def test_area_type(self):
        with pytest.raises(TypeError):
            res = self.rec.S([1, '2'])
            assert pytest.raises == TypeError

    def test_area_type_list(self):
        with pytest.raises(TypeError):
            tr = Rectangle([[3],[4]])
            res = self.rec.S()
            assert pytest.raises == TypeError


class TestCircle:
    circle = Circle([3])

    def test_len_args(self):
        print(self.circle.a)
        assert len(self.circle.a) == 1, 'Invalid list size'

    def test_perimeter_function(self):
        res = self.circle.P()
        assert res == 18.84955592153876, 'Invalid function'

    def test_perimeter_type(self):
        with pytest.raises(TypeError):
            res = self.circle.P(['2'])
            assert pytest.raises == TypeError

    def test_perimeter_type_list(self):
        with pytest.raises(TypeError):
            circle = Circle([[3],])
            res = self.circle.P()
            print("data1" + str(res))
            assert pytest.raises == TypeError

    def test_area_function(self):
        res = self.circle.S()
        assert res == 28.274333882308138, 'Invalid function'

    def test_area_type(self):
        with pytest.raises(TypeError):
            res = self.circle.S(['2'])
            assert pytest.raises == TypeError

    def test_area_type_list(self):
        with pytest.raises(TypeError):
            circle = Circle([[3],])
            res = self.circle.S()
            print("data1" + str(res))
            assert pytest.raises == TypeError



















#
#     @pytest.mark.unit
#     def test_perimeter_large(self, a=3, b=4, c=5):
#         fact = self.tr.P(a)
#         expected = a * a
#         print(fact, expected)
#         self.assertEqual(fact, expected)
#
# @pytest.mark.unit
# def test_process_input_add_integers(self):
#     res = self.tr.P([3,4,5])
#     assert res == 5, 'Invalid add integers'
#
# @pytest.mark.unit
# def test_process_input_add_lists():
#     res = process_input([2], [3], 'add')
#     assert res == [2, 3], 'Invalid add lists'
#
#
# def test_process_input_add_exception():
#     import pytest
#     with pytest.raises(TypeError):
#         res = process_input(1, '2', 'add')
#     # assert res == 3, 'Invalid add operation'
#
# def test_process_input():
#     res = process_input(10, 5, 'subtract')
#     assert res == 5, 'Subract incorrect'
#
# def test_process_input_divide_raised_exception():
#     """
#     check dision by zero
#     :return:
#     """
#     import pytest
#     err = None
#     with pytest.raises(Exception) as exc:
#         err = exc
#         process_input(10, 0, 'divide')
#     print(err.value)
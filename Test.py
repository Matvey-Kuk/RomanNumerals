import unittest

from NumberWithFractions import *


class TestAlteration(unittest.TestCase):

    #Это тесты, с помощью них проверяются разные кусочки программы

    def setUp(self):
        pass

    def test_addition(self):
        a = Number('XV')
        b = Number('VI')
        number = Number('XV') + Number('VI')
        self.assertEqual(a.get_as_arabic() + b.get_as_arabic(), number.get_as_arabic())

    def test_substraction(self):
        a = Number('XLCLLCVIV')
        b = Number('XVVII')
        number = a - b
        self.assertEqual(a.get_as_arabic() - b.get_as_arabic(), number.get_as_arabic())

    def test_multiplication(self):
        a = Number('XLCIV')
        b = Number('XCLIIICLVVI')
        number = a * b
        self.assertEqual(a.get_as_arabic() * b.get_as_arabic(), number.get_as_arabic())

    def test_division(self):
        a = Number('XXXIIII')
        b = Number('CCCCCCCCCCCCCCCLXXXXVIII')
        number = b / a
        self.assertEqual(b.get_as_arabic() / a.get_as_arabic(), number.get_as_arabic())

    def test_subtraction_form_removing(self):
        digits = Number('XIV').get_digits()
        self.assertEqual(digits, 'XIIII')

    def test_compare(self):
        self.assertTrue(Number('I') < Number('V'))
        self.assertFalse(Number('I') > Number('V'))
        self.assertFalse(Number('V') > Number('V'))

    #ТЕПЕРЬ ТЕСТЫ ДРОБНЫХ ЧИСЕЛ

    def test_integer_allocation(self):
        a = NumberWithFractions('I', 'XI', 'V')
        self.assertEqual(a.get_integer(), Number('III'))
        self.assertEqual(a.get_numerator(), Number('I'))
        self.assertEqual(a.get_denominator(), Number('V'))

    def test_fractional_division(self):
        b = NumberWithFractions('V', 'I', 'V')
        a = NumberWithFractions('I', 'I', 'VI')
        c = b / a
        self.assertEqual(c.get_integer(), Number('IIII'))
        self.assertEqual(c.get_numerator(), Number('XVI'))
        self.assertEqual(c.get_denominator(), Number('XXXV'))
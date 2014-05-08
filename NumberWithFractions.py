from Number import *


class NumberWithFractions():
    #А это уже класс с дробями

    def __init__(self, integer, numerator='', denominator=''):
        #Перегружаем конструктор и вводим числитель и знаменатель
        self.__integer_part = Number(integer)
        self.__numerator_part = Number(numerator)
        self.__denominator_part = Number(denominator)
        self.allocate_integers_from_fractions()

    def allocate_integers_from_fractions(self):
        #Выделить из числителя и знаменателя целые если есть и прибавить к целой части
        if self.__numerator_part / self.__denominator_part > Number(''):
            integer_adding = (self.__numerator_part / self.__denominator_part)
            self.__integer_part = self.__integer_part + integer_adding
            self.__numerator_part = self.__numerator_part - integer_adding * self.__denominator_part

    def __repr__(self):
        if len(self.__numerator_part.get_digits()) == 0:
            return repr(self.__integer_part)
        else:
            return repr(self.__integer_part) + ' ' + repr(self.__numerator_part) + '/' + repr(self.__denominator_part)

    def get_integer(self):
        return self.__integer_part

    def get_numerator(self):
        return self.__numerator_part

    def get_denominator(self):
        return self.__denominator_part

    def __truediv__(self, other):
        #Это уже деление дробных чисел, активно используется целочисленное деление из класса целых чисел.
        #Переводим все дроби в числитель и знаменатель и умножаем 1-ю на перевернутую 2-ю, потом выделяем целую часть.
        #Аминь.
        numerator = self.get_numerator() + (self.get_integer() * self.get_denominator())
        numerator = numerator * other.get_denominator()

        denominator = other.get_numerator() + (other.get_integer() * other.get_denominator())
        denominator = denominator * self.get_denominator()

        result = NumberWithFractions('', numerator.get_digits(), denominator.get_digits())
        return result
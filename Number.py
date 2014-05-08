

class Number(object):
    #Это класс целых чисел

    def __init__(self, representation):
        #Конструктор
        if type(representation) is list:
            self.__digits = ''.join(representation)
        else:
            self.__digits = representation
        self.remove_substract_form()
        self.__digits = Number.convert_to_sorted_form(self.__digits)
        self.__digits = Number.convert_to_compact_form(self.__digits)

    def remove_substract_form(self):
        #Приводим в форму без сокращений отрицанием (IV) -> (IIII)
        rules = {
            'IV': 'IIII',
            'IX': 'VIIII',
            'IIX': 'VIII',
            'XL': 'XXXX',
        }
        new_digits = self.__digits
        digits_backup = ''
        while not digits_backup == new_digits:
            digits_backup = new_digits
            for key in rules:
                new_digits = new_digits.replace(key, rules[key])
        self.__digits = new_digits

    def get_digits(self):
        #Можно из объекта получить строку с его значением
        return self.__digits

    def __add__(self, other):
        #Перегружаем оператор сложения
        summ_digits = self.get_digits() + other.get_digits()
        result = Number(Number.convert_to_sorted_form(summ_digits))
        result.modify_to_compact_form()
        return result

    def __sub__(self, other):
        #Перегружаем оператор вычитания
        self_digits = self.get_digits()
        other_digits = other.get_digits()
        while not(self_digits == '' or other_digits == ''):
            new_self_digits = self_digits
            new_other_digits = other_digits
            something_changed = False
            for self_digit in self_digits:
                for other_digit in other_digits:
                    if self_digit == other_digit and not something_changed:
                        new_self_digits = new_self_digits[:new_self_digits.find(self_digit)] + new_self_digits[new_self_digits.find(self_digit) + 1:]
                        new_other_digits = new_other_digits[:new_other_digits.find(self_digit)] + new_other_digits[new_other_digits.find(self_digit) + 1:]
                        something_changed = True
            self_digits = new_self_digits
            other_digits = new_other_digits
            if not something_changed:
                self_digits = Number.convert_to_expanded_form(self_digits)
                other_digits = Number.convert_to_expanded_form(other_digits)
        if other_digits == '':
            self_digits = Number.convert_to_compact_form(self_digits)
            return Number(self_digits)
        else:
            return None

    def __mul__(self, other):
        #Перегружаем оператор умножения
        multiplication_rules = {
            'I': {
                'I': 'I',
                'V': 'V',
                'X': 'X',
                'L': 'L',
                'C': 'C'
            },
            'V': {
                'I': 'V',
                'V': 'XXV',
                'X': 'L',
                'L': 'CCL',
                'C': 'CCCCC'
            },
            'X': {
                'I': 'X',
                'V': 'L',
                'X': 'C',
                'L': 'CCCCC',
                'C': 'CCCCCCCCCC'
            },
            'L': {
                'I': 'L',
                'V': 'CCL',
                'X': 'CCCCC',
                'L': 'CCCCCCCCCCCCCCCCCCCCCCCCC',
                'C': 'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC'
            },
            'C': {
                'I': 'C',
                'V': 'CCCCC',
                'X': 'CCCCCCCCCC',
                'L': 'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC',
                'C': 'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC'
            }
        }
        result_symbols = ''
        for first_symbol in self.get_digits():
            for last_sumbol in other.get_digits():
                result_symbols += multiplication_rules[first_symbol][last_sumbol]
        result_symbols = Number.convert_to_sorted_form(result_symbols)
        result_symbols = Number.convert_to_compact_form(result_symbols)
        return Number(result_symbols)

    def __truediv__(self, other):
        #Это то самое деление, но в данном случае оно получает только целую часть
        result = Number('')
        dividend = Number(self.get_digits())
        multiplicators = [Number('C'), Number('L'), Number('X'), Number('V'), Number('I')]
        for multiplicator in multiplicators:
            while multiplicator * other < dividend or multiplicator * other == dividend:
                # print('m' + repr(multiplicator.show_as_arabic()))
                # print('d' + repr(dividend.show_as_arabic()))
                # print('o' + repr(other.show_as_arabic()))
                result = result + multiplicator
                dividend = dividend - multiplicator * other
                # print('r' + repr(result.show_as_arabic()))
        return result

    def __lt__(self, other):
        #Перегружаем оператор "<", чтобы можно было сравнивать числа друг с другом
        return self - other is None

    def __repr__(self):
        #Перегружаем оператор вывода, чтобы можно было пихать объект в print()
        return self.__digits

    def get_as_arabic(self):
        arabic = 0
        rules = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100
        }
        for digit in self.get_digits():
            arabic += rules[digit]
        return arabic

    def __eq__(self, other):
        #Перегружаем оператор эквивалентности
        return self.get_digits() == other.get_digits()

    def modify_to_compact_form(self):
        #"Прими компактный вид"
        self.__digits = Number.convert_to_compact_form(self.__digits)

    @staticmethod
    def convert_to_expanded_form(digits):
        #Работает со строкой и раскладывает большие цифры в несколько более мелких. Например, V в IIIII
        new_digits = ''
        convertation_matrix = {
            'I': 'I',
            'V': 'IIIII',
            'X': 'VV',
            'L': 'XXXXX',
            'C': 'LL'
        }
        for digit in digits:
            new_digits += convertation_matrix[digit]
        return new_digits

    @staticmethod
    def convert_to_compact_form(digits):
        #Ужимает число до компактной формы
        new_digits = digits
        convertation_matrix = {
            'IIIII': 'V',
            'VV': 'X',
            'XXXXX': 'L',
            'LL': 'C'
        }
        digits_backup = ''
        while not digits_backup == new_digits:
            digits_backup = new_digits
            for key in convertation_matrix:
                new_digits = new_digits.replace(key, convertation_matrix[key])
        return new_digits

    @staticmethod
    def convert_to_sorted_form(digits):
        #Сортирует цифры в числе
        result = ''
        sorting_rules = ['C', 'L', 'X', 'V', 'I']
        number_of_digits = {}
        for digit in digits:
            if digit in number_of_digits:
                number_of_digits[digit] += 1
            else:
                number_of_digits[digit] = 1
        for rule in sorting_rules:
            if rule in number_of_digits:
                for a in range(0, number_of_digits[rule]):
                    result += rule
        return result
import unittest
from string_calculator import Calculator


class TestStringCalculator(unittest.TestCase):
    calculator = Calculator()

    def test_if_empty_string_return_zero(self):
        self.assertEqual(0, self.calculator.add(""))

    def test_if_number_return_same_number(self):
        self.assertEqual(1, self.calculator.add('1'))
        self.assertEqual(2, self.calculator.add('2'))

    def test_if_more_than_one_numbers_return_sum(self):
        self.assertEqual(3, self.calculator.add('1,2'))
        self.assertEqual(8, self.calculator.add('3,5'))
        self.assertEqual(20, self.calculator.add('3,7,10'))
        self.assertEqual(21, self.calculator.add('3,7,10,1'))

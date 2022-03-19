import unittest
from Calculator import Calculator


# Test case to test Calculator methods
class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.sum_add(5, 5), 10)

    def test_substract(self):
        self.assertEqual(self.calculator.subtracts_add(2, 1), 1)

    def test_divide(self):
        self.assertEqual(self.calculator.divide_add(10, 2), 5)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply_add(3, 7), 21)

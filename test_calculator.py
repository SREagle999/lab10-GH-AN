# https://github.com/SREagle999/lab10-GH-AN
# Partner 1: Abhay Narayan
# Partner 2: Gabriel Harris

import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self): 
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(4, 12), 16)
        self.assertEqual(calculator.add(7, 7), 14)

    def test_subtract(self): 
        self.assertEqual(calculator.sub(3, 1), 2)
        self.assertEqual(calculator.sub(10, 7), 3)
        self.assertEqual(calculator.sub(5, 4), 1)

    def test_multiply(self): 
        self.assertEqual(calculator.mul(2, 3), 6)
        self.assertEqual(calculator.mul(7, 2), 14)
        self.assertEqual(calculator.mul(3, 3), 9)

    def test_divide_by_zero(self): 
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)

    def test_logarithm(self): 
        self.assertEqual(calculator.log(10, 100), 2)
        self.assertEqual(calculator.log(2, 8), 3)
        self.assertEqual(calculator.log(5, 5), 1)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            calculator.log(10, -5)

    def test_divide(self): 
        self.assertEqual(calculator.div(2, 10), 5)
        self.assertEqual(calculator.div(4, 20), 5)
        self.assertAlmostEqual(calculator.div(3, 10), 3.333333, places=5)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 10)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 8)
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(10, -5)
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(10, 0)

    def test_hypotenuse(self):
        self.assertEqual(calculator.hypotenuse(3, 4), 5)
        self.assertEqual(calculator.hypotenuse(5, 12), 13)
        self.assertAlmostEqual(calculator.hypotenuse(1, 1), 1.414213, places=5)
        # Test with negative numbers (should work)
        self.assertEqual(calculator.hypotenuse(-3, -4), 5)

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(4), 2)
        self.assertEqual(calculator.square_root(9), 3)
        self.assertAlmostEqual(calculator.square_root(2), 1.414213, places=5)
        self.assertEqual(calculator.square_root(0), 0)
        with self.assertRaises(ValueError):
            calculator.square_root(-4)


if __name__ == '__main__':
    unittest.main()

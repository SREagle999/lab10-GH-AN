import unittest
import calculator


class TestCalculator(unittest.TestCase):



    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 3), 6)

        self.assertEqual(calculator.multiply(-2, 3), -6)

        self.assertEqual(calculator.multiply(0, 5), 0)

        self.assertEqual(calculator.multiply(2.5, 4), 10)

    def test_divide(self):
        self.assertEqual(calculator.divide(2, 10), 5)
        self.assertEqual(calculator.divide(4, 20), 5)
        self.assertAlmostEqual(calculator.divide(3, 10), 3.333333, places=5)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 10)

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
import unittest
from factorial import factorial_iterative, factorial_recursive

class TestFactorial(unittest.TestCase):
    def test_iterative_base_cases(self):
        self.assertEqual(factorial_iterative(0), 1)
        self.assertEqual(factorial_iterative(1), 1)

    def test_iterative_general_case(self):
        self.assertEqual(factorial_iterative(5), 120)

    def test_iterative_negative(self):
        with self.assertRaises(ValueError):
            factorial_iterative(-3)

    def test_recursive_base_cases(self):
        self.assertEqual(factorial_recursive(0), 1)
        self.assertEqual(factorial_recursive(1), 1)

    def test_recursive_general_case(self):
        self.assertEqual(factorial_recursive(5), 120)

    def test_recursive_negative(self):
        with self.assertRaises(ValueError):
            factorial_recursive(-2)

if __name__ == '__main__':
    unittest.main()

import unittest
from fibonacci import fibonacci_iterative, fibonacci_recursive

class TestFibonacci(unittest.TestCase):
    def test_iterative_base_cases(self):
        self.assertEqual(fibonacci_iterative(1), 0)
        self.assertEqual(fibonacci_iterative(2), 1)

    def test_iterative_general_case(self):
        self.assertEqual(fibonacci_iterative(5), 3)
        self.assertEqual(fibonacci_iterative(10), 34)

    def test_iterative_negative(self):
        with self.assertRaises(ValueError):
            fibonacci_iterative(0)

    def test_recursive_base_cases(self):
        self.assertEqual(fibonacci_recursive(1), 0)
        self.assertEqual(fibonacci_recursive(2), 1)

    def test_recursive_general_case(self):
        self.assertEqual(fibonacci_recursive(5), 3)
        self.assertEqual(fibonacci_recursive(10), 34)

    def test_recursive_negative(self):
        with self.assertRaises(ValueError):
            fibonacci_recursive(-3)

if __name__ == '__main__':
    unittest.main()

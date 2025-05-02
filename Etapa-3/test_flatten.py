import unittest
from flatten import flatten

class TestFlatten(unittest.TestCase):
    def test_flatten_simple_list(self):
        self.assertEqual(flatten([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_flatten_nested_lists(self):
        self.assertEqual(flatten([1, [2, 3], [4, [5, 6]]]), [1, 2, 3, 4, 5, 6])

    def test_flatten_mixed_data_structures(self):
        self.assertEqual(flatten([1, (2, 3), {'a': 4, 'b': 5}, [6, [7, 8]]]), [1, 2, 3, 'a', 4, 'b', 5, 6, 7, 8])

if __name__ == "__main__":
    unittest.main()
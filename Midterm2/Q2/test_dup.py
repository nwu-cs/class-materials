import unittest

from dup import has_any_duplicates,num_duplicates


class TestDuplicates(unittest.TestCase):
    a =[25, 4, 38, 22, 32, 42, 15, 28, 8, 33, 39, 34, 28, 48, 49, 6, 4, 42, 47, 24, 9, 19, 43, 44, 39, 16, 18, 16, 1, 43, 30, 32, 8, 20, 3, 11, 7, 16, 20, 19]
    b = range(1000)

    def test_has_any_duplicates1(self):
        self.assertTrue(has_any_duplicates(self.a))

    def test_has_any_duplicates2(self):
        self.assertFalse(has_any_duplicates(self.b))

    def test_num_duplicate1(self):
        self.assertEqual(num_duplicates(self.b),0)

    def test_num_duplicate2(self):
        self.assertEqual(num_duplicates(self.a),10)

if __name__ == '__main__':
    unittest.main()
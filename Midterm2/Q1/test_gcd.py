import unittest

from gcd import gcd


class TestGcd(unittest.TestCase):

    def test_gcd1(self):
        self.assertEqual(gcd(45, 6), 3)

    def test_gcd2(self):
        self.assertEqual(gcd(45, 9), 9)

    def test_gcd3(self):
        self.assertEqual(gcd(88, 16), 8)

    def test_gcd4(self):
        self.assertEqual(gcd(64, 120), 8)

    def test_gcd5(self):
        self.assertEqual(gcd(50, 4), 2)

    def test_gcd6(self):
        self.assertEqual(gcd(49, 8), 1)

    def test_gcd7(self):
        self.assertEqual(gcd(20, 5), 5)

    def test_gcd8(self):
        self.assertEqual(gcd(130, 25), 5)

if __name__ == '__main__':
    unittest.main()
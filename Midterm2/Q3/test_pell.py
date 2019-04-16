import unittest

from pell import pell


class TestDuplicates(unittest.TestCase):

    def test_pell50(self):
        x = pell(49)
        y = pell(50)
        self.assertEqual(x,2015874949414289041)
        self.assertEqual(y,4866752642924153522)

if __name__ == '__main__':
    unittest.main()
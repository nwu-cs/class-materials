import unittest

from crypto import Crypto


class TestCrypto(unittest.TestCase):

    def test_crypto1(self):
        a = "teststringshowingnumbersdontwork123789$%!#"
        c = Crypto("MANCHESTERBLUFF")
        b = c.encrypt(a)
        self.assertEqual(b,"FEFVZXJBRXTSIBNZGAWTFWKWUPYNBTDKXNTUJLBPVH")
        d = c.decrypt(b)
        self.assertEqual(d,"TESTSTRINGSHOWINGNUMBERSDONTWORKKLMQRSXYUW")

    def test_crypto2(self):
        a =        "ATTACKATDAWN"
        c = Crypto("MANCHESTERBLUFF")
        b = c.encrypt(a)
        self.assertEqual(b,"MTGCJOSMHRXY")
        d = c.decrypt(b)
        self.assertEqual(d,"ATTACKATDAWN")

if __name__ == '__main__':
    unittest.main()
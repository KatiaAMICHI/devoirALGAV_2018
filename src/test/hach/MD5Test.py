import sys
import unittest

if sys.version_info.major == 2:
    pass
else:
    pass
from src.main.hach import MD5


class MD5Test(unittest.TestCase):

    def test_hach(self):
        md5 = MD5()

        demo = [b"", b"a", b"abc", b"Hello", b"toto",
                b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
                b"12345678901234567890123456789012345678901234567890123456789012345678901234567890"]

        result = ["d41d8cd98f00b204e9800998ecf8427e", "0cc175b9c0f1b6a831c399e269772661",
                  "900150983cd24fb0d6963f7d28e17f72", "8b1a9953c4611296a827abf8c47804d7",
                  "f71dbe52628a3f83a77ab494817525c6", "d174ab98d277d9f5a5611c2c9f419d9f",
                  "57edf4a22be3c955ac49da2e2107b67a"]

        for message, message_decode in zip(demo, result):
            self.assertEqual(md5.md5_to_hex(md5.md5(message)), message_decode)

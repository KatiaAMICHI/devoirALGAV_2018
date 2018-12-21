import sys

if sys.version_info.major == 2:
    pass
else:
    pass
from src.main.hach.MD5 import MD5

if __name__ == '__main__':
    md5 = MD5()
    demo = [b"The quick brown fox jumps over the lazy dog", b"", b"a", b"abc", b"Hello", b"toto",
            b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
            b"12345678901234567890123456789012345678901234567890123456789012345678901234567890"]
    for message in demo:
        print(md5.md5_to_hex(md5.md5(message)), ' <= "', message.decode('ascii'), '"', sep='')

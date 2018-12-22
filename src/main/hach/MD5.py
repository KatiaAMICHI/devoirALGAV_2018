import math


class MD5(object):
    # Definir rotate_amounts comme suit
    rotate_amounts = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
                      5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
                      4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
                      6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

    # Utilisation des sinus d entiers pour les constantes
    # Utilisation de 758 constant
    constants = [int(abs(math.sin(i + 1)) * 2 ** 32) & 0xFFFFFFFF for i in range(64)]

    # Préparation de la listes variables :
    init_values = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]

    # Definition des lambda pour
    #           (b and c) ou (not b and d) + (d and b) ou (not d and c) + b xor c xor d + c xor (b ou not d)
    operation = 16 * [lambda b, c, d: (b & c) | (~b & d)] + \
                16 * [lambda b, c, d: (d & b) | (~d & c)] + \
                16 * [lambda b, c, d: b ^ c ^ d] + \
                16 * [lambda b, c, d: c ^ (b | ~d)]

    index_operation = 16 * [lambda i: i] + \
                      16 * [lambda i: (5 * i + 1) % 16] + \
                      16 * [lambda i: (3 * i + 5) % 16] + \
                      16 * [lambda i: (7 * i) % 16]

    # définition de la fonction rotation
    @staticmethod
    def left_rotate(x, c):
        """
        Fonction rotation
        :param x:
        :param c:
        :return:
        """
        x &= 0xFFFFFFFF
        return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

    def word_md5(self, message):
        """
        Permet de hacher le mot message
        :param message: mot a hacher
        :return: message hacher
        """
        message = bytearray(message)  # copy our input into a mutable buffer
        len_msg_bits = (8 * len(message)) & 0xffffffffffffffff
        message.append(0x80)

        # remplissage avec des zéros
        while len(message) % 64 != 56:
            message.append(0)

        message += len_msg_bits.to_bytes(8, byteorder='little')

        hash_result = self.init_values[:]

        for i in range(0, len(message), 64):
            a, b, c, d = hash_result
            chunk = message[i:i + 64]
            for j in range(64):
                f = self.operation[j](b, c, d)
                g = self.index_operation[j](j)
                to_rotate = a + f + self.constants[j] + int.from_bytes(chunk[4 * g:4 * g + 4], byteorder='little')
                new_b = (b + self.left_rotate(to_rotate, self.rotate_amounts[j])) & 0xFFFFFFFF
                a, b, c, d = d, new_b, b, c
            # ajout des résultat obtenue
            for j, val in enumerate([a, b, c, d]):
                hash_result[j] += val
                hash_result[j] &= 0xFFFFFFFF

        digest = sum(x << (32 * i) for i, x in enumerate(hash_result))

        raw = digest.to_bytes(16, byteorder='little')
        return '{:032x}'.format(int.from_bytes(raw, byteorder='big'))

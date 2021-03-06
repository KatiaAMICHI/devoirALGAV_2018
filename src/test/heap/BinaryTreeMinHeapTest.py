import pprint
import sys
import time
import unittest
from collections import OrderedDict

from src.main.FileReader import FileReader, plot

if sys.version_info.major == 2:
    pass
else:
    pass

from src.main.heap.TreeMinHeap.BinaryTreeMinHeap import BinaryTreeMinHeap


class BinaryTreeMinHeapTest(unittest.TestCase):
    def test_consIterInt(self):
        heap = BinaryTreeMinHeap()
        list_elem = [50, 30, 70, 20, 40, 60, 80, 2, 3, 4, 5, 0]
        heap.ConsIter(list_elem)

        self.assertEqual(heap.getroot().key, 0)
        self.assertEqual(heap.isBinaryTreeMinHeap(), True)

    def test_fichier_SuppMin(self):
        """
        OK log(n), log(1)
            """
        l1_dic = FileReader()

        a = {}
        for type_file in l1_dic.keys():
            old_val = 0
            for i in range(0, 5 * int(type_file), int(type_file)):
                h = BinaryTreeMinHeap()
                h.ConsIter(l1_dic[type_file][old_val:(i + int(type_file))])
                startC = time.time()
                min_value = h.deleteMin()
                endC = time.time() - startC
                self.assertEqual(h.isBinaryTreeMinHeap(), True)
                h.insert(min_value)
                self.assertEqual(h.isBinaryTreeMinHeap(), True)
                try:
                    a[type_file] += endC
                except:
                    a[type_file] = endC
                old_val = i + int(type_file)

        for ele in a.keys():
            a[ele] /= 5

        sortDic = OrderedDict(sorted(a.items(), key=lambda x: int(x[0])))

        pprint.pprint(sortDic)

        plot(sortDic, name='BinaryTreeMinHeap_deleteMin')

    def test_fichier_Insert(self):
        """
        OK <log(n) | log(1)
        """
        l1_dic = FileReader()

        a = {}
        for type_file in l1_dic.keys():
            old_val = 0
            for i in range(0, 5 * int(type_file), int(type_file)):
                h = BinaryTreeMinHeap()
                startC = time.time()
                for elem in l1_dic[type_file][old_val:(i + int(type_file))]:
                    h.insert(elem)
                endC = time.time() - startC
                endC /= len(l1_dic[type_file][old_val:(i + int(type_file))])
                self.assertEqual(h.isBinaryTreeMinHeap(), True)
                try:
                    a[type_file] += endC
                except:
                    a[type_file] = endC
                old_val = i + int(type_file)

        for ele in a.keys():
            a[ele] /= 5

        sortDic = OrderedDict(sorted(a.items(), key=lambda x: int(x[0])))

        pprint.pprint(sortDic)

        plot(sortDic, name="BinaryTreeMinHeap_Insert")

    def test_fichier_ConstIter(self):
        """
        OK ~ O(n) un peu moins
        """
        l1_dic = FileReader()

        a = {}
        for type_file in l1_dic.keys():
            old_val = 0
            for i in range(0, 5 * int(type_file), int(type_file)):
                h = BinaryTreeMinHeap()

                # contruction de la arbre binaire avec tous les éléments sans se soucier de la contrainte d'ordre
                h.ajout_simple(l1_dic[type_file][old_val:(i + int(type_file))])

                startC = time.time()
                h.ConsIter(is_tree=True, ajout_simple=False)
                endC = time.time() - startC
                self.assertEqual(h.isBinaryTreeMinHeap(), True)
                try:
                    a[type_file] += endC
                except:
                    a[type_file] = endC
                old_val = i + int(type_file)

        for ele in a.keys():
            a[ele] /= 5

        sortDic = OrderedDict(sorted(a.items(), key=lambda x: int(x[0])))

        pprint.pprint(sortDic)

        plot(sortDic, name="BinaryTreeMinHeap_ConstIter")

    def test_fichier_Merge(self):
        """
        OK
        """
        l1_dic = FileReader()

        a = {}
        l2_dic = list(l1_dic.keys())

        l2_dic.reverse()
        for type_file1, type_file2 in zip(l1_dic.keys(), l2_dic):
            old_val1 = 0
            old_val2 = 0
            for i, j in zip(range(0, 5 * int(type_file1), int(type_file1)),
                            range(0, 5 * int(type_file2), int(type_file2))):
                h1 = BinaryTreeMinHeap()
                h2 = BinaryTreeMinHeap()
                h1.ConsIter(l1_dic[type_file1][old_val1:(i + int(type_file1))])
                h2.ConsIter(l1_dic[type_file2][old_val2:(j + int(type_file2))])
                startC = time.time()
                h1 = h1.Union(h2)
                endC = time.time() - startC
                h1.isBinaryTreeMinHeap()
                try:
                    a[str(int(type_file1) + int(type_file2))] += endC
                except:
                    a[str(int(type_file1) + int(type_file2))] = endC
                old_val1 = i + int(type_file1)
                old_val2 = i + int(type_file2)

        for ele in a.keys():
            a[ele] /= 5
        pprint.pprint(a)

        sortDic = OrderedDict(sorted(a.items(), key=lambda x: int(x[0])))

        plot(sortDic, name="BinaryTreeMinHeap_Merge")

    def test_fichier_MergeALL(self):
        """
        OK   log(m*log(n+m) ; (m<n)
        """

        l1_dic = FileReader()

        a = {}
        nb_foreach_file = {}
        for type_file1 in l1_dic.keys():
            for type_file2 in l1_dic.keys():
                old_val = 0
                old_val2 = 0
                for i, j in zip(range(0, 5 * int(type_file1), int(type_file1)),
                                range(0, 5 * int(type_file2), int(type_file2))):
                    h1 = BinaryTreeMinHeap()
                    h2 = BinaryTreeMinHeap()
                    len_file = str(int(type_file1) + int(type_file2))
                    h1.ConsIter(l1_dic[type_file1][old_val:(i + int(type_file1))])
                    h2.ConsIter(l1_dic[type_file1][old_val2:(i + int(type_file2))])

                    startC = time.time()
                    h1 = h1.Union(h2)
                    endC = time.time() - startC
                    h1.isBinaryTreeMinHeap()
                    try:
                        nb_foreach_file[len_file] += 1
                        a[len_file] += endC
                    except:
                        nb_foreach_file[len_file] = 1
                        a[len_file] = endC
                    old_val = i + int(type_file1)
                    old_val2 = i + int(type_file2)

        for f in a.keys():
            a[f] /= nb_foreach_file[f]

        sortDic = OrderedDict(sorted(a.items(), key=lambda x: int(x[0])))

        pprint.pprint(sortDic)
        plot(sortDic, name="BinaryTreeMinHeap_MergeALL")
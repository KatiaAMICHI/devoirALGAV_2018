import pprint
import sys
import time
import unittest
from collections import OrderedDict

from src.main.FileReader import FileReader, plot
from src.main.binomialHeap import binomialHeap

if sys.version_info.major == 2:
    pass
else:
    pass


class BinomialHeapTest(unittest.TestCase):
    def test_size_1(self):
        h = binomialHeap.BinomialHeap()
        h.insert(3)
        print('nn : ', h.head.next.rank)
        h.is_binomialheap()
        self.assertEqual(1, len(h))
        self.assertEqual(3, h.get_min_value())
        self.assertEqual(3, h.delete_min())
        h.is_binomialheap()
        self.assertEqual(0, len(h))

    def test_size_2(self):
        h = binomialHeap.BinomialHeap()
        h.insert(3)
        h.insert(0)
        h.is_binomialheap()
        self.assertEqual(2, len(h))
        self.assertEqual(0, h.get_min_value())
        self.assertEqual(0, h.delete_min())

        self.assertEqual(1, len(h))
        self.assertEqual(3, h.get_min_value())
        self.assertEqual(3, h.delete_min())
        h.is_binomialheap()
        self.assertEqual(0, len(h))
        print('-----------------------------------------')

    def test_merge(self):
        h1 = binomialHeap.BinomialHeap()
        h1.insert(3)
        h1.insert(2)
        h2 = binomialHeap.BinomialHeap()
        h2.insert(1)
        h2.insert(9)
        h1.merge(h2)
        self.assertEqual(4, len(h1))
        h1.is_binomialheap()

    def test_ConsIter_int(self):
        h = binomialHeap.BinomialHeap()
        h.ConsIter([3, 19, 10, 2, 4, 6, 7, 8, 1, 0, 11, 34])
        self.assertEqual(12, len(h))
        self.assertEqual(2, len(h.get_children()))
        self.assertEqual(2, h.get_children()[0].rank)
        self.assertEqual(3, h.get_children()[1].rank)

    def test_fichier_SuppMin(self):
        """
        OK == log(n)
        """
        l1_dic = FileReader()

        a = {}
        nb_foreach_file = {}
        for type_file in l1_dic.keys():
            old_val = 0
            for i in range(0, 5 * int(type_file), int(type_file)):
                h = binomialHeap.BinomialHeap()
                h.ConsIter(l1_dic[type_file][old_val:(i + int(type_file))])
                min_value = h.get_min_value()

                startC = time.time()
                delete_min_value = h.delete_min()
                endC = time.time() - startC

                self.assertEqual(delete_min_value, min_value)

                h.is_binomialheap()
                h.insert(l1_dic[type_file][old_val:(i + int(type_file))][0])
                h.delete_min()
                h.is_binomialheap()

                try:
                    nb_foreach_file[type_file] += 1
                    a[type_file] += endC
                except:
                    nb_foreach_file[type_file] = 1
                    a[type_file] = endC
                old_val = i + int(type_file)

        for ele in a.keys():
            a[ele] /= nb_foreach_file[ele]

        sortDic = OrderedDict(sorted(a.items(), key=lambda x: int(x[0])))
        pprint.pprint(sortDic)

        plot(sortDic, name='BinomialHeap_SuppMin')

    def test_fichier_Ajout(self):
        """
        OK ~ O(1) | << O(log(n))
        """
        l1_dic = FileReader()

        a = {}
        nb_foreach_file = {}

        for type_file in l1_dic.keys():
            old_val = 0
            for i in range(0, 5 * int(type_file), int(type_file)):

                h = binomialHeap.BinomialHeap()
                startC = time.time()
                for ele in l1_dic[type_file][old_val:(i + int(type_file))]:
                    h.insert(ele)
                endC = time.time() - startC
                endC /= len(l1_dic[type_file][old_val:(i + int(type_file))])
                h.is_binomialheap()
                try:
                    nb_foreach_file[type_file] += 1
                    a[type_file] += endC
                except:
                    nb_foreach_file[type_file] = 1
                    a[type_file] = endC
                old_val = i + int(type_file)

        for ele in a.keys():
            a[ele] /= nb_foreach_file[ele]

        sortDic = OrderedDict(sorted(a.items(), key=lambda x: int(x[0])))

        pprint.pprint(sortDic)

        plot(sortDic, name='BinomialHeap_Ajout')

    def test_fichier_ConsIter(self):
        """
        OK ~< O(n)
        """

        l1_dic = FileReader()

        nb_foreach_file = {}
        a = {}
        for type_file in l1_dic.keys():
            old_val = 0
            for i in range(0, 5 * int(type_file), int(type_file)):
                h = binomialHeap.BinomialHeap()
                startC = time.time()
                h.ConsIter(l1_dic[type_file][old_val:(i + int(type_file))])
                endC = time.time() - startC
                h.is_binomialheap()
                try:
                    nb_foreach_file[type_file] += 1
                    a[type_file] += endC
                except:
                    nb_foreach_file[type_file] = 1
                    a[type_file] = endC
                old_val = i + int(type_file)

        for f in a.keys():
            a[f] /= nb_foreach_file[f]

        sortDic = OrderedDict(sorted(a.items(), key=lambda x: int(x[0])))

        pprint.pprint(sortDic)
        plot(sortDic, name='BinomialHeap_ConsIter')

    def test_fichier_Merge(self):
        """
        OK
        """
        l1_dic = FileReader()

        a = {}
        l2_dic = list(l1_dic.keys())
        nb_foreach_file = {}

        l2_dic.reverse()
        for type_file1, type_file2 in zip(l1_dic.keys(), l2_dic):
            old_val1 = 0
            old_val2 = 0
            for i, j in zip(range(0, 5 * int(type_file1), int(type_file1)),
                            range(0, 5 * int(type_file2), int(type_file2))):
                len_file = str(int(type_file1) + int(type_file2))

                h1 = binomialHeap.BinomialHeap()
                h2 = binomialHeap.BinomialHeap()
                h1.ConsIter(l1_dic[type_file1][old_val1:(i + int(type_file1))])
                h2.ConsIter(l1_dic[type_file2][old_val2:(j + int(type_file2))])
                startC = time.time()
                h1.merge(h2)
                endC = time.time() - startC
                h1.is_binomialheap()
                try:
                    nb_foreach_file[len_file] += 1
                    a[len_file] += endC
                except:
                    nb_foreach_file[len_file] = 1
                    a[str(int(type_file1) + int(type_file2))] = endC
                old_val1 = i + int(type_file1)
                old_val2 = i + int(type_file2)

        for ele in a.keys():
            a[ele] /= nb_foreach_file[ele]

        sortDic = OrderedDict(sorted(a.items(), key=lambda x: int(x[0])))

        pprint.pprint(sortDic)
        plot(sortDic, name='BinomialHeap_Merge')

    def test_fichier_MergeALL(self):
        """
        OK     O(1), O(log(n))
        """

        l1_dic = FileReader()

        a = {}
        nb_foreach_file = {}
        for type_file in l1_dic.keys():
            for type_file2 in l1_dic.keys():
                old_val = 0
                old_val2 = 0
                for i, j in zip(range(0, 5 * int(type_file), int(type_file)),
                                range(0, 5 * int(type_file2), int(type_file2))):
                    h = binomialHeap.BinomialHeap()
                    h2 = binomialHeap.BinomialHeap()
                    len_file = str(int(type_file) + int(type_file2))
                    h.ConsIter(l1_dic[type_file][old_val:(i + int(type_file))])
                    h2.ConsIter(l1_dic[type_file2][old_val2:(j + int(type_file2))])

                    startC = time.time()
                    h.merge(h2)
                    endC = time.time() - startC
                    h.is_binomialheap()
                    try:
                        nb_foreach_file[len_file] += 1
                        a[len_file] += endC
                    except:
                        nb_foreach_file[len_file] = 1
                        a[len_file] = endC
                    old_val = i + int(type_file)
                    old_val2 = i + int(type_file2)

        for f in a.keys():
            a[f] /= nb_foreach_file[f]

        sortDic = OrderedDict(sorted(a.items(), key=lambda x: int(x[0])))

        pprint.pprint(sortDic)
        plot(sortDic, name='BinomialHeap_MergeALL')
# TODO nb_foreach_file[f]

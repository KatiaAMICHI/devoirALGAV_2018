import sys
import unittest
import time
import pprint
import numpy as np

from collections import OrderedDict

from bokeh.plotting import figure, show

from src.main.FileReader import FileReader, plot

if sys.version_info.major == 2:
    pass
else:
    pass

from src.main.heap.TreeMinHeap.BinaryTreeMinHeap import BinaryTreeMinHeap


# TODO après suppMin last n'est plus bon

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
                h.deleteMin()
                endC = time.time() - startC
                self.assertEqual(h.isBinaryTreeMinHeap(), True)
                try:
                    a[type_file] += endC
                except:
                    a[type_file] = endC
                old_val = i + int(type_file)

        for ele in a.keys():
            a[ele] /= 5

        sortDic = OrderedDict(a.items())
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

        sortDic = OrderedDict(a.items())
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

        sortDic = OrderedDict(a.items())
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

        sortDic = OrderedDict(a.items())

        p = figure(title="BinaryTreeMinHeap_insert", y_axis_type="log",
                   x_range=(0, 50000), y_range=(list(sortDic.values())[0], 2),
                   background_fill_color="#fafafa")

        p.line(list(sortDic.keys()), list(sortDic.values()), legend="y=sqrt(x)",
               line_color="tomato", line_dash="dashed")

        p.legend.location = "top_left"

        show(p)

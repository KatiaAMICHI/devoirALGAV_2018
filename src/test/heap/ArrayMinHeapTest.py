import pprint
import sys
import time
import unittest
import numpy as np
from collections import OrderedDict

from src.main.FileReader import FileReader
from src.main.heap.ArrayMinHeap import ArrayMinHeap
from bokeh.plotting import figure, show

if sys.version_info.major == 2:
    pass
else:
    pass


class ArrayMinHeapTeat(unittest.TestCase):
    def test_int_all(self):
        heap0 = ArrayMinHeap(int_key=True)
        heap4 = ArrayMinHeap(int_key=True)

        #        print("################insert#########################")

        heap0.insert(50)
        heap0.insert(23)
        heap0.insert(11)
        heap0.insert(30)
        heap0.insert(0)
        self.assertEqual(heap0.is_arrayMinHeap(), True)

        #        print("################ConsIter#########################")

        heap1 = ArrayMinHeap(heap_array=[50, 23, 11, 30, 0])
        heap2 = ArrayMinHeap(heap_array=[50, 23, 11, 30, 0])

        heap1.ConsIterTab()
        heap2.ConsIterTab(sort=False)

        self.assertEqual(heap1.is_arrayMinHeap(), True)
        self.assertEqual(heap2.is_arrayMinHeap(), False)

        #        print("################Union#########################")

        heap = ArrayMinHeap(heap_array=[5, 3, 1, 39, 6])

        heap.ConsIterTab()
        self.assertEqual(heap.is_arrayMinHeap(), True)
        self.assertEqual(heap1.is_arrayMinHeap(), True)
        heap.Union(heap1)

        self.assertEqual(heap.is_arrayMinHeap(), True)
        self.assertEqual(heap.size, 10)

        #        print("################Delete#########################")
        heap4.ConsIterTab([50, 23, 11, 0])
        self.assertEqual(heap4.is_arrayMinHeap(), True)
        self.assertEqual(heap4.get_min(), 0)
        self.assertEqual(heap4.delete_min(), 0)
        self.assertEqual(heap4.get_min(), 11)
        self.assertEqual(heap4.size, 3)
        self.assertEqual(heap4.is_arrayMinHeap(), True)

    def test_fichier_SuppMin(self):
        """
        OK
        """
        l1_dic = FileReader()

        a = {}
        for type_file in l1_dic.keys():
            old_val = 0
            for i in range(0, 5 * int(type_file), int(type_file)):
                h = ArrayMinHeap()
                h.ConsIterTab(list_elem=l1_dic[type_file][old_val:(i + int(type_file))])
                startC = time.time()
                h.delete_min()
                endC = time.time() - startC
                self.assertEqual(h.is_arrayMinHeap(), True)
                try:
                    a[type_file] += endC
                except:
                    a[type_file] = endC
                old_val = i + int(type_file)

        for ele in a.keys():
            a[ele] /= 5
        pprint.pprint(a)

        sortDic = OrderedDict(a.items())

        p = figure(title="ArrayMinHeap-Delete", y_axis_type="log",
                   x_range=(0, 50000), y_range=(list(sortDic.values())[0], 2),
                   background_fill_color="#fafafa")

        p.line(list(sortDic.keys()), list(sortDic.values()), legend="y=sqrt(x)",
               line_color="tomato", line_dash="dashed")

        p.legend.location = "top_left"

        show(p)

    def test_fichier_Insert(self):
        """
        """

        l1_dic = FileReader()

        a = {}
        for type_file in l1_dic.keys():
            old_val = 0
            for i in range(0, 5 * int(type_file), int(type_file)):
                h = ArrayMinHeap()
                startC = time.time()
                for elem in l1_dic[type_file][old_val:(i + int(type_file))]:
                    h.insert(elem)
                endC = time.time() - startC
                self.assertEqual(h.is_arrayMinHeap(), True)
                try:
                    a[type_file] += endC
                except:
                    a[type_file] = endC
                old_val = i + int(type_file)

        for ele in a.keys():
            a[ele] /= 5
        pprint.pprint(a)

        sortDic = OrderedDict(a.items())

        p = figure(title="ArrayMinHeap-Insert", y_axis_type="log",
                   x_range=(0, 50000), y_range=(list(sortDic.values())[0], 2),
                   background_fill_color="#fafafa")

        p.line(list(sortDic.keys()), list(sortDic.values()), legend="y=sqrt(x)",
               line_color="tomato", line_dash="dashed")

        p.legend.location = "top_left"

        show(p)

    def test_fichier_ConstIter(self):
        """
        OK
        """
        l1_dic = FileReader()

        a = {}
        for type_file in l1_dic.keys():
            old_val = 0
            for i in range(0, 5 * int(type_file), int(type_file)):
                h = ArrayMinHeap()
                startC = time.time()
                h.ConsIterTab(list_elem=l1_dic[type_file][old_val:(i + int(type_file))])
                endC = time.time() - startC
                self.assertEqual(h.is_arrayMinHeap(), True)
                try:
                    a[type_file] += endC
                except:
                    a[type_file] = endC
                old_val = i + int(type_file)

        for ele in a.keys():
            a[ele] /= 5

        sortDic = OrderedDict(a.items())
        pprint.pprint(sortDic)

        p = figure(title="ArrayMinHeap-ConsIter", y_axis_type="log",
                   x_range=(0, 50000), y_range=(list(sortDic.values())[0], 2),
                   background_fill_color="#fafafa")

        p.line(list(sortDic.keys()), list(sortDic.values()), legend="y=sqrt(x)",
               line_color="tomato", line_dash="dashed")

        p.legend.location = "top_left"

        show(p)

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
                h1 = ArrayMinHeap()
                h2 = ArrayMinHeap()
                h1.ConsIterTab(l1_dic[type_file1][old_val1:(i + int(type_file1))])
                h2.ConsIterTab(l1_dic[type_file2][old_val2:(j + int(type_file2))])
                startC = time.time()
                h1 = h1.Union(h2)
                endC = time.time() - startC
                self.assertEqual(h1.is_arrayMinHeap(), True)

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

        p = figure(title="ArrayMinHeap-Insert", y_axis_type="log",
                   x_range=(0, 50000), y_range=(list(sortDic.values())[0], 2),
                   background_fill_color="#fafafa")

        p.line(list(sortDic.keys()), list(sortDic.values()), legend="y=sqrt(x)",
               line_color="tomato", line_dash="dashed")

        p.legend.location = "top_left"

        show(p)

import pprint
import random
import sys
import time
import unittest
from collections import OrderedDict

from bokeh.plotting import figure, show

from src.main.FileReader import FileReader, plot
from src.main.searchTree.AVLTree import AVLTree

if sys.version_info.major == 2:
    pass
else:
    pass


class MyTestCase(unittest.TestCase):
    def test_insert_int(self):
        """
        ok
        """
        tree = AVLTree()
        liste_elem1 = [50, 30, 70, 20, 40, 60, 80]

        for ele in liste_elem1:
            tree.insert(ele)

        self.assertEqual(tree.getheight(), 2)
        self.assertEqual(tree.getbalance(), 0)
        tree.is_avltree()

    def test_search_delete_int(self):
        """
        ok
        """
        tree = AVLTree()
        liste_elem1 = [50, 30, 70, 20, 40, 60, 80]

        for ele in liste_elem1:
            tree.insert(ele, sort=True)
        print(tree.print_pre_tree())
        print('hethright : ', tree.getheight())
        self.assertEqual(tree.getheight(), 2)
        self.assertEqual(tree.getbalance(), 0)
        self.assertEqual(tree.search(60), True)
        tree.delete_value(60)
        self.assertEqual(tree.search(60), False)
        tree.is_avltree()

    def test_fichier_Search(self):
        """
        OK ~ log(n)
        """
        l1_dic = FileReader()

        a = {}
        nb_foreach_file = {}

        for type_file in l1_dic.keys():
            old_val = 0
            for i in range(0, 5 * int(type_file), int(type_file)):
                h = AVLTree()

                h.ConsIter(l1_dic[type_file][old_val:(i + int(type_file))])

                delete_index_rand = random.randint(0, len(l1_dic[type_file][old_val:(i + int(type_file))]) - 1)
                value_to_delete = l1_dic[type_file][old_val:(i + int(type_file))][delete_index_rand]

                startC = time.time()
                h.search(value_to_delete)
                endC = time.time() - startC
                self.assertEqual(h.search(value_to_delete), True)

                h.delete_value(value_to_delete)
                self.assertEqual(h.search(value_to_delete), False)

                h.is_avltree()
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
        plot(sortDic, name="AVLTree_Recheche")

    def test_fichier_Search_Delete(self):
        """
        OK O(log(n)) | O(1)
        """
        l1_dic = FileReader()

        a = {}
        nb_foreach_file = {}

        for type_file in l1_dic.keys():
            old_val = 0
            for i in range(0, 5 * int(type_file), int(type_file)):
                h = AVLTree()
                h.ConsIter(l1_dic[type_file][old_val:(i + int(type_file))])

                delete_index_rand = random.randint(0, len(l1_dic[type_file][old_val:(i + int(type_file))]) - 1)
                value_to_delete = l1_dic[type_file][old_val:(i + int(type_file))][delete_index_rand]

                self.assertEqual(h.search(value_to_delete), True)

                startC = time.time()
                h.delete_value(value_to_delete)
                endC = time.time() - startC
                h.is_avltree()

                self.assertEqual(h.search(value_to_delete), False)

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
        plot(sortDic, name="AVL_tree_SuppElement")

    def test_fichier_Insert(self):
        """
        OK ~ O(log(n)
        """
        l1_dic = FileReader()

        a = {}
        nb_foreach_file = {}
        for type_file in l1_dic.keys():
            old_val = 0
            for i in range(0, 5 * int(type_file), int(type_file)):
                h = AVLTree()
                startC = time.time()
                for ele in l1_dic[type_file][old_val:(i + int(type_file))]:
                    h.insert(ele, sort=True)
                endC = time.time() - startC
                endC /= len(l1_dic[type_file][old_val:(i + int(type_file))])
                h.is_avltree()
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
        plot(sortDic, name="AVLTree_Ajout")

    def test_fichier_ConstIter(self):
        """
        OK ~ n*log(n)
        """
        l1_dic = FileReader()

        a = {}
        nb_foreach_file = {}
        for type_file in l1_dic.keys():
            old_val = 0
            for i in range(0, 5 * int(type_file), int(type_file)):
                h = AVLTree()
                startC = time.time()
                h.ConsIter(l1_dic[type_file][old_val:(i + int(type_file))])
                endC = time.time() - startC
                h.is_avltree()
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

        plot(sortDic, name="AVLTree")

    def test_fichier_Merge(self):
        """
        OK
        """
        l1_dic = FileReader()

        a = {}
        l2_dic = list(l1_dic.keys())

        l2_dic.reverse()
        nb_foreach_file = {}

        for type_file1, type_file2 in zip(l1_dic.keys(), l2_dic):
            old_val1 = 0
            old_val2 = 0
            for i, j in zip(range(0, 5 * int(type_file1), int(type_file1)),
                            range(0, 5 * int(type_file2), int(type_file2))):
                h1 = AVLTree()
                h2 = AVLTree()
                h1.ConsIter(l1_dic[type_file1][old_val1:(i + int(type_file1))])
                h2.ConsIter(l1_dic[type_file2][old_val2:(j + int(type_file2))])

                startC = time.time()
                h1 = h1.Union(h2)
                endC = time.time() - startC

                h1.is_avltree()
                try:
                    nb_foreach_file[str(int(type_file1) + int(type_file2))] += 1
                    a[str(int(type_file1) + int(type_file2))] += endC
                except:
                    nb_foreach_file[str(int(type_file1) + int(type_file2))] = 1
                    a[str(int(type_file1) + int(type_file2))] = endC
                old_val1 = i + int(type_file1)
                old_val2 = i + int(type_file2)

        for ele in a.keys():
            a[ele] /= nb_foreach_file[ele]
        pprint.pprint(a)

        sortDic = OrderedDict(sorted(a.items(), key=lambda x: int(x[0])))
        plot(sortDic, name="AVLTree_Union")

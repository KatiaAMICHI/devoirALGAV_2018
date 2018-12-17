import time
from collections import OrderedDict

from src.main.FileReader import Shakespeare, FileReader, plot, plot3
from src.main.binomialHeap import binomialHeapV2
from src.main.binomialHeap.binomialHeapV2 import BinomialHeap
from src.main.heap.ArrayMinHeap import ArrayMinHeap
from src.main.heap.TreeMinHeap.BinaryTreeMinHeap import BinaryTreeMinHeap
from src.main.searchTree.AVLTree import AVLTree
import sys

if sys.version_info.major == 2:
    pass
else:
    pass
from src.main.hach.MD5 import MD5
import pprint


def collisonShakespeare():
    tree = AVLTree()
    words = Shakespeare()
    md5 = MD5()
    word_dic = {}

    for word in words:
        tree.insert(md5.md5_to_hex(md5.md5(word.encode())))

    new_list_words = list(set(words))

    for word in new_list_words:
        md5_word = md5.md5_to_hex(md5.md5(bytes(word.encode())))
        if tree.search(md5_word):
            try:
                word_dic[md5_word].append(word)
            except:
                word_dic[md5_word] = [word]

    pprint.pprint(word_dic)
    for a in word_dic.keys():
        if len(word_dic[a]) < 1:
            print('a : ', a, 'word : ', word_dic[a])


def SuppMin_Tas_File():
    """
           OK
            """
    l1_dic = FileReader()

    a_binarytreeminHeap = {}
    a_arrayminheap = {}
    a_binomialheap = {}
    for type_file in l1_dic.keys():
        old_val = 0
        for i in range(0, 5 * int(type_file), int(type_file)):

            # BinaryTreeMinHeap
            binarytreeminHeap = BinaryTreeMinHeap()
            binarytreeminHeap.ConsIter(l1_dic[type_file][old_val:(i + int(type_file))])
            startC_binarytreeminHeap = time.time()
            binarytreeminHeap.deleteMin()
            endC_binarytreeminHeap = time.time() - startC_binarytreeminHeap
            assert binarytreeminHeap.isBinaryTreeMinHeap() is True

            # ArrayMinHeap
            arrayminheap = ArrayMinHeap()
            arrayminheap.ConsIterTab(list_elem=l1_dic[type_file][old_val:(i + int(type_file))])
            startC_arrayminheap = time.time()
            arrayminheap.delete_min()
            endC_arrayminheap = time.time() - startC_arrayminheap
            assert arrayminheap.is_arrayMinHeap() is True

            # BinaryTreeMinHeap
            binomialheap = BinomialHeap()
            binomialheap.ConsIter(l1_dic[type_file][old_val:(i + int(type_file))])
            min_value = binomialheap.get_min_value()
            startC_binomialheap = time.time()
            delete_min_value = binomialheap.delete_min()
            endC_binomialheap = time.time() - startC_binomialheap

            try:
                a_binarytreeminHeap[type_file] += endC_binarytreeminHeap
                a_arrayminheap[type_file] += endC_arrayminheap
                a_binomialheap[type_file] += endC_binomialheap
            except:
                a_binarytreeminHeap[type_file] = endC_binarytreeminHeap
                a_arrayminheap[type_file] = endC_arrayminheap
                a_binomialheap[type_file] = endC_binomialheap

            old_val = i + int(type_file)

    for e1, e2, e3 in zip(a_binarytreeminHeap.keys(), a_arrayminheap.keys(), a_binomialheap):
        a_binarytreeminHeap[e1] /= 5
        a_arrayminheap[e2] /= 5
        a_binomialheap[e3] /= 5

    sortDic_binarytreeminHeap = OrderedDict(a_binarytreeminHeap.items())
    sortDic_arrayminheap = OrderedDict(a_arrayminheap.items())
    sortDic_binomialheap = OrderedDict(a_binomialheap.items())
    pprint.pprint(sortDic_binarytreeminHeap)
    pprint.pprint(sortDic_arrayminheap)
    pprint.pprint(sortDic_binomialheap)

    plot3(sortDic_binarytreeminHeap, sortDic_arrayminheap, sortDic_binomialheap, n1='BinaryTreeMinHeap',
          n2='ArrayMinHeap',
          n3='BinomialHeap')


def Ajout_Tas_File():
    """
    OK
    """
    l1_dic = FileReader()

    a_binarytreeminHeap = {}
    a_arrayminheap = {}
    a_binomialheap = {}
    for type_file in l1_dic.keys():
        old_val = 0
        for i in range(0, 5 * int(type_file), int(type_file)):

            # BinaryTreeMinHeap
            binarytreeminHeap = BinaryTreeMinHeap()
            binarytreeminHeap.ConsIter(l1_dic[type_file][old_val:(i + int(type_file))])
            startC_binarytreeminHeap = time.time()
            for elem in l1_dic[type_file][old_val:(i + int(type_file))]:
                binarytreeminHeap.insert(elem)
            endC_binarytreeminHeap = time.time() - startC_binarytreeminHeap
            endC_binarytreeminHeap /= len(l1_dic[type_file][old_val:(i + int(type_file))])
            #assert binarytreeminHeap.isBinaryTreeMinHeap() is True

            # ArrayMinHeap
            arrayminheap = ArrayMinHeap()
            arrayminheap.ConsIterTab(list_elem=l1_dic[type_file][old_val:(i + int(type_file))])
            startC_arrayminheap = time.time()
            for elem in l1_dic[type_file][old_val:(i + int(type_file))]:
                arrayminheap.insert(elem)
            endC_arrayminheap = time.time() - startC_arrayminheap
            endC_arrayminheap/= len(l1_dic[type_file][old_val:(i + int(type_file))])
            #assert arrayminheap.is_arrayMinHeap() is True

            # BinaryTreeMinHeap
            binomialheap = BinomialHeap()
            binomialheap.ConsIter(l1_dic[type_file][old_val:(i + int(type_file))])
            startC_binomialheap = time.time()
            for elem in l1_dic[type_file][old_val:(i + int(type_file))]:
                binomialheap.insert(elem)
            endC_binomialheap = time.time() - startC_binomialheap
            endC_binomialheap /= len(l1_dic[type_file][old_val:(i + int(type_file))])

            try:
                a_binarytreeminHeap[type_file] += endC_binarytreeminHeap
                a_arrayminheap[type_file] += endC_arrayminheap
                a_binomialheap[type_file] += endC_binomialheap
            except:
                a_binarytreeminHeap[type_file] = endC_binarytreeminHeap
                a_arrayminheap[type_file] = endC_arrayminheap
                a_binomialheap[type_file] = endC_binomialheap

            old_val = i + int(type_file)

    for e1, e2, e3 in zip(a_binarytreeminHeap.keys(), a_arrayminheap.keys(), a_binomialheap):
        a_binarytreeminHeap[e1] /= 5
        a_arrayminheap[e2] /= 5
        a_binomialheap[e3] /= 5

    sortDic_binarytreeminHeap = OrderedDict(a_binarytreeminHeap.items())
    sortDic_arrayminheap = OrderedDict(a_arrayminheap.items())
    sortDic_binomialheap = OrderedDict(a_binomialheap.items())
    pprint.pprint(sortDic_binarytreeminHeap)
    pprint.pprint(sortDic_arrayminheap)
    pprint.pprint(sortDic_binomialheap)

    plot3(sortDic_binarytreeminHeap, sortDic_arrayminheap, sortDic_binomialheap, n1='BinaryTreeMinHeap',
          n2='ArrayMinHeap',
          n3='BinomialHeap')

def Ajout_Tas_File():
    """
    OK
    """
    l1_dic = FileReader()

    a_binarytreeminHeap = {}
    a_arrayminheap = {}
    a_binomialheap = {}
    for type_file in l1_dic.keys():
        old_val = 0
        for i in range(0, 5 * int(type_file), int(type_file)):

            # BinaryTreeMinHeap
            binarytreeminHeap = BinaryTreeMinHeap()
            binarytreeminHeap.ConsIter(l1_dic[type_file][old_val:(i + int(type_file))])
            startC_binarytreeminHeap = time.time()
            for elem in l1_dic[type_file][old_val:(i + int(type_file))]:
                binarytreeminHeap.insert(elem)
            endC_binarytreeminHeap = time.time() - startC_binarytreeminHeap
            endC_binarytreeminHeap /= len(l1_dic[type_file][old_val:(i + int(type_file))])
            #assert binarytreeminHeap.isBinaryTreeMinHeap() is True

            # ArrayMinHeap
            arrayminheap = ArrayMinHeap()
            arrayminheap.ConsIterTab(list_elem=l1_dic[type_file][old_val:(i + int(type_file))])
            startC_arrayminheap = time.time()
            for elem in l1_dic[type_file][old_val:(i + int(type_file))]:
                arrayminheap.insert(elem)
            endC_arrayminheap = time.time() - startC_arrayminheap
            endC_arrayminheap/= len(l1_dic[type_file][old_val:(i + int(type_file))])
            #assert arrayminheap.is_arrayMinHeap() is True

            # BinaryTreeMinHeap
            binomialheap = BinomialHeap()
            binomialheap.ConsIter(l1_dic[type_file][old_val:(i + int(type_file))])
            startC_binomialheap = time.time()
            for elem in l1_dic[type_file][old_val:(i + int(type_file))]:
                binomialheap.insert(elem)
            endC_binomialheap = time.time() - startC_binomialheap
            endC_binomialheap /= len(l1_dic[type_file][old_val:(i + int(type_file))])

            try:
                a_binarytreeminHeap[type_file] += endC_binarytreeminHeap
                a_arrayminheap[type_file] += endC_arrayminheap
                a_binomialheap[type_file] += endC_binomialheap
            except:
                a_binarytreeminHeap[type_file] = endC_binarytreeminHeap
                a_arrayminheap[type_file] = endC_arrayminheap
                a_binomialheap[type_file] = endC_binomialheap

            old_val = i + int(type_file)

    for e1, e2, e3 in zip(a_binarytreeminHeap.keys(), a_arrayminheap.keys(), a_binomialheap):
        a_binarytreeminHeap[e1] /= 5
        a_arrayminheap[e2] /= 5
        a_binomialheap[e3] /= 5

    sortDic_binarytreeminHeap = OrderedDict(a_binarytreeminHeap.items())
    sortDic_arrayminheap = OrderedDict(a_arrayminheap.items())
    sortDic_binomialheap = OrderedDict(a_binomialheap.items())
    pprint.pprint(sortDic_binarytreeminHeap)
    pprint.pprint(sortDic_arrayminheap)
    pprint.pprint(sortDic_binomialheap)

    plot3(sortDic_binarytreeminHeap, sortDic_arrayminheap, sortDic_binomialheap, n1='BinaryTreeMinHeap',
          n2='ArrayMinHeap',
          n3='BinomialHeap')

if __name__ == '__main__':
    a = "abc"
    # Question 6.12 / 6.13
    # collisonShakespeare()

    # Question 6.&4
    #SuppMin_Tas_File()
    Ajout_Tas_File()

import time
from collections import OrderedDict

from src.main.FileReader import Shakespeare, FileReader, plot, plot3, fichiers_ShakespeareMD5
from src.main.binomialHeap.binomialHeap import BinomialHeap
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


def collisonShakespeare(path=None):
    tree = AVLTree()
    words = Shakespeare(path=path)
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

    # pprint.pprint(word_dic)

    for a in word_dic.keys():
        if len(word_dic[a]) > 1:
            print('a : ', a, 'word : ', word_dic[a])
    print('Pas de collision')


def SuppMin_Tas_File():
    l1_dic = fichiers_ShakespeareMD5()

    a_binarytreeminHeap = {}
    a_arrayminheap = {}
    a_binomialheap = {}
    nb_file = {}
    for type_file in l1_dic.keys():

        # BinaryTreeMinHeap
        binarytreeminHeap = BinaryTreeMinHeap()
        binarytreeminHeap.ConsIter(l1_dic[type_file])
        startC_binarytreeminHeap = time.time()
        binarytreeminHeap.deleteMin()
        endC_binarytreeminHeap = time.time() - startC_binarytreeminHeap

        # ArrayMinHeap
        arrayminheap = ArrayMinHeap()
        arrayminheap.ConsIterTab(list_elem=l1_dic[type_file])
        startC_arrayminheap = time.time()
        arrayminheap.delete_min()
        endC_arrayminheap = time.time() - startC_arrayminheap
        assert arrayminheap.is_arrayMinHeap() is True

        # BinaryTreeMinHeap
        binomialheap = BinomialHeap()
        binomialheap.ConsIter(l1_dic[type_file])
        min_value = binomialheap.get_min_value()
        startC_binomialheap = time.time()
        delete_min_value = binomialheap.delete_min()
        endC_binomialheap = time.time() - startC_binomialheap

        try:
            nb_file[type_file] += 1
            a_binarytreeminHeap[type_file] += endC_binarytreeminHeap
            a_arrayminheap[type_file] += endC_arrayminheap
            a_binomialheap[type_file] += endC_binomialheap
        except:
            nb_file[type_file] = 1
            a_binarytreeminHeap[type_file] = endC_binarytreeminHeap
            a_arrayminheap[type_file] = endC_arrayminheap
            a_binomialheap[type_file] = endC_binomialheap

    for e1, e2, e3 in zip(a_binarytreeminHeap.keys(), a_arrayminheap.keys(), a_binomialheap):
        a_binarytreeminHeap[e1] /= nb_file[e1]
        a_arrayminheap[e2] /= nb_file[e1]
        a_binomialheap[e3] /= nb_file[e1]

    sortDic_binarytreeminHeap = OrderedDict(sorted(a_binarytreeminHeap.items(), key=lambda x: int(x[0])))
    sortDic_arrayminheap = OrderedDict(sorted(a_arrayminheap.items(), key=lambda x: int(x[0])))
    sortDic_binomialheap = OrderedDict(sorted(a_binomialheap.items(), key=lambda x: int(x[0])))

    print("BinaryTreeMinHeap")
    pprint.pprint(sortDic_binarytreeminHeap)
    print("ArrayMinHeap")
    pprint.pprint(sortDic_arrayminheap)
    print("BinomialHeap")
    pprint.pprint(sortDic_binomialheap)

    plot3(sortDic_binarytreeminHeap, sortDic_arrayminheap, sortDic_binomialheap,
          n1='BinaryTreeMinHeap',
          n2='ArrayMinHeap',
          n3='BinomialHeap',
          name='Temps d\'exécution de SuppMin (supp element pour avl) sur les fichiers Shakespeare')


def Ajout_Tas_File():
    l1_dic = fichiers_ShakespeareMD5()

    a_binarytreeminHeap = {}
    a_arrayminheap = {}
    a_binomialheap = {}
    nb_file = {}
    for type_file in l1_dic.keys():

        # BinaryTreeMinHeap
        binarytreeminHeap = BinaryTreeMinHeap()
        binarytreeminHeap.ConsIter(l1_dic[type_file])
        startC_binarytreeminHeap = time.time()
        for elem in l1_dic[type_file]:
            binarytreeminHeap.insert(elem)
        endC_binarytreeminHeap = time.time() - startC_binarytreeminHeap
        endC_binarytreeminHeap /= len(l1_dic[type_file])
        assert binarytreeminHeap.isBinaryTreeMinHeap() is True

        # ArrayMinHeap
        arrayminheap = ArrayMinHeap()
        arrayminheap.ConsIterTab(list_elem=l1_dic[type_file])
        startC_arrayminheap = time.time()
        for elem in l1_dic[type_file]:
            arrayminheap.insert(elem)
        endC_arrayminheap = time.time() - startC_arrayminheap
        endC_arrayminheap /= len(l1_dic[type_file])
        # assert arrayminheap.is_arrayMinHeap() is True

        # BinaryTreeMinHeap
        binomialheap = BinomialHeap()
        binomialheap.ConsIter(l1_dic[type_file])
        startC_binomialheap = time.time()
        for elem in l1_dic[type_file]:
            binomialheap.insert(elem)
        endC_binomialheap = time.time() - startC_binomialheap
        endC_binomialheap /= len(l1_dic[type_file])

        try:
            nb_file[type_file] += 1
            a_binarytreeminHeap[type_file] += endC_binarytreeminHeap
            a_arrayminheap[type_file] += endC_arrayminheap
            a_binomialheap[type_file] += endC_binomialheap
        except:
            nb_file[type_file] = 1
            a_binarytreeminHeap[type_file] = endC_binarytreeminHeap
            a_arrayminheap[type_file] = endC_arrayminheap
            a_binomialheap[type_file] = endC_binomialheap

    for e1, e2, e3 in zip(a_binarytreeminHeap.keys(), a_arrayminheap.keys(), a_binomialheap):
        a_binarytreeminHeap[e1] /= type_file[e1]
        a_arrayminheap[e2] /= type_file[e1]
        a_binomialheap[e3] /= type_file[e1]

    sortDic_binarytreeminHeap = OrderedDict(sorted(a_binarytreeminHeap.items(), key=lambda x: int(x[0])))
    sortDic_arrayminheap = OrderedDict(sorted(a_arrayminheap.items(), key=lambda x: int(x[0])))
    sortDic_binomialheap = OrderedDict(sorted(a_binomialheap.items(), key=lambda x: int(x[0])))

    print("BinaryTreeMinHeap")
    pprint.pprint(sortDic_binarytreeminHeap)
    print("ArrayMinHeap")
    pprint.pprint(sortDic_arrayminheap)
    print("BinomialHeap")
    pprint.pprint(sortDic_binomialheap)

    plot3(sortDic_binarytreeminHeap, sortDic_arrayminheap, sortDic_binomialheap, n1='BinaryTreeMinHeap',
          n2='ArrayMinHeap',
          n3='BinomialHeap',
          name='Temps d\'exécution de Ajout sur les fichiers Shakespeare')


def ConstIter_Tas_File():
    """
    OK
    """
    l1_dic = fichiers_ShakespeareMD5()

    a_binarytreeminHeap = {}
    a_arrayminheap = {}
    a_binomialheap = {}
    for type_file in l1_dic.keys():
        for i in range(0, 5 * int(type_file), int(type_file)):

            # BinaryTreeMinHeap
            binarytreeminHeap = BinaryTreeMinHeap()
            binarytreeminHeap.ConsIter(l1_dic[type_file])
            startC_binarytreeminHeap = time.time()
            binarytreeminHeap.ConsIter(is_tree=True, ajout_simple=False)
            endC_binarytreeminHeap = time.time() - startC_binarytreeminHeap

            assert binarytreeminHeap.isBinaryTreeMinHeap() is True

            # ArrayMinHeap
            arrayminheap = ArrayMinHeap()
            arrayminheap.ajout_simple(list_elem=l1_dic[type_file])

            startC_arrayminheap = time.time()
            arrayminheap.ConsIterTab(ajout_simple=False)
            endC_arrayminheap = time.time() - startC_arrayminheap

            assert arrayminheap.is_arrayMinHeap() is True

            # BinaryTreeMinHeap
            binomialheap = BinomialHeap()
            startC_binomialheap = time.time()
            binomialheap.ConsIter(l1_dic[type_file])
            endC_binomialheap = time.time() - startC_binomialheap

            binomialheap.is_binomialheap()

            try:
                a_binarytreeminHeap[type_file] += endC_binarytreeminHeap
                a_arrayminheap[type_file] += endC_arrayminheap
                a_binomialheap[type_file] += endC_binomialheap
            except:
                a_binarytreeminHeap[type_file] = endC_binarytreeminHeap
                a_arrayminheap[type_file] = endC_arrayminheap
                a_binomialheap[type_file] = endC_binomialheap

    for e1, e2, e3 in zip(a_binarytreeminHeap.keys(), a_arrayminheap.keys(), a_binomialheap):
        a_binarytreeminHeap[e1] /= 5
        a_arrayminheap[e2] /= 5
        a_binomialheap[e3] /= 5

    sortDic_binarytreeminHeap = OrderedDict(sorted(a_binarytreeminHeap.items(), key=lambda x: int(x[0])))
    sortDic_arrayminheap = OrderedDict(sorted(a_arrayminheap.items(), key=lambda x: int(x[0])))
    sortDic_binomialheap = OrderedDict(sorted(a_binomialheap.items(), key=lambda x: int(x[0])))

    pprint.pprint(sortDic_binarytreeminHeap)
    pprint.pprint(sortDic_arrayminheap)
    pprint.pprint(sortDic_binomialheap)

    plot3(sortDic_binarytreeminHeap, sortDic_arrayminheap, sortDic_binomialheap, n1='BinaryTreeMinHeap',
          n2='ArrayMinHeap',
          n3='BinomialHeap',
          name='Temps d\'exécution de ConsIter sur les fichiers Shakespeare')

    def MergeALL_Tas_File():
        l1_dic = fichiers_ShakespeareMD5()

        nb_foreach_file = {}
        a_binarytreeminHeap = {}
        a_arrayminheap = {}
        a_binomialheap = {}
        for type_file in l1_dic.keys():
            for type_file2 in l1_dic.keys():
                len_file = str(int(type_file) + int(type_file2))
                list_elem1 = l1_dic[type_file]
                list_elem2 = l1_dic[type_file2]

                # BinaryTreeMinHeap
                binaryTreeMinHeap1 = BinaryTreeMinHeap()
                binaryTreeMinHeap2 = BinaryTreeMinHeap()

                binaryTreeMinHeap1.ConsIter(list_elem1)
                binaryTreeMinHeap2.ConsIter(list_elem2)

                startC_binaryTreeMinHeap = time.time()
                binaryTreeMinHeap1.Union(binaryTreeMinHeap2)
                endC_binaryTreeMinHeap = time.time() - startC_binaryTreeMinHeap

                # ArrayMinHeap
                arrayMinHeap1 = ArrayMinHeap()
                arrayMinHeap2 = ArrayMinHeap()
                arrayMinHeap1.ajout_simple(list_elem=list_elem1)
                arrayMinHeap2.ajout_simple(list_elem=list_elem2)
                arrayMinHeap1.ConsIterTab(ajout_simple=False)
                arrayMinHeap2.ConsIterTab(ajout_simple=False)

                startC_arrayMinHeap = time.time()
                arrayMinHeap1.Union(arrayMinHeap2)
                endC_arrayMinHeap = time.time() - startC_arrayMinHeap

                # BinomialHeap
                binomialHeap1 = BinomialHeap()
                binomialHeap2 = BinomialHeap()
                binomialHeap1.ConsIter(list_elem1)
                binomialHeap2.ConsIter(list_elem2)

                startC_binomialHeap = time.time()
                binomialHeap1.merge(binomialHeap2)
                endC_binomialHeap = time.time() - startC_binomialHeap

                # binomialHeap1.is_binomialheap()

                try:
                    nb_foreach_file[len_file] += 1
                    a_binarytreeminHeap[type_file] += endC_binaryTreeMinHeap
                    a_arrayminheap[type_file] += endC_arrayMinHeap
                    a_binomialheap[type_file] += endC_binomialHeap
                except:
                    nb_foreach_file[len_file] = 1
                    a_binarytreeminHeap[type_file] = endC_binaryTreeMinHeap
                    a_arrayminheap[type_file] = endC_arrayMinHeap
                    a_binomialheap[type_file] = endC_binomialHeap

        for e1, e2, e3 in zip(a_binarytreeminHeap.keys(), a_arrayminheap.keys(), a_binomialheap):
            a_binarytreeminHeap[e1] /= 5
            a_arrayminheap[e2] /= 5
            a_binomialheap[e3] /= 5

        sortDic_binarytreeminHeap = OrderedDict(sorted(a_binarytreeminHeap.items(), key=lambda x: int(x[0])))
        sortDic_arrayminheap = OrderedDict(sorted(a_arrayminheap.items(), key=lambda x: int(x[0])))
        sortDic_binomialheap = OrderedDict(sorted(a_binomialheap.items(), key=lambda x: int(x[0])))

        pprint.pprint(sortDic_binarytreeminHeap)
        pprint.pprint(sortDic_arrayminheap)
        pprint.pprint(sortDic_binomialheap)

        plot3(sortDic_binarytreeminHeap, sortDic_arrayminheap, sortDic_binomialheap, n1='BinaryTreeMinHeap',
              n2='ArrayMinHeap',
              n3='BinomialHeap',
              name='Temps d\'exécution de Union sur les fichiers Shakespeare')


if __name__ == '__main__':
    # Question 6.12 / 6.13

    # collisonShakespeare()

    # Question 6.&4

    # SuppMin_Tas_File()
    Ajout_Tas_File()
    # ConstIter_Tas_File()
    # MergeALL_Tas_File()

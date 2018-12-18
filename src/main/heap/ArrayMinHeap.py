import random
import time
from builtins import list

from src.main.FileReader import inf
import numpy as np

DEB = 2
FIN = 10
SIZE = 5000


class ArrayMinHeap:
    def __init__(self, heap_array=None, int_key=False):
        if heap_array is not None:
            self.heap_array = np.array(heap_array)
            self.size = self.heap_array.__len__()
        elif int_key:
            self.heap_array = np.full((SIZE), np.int)
            self.size = 0
        else:
            # initialisation d'un tableaux de str de taille 100
            self.heap_array = np.full((SIZE), np.str)
            self.size = 0

    def __len__(self):
        return len(self.heap_array)

    def clear_heap(self):
        self.heap_array.clear()

    def get_heap_array(self):
        return self.heap_array[0:self.size]

    def parent(self, i):
        return (i - 1) / 2

    def percUp(self, i, key):
        while i > 0:
            pere = (i - 1) // 2
            e = self.heap_array[pere]
            if inf(e, key, DEB, FIN):
                break
            self.heap_array[i] = e
            i = pere
        self.heap_array[i] = key

    def swap(self, a, b):
        tmp = a
        a = b
        b = tmp
        return a, b

    def percDown(self, i):
        while (i * 2 + 1) < self.size:
            mc = self.min_child(i)
            if not inf(self.heap_array[i], self.heap_array[mc], DEB, FIN):
                # print('je swap entre le pere : ', self.heap_array[i], ' | et le fils : ', self.heap_array[mc])
                # tmp = self.heap_array[i]
                # self.heap_array[i] = self.heap_array[mc]
                # self.heap_array[mc] = tmp
                self.heap_array[i], self.heap_array[mc] = self.swap(self.heap_array[i], self.heap_array[mc])
            i = mc

    def min_child(self, i):
        """
        Renvoie le fils le plus petit de i
        :type i :
        :rtype: int | str
        """
        pere = i
        fils1 = 2 * pere + 1
        if fils1 >= self.size:
            return i * 2  # i
        else:
            if fils1 + 1 >= self.size:
                return fils1
            elif inf(self.heap_array[fils1], self.heap_array[fils1 + 1], DEB, FIN):
                return fils1
            else:
                return fils1 + 1

    def empty(self):
        if self.size == 0:
            True
        return False

    def full(self):
        return self.size == self.__len__()

    def resize(self):
        pass

    def insert(self, val, sort=True):
        if self.full():
            if isinstance(self.heap_array[0], np.int64) or isinstance(self.heap_array[0], np.int):
                tmp = self.heap_array
                self.heap_array = np.full(SIZE * 2, np.int)
                self.heap_array[0:self.size] = tmp
            if isinstance(self.heap_array[0], np.str):
                tmp = self.heap_array
                self.heap_array = np.full(2 * self.__len__(), np.str)
                self.heap_array[0:self.size] = tmp
        self.heap_array[self.size] = val
        self.size += 1
        if sort:
            if self.size > 1:
                self.percUp(self.size - 1, val)

    def get_min(self):
        return self.heap_array[0]

    def echange(self, pere, fils):
        """
        Permet d echanger les valeurs de pere et fils
        """
        tmp = pere
        pere = fils
        fils = tmp
        return pere, fils

    def update_tree(self):
        """
        Permet de metre a jour notre Tas
        """
        index = self.size // 2
        i = index - 1
        while i >= 0:
            self.percDown(i)
            i -= 1

    def delete_min(self, sort=True):
        """
        Permet de supprrimer le min dans un Tas
        @param T - Tas min
        @return le Tas t sans l element min (la racine)
        """

        val_min = self.heap_array[0]

        self.heap_array[0] = self.get_heap_array()[self.size - 1]
        self.heap_array = np.delete(self.heap_array,
                                    self.size - 1)  # supprimer le denier element du tableau (celui qu'on vient de remonter)
        self.size -= 1
        if sort:
            self.percDown(0)

        return val_min

    def ajout_simple(self, list_elem):
        if list_elem is not None:
            for ele in list_elem:
                self.insert(ele, False)

    def ConsIterTab(self, list_elem=None, ajout_simple=True):
        if ajout_simple:
            self.ajout_simple(list_elem)

        self.update_tree()

    def is_arrayMinHeap(self):
        index = self.size // 2 - 1

        for i in range(index, -1, -1):
            if (i * 2) < self.size:
                mc = self.min_child(i)
                # print(' je suis a l index : ', i, 'de valeur : ',  self.heap_array[i], ' je verifier avec mon fils min l index : ', mc, ' de valeur : ', self.heap_array[mc])
                if not inf(self.heap_array[i], self.heap_array[mc], DEB, FIN):
                    if not (self.heap_array[i] == self.heap_array[mc]):
                        print(self.heap_array[i], ' |||  ', self.heap_array[mc])
                        # print(len(self.heap_array[i]), ' |||  ', len(self.heap_array[mc]))
                        return False
                i = mc
        return True

    def Union(self, T_other):

        # Cas de base
        if not isinstance(T_other, ArrayMinHeap):
            raise AssertionError("Error - Tree_other most be instance of ArrayMinHeap")
        #elif not self.is_arrayMinHeap() or not T_other.is_arrayMinHeap():
         #   raise AssertionError("Error - Invalid structure MinHeap for self.tree or tree_other")
        elif T_other is self:
            raise AssertionError("Error - it the same tree")
        elif T_other.size == 0:
            #raise AssertionError("Error - tree_other is empty")
            return self
        elif self.size == 0:
            # on initialise notre arbre avec l'arbe passer en paramètre
            return T_other
        # autre cas
        elif self.size >= T_other.size:
            self.ConsIterTab(list_elem=T_other.get_heap_array())
            return self
        elif self.size < T_other.size:
            T_other.ConsIterTab(self.get_heap_array())
            return T_other


if __name__ == "__main__":
    """
    heap0 = ArrayMinHeap(int_key=True)
    heap4 = ArrayMinHeap(int_key=True)

    print("################insert#########################")

    heap0.insert(50)
    heap0.insert(23)
    heap0.insert(11)
    heap0.insert(30)
    heap0.insert(0)
    print('heap0 : ', heap0.get_heap_array())
    """
    print("################ConsIter#########################")
    heap1 = ArrayMinHeap()
    heap2 = ArrayMinHeap(heap_array=[50, 23, 11, 30, 0])

    # print("heap1 : ", heap1.size)
    # print("heap2 : ", heap2.size)

    heap1.ConsIterTab(list_elem=[50, 23, 11, 30, 0])
    heap2.ConsIterTab(sort=False)

    # print("heap1 : ", heap1.get_heap_array())
    # print(heap1.is_arrayMinHeap())
    # print(heap2.is_arrayMinHeap())

    print("################Union#########################")
    heap = ArrayMinHeap(heap_array=[5, 3, 1, 39, 6])

    heap.ConsIterTab()
    print('heap : ', heap.get_heap_array())
    print('heap1 : ', heap1.get_heap_array())
    heap = heap.Union(heap1)
    print('new heap : ', heap.get_heap_array())
    #
    """
    print("################Delete#########################")
    heap4.ConsIterTab([50, 23, 11, 30, 0])
    print('heap_array : ', heap4.get_heap_array())
    print('min : ', heap4.get_min())
    print('delete : ', heap4.delete_min())
    print('après le delete du min : ', heap4.get_heap_array())
    heap4.insert(1)
    print('après ajout : ', heap4.get_heap_array())
    heap4.insert(12)
    print('après ajout : ', heap4.get_heap_array())

    print()
    """
    print("################bbbbbbbbbbbb#########################")
    # print()
    # hh = ArrayMinHeap()
    # hh2 = ArrayMinHeap()
    # s = 10000
    # li = np.full(s, np.int)
    # for i in range(0, s, 1):
    #     li[i] = random.randint(0, 101, 2)
    #
    # print(' avant : ', li)
    # for i in li:
    #     hh.insert(i)
    #
    # print('h1 : ', hh.is_arrayMinHeap())
    # print()


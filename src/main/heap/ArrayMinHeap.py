import random
import time
from builtins import list

from src.main.FileReader import inf
import numpy as np

DEB = 2
FIN = 10
SIZE = 5000  # la taille initiale de notre tableau


class ArrayMinHeap:
    def __init__(self, heap_array=None, int_key=False):
        """
        Installation du tas, self.heap_array: représentat le tableau courant de notre class
        :param heap_array: une liste d'element
        :param int_key: si le tas est un tas de int
        """
        if heap_array is not None:
            self.heap_array = np.array(heap_array)
            self.size = self.heap_array.__len__()
        elif int_key:
            self.heap_array = np.full((SIZE), np.int)
            self.size = 0
        else:
            # initialisation d'un tableaux de str de taille SIZE
            self.heap_array = np.full((SIZE), np.str)
            self.size = 0

    def __len__(self):
        """

        :return: la taille du tas
        """
        return len(self.heap_array)

    def clear_heap(self):
        """
        Cleaner le tableau
        """
        self.heap_array.clear()

    def get_heap_array(self):
        """

        :return: le tableau avec nous vrai valeur
        """
        return self.heap_array[0:self.size]

    def parent(self, i):
        """

        :param i: un index dans le tableau
        :return: le pere de index i
        """
        return (i - 1) / 2

    def percUp(self, i, key):
        """
        Permet de faire des swap en partant de i jusqu'a la racinec
        :param i: index dans le tableau
        :param key: la valeur ajouter
        """
        while i > 0:
            pere = (i - 1) // 2
            e = self.heap_array[pere]
            if inf(e, key, DEB, FIN):
                break
            self.heap_array[i] = e
            i = pere
        self.heap_array[i] = key

    def swap(self, a, b):
        """
        Faire un swap entre deux valeur
        :param a: valeur 1
        :param b: valeur 1
        :return: les deux valeur echanger
        """
        tmp = a
        a = b
        b = tmp
        return a, b

    def percDown(self, i):
        """
        Permet de faire des swap en partant de i jusqu'a aarriver a la fin de notre tableau
        :param i:
        """
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
        :type i : une valeur dans le tableau
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
        """

        :return: renvoie true si le tableau est vide, false dans le cas contraire
        """
        if self.size == 0:
            True
        return False

    def full(self):
        """

        :return: true si le tableau est plein
        """
        return self.size == self.__len__()

    def insert(self, val, sort=True):
        """
        Ajouter une nouvelle valeur dans l'arbre
        :param val: la valeur a ajouter
        :param sort: si on trie ou pas
        """
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
        """

        :return: Renvoie la valeur min du tableau
        """
        return self.heap_array[0]

    def echange(self, pere, fils):
        """
        Permet d echanger les valeurs de pere et de fils
        :return les valeur echanger
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

        :param si on met a jour ou pas
        :return la valeur suppr
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
        """
        Permet de faire des ajout simple
        :param list_elem:
        """
        if list_elem is not None:
            for ele in list_elem:
                self.insert(ele, False)

    def ConsIterTab(self, list_elem=None, ajout_simple=True):
        """
        Permet de contruire un tas

        :param list_elem: liste d'element a ajouter, true par defaut
        :param ajout_simple: si on effectue un ajout simple
        """
        if ajout_simple:
            self.ajout_simple(list_elem)

        self.update_tree()

    def is_arrayMinHeap(self):
        """
        Permet de vérifier la structure du Tas

        :return: True si ça respect la structure d'un tas, False dans le cas contraire
        """
        index = self.size // 2 - 1

        for i in range(index, -1, -1):
            if (i * 2) < self.size:
                mc = self.min_child(i)
                if not inf(self.heap_array[i], self.heap_array[mc], DEB, FIN):
                    if not (self.heap_array[i] == self.heap_array[mc]):
                        return False
                i = mc
        return True

    def Union(self, T_other):
        """
        Permet de faire l'union de deux Tas, on ajouter les element du tas avec le moins d'element dans l'autre

        :param T_other: Tsa
        :return: le tas résultat de la fusion de deux tas
        """

        # Cas de base
        if not isinstance(T_other, ArrayMinHeap):
            raise AssertionError("Error - Tree_other most be instance of ArrayMinHeap")
        # elif not self.is_arrayMinHeap() or not T_other.is_arrayMinHeap():
        #   raise AssertionError("Error - Invalid structure MinHeap for self.tree or tree_other")
        elif T_other is self:
            raise AssertionError("Error - it the same tree")
        elif T_other.size == 0:
            # raise AssertionError("Error - tree_other is empty")
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
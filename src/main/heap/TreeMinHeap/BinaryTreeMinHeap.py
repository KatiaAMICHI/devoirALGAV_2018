from math import *

from src.main.FileReader import inf
from src.main.heap.TreeMinHeap.BinaryTreeHeapNode import Node
import graphviz as gv

DEB = 2
FIN = 10


# TODO updateMin
class BinaryTreeMinHeap(object):

    def __init__(self):
        self.root = None
        self.last = None
        self.nbElem = 0

    def getroot(self):
        return self.root

    def set_root(self, root):
        self.root.key = root.key

    def get_last(self):
        return self.last

    def set_last(self, last):
        self.last.key = last

    def get_nbElem(self):
        return self.nbElem

    def nb_node(self):
        return self.nbElem - (self.nbElem + 1) / 2

    def get_hauteur(self):
        h = log(self.nbElem, 2)  # math.log(number,base)
        if h > floor(h):
            return floor(h) + 1
        return h

    # si on met a jour alors mtr a la valeur True dans le cas contraire False
    def insert(self, val, mtr=True):
        node = Node(val)
        num = self.nbElem + 1

        # si arbre est vide
        if self.root is None:
            self.root = node

        # si last element est a la palce 2^n-1
        elif ((num & (num - 1)) == 0) and num != 0:
            currant = self.root
            # trouver l element le plus a gauche
            while currant.left is not None:
                currant = currant.left
            currant.insert_child(node)

        else:
            # si le last element est un _child droit
            instru = []
            find = False

            instru.append(self.last)
            currant = self.last.parent

            # O(log(n) || trouver la permiere hauteur avec un autre _child droit
            # tant que {\displaystyle x} x n'est pas la root de l arbre
            # et que x est strictement supérieur à son père, on échange les positions de et son père.
            while currant.parent is not None and currant.right in instru:
                if currant not in instru:
                    instru.append(currant)
                currant = currant.parent

            while not find:
                if currant not in instru:
                    instru.append(currant)

                if currant.left is not None and currant.left not in instru:
                    instru.append(currant.left)
                    currant = currant.left

                elif currant.right is not None and currant.right not in instru:
                    instru.append(currant.right)
                    currant = currant.right

                if currant.insert_child(node):
                    find = True

        self.nbElem += 1
        self.last = node

        if (mtr):
            self.updateTree()

        return True

    # O(log(n))
    def updateTree(self):
        cons = self.last
        new_child = None

        if cons.parent is not None:
            new_child = cons.parent

        while new_child is not None and inf(cons.key, new_child.key, DEB, FIN):

            tmp1 = cons.key
            cons.key = new_child.key
            new_child.key = tmp1

            cons = cons.parent
            if cons.parent is None:
                self.root = cons
            if not cons.have_child():
                self.last = cons

            new_child = new_child.parent

    def isBinaryTreeMinHeap(self):
        cons = self.last
        tmp = None
        new_child = None

        if self.nbElem == 0:
            return True
        if cons.parent is not None:
            new_child = cons.parent

        while new_child is not None and inf(cons.key, new_child.key, DEB, FIN):
            if inf(cons.key, new_child.key, DEB, FIN):
                return False
            cons = cons.parent
            new_child = new_child.parent
        return True

    def printTree(self):
        currant = self.root
        if currant is not None:
            return self._printTree(currant, [])

    def _printTree(self, root, result):
        if root is not None:
            self._printTree(root.left, result)
            result.append(root.key)
            self._printTree(root.right, result)
        return result

    def echangeConstW(self, cons, new_child, bool_left):
        tmp1 = cons.key
        cons.key = new_child.key
        new_child.key = tmp1
        consf = cons

        min_child2 = new_child.min_child()

        while min_child2 is not None and not inf(new_child.key, min_child2.key, DEB, FIN):
            tmp1 = new_child.key
            new_child.key = min_child2.key
            min_child2.key = tmp1

            if new_child.is_left(min_child2):
                new_child = new_child.get_left()
            elif new_child.is_right(min_child2):
                new_child = new_child.get_right()
            min_child2 = new_child.min_child()

        if bool_left:
            return consf.key, consf.left.key
        return consf.key, consf.right.key

    def ajout_simple(self, listElem):
        for elem in listElem:
            self.insert(elem, False)

    def ConsIter(self, listElem=None, is_tree=False, ajout_simple=True):

        """
        @param listElem - une liste d'elements ordener de sorte a avoir la racine
                suivie du fils droit puis du fils gauche
        @return true si OK false dans le cas contraire
        """

        if ajout_simple and not is_tree and listElem is not None:
            # contruction de la arbre binaire avec tous les éléments sans se soucier de la contrainte d'ordre
            self.ajout_simple(listElem)

        if self.nbElem == 1:
            return self

        n_current = self.root
        # le dernier node gauche de notre arbre
        while n_current is not None and n_current.get_left().is_parent():
            n_current = n_current.get_left()

        ok = False
        n_before = None

        while not ok and n_current is not None:
            if n_current.get_parent() is None and (
                    n_current.get_right() is None or n_current.get_right().key == n_before or not n_current.get_right().is_parent()):
                ok = True
            if n_current.get_right() is not None and n_before != n_current.get_right().key and n_current.get_right().is_parent():
                n_current = n_current.get_right()
                while n_current.get_left().is_parent():
                    n_current = n_current.get_left()
            if n_current.get_right() is not None:
                min_child = self.minChild(n_current.get_left().key, n_current.get_right().key)
            elif n_current.get_left():
                min_child = n_current.get_left().key
            if not inf(n_current.key, min_child, DEB, FIN):
                if min_child == n_current.left.key:
                    n_current.key, n_current.left.key = self.echangeConstW(n_current, n_current.left, True)

                elif min_child == n_current.right.key:
                    n_current.key, n_current.right.key = self.echangeConstW(n_current, n_current.right, False)
            if ok:
                break
            if n_before is None:
                n_before = n_current.key
            if n_current.get_parent() is not None:
                n_before = n_current.key
                n_current = n_current.get_parent()

    def minChild(self, n1, n2):
        if n1 == n2:
            return n1
        elif inf(n1, n2, DEB, FIN):
            return n1
        return n2

    def echange(self, cons, new_child):
        tmp1 = cons
        cons = new_child
        new_child = tmp1
        return cons, new_child

    def get_last(self):
        node = self.last

        while not node.get_parent().get_parent().is_left(node.get_parent()):
            if node.get_parent() is None:
                # alors on a atteint la racine
                node = node.get_left()
            elif node.get_parent().is_left(node):
                # si c'est un fils gauche je descend le plus possible
                while node.get_right() is not None:
                    node = node.get_right()
                self.last.key = node.get_parent().get_left()
            if node.get_parent().is_right(node):
                node = node.get_parent()

    # O(log(n))
    # soit l union de deux tas ou mettre le dernier elment a la racine et faire updateTree()
    def deleteMin(self):
        """
        @param T - Tas min
        @return la valeur supprimer
        """

        # verifier si A est un arbre vide
        if self.root is None:
            return None

        # si un seul element
        elif self.nbElem == 1:
            return None

        else:
            del_min = self.root.key
            self.root.key = self.last.key
            if self.last.get_parent().is_right(self.last):
                self.last.key = self.last.get_parent().get_left().key
            elif self.last.get_parent().is_left(self.last):
                self.last.key = self.last.get_parent().key

            keyMin = self.root
            left = keyMin.get_left()
            right = keyMin.get_right()
            while inf(left.key, keyMin.key, DEB, FIN) or inf(right.key, keyMin.key, DEB, FIN):
                if inf(left.key, keyMin.key, DEB, FIN):
                    left.key, keyMin.key = self.echange(left.key, keyMin.key)
                elif inf(right.key, keyMin.key, DEB, FIN):
                    right.key, keyMin.key = self.echange(right.key, keyMin.key)
        return del_min

    def Union(self, T2):
        """
        @param self - Tas min 1
        @param T2 - Tas min 2
        @return un Tas correspondant a l union des deux tas T1 & T2
        """
        if not isinstance(T2, BinaryTreeMinHeap):
            raise AssertionError("Error - Tas2 is not instance of BinaryTreeMinHeap")

        # verifier si T1 est nul
        if self.nbElem == 0:
            return T2

        # verifier si T2 est nul
        if T2.get_nbElem() == 0:
            return self

        # si T1 est plus grand alors en ajouter les element de T2 dans T1
        if self.nbElem > T2.get_nbElem():
            elem_T2 = T2.printTree()
            self.ConsIter(elem_T2)
            return self
        else:
            elem_T1 = self.printTree()
            T2.ConsIter(elem_T1)
            return T2

    def plot(self):
        self.root.plot()


if __name__ == '__main__':
    arbre = BinaryTreeMinHeap()
    arbre1 = BinaryTreeMinHeap()
    liste_elem = [50, 30, 70, 20, 40, 60, 80, 2, 3, 4, 5, 0]
    ll = [50, 30, 70, 20, 40, 60, 80]

    for elem in liste_elem:
        arbre.insert(elem, True)
    #

    arbre1.ConsIter(ll)  # [20, 30, 40, 50, 60, 70, 80]

    #
    print('arbre : ', arbre.printTree(), ' | estTasMin : ', arbre.isBinaryTreeMinHeap())
    print('arbre 1: ', arbre1.printTree(), ' | estTasMin : ', arbre1.isBinaryTreeMinHeap())

    arbre = arbre.Union(arbre1)
    print(arbre.isBinaryTreeMinHeap())
    arbre1.plot()

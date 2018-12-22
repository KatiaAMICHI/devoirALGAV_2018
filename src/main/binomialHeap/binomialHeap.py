from math import *

from src.main.FileReader import inf

DEB = 2
FIN = 10


class BinomialHeap(object):
    def __init__(self):
        self.head = BinomialHeap.Node()

    def is_empty(self):
        """
        vérifier si head est null
        :return true dans le cas où head soit None, False dans le cas contraire
        :rtype bool
        """
        return self.head.next is None

    def nb_heap(self):
        """
        Calcule le nombre de tas dans notre file binomial

        :return:le nombre de tas dans notre file binomial
        :rtype result : int
        """
        result = 0
        node = self.head.next
        while node is not None:
            result += 1
            node = node.next
        return result

    def get_children(self):
        """
        Récuperer la liste de fils d'un noeud

        :return: une list de fils
        :rtype result : list
        """
        result = []
        node = self.head.next
        while node is not None:
            result.append(node)
            node = node.next
        return result

    def clear(self):
        """
        Clean note file binomial
        """
        self.head.next = None

    def __len__(self):
        """

        :return:
        """
        result = 0
        node = self.head.next
        while node is not None:
            result |= 1 << node.rank
            node = node.next
        return result

    def get_min_value(self):
        """
        cherche la valeur minamal parmit tout les racine des sous arbre

        :return: retourne la valeur minimal
        :rtype: int | str
        """
        if self.head.next is None:
            raise Exception("Error - The heap is empty")
        min_value = None
        currant_node = self.head.next

        while currant_node is not None:
            if min_value is None or inf(currant_node.value, min_value, DEB, FIN):
                min_value = currant_node.value
            currant_node = currant_node.next

        return min_value

    def get_min_node(self):
        """
        Cherche le noeud avec la valeur minimal parmit tout les racine des sous arbre
            génére une erreur dans le cas où la file soit vide

        :return: retourne la valeur minimal
        :rtype: BinomialHeap.Node
        """
        if self.head.next is None:
            raise Exception("Error - The heap is empty")
        min_node = None
        currant_node = self.head.next

        while currant_node is not None:

            if min_node is None or inf(currant_node.value, min_node.value, DEB, FIN):
                min_node = currant_node
            currant_node = currant_node.next

        return min_node

    def delete_min(self):
        """
        Supp la valeur minimum,
            génére une erreur dans le cas où la file soit vide

        :rtype: int | str
        :return return la valeur supprimer
        """

        if self.head.next is None:
            raise Exception("Error - The heap is empty")
        min_value = None
        node_before_min_value = None

        prev_node = self.head

        # checher la racine qui a la valeur minimum
        while True:
            node = prev_node.next
            if node is None:
                break
            if min_value is None or inf(node.value, min_value, DEB, FIN):
                min_value = node.value
                node_before_min_value = prev_node
            prev_node = node

        min_node = node_before_min_value.next
        node_before_min_value.next = min_node.next
        min_node.next = None
        # fusion les sous-fils avec notre structure origine
        self._merge(min_node.remove_root())
        return min_value

    def insert(self, val):
        """
        Ajout de va a self, a partir de _merge entre self et new BinomialHeap
        """
        self._merge(BinomialHeap.Node(val))

    def _insert(self, list_val):
        """
        Ajout de list_val a self, en utilisant _merge entre self et new BinomialHeap pour chaque val de la liste
        :param list_val : la liste de valeur à ajouter
        :type list_val: list
        """
        for val in list_val:
            self._merge(BinomialHeap.Node(val))

    def merge(self, h):
        """
        Union entre deux BinomialHeap
        """
        if h is self:
            raise AssertionError("Error - it is the same tree")

        if not isinstance(h, BinomialHeap):
                raise AssertionError("Error - it is not instance of BinomialHeap")

        self._merge(h.head.next)
        h.head.next = None

    def _merge(self, other):
        """
        Union entre deux BinomialHeap
        """
        this = self.head.next
        self.head.next = None
        prevtail = None
        tail = self.head

        while this is not None or other is not None:
            if other is None or (this is not None and this.rank <= other.rank):
                node = this
                this = this.next
            else:
                node = other
                other = other.next
            node.next = None

            if tail.rank < node.rank:
                prevtail = tail
                tail.next = node
                tail = node
            elif tail.rank == node.rank + 1:
                assert prevtail is not None
                node.next = tail
                prevtail.next = node
                prevtail = node
            # si ils ont le même rang
            elif tail.rank == node.rank:
                # Union nodes
                if inf(tail.value, node.value, DEB, FIN) or tail.value == node.value:
                    node.next = tail.down
                    tail.down = node
                    tail.rank += 1
                else:
                    assert prevtail is not None
                    tail.next = node.down
                    node.down = tail
                    node.rank += 1
                    tail = node
                    prevtail.next = node
            else:
                raise AssertionError()

    def ConsIter(self, item_list):
        """
        Construction de la file binomiale avec la liste d'element,
            en utilisant la décomposition binaire,
            puis faire appele a la méthode insert

        :param item_list: l la liste d'elements a ajouter
        :type: item_list: list
        """

        if len(item_list) == 0:
            return

        i = 0
        nb_ele = bin(len(item_list))[2:]
        h_tmp = BinomialHeap()

        old_val = 0
        list_eleme_b = list(str(nb_ele))
        list_eleme_b.reverse()
        for e in list_eleme_b:
            if e == "1":
                h_tmp.clear()
                h_tmp._insert(item_list[old_val:(2 ** i + old_val)])
                self.merge(h_tmp)
                old_val = 2 ** i + old_val

            i += 1

    def is_binomialheap(self):
        """
        Vérifier si on respecte bien la structure d'un tas binomial
        """
        if self.head.value is not None and self.head.rank != -1:
            raise AssertionError("Error - Head must be dummy node")
        self.head.check_is_binomialheap(True, None)

    class Node(object):

        def __init__(self, val=None):
            """
            Initialisation du noeaud

            :param val:
            """
            self.value = val
            if val is None:
                self.rank = -1
            else:
                self.rank = 0
            self.down = None
            self.next = None

        def get_rank(self):
            """

            :return: renvoie la rang du noeud
            """
            return self.rank

        def remove_root(self):
            """

            :return:
            """
            assert self.next is None
            result = None
            down_node = self.down
            while down_node is not None:
                next_node = down_node.next
                down_node.next = result
                result = down_node
                down_node = next_node
            return result

        def check_is_binomialheap(self, is_root, min_result):
            """
            Vérifier la structure d'un tas binomial
            """
            if is_root != (min_result is None):
                raise AssertionError("Error - Invalid arguments")
            if (self.rank < 0) != (self.value is None):
                raise AssertionError("Error - Invalid node rank or value")
            if not is_root and not inf(min_result, self.value, DEB, FIN) and (min_result != self.value):
                raise AssertionError("Error - Invalid MinHeap")

            # check for children
            if self.rank > 0:
                if self.down is None and self.down.rank != self.rank:
                    raise AssertionError("Error - Down node must not be None ")
                self.down.check_is_binomialheap(False, self.value)
                if not is_root:
                    if self.next is None or self.next.rank != self.rank - 1:
                        raise AssertionError("Error - Absence of next node or invalid rank")
                    self.next.check_is_binomialheap(False, min_result)
            elif self.down is not None:
                raise AssertionError("Error - Invalid node rank must be > 0")

            # check foreach root
            if is_root and self.next is not None:
                if self.next.rank <= self.rank:
                    raise AssertionError("Error - invalid rank for next node")

                self.next.check_is_binomialheap(True, None)


if __name__ == "__main__":
    h = BinomialHeap()
    h2 = BinomialHeap()
    list_elem1 = [3, 19, 10, 2, 4]
    list_elem2 = [6, 7, 8, 1, 0, 11, 34]

    h.ConsIter(list_elem1)
    h2.ConsIter(list_elem2)
    print(h.get_children()[1].rank)


    h.merge(h2)
    h.is_binomialheap()
    print("*******************************************************************")
    print(h.get_children()[1].rank)

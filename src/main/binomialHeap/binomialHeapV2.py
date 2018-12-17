from math import *

from src.main.FileReader import inf

DEB = 2
FIN = 10


class BinomialHeap(object):
    def __init__(self):
        self.head = BinomialHeap.Node()

    def is_empty(self):
        return self.head.next is None

    def nb_heap(self):
        result = 0
        node = self.head.next
        while node is not None:
            result += 1
            node = node.next
        return result

    def get_children(self):
        result = []
        node = self.head.next
        while node is not None:
            result.append(node)
            node = node.next
        return result

    def clear(self):
        self.head.next = None

    def __len__(self):
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
        cherche la valeur minamal parmit tout les racine des sous arbre
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
        Delete the min value
        :rtype: int | str
        :return return the min value
        """

        if self.head.next is None:
            raise Exception("Error - The heap is empty")
        min_value = None
        node_before_min_value = None

        prev_node = self.head
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
        self._merge(min_node.remove_root())
        return min_value

    def insert(self, val):
        """
        Insert value into self, using _merge between self and new BinomialHeap
        """
        self._merge(BinomialHeap.Node(val))

    def _insert(self, list_val):
        """
        Insert list of value into self, using _merge between self and new BinomialHeap foreach val
        :type list_val: list
        """
        for val in list_val:
            self._merge(BinomialHeap.Node(val))

    def merge(self, h):
        """
        Merge between two BinomialHeap
        """
        if h is self:
            raise AssertionError("Error - it is the same tree")

        if not isinstance(h, BinomialHeap):
                raise AssertionError("Error - it is not instance of BinomialHeap")

        self._merge(h.head.next)
        h.head.next = None

    def _merge(self, other):
        """
        Merge between self and other
        """
        assert self.head.rank == -1
        assert other is None or other.rank >= 0
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
            elif tail.rank == node.rank:
                # Merge nodes
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
        :param item_list: list of element to insert
        :type: list
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
        if self.head.value is not None and self.head.rank != -1:
            raise AssertionError("Error - Head must be dummy node")
        self.head.check_is_binomialheap(True, None)

    class Node(object):

        def __init__(self, val=None):
            self.value = val
            if val is None:
                self.rank = -1
            else:
                self.rank = 0
            self.down = None
            self.next = None

        def get_rank(self):
            return self.rank

        def remove_root(self):
            assert self.next is None
            result = None
            down_node = self.down
            while down_node is not None:  # Reverse the order of nodes from descending rank to ascending rank
                next_node = down_node.next
                down_node.next = result
                result = down_node
                down_node = next_node
            return result

        def check_is_binomialheap(self, is_root, min_result):
            """
            Check structure of binomialHeap
            """
            if is_root != (min_result is None):
                raise AssertionError("Error - Invalid arguments")
            if (self.rank < 0) != (self.value is None):
                raise AssertionError("Error - Invalid node rank or value")
            if not is_root and not inf(min_result, self.value, DEB, FIN) and (min_result != self.value):
                print('>>>>>>>>>>> : ', min_result, '|||| -', self.value)
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

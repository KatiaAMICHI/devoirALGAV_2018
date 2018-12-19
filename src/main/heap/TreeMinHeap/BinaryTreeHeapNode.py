from src.main.FileReader import inf
import graphviz as gv


class Node:

    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def get_parent(self):
        return self.parent

    def get_key(self):
        return self.key

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    # Ajout dans le fils direct du node, retourne false s'il a deja deux fils
    def insert_child(self, new_fils):
        if self.left is None:
            # print('Ajout comme fils Gauche : ', newFils.key, ' a : ', self.key)
            self.left = new_fils
            self.left.parent = self

            return True

        elif self.right is None:
            # print('Ajout comme fils Droit : ', newFils.key, ' a : ', self.key)
            self.right = new_fils
            self.right.parent = self

            return True

        return False

    def del_child(self):
        self.left = None
        self.right = None

    def is_full(self):
        if self.left is not None and self.right is not None:
            return True
        return False

    def have_child(self):
        if self.left is not None or self.right is not None:
            return True
        return False

    def is_left(self, f):
        if self.left == f:
            return True
        return False

    def is_right(self, f):
        if self.right == f:
            return True
        return False

    def min_child(self):
        if self.right is not None:
            if not inf(self.left.key, self.right.key, 2, 10):
                return self.left
            else:
                return self.right
        elif self.left is not None:
            return self.left
        return None

    def is_parent(self):
        if self.left is None and self.right is None:
            return False
        return True

    def plot(self):
        gtree = gv.Digraph(format='png')
        print('>>>>>>>< ', self.key)
        return self.to_graph(gtree, str(self.key))

    def to_graph(self, g, prefixe):
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        """ construit une représentation de l'arbre pour pouvoir
            l'afficher
        """
        if not self.is_full():
            g.node(prefixe, str(self.key), shape='ellipse')
        else:
            g.node(prefixe, str(self.key), shape='ellipse')
            if self.left is not None:

                print('////////////////////////////', type(self.left))
                self.left.to_graph(g, prefixe + "g")
                g.edge(prefixe, prefixe + "g")
            if self.right is not None:
                self.right.to_graph(g, prefixe + "d")
                g.edge(prefixe, prefixe + "d")
        return g

from src.main.FileReader import inf, sup

DEB = 2
FIN = 10


class AVLTree(object):
    """
    Arbre de recherche Avl
    """

    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0  # height(LeftSubTree) - height(RightSubTree)

    def getheight(self):
        return self.height

    def getbalance(self):
        return self.balance

    def edit_heights(self, recursive=True):
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.edit_heights()
                if self.node.right:
                    self.node.right.edit_heights()

            self.height = 1 + max(self.node.left.height, self.node.right.height)
        else:
            self.height = -1

    def edit_balances(self, recursive=True):
        """
        Différence de hauteur entre les deux fils d'un noeud
        :param recursive: de calculer la différence de hauteur de façon recursive; pour chaque sous fils
        """
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.edit_balances()
                if self.node.right:
                    self.node.right.edit_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def requilibrage(self):
        """
        Requilibrage de notre arbre dans dans cas où on a une différence d'hautre de plus de 1 entre nos sous-arbres
        """

        # mise a jour de heights et de balance
        # augmenter de 1
        self.edit_heights(recursive=False)
        self.edit_balances(recursive=False)

        # tant qu'on a une différence d'équilibraque qui est supérieur à 1 et inférieur a -1 on continue
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                # alors le sous-arbre doit a une hauteur plus grande que celle du sous-arbre gauche
                if self.node.left.balance < 0:
                    self.node.left.rotate_left()
                    self.edit_heights()
                    self.edit_balances()

                self.rotate_right()
                self.edit_heights()
                self.edit_balances()
            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rotate_right()
                    self.edit_heights()
                    self.edit_balances()

                self.rotate_left()
                self.edit_heights()
                self.edit_balances()

    def delete_value(self, key):
        """
        Supprition d'une key dans l'arbre
        :type key : int | str
        :param key: la cle a supprimer dans notre arbre
        """
        if self.node is not None:
            if self.node.key == key:
                # la clé est trouvée
                if not self.node.left.node and not self.node.right.node:
                    # la clé est trouvée dans le noeud feuille, on la supprime
                    self.node = None
                # notre noeud n'a pas de sous arbre droit
                elif not self.node.right.node:
                    self.node = self.node.left.node
                # notre noeud n'a pas de sous arbre gauche
                elif not self.node.left.node:
                    self.node = self.node.right.node
                else:
                    # remplacer node par par un successeur; le plus grand des noeud dans le sous arbre gauche
                    #                                   ou  le plus petit noeud dans le sous atbre droit
                    successor = self.node.left.node
                    while successor and successor.right.node:
                        successor = successor.right.node

                    if successor:
                        self.node.key = successor.key

                        # superstition du successeur dans l'arbre gauche
                        self.node.left.delete_value(successor.key)

            elif inf(key, self.node.key, DEB, FIN):
                # la cle est dans l'arbe gauche
                self.node.left.delete_value(key)

            elif sup(key, self.node.key, DEB, FIN):
                # la cle est dans l'arbe droit
                self.node.right.delete_value(key)

            # requilibrage de l'arbre
            self.requilibrage()

    def insert(self, key, sort=False):
        """
        Insertion d'une nouvelle key dans l'arbre
        :param key: la valeur a ajouter dans notre arbre
        :param sort: true dans le cas si on veut equilibré notre arbre,
                        false dans le cas contraire; si on veut ajouter nos elements sans prendre en compte la contrainte d'équilibrage
        :type key: int | str
        """

        # creation d'un node avec comme valeur key
        n = self.NodeAVL(key)

        # inisialisation de l'arbre
        if not self.node:
            self.node = n
            self.node.left = AVLTree()
            self.node.right = AVLTree()
        # inserer la key dans sous arbre gauche
        elif inf(key, self.node.key, DEB, FIN):
            self.node.left.insert(key, sort=sort)
        # inserer la key dans sous arbre droit
        elif sup(key, self.node.key, DEB, FIN):
            self.node.right.insert(key, sort=sort)

        if sort:
            # requilibrage de l'arbre
            self.requilibrage()

    def rotate_right(self):
        """
        Right rotation
        """
        new_root = self.node.left.node
        new_left_sub = new_root.right.node
        old_root = self.node

        self.node = new_root
        old_root.left.node = new_left_sub
        new_root.right.node = old_root

    def rotate_left(self):
        """
        Left rotation
        """
        new_root = self.node.right.node
        new_left_sub = new_root.left.node
        old_root = self.node

        self.node = new_root
        old_root.right.node = new_left_sub
        new_root.left.node = old_root

    def search(self, key):
        """
        :type key : int | str
        :rtype: bool
        """
        current = self.node
        while current is not None:
            if current.key == key:
                return True
            elif inf(key, current.key, DEB, FIN):
                current = current.left.node
            elif not inf(key, current.key, DEB, FIN):
                current = current.right.node
        return False

    def search2(self, root, key):

        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search(root.right, key)

        return self.search(root.left, key)

    def is_avltree(self):
        if self.balance not in [-1, 0, 1]:
            print('balance : ', self.balance)
            raise AssertionError("Error - Balance")
        if self.node is not None and self.node.right.node is not None:
            if not inf(self.node.key, self.node.right.node.key, DEB, FIN):
                raise AssertionError("Error - Node right can not be < to Node parent")
        if self.node is not None and self.node.left.node is not None:
            if inf(self.node.key, self.node.left.node.key, DEB, FIN):
                raise AssertionError("Error - Node left can not be > to Node parent")
        if self.node is not None:
            self.node.left.is_avltree()
            self.node.right.is_avltree()
        return True

    def ConsIter(self, list_value):
        for val in list_value:
            self.insert(val, sort=True)

    def Union(self, avl_tree):
        """
        Union de deux arbre de recherche
        :param avl_tree:
        :type avl_tree: AVLTree
        :return:
        """

        if not isinstance(avl_tree, AVLTree):
                raise AssertionError("Error - avl_tree is not instance of AVL")

        if len(self.print_pre_tree()) < len(avl_tree.print_pre_tree()):
            for ele in self.print_pre_tree():
                avl_tree.insert(ele, sort=True)
            return avl_tree
        else:
            for ele in avl_tree.print_pre_tree():
                self.insert(ele, sort=True)
            return self

    def print_pre_tree(self):
        result = []
        if not self.node:
            return result
        result.append(self.node.key)
        result.extend(self.node.left.print_tree())
        result.extend(self.node.right.print_tree())

        return result

    def print_inf_tree(self):
        result = []
        if not self.node:
            return result
        result.extend(self.node.left.print_tree())
        result.append(self.node.key)
        result.extend(self.node.right.print_tree())

        return result

    def print_post_tree(self):
        result = []
        if not self.node:
            return result
        result.extend(self.node.left.print_tree())
        result.extend(self.node.right.print_tree())
        result.append(self.node.key)

        return result

    def print_tree(self):
        result = []
        if not self.node:
            return result
        result.extend(self.node.left.print_tree())
        result.append(self.node.key)
        result.extend(self.node.right.print_tree())

        return result

    """
    Class Node AVL
    """

    class NodeAVL(object):
        """
        A node in an avl tree.
        """

        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None


if __name__ == '__main__':
    tree = AVLTree()
    tree2 = AVLTree()
    liste_elem3 = [34, 67, 21]
    liste_elem4 = [2, 2, 4, 5, 6]

    for ele in liste_elem3:
        tree.insert(ele, sort=True)

    for ele in liste_elem4:
        tree2.insert(ele, sort=True)

    print('height : ', tree.getheight())
    print('balance : ', tree.getbalance())
    print('tree :', tree.print_tree())
    print('node : ', tree.node.key)
    print('fils left : ', tree.node.left.node.key)

    tree = tree.Union(tree2)
    print()
    print(".............................................;")
    print()
    print('height : ', tree.getheight())
    print('balance : ', tree.getbalance())
    print('tree :', tree.print_tree())
    print('node : ', tree.node.key)
    print('fils left : ', tree.node.left.node.key)

""" Python Binary Tree Implementation """

from tree import Tree

class BinaryTree(Tree):
    """ Abstract base class for binary tree Implementation """

    def left(self, p):
        """ Return Position representing p's left child """
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """ Return Position representing p's right child """
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self, p):
        """ Return the Position representing p's sibling """
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.right(parent):
                return self.left(parent)
            else:
                return self.right(parent)
        

    def children(self, p):
        """ Generate an iteration of Positions of p's children """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

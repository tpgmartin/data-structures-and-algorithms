""" Python Tree abstract base class Implementation """

class Tree(object):
    """ Abstract base class for tree Implementation """

    class Position(object):
        """ Abstract base class representing the location of a single point """

        def element(self):
            """ Return element stored at this Position (class) """
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """ Check if does represent same Position """
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """ Check if do not represent same Position """
            return not self == other

    def root(self):
        """ Return Position representing the tree's root """
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """ Return Position representing p's parent """
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """ Return the number of children for Position p """
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """ Generate an iteration of Positions of p's children """
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """ Return the total number of element in the tree """
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        """ Return True if Position p is root of tree """
        return self.root() == p

    def is_leaf(self, p):
        """ Return True if Position p does not have any children """
        return self.num_children(p) == 0

    def is_empty(self):
        """ Return True if tree empty """
        return len(self) == 0

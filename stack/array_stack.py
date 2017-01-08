""" Python Array Stack Implementation """

from error import EmptyError

class ArrayStack(object):
    """ Stack ADT implmentation using Python list """

    def __init__(self):
        self._data = []

    def is_empty(self):
        """ Return true if stack empty """
        return len(self._data) == 0

    def push(self, elem):
        """ Push element to top of stack """
        self._data.append(elem)

    def top(self):
        """ Push element to top of stack """
        if self.is_empty():
            raise EmptyError('Stack is empty')
        return self._data[-1]

    def pop(self):
        """ Remove and return element from top of stack """
        if self.is_empty():
            raise EmptyError('Stack is empty')
        return self._data.pop()

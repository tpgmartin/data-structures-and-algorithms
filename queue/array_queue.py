""" Python Array Queue Implementation """

from error import EmptyError

class ArrayQueue(object):
    """ Queue ADT implmentation using Python list """
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0 # list index

    def __len__(self):
        """  Return number of elements in queue """
        return self._size

    def is_empty(self):
        """ Return true if queue empty """
        return self._size == 0

    def first(self):
        """ Return value of element at front of queue if present """
        if self.is_empty():
            return EmptyError('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """ Return and remove element at front of queue if present """
        if self.is_empty():
            return EmptyError('Queue is empty')
        element = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return element

    def enqueue(self, element):
        """ Add element to back of queue  """
        if self._size == len(self._data):
            self.__resize(2 * len(self._data))
        index = (self._front + self._size) % len(self._data)
        self._data[index] = element
        self._size += 1


    def __resize(self, capacity):
        """ Resize to 2 * current queue size  """
        prev_data = self._data
        self._data = [None] * capacity
        pointer = self._front
        for i in range(self._size):
            self._data[i] = prev_data[pointer]
            pointer = (pointer + 1) % len(prev_data)
        self._front = 0

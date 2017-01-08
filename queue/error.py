""" Error module """

class Error(Exception):
    """ Base class for module """
    pass

class EmptyError(Error):
    """ Raise error if empty """

    def __init__(self, msg):
        self.msg = msg

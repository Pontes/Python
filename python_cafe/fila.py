from node import Node

class Fila:

    def __init__(self):
        self._size = 0
        self.first = None
        self.last = None

    def push(self, elem):
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._size = self._size + 1


    def pop(self):
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            self._size = self._size - 1
            return ('Elemento removido: {}'.format(elem))
        raise IndexError("*** A Fila está vazia! *** ")

    def peek(self):
        if self._size > 0:
            elem = self.first.data
            return elem
        raise IndexError("*** A Fila está vazia! *** ")

    def __len__(self):
        return self._size

    def __repr__(self):
        if self._size > 0:
            x = ""
            pointer = self.first
            while pointer:
                x = x + str(pointer.data) + "->"
                pointer = pointer.next
            return x
        raise "*** Fila está vazia! **"

    def __str__(self):
        return self.__repr__()


from node import Node
class Queue:

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

        self._size += 1

    def pop(self):
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            self._size -= 1
            return elem
        raise IndexError('*** THE QUEUE IS EMPTY! ***')

    def peek(self):
        if self._size > 0:
            return self.first.data
        raise IndexError('*** THE QUEUE IS EMPTY! ***')

    def __len__(self):
        return self._size

    def __repr__(self):
        if self._size > 0:
            x = ""
            pointer = self.first
            while pointer:
                x = x + str(pointer.data) + " "
                return x
        raise IndexError('*** THE QUEUE IS EMPTY! ***')

    def __str__(self):
        return self.__repr__()
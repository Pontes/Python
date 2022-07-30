from node import Node

class Fila2:

    def __init__(self):
        self._size = 0
        self.primeiro = None
        self.ultimo = None

    def inserir(self, elem):
        node = Node(elem)
        if self.ultimo is None:
            self.ultimo = node
        else:
            self.ultimo.next = node
            self.ultimo = node

        if self.primeiro is None:
            self.primeiro = node

        self._size = self._size + 1

    def remover(self):
        if self._size > 0:
            elem = self.primeiro.data
            self.primeiro = self.primeiro.next
            self._size = self._size - 1
            return "Removido: {}".format(elem)
        raise IndexError("*** Queue is empty! ***")

    def mostrar(self):
        if self._size > 0:
            elem = self.primeiro.data
            return elem
        raise IndexError("*** Queue is empty! ***")

    def __len__(self):
        return self._size

    def __repr__(self):
        if self._size > 0:
            x = ""
            ponteiro = self.primeiro
            while ponteiro:
                x = x + str(ponteiro.data) + " "
                ponteiro = ponteiro.next
            return x
        raise IndexError("*** Queue is empty! ***")

    def __str__(self):
        return self.__repr__()



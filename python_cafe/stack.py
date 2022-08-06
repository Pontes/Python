from node import Node
"""
inserir na pilha
remover da pilha
observar o topo da pilha
"""
class Stack:

    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        #insere um elemento na pilha
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    def pop(self):
        # remover o elemento do topo da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.data
        raise IndexError("*** A pilha está vazia! ***")

    def peek(self):
        #retorna o topo da pilha sem remover
        if self._size > 0:
            return self.top.data
        raise IndexError("*** A pilha está vazia! ***")

    def __len__(self):
        return self._size

    def __repr__(self):
        r = ""
        pointer = self.top
        while pointer:
            r = +r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()
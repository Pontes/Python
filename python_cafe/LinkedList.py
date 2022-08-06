from node import Node

class LinkedList:

    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            # inserção quando a lista já possui elementos
            pointer = self.head
            # print("Pointer Recebendo head {}".format(self.head))
            while(pointer.next):
                pointer = pointer.next
                # print("proximo pointer: {}".format(pointer))
            pointer.next = Node(elem)
            # print("Pointer.next recebendo node: {}".format(pointer.next))
        else:
            # primeira inserção
            self.head = Node(elem)
            # print("primeir Inserção: {}".format(self.head))

        self._size = self._size+1
        # print("Tamanho {}".format(self._size))

    def __len__(self):
        """Retorna o tamanho da lista"""
        # print("recebendo tamanho da lista: {} ".format(self._size))
        return self._size

    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range!")
        return pointer

    def set(self, index, elem):
        pass

    def __getitem__(self, index):

        pointer = self._getnode(index)
        if pointer:
            # print("Retornando dado do pointer {}".format(pointer.data))
            return pointer.data
        else:
            raise IndexError("List index out of range!")


    def __setitem__(self, index, elem):
        # lista[5] =9
        # lista.set(5,9)
        pointer = self._getnode(index)

        if pointer:
            pointer.data = elem
        else:
            raise IndexError("List index out of range!")


    def index(self,elem):
        """ Retorna o índice do elemento na lista"""
        pointer = self.head
        # print("Buscando indice do elemento: {}".format(pointer))
        i = 0
        while pointer:
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1

        raise ValueError("{} is not in list". format(elem))

    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size +1

    def remove(self, elem):
        if self.head == None:
            raise ValueError("{} is not in list". format(elem))
        elif self.head.data == elem:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self._size = self._size - 1
                    return True
                ancestor = pointer
                pointer = pointer.next
        raise ValueError("{} is not in list". format(elem))

    def __repr__(self):
        r = ""
        pointer = self.head
        while pointer:
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()



if __name__ == '__main__':
        lista = LinkedList()
        lista.append(7)
        lista.append(80)
        lista.append(56)
        lista.append(32)

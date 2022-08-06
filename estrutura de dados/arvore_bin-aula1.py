class arvore():
    def __init__(self,val=None):
        if val != None:
            self.val = val
        else:
            self.val = None
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = arvore(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = arvore(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

    def imprimirValor(self):
        if self.left:
            self.left.imprimirValor()
        print(self.val)
        if self.right:
            self.right.imprimirValor()


t = arvore(20)
t.left = arvore(18)
t.right = arvore(22)
t.insert(19)
t.insert(21)
t.insert(24)
t.insert(5)
t.insert(2)
t.insert(7)
t.imprimirValor()



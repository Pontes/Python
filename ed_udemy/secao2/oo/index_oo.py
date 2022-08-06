
class Triangulo:
    def __init__(self, lado1, lado2, lado3, base, altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def tipo(self):
        if self.lado1>self.lado2 + self.lado3:
            return "Não é um triangulo"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado1 == self.lado2:
            return "triangulo isósceles"
        else:
            return "outro tipo de triângulo"


t1 = Triangulo(2,1,3,4,3)

print(t1.lado1)
print(t1.lado2)
print(t1.lado3)

print("-"*50)

t2 = Triangulo(8,8,8,16,9)

print(t2.lado1)
print(t2.lado2)
print(t2.lado3)
print(t2.base)
print(t2.altura)
print("-"*50)
print(t2.area())
print(t2.tipo())

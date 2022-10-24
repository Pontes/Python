
class Retangulo:
    def __init__(self,base, altura):
        self.base = base
        self.altura = altura

    def alterarValor(self):
        if self.base < 0:
            self.base = abs(self.base)
        
        if self.altura < 0 :
            self.altura = abs(self.altura)   
    
    def calcularArea(self):
        self.alterarValor()
        return self.base * self.altura

    def calcularPerimetro(self):
        return 2 * (self.base + self.altura)
    
    def retornarValorLados(self):
        print(f'Base: {self.base} \nAltura: {self.altura}')



def main():
    lado1 = int(input("informe o lado A:"))
    lado2 = int(input("informe o lado B:"))

    R1 = Retangulo(lado1, lado2)
    area = R1.calcularArea()
    print("A quantidade de azuleijos é: " + str(area/2))

    p = R1.calcularPerimetro()
    print(f"Perimetro: {p}")

    print()
    R1.retornarValorLados()
    print()
    
    
main()
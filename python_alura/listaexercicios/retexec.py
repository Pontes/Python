from retangulo import Retangulo

print("=================================================")
print("***        Iniciando o programa Retângulo     ***")
print("=================================================")
base = int(input("Digite o valor da base: "))
altura = int(input("Digite o valor da Altura: "))

ret = Retangulo(base, altura)

print("Area do retangulo: ", ret.calcularArea())
print("Perimetro do Retangulo: ", ret.calcularPerimetro())



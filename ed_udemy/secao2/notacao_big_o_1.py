# levando em consideração que n é 10
# esse função executa 11 passos em sua operação
# então éssa função é O(11)

def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i

    return soma

# Essa função executa apenas 3 passos
#  então ésse função é O(3)

def soma2(n):
    return (n * (n + 1)) / 2




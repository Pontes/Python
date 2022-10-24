def palind(texto):
    start = 0
    size = len(texto)-1

    if start == size:
        return True
    elif start != size:
        return False
    else:
        return palid(texto)


# def palindromo(str, comeco, fim):
#     # Primeiro caso base
#     if comeco == fim:
#         return True
#     # Segundo caso base
#     elif str[comeco] != str[fim]:
#         return False
#     else:
#     # Passo em direção ao fim do problema
#       return palindromo(str, comeco + 1, fim - 1)


nome = "rotor"
print("O nome", nome, "eh palindromo?", palind(nome)
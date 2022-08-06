def reverter(texto):
    tam = len(texto)
    if tam == 1 :
        return texto
    else:
        return reverter(texto[1:]) + texto[0]

print(reverter("azafrao"))
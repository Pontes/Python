
with open('frases.txt') as texto:
    # for linha in texto:
    #     print(linha)

    r = texto.readlines()
    print(r)

with open('texto2.txt','w') as texto:
    texto.write('Ola a todos')
#leitura de arquivos

arquivo = open("palavras.txt", "r")
# para ler o arquivo arquivo.read()
linha = arquivo.readline()
type(linha)
print(linha)
print("=====================================")

# aqui lendo o arquivo linha por linha
for linha in arquivo:
    print(linha)

print("=====================================")
arquivo.close()
print("imprimindo  segundo for")

arquivo = open("palavras.txt", "r")

# aqui lendo o arquivo linha por linha e retirando a linha vazia
for linha in arquivo:
    print(linha.strip())

arquivo.close()
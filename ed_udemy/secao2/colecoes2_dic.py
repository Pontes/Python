#######################
## Dicionários

coleta = {'Aedes aegyt': 32, 'Aedes albopictus': 22, 'anopheles darlingi': 14}
print(coleta['Aedes aegyt'])
coleta['Rhodnius montenegrensis ']  = 11
print(coleta)

# apagar um elemento
del(coleta)['Aedes albopictus']
print(coleta)

#exibir o dicionário completo
print(coleta.items())
## o comando abaixo retornas somentes as chaves
print(coleta.keys())
## o comando abaixo retorna somente os valores
print(coleta.values())

coleta2 = {'Anopheles gambie': 13, 'Anopheles deaneorum': 14 }
print(coleta2)
## update server para concatenar dicionários
coleta.update(coleta2)
print(coleta)

## percorrer um dicionário
for especies, num_especies in coleta.items():
    print(f'Espécies: {especies}, números de espécimes coletados: {num_especies}')




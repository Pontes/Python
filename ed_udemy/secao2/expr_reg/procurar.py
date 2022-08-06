import re

# fraseTel = "Olá, meu número de telefone é (21)9999-9999"
# x1 = re.search('\(\d{2}\)\d{4,5}-\d{4}',fraseTel)
# ### search busca a primeira ocorrencia no texto

# frasePlacaCarro = "A placa do carro que eu anotei durante o acidente foi FRT-1998"
# x2 = re.search('[A-Za-z]{3}-\d{4}',frasePlacaCarro)

# fraseEmail = "Entre em contato, meu email é teste@teste.com"
# x3 = re.search('\w+@\w+\.com', fraseEmail)

# print(f'telefone: {x1}')
# print(f'placa do carro: {x2}')
# print(f'email: {x3}')

# ### a função match verificar se encontra a ocorrencia no inicio do texto
# y1 = re.match('\(\d{2}\)\d{4,5}-\d{4}',fraseTel)
# print(f'telefone no inicio: {y1}')

# fraseTel2 = "(21)9999-9999 meu número de telefone "
# y1_1 = re.match('\(\d{2}\)\d{4,5}-\d{4}',fraseTel2)
# print(f'telefone: {y1_1}')

# print("*"*20)
# print("Função findall")
# ## findall encontra várias ocorrencias
# fraseTel3 = "(21)9999-9999 meu número de telefone e o segundo (11)12347-9858 "
# z1 = re.findall('\(\d{2}\)\d{4,5}-\d{4}',fraseTel3)
# print(f'telefone: {z1}')

## criando teste  com findall

texto = " vamos ver o que ele apresenta de contagem no em um texto um pouco maior teste@gmail.com, lLorem ipsum dolor sit amet, consectetur adipiscing elit. Duis iaculis ullamcorper aliquam. Quisque faucibus nisi et tincidunt viverra. Aenean eu commodo turpis. Nullam nec pretium justo, a pretium nisi. Etiam quis molestie nibh. Proin ultricies placerat fringilla. Sed elementum, lacus vitae porttitor facilisis, lectus metus euismod dolor, vel efficitur nisl leo et mauris. Duis suscipit teste122@gmail.com.br diam nec lorem efficitur, ullamcorper tristique mauris bibendum. Aenean tristique facilisis elit sed ultricies. Suspendisse nec ipsum orci. Praesent nulla quam, ornare sit amet mauris vestibulum, dignissim pellentesque libero. Nulla facilisi. Vivamus sodales eget tellus blandit cursus. Mauris in eros a nunc placerat tempus. Mauris maximus, turpis at molestie finibus, augue  teste@gmail.com.zy tellus ultrices metus, id ullamcorper magna erat tincidunt teste@gmail.com ligula. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur placerat turpis eget tellus lacinia, a tincidunt nisl pharetra. Proin neque metus, aliquet eget lacus nec, mollis facilisis libero. Quisque dictum augue eu diam malesuada, maximus volutpat lacus porta. Morbi teste123@gmail.com.br nec malesuada est, quis varius massa. Integer sit amet rutrum eros."
emailInter = re.findall('\w+@\w+\.\w*', texto)
emailNac = re.findall('\w+@\w+\.\w+\.*\w*', texto)
print(f'emails: {emailNac}')



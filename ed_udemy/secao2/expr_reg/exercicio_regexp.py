import re

texto = " rua ivone dos santos cardoso, 26, cep 24913-000, site http://pontesti.com.br, https://pontesti.net"

numero = re.findall('\d{1,8}', texto)
cep = re.findall('\d{5}-\d{3}', texto)
url = re.findall('https?\://[a-zA-Z0-9./]+', texto)

print(f'Numero: {numero}, CEP: {cep}, site:{url}')
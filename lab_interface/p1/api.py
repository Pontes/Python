"""! @Arquivo API"""

##
# Tem por finalidade  fazer a conexão e retornar os dados do rastreio dos correios
# Nesse arquivo tem importado as bibliotecas request, beautifilsoup, constants e beautifultable

import requests # biblioteca que traz funcionalidades do protocolo http
from bs4 import BeautifulSoup # biblioteca para extrair dados de arquivos HTML e XML
import constants #biblioteca com a url para conexão de rastreio
from beautifultable import BeautifulTable #biblioteca que permite imprimir dados em forma de tabelas para o terminal

def consultaCorreios(codigo):
    """! @Função consultaCorreios """
    ##
    #    Função consultaCorreios, uma função que recebe o código de rastreio, faz a conexão com a url e trata os dados
    #    recebido e retorna as informações em dados tabulares
    #    :param codigo: código de rastreio que é um string passada via terminal pelo usuário
    #    :return: retorna vazio, pois os dados já são impressos pela função

    dadosCorreios = requests.get(constants.urlPrincipal() + codigo) #Variavel que recebe a url e o código de rastreio e faz a conexão

    htmlCorreios = BeautifulSoup(dadosCorreios.text, 'html.parser') #Dados recebidos da conexão tratados pela lib BeautifulSoap e convertidos em texto
    """! @BeautifulSoup - Tratamento dos dados do site """

    ##
    # Início do tratamento e busca dos dados em uma parte específica do site na qual foi passada a url

    showCorreios = htmlCorreios.find('div', attrs={'class':'card-header'})
    objeto = showCorreios.find('div', attrs={'class': 'main_title_3'}).text
    statusObjeto = showCorreios.find('ul', attrs={'class': 'linha_status m-0'})
    itemsObjeto1 = statusObjeto.find_all('li')

    lista = []
    lista.append(objeto.strip())
    for x in itemsObjeto1:
        lista.append(x.text)

    tabela = BeautifulTable() # Uso da biblioteca BeautifulTable para formar a saída dos dados de forma tabulares
    tabela.rows.append([lista[0],lista[1],lista[2],lista[3]])
    tabela.columns.header = ["Ultimo Status", "status", "data", "local"]
    print(tabela) #impressão dos dados tabulares para o usuário na tela do terminal
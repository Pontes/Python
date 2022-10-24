"""! @arquivo APP.PY """
##
# Arquivo principal do programa de rastreio dos correios feito em python
# nesse arquivo principal importamos a API que fará a conexão e o tratamento dos dados

import api

def main():
    """! @Função principal do programa """

    ##
    # @função main()
    # nessa função é solicitado ao usuário a inserção do código de rastreio.
    # Logo em seguida e chamada a função consultaCorreios para fazer a conexão
    # trazer as informações do rastreio

    codigoRast = input("Entre com o codigo de rastreio: ")
    api.consultaCorreios(codigoRast)

main()
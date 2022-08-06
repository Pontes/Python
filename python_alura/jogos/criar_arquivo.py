# funão para abrir arquivo função nativa do python built-in
# w -  para escrita (write)
# R - para leitura (read)
# a - para adicionar conteúdo (append)
arquivo = open("palavras.txt","w")

#escrevendo no arquivo
arquivo.write("banana\n")
arquivo.write("morango\n")
arquivo.write("melancia\n")
# fechando o arquivo
arquivo.close()

arquivo = open("palavras.txt", "a")
arquivo.write("abacate\n")
arquivo.write("maça\n")
arquivo.write("abacaxi\n")

arquivo.close()


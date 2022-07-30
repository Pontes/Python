classe  não :
    def  __init__ ( self , data ):
        eu . dados  =  dados
        eu . setaFilhos ( nenhum , nenhum )

    def  setaFilhos ( self , esquerda , direita ):
        eu . esquerda  =  esquerda
        eu . direita  =  direita

    def  balanco ( self ):
        prof_esq  =  0
        se  eu . esquerda :
            prof_esq  =  self . esquerda . profundidade ()
        prof_dir  =  0
        se  eu . direita :
            prof_dir  =  self . direita . profundidade ()
        return  prof_esq  -  prof_dir

    def  profundidade ( self ):
        prof_esq  =  0
        se  eu . esquerda :
            prof_esq  =  self . esquerda . profundidade ()
        prof_dir  =  0
        se  eu . direita :
            prof_dir  =  self . direita . profundidade ()
        retornar  1  +  max ( prof_esq , prof_dir )

    def  rotacaoEsquerda ( self ):
        eu . dados , self . direita . dados  =  self . direita . dados , self . dados
        old_esquerda  =  self . esquerda
        eu . setaFilhos ( auto . direita , auto . direita . direita )
        eu . esquerda . setaFilhos ( old_esquerda , self . esquerda . esquerda )

    def  rotacaoDireita ( self ):
        eu . dados , self . esquerda . dados  =  self . esquerda . dados , self . dados
        old_direita  =  self . direita
        eu . setaFilhos ( self . esquerda . esquerda , self . esquerda )
        eu . direita . setaFilhos ( auto . direita . direita , old_direita )

    def  rotacaoEsquerdaDireita ( self ):
        eu . esquerda . rotacaoEsquerda ()
        eu . rotacaoDireita ()

    def  rotacaoDireitaEsquerda ( self ):
        eu . direita . rotacaoDireita ()
        eu . rotacaoEsquerda ()

    def  executaBalanco ( self ):
        bal  =  self . balanco ()
        se  bal  >  1 :
            se  eu . esquerda . balanco () >  0 :
                eu . rotacaoDireita ()
            mais :
                eu . rotacaoEsquerdaDireita ()
        elif  bal  <  - 1 :
            se  eu . direita . balanco () <  0 :
                eu . rotacaoEsquerda ()
            mais :
                eu . rotacaoDireitaEsquerda ()

    def  insere ( self , data ):
        se  dados  <=  self . dados :
            se  não  for eu . esquerda :
                eu . esquerda  =  Não ( dados )
            mais :
                eu . esquerda . dentro ( dados )
        mais :
            se  não  for eu . direita :
                eu . direita  =  Não ( dados )
            mais :
                eu . direita . dentro ( dados )
        eu . executaBalanco ()

    def  imprimeArvore ( self , indent  =  0 ):
        imprimir  ""  *  travessão  +  str ( auto . de dados )
        se  eu . esquerda :
            eu . esquerda . imprimeArvore ( recuo  +  2 )
        se  eu . direita :
            eu . direita . imprimeArvore ( recuo  +  2 )
from time import time
import turtle

def drawBar(t, altura):
    """Faça a  tartaruga t desenhar uma barra, de altura `altura`."""

    t.begin_fill()  # comece preenchendo o perfil
    t.left(90)
    t.forward(altura)
    t.write(' ' + str(altura+5))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(altura)
    t.left(90)
    t.end_fill()    #pare de preencher o perfil

xs = [50,55,45,35,25,68,75] # aqui vão os dados
alturamax = max(xs)
numbarras = len(xs)
moldura = 20

tess  = turtle.Turtle() #cria a tess e inicializa alguns de seus atributos
tess.color = ("red")
tess.fillcolor("white")
tess.pensize(3)

wn = turtle.Screen()    # inicializa a janela e seus atributos
wn.bgcolor("lightgreen")
wn.setworldcoordinates(0-moldura, 0-moldura, 40*numbarras+moldura, alturamax+moldura)

for a in xs:
    drawBar(tess, a)

wn.exitonclick()

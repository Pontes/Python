import turtle

def drawSquareMultColor(t, tam):
    """Faça a tartaruga t desenhar um quadrado multicolorido de lado tam."""

    for i in ['red', 'purple', 'hotpink', 'blue']:
        t.color(i)
        t.forward(tam)
        t.right(90)


wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(3)

tamanho = 20

for i in range(15):
    drawSquareMultColor(tess, tamanho)
    tamanho = tamanho +10
    tess.forward(10)
    tess.left(18)

wn.exitonclick()
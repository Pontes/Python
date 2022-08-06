import turtle

def drawSquare(t, tamanho):

    for i in range(4):
        t.forward(tamanho)
        t.left(90)
    

def nextSquare(qtd):

    tess = turtle.Turtle()

    for i in range(1,qtd+1):
        drawSquare(tess,100)
        tess.left(18)


wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.screensize(500,500)
nextSquare(20)

wn.exitonclick()

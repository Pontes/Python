import turtle

def drawSquare(t, tam):
    """Faça a tartaruga t desenha um quadrado de lado tam."""

    for i in range(4):
        t.forward(tam)
        t.left(90)

wn = turtle.Screen()  #inicializa a janela e seus atributos
wn.bgcolor("lightgreen")

alex = turtle.Turtle() #cria alex
drawSquare(alex, 50) #chama a função drawSquare para desenhar um quadrado

alex.penup()
alex.goto(100,10)
alex.pendown()

drawSquare(alex,100)

alex.penup()
alex.goto(100,0)
alex.pendown()

drawSquare(alex,100)

wn.exitonclick()
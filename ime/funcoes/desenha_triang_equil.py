import turtle

def trianguloEquilatero(t,tamanho):

    for i in range(3):
        t.forward(tamanho)
        t.left(120)

wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.screensize(500,300)

tess = turtle.Turtle()
trianguloEquilatero(tess,150)

wn.exitonclick()
        
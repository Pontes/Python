import turtle

def espiral(t,volta, angulo,tamanho):
    tam = tamanho
    for i in range(volta):
        t.forward(tam)
        t.right(angulo)
        tam = tam + tamanho

wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.screensize(1000,1000)

tess = turtle.Turtle()
espiral(tess,80,90, 4)
tess.penup()
tess.goto(450,0)
tess.pendown()
espiral(tess, 80,88,4)


wn.exitonclick()

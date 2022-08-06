import turtle

def poli(t, numeroLados, tamanho):
    
    for i in range(numeroLados):
        t.forward(tamanho)
        t.left(45)


wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.screensize(500,300)

tess = turtle.Turtle()
poli(tess,8,50)


wn.exitonclick()
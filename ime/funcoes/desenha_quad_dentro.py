import turtle

def drawSquare(t, tamanho):

    for i in range(4):
        t.forward(tamanho)
        t.left(90)
    

def proximoSquare(x):
    marley = turtle.Turtle()
    
    for i in range(1,x+1):
        marley.pendown()
        drawSquare(marley, 20*i*2)
        marley.penup()
        marley.left(225)
        marley.goto(-20*i,-20*i)
        marley.left(135)
        
        
#quadrados = int(input("Digite o numero de quadrados: "))

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.screensize(500,300)

proximoSquare(5)

wn.exitonclick()

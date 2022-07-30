import turtle

def drawSquare(t, tamanho):

    for i in range(4):
        t.forward(tamanho)
        t.left(90)

def proximoSquare(x):
    marley = turtle.Turtle()
    
    for i in range(1,x+1):
        marley.pendown()
        drawSquare(marley, 20)
        marley.penup()
        marley.goto(40*i,0)
        
quadrados = int(input("Digite o numero de quadrados: "))

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.screensize(500,300)

proximoSquare(quadrados)




    


wn.exitonclick()

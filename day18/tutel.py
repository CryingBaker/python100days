from turtle import Turtle,Screen

def drawshape(innerangle,i):
    for _ in range(i):
        tutel.forward(100)
        tutel.left(180-innerangle)

tutel = Turtle()

tutel.shape("turtle")
tutel.color("green")

angle = 180

for i in range(3,200):
    innerangle = angle/i
    drawshape(innerangle,i)
    angle += 180 

screen = Screen()
screen.exitonclick()
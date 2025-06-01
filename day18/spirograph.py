import turtle as t
import random

vedal = t.Turtle()
t.colormode(255)

vedal.speed("fastest")

def generatecolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def drawspirograph(gap):
    angle = 0
    for i in range(int(360/gap)):
        vedal.color(generatecolor())
        vedal.circle(100)
        angle+=gap
        vedal.setheading(angle)


drawspirograph(4)
screen = t.Screen()
screen.exitonclick()
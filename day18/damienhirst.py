import colorgram
import random
import turtle as ttl

tutel = ttl.Turtle()
ttl.colormode(255)
tutel.pensize(20)
tutel.hideturtle()

colors = colorgram.extract("image.jpg",20)

def getcolor():
    color = random.choice(colors)
    rgb = color.rgb
    return (rgb[0],rgb[1],rgb[2])

def drawlikedh(x,y):
    tutel.penup()
    tutel.left(225)
    tutel.forward(200)
    tutel.setheading(0)
    tutel.pendown()
    for i in range(1,x+1):
        for _ in range(y):
            tutel.color(getcolor())
            tutel.forward(0)
            tutel.penup()
            tutel.forward(50)
            tutel.pendown()
        tutel.penup()
        tutel.backward(50*x)
        tutel.left(90)
        tutel.forward(50)
        tutel.right(90)
        tutel.pendown()

drawlikedh(10,10)

screen = ttl.Screen()
screen.exitonclick()

import turtle as t
import random

t.colormode(255)
tutel = t.Turtle()

directions = [0,90,180,270]

def change_direction(tutel,angle):
    currentangle = tutel.heading()
    difference = angle - currentangle
    tutel.left(difference)

def generatecolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

tutel.pensize(10)
tutel.speed(0)

for _ in range(1000):
    tutel.color(generatecolor())
    new_direction = random.choice(directions)
    change_direction(tutel,new_direction)
    tutel.forward(15)

screen = t.Screen()
screen.exitonclick()
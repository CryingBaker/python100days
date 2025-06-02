import turtle as ttl

tutel = ttl.Turtle()
screen = ttl.Screen()

def moveforward():
    tutel.forward(20)

def movebackward():
    tutel.backward(20)

def movecounterclockwise():
    tutel.setheading(tutel.heading()+10)

def moveclockwise():
    tutel.setheading(tutel.heading()-10)

def clear():
    tutel.clear()
    tutel.penup()
    tutel.home()
    tutel.pendown()

screen.listen()
screen.onkey(key="w",fun=moveforward)
screen.onkey(key="s",fun=movebackward)
screen.onkey(key="a",fun=movecounterclockwise)
screen.onkey(key="d",fun=moveclockwise)
screen.onkey(key="c",fun=clear)
screen.exitonclick()
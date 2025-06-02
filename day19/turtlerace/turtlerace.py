import turtle
from turtle import Screen,Turtle
import tkinter as TK
import random

STARTINGPOSX = -300
STARTINGPOSY = -100
WINPOSITION = 600
colors = ["green","blue","red","orange","yellow","brown","black","purple"]

def create_turtles(x):
    turtles = []
    turtle_colors = []
    turtle_position = []
    for _ in range(x):
        newturtle = Turtle()
        newturtle.shape("turtle")
        color = random.choice(colors)
        turtle_colors.append(color)
        colors.remove(color)
        newturtle.color = newturtle.color(color)
        newturtle.penup()
        newturtle.speed("fastest")
        turtles.append(newturtle)
        turtle_position.append(0)
    return turtles,turtle_colors,turtle_position

def position_turtles(turtles):
    posx = STARTINGPOSX
    posy = STARTINGPOSY
    for turtle in turtles:
        turtle.goto(posx,posy)
        posy+=50

def turtle_moves(turtles,turtle_position):
    for i in range(len(turtles)):
        winner = check_turtle_won(turtle_position)
        if winner:
            winner_color = turtles[winner].pencolor()
            return winner_color, turtle_position
        distance = random.randint(1,7)
        turtles[i].forward(distance)
        turtle_position[i]+= distance
    return None, turtle_position

def check_turtle_won(turtle_position):
    for i in range(len(turtle_position)):
        if turtle_position[i]>WINPOSITION:
            return i
        
def returncolors(turtle_colors):
    statement = ""
    for color in turtle_colors:
        statement+=color
        statement+="/"
    return statement

def game():
    turtles,turtle_colors,turtle_position = create_turtles(5)
    turtle_won = ""
    position_turtles(turtles)
    user_bet = turtle.textinput("Make your bet",f"Which turtle do you think will win? ({returncolors(turtle_colors)}): ")
    while not turtle_won:
        turtle_won,turtle_position = turtle_moves(turtles,turtle_position)
    if user_bet == turtle_won:
        TK.messagebox.showinfo("Result",f"{turtle_won} won the game. You won the bet")
    else:
        TK.messagebox.showinfo("Result",f"{turtle_won} won the game. You lost the bet")
    
game()

screen = Screen()
screen.exitonclick()
from turtle import Screen
from player import Player
from boundary import Boundary
from ball import Ball
from score import Score

screen = Screen()
boundary = Boundary(screen)
player1 = Player(1,screen)
player2 = Player(2,screen)
score1 = Score(1)
score2 = Score(2)
ball = Ball(player1,player2,score1,score2)
screen.screensize(canvheight=600,canvwidth=600)
screen.bgcolor("black")
# screen.tracer(0)
screen.listen()
screen.onkey(key = "w",fun = player1.moveup)
screen.onkey(key = "s",fun = player1.movedown)
screen.onkey(key = "Up",fun = player2.moveup)
screen.onkey(key = "Down",fun = player2.movedown)
ball.moveball()
screen.exitonclick()



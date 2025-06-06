import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard(screen)
player = Player(screen,scoreboard)
cars = CarManager(screen,player,scoreboard)
screen.listen()
while True:
    cars.movecars()
    screen.onkey(key = "Up",fun = player.move)
    screen.exitonclick()

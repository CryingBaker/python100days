import time
import turtle as ttl
from snake import Snake
from food import Food
from score import Score

gamenoton = True

with open("highscore.txt","r") as highscore:
    score = Score(int(highscore.read()))

screen = ttl.Screen()

def initgame():
    global gamenoton
    gamenoton = False
    food = Food()
    snake = Snake(screen,food,score)
    return food,snake

def game(food,snake):
    global gamenoton
    snake.create_snake()
    screen.update()
    screen.tracer(0)
    screen.screensize(canvheight=650,canvwidth=650)
    screen.title("Snake Game")
    screen.bgcolor("black")
    screen.listen()
    screen.onkey(key = "space", fun = snake.start_movement)
    screen.onkey(key = "w",fun = snake.move_snake_upward)
    screen.onkey(key = "a",fun = snake.move_snake_backward)
    screen.onkey(key = "s",fun = snake.move_snake_downward)
    screen.onkey(key = "d",fun = snake.move_snake_forward)
    screen.onkey(key = "q",fun = startgame)

def startgame():
    screen.clear()
    food,snake = initgame()
    game(food,snake)
    screen.exitonclick()

startgame()
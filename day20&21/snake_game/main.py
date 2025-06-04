import time
import turtle as ttl
from snake import Snake
from food import Food
from score import Score

def game():
    screen = ttl.Screen()
    food = Food()
    score = Score()
    snake = Snake(screen,food,score)
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
    screen.exitonclick()

game()
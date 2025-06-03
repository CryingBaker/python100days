import turtle as ttl
import time

SNAKE_WIDTH = 20
STARTINGPOSITIONX = 0
STARTINGPOSITIONY = 0
SNAKESTARTINGSIZE = 3

class Snake:
    def __init__(self,screen):
        self.screen = screen
        self.snake_body = []

    def create_snakepart(self):
        snake_body = ttl.Turtle()
        snake_body.pensize(SNAKE_WIDTH)
        snake_body.shape("square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.speed("slowest")
        return snake_body

    def position_snakepart(self,snake_part,posx,posy):
        snake_part.goto(posx,posy)

    def create_snake(self):
        posx = STARTINGPOSITIONX
        posy = STARTINGPOSITIONY
        for _ in range(SNAKESTARTINGSIZE):
            snake_part = self.create_snakepart()
            self.snake_body.append(snake_part)
            self.position_snakepart(snake_part,posx,posy)
            posx -= SNAKE_WIDTH

    def move_snake_forward(self):
        if self.snake_body[0].heading()!=180:
            self.snake_body[0].setheading(0)
        
    def move_snake_upward(self):
        if self.snake_body[0].heading()!=270:
            self.snake_body[0].setheading(90)

    def move_snake_downward(self):
        if self.snake_body[0].heading()!=90:
            self.snake_body[0].setheading(270)

    def move_snake_backward(self):
        if self.snake_body[0].heading()!=0:
            self.snake_body[0].setheading(180)

    def start_movement(self):
        while True:
            self.snake_body[0].forward(20)
            for snake_part in range(len(self.snake_body)-1):
                self.snake_body[len(self.snake_body) - snake_part - 1].goto(self.snake_body[len(self.snake_body) - snake_part - 2].position())
            self.screen.update()
            time.sleep(0.1)
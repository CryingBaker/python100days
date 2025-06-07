import turtle as ttl
import time
import tkinter as TK

SNAKE_WIDTH = 20
STARTINGPOSITIONX = 0
STARTINGPOSITIONY = 0
SNAKESTARTINGSIZE = 3
DISTANCEERRORALLOWED = 20

class Snake:
    def __init__(self,screen,food,score):
        self.screen = screen
        self.snake_body = []
        self.food = food
        self.score = 0
        self.highscore = 0
        self.scoreturtle = score
        self.scoreturtle.setscore(self.score)
        self.snake_alive = True

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
        while self.snake_alive:
            if not self.snake_alive:
                break
            for snake_part in range(len(self.snake_body)-1):
                self.snake_body[len(self.snake_body) - snake_part - 1].goto(self.snake_body[len(self.snake_body) - snake_part - 2].position())
                self.hitfood(self.food)
            self.snake_body[0].forward(20)
            self.check_dead()    
            self.screen.update()
            time.sleep(0.1)
        
    def hitfood(self,food):
        foodposx = food.xcor()
        foodposy = food.ycor()
        posx = self.snake_body[0].xcor()
        posy = self.snake_body[0].ycor()
        if (foodposx - DISTANCEERRORALLOWED <= posx <= foodposx + DISTANCEERRORALLOWED) and (foodposy - DISTANCEERRORALLOWED <= posy <= foodposy + DISTANCEERRORALLOWED):
            food.generatefood()
            self.snake_body.append(self.create_snakepart())
            self.screen.update()
            self.score += 1
            self.scoreturtle.setscore(self.score)
    
    def showpopup(self):
        TK.messagebox.showinfo("Game Over", f"You scored {self.score}")

    def check_dead(self):
        if (self.snake_body[0].xcor()>290) or (self.snake_body[0].xcor()<-290) or (self.snake_body[0].ycor()>290) or (self.snake_body[0].ycor()<-290):
            self.snake_alive = False
            # self.showpopup()
            self.scoreturtle.game_over()
            return
        for part in range(1,len(self.snake_body)-1):
            if (self.snake_body[0].xcor() == self.snake_body[part].xcor()) and (self.snake_body[0].ycor() == self.snake_body[part].ycor()):
                self.snake_alive = False
                # self.showpopup()
                self.scoreturtle.game_over()
                return
        
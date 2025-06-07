from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.posx = random.randint(-280,281)
        self.posy = random.randint(-280,281)
        self.goto(self.posx,self.posy)

    def generatefood(self):
        posx = random.randint(-280,281)
        posy = random.randint(-280,281)
        while (self.posx - 50 <= posx <= self.posx + 10) or (self.posy - 10 <= posy <= self.posy + 10):
            posx = random.randint(-280,281)
            posy = random.randint(-280,281)
        self.posx = posx
        self.posy = posy
        self.goto(self.posx,self.posy)
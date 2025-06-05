from turtle import Turtle

class Score(Turtle):
    def __init__(self,player):
        super().__init__()
        self.penup()
        self.color("white")
        if player == 1:
            self.goto(-100,300)
        elif player == 2:
            self.goto(100,300)
        self.pendown()
        self.hideturtle()
        self.changescore(0)
    
    def changescore(self,score):
        self.clear()
        self.write(f"{score}",False,"left",("Arial",20))
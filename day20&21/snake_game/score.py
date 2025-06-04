from turtle import Turtle

POSX = 0
POSY = 300

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pensize(50)
        self.color("white")
        self.hideturtle()
        self.goto(POSX,POSY)
        self.speed("fastest")

    def setscore(self,score):
        self.clear()
        self.write(f"Score: {score}",False,"center",("Arial",20))
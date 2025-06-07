from turtle import Turtle

POSX = 0
POSY = 300

class Score(Turtle):
    def __init__(self,highscore):
        super().__init__()
        self.penup()
        self.pensize(50)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(POSX,POSY)
        self.speed("fastest")
        self.highscore = highscore

    def setscore(self,score):
        self.clear()
        self.score = score
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt","w") as file:
                file.write(str(self.highscore))
        self.write(f"Score: {score} High Score: {self.highscore}",False,"center",("Arial",20))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over. Press 'Q' to start again.",False,"center",("Arial",20))
        self.goto(POSX,POSY)

        
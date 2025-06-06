from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        self.level = 1
        self.penup()
        self.goto(-280,250)
        self.hideturtle()
        self.change_level()
    
    def change_level(self):
        self.clear()
        self.write(f"Level: {self.level}",False,"left",FONT)

    def increase_level(self):
        self.level += 1
        self.change_level()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",False,"center",FONT)

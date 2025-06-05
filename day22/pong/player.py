from turtle import Turtle

STARTINGPOSITIONX = 300
STARTINGPOSITIONY = 0

class Player(Turtle):
    def __init__(self,player_no,screen):
        super().__init__()
        self.screen = screen
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=1,stretch_len=3)
        self.score = 0
        if player_no == 1:
            posx = -STARTINGPOSITIONX
            posy = STARTINGPOSITIONY
        elif player_no == 2:
            posx = STARTINGPOSITIONX
            posy = STARTINGPOSITIONY
        self.goto(posx,posy)
        self.left(90)
    
    def moveup(self):
        self.forward(30)

    def movedown(self):
        self.backward(30)
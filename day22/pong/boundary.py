from turtle import Turtle

BOUNDARYLOCATIONX = 0
BOUNDARYSTART = 350
BOUNDARYEND = -350

class Boundary(Turtle):
    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        self.color("white")
        self.pensize(5)
        self.penup()
        self.goto(BOUNDARYLOCATIONX,BOUNDARYSTART)
        self.right(90)
        for _ in range(abs(int((BOUNDARYEND - BOUNDARYSTART)/10))):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
        # self.screen.update()
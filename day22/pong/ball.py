from turtle import Turtle

class Ball(Turtle):
    def __init__(self,player1,player2,score1,score2):
        super().__init__()
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2
        self.playerwon = None
        self.movedirx = 2 #Move right 5
        self.movediry = 3 #Move up 5
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
    
    def moveball(self):
        while self.playerwon == None:
            self.goto(self.xcor()+self.movedirx,self.ycor()+self.movediry)
            self.hitball(self.player1,self.player2)
            self.hitborder()
            self.playerwon = self.moveout()
        if self.playerwon == 1:
            self.player1.score += 1
            self.score1.changescore(self.player1.score)
        elif self.playerwon == 2:
            self.player2.score += 1
            self.score2.changescore(self.player2.score)
        self.reset()

    def hitball(self,player1,player2):
        if (self.distance(player1) < 25) or (self.distance(player2) < 25):
            self.movedirx *= -1

    def hitborder(self):
        if self.ycor() > 300 or self.ycor() < -300:
            self.movediry *= -1
            
    def moveout(self):
        if self.xcor() > 300:
            print("moved out")
            return 1
        elif self.xcor() < - 300:
            print("Moved out")
            return 2
        return None
    
    def reset(self):
        self.goto(0,0)
        self.playerwon = None
        self.moveball()
            
        
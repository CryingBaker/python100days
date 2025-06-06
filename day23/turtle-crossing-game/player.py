from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self,screen,scoreboard):
        super().__init__()
        self.screen = screen
        self.scoreboard = scoreboard
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.screen.update()

    def move(self):
        self.forward(MOVE_DISTANCE)
        if self.ycor() > FINISH_LINE_Y:
            self.reset()
            self.scoreboard.increase_level()
        self.screen.update()

    def reset(self):
        self.goto(STARTING_POSITION)
        self.screen.update()

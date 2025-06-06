from turtle import Turtle
import random
import time
from player import FINISH_LINE_Y

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CARCOUNT = 30

class CarManager:
    def __init__(self,screen,player,scoreboard):
        self.scoreboard = scoreboard
        self.player = player
        self.screen = screen
        self.game_continue = True
        self.move_distance = STARTING_MOVE_DISTANCE
        self.cars = []
        self.car_position = []
        self.generate_cars(CARCOUNT)

    def generate_cars(self,number):
        for _ in range(number):
            car = Turtle()
            posx = random.randint(-300,300)
            posy = random.randrange(-250,250,10)
            while (posx,posy) in self.car_position:
                posx = random.randint(-300,300)
                posy = random.randrange(-230,250,10)
            car.shape("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(1,2)
            car.goto(posx,posy)
            car.setheading(180)
            car.speed("slowest")
            self.cars.append(car)
            self.car_position.append(car.position())
        
    def movecars(self):
        while self.game_continue:
            for anycar in self.cars:
                anycar.forward(self.move_distance)
                self.detect_collision()
                if anycar.xcor() < -300:
                    posx = random.randint(300,900)
                    posy = random.randrange(-250,250,10)
                    anycar.goto(posx,posy)
                time.sleep(0.0005)
                self.increase_level()
                self.screen.onkey(key = "Up",fun = self.player.move)
                self.screen.update()
    
    def detect_collision(self):
        for car in self.cars:
            playerposx = self.player.xcor()
            playerposy = self.player.ycor()
            if (car.xcor() - 20 <=playerposx <= car.xcor() + 20) and (car.ycor() - 10 <=playerposy <= car.ycor() + 10):
                self.scoreboard.game_over()
                self.game_continue = False
                
    def increase_level(self):
        if self.player.ycor() > FINISH_LINE_Y:
            self.move_distance += MOVE_INCREMENT
            
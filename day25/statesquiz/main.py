import turtle as ttl
from turtle import Turtle,Screen
import pandas

FILE = "indian_states.csv"
IMAGE = "india2011.gif"

class StateNamingGame():
    def __init__(self,screen):
        self.state_marker = Turtle()
        self.state_marker.hideturtle()
        self.state_marker.penup()
        self.score = 0
        self.state_data = pandas.read_csv(FILE)
        self.states = self.state_data["state"].to_list()
        for state in range(len(self.states)):
            self.states.append(self.states[0].lower())
            self.states.pop(0)

    def getuserinput(self):
        state_name = ttl.textinput("Name the State","Enter the name of a state")
        # print(type(state_name))
        state_name = state_name.lower()
        if state_name == "i give up":
            self.show_score()
            dictionary = {"States you forgot":self.states}
            diction = pandas.DataFrame(dictionary)
            diction.to_csv("states_to_learn.csv")
        return state_name
    
    def show_score(self):
        self.state_marker.goto(0,275)
        self.state_marker.write(f"Score: {self.score}/{len(self.states)}",False,"center",("Arial",15,"normal"))

    def guess_state(self,user_input):
        if user_input in self.states:
            self.states.remove(user_input)
            posx = int(self.state_data[self.state_data["state"] == user_input]["x"])
            posy = int(self.state_data[self.state_data["state"] == user_input]["y"])
            self.state_marker.goto(posx,posy)
            self.state_marker.pendown()
            self.state_marker.write(f"{user_input.title()}")
            self.state_marker.penup()
            self.score += 1

    def start_game(self):
        while self.score<len(self.states):
            user_input = self.getuserinput()
            self.guess_state(user_input)
        self.show_score()

screen = Screen()
screen.bgpic(IMAGE)
game = StateNamingGame(screen)
game.start_game()
screen.exitonclick()

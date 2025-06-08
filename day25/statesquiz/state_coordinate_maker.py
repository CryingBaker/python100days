from turtle import Turtle,Screen
import turtle as ttl
import pandas

states = Turtle()
screen = Screen()
screen.bgpic("india2011.gif")

state_coordinates = {
    "state":[],"x":[],"y":[]
}

def get_state_name():
    user_input = ttl.textinput("Enter","State Name:")
    return user_input

def get_mouse_coordinates(x,y):
        state_name = get_state_name()
        state_name = state_name.lower()
        posx = x
        posy = y
        state_coordinates["state"].append(state_name)
        state_coordinates["x"].append(x)
        state_coordinates["y"].append(y)
        print(state_coordinates)

screen.onscreenclick(get_mouse_coordinates)

ttl.mainloop()

state_data = pandas.DataFrame(state_coordinates)
state_data.to_csv("indian_states.csv")
# screen.exitonclick()
from gamedata import data
from art import logo,vs
import random

def choose(previous):
    thing = random.choice(data)
    while thing == previous:
        thing = random.choice(data)
    return thing

def evaluate(thing1,thing2):
    lookup = {
        "a" : thing1,
        "b" : thing2,
    }
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_choice == "a":
        other_choice = "b"
    elif user_choice == "b":
        other_choice = "a"
    if lookup[user_choice]["follower_count"]>lookup[other_choice]["follower_count"]:
        return True
    return False

def game():
    score = 0
    lost = False
    thing1 = None
    thing2 = None
    while lost == False:
        print(logo)
        if thing2 != None:
            thing1 = dict(thing2)
        else:
            thing1 = choose(None)
        thing2 = choose(thing1)
        if score>0:
            print(f"You're right! Current score:{score}")
        print(f"Compare A: {thing1['name']}, a {thing1['description']} from {thing1['country']}.")
        print(vs)
        print(f"Compare B: {thing2['name']}, a {thing2['description']} from {thing2['country']}.")
        lost = not evaluate(thing1,thing2)
        print("\n"*100)
        if(lost == False):
            score += 1
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
game()

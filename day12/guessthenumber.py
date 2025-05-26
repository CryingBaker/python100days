import random

logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

HARD_DIFFICULTY = 5
EASY_DIFFICULTY = 10

def choose_number():
    number = random.randint(1,100)
    return number

def eval_guess(guess,number):
    if guess < number:
        print("Too low")
        return "not_correct"
    elif guess > number:
        print("Too high")
        return "not_correct"
    elif guess == number:
        return "correct"

def guess(difficulty,number):
    attempts = HARD_DIFFICULTY
    if difficulty=='easy':
        attempts = EASY_DIFFICULTY
    for i in range(attempts):
        print(f"You have {attempts - i} attempts remaining to guess the number.")
        player_guess = int(input("Make a guess: "))
        evaluation = eval_guess(player_guess,number)
        if evaluation == "correct":
            return evaluation
    return evaluation
    

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = choose_number()
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    evaluation = guess(difficulty,number)
    play_again = ""
    if evaluation == "not_correct":
        play_again = input("You've run out of guesses. Do you want to play again? Type 'yes' or 'no': ").lower()
    elif evaluation == "correct":
        play_again = input(f"You got it! The number was {number}. Do you want to play again? Type 'yes' or 'no': ").lower()
    return play_again

while True:
    play_again = game()
    if play_again == "no":
        break
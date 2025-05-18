import random

print(random.randrange(1,10,3))
gamedecider = random.randint(0,2)
userchoice = input("Enter your play Rock(R), Papers(P) and Scissors(S): ")
print("You chose:")
if userchoice == "R":
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif userchoice == "P":
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif userchoice == "S":
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)
else:
    print("Invalid choice")

print("Computer chose:")
if gamedecider == 0:
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
    if userchoice == "S":
        print("You lose!")
    elif userchoice == "R":
        print("You drew!")
    elif userchoice == "P":
        print("You win!")
elif gamedecider == 1:
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
    if userchoice == "R":
        print("You lose!")
    elif userchoice == "P":
        print("You drew!")
    elif userchoice == "S":
        print("You win!")
elif gamedecider == 2:
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)
    if userchoice == "P":
        print("You lose!")
    elif userchoice == "S":
        print("You drew!")
    elif userchoice == "R":
        print("You win!")
else:
    print("Invalid choice")

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

userchoice = int(input("Enter 0 for Rock, 1 for Paper and 2 for Scissors: "))
compchoice = random.randint(0,2)

if userchoice == 0:
    print(f"You chose:\n{rock}")
elif userchoice == 1:
    print(f"You chose:\n{paper}")
elif userchoice == 2:
    print(f"You chose:\n{scissors}")
else:
    print("You made an invalid choice")

if compchoice == 0:
    print(f"Computer chose:\n{rock}")
elif compchoice == 1:
    print(f"Computer chose:\n{paper}")
elif compchoice == 2:
    print(f"Computer chose:\n{scissors}")
else:
    print("Computer made an invalid choice")

if userchoice == compchoice-1 or userchoice == 2 and compchoice == 0:
    print("You lost")
elif userchoice == compchoice+1 or userchoice == 0 and compchoice == 2:
    print("You won")
elif userchoice == compchoice:
    print("You drew")
else:
    print("Invalid result")
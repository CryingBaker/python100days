import random
from words import word_list
from hangmanimages import stages

word = random.choice(word_list)
guessed = 0
hangman = 6
placeholderlist = []
for i in word:
    placeholderlist.append("_")
placeholder = "".join(placeholderlist)
print(placeholder)
guessedletters=[]

while guessed<len(word) and hangman>0:
    guess = input("Guess a letter: ").lower()
    if guess not in guessedletters:
        guessedletters.append(guess)
    else:
        print(f"You've already guessed {guess}")
        continue
        
    prevguess = guessed
    for i in range(len(word)):
        if word[i] == guess:
            placeholderlist[i] = guess
            guessed += 1

    if prevguess == guessed:
        hangman-=1

    print(stages[hangman])

    placeholder = "".join(placeholderlist)
    print(placeholder)

if guessed == len(word):
    print("You won!")
else:
    print(f"You lost, the word was {word}")
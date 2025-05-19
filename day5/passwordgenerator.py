import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

nr_characters = nr_letters-nr_symbols-nr_numbers

random_password = ""

while nr_letters!=0:
    choice = random.randint(0,2)
    if choice == 0:
        if nr_symbols != 0:
            random_password+=symbols[random.randint(0,len(symbols)-1)]
            nr_symbols-=1
            nr_letters-=1
    elif choice == 1:
        if nr_numbers != 0:
            random_password+=numbers[random.randint(0,len(numbers)-1)]
            nr_numbers-=1
            nr_letters-=1
    elif choice == 2:
        if nr_characters != 0:
            random_password+=letters[random.randint(0,len(letters)-1)]
            nr_characters-=1
            nr_letters-=1

print(random_password)

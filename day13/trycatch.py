try:
    age = int(input("What is your age?"))
except ValueError:
    print("Enter a valid age in numbers.")
    age = int(input("What is your age?"))

if age>18:
    print(f"You can vote at {age}.")
else:
    print(f"You cannot vote at {age}.")
from art import logo

def add(num1,num2):
    """Calculates sum of two numbers"""
    return num1 + num2

def subtract(num1,num2):
    """Calculates difference between two numbers"""
    return num1 - num2

def multiply(num1,num2):
    """Calculates the product of two numbers"""
    return num1 * num2

def divide(num1,num2):
    """Calculates the quotient of two numbers"""
    return num1 / num2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def calculator(operation,num1,num2):
    return f"{num1} {operation} {num2} = {operations[operation](num1,num2)}"

doContinue = ""

while True:
    print(logo)
    print("Welcome to the Calculator")
    num1 = int(input("Enter the first number:\n"))
    num2 = int(input("Enter the second number:\n"))
    operation = input("Enter an operation to perform ('+' for addition, '-' for subtraction, '*' for multiplication, '/' for division):\n")
    print(calculator(operation,num1,num2))
    doContinue = input("Do you want to use the calculator again? Type 'yes' or 'no':").lower()
    if doContinue == "no":
        break
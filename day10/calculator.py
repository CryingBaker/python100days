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
    """Returns a string and a value after calculating the answer in the format string : number1 (operation) number2 = (answer), value: answer"""
    answer = operations[operation](num1,num2)
    return f"{num1} {operation} {num2} = {answer}",answer

doContinue = ""
prevAns = 0

while True:
    print(logo)
    print("Welcome to the Calculator")
    if doContinue != "yes":
        num1 = int(input("Enter the first number:\n"))
    else:
        print(f"Number 1: {num1}")
    num2 = int(input("Enter the second number:\n"))
    operation = input("Enter an operation to perform ('+' for addition, '-' for subtraction, '*' for multiplication, '/' for division):\n")
    output,prevAns = calculator(operation,num1,num2)
    print(output)
    doContinue = input("Do you want to use the calculator again? Type 'yes' to keep the answer or 'y' to continue without storing answer or 'no':").lower()
    if doContinue == "no":
        break
    elif doContinue == "yes":
        num1 = prevAns
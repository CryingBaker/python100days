import random

alphabets = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = [
    '!','#','$','%','&','*','+','-','<','=','>','?','@'
]


def generate_password(no_alphabets,no_numbers,no_symbols):
    password = []
    for _ in range(no_alphabets):
        password.append(random.choice(alphabets))
    for _ in range(no_numbers):
        password.append(random.choice(numbers))
    for _ in range(no_symbols):
        password.append(random.choice(symbols))
    random.shuffle(password)
    return "".join(password)

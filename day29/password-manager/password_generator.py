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
    password = ""
    for _ in range(no_alphabets):
        password += random.choice(alphabets)
    for _ in range(no_numbers):
        password += random.choice(numbers)
    for _ in range(no_symbols):
        password += random.choice(symbols)
    password_list = list(password)
    random.shuffle(password_list)
    return "".join(password_list)

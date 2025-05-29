TURN_OFF_COMMAND = "off"
REPORT_COMMAND = "report"

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coffee_machine_money = 0.0

def generate_report():
    """Generates report for the coffee machine contents"""
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${coffee_machine_money}")

def process_coins(coins_entered):
    """Processes the coins entered by user and returns the monetary value of said coins"""
    money = 0.0
    money += coins_entered["quarter"]*0.25 + coins_entered["dime"]*0.1 + coins_entered["nickel"]*0.05 + coins_entered["penny"]*0.01
    return money

def check_cost(coffee_to_make):
    """Returns the cost of the coffee chosen"""
    return MENU[coffee_to_make]["cost"]

def check_transaction(coffee_to_make,money):
    """Checks if the money entered is enough, returns True and the excess (if any) if it is enough, else returns false"""
    cost = check_cost(coffee_to_make)
    if money >= cost:
        return True, round(money-cost,2)
    return False

def check_enough_resources(coffee_to_make):
    """Checks if there are enough resources to make the coffee"""
    for ingredient in MENU[coffee_to_make]["ingredients"]:
        if resources[ingredient]<MENU[coffee_to_make]["ingredients"][ingredient]:
            return False,ingredient
    return True, None

def make_coffee(coffee_to_make):
    """Makes coffee i.e. decrements resources, increments money"""
    global coffee_machine_money
    for ingredient in MENU[coffee_to_make]["ingredients"]:
        resources[ingredient] -= MENU[coffee_to_make]["ingredients"][ingredient]
    coffee_machine_money += MENU[coffee_to_make]["cost"]
    print(f"Here's your {coffee_to_make}. Enjoy!")

def enter_coins():
    """Gets amount of coins entered by the user"""
    coins_entered = {
                "quarter":0,
                "dime":0,
                "nickel":0,
                "penny":0,
            }
    for cointype in coins_entered:
        coincount = float(input(f"Enter how many {cointype}s? :"))
        coins_entered[cointype]+=coincount
    return coins_entered

def coffee_machine():
    """Complete program for the coffee machine"""
    while True:
        coffee_to_make = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if coffee_to_make == TURN_OFF_COMMAND:
            break
        elif coffee_to_make == REPORT_COMMAND:
            generate_report()
        else:
            enough_resources, ingredient_missing = check_enough_resources(coffee_to_make)
            if not enough_resources:
                print(f"Sorry there is not enough {ingredient_missing}")
                continue
            coins_entered = enter_coins()
            money = process_coins(coins_entered)
            transaction_check,changereturned = check_transaction(coffee_to_make,money)
            if not transaction_check:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Here's ${changereturned} in change.")
                make_coffee(coffee_to_make)

coffee_machine()
            
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneymachine = MoneyMachine()
coffeemachine = CoffeeMaker()
menu = Menu()

def formatmenuitems():
    menu_items = list(menu.get_items())
    menu_items[len(menu_items)-1] = ")"
    items = "".join(menu_items)
    return items

while True:
    user_input = input(f"What would you like? ({formatmenuitems()}: ")
    if user_input == "off":
        break
    elif user_input == "report":
        coffeemachine.report()
        moneymachine.report()
    else:
        coffee_to_make = menu.find_drink(user_input)
        sufficient_resources = coffeemachine.is_resource_sufficient(coffee_to_make)
        if sufficient_resources:
            payment = moneymachine.make_payment(coffee_to_make.cost)
            if payment:
                coffeemachine.make_coffee(coffee_to_make)

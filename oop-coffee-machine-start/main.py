from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

make_coffee = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == "off":
        print("The coffee machine will turn off!")
        break
    elif choice == "report":
        make_coffee.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if make_coffee.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            make_coffee.make_coffee(drink)
            break
            
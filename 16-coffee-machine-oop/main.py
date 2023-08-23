from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    item = input(f"What would you like? {menu.get_items()}: ")

    is_turn_on = True
    if item == 'off':
        is_turn_on = False
    elif item == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(item)
        if money_machine.make_payment(drink.cost):
            if coffee_maker.is_resource_sufficient(drink):
                coffee_maker.make_coffee(drink)
            else:
                break

    if not is_turn_on:
        print("The machine is off for maintenance, sorry.")
        break

# coins: penny 1 cent 0.01, nickel 5 cents 0.05, dime 10 cents, quarter 25 cents 0.25
# print report:  tells how much resources have left when typing report on "what would you lick"
# revisar que los recursos son suficientes
# procesar monedas - pide una cantidad de cada moneda, si no es suficiente, devuelve el dinero y pregunta de nuevo
# si das de mas, devuelve el cambio y la cantidad del precio del cafe se suma
# revisa si la transaccion es exitosa
# prepara cafe

# if coffe_selection == report, should print the report

from coffe_data import MENU, resources


def main():
    while True:
        coffee = input("What would you like? (espresso/latte/cappuccino): ")

        if coffee == 'report':
            print_report()
        else:
            if not is_enough_resources(coffee):
                print("Not enough resources.")
            else:
                payment = get_payment()
                if not is_payment_enough(coffee, payment):
                    print("Incomplete payment. Return money")
                else:
                    coffee_cost = MENU[coffee]['cost']
                    resources["money"] += coffee_cost
                    payment_change(coffee_cost, payment)
                    make_coffe(coffee)


# TODO: 1. Print report of sufficient resources
def print_report() -> None:
    """Prints a report of the resources in the machine"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


# TODO: 2. Check if resources are sufficient when making coffee
def is_enough_resources(coffee_type: str) -> bool:
    """Returns True if there are enough resources to produce the chosen coffee"""
    coffee_ingredients = MENU[coffee_type]["ingredients"]
    for ingredient, quantity in coffee_ingredients.items():
        if resources[ingredient] < quantity:
            return False
    return True


# TODO: 3. Process coins
def get_payment() -> float:
    """Ask how many pennies, nickels, dimes and quarters the user will give the machine
    and returns the total"""
    pennies = int(input("How many pennies?: "))
    nickels = int(input("How many nickels?: "))
    dimes = int(input("How many dimes?: "))
    quarters = int(input("How many quarters?: "))

    total = (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.1) + (quarters * 0.15)

    return total


# TODO: 4 Check if the transaction is successful
def is_payment_enough(coffee: str, payment: float) -> bool:
    """Returns True if the payment is enough for the coffee"""
    if payment >= MENU[coffee]['cost']:
        return True
    return False


def payment_change(coffee_cost: float, payment: float) -> None:
    """If the payment exceeds the cost of the coffee, prints the subtraction"""
    if payment > coffee_cost:
        print(f"Here's your change: ${round(payment - coffee_cost, 2)}")


# TODO: 5 Make coffee
def make_coffe(coffee: str) -> None:
    """Subtracts the ingredients of the coffee from resources
    and prepares the coffee"""
    coffee_ingredients = MENU[coffee]["ingredients"]
    for ingredient, quantity in coffee_ingredients.items():
        resources[ingredient] -= quantity

    print(f"Thanks, Here's your {coffee} :)")


main()



def order():
    """simply returns a user input"""
    return input("What would you like to order? (espresso/latte/cappuccino): ")


def off():
    """Turns the machine off for maintenance(closes the program, resets values)"""
    exit()


def report(water, milk, coffee, money):
    """Prints 4 statements, to display amount of water, milk, coffee, and money"""
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")

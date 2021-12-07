from data import *
from functions import *
program_status = 'cont'
while program_status == 'cont':
    #TODO ask user what they would like (should be repeatable after each drink purchase)
    print('')
    print("☕Welcome to the Coffee Machine Program!☕")
    user_input = order()

    #TODO turn the machine off when given the "off" command
    if user_input == 'off':
        off()

    #TODO print a report on command "report", should show current resource values (water, milk, coffee, money)
    if user_input == 'report':
        report(resources["water"], resources["milk"], resources["coffee"], resources["money"])

    #TODO Check resources against recipe (take user drink and see if there are enough resources for that drink) If there is
    #TODO not enough, say so, and no drink for the user.
    if user_input != 'report':
        for item in MENU[user_input]["ingredients"]:
        #    print(f"Recipe: {MENU[user_input]['ingredients'][item]}")
        #    print(f"Resources left: {resources[item]}")
            if MENU[user_input]['ingredients'][item] > resources[item]:
                print(f"Sorry, we are out of {user_input}")
                make_drink = False
            else:
                make_drink = True

        #TODO process coins. If there are sufficient resources for the desired drink, move on to ask for coins from the user,
        #TODO and calculate the monetary value
        if make_drink == True:
            print("Please insert coins.")
            quarters = float(input("how many quarters?: ")) * 0.25
            dimes = float(input("how many dimes?: ")) * 0.10
            nickles = float(input("how many nickles?: ")) * 0.05
            pennies = float(input("how many pennies?: ")) * 0.01
            value = quarters + dimes + nickles + pennies
            resources['money'] += MENU[user_input]['cost']

            #TODO check if the user gave enough. Refund money if it was not enough. Otherwise add money to machine and offer any
            #TODO change if the user gave too much
            if MENU[user_input]['cost'] > value:
                print(f"${value} is not enough, you have been refunded.")
                make_drink = False
            elif MENU[user_input]['cost'] < value:
                user_change = round(value - MENU[user_input]['cost'], 2)
                print(f"Here is ${user_change} in change.")
                make_drink = True

        #TODO Make da coffee. Deplete the proper resources. Then give user their drink.
        if make_drink == True:
            for item in MENU[user_input]['ingredients']:
                resources[item] -= MENU[user_input]['ingredients'][item]
            print(f"Here is your {user_input} ☕. Enjoy!")




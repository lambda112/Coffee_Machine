from rescource_data import MENU, resources


# Ask the user what flavour they want return flavour type

def get_order():
    coffee_type = input("What would you like? (espresso, latte, cappuccino): ")
    while coffee_type not in MENU.keys():
        coffee_type = input("Enter valid order! (espresso, latte, cappuccino): ")

    coffee_type = MENU[coffee_type]
    return coffee_type


# Allow machine to be turned off with the keyword 'off' 


# Allow user to enter keyword report, which will generate a report that shows current rescource values


# Check if there are enough rescources


# Process coins 


# Check if transaction is successful